# 🚀 PythonFlask 快速入門指南 🌟

Python Flask 入門指南：帶你掌握這款輕量級且強大的網頁框架工具！開發網頁不再是難事 👍

---

## 🛠️ 開發環境優化：讓 Code Runner 輸出到 Terminal

為了讓 GitHub Copilot 能夠更好地協助我們（因為 Copilot 雖然有 `#terminalLastCommand`，但無法直接讀取【輸出】視窗的訊息），我們建議將 `code-runner.runInTerminal` 設定為開啟狀態。

這樣一來，所有的程式執行結果都會直接呈現在終端機，**方便分析錯誤，再也不用手動複製貼上，省時又省力！** ✨

### 📌 設定預設終端機
請在 VS Code 設定中確認你的 `terminal.integrated.defaultProfile`：
- `Command Prompt` (即 `cmd.exe`) 💻
- `PowerShell` (建議使用最新版本，如 `PowerShell 7.5.x`) ⚡

---

## 📦 環境管理：使用 uv

我們推薦使用高效的 `uv` 來管理 Python 環境，讓套件安裝與環境隔離變得更加簡單！
🔗 [深入瞭解如何使用 uv 管理 Python 環境](https://github.com/chiisen/uv) 📖

---

## 🔥 快速啟動 Flask 套件

你可以直接使用 `uv` 執行 Flask 應用程式，無需複雜配置：

```shell
# 執行 Flask Hello World
uv run --with Flask .\src\flask\flask_hello.py
```

### 🌐 瀏覽測試
1. 點擊開啟程式碼：[flask_hello.py](./src/flask/flask_hello.py) 📄
2. 在瀏覽器輸入：[http://127.0.0.1:5000](http://127.0.0.1:5000) 🌍
3. **小技巧**：如果拿掉 `flask_hello.py` 中的 `port=5000` 參數，你可以透過 uv 指令彈性指定埠號：
   ```shell
   uv run --with Flask .\src\flask\flask_hello.py --port 5000
   ```

---

## 🧪 測試與文件

- **API 測試**：使用 [requestLocal.http](./requestLocal.http) 進行本地請求測試 🧪
- **傳統安裝方式**：如果你習慣使用一般的 pip 安裝 Flask，請參考 [Flask 安裝文檔](./docs/flask.md) 📚

---
*祝你的 Flask 開發旅程順利！如果有任何問題，歡迎隨時查閱文檔。🚀*


