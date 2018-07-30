import sqlite3

from os import environ

DATABASE_NAME = environ.get('DATABASE_NAME')

con = sqlite3.connect(DATABASE_NAME)
cr = con.cursor()

create_table_users_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cr.execute(create_table_users_query)

create_table_items_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cr.execute(create_table_items_query)

con.commit()
con.close()