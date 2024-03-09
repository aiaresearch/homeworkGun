import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
from util.convert_passwd import convert


def __get_student(conn, class_id):
    cur = conn.cursor()
    cur.execute(f"SELECT name, id FROM students WHERE class_id = {class_id};")
    students = cur.fetchall()
    cur.close()
    return students

def __match_user(conn, username, passwd):
    cur = conn.cursor()
    print(username, passwd)
    cur.execute(f"SELECT password, salt FROM users WHERE username = '{username}';")
    password, salt = cur.fetchone()
    return True if convert(passwd, salt) == password else False
