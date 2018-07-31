from werkzeug.security import safe_str_cmp
from models.user import UserModel
from pdb import set_trace as debug


def authenticate(username, passwd):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, passwd):
        return user

def identity(payload):
    user_id = payload.get('identity')
    return UserModel.find_by_id(user_id)