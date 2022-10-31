import sqlite3


def get_db_conn() -> sqlite3.Connection:
    return sqlite3.connect("database.db")
