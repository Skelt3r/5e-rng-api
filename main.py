from func.dice import *
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


# Default resource to display if no endpoint is passed
class Welcome(Resource):
    def get(self):
        return welcome()


# Resource for using the /roll command
class Roll(Resource):
    def get(self, input):
        try:
            if input == 'stats':
                return roll_stats(json=True)
            else:
                return interpret_roll(input)
        except:
            return invalid_input(), 400


# Add resources to API
api.add_resource(Welcome, '/', '/roll', '/help')
api.add_resource(Roll, '/roll/<string:input>')

if __name__ == '__main__':
    app.run()
