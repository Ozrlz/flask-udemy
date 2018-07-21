from os import environ

from flask import Flask
from flask_restful import Resource, Api
from pdb import set_trace as debug

FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)
api = Api(app)

items = [{

}]

class Item(Resource):

    def get(self, name):
        for item in items:
            if item.get('name') == name:
                return item
        return {'message': 'item not found u.u'}, 404

    def post(self, name):
        item = {'name': name, 'price': 15.99}
        items.append(item)
        return item, 201

if __name__ == '__main__':
    api.add_resource(Item, '/item/<string:name>')
    app.run(port=FLASK_PORT, host='0.0.0.0')