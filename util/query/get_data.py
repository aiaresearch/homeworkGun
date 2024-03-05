import sys
import os


def __get_student(conn, class_id):
    cur = conn.cursor()
    cur.execute(f"SELECT name, id FROM students WHERE class_id = {class_id};")
    students = cur.fetchall()
    cur.close()
    return students