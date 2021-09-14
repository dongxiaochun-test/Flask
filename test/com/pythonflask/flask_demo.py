from flask import Flask
from flask_restful import Resource,Api

from com.pythonflask.log_util import logger

app = Flask(__name__)
api = Api(app)

class TestCaseServer(Resource):

    def get(self):
        logger.info("get method")
        return {"code" : 0, "msg" : "get success"}

    def post(self):
        logger.info("post method")
        return {"code": 0, "msg": "post success"}

    def put(self):
        logger.info("put method")
        return {"code": 0, "msg": "put success"}

    def delete(self):
        logger.info("delete method")
        return {"code": 0, "msg": "delete success"}

if __name__ == '__main__':
    app.run(debug=True)
