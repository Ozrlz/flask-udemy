from os import environ

from flask import Flask
from flask_restful import  Api, reqparse
from pdb import set_trace as debug
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

FLASK_PORT = environ.get('FLASK_PORT')
DATABASE_NAME = environ.get('DATABASE_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key'
api = Api(app)

# Create tables before the first requests gets dispatched
@app.before_first_request
def create_tables():
    db.create_all() 

jwt = JWT(app, authenticate, identity) # /auth endpoint created



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')
    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    app.run(port=FLASK_PORT, host='0.0.0.0', debug=True)