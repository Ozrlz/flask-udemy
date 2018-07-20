from os import environ

from flask import Flask, jsonify, request, render_template
from pdb import set_trace as debug

FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)
stores = [
    {
        'name': 'My store xd',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data.get('name'),
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name): # The parameter must match the name on the decorator
    # Return the store, else an error msg
    for store in stores:
        if store.get('name') == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found ):'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({
        'stores': stores
    })


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store.get('name') == name:
            debug()
            store.get('items').append(request_data)
            # return jsonify({'message': 'The items were pushed xd'})
            return jsonify(request_data)
    return jsonify({'message': 'The store was not found ):'} )


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify({'items': store.get('items')})
    return jsonify({'message': 'The store was not found ):'})

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=FLASK_PORT, host='0.0.0.0')