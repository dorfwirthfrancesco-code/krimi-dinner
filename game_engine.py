"""
KrimiDinner Game Engine v2
- Host has NO special role — random like everyone else
- Tasks sent automatically based on game state
- Organic flow, no forced phases
"""
import random
import json
from scenarios.dunkelbach import SCENARIO

SCENARIOS = {"dunkelbach": SCENARIO}

def get_scenario(scenario_id):
    return SCENARIOS.get(scenario_id, SCENARIO)

# ── Role Assignment ───────────────────────────────────────────────────────────

def assign_roles(scenario_id, player_ids, lang="de"):
    """Assign roles randomly to all players. Host gets a random role too."""
    scenario = get_scenario(scenario_id)
    n = len(player_ids)

    # Get eligible roles sorted by min_players
    all_roles = scenario["roles"]
    eligible = [(k, v) for k, v in all_roles.items() if v["min_players"] <= n]

    # Sort: mandatory first (min 4), then optional
    mandatory = sorted([r for r in eligible if r[1]["min_players"] == 4], key=lambda x: x[0])
    optional  = sorted([r for r in eligible if r[1]["min_players"] > 4],  key=lambda x: x[1]["min_players"])

    # Pick roles to use — fill up to player count
    selected = mandatory + optional
    selected = selected[:n]

    # Shuffle both players and roles independently for true randomness
    shuffled_players = player_ids[:]
    random.shuffle(shuffled_players)
    random.shuffle(selected)

    # Pick murderer from eligible roles
    murderer_candidates = [r for r in selected if r[1].get("can_be_murderer", False)]
    if not murderer_candidates:
        murderer_candidates = selected
    murderer_key = random.choice(murderer_candidates)[0]

    # Two murderers: 20% chance at 8+ players
    second_murderer_key = None
    if n >= 8 and random.random() < 0.20:
        others = [r for r in murderer_candidates if r[0] != murderer_key]
        if others:
            second_murderer_key = random.choice(others)[0]

    # Build base assignments
    assignments = {}
    for i, pid in enumerate(shuffled_players):
        if i >= len(selected):
            break
        role_key, role_data = selected[i]
        assignments[pid] = {
            "role_key":          role_key,
            "role_name":         role_data["name"][lang],
            "is_murderer":       (role_key == murderer_key or role_key == second_murderer_key),
            "is_second_murderer": role_key == second_murderer_key,
            "is_wildcard":       role_data.get("is_wildcard", False),
            "can_be_ghost":      role_data.get("ghost_mode", False),
        }

    # Baron knows the murderer's name
    baron_id = next((pid for pid, a in assignments.items() if a["role_key"] == "baron"), None)
    murderer_id = next((pid for pid, a in assignments.items() if a.get("is_murderer") and not a.get("is_second_murderer")), None)
    if baron_id and murderer_id:
        murderer_role = assignments[murderer_id]["role_name"]
        assignments[baron_id]["knows_murderer_role"] = murderer_role
        assignments[baron_id]["knows_murderer_id"]   = murderer_id

    # Inspector: 70% chance letter names correct person
    inspector_id = next((pid for pid, a in assignments.items() if a["role_key"] == "detective"), None)
    if inspector_id:
        if random.random() < 0.70 and murderer_id:
            assignments[inspector_id]["barons_feared_role"] = assignments[murderer_id]["role_name"]
            assignments[inspector_id]["barons_feared_id"]   = murderer_id
        else:
            # Red herring — pick a random non-murderer
            others = [pid for pid in assignments if pid != inspector_id and not assignments[pid].get("is_murderer")]
            if others:
                rh = random.choice(others)
                assignments[inspector_id]["barons_feared_role"] = assignments[rh]["role_name"]
                assignments[inspector_id]["barons_feared_id"]   = rh

    # Viktor lover pair
    viktor_id = next((pid for pid, a in assignments.items() if a["role_key"] == "lover"), None)
    if viktor_id:
        candidates = [pid for pid in assignments if pid != viktor_id and not assignments[pid].get("is_murderer")]
        if candidates:
            lover_id = random.choice(candidates)
            assignments[viktor_id]["secret_lover_id"]   = lover_id
            assignments[viktor_id]["secret_lover_role"] = assignments[lover_id]["role_name"]
            assignments[lover_id]["secret_lover_id"]    = viktor_id
            assignments[lover_id]["secret_lover_role"]  = assignments[viktor_id]["role_name"]
            assignments[lover_id]["is_viktors_lover"]   = True

    # Shadow: blackmail targets
    shadow_id = next((pid for pid, a in assignments.items() if a["role_key"] == "shadow"), None)
    if shadow_id:
        others = [pid for pid in assignments if pid != shadow_id]
        targets = random.sample(others, min(3, len(others)))
        bm = []
        for t in targets:
            rk = assignments[t]["role_key"]
            secret = scenario["roles"].get(rk, {}).get("secret", {}).get(lang, "Hat ein Geheimnis.")
            bm.append({"target_id": t, "target_role": assignments[t]["role_name"], "info": secret[:120]})
        assignments[shadow_id]["blackmail_targets"] = bm

    # Stranger: surveillance target = murderer
    stranger_id = next((pid for pid, a in assignments.items() if a["role_key"] == "stranger"), None)
    if stranger_id and murderer_id:
        assignments[stranger_id]["surveillance_target_id"]   = murderer_id
        assignments[stranger_id]["surveillance_target_role"] = assignments[murderer_id]["role_name"]

    # Cook knows who hired them (= murderer)
    cook_id = next((pid for pid, a in assignments.items() if a["role_key"] == "cook"), None)
    if cook_id and murderer_id and not assignments[cook_id].get("is_murderer"):
        assignments[cook_id]["hired_by_id"]   = murderer_id
        assignments[cook_id]["hired_by_role"] = assignments[murderer_id]["role_name"]

    # Butler saw niece in library (if both exist)
    butler_id = next((pid for pid, a in assignments.items() if a["role_key"] == "butler"), None)
    niece_id  = next((pid for pid, a in assignments.items() if a["role_key"] == "niece"),  None)
    if butler_id and niece_id:
        assignments[butler_id]["saw_in_library_id"]   = niece_id
        assignments[butler_id]["saw_in_library_role"] = assignments[niece_id]["role_name"]
        assignments[niece_id]["butler_saw_me"]        = True
        assignments[niece_id]["butler_id"]            = butler_id

    return assignments


