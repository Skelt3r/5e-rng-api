from copy import copy
from data.core import Data as d
from data.framework import Framework
from json import dumps
from random import choice
from sys import exit
from .tools import choose_alignment, remove_inherent_dupes, sort_all
                    
import func.modifiers as m


# Returns a JSON serializable character object
def compile_character(fw):
    return {
        'character': fw.character,
        'abilities': fw.abilities,
        'skills': fw.skills,
        'proficiencies': fw.proficiencies,
        'spells': fw.spells,
        'inventory': fw.inventory
    }


# Check for user input, otherwise apply random generation
def read_user_input(fw, race, cls, gender, alignment):
    if race != None:
        fw.character['bio']['race'] = race
    else:
        fw.character['bio']['race'] = choice(d.races)

    if cls != None:
        fw.character['bio']['class'] = cls
    else:
        fw.character['bio']['class'] = choice(d.classes)
    
    if gender != None:
        fw.character['bio']['gender'] = gender
    else:
        fw.character['bio']['gender'] = choice(['male', 'female'])
    
    if alignment != None:
        fw.character['bio']['alignment'] = alignment
    else:
        fw.character['bio']['alignment'] = choose_alignment(fw.character['bio']['race'])


# Ensure that user input is valid, otherwise return an error
def validate_user_input(race, cls, gender, alignment):
    def check_race_input():
        if race == None or race in d.races:
            return True
        else:
            return False

    def check_class_input():
        if cls == None or cls in d.classes:
            return True
        else:
            return False
        
    def check_gender_input():
        if gender == None or gender in ['male', 'female']:
            return True
        else:
            return False
        
    def check_alignment_input():
        if alignment == None or alignment in d.alignments['all']:
            return True
        else:
            return False
    
    def check_all_inputs():
        if (check_race_input() == True and
            check_class_input() == True and
            check_gender_input() == True and
            check_alignment_input() == True):
            return True
        else:
            return False

    if check_all_inputs() == True:
        return True
    else:
        return False


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


# Generate a character based on user input
# Accepts the same arguments as the random generator
def custom_character_gen(race=None,
                         cls=None,
                         background=None,
                         gender=None,
                         alignment=None,
                         name=None):

    if validate_user_input(race, cls, gender, alignment) == True:
        fw = Framework()

        read_user_input(fw, race, cls, gender, alignment)

        m.assign_stats(fw)
        m.assign_race_mods(fw)
        m.assign_subrace_mods(fw)
        m.assign_class_mods(fw)
        m.assign_bg_mods(fw)
        m.assign_equipment(fw)
        m.assign_ability_mods(fw)
        m.assign_skill_mods(fw)
        m.assign_skill_prof(fw)
        m.assign_save_mods(fw)
        m.assign_save_prof(fw)
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
    
    else:
        return 'custom_character_gen: invalid character input'
