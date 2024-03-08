import os
import sys
import subprocess
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.connect import get_connection, DatabaseType

def init_database():

    # completed = subprocess.run(['createdb', '-h', 'localhost', '-p', '5432', '-U', 'postgres', 'homework_db'])
    # if completed.returncode!= 0:
    #     print("Failed to create database, it looks like it already exists.")
    # completed.check_returncode()

    conn = get_connection(DatabaseType.POSTGRES)
    
    cursor = conn.cursor()
    
    # create tables
    cursor.execute("""CREATE EXTENSION IF NOT EXISTS "uuid-ossp";""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        class_id INTEGER NOT NULL
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS homeworks (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        title VARCHAR(50) NOT NULL,
        description TEXT,
        assigned_at DATE NOT NULL,
        due_at DATE NOT NULL,
        class_id INTEGER NOT NULL,
                   
        FOREIGN KEY (class_id) REFERENCES classes(id)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS submissions (
                   
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        homework_id UUID NOT NULL,
                   
        student_id INTEGER NOT NULL,
        submitted_at DATE NOT NULL,
                   
        FOREIGN KEY (homework_id) REFERENCES homeworks(id),
        FOREIGN KEY (student_id) REFERENCES students(id)
    );""")

    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    init_database()