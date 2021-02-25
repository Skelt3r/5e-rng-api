# Class for storing and retrieving core data
class CoreData():
    # List of races
    races = [
        'dragonborn',
        'dwarf',
        'elf',
        'gnome',
        'half-elf',
        'half-orc',
        'halfling',
        'human',
        'tiefling'
    ]

    # Dict of subraces
    subraces = {
        'dragonborn': [],
        'dwarf': [
            'hill dwarf'
        ],
        'elf': [
            'high elf'
        ],
        'gnome': [
            'rock gnome'
        ],
        'half-elf': [],
        'halfling': [
            'lightfoot'
        ],
        'half-orc': [],
        'human': [],
        'tiefling': []
    }

    # List of classes
    classes = [
        'barbarian',
        'bard',
        'cleric',
        'druid',
        'fighter',
        'monk',
        'paladin',
        'ranger',
        'rogue',
        'sorcerer',
        'warlock',
        'wizard'
    ]

    # List of languages
    languages = [
        'abyssal',
        'celestial',
        'common',
        'deep speech',
        'draconic',
        'dwarvish',
        'elvish',
        'giant',
        'gnomish',
        'goblin',
        'halfling',
        'infernal',
        'orc',
        'primordial',
        'sylvan',
        'undercommon'
    ]

    # Dict of alignments
    alignments = {
        'lawful': [
            'lawful good',
            'lawful neutral',
            'lawful evil'
        ],
        'chaotic': [
            'chaotic good',
            'chaotic neutral',
            'chaotic evil'
        ],
        'good': [
            'lawful good',
            'chaotic good',
            'neutral good'
        ],
        'evil': [
            'lawful evil',
            'chaotic evil',
            'neutral evil'
        ],
        'neutral': [
            'neutral',
            'neutral good',
            'neutral evil'
        ],
        'all': [
            'lawful good',
            'lawful neutral',
            'lawful evil',
            'chaotic good',
            'chaotic neutral',
            'chaotic evil',
            'neutral',
            'neutral good',
            'neutral evil'
        ]
    }

    # List of abilities for reference
    ability_list = [
        'strength',
        'dexterity',
        'constitution',
        'intelligence',
        'wisdom',
        'charisma'
    ]

    # List of skills for reference
    skill_list = [
        'acrobatics',
        'animal_handling',
        'arcana',
        'athletics',
        'deception',
        'history',
        'insight',
        'intimidation',
        'investigation',
        'medicine',
        'nature',
        'perception',
        'performance',
        'persuasion',
        'religion',
        'sleight_of_hand',
        'stealth',
        'survival'
    ]

    # Dict of skills grouped by class, used for assigning proficiency
    skill_prof_dict = {
        'all': [
            'acrobatics',
            'animal_handling',
            'arcana',
            'athletics',
            'deception',
            'history',
            'insight',
            'intimidation',
            'investigation',
            'medicine',
            'nature',
            'perception',
            'performance',
            'persuasion',
            'religion',
            'sleight_of_hand',
            'stealth',
            'survival'
        ],
        'barbarian': [
            'animal_handling',
            'athletics',
            'intimidation',
            'nature',
            'perception',
            'survival'
        ],
        'cleric': [
            'history',
            'insight',
            'medicine',
            'persuasion',
            'religion'
        ],
        'druid': [
            'arcana',
            'animal_handling',
            'insight',
            'medicine',
            'nature',
            'perception',
            'religion',
            'survival'
        ],
        'fighter': [
            'acrobatics',
            'animal_handling',
            'athletics',
            'history',
            'insight',
            'intimidation',
            'perception',
            'survival'
        ],
        'monk': [
            'acrobatics',
            'athletics',
            'history',
            'insight',
            'religion',
            'stealth'
        ],
        'paladin': [
            'athletics',
            'insight',
            'intimidation',
            'medicine',
            'persuasion',
            'religion'
        ],
        'ranger': [
            'animal_handling',
            'athletics',
            'insight',
            'investigation',
            'nature',
            'perception',
            'stealth',
            'survival'
        ],
        'rogue': [
            'acrobatics',
            'athletics',
            'deception',
            'insight',
            'intimidation',
            'investigation',
            'perception',
            'performance',
            'persuasion',
            'sleight_of_hand',
            'stealth'
        ],
        'sorcerer': [
            'arcana',
            'deception',
            'insight',
            'intimidation',
            'persuasion',
            'religion'
        ],
        'warlock': [
            'arcana',
            'deception',
            'history',
            'intimidation',
            'investigation',
            'nature',
            'religion'
        ],
        'wizard': [
            'arcana',
            'history',
            'insight',
            'investigation',
            'medicine',
            'religion'
        ]
    }

    draconic_ancestries = [
        'black',
        'blue',
        'brass',
        'bronze',
        'copper',
        'gold',
        'green',
        'red',
        'silver',
        'white'
    ]

    fighting_styles = [
        'archery',
        'defense',
        'dueling',
        'great weapon fighting',
        'protection',
        'two-weapon fighting'
    ]

    enemy_types = [
        'aberrations',
        'beasts',
        'celestials',
        'constructs',
        'dragons',
        'elementals',
        'fey',
        'fiends',
        'giants',
        'monstrosities',
        'oozes',
        'plants',
        'undead'
    ]
