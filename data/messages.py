
def welcome():
    return {'message': 'Welcome to the 5e RNG API! See the available functions below.',
            'functions': {
                'GET': {
                    '/roll/XdX': {'description': 'Use the following syntax for rolling dice.',
                                  'examples': ['/roll/1d20',
                                               '/roll/2d6+5',
                                               '/roll/4d4-1']},
                    '/roll/stats': {'description': 'Randomly generate a set of 5e ability scores.'}}}}


def invalid_input():
    return {'error': 'invalid-input',
            'message': 'Bad request! Please enter a valid endpoint.',
            'examples': ['/roll/1d20',
                         '/roll/2d6',
                         '/roll/4d4+5',
                         '/roll/stats',
                         '/generate/pc'],
            'status': 400}


def invalid_roll_count():
    return {'error': 'invalid-roll-count',
            'message': 'The endpoint accepts a minimum of 1 roll or a maximum of 100 rolls.',
            'status': 400}


def invalid_dice_type():
    return {'error': 'invalid-dice-type',
            'message': 'The endpoint accepts a range of d2-d100 dice types.',
            'status': 400}
