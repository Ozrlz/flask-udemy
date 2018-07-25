import sqlite3

con = sqlite3.connect('test.db')
cr = con.cursor()

create_table_query = "CREATE TABLE users (id int, username text, password text)"
cr.execute(create_table_query)

user = (1, "ozrlz", "qwasdasd")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cr.execute(insert_query, user)

users = [
    (1, "ozrlz1", "qwasdasd"),
    (2, "ozrlz2", "qwasdasd"),
    (3, "ozrlz3", "qwasdasd"),
    (4, "ozrlz4", "qwasdasd"),
]

cr.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cr.execute(select_query):
    print (row)

con.commit()
con.close()
