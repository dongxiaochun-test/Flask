from flask import Flask
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)

class HelloWord(Resource):

    def get(self):
        return {"hello" : "word"}

api.add_resource(HelloWords, '/')


if __name__ == '__main__':
    app.run(debug=True)