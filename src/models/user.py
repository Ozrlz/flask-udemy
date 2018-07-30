from os import environ
import sqlite3
from db import db

DATABASE_NAME = environ.get('DATABASE_NAME')  

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) # 80 Chars at most
    passwd = db.Column(db.String(80))

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

