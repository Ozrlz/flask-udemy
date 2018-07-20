from os import environ

from flask import Flask

app = Flask(__name__)
FLASK_PORT = environ.get('FLASK_PORT')

@app.route('/')
def home():
    return "Hello world!"

app.run(port=FLASK_PORT, host='0.0.0.0')