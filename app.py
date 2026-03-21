from flask import Flask, render_template, redirect, url_for, session, request
from functools import wraps
import os, random, string, json
import urllib.request, urllib.error

# Lade .env manuell (kein python-dotenv nötig)
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    os.environ.setdefault(key.strip(), val.strip())

load_env()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'krimi-dinner-dev-key-change-in-production')
app.config['PERMANENT_SESSION_LIFETIME'] = __import__('datetime').timedelta(days=30)

# ── Supabase Config ───────────────────────────────────────────────────────────
SB_URL = os.environ.get('SUPABASE_URL', '').rstrip('/')
SB_KEY = os.environ.get('SUPABASE_KEY', '')
SB_OK  = bool(SB_URL and SB_KEY and 'DEINE-URL' not in SB_URL)

# ── Supabase HTTP Helpers ─────────────────────────────────────────────────────
def sb_headers(token=None):
    h = {
        'apikey': SB_KEY,
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token or SB_KEY}',
        'Prefer': 'return=representation',
    }
    return h

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

def sb_auth(path, data):
    """Supabase Auth API call"""
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
    except Exception as e:
        raise

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
    return rows[0] if rows else {'username': session.get('username', 'Gast'), 'genre': '', 'rank': 1}

def get_stats(user_id, token=None):
    empty = {'games': 0, 'wins': 0, 'murderer': 0, 'solved': 0}
    if not SB_OK or user_id == 'demo':
        return empty
    rows = sb_get('game_history', f'user_id=eq.{user_id}&select=*', token) or []
    return {
        'games':    len(rows),
        'wins':     sum(1 for r in rows if r.get('result') == 'gewonnen'),
        'murderer': sum(1 for r in rows if r.get('role') == 'Moerder'),
        'solved':   sum(1 for r in rows if r.get('role') == 'Detektiv' and r.get('result') == 'gewonnen'),
    }

# ── Auth Routes ───────────────────────────────────────────────────────────────
@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/prescreen')
def prescreen():
    return render_template('prescreen.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        if not SB_OK:
            session['user_id']  = 'demo'
            session['username'] = email.split('@')[0] if email else 'Gast'
            return redirect(url_for('home'))
        try:
            res = sb_auth('token?grant_type=password', {'email': email, 'password': password})
            session['user_id']      = res['user']['id']
            session['access_token'] = res['access_token']
            p = get_profile(res['user']['id'], res['access_token'])
            session['username'] = p.get('username', email.split('@')[0])
            remember = request.form.get('remember_me') == 'on'
            if remember:
                session.permanent = True
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
                error = 'Registrierung fehlgeschlagen. Bitte E-Mail bestätigen.'
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

# ── App Routes ────────────────────────────────────────────────────────────────
@app.route('/home')
@login_required
def home():
    return render_template('home.html', username=session.get('username', 'Gast'))

@app.route('/create-game', methods=['GET', 'POST'])
@login_required
def create_game():
    if request.method == 'POST':
        code  = gen_code()
        uid   = session.get('user_id')
        token = session.get('access_token')
        if SB_OK and uid != 'demo':
            res = sb_post('lobbies', {
                'code': code, 'host_id': uid,
                'scenario': request.form.get('scenario', 'orient'),
                'max_players': int(request.form.get('max_players', 6))
            }, token)
            if res:
                lobby_id = res[0]['id'] if isinstance(res, list) else res.get('id')
                if lobby_id:
                    sb_post('lobby_players', {'lobby_id': lobby_id, 'user_id': uid}, token)
        session['game_code'] = code
        return render_template('lobby.html', code=code,
                               players=[session.get('username', 'Gast')], is_host=True)
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
            players = [session.get('username', 'Gast')]
            if SB_OK and uid != 'demo':
                lobbies = sb_get('lobbies', f'code=eq.{code}&select=id', token)
                if lobbies:
                    lobby_id = lobbies[0]['id']
                    sb_post('lobby_players', {'lobby_id': lobby_id, 'user_id': uid}, token)
                    lp = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=profiles(username)', token) or []
                    players = [r['profiles']['username'] for r in lp if r.get('profiles')]
                else:
                    error = 'Lobby nicht gefunden.'
            if not error:
                session['game_code'] = code
                return render_template('lobby.html', code=code, players=players, is_host=False)
    return render_template('join_game.html', error=error)

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

@app.route('/friends')
@login_required
def friends():
    uid   = session.get('user_id')
    token = session.get('access_token')
    friends_list  = []
    pending_in    = []  # requests I received
    pending_out   = []  # requests I sent
    search_results = []
    search_query  = request.args.get('q', '').strip()
    msg = request.args.get('msg', '')

    if SB_OK and uid != 'demo':
        # Accepted friends
        rows = sb_get('friendships',
            f'user_id=eq.{uid}&status=eq.accepted&select=friend_id,profiles!friendships_friend_id_fkey(id,username)',
            token) or []
        friends_list = [{'id': r['profiles']['id'], 'name': r['profiles']['username']}
                        for r in rows if r.get('profiles')]

        # Incoming pending requests
        rows_in = sb_get('friendships',
            f'friend_id=eq.{uid}&status=eq.pending&select=id,user_id,profiles!friendships_user_id_fkey(id,username)',
            token) or []
        pending_in = [{'id': r['id'], 'user_id': r['user_id'], 'name': r['profiles']['username']}
                      for r in rows_in if r.get('profiles')]

        # Outgoing pending requests
        rows_out = sb_get('friendships',
            f'user_id=eq.{uid}&status=eq.pending&select=id,friend_id,profiles!friendships_friend_id_fkey(username)',
            token) or []
        pending_out = [{'id': r['id'], 'name': r['profiles']['username']}
                       for r in rows_out if r.get('profiles')]

        # Search
        if search_query:
            results = sb_get('profiles',
                f'username=ilike.*{search_query}*&select=id,username&limit=10', token) or []
            # Filter out self and existing friends/pending
            known_ids = {uid} | {f['id'] for f in friends_list} |                         {p['user_id'] for p in pending_in} |                         {r['friend_id'] for r in rows_out}
            search_results = [r for r in results if r['id'] not in known_ids]

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
        sb_patch('friendships', f'id=eq.{friendship_id}&friend_id=eq.{uid}',
                 {'status': 'accepted'}, token)
        # Also create reverse friendship
        rows = sb_get('friendships', f'id=eq.{friendship_id}&select=user_id', token) or []
        if rows:
            sb_post('friendships', {'user_id': uid, 'friend_id': rows[0]['user_id'], 'status': 'accepted'}, token)
    return redirect(url_for('friends'))

@app.route('/friends/decline/<friendship_id>')
@login_required
def friends_decline(friendship_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        # Delete the request
        url  = f'{SB_URL}/rest/v1/friendships?id=eq.{friendship_id}&friend_id=eq.{uid}'
        req  = __import__('urllib.request', fromlist=['Request']).Request(
            url, headers=sb_headers(token), method='DELETE')
        try: __import__('urllib.request').urlopen(req, timeout=8)
        except: pass
    return redirect(url_for('friends'))

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

if __name__ == '__main__':
    print()
    print('  Krimi Dinner')
    print(f'  Supabase: {"verbunden (" + SB_URL + ")" if SB_OK else "Demo-Modus (keine .env)"}')
    print('  http://localhost:5000')
    print()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
