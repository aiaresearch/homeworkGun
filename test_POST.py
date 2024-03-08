import os
import sys
import sqlite3
import requests
import json

# 将当前目录添加到系统路径中
sys.path.append(os.path.dirname(__file__))

# 导入connect模块
from util.connect import get_connection, DatabaseType

# SQLite数据库连接
conn = get_connection(DatabaseType.SQLITE)

# 定义将数据POST到PostgreSQL的函数
def post_to_postgresql(data):
    url = 'your_postgresql_api_url'
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError异常
        print("Data posted to PostgreSQL successfully.")
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

# 定义从SQLite数据库中提取数据的函数
def fetch_data_from_sqlite():
    data = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students;")
    # 查询SQLite数据库中的数据
    rows = cursor.fetchall()
    cursor.close()  # 关闭游标

    # 将元组列表转换为字典列表
    keys = ['name', 'id','classid']
    data = [dict(zip(keys, row)) for row in rows]
    
    return data


def main():
    data_to_post = fetch_data_from_sqlite()
    print("Data to be posted to PostgreSQL:")
    for row in data_to_post:
        print(row)
    post_to_postgresql(data_to_post)
    conn.close()  # 关闭数据库连接

if __name__ == '__main__':
    main()
