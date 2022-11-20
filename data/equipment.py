class EquipmentData():
    """Class for storing and retrieving equipment data"""
    armor = {
        'light': [
            'padded',
            'leather',
            'studded leather'
        ],
        'medium': [
            'hide',
            'chain shirt',
            'scale mail',
            'breastplate',
            'half plate'
        ],
        'heavy': [
            'ring mail',
            'chain mail',
            'splint',
            'plate'
        ]
    }

    weapons = {
        'melee': {
            'simple': [
                'club',
                'dagger',
                'greatclub',
                'handaxe',
                'javelin',
                'light hammer',
                'mace',
                'quarterstaff',
                'sickle',
                'spear'
            ],
            'martial': [
                'battleaxe',
                'flail',
                'glaive',
                'greataxe',
                'greatsword',
                'halberd',
                'lance',
                'longsword',
                'maul',
                'morningstar',
                'pike',
                'rapier',
                'scimitar',
                'shortsword',
                'trident',
                'war pick',
                'warhammer',
                'whip'
            ]
        },
        'ranged': {
            'simple': [
                'light crossbow',
                'dart',
                'shortbow',
                'sling'
            ],
            'martial': [
                'blowgun',
                'hand crossbow',
                'heavy crossbow',
                'longbow',
                'net'
            ]
        }
    }

    tools = [
        "alchemist's supplies",
        "brewer's supplies",
        "calligrapher's supplies",
        "carpenter's tools",
        "cartographer's tools",
        "cobbler's tools",
        "cook's utensils",
        "glassblower's tools",
        "jeweler's tools",
        "leatherworker's tools",
        "mason's tools",
        "painter's supplies",
        "potter's tools",
        "smith's tools",
        "tinker's tools",
        "weaver's tools",
        "woodcarver's tools"
    ]

    gaming_sets = [
        'dice set',
        'playing card set'
    ]

    instruments = [
        'bagpipes',
        'drum',
        'dulcimer',
        'flute',
        'lute',
        'lyre',
        'horn',
        'pan flute',
        'shawm',
        'viol'
    ]

    equipment_packs = {
        'burglar': [
            'backpack',
            '1,000 ball bearings',
            '10 feet of string',
            'bell', 
            '5 candles',
            'crowbar',
            'hammer',
            '10 pitons',
            'hooded lantern',
            '2 flasks of oil',
            '5 days of rations',
            'tinderbox',
            'waterskin',
            '50 feet of hempen rope'
        ],
        'diplomat': [
            'chest',
            'case for maps',
            'case for scrolls',
            'set of fine clothes',
            'bottle of ink',
            'ink pen',
            'lamp',
            '2 flasks of oil',
            '5 sheets of paper',
            'vial of perfume',
            'sealing wax',
            'soap'
        ],
        'dungeoneer': [
            'backpack',
            'crowbar',
            'hammer',
            '10 pitons',
            '10 torches',
            'tinderbox',
            '10 days of rations',
            'waterskin'
        ],
        'entertainer': [
            'backpack',
            'bedroll',
            '2 costumes',
            '5 candles',
            '5 days of rations',
            'waterskin',
            'disguise kit'
        ],
        'explorer': [
            'backpack',
            'bedroll',
            'mess kit',
            'tinderbox',
            '10 torches',
            '10 days of rations',
            'waterskin',
            '50 feet of hempen rope'
        ],
        'priest': [
            'backpack',
            'blanket',
            '10 candles',
            'tinderbox',
            'alm box',
            '2 blocks of incense',
            'censer',
            'vestments',
            '2 days of rations',
            'waterskin'
        ],
        'scholar': [
            'backpack',
            'book of lore',
            'bottle of ink',
            'ink pen',
            '10 sheets of parchment',
            'small bag of sand',
            'small knife'
        ],
    }
