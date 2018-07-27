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
        item = self.find_by_name(name)        
        return item if item else {'mesage': 'An item with a name {} did not exists'.format(name)}

    @classmethod
    def find_by_name(cls, name):
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

    def post(self, name):
        if Item.find_by_name(name):
            return {"message": "An item with the name {} already exists".format(name)}, 400
        
        payload = Item.parser.parse_args()
        item = {'name': name, 'price': payload.get('price')}
        try:
            Item.insert(item)        
        except:
            return {"message": "An error ocurred while inserting the item"}, 500
        
        return item, 201

    @classmethod
    def insert(cls, item):
        '''
        Args:
            cls -> The current class
            item -> Dictionary with name and price keys'''
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cr.execute(query, (item.get('name'), item.get('price')))

        con.commit()
        con.close()

    @classmethod
    def update(cls, item):
        '''
        Args:
            cls -> The current class
            item -> Dictionary with name and price keys'''
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        cr.execute(query, (item.get('price'), item.get('name')) )
        con.commit()
        con.close()


    def delete(self, name):
        if Item.find_by_name(name) is None:
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
        item = Item.find_by_name(name)
        updated_item = {
            'name': name,
            'price': payload.get('price')
        }
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error ocurred while inserting the item"}, 500
        else:
            try:
                Item.update(updated_item)
            except:
                return {"message": "An error ocurred while updating the item"}, 500

        return updated_item


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