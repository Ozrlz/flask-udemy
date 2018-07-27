from os import environ
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

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
        item = ItemModel.find_by_name(name)        
        return item.json() if item else {'mesage': 'An item with a name {} did not exists'.format(name)}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with the name {} already exists".format(name)}, 400
        
        payload = Item.parser.parse_args()
        item = ItemModel(name, payload.get('price') )
        try:
            item.insert()
        except:
            return {"message": "An error ocurred while inserting the item"}, 500
        
        return item.json(), 201
    
    def delete(self, name):
        if ItemModel.find_by_name(name) is None:
            return {'message': 'Item with name {} not found'.format(name)}, 400
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cr.execute(query, (name,))
        con.commit()
        con.close()
        return {'message': 'Item deleted'}

    def put(self, name):
        payload = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name,payload.get('price'))
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error ocurred while inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error ocurred while updating the item"}, 500

        return updated_item.json()


class ItemList(Resource):
    
    def get(self):
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = 'SELECT * FROM items'
        result = cr.execute(query)
        items = []

        for row in result:
            items.append({
                'name': row[0],
                'price': row[1]
            })

        con.close()
        return {'items': items}, 200