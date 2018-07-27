from werkzeug.security import safe_str_cmp
from resources.user import User
from pdb import set_trace as debug


def authenticate(username, passwd):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.passwd, passwd):
        return user

def identity(payload):
    user_id = payload.get('identity')
    return User.find_by_id(user_id)