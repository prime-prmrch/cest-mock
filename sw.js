/**
 * Service Worker for Cambridge English Skills Simulator (CEST Mock)
 * Provides progressive offline caching for core application assets and background audio pre-caching.
 */

const STATIC_CACHE = 'cest-mock-static-v8';
const AUDIO_CACHE = 'cest-mock-audio-v2';

const STATIC_ASSETS = [
  './',
  './index.html',
  './test.html',
  './css/style.css',
  './js/engine.js',
  './manifest.json',
  './icons/icon.svg',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './data/bank.json'
];

const ALL_AUDIO_TRACKS = [
  './audio/task1_v1.mp3', './audio/task1_v2.mp3', './audio/task1_v3.mp3', './audio/task1_v4.mp3', './audio/task1_v5.mp3',
  './audio/task2_v1.mp3', './audio/task2_v2.mp3', './audio/task2_v3.mp3', './audio/task2_v4.mp3', './audio/task2_v5.mp3',
  './audio/task3_v1.mp3', './audio/task3_v2.mp3', './audio/task3_v3.mp3', './audio/task3_v4.mp3', './audio/task3_v5.mp3',
  './audio/task4_v1.mp3', './audio/task4_v2.mp3', './audio/task4_v3.mp3', './audio/task4_v4.mp3', './audio/task4_v5.mp3',
  './audio/task5_v1.mp3', './audio/task5_v2.mp3', './audio/task5_v3.mp3', './audio/task5_v4.mp3', './audio/task5_v5.mp3',
  './audio/task6_v1.mp3', './audio/task6_v2.mp3', './audio/task6_v3.mp3', './audio/task6_v4.mp3', './audio/task6_v5.mp3'
];

// Install: pre-cache application shell and core data, then queue background audio cache
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }).then(() => {
      // Background non-blocking audio pre-cache
      caches.open(AUDIO_CACHE).then(async (audioCache) => {
        for (const track of ALL_AUDIO_TRACKS) {
          try {
            const match = await audioCache.match(track);
            if (!match) {
              const resp = await fetch(track);
              if (resp.ok) await audioCache.put(track, resp);
            }
          } catch (e) {
            console.warn('[SW] Could not pre-cache audio track:', track, e);
          }
        }
      });
      return self.skipWaiting();
    })
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
        // Try multiple URL path match strategies (absolute and relative)
        const cached = (await cache.match(url.pathname, { ignoreSearch: true })) ||
                       (await cache.match(request.url, { ignoreSearch: true })) ||
                       (await cache.match(`.${url.pathname.substring(url.pathname.lastIndexOf('/audio/'))}`, { ignoreSearch: true }));
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

  // App shell, documents, scripts, styles, data: Network-First with offline cache fallback
  event.respondWith(
    fetch(request).then((networkResponse) => {
      if (networkResponse && networkResponse.status === 200) {
        const responseToCache = networkResponse.clone();
        caches.open(STATIC_CACHE).then((cache) => {
          cache.put(request, responseToCache);
        });
      }
      return networkResponse;
    }).catch(() => {
      return caches.match(request, { ignoreSearch: false });
    })
  );
});
