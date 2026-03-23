/**
 * KrimiSound v2 — Deep atmospheric noir audio
 * Continuous looping buffer — never breaks or cuts out.
 */
const KrimiSound = (() => {
  let ctx = null;
  let masterGain = null;
  let musicGain = null;
  let sfxGain = null;
  let musicSource = null;
  let musicBuffer = null;
  let musicPlaying = false;

  function getCtx() {
    if (!ctx) {
      ctx = new (window.AudioContext || window.webkitAudioContext)();
      masterGain = ctx.createGain();
      masterGain.gain.setValueAtTime(1, ctx.currentTime);
      masterGain.connect(ctx.destination);
      musicGain = ctx.createGain();
      musicGain.gain.setValueAtTime(0, ctx.currentTime);
      musicGain.connect(masterGain);
      sfxGain = ctx.createGain();
      sfxGain.gain.setValueAtTime(0.45, ctx.currentTime);
      sfxGain.connect(masterGain);
    }
    return ctx;
  }

  // Build a 40-second stereo buffer of deep noir ambient drone.
  // Low sine waves in A-minor + filtered noise texture.
  function buildBuffer() {
    const c  = getCtx();
    const sr = c.sampleRate;
    const dur = 40;
    const buf = c.createBuffer(2, sr * dur, sr);

    const leftFreqs  = [55, 82.4, 110, 130.8];
    const rightFreqs = [54.6, 82.1, 110.4, 131.2];

    for (let ch = 0; ch < 2; ch++) {
      const data  = buf.getChannelData(ch);
      const freqs = ch === 0 ? leftFreqs : rightFreqs;

      // LPF state for noise
      let prev = 0;

      for (let i = 0; i < sr * dur; i++) {
        const t = i / sr;
        let s = 0;

        // Layered sine drones
        freqs.forEach((f, idx) => {
          const baseAmp = 0.16 / (idx + 1);
          // Very slow LFO breathing (0.05–0.12 Hz)
          const lfo = 1 + 0.25 * Math.sin(2 * Math.PI * (0.05 + idx * 0.015) * t);
          s += baseAmp * lfo * Math.sin(2 * Math.PI * f * t);
        });

        // Deep sub (27.5 Hz, very soft)
        s += 0.05 * Math.sin(2 * Math.PI * 27.5 * t);

        // Lowpass filtered noise (wind-like, very quiet)
        const noise = Math.random() * 2 - 1;
        prev = 0.97 * prev + 0.03 * noise; // simple RC lowpass
        s += prev * 0.07;

        // Fade in/out at loop boundaries (2 s each end)
        const fade = sr * 2;
        if (i < fade)              s *= i / fade;
        if (i > sr * dur - fade)   s *= (sr * dur - i) / fade;

        data[i] = Math.max(-1, Math.min(1, s));
      }
    }
    return buf;
  }

  function startMusic() {
    if (musicPlaying) return;
    if (localStorage.getItem('music') === 'off') return;
    try {
      const c = getCtx();
      if (c.state === 'suspended') c.resume();
      if (!musicBuffer) musicBuffer = buildBuffer();

      musicSource        = c.createBufferSource();
      musicSource.buffer = musicBuffer;
      musicSource.loop   = true; // ← seamless loop, never stops
      musicSource.connect(musicGain);
      musicSource.start(0);

      // Gentle fade-in
      musicGain.gain.cancelScheduledValues(c.currentTime);
      musicGain.gain.setValueAtTime(0, c.currentTime);
      musicGain.gain.linearRampToValueAtTime(0.5, c.currentTime + 4);

      musicPlaying = true;
    } catch(e) { console.warn('[KrimiSound] music error:', e); }
  }

  function stopMusic() {
    if (!musicPlaying || !musicSource) return;
    try {
      const c = getCtx();
      musicGain.gain.linearRampToValueAtTime(0, c.currentTime + 2);
      const src = musicSource;
      setTimeout(() => { try { src.stop(); } catch(e){} }, 2200);
      musicPlaying = false;
      musicSource  = null;
    } catch(e){}
  }

  // Soft dull thud click — lowpass-filtered noise burst
  function playClick() {
    if (localStorage.getItem('sfx') === 'off') return;
    try {
      const c = getCtx();
      if (c.state === 'suspended') c.resume();

      const len  = Math.floor(c.sampleRate * 0.055);
      const nb   = c.createBuffer(1, len, c.sampleRate);
      const d    = nb.getChannelData(0);
      for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;

      const src = c.createBufferSource();
      src.buffer = nb;

      const filter = c.createBiquadFilter();
      filter.type  = 'lowpass';
      filter.frequency.setValueAtTime(220, c.currentTime);
      filter.Q.setValueAtTime(0.4, c.currentTime);

      const g = c.createGain();
      g.gain.setValueAtTime(0.3, c.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001, c.currentTime + 0.055);

      src.connect(filter);
      filter.connect(g);
      g.connect(sfxGain);
      src.start();
      src.stop(c.currentTime + 0.06);
    } catch(e){}
  }

  function init() {
    // Start on first interaction
    const once = () => {
      startMusic();
      document.removeEventListener('click',   once);
      document.removeEventListener('keydown', once);
    };
    document.addEventListener('click',   once, { passive: true });
    document.addEventListener('keydown', once, { passive: true });

    // Click sounds on interactive elements
    document.addEventListener('click', (e) => {
      if (e.target.closest('a, button, .btn, label, .toggle-slider, .action-card, .nav-link, .bottom-nav-item')) {
        playClick();
      }
    }, { passive: true });
  }

  return { init, playClick, startMusic, stopMusic,
           setSfx:   (on) => localStorage.setItem('sfx',   on ? 'on' : 'off'),
           setMusic: (on) => { localStorage.setItem('music', on ? 'on' : 'off'); on ? startMusic() : stopMusic(); } };
})();

document.addEventListener('DOMContentLoaded', KrimiSound.init);
