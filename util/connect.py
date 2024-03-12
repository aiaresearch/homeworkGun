import sqlite3
import psycopg2
from enum import Enum
import os

# config = toml.load(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/config.toml')['databases']
# USER = os.getenv('PG_USER')
# PASSWORD = os.getenv('PG_PASSWD')
# DATABASE = os.getenv('PG_DATABASE')
# if USER is None or PASSWORD is None or DATABASE is None:
#     raise ValueError("Database credentials not found in environment variables.")

DB_NAME = "homework.db"


class DatabaseType(Enum):
    SQLITE = 1
    POSTGRES = 2

def connect_to_sqlite_db(database: str = DB_NAME) -> sqlite3.Connection:
    """
        连接到SQLite数据库并返回connection
    """

    conn = sqlite3.connect(database)
    return conn

# def connect_to_postgres_db() -> psycopg2.extensions.connection:
#     """
#         连接到postgreSQL数据库并返回connection
#     """
#     conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, port="5432")
#     return conn

def get_connection(dbType: DatabaseType):
    if dbType == DatabaseType.SQLITE:
        return connect_to_sqlite_db()
    # elif dbType == DatabaseType.POSTGRES:
        # return connect_to_postgres_db()