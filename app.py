from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from functools import wraps
import os, random, string, json
import urllib.request, urllib.error

# ── Load .env manually (no external lib needed) ───────────────────────────────
def load_env():
    path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())
load_env()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'krimi-dinner-secret-key-2024')
app.config['PERMANENT_SESSION_LIFETIME'] = __import__('datetime').timedelta(days=30)

# ── Supabase Config ───────────────────────────────────────────────────────────
SB_URL = os.environ.get('SUPABASE_URL', '').rstrip('/')
SB_KEY = os.environ.get('SUPABASE_KEY', '')
SB_OK  = bool(SB_URL and SB_KEY and 'DEINE-URL' not in SB_URL)

# ── Supabase HTTP ─────────────────────────────────────────────────────────────
def sb_headers(token=None):
    return {
        'apikey': SB_KEY,
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token or SB_KEY}',
        'Prefer': 'return=representation',
    }

def sb_get(path, params='', token=None):
    if not SB_OK: return None
    url = f'{SB_URL}/rest/v1/{path}?{params}'
    req = urllib.request.Request(url, headers=sb_headers(token))
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f'[SB GET] {path}: {e}')
        return None

def sb_post(path, data, token=None):
    if not SB_OK: return None
    url  = f'{SB_URL}/rest/v1/{path}'
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=sb_headers(token), method='POST')
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f'[SB POST] {path}: {e}')
        return None

def sb_patch(path, params, data, token=None):
    if not SB_OK: return None
    url  = f'{SB_URL}/rest/v1/{path}?{params}'
    body = json.dumps(data).encode()
    req  = urllib.request.Request(url, data=body, headers=sb_headers(token), method='PATCH')
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            txt = r.read()
            return json.loads(txt) if txt else {}
    except Exception as e:
        print(f'[SB PATCH] {path}: {e}')
        return None

def sb_delete(path, params, token=None):
    if not SB_OK: return None
    url = f'{SB_URL}/rest/v1/{path}?{params}'
    req = urllib.request.Request(url, headers=sb_headers(token), method='DELETE')
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return True
    except Exception as e:
        print(f'[SB DELETE] {path}: {e}')
        return False

