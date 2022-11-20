class Framework:
    """Framework class for generating unique character objects"""
    def __init__(self):
        self.character = {
            'bio': {
                'race': '',
                'subrace': '',
                'class': '',
                'background': {
                    'skill_prof_1': '',
                    'skill_prof_2': '',
                    'tool_prof': '',
                    'lang_prof': ''
                },
                'traits': [],
                'alignment': '',
                'gender': '',
                'age': 0,
                'size': '',
                'height': '',
                'weight': 0
            },
            'stats': {
                'level': 1,
                'hit_points': 0,
                'hit_dice': 0,
                'armor_class': 10,
                'initiative': 0,
                'speed': 0,
                'proficiency_bonus': 2,
                'passive_perception': 10,
                'resistances': [],
                'immunities': []
            }
        }
        self.abilities = {
            'strength': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            },
            'dexterity': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            },
            'constitution': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            },
            'intelligence': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            },
            'wisdom': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            },
            'charisma': {
                'score': 0,
                'modifier': 0,
                'saving_throw': {
                    'modifier': 0,
                    'proficient': False
                }
            }
        }
        self.skills = {
            'acrobatics': {
                'modifier': 0,
                'proficient': False
            },
            'animal_handling': {
                'modifier': 0,
                'proficient': False
            },
            'arcana': {
                'modifier': 0,
                'proficient': False
            },
            'athletics': {
                'modifier': 0,
                'proficient': False
            },
            'deception': {
                'modifier': 0,
                'proficient': False
            },
            'history': {
                'modifier': 0,
                'proficient': False
            },
            'insight': {
                'modifier': 0,
                'proficient': False
            },
            'intimidation': {
                'modifier': 0,
                'proficient': False
            },
            'investigation': {
                'modifier': 0,
                'proficient': False
            },
            'medicine': {
                'modifier': 0,
                'proficient': False
            },
            'nature': {
                'modifier': 0,
                'proficient': False
            },
            'perception': {
                'modifier': 0,
                'proficient': False
            },
            'performance': {
                'modifier': 0,
                'proficient': False
            },
            'persuasion': {
                'modifier': 0,
                'proficient': False
            },
            'religion': {
                'modifier': 0,
                'proficient': False
            },
            'sleight_of_hand': {
                'modifier': 0,
                'proficient': False
            },
            'stealth': {
                'modifier': 0,
                'proficient': False
            },
            'survival': {
                'modifier': 0,
                'proficient': False
            }
        }
        self.proficiencies = {
            'armor': [],
            'weapons': [],
            'tools': [],
            'languages': [],
            'instruments': [],
            'gaming_sets': [],
            'vehicles': [],
            'misc': []
        }
        self.spells = {
            'innate': [],
            'cantrips': [],
            '1st_level': [],
            'spellcasting_ability': '',
            'spell_save_dc': 0,
            'spell_attack_bonus': 0,
            'spell_slots': {
                '1st_level': 0
            }
        }
        self.inventory = {
            'armor': [],
            'weapons': [],
            'ammo': [],
            'misc': [],
            'gold': 0,
        }
