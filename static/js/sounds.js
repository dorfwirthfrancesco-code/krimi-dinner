// ── Krimi Dinner Sound System ─────────────────────────────────────────────────
// Atmospheric background music + UI click sounds using Web Audio API
// No external files needed

const KrimiSound = (() => {
  let ctx = null;
  let musicGain = null;
  let musicNodes = [];
  let musicPlaying = false;
  let sfxEnabled = true;
  let musicEnabled = true;

  function getCtx() {
    if (!ctx) {
      ctx = new (window.AudioContext || window.webkitAudioContext)();
      musicGain = ctx.createGain();
      musicGain.gain.setValueAtTime(0.08, ctx.currentTime);
      musicGain.connect(ctx.destination);
    }
    return ctx;
  }

  // ── Click sound: short soft tap ──────────────────────────────────────────
  function playClick() {
    if (!sfxEnabled) return;
    try {
      const c = getCtx();
      const osc  = c.createOscillator();
      const gain = c.createGain();
      osc.connect(gain);
      gain.connect(c.destination);
      osc.type = 'sine';
      osc.frequency.setValueAtTime(880, c.currentTime);
      osc.frequency.exponentialRampToValueAtTime(440, c.currentTime + 0.06);
      gain.gain.setValueAtTime(0.12, c.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, c.currentTime + 0.08);
      osc.start(c.currentTime);
      osc.stop(c.currentTime + 0.08);
    } catch(e) {}
  }

  // ── Atmospheric noir background music ────────────────────────────────────
  // Slow ambient drone with subtle movement
  function createDroneNote(freq, detune, startTime, duration) {
    const c = getCtx();
    const osc  = c.createOscillator();
    const gain = c.createGain();
    osc.connect(gain);
    gain.connect(musicGain);
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, startTime);
    osc.detune.setValueAtTime(detune, startTime);
    gain.gain.setValueAtTime(0, startTime);
    gain.gain.linearRampToValueAtTime(1, startTime + 2);
    gain.gain.setValueAtTime(1, startTime + duration - 2);
    gain.gain.linearRampToValueAtTime(0, startTime + duration);
    osc.start(startTime);
    osc.stop(startTime + duration);
    return { osc, gain };
  }

  function createFilteredNoise(startTime, duration) {
    const c = getCtx();
    const bufferSize = c.sampleRate * 2;
    const buffer = c.createBuffer(1, bufferSize, c.sampleRate);
    const data   = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

    const source = c.createBufferSource();
    source.buffer = buffer;
    source.loop   = true;

    const filter = c.createBiquadFilter();
    filter.type  = 'lowpass';
    filter.frequency.setValueAtTime(120, startTime);

    const gain = c.createGain();
    gain.gain.setValueAtTime(0, startTime);
    gain.gain.linearRampToValueAtTime(0.15, startTime + 3);
    gain.gain.setValueAtTime(0.15, startTime + duration - 3);
    gain.gain.linearRampToValueAtTime(0, startTime + duration);

    source.connect(filter);
    filter.connect(gain);
    gain.connect(musicGain);
    source.start(startTime);
    source.stop(startTime + duration);
    return source;
  }

  function scheduleMusicLoop() {
    if (!musicPlaying || !musicEnabled) return;
    const c   = getCtx();
    const now = c.currentTime;
    const dur = 24; // seconds per loop

    // Minor chord drone: Am feel (A2, E3, A3, C4)
    const notes = [
      { freq: 110,  detune: 0   },  // A2
      { freq: 165,  detune: -8  },  // E3
      { freq: 220,  detune: 5   },  // A3
      { freq: 261,  detune: -5  },  // C4
      { freq: 82.4, detune: 0   },  // E2
    ];

    notes.forEach(n => createDroneNote(n.freq, n.detune, now, dur));
    createFilteredNoise(now, dur);

    // Schedule next loop
    setTimeout(scheduleMusicLoop, (dur - 2) * 1000);
  }

  function startMusic() {
    if (musicPlaying || !musicEnabled) return;
    try {
      getCtx();
      if (ctx.state === 'suspended') ctx.resume();
      musicPlaying = true;
      scheduleMusicLoop();
    } catch(e) {}
  }

  function stopMusic() {
    musicPlaying = false;
    if (musicGain) {
      musicGain.gain.linearRampToValueAtTime(0, getCtx().currentTime + 1.5);
    }
  }

  function setSfx(on)   { sfxEnabled   = on; }
  function setMusic(on) {
    musicEnabled = on;
    if (on)  startMusic();
    else     stopMusic();
  }

  // Load preferences
  function loadPrefs() {
    sfxEnabled   = localStorage.getItem('sfx')   !== 'off';
    musicEnabled = localStorage.getItem('music') !== 'off';
  }

  // ── Init: start music + attach click sounds on first user interaction ──
  function init() {
    loadPrefs();
    const startOnce = () => {
      if (musicEnabled) startMusic();
      document.removeEventListener('click', startOnce);
      document.removeEventListener('keydown', startOnce);
    };
    document.addEventListener('click',   startOnce);
    document.addEventListener('keydown', startOnce);

    // Attach click sounds to all nav links and buttons
    document.addEventListener('click', (e) => {
      const el = e.target.closest('a.nav-link, a.bottom-nav-item, .btn, button, a.btn');
      if (el) playClick();
    });
  }

  return { init, playClick, startMusic, stopMusic, setSfx, setMusic };
})();

document.addEventListener('DOMContentLoaded', KrimiSound.init);
