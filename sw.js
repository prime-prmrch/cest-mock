/**
 * Service Worker for Cambridge English Skills Simulator (CEST Mock)
 * Provides progressive offline caching for core application assets and on-demand audio caching.
 */

const STATIC_CACHE = 'cest-mock-static-v1';
const AUDIO_CACHE = 'cest-mock-audio-v1';

const STATIC_ASSETS = [
  './',
  './index.html',
  './test.html',
  './css/style.css',
  './js/engine.js',
  './js/scoring.js',
  './manifest.json',
  './icons/icon.svg',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './data/index.json',
  './mock_test_1/test_data.json',
  './mock_test_2/test_data.json',
  './mock_test_3/test_data.json'
];

// Install: pre-cache application shell and core data
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activate: clean up outdated caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== STATIC_CACHE && key !== AUDIO_CACHE)
            .map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Strategy dispatcher
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Non-GET requests pass through directly
  if (request.method !== 'GET') {
    return;
  }

  // Audio assets: Cache-first with network fallback and dynamic caching
  if (url.pathname.endsWith('.mp3')) {
    event.respondWith(
      caches.open(AUDIO_CACHE).then(async (cache) => {
        const cached = await cache.match(url.pathname, { ignoreSearch: true });
        if (cached) {
          return cached;
        }

        try {
          const networkResponse = await fetch(request);
          if (networkResponse && (networkResponse.status === 200 || networkResponse.status === 206)) {
            cache.put(url.pathname, networkResponse.clone());
          }
          return networkResponse;
        } catch (error) {
          if (cached) return cached;
          return new Response('Audio file unavailable offline.', { status: 503, statusText: 'Offline' });
        }
      })
    );
    return;
  }

  // App shell & Data: Cache-first with background network update (Stale-While-Revalidate)
  event.respondWith(
    caches.match(request, { ignoreSearch: false }).then((cachedResponse) => {
      const fetchPromise = fetch(request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(STATIC_CACHE).then((cache) => {
            cache.put(request, responseToCache);
          });
        }
        return networkResponse;
      }).catch((err) => {
        return cachedResponse;
      });

      return cachedResponse || fetchPromise;
    })
  );
});

// Message listener for batch pre-caching audio on demand
self.addEventListener('message', (event) => {
  if (event.data && event.data.action === 'CACHE_AUDIO_URLS') {
    const urls = event.data.urls || [];
    event.waitUntil(
      caches.open(AUDIO_CACHE).then(async (cache) => {
        for (const audioUrl of urls) {
          try {
            const pathKey = new URL(audioUrl, self.location.href).pathname;
            const existing = await cache.match(pathKey);
            if (!existing) {
              const res = await fetch(audioUrl);
              if (res.ok) {
                await cache.put(pathKey, res);
              }
            }
          } catch (e) {
            console.warn('[SW] Could not precache audio:', audioUrl, e);
          }
        }
      })
    );
  }
});
