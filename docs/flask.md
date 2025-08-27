# Flask
Flask 是輕量級的網頁框架

## 安裝
```bash
pip install Flask
```

## 建立 API
建立 [app.py](../src/flask/app.py) 檔案
```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hello")
def say_hello():
    return "Hello from /hello route!"
```

## 執行
進到 app.py 目錄
```python
cd .\src\flask
```
用 flask 執行 app.py，
直接用 launch.json 執行會直接結束程式。
```python
flask run 
```
flask_hello.py 則可以直接用 launch.json 執行與中斷。
