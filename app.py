from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from functools import wraps
from translations import get_t, SUPPORTED_LANGS
from game_engine import (assign_roles, get_role_card, get_initial_clues,
                         check_win_conditions, get_ending_text,
                         get_tasks_for_trigger, get_atmosphere_message)
import os, random, string, json, hmac, hashlib
import urllib.request, urllib.error

# ── Lemon Squeezy Config ─────────────────────────────────────────────────────
LS_API_KEY      = os.environ.get('LEMONSQUEEZY_API_KEY', '')
LS_STORE_ID     = os.environ.get('LEMONSQUEEZY_STORE_ID', '339836')
LS_WEBHOOK_SECRET = os.environ.get('LEMONSQUEEZY_WEBHOOK_SECRET', '')

# Variant IDs for each scenario (set after creating products in LS dashboard)
def _clean_id(v):
    """Strip whitespace and quotes from env var values."""
    v = v.strip()
    if len(v) >= 2 and v[0] in ('"', "'") and v[-1] in ('"', "'"):
        v = v[1:-1]
    return v

LS_VARIANTS = {
    'venedig':    _clean_id(os.environ.get('LS_VARIANT_VENEDIG', '')),
    'butler':     _clean_id(os.environ.get('LS_VARIANT_BUTLER', '')),
    'noir':       _clean_id(os.environ.get('LS_VARIANT_NOIR', '')),
    'dunkelberg': _clean_id(os.environ.get('LS_VARIANT_DUNKELBERG', '')),
    'cocktails':  _clean_id(os.environ.get('LS_VARIANT_COCKTAILS', '')),
}

def ls_headers():
    return {
        'Authorization': f'Bearer {LS_API_KEY}',
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }

def ls_create_checkout(variant_id, user_email, user_id, scenario):
    """Create a Lemon Squeezy checkout URL."""
    if not LS_API_KEY or not variant_id:
        print(f"LS checkout missing: api_key={bool(LS_API_KEY)}, variant={variant_id}")
        return None
    checkout_data = {'custom': {'user_id': user_id, 'scenario': scenario}}
    if user_email:
        checkout_data['email'] = user_email
    payload = json.dumps({
        'data': {
            'type': 'checkouts',
            'attributes': {
                'checkout_data': checkout_data,
                'checkout_options': {
                    'embed': False,
                    'media': False,
                    'button_color': '#f5f5f3',
                },
                'product_options': {
                    'redirect_url': f'https://web-production-ad99.up.railway.app/shop/success?scenario={scenario}',
                    'receipt_button_text': 'Zurück zum Shop',
                    'receipt_link_url': 'https://web-production-ad99.up.railway.app/shop',
                },
                'expires_at': None,
            },
            'relationships': {
                'store': {'data': {'type': 'stores', 'id': str(LS_STORE_ID)}},
                'variant': {'data': {'type': 'variants', 'id': str(variant_id)}},
            },
        }
    }).encode()
    req = urllib.request.Request(
        'https://api.lemonsqueezy.com/v1/checkouts',
        data=payload, headers=ls_headers(), method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            return data['data']['attributes']['url']
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f'LS checkout HTTP error {e.code}: {body}')
        return None
    except Exception as e:
        print(f'LS checkout error: {e}')
        return None

def ls_verify_webhook(payload_bytes, signature):
    """Verify Lemon Squeezy webhook signature."""
    if not LS_WEBHOOK_SECRET:
        return True  # skip in dev
    expected = hmac.new(
        LS_WEBHOOK_SECRET.encode(), payload_bytes, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature or '')

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
app.secret_key = os.environ.get('SECRET_KEY', 'krimi-dinner-secret-2024')
app.config['PERMANENT_SESSION_LIFETIME'] = __import__('datetime').timedelta(days=30)

SB_URL = os.environ.get('SUPABASE_URL', '').rstrip('/')
SB_KEY = os.environ.get('SUPABASE_KEY', '')
SB_OK  = bool(SB_URL and SB_KEY and 'DEINE-URL' not in SB_URL)

# ── Context processor: inject translations into every template ────────────────
@app.context_processor
def inject_t():
    lang = session.get('lang', 'en')
    return {
        't': get_t(lang),
        'lang': lang,
        'supported_langs': SUPPORTED_LANGS,
        'config': {'SUPABASE_URL': SB_URL, 'SUPABASE_KEY': SB_KEY},
    }

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
        urllib.request.urlopen(req, timeout=8)
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

