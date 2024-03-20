import os
import sys
import uuid
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from util.database.connect import get_connection


def insert_homework_creation(title, subject, start_date, end_date) -> str:
    homework_id = uuid.uuid4().hex

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO homeworks VAlUES ('{homework_id}', '{title}', {subject}, '{start_date}', '{end_date}');")
    conn.commit()
    cursor.close()
    conn.close()

    return homework_id
