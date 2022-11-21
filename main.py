from data.messages import invalid_input, welcome
from func.dice import interpret_roll, roll_stats
from func.generators import character_gen
from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    """Return a default response if no endpoint is passed"""
    def get(self):
        return welcome


class Roll(Resource):
    """Define the behavior for the /roll path"""
    def get(self, input):
        try:
            return interpret_roll(input)
        except:
            return invalid_input, 400


class Generate(Resource):
    """Define the behavior for the /generate path"""
    def get(self, input):
        if input == 'stats':
            return roll_stats(json=True)
        elif input == 'character':
            return character_gen(random=True)
        else:
            return invalid_input, 400

    parser = reqparse.RequestParser(trim=True)
    parser.add_argument('name', location='form', type=str)
    parser.add_argument('race', location='form', type=str)
    parser.add_argument('class', location='form', type=str)
    parser.add_argument('gender', location='form', type=str)
    parser.add_argument('alignment', location='form', type=str)
    
    def post(self, input):
        if input == 'character':
            args = self.parser.parse_args()
            return character_gen(False, args['name'], args['race'], args['class'], args['gender'], args['alignment']), 201
        else:
            return invalid_input, 400


api.add_resource(Welcome, '/', '/help', '/generate', '/roll')
api.add_resource(Roll, '/roll/<string:input>')
api.add_resource(Generate, '/generate/<string:input>')


if __name__ == '__main__':
    app.run()
