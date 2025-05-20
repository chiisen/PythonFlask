# 🚀 PythonFlask
Python Flask 入門指南 : 輕量級網頁框架教學👍  

---

# 🚀 讓 code-runner 輸出到 Terminal (Python)
GitHub Copilot 只有 `#terminalLastCommand`  
無法取得 【輸出】視窗的訊息  
所以調整 `code-runner.runInTerminal`  
方便分析錯誤，不用複製貼上，省麻煩。  

## 設定預設終端機
```shell
terminal.integrated.defaultProfile
```
`Command Prompt` 是 `cmd.exe`  
`PowerShell` 是 `PowerShell 7.5.1`  

# 🚀 使用 uv 管理 Python 環境
[使用 uv 管理 Python 環境](https://github.com/chiisen/uv)

---

# 🚀 安裝 Flask 套件
```shell
uv run --with Flask .\src\flask\flask_hello.py
```

[flask_hello.py](./src/flask/flask_hello.py)  
瀏覽網址 http://127.0.0.1:5000  
拿掉 `flask_hello.py` 中的 `port=5000` 可以改由 uv 指令指定 port  
```shell
uv run --with Flask .\src\flask\flask_hello.py --port 5000
```

---

