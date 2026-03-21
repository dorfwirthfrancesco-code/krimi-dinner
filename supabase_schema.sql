-- ============================================================
-- Krimi Dinner – Supabase Datenbankschema
-- Dieses SQL in Supabase unter: SQL Editor -> New Query einfuegen
-- ============================================================

-- Profile (ergaenzt die auth.users Tabelle von Supabase)
CREATE TABLE IF NOT EXISTS profiles (
  id          UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  username    TEXT UNIQUE NOT NULL,
  genre       TEXT DEFAULT 'Klassischer Krimi',
  rank        INTEGER DEFAULT 1,
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Spielhistorie
CREATE TABLE IF NOT EXISTS game_history (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID REFERENCES profiles(id) ON DELETE CASCADE,
  scenario    TEXT NOT NULL,
  role        TEXT,           -- z.B. "Detektiv", "Moerder", "Verdaechtiger"
  result      TEXT,           -- "gewonnen", "verloren"
  played_at   TIMESTAMPTZ DEFAULT NOW()
);

-- Freundesliste
CREATE TABLE IF NOT EXISTS friendships (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID REFERENCES profiles(id) ON DELETE CASCADE,
  friend_id   UUID REFERENCES profiles(id) ON DELETE CASCADE,
  status      TEXT DEFAULT 'pending',  -- 'pending', 'accepted'
  created_at  TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, friend_id)
);

-- Lobbys
CREATE TABLE IF NOT EXISTS lobbies (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code        TEXT UNIQUE NOT NULL,
  host_id     UUID REFERENCES profiles(id) ON DELETE CASCADE,
  scenario    TEXT NOT NULL,
  max_players INTEGER DEFAULT 6,
  status      TEXT DEFAULT 'waiting',  -- 'waiting', 'playing', 'finished'
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Lobby-Mitglieder
CREATE TABLE IF NOT EXISTS lobby_players (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lobby_id    UUID REFERENCES lobbies(id) ON DELETE CASCADE,
  user_id     UUID REFERENCES profiles(id) ON DELETE CASCADE,
  joined_at   TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(lobby_id, user_id)
);

-- ── Row Level Security (RLS) ──────────────────────────────
ALTER TABLE profiles       ENABLE ROW LEVEL SECURITY;
ALTER TABLE game_history   ENABLE ROW LEVEL SECURITY;
ALTER TABLE friendships    ENABLE ROW LEVEL SECURITY;
ALTER TABLE lobbies        ENABLE ROW LEVEL SECURITY;
ALTER TABLE lobby_players  ENABLE ROW LEVEL SECURITY;

-- Profiles: jeder kann lesen, nur eigenes bearbeiten
CREATE POLICY "profiles_select" ON profiles FOR SELECT USING (true);
CREATE POLICY "profiles_insert" ON profiles FOR INSERT WITH CHECK (auth.uid() = id);
CREATE POLICY "profiles_update" ON profiles FOR UPDATE USING (auth.uid() = id);

-- Game History: nur eigene sehen
CREATE POLICY "history_select" ON game_history FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "history_insert" ON game_history FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Friendships: eigene sehen und erstellen
CREATE POLICY "friends_select" ON friendships FOR SELECT USING (auth.uid() = user_id OR auth.uid() = friend_id);
CREATE POLICY "friends_insert" ON friendships FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "friends_update" ON friendships FOR UPDATE USING (auth.uid() = user_id OR auth.uid() = friend_id);

-- Lobbys: alle sehen, nur Host bearbeiten
CREATE POLICY "lobbies_select" ON lobbies FOR SELECT USING (true);
CREATE POLICY "lobbies_insert" ON lobbies FOR INSERT WITH CHECK (auth.uid() = host_id);
CREATE POLICY "lobbies_update" ON lobbies FOR UPDATE USING (auth.uid() = host_id);

-- Lobby Players: alle im Lobby sehen, selbst beitreten
CREATE POLICY "lobby_players_select" ON lobby_players FOR SELECT USING (true);
CREATE POLICY "lobby_players_insert" ON lobby_players FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "lobby_players_delete" ON lobby_players FOR DELETE USING (auth.uid() = user_id);

-- ── Trigger: Profil automatisch bei Registrierung erstellen ──
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, username)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'username', split_part(NEW.email, '@', 1))
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
