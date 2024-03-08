import os
import sys
import csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.generate_csv import generate_student
from util.connect import get_connection, DatabaseType


def create_database(db_type:DatabaseType = DatabaseType.SQLITE)  -> None:
    conn = get_connection(db_type)
    cur = conn.cursor()
    
        
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS submit (id INT PRIMARY KEY, time TEXT);")

    cur.close()
    conn.commit()
    conn.close()

def insert_students_from_csv(file_path:str, db_type:DatabaseType = DatabaseType.SQLITE) -> None:
    conn = get_connection(db_type)
    cur = conn.cursor()

    with open(file_path, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute(f"INSERT INTO students (id, name) VALUES ({int(row[0])}, '{row[1]}');")
        print(f"Inserted {len(list(reader))} students into the database.")


    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    csv_file = os.path.join(os.path.dirname(__file__),'students.csv')
    if not os.path.exists(csv_file):
        generate_student()
    
    insert_students_from_csv(csv_file)