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
    
def fetch_students_from_db():
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students;")
            student_list = cur.fetchall()
            return student_list

def fetch_submissions_from_db():
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM submit;")
            submission_ids = cur.fetchall()
            return submission_ids
            
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
    students = fetch_students_from_db()
    submissions = fetch_submissions_from_db()  # 调用get_submits函数从数据库检索提交
    unsubmits = get_unsubmits()  # 调用get_unsubmits函数从数据库检索未提交
    return render_template('index.html', users=students, submits=submissions, unsubmits=unsubmits)

if __name__ == '__main__':
    app.run()
