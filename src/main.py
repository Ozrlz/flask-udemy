from os import environ

from flask import Flask
from flask_restful import  Api, reqparse
from pdb import set_trace as debug
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)
app.secret_key = 'super_secret_key'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth endpoint created



if __name__ == '__main__':
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')
    app.run(port=FLASK_PORT, host='0.0.0.0', debug=True)