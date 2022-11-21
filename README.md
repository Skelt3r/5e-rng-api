## 5e RNG API

With the elimination of free Heroku dynos, this API is no longer publicly available. However, it still runs perfectly fine in a local environment.

The API currently supports the following GET requests...
```py
from requests import get
from rich import print
```
- `/roll/XdX` - Roll the dice! This endpoint currently supports a range of (1-100)d(2-100).
```py
req = get('http://127.0.0.1:5000/roll/1d20').json()
print(req)
>>> {
        'input': {
            'raw': '1d20',
            'num_rolls': 1,
            'dice_type': 'd20'
        },
        'result': 17
    }

req = get('http://127.0.0.1:5000/roll/4d6+2').json()
print(req)
>>> {
        'input': {
            'raw': '4d6+2',
            'num_rolls': 4,
            'dice_type': 'd6',
            'mod': 2
        },
        'results': [4, 2, 3, 5],
        'total': 16
    }
```
- `/generate/stats` - Randomly generate a set of 5e DND ability scores.
```py
req = get('http://127.0.0.1:5000/generate/stats').json()
print(req)
>>> { 'results': [17, 14, 14, 12, 12, 10] }
```
- `/generate/character` - Randomly generate a 5e DND player character.
```py
req = get('http://127.0.0.1:5000/generate/character').json()
print(req)
```
...as well as a POST request for customized character generation:
```py
from requests import post
from rich import print

body = {
    'name': 'Green Bean',
    'race': 'elf',
    'class': 'ranger',
    'gender': 'male',
    'alignment': 'neutral'
}

req = post('http://127.0.0.1:5000/generate/character', data=body).json()
print(req)
```

Feature ideas:
- Implement descriptions for features/traits, spells, items, etc.
- Expand custom character generation
- Generate characters beyond level 1
- NPC generation

This API was heavily inspired by the [DND 5e API](https://www.dnd5eapi.co/). Check them out!

This project is licensed under the terms of the MIT license.

The random character generation functionality of this project incorporates material from the [System Reference Document 5.1](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf), which is released under the terms of the [Open Gaming License Version 1.0a](https://www.wizards.com/default.asp?x=d20/oglfaq/20040123f).
