-- ============================================================
-- Krimi Dinner — Spiellogik Tabellen
-- In Supabase SQL Editor ausführen
-- ============================================================

CREATE TABLE IF NOT EXISTS game_sessions (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lobby_id   UUID REFERENCES lobbies(id) ON DELETE CASCADE,
  scenario   TEXT NOT NULL DEFAULT 'dunkelbach',
  phase      INTEGER DEFAULT 0,
  state      JSONB DEFAULT '{}',
  started_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS player_roles (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  game_id        UUID REFERENCES game_sessions(id) ON DELETE CASCADE,
  user_id        UUID REFERENCES profiles(id) ON DELETE CASCADE,
  role_key       TEXT NOT NULL,
  is_murderer    BOOLEAN DEFAULT FALSE,
  clues_received JSONB DEFAULT '[]',
  actions_taken  JSONB DEFAULT '[]',
  role_card      JSONB DEFAULT '{}',
  UNIQUE(game_id, user_id)
);

CREATE TABLE IF NOT EXISTS game_events (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  game_id     UUID REFERENCES game_sessions(id) ON DELETE CASCADE,
  event_type  TEXT NOT NULL DEFAULT 'message',
  from_player UUID REFERENCES profiles(id),
  to_player   UUID REFERENCES profiles(id),
  content     JSONB DEFAULT '{}',
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- RLS
ALTER TABLE game_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_roles  ENABLE ROW LEVEL SECURITY;
ALTER TABLE game_events   ENABLE ROW LEVEL SECURITY;

-- Policies
CREATE POLICY "gs_select" ON game_sessions FOR SELECT USING (true);
CREATE POLICY "gs_insert" ON game_sessions FOR INSERT WITH CHECK (true);
CREATE POLICY "gs_update" ON game_sessions FOR UPDATE USING (true);

CREATE POLICY "pr_select" ON player_roles FOR SELECT
  USING (auth.uid() = user_id OR true);
CREATE POLICY "pr_insert" ON player_roles FOR INSERT WITH CHECK (true);
CREATE POLICY "pr_update" ON player_roles FOR UPDATE USING (true);

CREATE POLICY "ge_select" ON game_events FOR SELECT
  USING (to_player IS NULL OR to_player = auth.uid() OR from_player = auth.uid());
CREATE POLICY "ge_insert" ON game_events FOR INSERT WITH CHECK (true);

-- Realtime for game events
ALTER PUBLICATION supabase_realtime ADD TABLE game_events;
ALTER PUBLICATION supabase_realtime ADD TABLE game_sessions;
