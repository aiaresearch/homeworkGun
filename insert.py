import psycopg2
from datetime import datetime
import toml
import os


# initialize connection and cursor

def insert(numbers) -> None:
    cfg = toml.load(os.path.join(os.path.dirname(__file__) +'\\config.toml'))
    cfg = cfg['databases']

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
