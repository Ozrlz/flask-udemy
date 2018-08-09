from flask_restful import Resource, reqparse
from pdb import set_trace as debug

from models.user import UserModel

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

        user = UserModel(**payload)
        user.save_to_db()
        return {"message": "User created"}


class User(Resource):

    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted'}, 200