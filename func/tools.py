from copy import deepcopy
from data.core import Data as cd
from math import floor
from random import choice, randint
from data.spells import spell_list
from sys import exit

import data.equipment as ed, os, sys


# This function removes duplicates that are inherent because of race/class/background features
def remove_inherent_dupes(fw):
    fw.character['bio']['traits'] = list(dict.fromkeys(fw.character['bio']['traits']))
    fw.proficiencies['armor'] = list(dict.fromkeys(fw.proficiencies['armor']))
    fw.proficiencies['weapons'] = list(dict.fromkeys(fw.proficiencies['weapons']))
    fw.proficiencies['tools'] = list(dict.fromkeys(fw.proficiencies['tools']))
    fw.proficiencies['languages'] = list(dict.fromkeys(fw.proficiencies['languages']))
    fw.inventory['misc'] = list(dict.fromkeys(fw.inventory['misc']))


# Choose the character's alignment
def choose_alignment(race):
    chance = randint(1, 100)

    if race == 'dragonborn':
        if chance <= 75:
            return choice(cd.alignments['good'])
        else:
            return choice(cd.alignments['evil'])

    elif race == 'dwarf':
        if chance <= 80:
            return 'lawful good'
        elif chance > 80 and chance <= 90:
            return choice(cd.alignments['lawful'])
        else:
            return choice(cd.alignments['all'])

    elif race == 'elf':
        if chance <= 90:
            return choice(['chaotic good', 'chaotic neutral'])
        else:
            return choice(cd.alignments['all'])

    elif race == 'gnome':
        if chance <= 80:
            return choice(cd.alignments['good'])
        else:
            return choice(cd.alignments['all'])

    elif race == 'half-elf':
        if chance <= 90:
            return choice(cd.alignments['chaotic'])
        else:
            return choice(cd.alignments['all'])

    elif race == 'half-orc':
        if chance <= 80:
            return choice(cd.alignments['chaotic'])
        elif chance > 80 and chance <= 90:
            return choice(cd.alignments['all'])
        else:
            return 'chaotic evil'

    elif race == 'halfling':
        if chance <= 90:
            return 'lawful good'
        else:
            return choice(cd.alignments['all'])

    elif race == 'human':
        return choice(cd.alignments['all'])

    elif race == 'tiefling':
        if chance <= 50:
            return choice(cd.alignments['chaotic'])
        elif chance > 50 and chance <= 80:
            return choice(cd.alignments['evil'])
        else:
            return choice(cd.alignments['all'])
    
    else:
        return 'pick_alignment: invalid race input'


# Used with the Ranger only
def assign_favored_enemy():
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
    return choice(enemy_types)


# Used to generate a character's height and weight
def body_gen(fw, base_height, base_weight, height_mod, weight_mod):
    final_height = base_height + height_mod
    final_weight = height_mod * weight_mod + base_weight
    fw.character['bio']['height'] = f'{floor(final_height / 12)} ft. {final_weight % 12} in.'
    fw.character['bio']['weight'] = f'{final_weight} lbs.'


# Used to randomly assign ability scores
def randomize_stats(fw, stats, temp_abils, start, stop):
    for stat in range(start, stop):
        ability = choice(temp_abils)
        fw.abilities[ability]['score'] = stats[stat]
        temp_abils.remove(ability)


# Used to assign instrument proficiencies
def select_instruments(fw, num_inst):
    count = num_inst
    temp_instruments = deepcopy(ed.instruments)

    while count > 0:
        x = choice(temp_instruments)
        if x in fw.proficiencies['instruments']:
            continue
        else:
            fw.proficiencies['instruments'].append(x)
            temp_instruments.remove(x)
            count -= 1


