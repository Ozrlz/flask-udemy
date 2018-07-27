import sqlite3
from os import environ

from flask_restful import Resource, reqparse
from pdb import set_trace as debug

from models.user import UserModel

DATABASE_NAME = environ.get('DATABASE_NAME')

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
        payload = cls.parser.parse_args()
        if UserModel.find_by_username(payload.get('username')):
            return {"message": "A user with name {} already exists".format(payload.get('username'))}
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cr.execute(query, (payload.get('username'), payload.get('password')))
        
        con.commit()
        con.close()

        return {"message": "User created"}