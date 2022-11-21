from data.core import CoreData
from data.framework import Framework
from random import choice
from .tools import choose_alignment, remove_inherent_dupes, sort_all
                    
import func.modifiers as m


def compile_character(framework:Framework):
    """Returns a JSON serializable character dictionary"""
    return {
        'character': {
            'bio': framework.character['bio'],
            'stats': framework.character['stats'],
            'abilities': framework.abilities,
            'skills': framework.skills,
            'proficiencies': framework.proficiencies,
            'spells': framework.spells,
            'inventory': framework.inventory
        }
    }


def character_gen(random:bool, name:str='', race:str='', class_:str='', gender:str='', alignment:str=''):
    """Generate a random character"""
    data = CoreData()
    framework = Framework()

    if random:
        framework.character['bio']['race'] = choice(data.races)
        framework.character['bio']['class'] = choice(data.classes)
        framework.character['bio']['gender'] = choice(['male', 'female'])
        framework.character['bio']['alignment'] = choose_alignment(framework.character['bio']['race'])
    else:
        assert race in data.races
        assert class_ in data.classes
        assert alignment in data.alignments
        framework.character['bio']['name'] = name
        framework.character['bio']['race'] = race.lower()
        framework.character['bio']['class'] = class_.lower()
        framework.character['bio']['gender'] = gender.lower()
        framework.character['bio']['alignment'] = alignment.lower()

    m.assign_stats(framework)
    m.assign_race_mods(framework)
    m.assign_subrace_mods(framework)
    m.assign_class_mods(framework)
    m.assign_bg_mods(framework)
    m.assign_equipment(framework)
    m.assign_ability_mods(framework)
    m.assign_save_mods(framework)
    m.assign_save_prof(framework)
    m.assign_skill_mods(framework)
    m.assign_skill_prof(framework)
    m.assign_spells(framework)
    m.assign_spellcasting_mods(framework)
    m.assign_armor_class(framework)
    m.assign_unarmored_defense(framework)
    m.assign_body_mods(framework)
    m.assign_age(framework)
    m.assign_hp(framework)
    m.assign_initiative(framework)
    m.assign_passive_perception(framework)
    remove_inherent_dupes(framework)
    sort_all(framework)

    return compile_character(framework)
