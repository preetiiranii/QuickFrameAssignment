import os, sqlite3
from sqlite3 import Error

class DBUtil:

    def __init__(self, db_file, db_conn):
        self.db_file = db_file
        self.db_conn = db_conn

    """ create a database connection to a SQLite database """
    def create_connection(self):
        try:
            if self.db_conn is None:
                self.db_conn = sqlite3.connect(self.db_file)
                print(sqlite3.version)
        except Error as e:
            print(e)

    """ close database connection """
    def close_connection(self):
        if self.db_conn:
            self.db_conn.close()

    """ fetch database connection if already exists, else create a new one """
    def get_connection(self):
        if self.db_conn is None:
            create_connection()
        return self.db_conn

    """ create a new table in database """
    def create_table(self, create_stmt):
        db_cursor = self.get_cursor()
        db_cursor.execute(create_stmt)

    """ populate table with values """
    def insert_table(self, insert_stmt):
        """insert value"""
        try:
            db_cursor = self.get_cursor()
            db_cursor.execute(insert_stmt)
        except Error as e:
            #print(e)
            #print(insert_stmt)
            pass



    """ Drop the table if exists """
    def drop_table(self, table_name):
        db_cursor = self.get_cursor()
        db_cursor.execute('DROP TABLE IF EXISTS ' + table_name+';')

    """ display table rows """
    def select_table(self, table_name):
        db_cursor = self.get_cursor()
        all_rows = db_cursor.execute('SELECT * FROM ' + table_name + ';')

        for row in all_rows:
            print(row)

    def commit(self):
        self.db_conn.commit()


    def get_cursor(self):
        if self.db_conn is None:
            create_connection()
        return (self.db_conn.cursor())


