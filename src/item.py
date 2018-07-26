from os import environ
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

DATABASE_NAME = environ.get('DATABASE_NAME')


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = 'SELECT * FROM items WHERE name=?'
        result = cr.execute(query, (name,))
        row = result.fetchone()

        if row:
            return {'item': {
                    'name': row[0],
                    'price': row[1]
                }
            }
        return {'mesage': 'An item with a name {} did not exists'.format(name)}

    def post(self, name):
        if next(filter(lambda x: x.get('name') == name, items), None):
            return {"message": "An item with the name {} already exists".format(name)}, 400
        
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