# Default welcome message
welcome = {
    'message': 'Welcome to the 5e RNG API! See the available functions below.',
    'functions': {
        'GET': {
            '/roll/XdX': {
                'description': 'Roll any number of any type of dice. See the syntax examples below.',
                'examples': [
                    '/roll/1d20',
                    '/roll/2d6+5',
                    '/roll/4d4-1'
                ]
            },
            '/generate/stats': {
                'description': 'Randomly generate a set of 5e DND ability scores.'
            },
            '/generate/pc': {
                'description': 'Randomly generate a 5e DND player character.'
            }
        }
    }
}

# Error message for invalid input
invalid_input = {
    'error': 'invalid-input',
    'message': 'Bad request! Please enter a valid endpoint.',
    'examples': [
        '/roll/1d20',
        '/roll/2d6',
        '/roll/4d4+5',
        '/generate/stats',
        '/generate/pc'
    ],
    'status': 400
}

# Error message for an invalid roll count
invalid_roll_count = {
    'error': 'invalid-roll-count',
    'message': 'The endpoint accepts a minimum of 1 roll or a maximum of 100 rolls.',
    'status': 400
}

# Error message for an invalid dice type
invalid_dice_type = {
    'error': 'invalid-dice-type',
    'message': 'The endpoint accepts a range of d2-d100 dice types.',
    'status': 400
}
