from data.messages import invalid_input, welcome
from func.dice import interpret_roll, roll_stats
from func.generators import random_character_gen
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    """Return a default response if no endpoint is passed"""
    def get(self):
        return welcome


class Roll(Resource):
    """Define the behavior for the /roll endpoint"""
    def get(self, input):
        try:
            return interpret_roll(input)
        except:
            return invalid_input, 400


class Generate(Resource):
    """Define the behavior for the /generate endpoint"""
    def get(self, input):
        if input == 'stats':
            return roll_stats(json=True)
        elif input == 'pc':
            return random_character_gen()
        else:
            return invalid_input, 400


api.add_resource(Welcome, '/', '/help', '/generate', '/roll')
api.add_resource(Roll, '/roll/<string:input>')
api.add_resource(Generate, '/generate/<string:input>')


if __name__ == '__main__':
    app.run()
