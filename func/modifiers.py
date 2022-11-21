from copy import deepcopy
from data.core import CoreData
from data.equipment import EquipmentData
from data.spells import SpellData
from .dice import roll_dice, roll_stats
from math import floor
from random import choice, randint, randrange

import func.tools as t


core_data = CoreData()
eq_data = EquipmentData()
spell_data = SpellData()


def assign_stats(framework):
    """Assign stats based on priority by class"""
    class_ = framework.character['bio']['class']
    stats = roll_stats()
    temp_abils = deepcopy(core_data.ability_list)

    match class_:
        case 'barbarian':
            temp_abils.remove('strength')
            temp_abils.remove('constitution')
            framework.abilities['strength']['score'] = stats[0]
            framework.abilities['constitution']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'bard':
            temp_abils.remove('charisma')
            temp_abils.remove('dexterity')
            framework.abilities['charisma']['score'] = stats[0]
            framework.abilities['dexterity']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'cleric':
            temp_abils.remove('wisdom')
            framework.abilities['wisdom']['score'] = stats[0]
            second = choice(['strength', 'constitution'])
            framework.abilities[second]['score'] = stats[1]
            temp_abils.remove(second)
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'druid':
            temp_abils.remove('wisdom')
            temp_abils.remove('constitution')
            temp_abils.remove('intelligence')
            framework.abilities['wisdom']['score'] = stats[0]
            framework.abilities['constitution']['score'] = stats[1]
            framework.abilities['intelligence']['score'] = stats[2]
            t.randomize_stats(framework, stats, temp_abils, 3, 6)
        case 'fighter':
            first = choice(['strength', 'dexterity'])
            framework.abilities[first]['score'] = stats[0]
            temp_abils.remove(first)
            if first == 'strength':
                temp_abils.remove('constitution')
                temp_abils.remove('dexterity')
                framework.abilities['constitution']['score'] = stats[1]
                framework.abilities['dexterity']['score'] = stats[2]
                t.randomize_stats(framework, stats, temp_abils, 3, 6)
            else:
                temp_abils.remove('intelligence')
                temp_abils.remove('constitution')
                framework.abilities['intelligence']['score'] = stats[1]
                framework.abilities['constitution']['score'] = stats[2]
                t.randomize_stats(framework, stats, temp_abils, 3, 6)
        case 'monk':
            temp_abils.remove('dexterity')
            temp_abils.remove('wisdom')
            framework.abilities['dexterity']['score'] = stats[0]
            framework.abilities['wisdom']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'paladin':
            temp_abils.remove('strength')
            temp_abils.remove('charisma')
            framework.abilities['strength']['score'] = stats[0]
            framework.abilities['charisma']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'ranger':
            temp_abils.remove('dexterity')
            temp_abils.remove('wisdom')
            framework.abilities['dexterity']['score'] = stats[0]
            framework.abilities['wisdom']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'rogue':
            temp_abils.remove('dexterity')
            framework.abilities['dexterity']['score'] = stats[0]
            second = choice(['intelligence', 'charisma'])
            framework.abilities[second]['score'] = stats[1]
            temp_abils.remove(second)
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case class_ if class_ in ['sorcerer', 'warlock']:
            temp_abils.remove('charisma')
            temp_abils.remove('constitution')
            framework.abilities['charisma']['score'] = stats[0]
            framework.abilities['constitution']['score'] = stats[1]
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case 'wizard':
            temp_abils.remove('intelligence')
            framework.abilities['intelligence']['score'] = stats[0]
            second = choice(['constitution', 'dexterity'])
            framework.abilities[second]['score'] = stats[1]
            temp_abils.remove(second)
            t.randomize_stats(framework, stats, temp_abils, 2, 6)
        case _:
            return 'assign_stats: invalid class input'


