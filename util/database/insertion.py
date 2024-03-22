import os
import sys
import uuid
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from util.database.connect import get_connection


def insert_homework_creation(subject, start_date, end_date) -> int:
    homework_id = uuid.uuid4().int

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO homeworks VAlUES ('{homework_id}', {subject}, '{start_date}', '{end_date}');")
    conn.commit()
    cursor.close()
    conn.close()

    return homework_id