def get_role_card(player_id, assignments, scenario_id, lang="de"):
    """Build the full role card for a player."""
    scenario  = get_scenario(scenario_id)
    a         = assignments[player_id]
    role_key  = a["role_key"]
    role_data = scenario["roles"][role_key]

    card = {
        "role_name":      role_data["name"][lang],
        "intro":          role_data["intro"][lang],
        "appearance":     role_data["appearance"][lang],
        "secret":         role_data["secret"][lang],
        "ability_name":   role_data["ability"]["name"][lang],
        "ability_desc":   role_data["ability"]["description"][lang],
        "win_condition":  role_data["win_condition"][lang],
        "starting_knowledge": role_data["starting_knowledge"][lang],
        "is_murderer":    a.get("is_murderer", False),
        "is_wildcard":    a.get("is_wildcard", False),
        "can_be_ghost":   a.get("can_be_ghost", False),
    }

    if a.get("is_murderer"):
        card["murderer_motive"] = role_data.get("murderer_motive_if_assigned", {}).get(lang, "")

    if a.get("knows_murderer_role"):
        card["knows_murderer_role"] = a["knows_murderer_role"]

    if a.get("barons_feared_role"):
        card["barons_feared_person"] = a["barons_feared_role"]

    if a.get("secret_lover_role"):
        card["secret_lover_role"] = a["secret_lover_role"]
        card["is_viktors_lover"]  = a.get("is_viktors_lover", False)

    if a.get("blackmail_targets"):
        card["blackmail_targets"] = a["blackmail_targets"]

    if a.get("surveillance_target_role"):
        card["surveillance_target"] = a["surveillance_target_role"]

    if a.get("hired_by_role"):
        card["hired_by"] = a["hired_by_role"]

    if a.get("saw_in_library_role"):
        card["saw_in_library"] = a["saw_in_library_role"]

    if a.get("butler_saw_me"):
        card["butler_saw_me"] = True

    return card


