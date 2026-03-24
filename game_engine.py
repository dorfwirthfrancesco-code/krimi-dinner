"""
KrimiDinner Game Engine
Handles role assignment, event triggers, clue distribution, win conditions.
"""
import random
import json
from scenarios.dunkelbach import SCENARIO

SCENARIOS = {"dunkelbach": SCENARIO}

def get_scenario(scenario_id):
    return SCENARIOS.get(scenario_id, SCENARIO)

def assign_roles(scenario_id, player_ids, lang="de"):
    """
    Assign roles to players. Returns dict of {player_id: role_data}.
    One player is randomly chosen as murderer.
    """
    scenario = get_scenario(scenario_id)
    n = len(player_ids)

    # Get eligible roles sorted by min_players
    all_roles = scenario["roles"]
    eligible = sorted(
        [(k, v) for k, v in all_roles.items() if v["min_players"] <= n],
        key=lambda x: x[1]["min_players"]
    )

    # Mandatory roles first (min_players == 4), then optional
    mandatory = [r for r in eligible if r[1]["min_players"] == 4]
    optional  = [r for r in eligible if r[1]["min_players"] > 4]

    # Select roles to use
    selected_roles = mandatory[:] + optional[:n - len(mandatory)]
    selected_roles = selected_roles[:n]

    # Shuffle players and assign
    shuffled_players = player_ids[:]
    random.shuffle(shuffled_players)
    random.shuffle(selected_roles)

    # Pick murderer from can_be_murderer roles
    murderer_candidates = [r for r in selected_roles if r[1]["can_be_murderer"]]
    if not murderer_candidates:
        murderer_candidates = selected_roles

    murderer_role_key = random.choice(murderer_candidates)[0]

    # Check for two murderers (8+ players, 20% chance)
    second_murderer_key = None
    if n >= 8 and random.random() < 0.20:
        remaining_candidates = [r for r in murderer_candidates if r[0] != murderer_role_key]
        if remaining_candidates:
            second_murderer_key = random.choice(remaining_candidates)[0]

    # Build assignments
    assignments = {}
    for i, player_id in enumerate(shuffled_players):
        if i >= len(selected_roles):
            break
        role_key, role_data = selected_roles[i]
        is_murderer = (role_key == murderer_role_key)
        is_second_murderer = (role_key == second_murderer_key)

        assignments[player_id] = {
            "role_key": role_key,
            "role_name": role_data["name"][lang],
            "is_murderer": is_murderer or is_second_murderer,
            "is_second_murderer": is_second_murderer,
            "is_wildcard": role_data.get("is_wildcard", False),
        }

    # Assign lover pairs if both roles present
    assignments = _assign_lover_pairs(assignments, shuffled_players)

    # Assign shadow's blackmail targets
    assignments = _assign_shadow_targets(assignments, scenario, lang)

    # Assign stranger's surveillance target
    assignments = _assign_stranger_target(assignments, lang)

    # Assign inspector's feared person (points toward murderer but could be wrong)
    assignments = _assign_inspector_target(assignments, murderer_role_key, selected_roles, lang)

    return assignments

def _assign_lover_pairs(assignments, player_ids):
    """If viktor role exists, assign a secret lover."""
    viktor_id = next((pid for pid, a in assignments.items() if a["role_key"] == "viktor" or a["role_key"] == "lover"), None)
    if not viktor_id:
        return assignments

    # Pick random non-murderer, non-viktor as lover
    candidates = [pid for pid in player_ids
                  if pid != viktor_id
                  and not assignments[pid].get("is_murderer")
                  and not assignments[pid].get("is_wildcard")]
    if candidates:
        lover_id = random.choice(candidates)
        assignments[viktor_id]["secret_lover_id"] = lover_id
        assignments[lover_id]["secret_lover_id"] = viktor_id
        assignments[lover_id]["is_viktors_lover"] = True

    return assignments

def _assign_shadow_targets(assignments, scenario, lang):
    """Shadow gets blackmail info on 3 random players."""
    shadow_id = next((pid for pid, a in assignments.items() if a["role_key"] == "shadow"), None)
    if not shadow_id:
        return assignments

    others = [pid for pid in assignments if pid != shadow_id]
    targets = random.sample(others, min(3, len(others)))

    blackmail_info = []
    for t in targets:
        role_key = assignments[t]["role_key"]
        role_data = scenario["roles"].get(role_key, {})
        secret = role_data.get("secret", {}).get(lang, "Hat ein Geheimnis.")
        blackmail_info.append({
            "target_id": t,
            "target_role": assignments[t]["role_name"],
            "info": secret[:100] + "..."  # Partial secret
        })

    assignments[shadow_id]["blackmail_targets"] = blackmail_info
    return assignments

