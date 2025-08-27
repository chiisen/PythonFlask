from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flask.app")
logger.info("Flask app logger initialized")

# 初始化 Flask 應用程式物件，設定好路由等資訊，但此時伺服器尚未啟動
app = Flask(__name__)
@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})

# 新增一個 /hello 的路由，當使用者瀏覽 /hello 時會執行此函式
@app.route("/hello")
def say_hello():
    return jsonify({"message": "Hello from /hello route!"})

# 當這個檔案被直接執行時，__name__ 會等於 "__main__"
# 如果這個檔案是被其他模組 import，__name__ 會等於檔案名稱 (例如 flask_hello)
# 這樣可以讓下方的程式碼只在直接執行時才會執行，而被 import 時不會執行
if __name__ == "__main__":
    logger.info("Starting Flask app on http://127.0.0.1:5000")
    # 啟動 Flask 內建伺服器，開始接收網頁請求
    app.run(host="127.0.0.1", port=5000)