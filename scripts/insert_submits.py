import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

QUERY_EXISTS = {DatabaseType.POSTGRES: "pg.database", DatabaseType.SQLITE: "sqlite_master"}
DATE_TYPE = {DatabaseType.POSTGRES: "DATE", DatabaseType.SQLITE: "TEXT"}


def insert_submits(db_type:DatabaseType = DatabaseType.SQLITE) -> None:
    conn = get_connection(db_type)
    cur = conn.cursor()

    students = []
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    size = len(students) // 2
    students = students[:size]
    submits = []
    for student in students:
        submits.append(student[0])
    for submit in submits:
        cur.execute(f"INSERT INTO submit VALUES ({submit},date());")

    print("Insertion done.")

    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_submits(DatabaseType.SQLITE)