def assign_race_mods(framework):
    """Assign various properties based on race input"""
    race = framework.character['bio']['race']
    temp_abils = deepcopy(core_data.ability_list)
    temp_langs = deepcopy(core_data.languages)
    temp_skills = deepcopy(core_data.skill_list)
    
    match race:
        case 'dragonborn':
            ancestry = choice(core_data.draconic_ancestries)
            framework.abilities['strength']['score'] += 2
            framework.abilities['charisma']['score'] += 1
            framework.character['stats']['speed'] += 30
            framework.character['bio']['traits'].extend(['breath weapon',
                                                         'damage resistance',
                                                         f'draconic ancestry ({ancestry} dragon)'])
            framework.proficiencies['languages'].extend(['common', 'draconic'])
            if ancestry in ['black', 'copper']:
                framework.character['stats']['resistances'].append('acid')
                framework.spells['innate'].append('breath weapon (acid)')
            elif ancestry in ['blue', 'bronze']:
                framework.character['stats']['resistances'].append('lightning')
                framework.spells['innate'].append('breath weapon (lightning)')
            elif ancestry in ['brass', 'gold', 'red']:
                framework.character['stats']['resistances'].append('fire')
                framework.spells['innate'].append('breath weapon (fire)')
            elif ancestry in ['silver', 'white']:
                framework.character['stats']['resistances'].append('cold')
                framework.spells['innate'].append('breath weapon (cold)')
            else:
                framework.character['stats']['resistances'].append('poison')
                framework.spells['innate'].append('breath weapon (poison)')
        case 'dwarf':
            framework.abilities['constitution']['score'] += 2
            framework.character['stats']['speed'] += 25
            framework.character['stats']['resistances'].append('poison')
            framework.character['bio']['traits'].extend(['darkvision',
                                                         'dwarven resilience',
                                                         'dwarven combat training',
                                                         'stonecunning'])
            framework.proficiencies['languages'].extend(['common', 'dwarvish'])
            framework.proficiencies['weapons'].extend(['battleaxe', 'handaxe', 'light hammer', 'warhammer'])
            tool_profs = ["smith's tools", "brewer's supplies", "mason's tools"]
            framework.proficiencies['tools'].append(choice(tool_profs))
        case 'elf':
            framework.abilities['dexterity']['score'] += 2
            framework.character['stats']['speed'] += 30
            framework.character['bio']['traits'].extend(['darkvision', 'keen senses', 'fey ancestry', 'trance'])
            framework.proficiencies['languages'].extend(['common', 'elvish'])
            framework.skills['perception']['proficient'] = True
        case 'gnome':
            framework.abilities['intelligence']['score'] += 2
            framework.character['stats']['speed'] += 25
            framework.character['bio']['traits'].extend(['darkvision', 'gnome cunning'])
            framework.proficiencies['languages'].extend(['common', 'gnomish'])
        case 'halfling':
            framework.abilities['dexterity']['score'] += 2
            framework.character['stats']['speed'] += 25
            framework.character['bio']['traits'].extend(['lucky', 'brave', 'halfling nimbleness'])
            framework.proficiencies['languages'].extend(['common', 'halfling'])
        case 'half-elf':
            framework.abilities['charisma']['score'] +=2
            inc = choice(temp_abils)
            framework.abilities[inc]['score'] += 1
            temp_abils.remove(inc)
            framework.abilities[choice(temp_abils)]['score'] += 1
            framework.character['stats']['speed'] += 30
            framework.character['bio']['traits'].extend(['darkvision', 'fey ancestry'])
            if 'common' in temp_langs: temp_langs.remove('common')
            temp_langs.remove('elvish')
            framework.proficiencies['languages'].extend(['common', 'elvish', choice(temp_langs)])
            prof = choice(temp_skills)
            framework.skills[prof]['proficient'] = True
            temp_skills.remove(prof)
            framework.skills[choice(temp_skills)]['proficient'] = True
        case 'half-orc':
            framework.abilities['strength']['score'] += 2
            framework.abilities['constitution']['score'] += 1
            framework.character['stats']['speed'] += 30
            framework.character['bio']['traits'].extend(['darkvision', 'menacing', 'relentless endurance', 'savage attacks'])
            framework.proficiencies['languages'].extend(['common', 'orc'])
            framework.skills['intimidation']['proficient'] = True
        case 'human':
            for ability in core_data.ability_list: framework.abilities[ability]['score'] += 1
            framework.character['stats']['speed'] += 30
            temp_langs.remove('common')
            framework.proficiencies['languages'].extend(['common', choice(temp_langs)])
        case 'tiefling':
            framework.abilities['charisma']['score'] += 2
            framework.abilities['intelligence']['score'] += 1
            framework.character['stats']['speed'] += 30
            framework.character['stats']['resistances'].append('fire')
            framework.character['bio']['traits'].extend(['darkvision', 'hellish resistance', 'infernal legacy'])
            framework.proficiencies['languages'].extend(['common', 'infernal'])
            framework.spells['cantrips'].append('thaumaturgy')
        case _:
            return 'assign_race_mods: invalid race input'


