import psycopg2
import toml
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType
from datetime import datetime

# PostgreSQL数据库连接参数
cfg = toml.load(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/config.toml')
cfg = cfg['databases']

def get_users():
    conn = get_connection(DatabaseType.POSTGRESQL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# 从数据库中获取提交列表
def get_submits():
    conn = get_connection(DatabaseType.POSTGRESQL)
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM submit WHERE time = {datetime.now().strftime('%Y-%m-%d')};")
    submits = cur.fetchall()
    cur.close()
    conn.close()
    return submits

def get_unsubmits():
    conn = get_connection(DatabaseType.POSTGRESQL)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM students WHERE id NOT IN (SELECT id FROM submit WHERE time = {datetime.now().strftime('%Y-%m-%d')});")
    unsubmits = cur.fetchall()
    cur.close()
    conn.close()  
    return unsubmits