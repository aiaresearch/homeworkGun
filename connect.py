import sqlite3

DB_NAME = "test.db"

def connect_to_db(database: str = DB_NAME) -> sqlite3.Connection.cursor:
    """
        连接到数据库并返回cursor
    """

    conn = sqlite3.connect(database)
    return conn.cursor()