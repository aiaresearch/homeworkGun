import psycopg2
from datetime import datetime
import toml
import os


# 初始化数据库连接
def init_db() -> dict:
    return toml.load(os.path.join(os.path.dirname(__file__) +'\\config.toml'))

def insert_submit(numbers) -> None:
    cfg = init_db()['databases']

    conn = psycopg2.connect(
    host=cfg['host'],
    database=cfg['database'],
    user=cfg['username'],
    password=cfg['password'],
    )
    cur = conn.cursor()

    for number in numbers:
        cur.execute(f"SELECT * FROM students WHERE id = {number};")
        ret = cur.fetchone()
        if ret is None:
            continue
        else:
            cur.execute(f"INSERT INTO submit VALUES ({number}, '{datetime.now().strftime('%Y-%m-%d')}');")
            print(f"Inserted {number} into submit table")