def _assign_stranger_target(assignments, lang):
    """Stranger's surveillance file targets the murderer (or near-murderer)."""
    stranger_id = next((pid for pid, a in assignments.items() if a["role_key"] == "stranger"), None)
    if not stranger_id:
        return assignments

    murderer_id = next((pid for pid, a in assignments.items() if a.get("is_murderer")), None)
    if murderer_id:
        assignments[stranger_id]["surveillance_target_id"] = murderer_id
        assignments[stranger_id]["surveillance_target_role"] = assignments[murderer_id]["role_name"]

    return assignments

def _assign_inspector_target(assignments, murderer_role_key, selected_roles, lang):
    """Inspector's letter names the murderer — 70% chance correct, 30% wrong."""
    inspector_id = next((pid for pid, a in assignments.items() if a["role_key"] == "detective"), None)
    if not inspector_id:
        return assignments

    if random.random() < 0.70:
        # Letter correctly names murderer
        feared_id = next((pid for pid, a in assignments.items() if a.get("is_murderer")), None)
    else:
        # Letter names a red herring
        candidates = [pid for pid in assignments if pid != inspector_id and not assignments[pid].get("is_murderer")]
        feared_id = random.choice(candidates) if candidates else None

    if feared_id:
        assignments[inspector_id]["barons_feared_person_id"] = feared_id
        assignments[inspector_id]["barons_feared_role"] = assignments[feared_id]["role_name"]

    return assignments

def get_role_card(player_id, assignments, scenario_id, lang="de"):
    """Build the full role card for a player."""
    scenario = get_scenario(scenario_id)
    assignment = assignments[player_id]
    role_key = assignment["role_key"]
    role_data = scenario["roles"][role_key]

    card = {
        "role_name": role_data["name"][lang],
        "intro": role_data["intro"][lang],
        "appearance": role_data["appearance"][lang],
        "secret": role_data["secret"][lang],
        "ability_name": role_data["ability"]["name"][lang],
        "ability_desc": role_data["ability"]["description"][lang],
        "win_condition": role_data["win_condition"][lang],
        "starting_knowledge": role_data["starting_knowledge"][lang],
        "is_murderer": assignment.get("is_murderer", False),
        "is_wildcard": assignment.get("is_wildcard", False),
    }

    # Add murderer-specific info (revealed at minute 10 of phase 1)
    if assignment.get("is_murderer"):
        card["murderer_motive"] = role_data.get("murderer_motive_if_assigned", {}).get(lang, "")
        card["murderer_reveal_delay"] = 600  # 10 minutes in seconds

    # Add lover info
    if assignment.get("secret_lover_id"):
        lover_id = assignment["secret_lover_id"]
        lover_role = assignments.get(lover_id, {}).get("role_name", "?")
        card["secret_lover_role"] = lover_role
        card["is_viktors_lover"] = assignment.get("is_viktors_lover", False)

    # Add shadow blackmail info
    if assignment.get("blackmail_targets"):
        card["blackmail_targets"] = assignment["blackmail_targets"]

    # Add stranger surveillance info
    if assignment.get("surveillance_target_role"):
        card["surveillance_target"] = assignment["surveillance_target_role"]

    # Add inspector letter info
    if assignment.get("barons_feared_role"):
        card["barons_feared_person"] = assignment["barons_feared_role"]

    return card

def get_initial_clues(player_id, assignments, scenario_id, lang="de"):
    """Return the initial clues a player starts with."""
    scenario = get_scenario(scenario_id)
    assignment = assignments[player_id]
    role_key = assignment["role_key"]
    role_data = scenario["roles"][role_key]

    clue_keys = role_data.get("clues_i_hold", [])
    clues = []
    for ck in clue_keys:
        clue_data = scenario["clues"].get(ck)
        if clue_data:
            clues.append({
                "id": ck,
                "name": clue_data["name"][lang],
                "text": clue_data["text"][lang],
            })
    return clues

