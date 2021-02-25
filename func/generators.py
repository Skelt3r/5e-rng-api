from data.core import CoreData as d
from data.framework import Framework
from random import choice
from .tools import choose_alignment, remove_inherent_dupes, sort_all
                    
import func.modifiers as m


# Returns a JSON serializable character object
def compile_character(fw):
    return {
        'character': {
            'bio': fw.character['bio'],
            'stats': fw.character['stats'],
            'abilities': fw.abilities,
            'skills': fw.skills,
            'proficiencies': fw.proficiencies,
            'spells': fw.spells,
            'inventory': fw.inventory
        }
    }


# Generate a completely random character
def random_character_gen():
    fw = Framework()

    fw.character['bio']['race'] = choice(d.races)
    fw.character['bio']['class'] = choice(d.classes)
    fw.character['bio']['gender'] = choice(['male', 'female'])
    fw.character['bio']['alignment'] = choose_alignment(fw.character['bio']['race'])

    m.assign_stats(fw)
    m.assign_race_mods(fw)
    m.assign_subrace_mods(fw)
    m.assign_class_mods(fw)
    m.assign_bg_mods(fw)
    m.assign_equipment(fw)
    m.assign_ability_mods(fw)
    m.assign_save_mods(fw)
    m.assign_save_prof(fw)
    m.assign_skill_mods(fw)
    m.assign_skill_prof(fw)
    m.assign_spells(fw)
    m.assign_spellcasting_mods(fw)
    m.assign_armor_class(fw)
    m.assign_unarmored_defense(fw)
    m.assign_body_mods(fw)
    m.assign_age(fw)
    m.assign_hp(fw)
    m.assign_initiative(fw)
    m.assign_passive_perception(fw)

    remove_inherent_dupes(fw)
    sort_all(fw)

    return compile_character(fw)
