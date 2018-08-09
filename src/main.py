from os import environ

from flask import Flask
from flask_restful import  Api, reqparse
from pdb import set_trace as debug
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import User

FLASK_PORT = environ.get('FLASK_PORT')
DATABASE_NAME = environ.get('DATABASE_NAME', 'test.db')
PSQL_USR = environ.get('POSTGRES_USER')
PSQL_PASSWD = environ.get('POSTGRES_PASSWORD')
PSQL_PORT = environ.get('POSTGRES_PORT')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://' + \
    PSQL_USR + ':' + PSQL_PASSWD + '@db:' + PSQL_PORT + '/' + DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True # Propagates all the JWT exceptions 
# raised, not only the flask ones
app.secret_key = 'super_secret_key'
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')

jwt = JWT(app, authenticate, identity) # /auth endpoint created



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # Create tables before the first requests gets dispatched
    @app.before_first_request
    def create_tables():
        db.create_all() 
    app.run(port=FLASK_PORT, host='0.0.0.0', debug=True)