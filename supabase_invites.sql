-- Run this in Supabase SQL Editor

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

CREATE POLICY "invites_select" ON lobby_invites FOR SELECT
  USING (auth.uid() = from_user_id OR auth.uid() = to_user_id);
CREATE POLICY "invites_insert" ON lobby_invites FOR INSERT
  WITH CHECK (auth.uid() = from_user_id);
CREATE POLICY "invites_update" ON lobby_invites FOR UPDATE
  USING (auth.uid() = to_user_id);
CREATE POLICY "invites_delete" ON lobby_invites FOR DELETE
  USING (auth.uid() = from_user_id OR auth.uid() = to_user_id);