def check_win_conditions(game_state, assignments, votes, scenario_id):
    """
    Evaluate win conditions after final vote.
    Returns list of winners and the ending type.
    """
    scenario = get_scenario(scenario_id)
    murderer_ids = [pid for pid, a in assignments.items() if a.get("is_murderer")]

    if not murderer_ids:
        return {"ending": "error", "winners": []}

    primary_murderer_id = murderer_ids[0]
    vote_counts = {}
    for v in votes.values():
        vote_counts[v] = vote_counts.get(v, 0) + 1

    if not vote_counts:
        return {"ending": "no_vote", "winners": []}

    most_voted = max(vote_counts, key=vote_counts.get)

    # Shadow win check
    shadow_id = next((pid for pid, a in assignments.items() if a["role_key"] == "shadow"), None)
    if shadow_id and game_state.get("will_stolen"):
        return {
            "ending": "shadow_wins",
            "winners": [shadow_id],
            "murderer_id": primary_murderer_id,
        }

    # Correct murderer caught
    if most_voted == primary_murderer_id:
        winners = [pid for pid, v in votes.items() if v == primary_murderer_id]

        # Perfect solve bonus
        witness_id = next((pid for pid, a in assignments.items() if a["role_key"] == "witness"), None)
        doctor_id  = next((pid for pid, a in assignments.items() if a["role_key"] == "doctor"), None)
        perfect    = (witness_id in winners and doctor_id in winners
                      and game_state.get("witness_vision_correct")
                      and game_state.get("doctor_correct"))

        return {
            "ending": "perfect_solve" if perfect else "murderer_caught",
            "winners": winners,
            "murderer_id": primary_murderer_id,
        }
    else:
        # Murderer escapes
        return {
            "ending": "murderer_escapes",
            "winners": murderer_ids,
            "wrongly_convicted": most_voted,
            "murderer_id": primary_murderer_id,
        }

def get_atmosphere_message(phase, elapsed_minutes, lang="de"):
    """Return atmosphere message for current game state."""
    scenario = SCENARIO
    for msg in scenario.get("atmosphere_messages", []):
        if msg.get("trigger_time_min") and msg.get("phase") == phase:
            if abs(elapsed_minutes - msg["trigger_time_min"]) < 1:
                return msg["text"][lang]
        if msg.get("trigger") == f"phase_{phase}_start" and elapsed_minutes < 1:
            return msg["text"][lang]
    return None

def get_physical_tasks_for_phase(phase, player_ids, assignments, elapsed_minutes, scenario_id):
    """Return physical tasks that should be triggered now."""
    scenario = get_scenario(scenario_id)
    tasks_to_send = []

    for task_id, task in scenario.get("physical_tasks", {}).items():
        if task.get("trigger_phase") != phase:
            continue

        # Determine recipient
        assigned_role = task.get("assigned_to")
        recipient_id = None

        if assigned_role == "all":
            for pid in player_ids:
                tasks_to_send.append({"task": task, "recipient": pid})
            continue
        elif assigned_role == "witness":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "witness"), None)
        elif assigned_role == "doctor":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "doctor"), None)
        elif assigned_role == "stranger":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "stranger"), None)
        elif assigned_role == "shadow":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "shadow"), None)
        elif assigned_role == "detective":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "detective"), None)
        elif assigned_role == "cook":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "cook"), None)
        elif assigned_role == "medium":
            recipient_id = next((pid for pid, a in assignments.items() if a["role_key"] == "medium"), None)
        elif assigned_role == "random":
            non_murderers = [pid for pid, a in assignments.items() if not a.get("is_murderer")]
            recipient_id = random.choice(non_murderers) if non_murderers else random.choice(player_ids)
        elif assigned_role == "random_non_murderer":
            non_murderers = [pid for pid, a in assignments.items() if not a.get("is_murderer")]
            recipient_id = random.choice(non_murderers) if non_murderers else None

        if recipient_id:
            tasks_to_send.append({"task": task, "recipient": recipient_id})

    return tasks_to_send

def get_ending_text(ending_type, murderer_name, scenario_id, lang="de"):
    """Get the ending text for display."""
    scenario = get_scenario(scenario_id)
    ending = scenario["endings"].get(ending_type, scenario["endings"]["murderer_caught"])
    text = ending["text"][lang] if isinstance(ending.get("text"), dict) else ending.get("text", "")
    title = ending["title"][lang] if isinstance(ending.get("title"), dict) else ending.get("title", "")
    return {
        "title": title,
        "text": text.replace("{murderer_name}", murderer_name)
    }