def sb_auth(path, data):
    if not SB_OK: return None
    url  = f'{SB_URL}/auth/v1/{path}'
    body = json.dumps(data).encode()
    h    = {'apikey': SB_KEY, 'Content-Type': 'application/json'}
    req  = urllib.request.Request(url, data=body, headers=h, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        err = json.loads(e.read())
        raise Exception(err.get('msg') or err.get('message') or str(err))

# ── Helpers ───────────────────────────────────────────────────────────────────
def gen_code(n=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def get_profile(user_id, token=None):
    if not SB_OK or user_id == 'demo':
        return {'username': session.get('username', 'Gast'), 'genre': '', 'rank': 1}
    rows = sb_get('profiles', f'id=eq.{user_id}&select=*', token)
    return rows[0] if rows else {'username': session.get('username', 'Gast')}

def get_stats(user_id, token=None):
    if not SB_OK or user_id == 'demo':
        return {'games': 0, 'wins': 0, 'murderer': 0, 'solved': 0}
    rows = sb_get('game_history', f'user_id=eq.{user_id}&select=*', token) or []
    return {
        'games':    len(rows),
        'wins':     sum(1 for r in rows if r.get('result') == 'gewonnen'),
        'murderer': sum(1 for r in rows if r.get('role') == 'Moerder'),
        'solved':   sum(1 for r in rows if r.get('role') == 'Detektiv' and r.get('result') == 'gewonnen'),
    }

def profiles_by_ids(ids, token=None):
    if not ids: return {}
    rows = sb_get('profiles', f'id=in.({",".join(ids)})&select=id,username', token) or []
    return {r['id']: r['username'] for r in rows}

# ── Splash / Prescreen ────────────────────────────────────────────────────────
@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/prescreen')
def prescreen():
    return render_template('prescreen.html')

# ── Auth ──────────────────────────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember_me') == 'on'
        if not SB_OK:
            session.permanent = remember
            session['user_id']  = 'demo'
            session['username'] = email.split('@')[0] if email else 'Gast'
            return redirect(url_for('home'))
        try:
            res = sb_auth('token?grant_type=password', {'email': email, 'password': password})
            session.permanent       = remember
            session['user_id']      = res['user']['id']
            session['access_token'] = res['access_token']
            p = get_profile(res['user']['id'], res['access_token'])
            session['username'] = p.get('username', email.split('@')[0])
            return redirect(url_for('home'))
        except Exception as e:
            error = 'E-Mail oder Passwort falsch.'
            print(f'[Login] {e}')
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        email     = request.form.get('email', '').strip()
        username  = request.form.get('username', '').strip()
        password  = request.form.get('password', '')
        password2 = request.form.get('password2', '')
        if not username:
            error = 'Bitte einen Anzeigenamen eingeben.'
        elif len(password) < 6:
            error = 'Passwort muss mindestens 6 Zeichen haben.'
        elif password != password2:
            error = 'Passwörter stimmen nicht überein.'
        else:
            if not SB_OK:
                session['user_id']  = 'demo'
                session['username'] = username
                return redirect(url_for('home'))
            try:
                res = sb_auth('signup', {
                    'email': email, 'password': password,
                    'data': {'username': username}
                })
                uid = res.get('user', {}).get('id') or res.get('id')
                if uid:
                    session['user_id']  = uid
                    session['username'] = username
                    if res.get('access_token'):
                        session['access_token'] = res['access_token']
                    return redirect(url_for('home'))
                error = 'Bitte E-Mail bestätigen und dann einloggen.'
            except Exception as e:
                err = str(e)
                error = 'Diese E-Mail ist bereits registriert.' if 'already' in err.lower() else err
    return render_template('register.html', error=error)

@app.route('/auth/google')
def auth_google():
    if not SB_OK:
        return redirect(url_for('login'))
    callback = url_for('auth_callback', _external=True)
    return redirect(f'{SB_URL}/auth/v1/authorize?provider=google&redirect_to={callback}')

@app.route('/auth/callback')
def auth_callback():
    return render_template('auth_callback.html', sb_url=SB_URL, sb_key=SB_KEY)

@app.route('/auth/session', methods=['POST'])
def auth_session():
    data  = request.get_json()
    token = data.get('access_token', '')
    uid   = data.get('user_id', '')
    uname = data.get('username', '')
    if uid and token:
        session['user_id']      = uid
        session['access_token'] = token
        session['username']     = uname or uid[:8]
    return {'ok': True}

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── Home ──────────────────────────────────────────────────────────────────────
@app.route('/home')
@login_required
def home():
    return render_template('home.html', username=session.get('username', 'Gast'))

# ── Shop ──────────────────────────────────────────────────────────────────────
@app.route('/shop')
@login_required
def shop():
    items = [
        {'name': 'Das Venedig-Komplott',   'genre': 'Klassischer Krimi', 'players': '4–8',  'duration': '90 min',  'price': '4,99', 'owned': False, 'tag': 'Neu'},
        {'name': 'Mord im Orient-Express', 'genre': 'Historisch',        'players': '5–10', 'duration': '75 min',  'price': '',     'owned': True,  'tag': ''},
        {'name': 'Die Rache des Butlers',  'genre': 'Cozy Mystery',      'players': '3–6',  'duration': '60 min',  'price': '2,99', 'owned': False, 'tag': 'Beliebt'},
        {'name': 'Noir Downtown',          'genre': 'Hardboiled',        'players': '4–8',  'duration': '90 min',  'price': '4,99', 'owned': False, 'tag': ''},
        {'name': 'Schloss Dunkelberg',     'genre': 'Gothic',            'players': '5–9',  'duration': '120 min', 'price': '5,99', 'owned': False, 'tag': 'Neu'},
        {'name': 'Cocktails & Leichen',    'genre': 'Komödie',           'players': '4–7',  'duration': '60 min',  'price': '2,99', 'owned': False, 'tag': ''},
    ]
    return render_template('shop.html', items=items)

# ── Profile ───────────────────────────────────────────────────────────────────
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    uid   = session.get('user_id')
    token = session.get('access_token')
    if request.method == 'POST':
        uname = request.form.get('username', '').strip()
        genre = request.form.get('genre', '')
        if uname:
            session['username'] = uname
            if SB_OK and uid != 'demo':
                sb_patch('profiles', f'id=eq.{uid}', {'username': uname, 'genre': genre}, token)
        return redirect(url_for('profile'))
    p     = get_profile(uid, token)
    stats = get_stats(uid, token)
    return render_template('profile.html',
        username=p.get('username', session.get('username', 'Gast')),
        profile=p, stats=stats)

# ── Settings ──────────────────────────────────────────────────────────────────
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        session['settings'] = {
            'sound':         'on' if request.form.get('sound') else 'off',
            'music':         'on' if request.form.get('music') else 'off',
            'notifications': 'on' if request.form.get('notifications') else 'off',
            'language':      request.form.get('language', 'de'),
        }
        return redirect(url_for('settings'))
    s = session.get('settings', {'sound':'on','music':'on','notifications':'on','language':'de'})
    return render_template('settings.html', settings=s)

# ── Friends ───────────────────────────────────────────────────────────────────
@app.route('/friends')
@login_required
def friends():
    uid   = session.get('user_id')
    token = session.get('access_token')
    friends_list   = []
    pending_in     = []
    pending_out    = []
    search_results = []
    search_query   = request.args.get('q', '').strip()
    msg            = request.args.get('msg', '')

    if SB_OK and uid != 'demo':
        # Accepted friends
        accepted = sb_get('friendships', f'user_id=eq.{uid}&status=eq.accepted&select=friend_id', token) or []
        friend_ids = [r['friend_id'] for r in accepted]
        if friend_ids:
            pm = profiles_by_ids(friend_ids, token)
            friends_list = [{'id': fid, 'name': pm.get(fid, '?')} for fid in friend_ids]

        # Incoming pending
        rows_in = sb_get('friendships', f'friend_id=eq.{uid}&status=eq.pending&select=id,user_id', token) or []
        if rows_in:
            pm2 = profiles_by_ids([r['user_id'] for r in rows_in], token)
            pending_in = [{'id': r['id'], 'user_id': r['user_id'], 'name': pm2.get(r['user_id'], '?')} for r in rows_in]

        # Outgoing pending
        rows_out = sb_get('friendships', f'user_id=eq.{uid}&status=eq.pending&select=id,friend_id', token) or []
        if rows_out:
            pm3 = profiles_by_ids([r['friend_id'] for r in rows_out], token)
            pending_out = [{'id': r['id'], 'name': pm3.get(r['friend_id'], '?')} for r in rows_out]

        # Search
        if search_query:
            results = sb_get('profiles', f'username=ilike.*{search_query}*&select=id,username&limit=10', token) or []
            known = {uid} | set(friend_ids) | {r['user_id'] for r in rows_in} | {r['friend_id'] for r in rows_out}
            search_results = [r for r in results if r['id'] not in known]
    else:
        friends_list = [
            {'id': '1', 'name': 'MaxMustermann'},
            {'id': '2', 'name': 'ElsaKrimi'},
        ]

    return render_template('friends.html',
        friends=friends_list, pending_in=pending_in, pending_out=pending_out,
        search_results=search_results, search_query=search_query, msg=msg)

@app.route('/friends/add/<friend_id>')
@login_required
def friends_add(friend_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo' and uid != friend_id:
        sb_post('friendships', {'user_id': uid, 'friend_id': friend_id, 'status': 'pending'}, token)
    return redirect(url_for('friends', msg='sent'))

@app.route('/friends/accept/<friendship_id>')
@login_required
def friends_accept(friendship_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        rows = sb_get('friendships', f'id=eq.{friendship_id}&select=user_id,friend_id', token) or []
        if rows and rows[0]['friend_id'] == uid:
            sender_id = rows[0]['user_id']
            sb_patch('friendships', f'id=eq.{friendship_id}', {'status': 'accepted'}, token)
            sb_post('friendships', {'user_id': uid, 'friend_id': sender_id, 'status': 'accepted'}, token)
    return redirect(url_for('friends'))

@app.route('/friends/decline/<friendship_id>')
@login_required
def friends_decline(friendship_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        sb_delete('friendships', f'id=eq.{friendship_id}', token)
    return redirect(url_for('friends'))

# ── Lobby ─────────────────────────────────────────────────────────────────────
@app.route('/create-game', methods=['GET', 'POST'])
@login_required
def create_game():
    if request.method == 'POST':
        uid      = session.get('user_id')
        token    = session.get('access_token')
        code     = gen_code()
        scenario = request.form.get('scenario', 'orient')
        max_p    = int(request.form.get('max_players', 6))

        if SB_OK and uid != 'demo':
            # Delete any old lobbies this user hosted
            old = sb_get('lobbies', f'host_id=eq.{uid}&status=eq.waiting&select=id', token) or []
            for o in old:
                sb_delete('lobby_players', f'lobby_id=eq.{o["id"]}', token)
                sb_delete('lobbies', f'id=eq.{o["id"]}', token)

            res = sb_post('lobbies', {
                'code': code, 'host_id': uid,
                'scenario': scenario, 'max_players': max_p, 'status': 'waiting'
            }, token)
            if res:
                lobby_id = res[0]['id'] if isinstance(res, list) else res.get('id')
                if lobby_id:
                    sb_post('lobby_players', {'lobby_id': lobby_id, 'user_id': uid}, token)
                    session['lobby_id'] = lobby_id

        session['game_code'] = code
        session['is_host']   = True
        return redirect(url_for('lobby', code=code))
    return render_template('create_game.html')

@app.route('/join-game', methods=['GET', 'POST'])
@login_required
def join_game():
    error = None
    if request.method == 'POST':
        code  = request.form.get('code', '').strip().upper()
        uid   = session.get('user_id')
        token = session.get('access_token')
        if len(code) != 6:
            error = 'Ungültiger Code. Bitte 6 Zeichen eingeben.'
        else:
            if SB_OK and uid != 'demo':
                lobbies = sb_get('lobbies', f'code=eq.{code}&status=eq.waiting&select=id,max_players', token) or []
                if not lobbies:
                    error = 'Lobby nicht gefunden oder bereits gestartet.'
                else:
                    lobby_id = lobbies[0]['id']
                    # Check if already in lobby
                    existing = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&user_id=eq.{uid}&select=id', token) or []
                    if not existing:
                        sb_post('lobby_players', {'lobby_id': lobby_id, 'user_id': uid}, token)
                    session['game_code'] = code
                    session['lobby_id']  = lobby_id
                    session['is_host']   = False
                    return redirect(url_for('lobby', code=code))
            else:
                session['game_code'] = code
                session['is_host']   = False
                return redirect(url_for('lobby', code=code))
    return render_template('join_game.html', error=error)

@app.route('/lobby/<code>')
@login_required
def lobby(code):
    uid   = session.get('user_id')
    token = session.get('access_token')
    is_host = session.get('is_host', False)
    players = [session.get('username', 'Gast')]
    lobby_id = session.get('lobby_id', '')
    scenario = 'Mord im Orient-Express'

    if SB_OK and uid != 'demo' and lobby_id:
        lp = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=user_id', token) or []
        player_ids = [r['user_id'] for r in lp]
        if player_ids:
            pm = profiles_by_ids(player_ids, token)
            players = [pm.get(pid, '?') for pid in player_ids]
        lb = sb_get('lobbies', f'id=eq.{lobby_id}&select=scenario,status', token) or []
        if lb:
            scenario = lb[0].get('scenario', scenario)
            if lb[0].get('status') == 'playing':
                return redirect(url_for('game', code=code))

    return render_template('lobby.html',
        code=code, players=players, is_host=is_host,
        lobby_id=lobby_id, scenario=scenario)

@app.route('/lobby/<code>/start', methods=['POST'])
@login_required
def lobby_start(code):
    uid   = session.get('user_id')
    token = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    if SB_OK and uid != 'demo' and lobby_id:
        lb = sb_get('lobbies', f'id=eq.{lobby_id}&select=host_id', token) or []
        if lb and lb[0]['host_id'] == uid:
            sb_patch('lobbies', f'id=eq.{lobby_id}', {'status': 'playing'}, token)
    return redirect(url_for('game', code=code))

@app.route('/game/<code>')
@login_required
def game(code):
    return render_template('game.html', code=code,
        username=session.get('username', 'Gast'),
        scenario=session.get('scenario', 'Mord im Orient-Express'))

# ── API: Lobby poll ───────────────────────────────────────────────────────────
@app.route('/api/lobby/<code>')
@login_required
def api_lobby(code):
    token    = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    if not SB_OK or not lobby_id:
        return jsonify({'players': [session.get('username','Gast')], 'status': 'waiting', 'count': 1})
    try:
        lb = sb_get('lobbies', f'id=eq.{lobby_id}&select=status', token) or []
        status = lb[0]['status'] if lb else 'waiting'
        lp = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=user_id', token) or []
        player_ids = [r['user_id'] for r in lp]
        pm = profiles_by_ids(player_ids, token) if player_ids else {}
        players = [pm.get(pid, '?') for pid in player_ids]
        return jsonify({'players': players, 'status': status, 'count': len(players)})
    except Exception as e:
        print(f'[API lobby] {e}')
        return jsonify({'players': [], 'status': 'waiting', 'count': 0})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'\n  Krimi Dinner')
    print(f'  Supabase: {"verbunden" if SB_OK else "Demo-Modus"}')
    print(f'  http://localhost:{port}\n')
    app.run(debug=False, host='0.0.0.0', port=port)
