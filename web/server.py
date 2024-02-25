from flask import Flask, render_template
#from zhipuai import ZhipuAI
import psycopg2
import toml
import os
import webbrowser
import threading

app = Flask(__name__)
#client = ZhipuAI(api_key="YOUR_API_KEY") # 请填写您自己的APIKey

# PostgreSQL数据库连接参数
cfg = toml.load(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/config.toml')
cfg = cfg['databases']

DB_HOST = cfg['host']
DB_NAME = cfg['database']
DB_USER = cfg['username']
DB_PASSWORD = cfg['password']

# 连接到PostgreSQL数据库
def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# 从数据库中获取用户列表
def get_users():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# 从数据库中获取提交列表
def get_submits():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM submit;")
    submits = cur.fetchall()
    cur.close()
    conn.close()
    return submits

def get_unsubmits():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id NOT IN (SELECT id FROM submit);")
    unsubmits = cur.fetchall()
    cur.close()
    conn.close()  
    return unsubmits
@app.route('/')
def index():
    users = get_users()
    submits = get_submits()  # 调用get_submits函数从数据库检索提交
    unsubmits = get_unsubmits()  # 调用get_unsubmits函数从数据库检索未提交
    return render_template('index.html', users=users, submits=submits, unsubmits=unsubmits)

def open_browser():
    # 在 Flask 应用启动时自动打开浏览器并访问指定的网址
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    # 在启动 Flask 应用程序后，启动一个线程来自动打开浏览器
    app_thread = threading.Thread(target=open_browser)
    app_thread.start()

    # 启动 Flask 应用程序
    app.run(debug=True)
