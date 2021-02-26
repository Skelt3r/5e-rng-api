## 5th Edition Pseudorandom Number Generator Application Programming Interface

Base URL: https://prng-api.herokuapp.com/

The API currently supports the following GET requests:  
- `/roll/XdX` - Roll the dice! This endpoint currently supports a range of (1-100)d(2-100).
- `/generate/stats` - Randomly generate a set of 5e DND ability scores.
- `/generate/pc` - Randomly generate a 5e DND player character.

Planned features:
- Implement descriptions for features/traits, spells, items, etc.
- Generate characters beyond level 1
- Custom character generation with the option to define certain parameters
- NPC generation
- ???

More detailed info coming soon...

## If you have any cool ideas, feature suggestions, or bugs to report, feel free to open a ticket or make your own pull request!

This project was heavily inspired by the [5e DND API](https://www.dnd5eapi.co/). Check them out!

This project is licensed under the terms of the MIT license.

The random character generation functionality of this project incorporates material from the [System Reference Document 5.1](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf), which is released under the terms of the [Open Gaming License Version 1.0a](https://www.wizards.com/default.asp?x=d20/oglfaq/20040123f).
