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
    with open(os.path.join(os.path.abspath(os.path.dirname(os.pardir)), 'util', 'database', 'init_server_db.sql'), 'r') as file:
        cursor.execute(file.read())

    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    init_database()