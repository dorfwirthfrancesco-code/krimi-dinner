// Krimi Dinner Service Worker v1
const CACHE = 'krimi-v1';
const STATIC = [
  '/',
  '/static/css/style.css',
  '/static/js/sounds.js',
  '/static/manifest.json',
  '/offline',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(STATIC)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  // Only handle GET requests
  if (e.request.method !== 'GET') return;
  
  const url = new URL(e.request.url);
  
  // Network first for HTML pages (always fresh content)
  if (e.request.headers.get('accept')?.includes('text/html')) {
    e.respondWith(
      fetch(e.request)
        .catch(() => caches.match('/offline'))
    );
    return;
  }

  // Cache first for static assets
  if (url.pathname.startsWith('/static/')) {
    e.respondWith(
      caches.match(e.request).then(cached => {
        if (cached) return cached;
        return fetch(e.request).then(res => {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
          return res;
        });
      })
    );
    return;
  }

  // Network only for everything else
  e.respondWith(fetch(e.request).catch(() => caches.match('/offline')));
});
