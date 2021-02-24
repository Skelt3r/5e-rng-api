from data.messages import invalid_input, invalid_dice_type, invalid_roll_count
from random import randint

# Roll any number of any type of dice
def roll_dice(num_sides=20, num_rolls=1):
    if num_rolls == 1:
        return randint(1, num_sides)
    elif num_rolls > 1:
        return [randint(1, num_sides) for _roll in range(num_rolls)]
    else:
        return invalid_input, 400


# Roll a set of ability scores
def roll_stats(json=False):
    # Roll 4d6, drop the lowest roll, and return the remaining sum
    def stat_gen():
        rolls = sorted(roll_dice(num_sides=6, num_rolls=4))
        rolls.pop(0)
        return sum(rolls)
    
    stats = sorted([stat_gen() for _stat in range(0, 6)], reverse=True)

    if json == True:
        return {'results': stats}
    else:
        return stats


# Construct a response based on the given input
def interpret_roll(input):
    # Dissect the command into useful parts
    nums = input.split('d')
    num_rolls = int(nums[0])

    # Check for modifiers
    if nums[1].find('+') != -1:
        num_sides = int(nums[1].split('+')[0])
        mod = int(nums[1].split('+')[1])
    elif nums[1].find('-') != -1:
        num_sides = int(nums[1].split('-')[0])
        mod = -int(nums[1].split('-')[1])
    else:
        num_sides = int(nums[1])
        mod = 0

    result = roll_dice(num_sides, num_rolls)

    if num_rolls > 100 or num_rolls < 1:
        return invalid_roll_count, 400
    elif num_sides > 100 or num_sides < 2:
        return invalid_dice_type, 400
    elif num_rolls == 1 and mod == 0:
        return {'input': {'raw': input, 'num_rolls': num_rolls, 'dice_type': f'd{num_sides}'},
                'result': result}
    elif num_rolls == 1 and mod != 0:
        return {'input': {'raw': input, 'num_rolls': num_rolls, 'dice_type': f'd{num_sides}', 'mod': mod},
                'result': result,
                'total': result + mod}
    elif num_rolls > 1 and mod == 0:
        return {'input': {'raw': input, 'num_rolls': num_rolls, 'dice_type': f'd{num_sides}'},
                'results': result,
                'total': sum(result)}
    elif num_rolls > 1 and mod != 0:
        return {'input': {'raw': input, 'num_rolls': num_rolls, 'dice_type': f'd{num_sides}', 'mod': mod},
                'results': result,
                'total': sum(result) + mod}
    else:
        return invalid_input, 400
