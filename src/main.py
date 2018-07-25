from os import environ

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pdb import set_trace as debug
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)
app.secret_key = 'super_secret_key'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth endpoint created

items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x.get('name') == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x.get('name') == name, items), None):
            return {"message": "An item with the name {} already exists".format(name)}, 400
            
        # Fails if does not have a payload or the ContentType header is not set
        # Can be bypassed with the force flag, but always executes it
        # Also, the silent flag can help not to rise an error
        
        payload = Item.parser.parse_args()
        
        item = {'name': name, 'price': payload.get('price')}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x.get('name') != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        payload = Item.parser.parse_args()
        item = next(filter(lambda x: x.get('name') == name, items), None)
        if item is None:
            item = {
                'name': name,
                'price': payload.get('price')
            }
            items.append(item)
        else:
            item.update(payload)
        return item


class ItemList(Resource):
    
    def get(self):
        return {'items': items}

if __name__ == '__main__':
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    app.run(port=FLASK_PORT, host='0.0.0.0', debug=True)