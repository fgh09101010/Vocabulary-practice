<div align="center">

# 🚀 極致單字卡 (Ultimate Flashcards)

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Ffgh09101010%2FVocabulary-practice&label=VIEWERS&countColor=%234F46E5&style=flat-square)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)
![Energy](https://img.shields.io/badge/Energy-100%25-orange?style=flat-square)
![Coffee](https://img.shields.io/badge/Powered%20by-Coffee-brown?style=flat-square&logo=buy-me-a-coffee)
![Love](https://img.shields.io/badge/Made%20with-Love-red?style=flat-square)

**以純前端技術打造的現代化單字學習網頁應用程式**

## [✨ 立即體驗](https://fgh09101010.github.io/Vocabulary-practice/) 

</div>

---

## 📖 專案簡介
這是一個專為大學生設計的單字練習工具，結合了視覺、聽覺與 AI 輔助記憶。本專案特別實作了隱形訪客追蹤系統，能透過 Google Sheets 紀錄並分析學習者的行為數據，實現數據驅動的學習優化。

### ✨ 核心特色功能
- **📊 彈性題庫設定**：支援 CSV 讀取，可自由選擇抽題數量、循序練習或隨機亂序排列。
- **📖 結合 PDF 閱讀**：動態偵測並關聯課文 PDF，實現「先閱讀、後測驗」的完整學習閉環。
- **🖼️ 動態維基配圖**：即時串接 Wikipedia API 抓取單字對應圖片，強化圖像連結記憶。
- **🔊 原生語音朗讀**：內建 TTS 系統，提供標準美式發音，支援離線朗讀。
- **🤖 AI 記憶輔助**：練習結束後自動生成專屬 ChatGPT 指令，讓 AI 為您量身打造諧音記憶法。
- **📱 響應式 UI**：採用現代化 Glassmorphism 毛玻璃設計，完美適配手機與電腦螢幕。

---

## 📂 專案架構與運行

### 檔案結構
```text
/
├── index.html       # 主應用程式 (單字卡)
├── dashboard.html   # 管理員數據看板 (KPI 與圖表動態分析)
├── data/            # 題庫目錄 (CSV 格式)
└── pdf/             # 關聯文章目錄 (PDF 格式)
````

### 如何運行

1.  使用 VS Code 開啟此專案資料夾。
2.  啟動 **Live Server** 插件運行 `index.html`。
3.  *重要備註：由於瀏覽器 CORS 安全限制，請勿直接以檔案路徑開啟，否則無法讀取 CSV 資料。*

-----

## 🛠️ 技術棧 (Tech Stack)

* **前端**：HTML5, CSS3 (CSS Variables, Flexbox), Vanilla JavaScript (ES6+).
* **第三方套件**：
  * [PapaParse](https://www.papaparse.com/) (用於解析 CSV 檔案)
  * [FontAwesome](https://fontawesome.com/) (向量圖示)
* **外部 API**：
  * Wikipedia Action API (抓取圖片)

---

## 👨‍💻 開發者資訊

<div align="center">

<table style="border: none; border-collapse: collapse;">
  <tr>
    <td align="center" width="150px" style="border: none;">
      <a href="https://github.com/fgh09101010">
        <img src="https://github.com/fgh09101010.png" width="120px;" style="border-radius: 50%; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="fgh09101010"/><br />
        <br />
        <b>fgh09101010</b>
      </a>
    </td>
    <td align="left" style="border: none; vertical-align: top; padding-left: 20px;">
      <h3>🎓 大學四年級學生 | 數據開發者</h3>
      <p>熱衷於將日常需求<b>自動化</b>與<b>遊戲化</b>。專注於 Web 前端技術、Python 數據分析與機器學習模型研究。目前正致力於開發能提升學習效率的數位工具。</p>
      <div style="margin-top: 10px;">
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JS" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Google_Apps_Script-4285F4?style=flat-square&logo=google&logoColor=white" alt="GAS" />
        <img src="https://img.shields.io/badge/Status-Actively_Learning-brightgreen?style=flat-square" alt="Status" />
      </div>
      <p style="font-size: 0.9em; color: #555; margin-top: 15px;">
        📫 聯絡我：<a href="mailto:fgh09101010@gmail.com">透過電子郵件交流</a>
      </p>
    </td>
  </tr>
</table>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=fgh09101010&show_icons=true&theme=radical&cache_seconds=1800" alt="fgh09101010's GitHub Stats" />

  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=fgh09101010&layout=compact&theme=radical&cache_seconds=1800" alt="fgh09101010's Top Langs" />
</div>

---
