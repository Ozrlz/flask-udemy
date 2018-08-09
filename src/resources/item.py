from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required,
        get_jwt_claims,
        jwt_required,
        jwt_optional,
        get_jwt_identity,
        fresh_jwt_required
    )
    
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
    )

    @jwt_required # Now is not a decorator with arguments, so we do not use the () 
    def get(self, name):
        item = ItemModel.find_by_name(name)        
        return item.json() if item else {'mesage': 'An item with a name {} did not exists'.format(name)}

    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with the name {} already exists".format(name)}, 400
        
        payload = Item.parser.parse_args()
        item = ItemModel(name, **payload)
        try:
            item.save_to_db()
        except:
            return {"message": "An error ocurred while inserting the item"}, 500
        
        return item.json(), 201
    
    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims.get('is_admin'):
            return {'message': 'Admin privilige required'}, 401
        item = ItemModel.find_by_name(name)
        if item is None:
            return {'message': 'Item with name {} not found'.format(name)}, 400
        item.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, name):
        payload = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **payload)
        else:
            item.price = payload.get('price')

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:
            return {'items': items}, 200
        return {
            'items': [item.get('name') for item in items],
            'message': 'More data available if you log in.'
        }, 200