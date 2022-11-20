from copy import copy
from data.core import CoreData
from data.equipment import EquipmentData
from data.spells import SpellData
from math import floor
from random import choice, randint


core_data = CoreData()
eq_data = EquipmentData()
spell_data = SpellData()


def remove_inherent_dupes(framework):
    """Removes duplicates that are inherent because of race/class/background features"""
    framework.character['bio']['traits'] = list(dict.fromkeys(framework.character['bio']['traits']))
    framework.proficiencies['armor'] = list(dict.fromkeys(framework.proficiencies['armor']))
    framework.proficiencies['weapons'] = list(dict.fromkeys(framework.proficiencies['weapons']))
    framework.proficiencies['tools'] = list(dict.fromkeys(framework.proficiencies['tools']))
    framework.proficiencies['languages'] = list(dict.fromkeys(framework.proficiencies['languages']))
    framework.inventory['misc'] = list(dict.fromkeys(framework.inventory['misc']))


def choose_alignment(race):
    """Randomly choose the character's alignment based on race"""
    chance = randint(1, 100)

    match race:
        case 'dragonborn':
            if chance <= 75:
                return choice(core_data.alignments['good'])
            else:
                return choice(core_data.alignments['evil'])
        case 'dwarf':
            if chance <= 80:
                return 'lawful good'
            elif chance > 80 and chance <= 90:
                return choice(core_data.alignments['lawful'])
            else:
                return choice(core_data.alignments['all'])
        case 'elf':
            if chance <= 90:
                return choice(['chaotic good', 'chaotic neutral'])
            else:
                return choice(core_data.alignments['all'])
        case 'gnome':
            if chance <= 80:
                return choice(core_data.alignments['good'])
            else:
                return choice(core_data.alignments['all'])
        case 'half-elf':
            if chance <= 90:
                return choice(core_data.alignments['chaotic'])
            else:
                return choice(core_data.alignments['all'])
        case 'half-orc':
            if chance <= 80:
                return choice(core_data.alignments['chaotic'])
            elif chance > 80 and chance <= 90:
                return choice(core_data.alignments['all'])
            else:
                return 'chaotic evil'
        case 'halfling':
            if chance <= 90:
                return 'lawful good'
            else:
                return choice(core_data.alignments['all'])
        case 'human':
            return choice(core_data.alignments['all'])
        case 'tiefling':
            if chance <= 50:
                return choice(core_data.alignments['chaotic'])
            elif chance > 50 and chance <= 80:
                return choice(core_data.alignments['evil'])
            else:
                return choice(core_data.alignments['all'])
        case _:
            return 'pick_alignment: invalid race input'


def body_gen(framework, base_height, base_weight, height_mod, weight_mod):
    """Generate a character's height and weight"""
    final_height = base_height + height_mod
    final_weight = height_mod * weight_mod + base_weight
    framework.character['bio']['height'] = f'{floor(final_height / 12)} ft. {final_weight % 12} in.'
    framework.character['bio']['weight'] = f'{final_weight} lbs.'


def randomize_stats(framework, stats, temp_abils, start, stop):
    """Randomly assign ability scores"""
    for stat in range(start, stop):
        ability = choice(temp_abils)
        framework.abilities[ability]['score'] = stats[stat]
        temp_abils.remove(ability)


def select_instruments(framework, num_inst):
    """Assign instrument proficiencies"""
    count = num_inst
    temp_instruments = copy(eq_data.instruments)
    while count > 0:
        inst = choice(temp_instruments)
        if inst in framework.proficiencies['instruments']:
            continue
        else:
            framework.proficiencies['instruments'].append(inst)
            temp_instruments.remove(inst)
            count -= 1


def splice_weapons(framework):
    """Remove already owned weapons from temp list"""
    temp_weapons = copy(eq_data.weapons)
    simple_melee_weapons = temp_weapons['melee']['simple']
    martial_melee_weapons = temp_weapons['melee']['martial']
    simple_ranged_weapons = temp_weapons['ranged']['simple']
    martial_ranged_weapons = temp_weapons['ranged']['martial']
    held_weapons = framework.inventory['weapons']

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


def select_weapons(framework, range_, type_, num=1):
    """Randomly select acquired weapons. Can choose from weapon type/class or be completely random"""
    temp_weapons = splice_weapons(framework)
    for _ in range(num):
        if range_ == 'random' and type_ != 'random':
            range_ = choice(['melee', 'ranged'])
            weapon = choice(temp_weapons[range_][type_])
            framework.inventory['weapons'].append(weapon)
            temp_weapons[range_][type_].remove(weapon)
        elif range_ != 'random' and type_ == 'random':
            type_ = choice(['simple', 'martial'])
            weapon = choice(temp_weapons[range_][type_])
            framework.inventory['weapons'].append(weapon)
            temp_weapons[range_][type_].remove(weapon)
        elif range_ == 'random' and type_ == 'random':
            type_ = choice(['melee', 'ranged'])
            range_ = choice(['simple', 'martial'])
            weapon = choice(temp_weapons[range_][type_])
            framework.inventory['weapons'].append(weapon)
            temp_weapons[range_][type_].remove(weapon)
        else:
            weapon = choice(temp_weapons[range_][type_])
            framework.inventory['weapons'].append(weapon)
            temp_weapons[range_][type_].remove(weapon)


def sort_all(framework):
    """Sort all lists alphabetically"""
    framework.character['bio']['traits'].sort()
    framework.character['stats']['resistances'].sort()
    framework.character['stats']['immunities'].sort()
    framework.spells['innate'].sort()
    framework.spells['cantrips'].sort()
    framework.spells['1st_level'].sort()
    framework.inventory['armor'].sort()
    framework.inventory['weapons'].sort()
    framework.inventory['misc'].sort()


def splice_languages(framework):
    """Remove all known languages from the parent list"""
    temp_langs = copy(core_data.languages)
    for known_lang in framework.proficiencies['languages']:
        for lang in temp_langs:
            if known_lang == lang:
                temp_langs.remove(lang)
    return temp_langs


def select_languages(framework, num_langs):
    """Randomly select a language and add it to the list of known languages"""
    temp_langs = splice_languages(framework)
    for _ in range(num_langs):
        lang = choice(temp_langs)
        framework.proficiencies['languages'].append(lang)
        temp_langs.remove(lang)
        count -= 1


def splice_profs(framework, profs):
    """Remove all known skill proficiencies from the parent list"""
    for prof in profs:
        if framework.skills[prof]['proficient']:
            profs.remove(prof)


def select_profs(framework, profs, num_profs):
    """Randomly select proficient skills from the appropriate class list"""
    for _ in range(num_profs):
        prof = choice(profs)
        framework.skills[prof]['proficient'] = True
        profs.remove(prof)


def splice_spells(framework, spell_level):
    """Remove all known spells from the parent list"""
    class_ = framework.character['bio']['class']
    temp_spells = copy(spell_data.spell_list[class_][spell_level])
    for spell in framework.spells[spell_level]:
        if spell in temp_spells:
            temp_spells.remove(spell)
    return temp_spells


def select_spells(framework, num_spells, spell_level):
    """Used to select known spells from the appropriate class list"""
    temp_spells = splice_spells(framework, spell_level)
    for _ in range(num_spells):
        spell = choice(temp_spells)
        framework.spells[spell_level].append(spell)
        temp_spells.remove(spell)


def unpack_gear(framework, pack): 
    """Unpack all of the items in a starting equipment pack and add them to the character's inventory"""
    for item in eq_data.equipment_packs[pack]: 
        framework.inventory['misc'].append(item)
