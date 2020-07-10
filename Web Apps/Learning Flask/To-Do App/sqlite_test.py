# 1.import sqlite
import sqlite3

# 2. create a connection to DB     
conn = sqlite3.connect('todo.db')

# 3. Write your sql query   
query1 = """
        CREATE TABLE IF NOT EXISTS "User" (
          UID INTEGER PRIMARY KEY,
          Name TEXT,
          Email Varchar
        );
        """
query2 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

# 4. execute the query
result = conn.execute(query1)
result = conn.execute(query2)