import sqlite3
import traceback
import sys

class Database:

    def __init__(self):
        self.models = 0


    def create_table(self, conn):
        try:
            conn.execute('''CREATE TABLE TELEMETRYDATA
                        (ID INT PRIMARY KEY NOT NULL,
                        DATA VARCHAR(100) NOT NULL);''')
            print('Created table')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))


    def insert_into_table(self, conn):
        data = input()
        count = 0
        try:
            cursor = conn.execute('select * from TELEMETRYDATA;')
            for row in cursor:
                count+=1
            conn.execute("""
                    insert into TELEMETRYDATA(ID, DATA) values(?, ?)""",
                    (count, data))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))


    def display_data(self, conn):
        try:
            cursor = conn.execute('select * from TELEMETRYDATA;')
            for row in cursor:
                print(row[0],"\t",row[1],"\n")
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))


    def drop_table(self, conn):
        try:
            conn.execute('drop table TELEMETRYDATA')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

    def pointer_to_rows(self, conn):
        try:
            cursor = conn.execute('select * from TELEMETRYDATA;')
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        return cursor
