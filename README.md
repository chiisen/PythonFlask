# PythonFlask
Python Flask 入門指南 : 輕量級網頁框架教學

---

# 使用 uv 管理 Python 環境
[使用 uv 管理 Python 環境](./docs/uv/uv.md)

---

# 安裝 Flask 套件
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

