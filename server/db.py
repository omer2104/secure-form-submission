import sqlite3


conn = sqlite3.connect("info.sqlite")


cursor = conn.cursor()
sql_query = """ CREATE TABLE info (
   email text PRIMARY KEY,
   content text NOT NULL
)"""
cursor.execute(sql_query)
