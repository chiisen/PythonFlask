# PythonFlask
Python Flask 入門指南 : 輕量級網頁框架教學

# uv 安裝
uv 本身並不需要 Python，所以不建議用 pip 或是 pipx 安裝，這樣都會跟特定的 Python 環境綁在一起，Windows 上就直接透過 PowerSehll 安裝即可：
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
或是透過 scoop 等軟體管理工具安裝:
```shell
scoop install uv
```

# 安裝 Flask 套件
```shell
pip install Flask
```