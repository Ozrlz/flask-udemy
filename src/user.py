import sqlite3
from os import environ

from flask_restful import Resource, reqparse
from pdb import set_trace as debug

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

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"    
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @classmethod
    def post(cls):
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        payload = cls.parser.parse_args()
        cr.execute(query, (payload.get('username'), payload.get('password')))
        
        con.commit()
        con.close()

        return {"message": "User created"}, 201