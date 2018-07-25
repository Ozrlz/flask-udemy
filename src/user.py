import sqlite3
from os import environ

DATABASE_NAME = environ.get('DATABASE_NAME')

class User:
    def __init__(self, _id, username, passwd):
        self.id = _id
        self.username = username
        self.passwd = passwd

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,) )
        row = result.fetchone()
        user = cls(*row) if row else None
        
        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        user = cls(*row) if row else None

        connection.close()
        return user
