import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from util.database.connect import get_connection


def insert_homework(homework_id, subject, start_date, end_date) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO homeworks VAlUES ('{homework_id}', {subject}, '{start_date}', '{end_date}');")
    conn.commit()
    cursor.close()
    conn.close()

    return homework_id


def insert_students(students: list[list[int, str]]):
    conn = get_connection()
    cursor = conn.cursor()
    
    for student in students:
        cursor.execute(f"INSERT INTO students VALUES ({student[0]}, '{student[1]}');")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def insert_submission(homework_id, school_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT subject FROM homeworks WHERE homework_id = {homework_id};")
    subject = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO submissions VALUES ({subject}, {homework_id}, {school_id});")
    conn.commit()
    cursor.close()
    conn.close()
    
    return subject