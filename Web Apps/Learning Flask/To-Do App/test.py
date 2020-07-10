# 1.import sqlite
import sqlite3

# 2. create a connection to DB     
conn = sqlite3.connect('todo.db')

# 3. Write your sql query   
query = "show tables;"

# 4. execute the query
result = conn.execute(query)