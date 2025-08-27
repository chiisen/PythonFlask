# Hello World 範例
```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
```

第一行 : `from flask import Flask`
```python
另外一種更常見的 import 方式，可以簡化第二行的建構式宣告。

方法一:
import Flask 
app = flask.Flask(__name__)

方法二:
from flask import Flask
app = Flask(__name__)

方法二為官網的範例。
```

第二行 : `app = Flask(__name__)`
```bash
Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。
是固定用法，以便讓 Flask 知道在哪裡尋找資源。
(例如: 模板和靜態文件)
```

第三行 : `@app.route("/")`
裝飾器是告訴 Flask，哪個 URL 應該觸發我們的函式。

斜線代表的就是網站的根目錄，可以疊加。

例如: 新增一個 /hello 的位址
```python
@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"
```
網站訪問首頁與/hello，呈現的同樣是 hello 函式，回傳的 Hello World 文字。

- def hello(): : 被觸發的函式 第四行
- return "Hello, World!" : 函式回傳的文字字串，也等於 Web API 回傳的內容。第五行
# flask run 指令
```bash
官方範例，檔名為 app.py 使用的是 flask run 指令，可以直接啟動網站。

在日常的開發中，可以再加上 python 的 main 方法，
執行 app.run() 函式，執行網頁伺服器的啟動動作。
```
調整後 : hello-world.py
```python
# save this as app.py
import flask
app = flask.Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
```
# 註冊路由
除了固定的導向位址，URL 也可以成為函式接收的參數
## routing.py
```python
@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)
```
<name> 代表接收 name 參數為 字串型態
- 訪問 : http://127.0.0.1:5000/data/appInfo/FlaskSE
- 打印 : type(name) : <class 'str'>
- 網頁 : String => FlaskSE

```python
@app.route('/data/appInfo/id/<int:id>', methods=['GET'])
def queryDataMessageById(id):
    print("type(id) : ", type(id))
    return 'int => {}'.format(id)
```
- 訪問 : http://127.0.0.1:5000/data/appInfo/id/5
- 打印 : type(id) : <class 'int'>
- 網頁 : int => 5

```python
@app.route('/data/appInfo/version/<float:version>', methods=['GET'])
def queryDataMessageByVersion(version):
    print("type(version) : ", type(version))
    return 'float => {}'.format(version)
```
- 訪問 : http://127.0.0.1:5000/data/appInfo/version/1.01
- 打印 : type(version) : <class 'float'>
- 網頁 : float => 1.01

# 網頁模版 - Html 回傳
Python Flask 使用 Jinja2 的模板引擎

## 最簡單的網頁格式
```python
@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'
```
- 網頁顯示 : H1 大標題的 Hello World 元素
- 簡單的格式還可以，複雜一點，回傳 html 檔案會較為理想。

---

# templates 資料夾
在 python 執行檔的目錄下，創建 templates 資料夾，html 檔案放置於此
- /render.py
- /templates
    - /home.html
    - /page.html
    - /static.html

## render.py
```python
@app.route('/home')
def home():
    return render_template('home.html')
```
## templates/home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title>Home</title>
</head>
<body>
        <h1>My Website Text</h1>
        <table border="1">
                <tr>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                </tr>
                <tr>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                </tr>
                <tr>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                        <td>Text Text Text</td>
                </tr>
        </table>
</body>
</html>
```
- 訪問 : http://127.0.0.1:5000/home

---

# Jinja2 模板引擎
API 返回網頁時，可以做更多的事情
```
先看完整的程式碼，接續有說明。
```

## render.py
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

if __name__ == '__main__':
    app.run()
```
## templates/page.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template - Page</title>
</head>

<body>
    <h1>Template - Page </h1>
    <h2>{{text}}</h2>

    {% if appInfo != undefined %}

    <h2>AppInfo : </h2>
    <p>id : {{appInfo.id}}</p>
    <p>name : {{appInfo.name}}</p>
    <p>version : {{appInfo.version}}</p>
    <p>author : {{appInfo.author}}</p>
    <p>remark : {{appInfo.remark}}</p>
    {% endif %}

    {% if data != undefined %}
    <h2>Data : </h2>
    <table border="1">
        {% for key, value in data.items() %}
        <tr>
            <th> {{ key }} </th>
            <td> {{ value }} </td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
</body>

