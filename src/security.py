from werkzeug.security import safe_str_cpm
from user import User

users = [
    User(1, 'bob', 'asd')
]

username_mapping = { u.username: u for u in users }
userid_mapping = {u.id: u for u in users}

def authenticate(username, passwd):
    user = username_mapping.get(username, None)
    if user and safe_str_cpm(user.passwd, passwd):
        return user

def identity(payload):
    user_id = payload.get('identity')
    return userid_mapping.get(user_id, None)