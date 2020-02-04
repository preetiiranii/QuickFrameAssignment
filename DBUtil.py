import os, sqlite3
from sqlite3 import Error

db_conn = None
db_file = os.getcwd() + r"\pythonsqlite.db"

""" create a database connection to a SQLite database """
def create_connection():
    global db_conn
    try:
        if db_conn is None:
            db_conn = sqlite3.connect(db_file)
            print(sqlite3.version)
    except Error as e:
        print(e)

""" close database connection """
def close_connection():
    if db_conn:
        db_conn.close()

""" fetch database connection if already exists, else create a new one """
def get_connection():
    if db_conn is None:
        create_connection()
    return db_conn

""" create a new table in database """
def create_table(create_stmt):
    db_cursor = get_cursor()
    db_cursor.execute(create_stmt)

""" populate table with values """
def insert_table(insert_stmt):
    """insert value"""
    db_cursor = get_cursor()
    db_cursor.execute(insert_stmt)

""" Drop the table if exists """
def drop_table(table_name):
    db_cursor = get_cursor()
    db_cursor.execute('DROP TABLE IF EXISTS ' + table_name+';')

""" display table rows """
def select_table(table_name):
    db_cursor = get_cursor()
    all_rows = db_cursor.execute('SELECT * FROM ' + table_name + ';')

    for row in all_rows:
        print(row)

def commit():
    db_conn.commit()


def get_cursor():
    if db_conn is None:
        create_connection()
    return (db_conn.cursor())