def assign_subrace_mods(framework):
    """Assign subrace properties"""
    if len(core_data.subraces[framework.character['bio']['race']]) != 0:
        subrace = core_data.subraces[framework.character['bio']['race']][0]
        framework.character['bio']['subrace'] = subrace

        match subrace:
            case 'hill dwarf':
                framework.abilities['wisdom']['score'] += 1
                framework.character['bio']['traits'].append('dwarven toughness')
                framework.character['stats']['hit_points'] += 1
            case 'high elf':
                framework.abilities['intelligence']['score'] += 1
                framework.character['bio']['traits'].append('elf weapon training')
                framework.proficiencies['weapons'].extend(['longsword', 'shortsword', 'shortbow', 'longbow'])
                framework.spells['cantrips'].append(choice(spell_data.spell_list['wizard']['cantrips']))
            case 'rock gnome':
                framework.abilities['constitution']['score'] += 1
                framework.character['bio']['traits'].extend(["artificer's lore", 'tinker'])
                framework.proficiencies['tools'].append("artisan's tools")
            case 'lightfoot':
                framework.abilities['charisma']['score'] += 1
                framework.character['bio']['traits'].append('naturally stealthy')
    else:
        framework.character['bio']['subrace'] = None


def assign_class_mods(framework):
    """Assign various modifiers based on class"""
    class_ = framework.character['bio']['class']
    temp_tools = deepcopy(eq_data.tools)

    if class_ == 'bard':
        profs = deepcopy(core_data.skill_prof_dict['all'])
    else:
        profs = deepcopy(core_data.skill_prof_dict[class_])

    match class_:
        case 'barbarian':
            framework.character['stats']['hit_dice'] = 'd12'
            framework.character['bio']['traits'].extend(['rage', 'unarmored defense'])
            framework.character['stats']['rages'] = 2
            framework.character['stats']['rage_damage'] = 2
            framework.proficiencies['armor'].extend(['light armor', 'medium armor', 'shields'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
            framework.abilities['strength']['saving_throw']['proficient'] = True
            framework.abilities['constitution']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
        case 'bard':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(['bardic inspiration', 'spellcasting'])
            framework.proficiencies['armor'].append('light armor')
            framework.proficiencies['weapons'].extend(['simple weapons', 'hand crossbow', 'longsword', 'rapier', 'shortsword'])
            framework.proficiencies['instruments'].append('lute')
            t.select_instruments(framework, 2)
            framework.abilities['dexterity']['saving_throw']['proficient'] = True
            framework.abilities['charisma']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 2
        case 'cleric':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(['divine domain (life)', 'disciple of life', 'spellcasting'])
            framework.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
            framework.proficiencies['weapons'].append('simple weapons')
            framework.abilities['wisdom']['saving_throw']['proficient'] = True
            framework.abilities['charisma']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 2
        case 'druid':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(['druidic', 'spellcasting'])
            framework.proficiencies['armor'].extend(['light armor (nonmetal)', 'medium armor (nonmetal)', 'shields (nonmetal)'])
            framework.proficiencies['weapons'].extend(['club', 'dagger', 'dart', 'javelin', 'mace', 'quarterstaff', 'scimitar',
                                                       'sickle', 'sling', 'spear'])
            framework.proficiencies['tools'].append('herbalism kit')
            framework.abilities['intelligence']['saving_throw']['proficient'] = True
            framework.abilities['wisdom']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 2
        case 'fighter':
            framework.character['stats']['hit_dice'] = 'd10'
            framework.character['bio']['traits'].extend([f'fighting style ({choice(core_data.fighting_styles)})', 'second wind'])
            framework.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
            framework.abilities['strength']['saving_throw']['proficient'] = True
            framework.abilities['constitution']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
        case 'monk':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(['unarmored defense', 'martial arts'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'shortsword'])
            framework.abilities['strength']['saving_throw']['proficient'] = True
            framework.abilities['dexterity']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
        case 'paladin':
            framework.character['stats']['hit_dice'] = 'd10'
            framework.character['bio']['traits'].extend(['divine sense', 'lay on hands'])
            framework.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
            framework.abilities['wisdom']['saving_throw']['proficient'] = True
            framework.abilities['charisma']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
        case 'ranger':
            framework.character['stats']['hit_dice'] = 'd10'
            framework.character['bio']['traits'].extend([f'favored enemy ({choice(core_data.enemy_types)})', 'natural explorer'])
            framework.proficiencies['armor'].extend(['light armor', 'medium armor', 'shields'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
            framework.abilities['strength']['saving_throw']['proficient'] = True
            framework.abilities['dexterity']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
        case 'rogue':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(['expertise', 'sneak attack', "thieves' cant"])
            framework.proficiencies['armor'].extend(['light armor'])
            framework.proficiencies['weapons'].extend(['simple weapons', 'hand crossbow', 'longsword', 'rapier', 'shortsword'])
            framework.proficiencies['tools'].append("thieves' tools")
            framework.abilities['dexterity']['saving_throw']['proficient'] = True
            framework.abilities['intelligence']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 4)
        case 'sorcerer':
            framework.character['stats']['hit_dice'] = 'd6'
            framework.character['bio']['traits'].extend(['dragon ancestor',
                                                         'draconic resilience',
                                                         'spellcasting',
                                                         'sorcerous origin (draconic bloodline)'])
            framework.proficiencies['weapons'].extend(['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow'])
            framework.abilities['constitution']['saving_throw']['proficient'] = True
            framework.abilities['charisma']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 2
            framework.character['stats']['hit_points'] += 1
            if framework.character['bio']['race'] == 'dragonborn':
                ancestry = framework.character['bio']['subrace']
            else:
                ancestry = choice(core_data.draconic_ancestries)
                framework.proficiencies['languages'].append('draconic')
        case 'warlock':
            framework.character['stats']['hit_dice'] = 'd8'
            framework.character['bio']['traits'].extend(["dark one's blessing", 'otherworldly patron (the fiend)', 'pact magic'])
            framework.proficiencies['armor'].extend(['light armor'])
            framework.proficiencies['weapons'].extend(['simple weapons'])
            framework.abilities['wisdom']['saving_throw']['proficient'] = True
            framework.abilities['charisma']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 1
            spell_data.spell_list['warlock']['1st_level'].extend(['burning hands', 'command'])
        case 'wizard':
            framework.character['stats']['hit_dice'] = 'd6'
            framework.character['bio']['traits'].extend(['spellcasting', 'arcane recovery'])
            framework.proficiencies['weapons'].extend(['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow'])
            framework.abilities['intelligence']['saving_throw']['proficient'] = True
            framework.abilities['wisdom']['saving_throw']['proficient'] = True
            t.splice_profs(framework, profs)
            t.select_profs(framework, profs, 2)
            framework.spells['spell_slots']['1st_level'] = 2
        case _:
            return 'assign_class_mods: invalid class input'


def assign_bg_mods(framework):
    """Assign background mods, this is completely random for SRD compliance"""
    temp_skills = deepcopy(core_data.skill_list)
    temp_tools = deepcopy(eq_data.tools)
    temp_langs = deepcopy(core_data.languages)

    for skill in temp_skills:
        if framework.skills[skill]['proficient'] == True:
            temp_skills.remove(skill)

    s1 = choice(temp_skills)
    temp_skills.remove(s1)
    s2 = choice(temp_skills)
    temp_skills.remove(s2)

    framework.character['bio']['background']['skill_prof_1'] = s1.replace('_', ' ')
    framework.character['bio']['background']['skill_prof_2'] = s2.replace('_', ' ')
    framework.skills[s1]['proficient'] = True
    framework.skills[s2]['proficient'] = True

    for tool in temp_tools:
        if tool in framework.proficiencies['tools']:
            temp_tools.remove(tool)

    t1 = choice(temp_tools)
    framework.character['bio']['background']['tool_prof'] = t1
    framework.proficiencies['tools'].append(t1)

    for lang in temp_langs:
        if lang in framework.proficiencies['languages']:
            temp_langs.remove(lang)

    l1 = choice(temp_langs)
    framework.character['bio']['background']['lang_prof'] = l1
    framework.proficiencies['languages'].append(l1)
    framework.inventory['gold'] += randrange(5, 26, 5)


def assign_equipment(framework):
    """Assign equipment based on character class"""
    class_ = framework.character['bio']['class']
    temp_weapons_melee_simple = deepcopy(eq_data.weapons['melee']['simple'])
    temp_weapons_ranged_simple = deepcopy(eq_data.weapons['ranged']['simple'])

    match class_:
        case 'barbarian':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['weapons'].append('two handaxes')
            else:
                temp_weapons_melee_simple.remove('handaxe')
                t.select_weapons(framework, 'melee', 'simple')
            
            framework.inventory['weapons'].append(choice(['greataxe', choice(eq_data.weapons['melee']['martial'])]))
            framework.inventory['weapons'].append('four javelins')
            t.unpack_gear(framework, 'explorer')
        case 'bard':
            temp_weapons_melee_simple.remove('dagger')
            framework.inventory['weapons'].append(choice(['rapier', 'longsword', choice(temp_weapons_melee_simple)]))
            framework.inventory['misc'].append(choice(framework.proficiencies['instruments']))
            framework.inventory['armor'].append('leather')
            framework.inventory['weapons'].append('dagger')
            t.unpack_gear(framework, choice(['diplomat', 'entertainer']))
        case 'cleric':
            framework.inventory['weapons'].append(choice(['mace', 'warhammer']))
            framework.inventory['armor'].append(choice(['scale mail', 'chain mail', 'leather']))
            framework.inventory['armor'].append('shield')
            framework.inventory['misc'].append('holy symbol')
            t.unpack_gear(framework, choice(['priest', 'explorer']))
        case 'druid':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['armor'].append('wooden shield')
            else:
                t.select_weapons(framework, 'random', 'simple')
            
            framework.inventory['weapons'].append(choice(['scimitar', choice(eq_data.weapons['melee']['simple'])]))
            framework.inventory['armor'].append('leather')
            framework.inventory['misc'].append('druidic focus')
            t.unpack_gear(framework, 'explorer')
        case 'fighter':
            x = choice([1, 2])
            y = choice([1, 2])

            if x == 1:
                framework.inventory['armor'].append('chain mail')
                framework.inventory['weapons'].append('light crossbow')
                framework.inventory['ammo'].append('20 bolts')
            else:
                framework.inventory['armor'].append('leather')
                framework.inventory['weapons'].append('longbow')
                framework.inventory['ammo'].append('20 arrows')
                framework.inventory['weapons'].append('two handaxes')

            if y == 1:
                t.select_weapons(framework, 'random', 'martial')
                framework.inventory['armor'].append('shield')
            else:
                t.select_weapons(framework, 'random', 'martial', 2)
            
            t.unpack_gear(framework, choice(['dungeoneer', 'explorer']))
        case 'monk':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['weapons'].append('shortsword')
            else:
                t.select_weapons(framework, 'random', 'simple')
            
            t.unpack_gear(framework, choice(['dungeoneer', 'explorer']))
            framework.inventory['weapons'].append('10 darts')

            if 'dart' in framework.inventory['weapons']:
                framework.inventory['weapons'].remove('dart')
                framework.inventory['weapons'].remove('10 darts')
                framework.inventory['weapons'].append('11 darts')
        case 'paladin':
            x = choice([1, 2])
            y = choice([1, 2])

            if x == 1:
                t.select_weapons(framework, 'random', 'martial')
                framework.inventory['armor'].append('shield')
            else:
                t.select_weapons(framework, 'random', 'martial', 2)
            
            if y == 1:
                framework.inventory['weapons'].append('five javelins')
            else: 
                t.select_weapons(framework, 'melee', 'simple')
            
            t.unpack_gear(framework, choice(['priest', 'explorer']))
            framework.inventory['armor'].append('chain mail')
            framework.inventory['misc'].append('holy symbol')
        case 'ranger':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['weapons'].append('two shortswords')
            else:
                t.select_weapons(framework, 'melee', 'simple', 2)
            
            t.unpack_gear(framework, choice(['dungeoneer', 'explorer']))
            framework.inventory['armor'].append(choice(['scale mail', 'leather']))
            framework.inventory['weapons'].append('longbow')
            framework.inventory['ammo'].append('20 arrows')
        case 'rogue':
            framework.inventory['weapons'].append('shortsword')
            framework.inventory['weapons'].append(choice(['rapier', 'shortbow']))

            if 'shortbow' in framework.inventory['weapons']:
                framework.inventory['ammo'].append('20 arrows')
            
            t.unpack_gear(framework, choice(['burglar', 'dungeoneer', 'explorer']))
            framework.inventory['armor'].append('leather')
            framework.inventory['weapons'].append('two daggers')
            framework.inventory['misc'].append("thieves' tools")
        case 'sorcerer':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['weapons'].append('light crossbow')
                framework.inventory['ammo'].append('20 bolts')
            else:
                t.select_weapons(framework, 'random', 'simple')
            
            framework.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
            framework.inventory['weapons'].append('two daggers')
            t.unpack_gear(framework, choice(['dungeoneer', 'explorer']))

            if 'dagger' in framework.inventory['weapons']:
                framework.inventory['weapons'].remove('dagger')
                framework.inventory['weapons'].remove('two daggers')
                framework.inventory['weapons'].append('three daggers')
        case 'warlock':
            x = choice([1, 2])

            if x == 1:
                framework.inventory['weapons'].append('light crossbow')
                framework.inventory['ammo'].append('20 bolts')
            else:
                t.select_weapons(framework, 'random', 'simple')
            
            framework.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
            framework.inventory['armor'].append('leather')
            framework.inventory['weapons'].append('two daggers')
            t.unpack_gear(framework, choice(['dungeoneer', 'scholar']))
            t.select_weapons(framework, 'random', 'simple')

            if 'dagger' in framework.inventory['weapons']:
                framework.inventory['weapons'].remove('dagger')
                framework.inventory['weapons'].remove('two daggers')
                framework.inventory['weapons'].append('three daggers')
        case 'wizard':
            framework.inventory['weapons'].append(choice(['quarterstaff', 'dagger']))
            framework.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
            t.unpack_gear(framework, choice(['explorer', 'scholar']))
            framework.inventory['misc'].append('spellbook')
        case _:
            return 'assign_equipment: invalid class input'


def assign_spells(framework):
    """Assign spells based on character class"""
    class_ = framework.character['bio']['class']

    match class_:
        case 'bard':
            t.select_spells(framework, 2, 'cantrips')
            t.select_spells(framework, 4, '1st_level')
        case 'cleric':
            t.select_spells(framework, 3, 'cantrips')
            framework.spells['1st_level'] = spell_data.spell_list[class_]['1st_level']
        case 'druid':
            t.select_spells(framework, 2, 'cantrips')
            framework.spells['1st_level'] = spell_data.spell_list[class_]['1st_level']
        case 'sorcerer':
            t.select_spells(framework, 4, 'cantrips')
            t.select_spells(framework, 2, '1st_level')
        case 'warlock':
            t.select_spells(framework, 2, 'cantrips')
            t.select_spells(framework, 2, '1st_level')
        case 'wizard':
            t.select_spells(framework, 3, 'cantrips')
            t.select_spells(framework, 6, '1st_level')
        case class_ if class_ in ['barbarian', 'fighter', 'monk', 'paladin', 'ranger', 'rogue']:
            pass
        case _:
            return 'assign_spells: invalid class input'


def assign_spellcasting_mods(framework):
    """Assign spellcasting ability, DC, and spell attack modifier"""
    class_ = framework.character['bio']['class']
    prof_bonus = framework.character['stats']['proficiency_bonus']

    match class_:
        case class_ if class_ in ['bard', 'sorcerer', 'warlock']:
            framework.spells['spellcasting_ability'] = 'charisma'
            framework.spells['spell_save_dc'] = 8 + prof_bonus + framework.abilities['charisma']['modifier']
            framework.spells['spell_attack_bonus'] = prof_bonus + framework.abilities['charisma']['modifier']
        case class_ if class_ in ['cleric', 'druid']:
            framework.spells['spellcasting_ability'] = 'wisdom'
            framework.spells['spell_save_dc'] = 8 + prof_bonus + framework.abilities['wisdom']['modifier']
            framework.spells['spell_attack_bonus'] = prof_bonus + framework.abilities['wisdom']['modifier']
        case 'wizard':
            framework.spells['spellcasting_ability'] = 'intelligence'
            framework.spells['spell_save_dc'] = 8 + prof_bonus + framework.abilities['intelligence']['modifier']
            framework.spells['spell_attack_bonus'] = prof_bonus + framework.abilities['intelligence']['modifier']
        case _:
            return 'assign_spellcasting_mods: invalid class input'


def assign_ability_mods(framework):
    """Assign ability modifers"""
    for ability in core_data.ability_list:
        framework.abilities[ability]['modifier'] = floor((framework.abilities[ability]['score'] - 10) / 2)


def assign_skill_mods(framework):
    """Assign skill modifiers"""
    framework.skills['acrobatics']['modifier'] += framework.abilities['dexterity']['modifier']
    framework.skills['animal_handling']['modifier'] += framework.abilities['wisdom']['modifier']
    framework.skills['arcana']['modifier'] += framework.abilities['intelligence']['modifier']
    framework.skills['athletics']['modifier'] += framework.abilities['strength']['modifier']
    framework.skills['deception']['modifier'] += framework.abilities['charisma']['modifier']
    framework.skills['history']['modifier'] += framework.abilities['intelligence']['modifier']
    framework.skills['insight']['modifier'] += framework.abilities['wisdom']['modifier']
    framework.skills['intimidation']['modifier'] += framework.abilities['charisma']['modifier']
    framework.skills['investigation']['modifier'] += framework.abilities['intelligence']['modifier']
    framework.skills['medicine']['modifier'] += framework.abilities['wisdom']['modifier']
    framework.skills['nature']['modifier'] += framework.abilities['intelligence']['modifier']
    framework.skills['perception']['modifier'] += framework.abilities['wisdom']['modifier']
    framework.skills['performance']['modifier'] += framework.abilities['charisma']['modifier']
    framework.skills['persuasion']['modifier'] += framework.abilities['charisma']['modifier']
    framework.skills['religion']['modifier'] += framework.abilities['intelligence']['modifier']
    framework.skills['sleight_of_hand']['modifier'] += framework.abilities['dexterity']['modifier']
    framework.skills['stealth']['modifier'] += framework.abilities['dexterity']['modifier']
    framework.skills['survival']['modifier'] += framework.abilities['wisdom']['modifier']


def assign_save_mods(framework):
    """Assign saving throw modifiers"""
    for ability in core_data.ability_list:
        framework.abilities[ability]['saving_throw']['modifier'] += framework.abilities[ability]['modifier']


def assign_save_prof(framework):
    """Add proficiency bonus to saving throws"""
    for ability in core_data.ability_list:
        if framework.abilities[ability]['saving_throw']['proficient'] == True:
            framework.abilities[ability]['saving_throw']['modifier'] += framework.character['stats']['proficiency_bonus']


def assign_skill_prof(framework):
    """Add proficiency bonus to skill points"""
    for skill in core_data.skill_list:
        if framework.skills[skill]['proficient'] == True:
            framework.skills[skill]['modifier'] += framework.character['stats']['proficiency_bonus']


def assign_hp(framework):
    """Assign starting hit points"""
    hit_dice = int(framework.character['stats']['hit_dice'].strip('d'))
    framework.character['stats']['hit_points'] = hit_dice + framework.abilities['constitution']['modifier']


def assign_armor_class(framework):
    """Add armor class"""
    armor = framework.inventory['armor']
    dex_mod = framework.abilities['dexterity']['modifier']

    match armor:
        case 'padded':
            framework.character['stats']['armor_class'] = 11 + dex_mod
        case 'leather':
            framework.character['stats']['armor_class'] = 11 + dex_mod
        case 'studded leather':
            framework.character['stats']['armor_class'] = 12 + dex_mod
        case 'hide' if dex_mod <= 2:
            framework.character['stats']['armor_class'] = 12
        case 'hide' if dex_mod > 2:
            framework.character['stats']['armor_class'] = 14
        case 'chain shirt' if dex_mod <= 2:
            framework.character['stats']['armor_class'] = 13 + dex_mod
        case 'chain shirt' if dex_mod > 2:
            framework.character['stats']['armor_class'] = 15
        case 'scale mail' if dex_mod <= 2:
            framework.character['stats']['armor_class'] = 14
        case 'scale mail' if dex_mod > 2:
            framework.character['stats']['armor_class'] = 16 + dex_mod
        case 'breastplate' if dex_mod <= 2:
            framework.character['stats']['armor_class'] = 14 + dex_mod
        case 'breastplate' if dex_mod > 2:
            framework.character['stats']['armor_class'] = 16
        case 'half plate' if dex_mod <= 2:
            framework.character['stats']['armor_class'] = 15 + dex_mod
        case 'half plate' if dex_mod > 2:
            framework.character['stats']['armor_class'] = 17
        case 'ring mail':
            framework.character['stats']['armor_class'] = 14
        case 'chain mail':
            framework.character['stats']['armor_class'] = 16
        case 'splint':
            framework.character['stats']['armor_class'] = 17
        case 'plate':
            framework.character['stats']['armor_class'] = 18


def assign_unarmored_defense(framework):
    """Add class specific armor resilience"""
    class_ = framework.character['bio']['class']

    match class_:
        case 'barbarian':
            framework.character['stats']['unarmored_defense'] = 10 + framework.abilities['dexterity']['modifier'] + framework.abilities['constitution']['modifier']
            if framework.character['stats']['unarmored_defense'] > framework.character['stats']['armor_class']:
                framework.character['stats']['armor_class'] = framework.character['stats']['unarmored_defense']
        case 'monk':
            framework.character['stats']['unarmored_defense'] = 10 + framework.abilities['dexterity']['modifier'] + framework.abilities['wisdom']['modifier']
            if framework.character['stats']['unarmored_defense'] > framework.character['stats']['armor_class']:
                framework.character['stats']['armor_class'] = framework.character['stats']['unarmored_defense']
        case 'sorcerer':
            framework.character['stats']['unarmored_defense'] = 13 + framework.abilities['dexterity']['modifier']
            if framework.character['stats']['unarmored_defense'] > framework.character['stats']['armor_class']:
                framework.character['stats']['armor_class'] = framework.character['stats']['unarmored_defense']


def assign_initiative(framework):
    """Add initiative bonus"""
    framework.character['stats']['initiative'] = framework.abilities['dexterity']['modifier']


def assign_passive_perception(framework):
    """Add passive perception"""
    framework.character['stats']['passive_perception'] += framework.abilities['wisdom']['modifier']


def assign_body_mods(framework):
    """Assign bodily attributes based on race input"""
    race = framework.character['bio']['race']
    base_height = 0
    base_weight = 0
    height_mod = 0
    weight_mod = 0
    
    match race:
        case 'dragonborn':
            framework.character['bio']['size'] = 'medium'
            base_height = 66
            base_weight = 175
            height_mod = sum(roll_dice(8, 2))
            weight_mod = sum(roll_dice(6, 2))
        case 'dwarf':
            framework.character['bio']['size'] = 'medium'
            base_height = 44
            base_weight = 115
            height_mod = sum(roll_dice(4, 2))
            weight_mod = sum(roll_dice(6, 2))
        case 'elf':
            framework.character['bio']['size'] = 'medium'
            base_height = 54
            base_weight = 90
            height_mod = sum(roll_dice(10, 2))
            weight_mod = roll_dice(4, 1)
        case 'gnome':
            framework.character['bio']['size'] = 'small'
            base_height = 33
            base_weight = 35
            height_mod = sum(roll_dice(4, 2))
            weight_mod = 1
        case 'half-elf':
            framework.character['bio']['size'] = 'medium'
            base_height = 57
            base_weight = 110
            height_mod = sum(roll_dice(8, 2))
            weight_mod = sum(roll_dice(4, 2))
        case 'half-orc':
            framework.character['bio']['size'] = 'medium'
            base_height = 58
            base_weight = 140
            height_mod = sum(roll_dice(10, 2))
            weight_mod = sum(roll_dice(6, 2))
        case 'halfling':
            framework.character['bio']['size'] = 'small'
            base_height = 31
            base_weight = 35
            height_mod = sum(roll_dice(4, 2))
            weight_mod = 1
        case 'human':
            framework.character['bio']['size'] = 'medium'
            base_height = 56
            base_weight = 110
            height_mod = sum(roll_dice(10, 2))
            weight_mod = sum(roll_dice(4, 2))
        case 'tiefling':
            framework.character['bio']['size'] = 'medium'
            base_height = 56
            base_weight = 110
            height_mod = sum(roll_dice(8, 2))
            weight_mod = sum(roll_dice(4, 2))
        case _:
            return 'assign_body_type: invalid race input'

    t.body_gen(framework, base_height, base_weight, height_mod, weight_mod)


def assign_age(framework):
    """Assign age based on race input"""
    race = framework.character['bio']['race']

    match race:
        case race if race in ['dragonborn', 'human', 'tiefling']:
            framework.character['bio']['age'] = randint(18, 75)
        case 'dwarf':
            framework.character['bio']['age'] = randint(50, 300)
        case 'elf':
            framework.character['bio']['age'] = randint(100, 700)
        case 'gnome':
            framework.character['bio']['age'] = randint(40, 450)
        case 'halfling':
            framework.character['bio']['age'] = randint(20, 125)
        case 'half-elf':
            framework.character['bio']['age'] = randint(20, 175)
        case 'half-orc':
            framework.character['bio']['age'] = randint(15, 60)
        case _:
            return 'assign_age: invalid race input'
