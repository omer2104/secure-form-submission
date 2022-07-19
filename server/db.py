import sqlite3


conn = sqlite3.connect("info.sqlite")


cursor = conn.cursor()
sql_query = """ CREATE TABLE reviews (
   review_id INTEGER PRIMARY KEY AUTOINCREMENT,
   name text NOT NULL,
   email text NOT NULL,
   productName text NOT NULL,
   days int NOT NULL,
   satisfaction text NOT NULL,
   verdict text NOT NULL
)"""
cursor.execute(sql_query)