def get_initial_clues(player_id, assignments, scenario_id, lang="de"):
    scenario  = get_scenario(scenario_id)
    a         = assignments[player_id]
    role_data = scenario["roles"][a["role_key"]]
    clues = []
    for ck in role_data.get("clues_i_hold", []):
        cd = scenario["clues"].get(ck)
        if cd:
            clues.append({"id": ck, "name": cd["name"][lang], "text": cd["text"][lang]})
    return clues


# ── Task Distributor ──────────────────────────────────────────────────────────

def get_tasks_for_trigger(trigger, game_state, assignments, player_ids, scenario_id, lang="de"):
    """
    Main task dispatcher. Called whenever a trigger fires.
    Returns list of {recipient_id, task_id, instruction, game_effect, broadcast, private}
    """
    scenario = get_scenario(scenario_id)
    tasks_to_send = []
    done_tasks = game_state.get("tasks_sent", [])

    for task_id, task in scenario.get("physical_tasks", {}).items():
        if task_id in done_tasks:
            continue
        if task.get("trigger_condition") != trigger:
            continue

        assigned_to = task.get("assigned_to", "random")
        recipients  = _resolve_recipients(assigned_to, task, game_state, assignments, player_ids)

        for pid in recipients:
            instruction = task.get("instruction", {}).get(lang, "")
            if not instruction:
                continue

            # Murderer-specific tasks get private flag
            is_private = task.get("private", False) or "murderer" in task_id

            tasks_to_send.append({
                "task_id":     task_id,
                "recipient_id": pid,
                "instruction": instruction,
                "game_effect": task.get("game_effect", ""),
                "broadcast":   task.get("broadcast", False),
                "private":     is_private,
                "what_they_find": task.get("what_they_find", {}).get(lang, ""),
                "clue_revealed":  task.get("clue_revealed", {}).get(lang, ""),
            })

    return tasks_to_send


def _resolve_recipients(assigned_to, task, game_state, assignments, player_ids):
    """Resolve who receives a task."""
    murderer_ids = [pid for pid, a in assignments.items() if a.get("is_murderer")]
    murderer_id  = murderer_ids[0] if murderer_ids else None

    role_map = {
        "witness":   "witness",
        "doctor":    "doctor",
        "stranger":  "stranger",
        "shadow":    "shadow",
        "detective": "detective",
        "cook":      "cook",
        "medium":    "medium",
        "butler":    "butler",
        "baron":     "baron",
        "niece":     "niece",
    }

    if assigned_to == "all":
        return player_ids[:]

    if assigned_to == "murderer":
        return murderer_ids

    if assigned_to == "random_non_murderer":
        candidates = [pid for pid in player_ids if pid not in murderer_ids]
        return [random.choice(candidates)] if candidates else []

    if assigned_to == "random":
        return [random.choice(player_ids)]

    if assigned_to == "viktor_secret_lover":
        lover_id = next(
            (pid for pid, a in assignments.items() if a.get("is_viktors_lover")), None)
        return [lover_id] if lover_id else []

    # Role-based
    if assigned_to in role_map:
        role_key = role_map[assigned_to]
        pid = next((p for p, a in assignments.items() if a["role_key"] == role_key), None)
        return [pid] if pid else []

    return []


def get_atmosphere_message(trigger, lang="de"):
    """Return atmosphere broadcast for a trigger."""
    for msg in SCENARIO.get("atmosphere_messages", []):
        if msg.get("trigger") == trigger:
            return msg["text"].get(lang, msg["text"].get("en", ""))
    return None


# ── Game Triggers ─────────────────────────────────────────────────────────────
# These are the trigger names the app uses to fire tasks

