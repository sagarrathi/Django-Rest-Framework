import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"

try:
    cursor.execute(create_table)

except:
    pass


connection.commit()
connection.close()
