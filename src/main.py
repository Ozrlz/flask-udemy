from os import environ

from flask import Flask

FLASK_PORT = environ.get('FLASK_PORT')
app = Flask(__name__)

# PORT - To retrieve data
# GET - to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name): # The parameter must match the name on the decorator
    return name

# GET /store
@app.route('/store')
def get_stores():
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass



app.run(port=FLASK_PORT, host='0.0.0.0')