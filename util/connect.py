import sqlite3
import psycopg2
from enum import Enum
import os

DB_NAME = "homework.db"


def connect_to_sqlite_db(database: str = DB_NAME) -> sqlite3.Connection:
    """
        连接到SQLite数据库并返回connection
    """

    conn = sqlite3.connect(database)
    return conn

def get_connection():
        return connect_to_sqlite_db()