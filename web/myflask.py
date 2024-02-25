from flask import Flask, render_template
from connect import get_connection, DatabaseType

app = Flask(__name__)

# 从数据库中获取用户列表
def get_users():
    conn = get_connection(DatabaseType.POSTGRES)
    cur = conn.cursor
    cur.execute("SELECT * FROM students;")
    users = cur.fetchall()
    conn.close()
    return users

# 从数据库中获取提交列表
def get_submits():
    conn = get_connection(DatabaseType.POSTGRES)
    cur = conn.cursor
    cur.execute("SELECT id FROM submit;")
    submits = cur.fetchall()
    conn.close()
    return submits

def get_unsubmits():
    conn = get_connection(DatabaseType.POSTGRES)
    cur = conn.cursor
    cur.execute("SELECT * FROM students WHERE id NOT IN (SELECT id FROM submit);")
    unsubmits = cur.fetchall()
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