TRIGGER_SEQUENCE = [
    # (trigger_name, description, fires_at_minute_approx)
    ("game_started_5min",          "Spiel gestartet 5min",        5),
    ("first_10_minutes",           "Erste 10 Minuten",            10),
    ("random_15min",               "Zufällig 15min",              15),
    ("baron_death_minus_5min",     "Baron stirbt bald",           20),
    ("baron_dies",                 "Baron stirbt",                25),
    ("body_discovered",            "Leiche gefunden",             25),
    ("investigation_begins",       "Ermittlung beginnt",          27),
    ("first_30min",                "Erste 30 Minuten",            30),
    ("midgame_20min",              "Mitte Ermittlung",            40),
    ("random_20min",               "Zufällig 20min",              35),
    ("random_post_murder",         "Nach Mord",                   30),
    ("cook_under_pressure",        "Köchin unter Druck",          45),
    ("random_after_murder",        "Zufällig nach Mord",          35),
    ("butler_uses_ability",        "Butler nutzt Fähigkeit",      35),
    ("murder_announced",           "Mord angekündigt",            25),
    ("investigation_10min",        "Ermittlung 10min",            35),
    ("investigation_5min",         "Ermittlung 5min",             30),
    ("viktor_under_pressure",      "Viktor unter Druck",          50),
    ("investigation_midpoint",     "Ermittlungsmitte",            50),
    ("doctor_announces_cause",     "Arzt verkündet Todesursache", 40),
    ("medium_activated",           "Medium aktiviert",            45),
    ("someone_gets_close_to_truth","Jemand kommt nah",            55),
    ("random_any_time",            "Zufälliger Moment",           45),
    ("random_post_murder_20min",   "20min nach Mord",             45),
    ("atmosphere_trigger",         "Atmosphäre",                  40),
    ("both_suspects_high_suspicion","Zwei unter Verdacht",        50),
    ("baron_death_announced",      "Baron Tod angekündigt",       25),
    ("baron_proposes_toast",       "Baron toastet",               22),
    ("investigation_30min",        "Ermittlung 30min",            55),
]


# ── Win Conditions ────────────────────────────────────────────────────────────

def check_win_conditions(game_state, assignments, votes, scenario_id):
    scenario     = get_scenario(scenario_id)
    murderer_ids = [pid for pid, a in assignments.items() if a.get("is_murderer")]
    if not murderer_ids:
        return {"ending": "error", "winners": []}

    primary_murderer = murderer_ids[0]

    # Shadow win
    shadow_id = next((pid for pid, a in assignments.items() if a.get("role_key") == "shadow"), None)
    if shadow_id and game_state.get("will_stolen"):
        return {"ending": "shadow_wins", "winners": [shadow_id], "murderer_id": primary_murderer}

    if not votes:
        return {"ending": "no_vote", "winners": []}

    # Count votes
    vote_counts = {}
    for v in votes.values():
        vote_counts[v] = vote_counts.get(v, 0) + 1
    most_voted = max(vote_counts, key=vote_counts.get)

    if most_voted == primary_murderer:
        winners = [pid for pid, v in votes.items() if v == primary_murderer]
        # Perfect solve bonus
        witness_id = next((pid for pid, a in assignments.items() if a["role_key"] == "witness"), None)
        doctor_id  = next((pid for pid, a in assignments.items() if a["role_key"] == "doctor"),  None)
        perfect = (
            witness_id in winners and doctor_id in winners
            and game_state.get("witness_vision_correct")
            and game_state.get("doctor_correct")
        )
        return {
            "ending":      "perfect_solve" if perfect else "murderer_caught",
            "winners":     winners,
            "murderer_id": primary_murderer,
        }
    else:
        return {
            "ending":           "murderer_escapes",
            "winners":          murderer_ids,
            "wrongly_convicted": most_voted,
            "murderer_id":      primary_murderer,
        }


def get_ending_text(ending_type, murderer_name, scenario_id, lang="de"):
    scenario = get_scenario(scenario_id)
    ending   = scenario["endings"].get(ending_type, scenario["endings"]["murderer_caught"])
    title    = ending.get("title", {}).get(lang, ending.get("title", {}).get("en", ""))
    text_raw = ending.get("text", {})
    text     = text_raw.get(lang, text_raw.get("en", "")) if isinstance(text_raw, dict) else str(text_raw)
    return {"title": title, "text": text.replace("{murderer_name}", murderer_name)}
