from data.messages import invalid_input, welcome
from func.dice import interpret_roll, roll_stats
from func.generators import random_character_gen
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


# Return a default response if no endpoint is passed
class Welcome(Resource):
    def get(self):
        return welcome


# Define the behavior for the /roll endpoint
class Roll(Resource):
    def get(self, input):
        try:
            return interpret_roll(input)
        except:
            return invalid_input, 400


# Define the behavior for the /generate endpoint
class Generate(Resource):
    def get(self, input):
        if input == 'stats':
            return roll_stats(json=True)
        elif input == 'pc':
            return random_character_gen()
        else:
            return invalid_input, 400


# Add resources to API
api.add_resource(Welcome, '/', '/help', '/generate', '/roll')
api.add_resource(Roll, '/roll/<string:input>')
api.add_resource(Generate, '/generate/<string:input>')

if __name__ == '__main__':
    app.run()
