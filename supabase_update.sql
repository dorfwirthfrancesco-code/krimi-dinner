-- ============================================================
-- Run this in Supabase SQL Editor (New Query)
-- Adds avatar, lang, realtime, and invites table
-- ============================================================

-- 1. Add columns to profiles
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS avatar_id INTEGER DEFAULT 1;
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS lang TEXT DEFAULT 'en';

-- 2. Lobby invites table (skip if already exists)
CREATE TABLE IF NOT EXISTS lobby_invites (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lobby_id     UUID REFERENCES lobbies(id) ON DELETE CASCADE,
  from_user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  to_user_id   UUID REFERENCES profiles(id) ON DELETE CASCADE,
  code         TEXT NOT NULL,
  status       TEXT DEFAULT 'pending',
  created_at   TIMESTAMPTZ DEFAULT NOW()
);
ALTER TABLE lobby_invites ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "invites_select" ON lobby_invites;
DROP POLICY IF EXISTS "invites_insert" ON lobby_invites;
DROP POLICY IF EXISTS "invites_update" ON lobby_invites;
DROP POLICY IF EXISTS "invites_delete" ON lobby_invites;

CREATE POLICY "invites_select" ON lobby_invites FOR SELECT
  USING (auth.uid() = from_user_id OR auth.uid() = to_user_id);
CREATE POLICY "invites_insert" ON lobby_invites FOR INSERT
  WITH CHECK (auth.uid() = from_user_id);
CREATE POLICY "invites_update" ON lobby_invites FOR UPDATE
  USING (auth.uid() = to_user_id);
CREATE POLICY "invites_delete" ON lobby_invites FOR DELETE
  USING (auth.uid() = from_user_id OR auth.uid() = to_user_id);

-- 3. Enable Realtime (go to Supabase Dashboard → Database → Replication
--    and enable lobby_players, lobby_invites, lobbies)
--    OR run these (may need superuser):
-- ALTER PUBLICATION supabase_realtime ADD TABLE lobby_players;
-- ALTER PUBLICATION supabase_realtime ADD TABLE lobby_invites;
-- ALTER PUBLICATION supabase_realtime ADD TABLE lobbies;
