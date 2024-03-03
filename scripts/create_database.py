import os
import sys
import csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

QUERY_EXISTS = {DatabaseType.POSTGRES: "pg.database", DatabaseType.SQLITE: "sqlite_master"}
DATE_TYPE = {DatabaseType.POSTGRES: "DATE", DatabaseType.SQLITE: "TEXT"}

def create_database(db_type:DatabaseType = DatabaseType.SQLITE)  -> None:
    conn = get_connection(db_type)
    cur = conn.cursor()
    
        
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(50));")
    cur.execute(f"CREATE TABLE IF NOT EXISTS submit (id INT PRIMARY KEY, time {DATE_TYPE[db_type]});")

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
        print(f"Inserted {cur.rowcount} students into the database.")


    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    insert_students_from_csv(os.path.join(script_dir,'students.csv'))