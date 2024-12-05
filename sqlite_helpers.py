import sqlite3


def close_connection(db_connection):
    if db_connection:
        db_connection.close()


def open_connection(db_path):
    # Connect to SQLite database
    db_connection = sqlite3.connect(db_path)
    return db_connection