def sb_auth_reset(email):
    if not SB_OK: return None
    url  = f'{SB_URL}/auth/v1/recover'
    body = json.dumps({'email': email}).encode()
    h    = {'apikey': SB_KEY, 'Content-Type': 'application/json'}
    req  = urllib.request.Request(url, data=body, headers=h, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise Exception(json.loads(e.read()).get('msg', 'Error'))

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

def profiles_by_ids(ids, token=None):
    if not ids: return {}
    rows = sb_get('profiles', f'id=in.({",".join(ids)})&select=id,username', token) or []
    return {r['id']: r['username'] for r in rows}

def get_profile(user_id, token=None):
    if not SB_OK or user_id == 'demo':
        return {'username': session.get('username', 'Guest'), 'genre': '', 'rank': 1}
    rows = sb_get('profiles', f'id=eq.{user_id}&select=*', token)
    return rows[0] if rows else {'username': session.get('username', 'Guest')}

def get_stats(user_id, token=None):
    if not SB_OK or user_id == 'demo':
        return {'games': 0, 'wins': 0, 'murderer': 0, 'solved': 0}
    rows = sb_get('game_history', f'user_id=eq.{user_id}&select=*', token) or []
    return {
        'games':    len(rows),
        'wins':     sum(1 for r in rows if r.get('result') == 'won'),
        'murderer': sum(1 for r in rows if r.get('role') == 'murderer'),
        'solved':   sum(1 for r in rows if r.get('role') == 'detective' and r.get('result') == 'won'),
    }

# ── Splash / Prescreen ────────────────────────────────────────────────────────
@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/prescreen')
def prescreen():
    return render_template('prescreen.html')

# ── Language ──────────────────────────────────────────────────────────────────
@app.route('/set-lang/<lang>')
def set_lang(lang):
    if lang in SUPPORTED_LANGS:
        session['lang'] = lang
        # Save to profile if logged in
        uid   = session.get('user_id')
        token = session.get('access_token')
        if SB_OK and uid and uid != 'demo':
            sb_patch('profiles', f'id=eq.{uid}', {'lang': lang}, token)
    return redirect(request.referrer or url_for('home'))

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
            session.permanent  = remember
            session['user_id'] = 'demo'
            session['username']= email.split('@')[0] if email else 'Guest'
            return redirect(url_for('home'))
        try:
            res = sb_auth('token?grant_type=password', {'email': email, 'password': password})
            session.permanent        = remember
            session['user_id']       = res['user']['id']
            session['access_token']  = res['access_token']
            p = get_profile(res['user']['id'], res['access_token'])
            session['username'] = p.get('username', email.split('@')[0])
            if p.get('lang'):
                session['lang'] = p['lang']
            return redirect(url_for('home'))
        except Exception as e:
            t = get_t(session.get('lang','en'))
            error = t.get('login_title', 'Wrong email or password.')
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
        lang      = request.form.get('lang', 'en')
        if lang in SUPPORTED_LANGS:
            session['lang'] = lang
        if not username:
            error = 'Please enter a display name.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters.'
        elif password != password2:
            error = 'Passwords do not match.'
        else:
            if not SB_OK:
                session['user_id']  = 'demo'
                session['username'] = username
                return redirect(url_for('home'))
            try:
                res = sb_auth('signup', {
                    'email': email, 'password': password,
                    'data': {'username': username, 'lang': lang}
                })
                uid = res.get('user', {}).get('id') or res.get('id')
                if uid:
                    session['user_id']  = uid
                    session['username'] = username
                    if res.get('access_token'):
                        session['access_token'] = res['access_token']
                    return redirect(url_for('home'))
                error = 'Please confirm your email then sign in.'
            except Exception as e:
                err = str(e)
                error = 'This email is already registered.' if 'already' in err.lower() else err
    return render_template('register.html', error=error)

@app.route('/auth/google')
def auth_google():
    if not SB_OK: return redirect(url_for('login'))
    cb = url_for('auth_callback', _external=True)
    return redirect(f'{SB_URL}/auth/v1/authorize?provider=google&redirect_to={cb}')

@app.route('/auth/callback')
def auth_callback():
    return render_template('auth_callback.html', sb_url=SB_URL, sb_key=SB_KEY)

@app.route('/auth/session', methods=['POST'])
def auth_session():
    data  = request.get_json()
    token = data.get('access_token', '')
    uid   = data.get('user_id', '')
    uname = data.get('username', '')
    lang  = data.get('lang', 'en')
    if uid and token:
        session['user_id']      = uid
        session['access_token'] = token
        session['username']     = uname or uid[:8]
        if lang in SUPPORTED_LANGS:
            session['lang'] = lang
    return {'ok': True}

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    msg = None
    error = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        if not email:
            error = 'Please enter your email.'
        elif not SB_OK:
            msg = 'Demo mode — password reset not available.'
        else:
            try:
                sb_auth_reset(email)
                msg = 'Check your email for a reset link.'
            except Exception as e:
                error = str(e)
    return render_template('forgot_password.html', msg=msg, error=error)

@app.route('/save-game', methods=['POST'])
@login_required
def save_game():
    '''Called when a game ends to save history.'''
    uid   = session.get('user_id')
    token = session.get('access_token')
    data  = request.get_json() or {}
    if SB_OK and uid != 'demo':
        sb_post('game_history', {
            'user_id':  uid,
            'scenario': data.get('scenario', ''),
            'role':     data.get('role', ''),
            'result':   data.get('result', ''),
        }, token)
    return jsonify({'ok': True})

# ── Home ──────────────────────────────────────────────────────────────────────
@app.route('/home')
@login_required
def home():
    return render_template('home.html', username=session.get('username', 'Guest'))

# ── Shop ──────────────────────────────────────────────────────────────────────
@app.route('/shop')
@login_required
def shop():
    t        = get_t(session.get('lang', 'en'))
    uid      = session.get('user_id')
    token    = session.get('access_token')

    # Get user's purchases
    owned = {'dunkelbach'}  # always free
    if SB_OK and uid != 'demo':
        rows = sb_get('purchases', f'user_id=eq.{uid}&select=scenario', token) or []
        for r in rows:
            owned.add(r['scenario'])

    items = [
        {'id': 'venedig',    'name': 'Die Maske des Verräters', 'genre': t['genre_classic'],    'players': '4–11', 'duration': '90–120 min', 'price': '4.99', 'tag': 'New'},
        {'id': 'butler',     'name': 'Die Rache des Butlers',   'genre': t['genre_cozy'],       'players': '3–6',  'duration': '60 min',    'price': '2.99', 'tag': ''},
        {'id': 'noir',       'name': 'Noir Downtown',           'genre': t['genre_hardboiled'], 'players': '4–8',  'duration': '90 min',    'price': '4.99', 'tag': ''},
        {'id': 'dunkelberg', 'name': 'Schloss Dunkelberg',      'genre': t['genre_gothic'],     'players': '5–9',  'duration': '120 min',   'price': '5.99', 'tag': ''},
        {'id': 'cocktails',  'name': 'Cocktails & Leichen',     'genre': t['genre_comedy'],     'players': '4–7',  'duration': '60 min',    'price': '2.99', 'tag': ''},
    ]
    for item in items:
        item['owned'] = item['id'] in owned

    return render_template('shop.html', t=t, items=items)

@app.route('/debug/ls')
def debug_ls():
    return jsonify({
        'api_key_set': bool(LS_API_KEY),
        'store_id': LS_STORE_ID,
        'variants_cleaned': LS_VARIANTS,
        'variant_venedig_raw': repr(os.environ.get('LS_VARIANT_VENEDIG', 'NOT SET')),
    })

@app.route('/shop/buy/<scenario_id>')
@login_required
def shop_buy(scenario_id):
    """Create Lemon Squeezy checkout and redirect."""
    uid   = session.get('user_id', '')
    token = session.get('access_token', '')
    email = session.get('email', '')

    # Try to get email from profile
    if not email and SB_OK and uid and uid != 'demo':
        try:
            rows = sb_get('profiles', f'id=eq.{uid}&select=username', token) or []
        except:
            pass

    variant_id = LS_VARIANTS.get(scenario_id, '').strip()
    if not variant_id:
        return render_template('shop_coming_soon.html', t=get_t(session.get('lang','en')))

    url = ls_create_checkout(variant_id, email, uid, scenario_id)
    if url:
        return redirect(url)
    # Show error page instead of silent redirect
    return render_template('shop_coming_soon.html', t=get_t(session.get('lang','en')))

@app.route('/shop/success')
@login_required
def shop_success():
    scenario = request.args.get('scenario', '')
    t = get_t(session.get('lang', 'en'))
    return render_template('shop_success.html', t=t, scenario=scenario)

@app.route('/lemon/webhook', methods=['POST'])
def lemon_webhook():
    """Handle Lemon Squeezy webhook — record purchase in DB."""
    payload = request.get_data()
    sig     = request.headers.get('X-Signature', '')

    if not ls_verify_webhook(payload, sig):
        return jsonify({'error': 'invalid signature'}), 401

    try:
        data  = json.loads(payload)
        event = request.headers.get('X-Event-Name', '')

        if event == 'order_created':
            attrs    = data.get('data', {}).get('attributes', {})
            custom   = attrs.get('custom_data', {}) or {}
            user_id  = custom.get('user_id')
            scenario = custom.get('scenario')
            order_id = str(data.get('data', {}).get('id', ''))
            variant_id = str(attrs.get('first_order_item', {}).get('variant_id', ''))
            amount   = attrs.get('total', 0)
            currency = attrs.get('currency', 'EUR')
            status   = attrs.get('status', '')

            if user_id and scenario and status in ('paid', 'complete'):
                # Check not already recorded
                existing = sb_get('purchases', f'user_id=eq.{user_id}&scenario=eq.{scenario}&select=id', None)
                if not existing:
                    sb_post('purchases', {
                        'user_id':          user_id,
                        'scenario':         scenario,
                        'lemon_order_id':   order_id,
                        'lemon_variant_id': variant_id,
                        'amount_cents':     amount,
                        'currency':         currency,
                        'status':           'paid',
                    }, None)
    except Exception as e:
        print(f'Webhook error: {e}')

    return jsonify({'ok': True}), 200


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    uid   = session.get('user_id')
    token = session.get('access_token')
    if request.method == 'POST':
        uname = request.form.get('username', '').strip()
        genre = request.form.get('genre', '')
        lang  = request.form.get('lang', session.get('lang', 'en'))
        if uname:
            session['username'] = uname
        if lang in SUPPORTED_LANGS:
            session['lang'] = lang
        avatar = request.form.get('avatar', '')
        if SB_OK and uid != 'demo':
            update = {'genre': genre, 'lang': lang}
            if uname: update['username'] = uname
            try:
                if avatar and avatar.isdigit(): update['avatar_id'] = int(avatar)
            except: pass
            sb_patch('profiles', f'id=eq.{uid}', update, token)
        return redirect(url_for('profile'))
    p     = get_profile(uid, token)
    stats = get_stats(uid, token)
    return render_template('profile.html',
        username=p.get('username', session.get('username','Guest')),
        profile=p, stats=stats)

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
        accepted   = sb_get('friendships', f'user_id=eq.{uid}&status=eq.accepted&select=friend_id', token) or []
        friend_ids = [r['friend_id'] for r in accepted]
        if friend_ids:
            pm = profiles_by_ids(friend_ids, token)
            friends_list = [{'id': fid, 'name': pm.get(fid,'?')} for fid in friend_ids]

        rows_in = sb_get('friendships', f'friend_id=eq.{uid}&status=eq.pending&select=id,user_id', token) or []
        if rows_in:
            pm2 = profiles_by_ids([r['user_id'] for r in rows_in], token)
            pending_in = [{'id': r['id'], 'user_id': r['user_id'], 'name': pm2.get(r['user_id'],'?')} for r in rows_in]

        rows_out = sb_get('friendships', f'user_id=eq.{uid}&status=eq.pending&select=id,friend_id', token) or []
        if rows_out:
            pm3 = profiles_by_ids([r['friend_id'] for r in rows_out], token)
            pending_out = [{'id': r['id'], 'name': pm3.get(r['friend_id'],'?')} for r in rows_out]

        if search_query:
            results = sb_get('profiles', f'username=ilike.*{search_query}*&select=id,username&limit=10', token) or []
            known = {uid} | set(friend_ids) | {r['user_id'] for r in rows_in} | {r['friend_id'] for r in rows_out}
            search_results = [r for r in results if r['id'] not in known]
    else:
        friends_list = [{'id':'1','name':'MaxMustermann'},{'id':'2','name':'ElsaKrimi'}]

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
            sb_patch('friendships', f'id=eq.{friendship_id}', {'status': 'accepted'}, token)
            sb_post('friendships', {'user_id': uid, 'friend_id': rows[0]['user_id'], 'status': 'accepted'}, token)
    return redirect(url_for('friends'))

@app.route('/friends/decline/<friendship_id>')
@login_required
def friends_decline(friendship_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        sb_delete('friendships', f'id=eq.{friendship_id}', token)
    return redirect(url_for('friends'))

@app.route('/friends/profile/<friend_id>')
@login_required
def friend_profile(friend_id):
    token = session.get('access_token')
    rows  = sb_get('profiles', f'id=eq.{friend_id}&select=*', token) or []
    if not rows:
        return redirect(url_for('friends'))
    p     = rows[0]
    stats = get_stats(friend_id, token)
    return render_template('friend_profile.html', friend=p, stats=stats)

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
            error = 'Invalid code. Please enter 6 characters.'
        else:
            if SB_OK and uid != 'demo':
                lobbies = sb_get('lobbies', f'code=eq.{code}&status=eq.waiting&select=id,max_players', token) or []
                if not lobbies:
                    error = 'Lobby not found or already started.'
                else:
                    lobby_id = lobbies[0]['id']
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
    uid      = session.get('user_id')
    token    = session.get('access_token')
    is_host  = session.get('is_host', False)
    lobby_id = session.get('lobby_id', '')
    players  = [session.get('username', 'Guest')]
    scenario = 'Mord im Orient-Express'
    friends_list = []

    if SB_OK and uid != 'demo' and lobby_id:
        lb = sb_get('lobbies', f'id=eq.{lobby_id}&select=scenario,status', token) or []
        if lb:
            scenario = lb[0].get('scenario', scenario)
            if lb[0].get('status') == 'playing':
                return redirect(url_for('game', code=code))
        lp = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=user_id', token) or []
        pids = [r['user_id'] for r in lp]
        if pids:
            pm = profiles_by_ids(pids, token)
            players = [pm.get(pid,'?') for pid in pids]
        # Get friends for invite (host only)
        if is_host:
            acc = sb_get('friendships', f'user_id=eq.{uid}&status=eq.accepted&select=friend_id', token) or []
            fids = [r['friend_id'] for r in acc]
            # Exclude already in lobby
            fids = [f for f in fids if f not in pids]
            if fids:
                pm2 = profiles_by_ids(fids, token)
                friends_list = [{'id': fid, 'name': pm2.get(fid,'?')} for fid in fids]

    return render_template('lobby.html',
        code=code, players=players, is_host=is_host,
        lobby_id=lobby_id, scenario=scenario, friends_list=friends_list)

@app.route('/lobby/<code>/start', methods=['POST'])
@login_required
def lobby_start(code):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    if SB_OK and uid != 'demo' and lobby_id:
        lb = sb_get('lobbies', f'id=eq.{lobby_id}&select=host_id', token) or []
        if lb and lb[0]['host_id'] == uid:
            sb_patch('lobbies', f'id=eq.{lobby_id}', {'status': 'playing'}, token)
    # Host goes to setup, others go to game_play via polling
    return redirect(url_for('game_setup', code=code))

@app.route('/lobby/<code>/invite/<friend_id>', methods=['POST'])
@login_required
def lobby_invite(code, friend_id):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    if SB_OK and uid != 'demo' and lobby_id:
        sb_post('lobby_invites', {
            'lobby_id': lobby_id,
            'from_user_id': uid,
            'to_user_id': friend_id,
            'code': code,
            'status': 'pending'
        }, token)
    return jsonify({'ok': True})

# ── API: poll lobby + invites ─────────────────────────────────────────────────
@app.route('/api/lobby/<code>')
@login_required
def api_lobby(code):
    token    = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    if not SB_OK or not lobby_id:
        return jsonify({'players': [session.get('username','Guest')], 'status': 'waiting', 'count': 1})
    try:
        lb      = sb_get('lobbies', f'id=eq.{lobby_id}&select=status', token) or []
        status  = lb[0]['status'] if lb else 'waiting'
        lp      = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=user_id', token) or []
        pids    = [r['user_id'] for r in lp]
        pm      = profiles_by_ids(pids, token) if pids else {}
        players = [pm.get(pid,'?') for pid in pids]
        return jsonify({'players': players, 'status': status, 'count': len(players)})
    except Exception as e:
        return jsonify({'players':[], 'status':'waiting', 'count':0})

@app.route('/api/invites')
@login_required
def api_invites():
    uid   = session.get('user_id')
    token = session.get('access_token')
    if not SB_OK or uid == 'demo':
        return jsonify({'invites': []})
    try:
        rows = sb_get('lobby_invites',
            f'to_user_id=eq.{uid}&status=eq.pending&select=id,code,from_user_id,created_at', token) or []
        if not rows: return jsonify({'invites': []})
        from_ids = list({r['from_user_id'] for r in rows})
        pm = profiles_by_ids(from_ids, token)
        invites = [{
            'id': r['id'],
            'code': r['code'],
            'from': pm.get(r['from_user_id'], '?'),
            'created_at': r['created_at']
        } for r in rows]
        return jsonify({'invites': invites})
    except Exception as e:
        return jsonify({'invites': []})

@app.route('/api/invites/<invite_id>/accept', methods=['POST'])
@login_required
def accept_invite(invite_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        rows = sb_get('lobby_invites', f'id=eq.{invite_id}&to_user_id=eq.{uid}&select=code,lobby_id', token) or []
        if rows:
            sb_patch('lobby_invites', f'id=eq.{invite_id}', {'status': 'accepted'}, token)
            # Join lobby
            lobby_id = rows[0]['lobby_id']
            code     = rows[0]['code']
            existing = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&user_id=eq.{uid}&select=id', token) or []
            if not existing:
                sb_post('lobby_players', {'lobby_id': lobby_id, 'user_id': uid}, token)
            session['game_code'] = code
            session['lobby_id']  = lobby_id
            session['is_host']   = False
            return jsonify({'ok': True, 'code': code})
    return jsonify({'ok': False})

@app.route('/api/invites/<invite_id>/decline', methods=['POST'])
@login_required
def decline_invite(invite_id):
    uid   = session.get('user_id')
    token = session.get('access_token')
    if SB_OK and uid != 'demo':
        sb_patch('lobby_invites', f'id=eq.{invite_id}', {'status': 'declined'}, token)
    return jsonify({'ok': True})

# ── Game ──────────────────────────────────────────────────────────────────────
@app.route('/game/<code>')
@login_required
def game(code):
    return render_template('game.html', code=code,
        username=session.get('username','Guest'),
        scenario=session.get('scenario', 'Mord im Orient-Express'))

# ── Settings ──────────────────────────────────────────────────────────────────
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    uid   = session.get('user_id')
    token = session.get('access_token')
    if request.method == 'POST':
        lang = request.form.get('language', session.get('lang','en'))
        if lang in SUPPORTED_LANGS:
            session['lang'] = lang
        session['settings'] = {
            'sound':         'on' if request.form.get('sound') else 'off',
            'music':         'on' if request.form.get('music') else 'off',
            'notifications': 'on' if request.form.get('notifications') else 'off',
            'language':      lang,
        }
        if SB_OK and uid and uid != 'demo':
            sb_patch('profiles', f'id=eq.{uid}', {'lang': lang}, token)
        return redirect(url_for('settings'))
    s = session.get('settings', {'sound':'on','music':'on','notifications':'on','language': session.get('lang','en')})
    return render_template('settings.html', settings=s)

# ── Game Routes ───────────────────────────────────────────────────────────────

# ── Helper: send event to player(s) ──────────────────────────────────────────
def send_event(game_id, event_type, content, to_player=None, from_player=None, token=None):
    """Insert a game event into the DB."""
    if not SB_OK or not game_id:
        return
    sb_post('game_events', {
        'game_id':     game_id,
        'event_type':  event_type,
        'from_player': from_player,
        'to_player':   to_player,
        'content':     json.dumps(content),
    }, token)

def fire_trigger(trigger, game_id, game_state, assignments, player_ids, lang, token):
    """Fire a game trigger — send tasks + atmosphere messages."""
    from game_engine import get_tasks_for_trigger, get_atmosphere_message

    # Mark trigger done
    done = game_state.get('triggers_fired', [])
    if trigger in done:
        return game_state
    done.append(trigger)
    game_state['triggers_fired'] = done

    # Send tasks
    tasks = get_tasks_for_trigger(trigger, game_state, assignments, player_ids, 'dunkelbach', lang)
    done_tasks = game_state.get('tasks_sent', [])

    for task in tasks:
        tid = task['task_id']
        if tid in done_tasks:
            continue
        done_tasks.append(tid)

        instruction = task['instruction']
        if task.get('what_they_find'):
            instruction += '\n\n📄 ' + task['what_they_find']
        if task.get('clue_revealed'):
            instruction += '\n\n🔍 ' + task['clue_revealed']

        if task.get('broadcast'):
            # Send to all
            send_event(game_id, 'task', {'text': instruction, 'task_id': tid},
                       to_player=None, token=token)
        else:
            # Send privately
            send_event(game_id, 'task', {'text': instruction, 'task_id': tid},
                       to_player=task['recipient_id'], token=token)

    game_state['tasks_sent'] = done_tasks

    # Atmosphere message
    atm = get_atmosphere_message(trigger, lang)
    if atm:
        send_event(game_id, 'atmosphere', {'text': atm}, to_player=None, token=token)

    # Update state in DB
    if SB_OK and game_id:
        sb_patch('game_sessions', f'id=eq.{game_id}', {'state': json.dumps(game_state)}, token)

    return game_state

def rebuild_assignments(game_id, token):
    """Rebuild assignments dict from player_roles table."""
    rows = sb_get('player_roles', f'game_id=eq.{game_id}&select=*', token) or []
    assignments = {}
    for r in rows:
        assignments[r['user_id']] = {
            'role_key':    r['role_key'],
            'role_name':   r['role_key'],
            'is_murderer': r.get('is_murderer', False),
            'is_wildcard': r['role_key'] == 'shadow',
        }
        # Restore extra fields from role_card
        rc = json.loads(r.get('role_card') or '{}')
        if rc.get('knows_murderer_id'):
            assignments[r['user_id']]['knows_murderer_id'] = rc['knows_murderer_id']
    return assignments

# ── Game Setup ────────────────────────────────────────────────────────────────
@app.route('/game/<code>/setup')
@login_required
def game_setup(code):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    lobby_id = session.get('lobby_id', '')
    lang     = session.get('lang', 'de')

    if not SB_OK or not lobby_id:
        return redirect(url_for('game_play', code=code))

    # Check if game already exists for this lobby
    existing = sb_get('game_sessions', f'lobby_id=eq.{lobby_id}&select=id', token) or []
    if existing:
        session['game_id'] = existing[0]['id']
        return redirect(url_for('game_play', code=code))

    # Get all players in lobby
    lp = sb_get('lobby_players', f'lobby_id=eq.{lobby_id}&select=user_id', token) or []
    player_ids = [r['user_id'] for r in lp]

    if not player_ids:
        return redirect(url_for('lobby', code=code))

    # Assign roles — EVERYONE random including host
    from game_engine import assign_roles, get_role_card, get_initial_clues
    assignments = assign_roles('dunkelbach', player_ids, lang)

    # Create game session
    init_state = {
        'triggers_fired': [],
        'tasks_sent':     [],
        'votes':          {},
        'events':         [],
        'elapsed_min':    0,
    }
    gs = sb_post('game_sessions', {
        'lobby_id': lobby_id,
        'scenario': 'dunkelbach',
        'phase':    1,
        'state':    json.dumps(init_state),
    }, token)

    if not gs:
        return redirect(url_for('game_play', code=code))

    game_id = gs[0]['id'] if isinstance(gs, list) else gs.get('id')
    session['game_id'] = game_id

    # Save each player's role
    for pid, assignment in assignments.items():
        rc     = get_role_card(pid, assignments, 'dunkelbach', lang)
        clues  = get_initial_clues(pid, assignments, 'dunkelbach', lang)
        sb_post('player_roles', {
            'game_id':        game_id,
            'user_id':        pid,
            'role_key':       assignment['role_key'],
            'is_murderer':    assignment.get('is_murderer', False),
            'clues_received': json.dumps(clues),
            'actions_taken':  json.dumps([]),
            'role_card':      json.dumps(rc),
        }, token)

    # Fire opening triggers
    gs_state = init_state.copy()
    gs_state = fire_trigger('game_started_5min', game_id, gs_state, assignments, player_ids, lang, token)
    gs_state = fire_trigger('first_10_minutes',  game_id, gs_state, assignments, player_ids, lang, token)

    # Send welcome atmosphere
    send_event(game_id, 'atmosphere',
               {'text': '🕯️ Das Spiel beginnt. Lest eure Rollenkarten. Stellt euch vor.' if lang == 'de'
                else '🕯️ The game begins. Read your role cards. Introduce yourselves.'},
               token=token)

    return redirect(url_for('game_play', code=code))

# ── Game Play ─────────────────────────────────────────────────────────────────
@app.route('/game/<code>/play')
@login_required
def game_play(code):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    game_id  = session.get('game_id', '')
    lang     = session.get('lang', 'de')

    if not SB_OK or not game_id:
        return render_template('game_play.html', code=code,
            username=session.get('username','?'), role_card=None, clues=[],
            phase=1, is_host=False, player_count=0, game_id='')

    my_role = sb_get('player_roles', f'game_id=eq.{game_id}&user_id=eq.{uid}&select=*', token) or []
    role_card = json.loads(my_role[0]['role_card']) if my_role else None
    clues     = json.loads(my_role[0]['clues_received']) if my_role else []

    gs = sb_get('game_sessions', f'id=eq.{game_id}&select=phase,state', token) or []
    phase      = gs[0]['phase'] if gs else 1
    game_state = json.loads(gs[0]['state']) if gs else {}

    # Host = player who created the lobby (not a special role)
    lb       = sb_get('lobbies', f'code=eq.{code}&select=host_id', token) or []
    is_host  = lb and lb[0]['host_id'] == uid

    all_roles    = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id,role_key', token) or []
    player_count = len(all_roles)

    # Check if baron (ghost mode)
    is_baron     = role_card and role_card.get('can_be_ghost', False)
    ghost_active = game_state.get('baron_dead', False)

    return render_template('game_play.html',
        code=code, game_id=game_id,
        username=session.get('username','?'),
        role_card=role_card, clues=clues,
        phase=phase, is_host=is_host,
        player_count=player_count,
        game_state=game_state,
        is_baron=is_baron,
        ghost_active=ghost_active,
        lang=lang)

# ── Trigger: Baron dies ───────────────────────────────────────────────────────
@app.route('/game/<code>/baron-dies', methods=['POST'])
@login_required
def baron_dies(code):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    game_id  = session.get('game_id', '')
    lang     = session.get('lang', 'de')

    if not SB_OK or not game_id:
        return jsonify({'ok': False})

    gs = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
    if not gs: return jsonify({'ok': False})
    state = json.loads(gs[0]['state'])
    if state.get('baron_dead'): return jsonify({'ok': True, 'already': True})

    state['baron_dead'] = True

    all_roles  = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id', token) or []
    player_ids = [r['user_id'] for r in all_roles]
    assignments = rebuild_assignments(game_id, token)

    # Fire death triggers
    state = fire_trigger('baron_dies',            game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('body_discovered',        game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('investigation_begins',   game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('murder_announced',       game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('baron_death_announced',  game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('random_post_murder',     game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('random_after_murder',    game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('investigation_5min',     game_id, state, assignments, player_ids, lang, token)
    state = fire_trigger('first_30min',            game_id, state, assignments, player_ids, lang, token)

    return jsonify({'ok': True})

# ── Trigger: Fire manual trigger ──────────────────────────────────────────────
@app.route('/game/<code>/trigger/<trigger_name>', methods=['POST'])
@login_required
def manual_trigger(code, trigger_name):
    uid      = session.get('user_id')
    token    = session.get('access_token')
    game_id  = session.get('game_id', '')
    lang     = session.get('lang', 'de')

    if not SB_OK or not game_id: return jsonify({'ok': False})

    gs = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
    if not gs: return jsonify({'ok': False})
    state = json.loads(gs[0]['state'])

    all_roles   = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id', token) or []
    player_ids  = [r['user_id'] for r in all_roles]
    assignments = rebuild_assignments(game_id, token)

    state = fire_trigger(trigger_name, game_id, state, assignments, player_ids, lang, token)
    return jsonify({'ok': True})

# ── Vote ──────────────────────────────────────────────────────────────────────
@app.route('/game/<code>/vote', methods=['POST'])
@login_required
def game_vote(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')
    data    = request.get_json() or {}
    accused = data.get('accused_id', '')

    if not SB_OK or not game_id or not accused:
        return jsonify({'ok': False})

    gs    = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
    state = json.loads(gs[0]['state']) if gs else {}
    state.setdefault('votes', {})[uid] = accused
    sb_patch('game_sessions', f'id=eq.{game_id}', {'state': json.dumps(state)}, token)
    return jsonify({'ok': True})

# ── Resolve ───────────────────────────────────────────────────────────────────
@app.route('/game/<code>/resolve')
@login_required
def game_resolve(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')
    lang    = session.get('lang', 'de')

    if not SB_OK or not game_id:
        return redirect(url_for('home'))

    gs = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
    if not gs: return redirect(url_for('home'))
    state = json.loads(gs[0]['state'])
    votes = state.get('votes', {})

    all_roles = sb_get('player_roles', f'game_id=eq.{game_id}&select=*', token) or []
    assignments = {}
    player_names = {}
    for r in all_roles:
        assignments[r['user_id']] = {
            'role_key':   r['role_key'],
            'is_murderer': r.get('is_murderer', False),
            'is_wildcard': r['role_key'] == 'shadow',
        }
        p = sb_get('profiles', f'id=eq.{r["user_id"]}&select=username', token) or []
        player_names[r['user_id']] = p[0]['username'] if p else '?'

    from game_engine import check_win_conditions, get_ending_text
    result        = check_win_conditions(state, assignments, votes, 'dunkelbach')
    murderer_id   = result.get('murderer_id', '')
    murderer_name = player_names.get(murderer_id, '?')
    murderer_role = assignments.get(murderer_id, {}).get('role_key', '?')
    ending        = get_ending_text(result['ending'], murderer_name, 'dunkelbach', lang)
    winners       = result.get('winners', [])
    winner_names  = [player_names.get(w, '?') for w in winners]

    # Save history for all players with full stats
    for r in all_roles:
        pid = r['user_id']
        won = pid in winners
        is_murderer = r.get('is_murderer', False)
        sb_post('game_history', {
            'user_id':        pid,
            'scenario':       'dunkelbach',
            'role':           r['role_key'],
            'result':         'won' if won else 'lost',
            'is_murderer':    is_murderer,
            'murderer_caught': result.get('ending') in ('murderer_caught','perfect_solve'),
            'players_count':  len(all_roles),
        }, token)

    # Build role reveals
    role_reveals = []
    for r in all_roles:
        rc = json.loads(r.get('role_card') or '{}')
        role_reveals.append({
            'username':    player_names.get(r['user_id'], '?'),
            'role_name':   rc.get('role_name', r['role_key']),
            'was_murderer': r.get('is_murderer', False),
            'secret':      rc.get('secret', ''),
            'won':         r['user_id'] in winners,
        })

    return render_template('game_resolve.html',
        code=code, ending=ending,
        winner_names=winner_names, role_reveals=role_reveals,
        murderer_name=murderer_name, murderer_role=murderer_role)

# ── API: Events poll ──────────────────────────────────────────────────────────
@app.route('/api/game/<code>/events')
@login_required
def api_game_events(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')
    since   = request.args.get('since', '1970-01-01T00:00:00')

    if not SB_OK or not game_id:
        return jsonify({'events': [], 'phase': 1})

    events = sb_get('game_events',
        f'game_id=eq.{game_id}&created_at=gt.{since}&order=created_at.asc&select=*',
        token) or []

    # Filter: public events + private events for this player
    my_events = [e for e in events
                 if e.get('to_player') is None or e.get('to_player') == uid]

    gs    = sb_get('game_sessions', f'id=eq.{game_id}&select=phase,state', token) or []
    phase = gs[0]['phase'] if gs else 1
    state = json.loads(gs[0]['state']) if gs else {}

    return jsonify({
        'events':      my_events,
        'phase':       phase,
        'baron_dead':  state.get('baron_dead', False),
        'will_stolen': state.get('will_stolen', False),
    })

# ── API: Clues ────────────────────────────────────────────────────────────────
@app.route('/api/game/<code>/clues')
@login_required
def api_game_clues(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')

    if not SB_OK or not game_id:
        return jsonify({'clues': []})

    my_role = sb_get('player_roles', f'game_id=eq.{game_id}&user_id=eq.{uid}&select=clues_received', token) or []
    clues   = json.loads(my_role[0]['clues_received']) if my_role else []
    return jsonify({'clues': clues})

# ── API: Use ability ──────────────────────────────────────────────────────────
@app.route('/api/game/<code>/use-ability', methods=['POST'])
@login_required
def use_ability(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')
    lang    = session.get('lang', 'de')
    data    = request.get_json() or {}
    ability = data.get('ability')

    if not SB_OK or not game_id: return jsonify({'ok': False})

    my_role = sb_get('player_roles', f'game_id=eq.{game_id}&user_id=eq.{uid}&select=*', token) or []
    if not my_role: return jsonify({'ok': False})

    role_key      = my_role[0]['role_key']
    actions_taken = json.loads(my_role[0]['actions_taken'] or '[]')

    # Each ability can only be used once
    ability_key = f'ability_{ability}'
    if ability_key in actions_taken:
        return jsonify({'ok': False, 'error': 'already_used'})

    actions_taken.append(ability_key)
    sb_patch('player_roles', f'game_id=eq.{game_id}&user_id=eq.{uid}',
             {'actions_taken': json.dumps(actions_taken)}, token)

    result = {'ok': True, 'message': ''}

    # Handle specific abilities
    if ability == 'open_letter' and role_key == 'niece':
        msg = 'Du hast den Brief geöffnet. Der Inhalt verändert alles.' if lang == 'de' else 'You opened the letter. The contents change everything.'
        result['message'] = msg
        send_event(game_id, 'clue_revealed',
                   {'clue': 'sealed_letter', 'by': uid,
                    'text': 'Constanze hat den versiegelten Brief geöffnet.' if lang == 'de'
                            else 'Constanze opened the sealed letter.'},
                   token=token)

    elif ability == 'steal_will' and role_key == 'shadow':
        gs    = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
        state = json.loads(gs[0]['state']) if gs else {}
        if state.get('will_location_known'):
            state['will_stolen'] = True
            sb_patch('game_sessions', f'id=eq.{game_id}', {'state': json.dumps(state)}, token)
            result['message'] = 'Testament gestohlen!' if lang == 'de' else 'Will stolen!'
            send_event(game_id, 'atmosphere',
                       {'text': '📜 Das Testament ist verschwunden.' if lang == 'de'
                                else '📜 The will has disappeared.'},
                       token=token)
        else:
            return jsonify({'ok': False, 'error': 'will_location_unknown'})

    elif ability == 'call_interrogation' and role_key == 'detective':
        result['message'] = 'Verhör ausgerufen.' if lang == 'de' else 'Interrogation called.'
        send_event(game_id, 'interrogation',
                   {'text': '🔦 Inspektor Wahl ruft ein offizielles Verhör ein!' if lang == 'de'
                            else '🔦 Inspector Wahl calls an official interrogation!'},
                   token=token)
        # Fire relevant trigger
        all_roles   = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id', token) or []
        player_ids  = [r['user_id'] for r in all_roles]
        assignments = rebuild_assignments(game_id, token)
        gs_data     = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
        state       = json.loads(gs_data[0]['state']) if gs_data else {}
        fire_trigger('someone_gets_close_to_truth', game_id, state, assignments, player_ids, lang, token)

    elif ability == 'diagnose' and role_key == 'doctor':
        diagnosis = data.get('diagnosis', '')
        result['message'] = f'Diagnose: {diagnosis}'
        send_event(game_id, 'announcement',
                   {'text': f'🩺 Dr. Voss: "{diagnosis}"'},
                   token=token)
        # Fire cook_under_pressure if digitalis mentioned
        if 'digital' in diagnosis.lower() or 'gift' in diagnosis.lower() or 'poison' in diagnosis.lower():
            all_roles   = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id', token) or []
            player_ids  = [r['user_id'] for r in all_roles]
            assignments = rebuild_assignments(game_id, token)
            gs_data     = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
            state       = json.loads(gs_data[0]['state']) if gs_data else {}
            fire_trigger('cook_under_pressure', game_id, state, assignments, player_ids, lang, token)
            fire_trigger('doctor_announces_cause', game_id, state, assignments, player_ids, lang, token)

    elif ability == 'reveal_truth' and role_key == 'cook':
        gs_data     = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
        state       = json.loads(gs_data[0]['state']) if gs_data else {}
        rc          = json.loads(my_role[0].get('role_card') or '{}')
        hired_by    = rc.get('hired_by', '?')
        msg = f'Rosa gesteht: Sie wurde von {hired_by} beauftragt.' if lang == 'de' else f'Rosa confesses: She was hired by {hired_by}.'
        result['message'] = msg
        send_event(game_id, 'confession', {'text': msg}, token=token)

    elif ability == 'ghost_whisper':
        # Baron whispers a clue to a specific player
        target_id = data.get('target_id')
        clue_text = data.get('clue_text', '')
        if target_id and clue_text:
            send_event(game_id, 'ghost_clue',
                       {'text': f'👻 Der Geist flüstert: {clue_text}' if lang == 'de'
                                else f'👻 The ghost whispers: {clue_text}',
                        'from_ghost': True},
                       to_player=target_id, from_player=uid, token=token)
            result['message'] = 'Hinweis geflüstert.' if lang == 'de' else 'Clue whispered.'

    elif ability == 'baron_last_toast':
        # Baron proposes the last toast — fires murderer task
        send_event(game_id, 'announcement',
                   {'text': '🥂 Baron erhebt sein Glas: "Auf die Wahrheit — sie kommt immer ans Licht."' if lang == 'de'
                            else '🥂 The Baron raises his glass: "To the truth — it always comes to light."'},
                   token=token)
        all_roles   = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id', token) or []
        player_ids  = [r['user_id'] for r in all_roles]
        assignments = rebuild_assignments(game_id, token)
        gs_data     = sb_get('game_sessions', f'id=eq.{game_id}&select=state', token) or []
        state       = json.loads(gs_data[0]['state']) if gs_data else {}
        fire_trigger('baron_proposes_toast', game_id, state, assignments, player_ids, lang, token)
        fire_trigger('baron_death_minus_5min', game_id, state, assignments, player_ids, lang, token)
        result['message'] = 'Toast ausgerufen.' if lang == 'de' else 'Toast proposed.'

    return jsonify(result)

# ── API: Players list ─────────────────────────────────────────────────────────
@app.route('/api/game/<code>/players')
@login_required
def api_game_players(code):
    uid     = session.get('user_id')
    token   = session.get('access_token')
    game_id = session.get('game_id', '')

    if not SB_OK or not game_id:
        return jsonify({'players': []})

    rows = sb_get('player_roles', f'game_id=eq.{game_id}&select=user_id,role_key', token) or []
    player_names = {}
    for r in rows:
        p = sb_get('profiles', f'id=eq.{r["user_id"]}&select=username', token) or []
        player_names[r['user_id']] = p[0]['username'] if p else '?'

    players = [{'id': r['user_id'], 'name': player_names[r['user_id']]} for r in rows]
    return jsonify({'players': players})


@app.route('/api/owned-scenarios')
@login_required
def api_owned_scenarios():
    uid   = session.get('user_id')
    token = session.get('access_token')
    owned = ['dunkelbach']  # always free
    if SB_OK and uid and uid != 'demo':
        rows = sb_get('purchases', f'user_id=eq.{uid}&select=scenario', token) or []
        for r in rows:
            owned.append(r['scenario'])
    return jsonify({'scenarios': owned})

# ── Error handlers ────────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    lang = session.get('lang', 'en')
    return render_template('404.html', t=get_t(lang), lang=lang,
                           supported_langs=SUPPORTED_LANGS,
                           config={'SUPABASE_URL': SB_URL, 'SUPABASE_KEY': SB_KEY}), 404

@app.errorhandler(500)
def server_error(e):
    lang = session.get('lang', 'en')
    return render_template('500.html', t=get_t(lang), lang=lang,
                           supported_langs=SUPPORTED_LANGS,
                           config={'SUPABASE_URL': SB_URL, 'SUPABASE_KEY': SB_KEY}), 500

@app.route('/offline')
def offline():
    return render_template('offline.html')

@app.route('/static/sw.js')
def sw():
    return app.send_static_file('sw.js'), 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'\n  Krimi Dinner')
    print(f'  Supabase: {"connected" if SB_OK else "demo mode"}')
    print(f'  http://localhost:{port}\n')
    app.run(debug=False, host='0.0.0.0', port=port)
