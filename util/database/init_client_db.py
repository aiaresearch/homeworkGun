import os
from .connect import get_connection


def database_init():
    if(os.path.exists('../homework.db')):
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    school_id INT PRIMARY KEY NOT NULL,
                    name VARCHAR(255) NOT NULL
    );''')

    cursor.execute('''DROP TABLE IF EXISTS homeworks;''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS homeworks (
                   homework_id INT PRIMARY KEY NOT NULL,
                   subject INT NOT NULL,
                   start_date DATE NOT NULL,
                   end_date DATE NOT NULL
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS submissions (
                   subject_id INT NOT NULL,
                   homework_id INT NOT NULL,
                   school_id INT NOT NULL
    );''')

    cursor.close()
    conn.commit()
    conn.close()

