## 5e RNG API

With the elimination of free Heroku dynos, this API is no longer publicly available. However, it still runs perfectly fine in a local environment.

The API currently supports the following GET requests...
- `/roll/XdX` - Roll the dice! This endpoint currently supports a range of (1-100)d(2-100).
- `/generate/stats` - Randomly generate a set of 5e DND ability scores.
- `/generate/character` - Randomly generate a 5e DND player character.

...as well as a POST request for character generation:
```py
from requests import post
from rich import print

headers = {
    'Content-Type': 'application/json'
}

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
