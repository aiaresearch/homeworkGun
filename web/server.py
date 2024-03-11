from flask import Flask, render_template, request
#from zhipuai import ZhipuAI
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType
from util.query import get_data
import webbrowser
import threading
import requests

app = Flask(__name__)
#client = ZhipuAI(api_key="YOUR_API_KEY") # 请填写您自己的APIKey

conn = get_connection(DatabaseType.POSTGRES)

# 从数据库中获取用户列表
def get_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# 从数据库中获取提交列表
def get_submits():
    cur = conn.cursor()
    cur.execute("SELECT id FROM submit;")
    submits = cur.fetchall()
    cur.close()
    conn.close()
    return submits

def get_unsubmits():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id NOT IN (SELECT id FROM submit);")
    unsubmits = cur.fetchall()
    cur.close()
    conn.close()  
    return unsubmits

def match_user(user_id, passwd):
    return get_data.__match_user(conn, user_id, passwd)


@app.route('/')
def index():
    users = get_users(conn)
    submits = get_submits(conn)  # 调用get_submits函数从数据库检索提交
    unsubmits = get_unsubmits(conn)  # 调用get_unsubmits函数从数据库检索未提交
    return render_template('index.html', users=users, submits=submits, unsubmits=unsubmits)

@app.route('/getinfo/student', methods=['GET'])
def get_studentinfo():
    class_id = request.args.get('class_id')
    return get_data.__get_student(conn, class_id)

@app.route('/login', methods=['POST'])
def check_login():
    data = request.form
    user_id = data['username']
    passwd = data['password']
    if match_user(user_id, passwd):
        return 'success'
    else:
        return 'fail'


if __name__ == '__main__':
    # 启动 Flask 应用
    app.run(debug=True)
    conn.close()