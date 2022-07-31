import sqlite3

connection =sqlite3.connect('data.db')

cursor=connection.cursor()

create_table="CREATE TABLE users (id int, username text, password text)"

try:
    cursor.execute(create_table)
except:
    pass


user=(1, "dsmonk", "sagar")
insert_query="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users=[
    (2, "mo", "saga"),
    (3, "ds", "sag"),
    (4, "monk", "sa"),
]
cursor.executemany(insert_query, users)


# select_query="SELECT * FROM users"

# for row in cursor.execute(select_query):
#     print(row)
    
connection.commit()
connection.close()