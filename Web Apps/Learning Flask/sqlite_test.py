# 1.import sqlite
import sqlite3

# 2. create a connection to DB     
conn = sqlite3.connect('todo.db')

# 3. Write your sql query   
query1 = """
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
query2 = "SHOW DATABASES"

# 4. execute the query
result = conn.execute(query1)
result = conn.execute(query2)