</html>
```
API 附帶參數: @app.route('/page/text')
## render.py
```python
@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")
```
- render_template() 函式 : 第二個參數可以附帶資料內容
## templates/page.html
```html
<h1>Template - Page </h1>
<h2>{{text}}</h2>
```
- text 參數 : 使用兩個大括號 {{ text }} 就可以將資料顯示在畫面上

API 字典型態與頁面條件式 : @app.route('/page/app')

## render.py
```python
@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)
```
- 不同的路由路徑，傳遞相同的網頁模版 :
    - @app.route('/page/app')
    - render_template('page.html', appInfo=appInfo)
- appInfo 參數 : 字典型態的變數，將更多的資料，在同一時間傳遞。

## templates/page.html
```html
{% if appInfo != undefined %}
<h2>AppInfo : </h2>
<p>id : {{appInfo.id}}</p>
<p>name : {{appInfo.name}}</p>
<p>version : {{appInfo.version}}</p>
<p>author : {{appInfo.author}}</p>
<p>remark : {{appInfo.remark}}</p>
{% endif %}
```
- 模板引擎，前端畫面條件式語法 :
    - {% if boolean %}
    - {% endif %}
    - if appInfo != undefined : 如果 appInfo 有資料，html 標籤內容生效
- {{appInfo.object}} : 字典參數取用資料方法，同樣兩個大括號包覆後生效。

# API : 字典型態與頁面迴圈
## render.py
```python
@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)
```
- 不同的路由路徑，傳遞相同的網頁模版 :
    - @app.route('/page/data')
    - return render_template('page.html', data=data)
- data 參數 : 字典型態的變數，與上一個相同，將更多的資料，同時間傳遞。

## templates/page.html
```html
{% if data != undefined %}
<h2>Data : </h2>
<table border="1">
    {% for key, value in data.items() %}
    <tr>
        <th> {{ key }} </th>
        <td> {{ value }} </td>
    </tr>
    {% endfor %}
</table>
{% endif %}
```
- 模板引擎，前端畫面條件式語法 : 與上一個相同
    - {% if boolean %}
    - {% endif %}
- 模板引擎，for 迴圈語法 : 將表格與參數內的資料，同時呈現出來
    - {% for key, value in data.items() %}
    - {{ key }} : 迴圈 key 值
    - {{ value }} : 迴圈 value 值
    - {% endfor %}

# static 資料夾
在 python 執行檔的目錄下，創建 static 資料夾，.js 與 .css 檔案放置於此

    - /render.py
    - /templates
        - /home.html
        - /page.html
        - /static.html
    - /static
        - /script.js
        - /style.css
前端開發的 javascript 與 css 檔案必須放在 static 資料夾才會生效。

## static.py
```python
@app.route('/static')
def staticPage():
    return render_template('static.html')
```

## static/script.js
```python
function sayHello(){
        alert("Hello World");
}
```

## templates/static.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title>Static - Page</title>
</head>
<body>
        <h1>Template - Page</h1>
        <button id="btnHello" onClick="sayHello()">Say Hello</button>
        <!-- <script src="../static/script.js"></script> -->
        <script type = "text/javascript" 
         src = "{{ url_for('static', filename = 'script.js') }}" ></script>
</body>
</html>
```
- 如果 src 的路徑不為 static
        - 點擊 button 不會有反應
        - 終端機顯示 http 404，表示找不到資源
- {{ url_for('static', filename = 'script.js') }}
        - 另外一種模板引擎的寫法，url_for 是轉址的函式
        - 第一個參數不動，調整 filename 參數可以使用其他資源

# 資料交換 - Form 表單提交 與 Ajax 資料交換
結合路由註冊與網頁模版，完整實現前端與後端的資料交換

## 前端 : 示範兩種
    1. Html - Form 表單提交
    2. jQuery - Ajax 資料交換
## 後端 : JSON 格式
- 讀寫實際的文件，模擬資料持久化

## Html - Form 表單提交
同樣先看代碼，接續代碼說明

## form.py
```python
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/form')
def formPage():
    return render_template('Form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        return redirect(url_for('success', name=user, action="post"))
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        return redirect(url_for('success', name=user, action="get"))

@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

if __name__ == '__main__':
    app.run()
```
## templates/form.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form - Submit</title>
</head>
<body>
    <h2>POST</h2>
    <form action="/submit" method="post">
        <h2>Enter Name:</h2>
        <p><input type="text" name="user" /></p>
        <p><input type="submit" value="submit" /></p>
    </form>
    <h2>GET</h2>
    <form action="/submit" method="get">
        <h2>Enter Name:</h2>
        <p><input type="text" name="user" /></p>
        <p><input type="submit" value="submit" /></p>
    </form>
</body>
</html>
```

# 前端 : Form 表單提交
## templates/form.html
```html
<form action="/submit" method="post">
    <h2>Enter Name:</h2>
    <p><input type="text" name="user" /></p>
    <p><input type="submit" value="submit" /></p>
</form>
<h2>GET</h2>
<form action="/submit" method="get">
    <h2>Enter Name:</h2>
    <p><input type="text" name="user" /></p>
    <p><input type="submit" value="submit" /></p>
</form>
```
- <form></form> : 兩個 form 表單元素
- action : 提交目標，也就是路由的 URL
- method : http 常見的提交方法，這裡分別實作 get 與 post 方法
- <input type="text" name="user" /> : 傳遞表單參數 name
- <input type="submit" value="submit" /> : html 元素，form 提交按鈕

# 後端 : 網頁模版與資料接口
































# 參考
[Python Flask 入門指南 : 輕量級網頁框架教學](https://devs.tw/post/448)

