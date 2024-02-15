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

@app.route('/')
def index():
    users = get_users()


    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
