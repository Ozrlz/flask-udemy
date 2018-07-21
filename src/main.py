from os import environ

from flask import Flask
from flask_restful import Resource, Api
from pdb import set_trace as debug

FLASK_PORT = environ.get('FLASK_PORT')

app = Flask(__name__)
api = Api(app)

class Student(Resource):

    def get(self, name):
        return {'student': name}

if __name__ == '__main__':
    api.add_resource(Student, '/student/<string:name>')
    app.run(port=FLASK_PORT, host='0.0.0.0')