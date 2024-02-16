from flask import Flask, render_template
import psycopg2
import toml
import os

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)