# 1.import sqlite
import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # We are calling user table first and to do table references an atribute of the user table

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          ID INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)    



    def create_user_table(self):

        query = "CREATE TABLE IF NOT EXISTS 'User' (UID INTEGER PRIMARY KEY,Name TEXT,Email VARCHAR,);"
        self.conn.execute(query)