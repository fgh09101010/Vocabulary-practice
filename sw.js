// 簡單的 Service Worker 讓網頁符合安裝條件
self.addEventListener('install', (e) => {
  console.log('[Service Worker] Install');
});

self.addEventListener('fetch', (e) => {
  // 即使不快取任何檔案，也必須有 fetch 事件監聽
  e.respondWith(fetch(e.request));
});