# Remove already owned weapons from temp list
def splice_weapons(fw):
    temp_weapons = deepcopy(ed.weapon_list)
    simple_melee_weapons = temp_weapons['melee']['simple']
    martial_melee_weapons = temp_weapons['melee']['martial']
    simple_ranged_weapons = temp_weapons['ranged']['simple']
    martial_ranged_weapons = temp_weapons['ranged']['martial']
    held_weapons = fw.inventory['weapons']

    for held in held_weapons:
        for weapon in simple_melee_weapons:
            if held == weapon:
                simple_melee_weapons.remove(weapon)
        for weapon in martial_melee_weapons:
            if held == weapon:
                martial_melee_weapons.remove(weapon)
        for weapon in simple_ranged_weapons:
            if held == weapon:
                simple_ranged_weapons.remove(weapon)
        for weapon in martial_ranged_weapons:
            if held == weapon:
                martial_ranged_weapons.remove(weapon)
        
    return temp_weapons


# Used to randomly select acquired weapons, can choose from weapon type/class or be completely random
def select_weapons(fw, rng, typ, num=1):
    temp_weapons = splice_weapons(fw)

    for x in range(num):
        if rng == 'random' and typ != 'random':
            rng = choice(['melee', 'ranged'])
            weapon = choice(temp_weapons[rng][typ])
            fw.inventory['weapons'].append(weapon)
            temp_weapons[rng][typ].remove(weapon)
        elif rng != 'random' and typ == 'random':
            typ = choice(['simple', 'martial'])
            weapon = choice(temp_weapons[rng][typ])
            fw.inventory['weapons'].append(weapon)
            temp_weapons[rng][typ].remove(weapon)
        elif rng == 'random' and typ == 'random':
            typ = choice(['melee', 'ranged'])
            rng = choice(['simple', 'martial'])
            weapon = choice(temp_weapons[rng][typ])
            fw.inventory['weapons'].append(weapon)
            temp_weapons[rng][typ].remove(weapon)
        else:
            weapon = choice(temp_weapons[rng][typ])
            fw.inventory['weapons'].append(weapon)
            temp_weapons[rng][typ].remove(weapon)


# Sort all lists alphabetically
def sort_all(fw):
    fw.character['bio']['traits'].sort()
    fw.character['stats']['resistances'].sort()
    fw.character['stats']['immunities'].sort()
    fw.spells['innate'].sort()
    fw.spells['cantrips'].sort()
    fw.spells['1st_level'].sort()
    fw.inventory['armor'].sort()
    fw.inventory['weapons'].sort()
    fw.inventory['misc'].sort()


# Remove all known languages from the parent list
def splice_languages(fw):
    temp_langs = deepcopy(cd.languages)

    for known_lang in fw.proficiencies['languages']:
        for lang in temp_langs:
            if known_lang == lang:
                temp_langs.remove(lang)

    return temp_langs


# Randomly select a language and add it to the list of known languages
def select_languages(fw, num_langs):
    temp_langs = splice_languages(fw)

    for l in range(num_langs):
        lang = choice(temp_langs)
        fw.proficiencies['languages'].append(lang)
        temp_langs.remove(lang)
        count -= 1


# Remove all known skill proficiencies from the parent list
def splice_profs(fw, profs):
    for x in profs:
        if fw.skills[x]['proficient'] == True:
            profs.remove(x)


# Randomly select proficient skills from the appropriate class list
def select_profs(fw, profs, num_profs):
    for p in range(num_profs):
        x = choice(profs)
        fw.skills[x]['proficient'] = True
        profs.remove(x)


# Remove all known spells from the parent list
def splice_spells(fw, spell_level):
    cls = fw.character['bio']['class']
    temp_spells = deepcopy(spell_list[cls][spell_level])

    for spell in fw.spells[spell_level]:
        if spell in temp_spells:
            temp_spells.remove(spell)
    
    return temp_spells


# Used to select known spells from the appropriate class list
def select_spells(fw, num_spells, spell_level):
    cls = fw.character['bio']['class']
    temp_spells = splice_spells(fw, spell_level)

    for s in range(num_spells):
        spell = choice(temp_spells)
        fw.spells[spell_level].append(spell)
        temp_spells.remove(spell)


# Unpack all of the items in a starting equipment pack and add them to the character's inventory
def unpack_gear(fw, pack): 
    for item in ed.equipment_packs[pack]: 
        fw.inventory['misc'].append(item)
