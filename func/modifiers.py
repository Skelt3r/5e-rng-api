from copy import deepcopy
from data.core import CoreData as cd
from data.equipment import EquipmentData as ed
from data.spells import SpellData as sd
from .dice import roll_dice, roll_stats
from math import floor
from random import choice, randint, randrange

import func.tools as t

# Assign stats based on priority by class
def assign_stats(fw):
    cls = fw.character['bio']['class']
    stats = roll_stats()
    temp_abils = deepcopy(cd.ability_list)

    if cls == 'barbarian':
        temp_abils.remove('strength')
        temp_abils.remove('constitution')
        fw.abilities['strength']['score'] = stats[0]
        fw.abilities['constitution']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'bard':
        temp_abils.remove('charisma')
        temp_abils.remove('dexterity')
        fw.abilities['charisma']['score'] = stats[0]
        fw.abilities['dexterity']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'cleric':
        temp_abils.remove('wisdom')
        fw.abilities['wisdom']['score'] = stats[0]
        second = choice(['strength', 'constitution'])
        fw.abilities[second]['score'] = stats[1]
        temp_abils.remove(second)
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'druid':
        temp_abils.remove('wisdom')
        temp_abils.remove('constitution')
        temp_abils.remove('intelligence')
        fw.abilities['wisdom']['score'] = stats[0]
        fw.abilities['constitution']['score'] = stats[1]
        fw.abilities['intelligence']['score'] = stats[2]
        t.randomize_stats(fw, stats, temp_abils, 3, 6)
    elif cls == 'fighter':
        first = choice(['strength', 'dexterity'])
        fw.abilities[first]['score'] = stats[0]
        temp_abils.remove(first)

        if first == 'strength':
            temp_abils.remove('constitution')
            temp_abils.remove('dexterity')
            fw.abilities['constitution']['score'] = stats[1]
            fw.abilities['dexterity']['score'] = stats[2]
            t.randomize_stats(fw, stats, temp_abils, 3, 6)
        else:
            temp_abils.remove('intelligence')
            temp_abils.remove('constitution')
            fw.abilities['intelligence']['score'] = stats[1]
            fw.abilities['constitution']['score'] = stats[2]
            t.randomize_stats(fw, stats, temp_abils, 3, 6)

    elif cls == 'monk':
        temp_abils.remove('dexterity')
        temp_abils.remove('wisdom')
        fw.abilities['dexterity']['score'] = stats[0]
        fw.abilities['wisdom']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'paladin':
        temp_abils.remove('strength')
        temp_abils.remove('charisma')
        fw.abilities['strength']['score'] = stats[0]
        fw.abilities['charisma']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'ranger':
        temp_abils.remove('dexterity')
        temp_abils.remove('wisdom')
        fw.abilities['dexterity']['score'] = stats[0]
        fw.abilities['wisdom']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'rogue':
        temp_abils.remove('dexterity')
        fw.abilities['dexterity']['score'] = stats[0]
        second = choice(['intelligence', 'charisma'])
        fw.abilities[second]['score'] = stats[1]
        temp_abils.remove(second)
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'sorcerer' or cls == 'warlock':
        temp_abils.remove('charisma')
        temp_abils.remove('constitution')
        fw.abilities['charisma']['score'] = stats[0]
        fw.abilities['constitution']['score'] = stats[1]
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    elif cls == 'wizard':
        temp_abils.remove('intelligence')
        fw.abilities['intelligence']['score'] = stats[0]
        second = choice(['constitution', 'dexterity'])
        fw.abilities[second]['score'] = stats[1]
        temp_abils.remove(second)
        t.randomize_stats(fw, stats, temp_abils, 2, 6)
    else:
        return 'assign_stats: invalid class input'


# Assign various properties based on race input
def assign_race_mods(fw):
    race = fw.character['bio']['race']
    temp_abils = deepcopy(cd.ability_list)
    temp_langs = deepcopy(cd.languages)
    temp_skills = deepcopy(cd.skill_list)
    
    if race == 'dragonborn':
        ancestry = choice(cd.draconic_ancestries)
        fw.abilities['strength']['score'] += 2
        fw.abilities['charisma']['score'] += 1
        fw.character['stats']['speed'] += 30
        fw.character['bio']['traits'].extend(['breath weapon',
                                              'damage resistance',
                                              f'draconic ancestry ({ancestry} dragon)'])

        fw.proficiencies['languages'].extend(['common', 'draconic'])

        if ancestry in ['black', 'copper']:
            fw.character['stats']['resistances'].append('acid')
            fw.spells['innate'].append('breath weapon (acid)')
        elif ancestry in ['blue', 'bronze']:
            fw.character['stats']['resistances'].append('lightning')
            fw.spells['innate'].append('breath weapon (lightning)')
        elif ancestry in ['brass', 'gold', 'red']:
            fw.character['stats']['resistances'].append('fire')
            fw.spells['innate'].append('breath weapon (fire)')
        elif ancestry in ['silver', 'white']:
            fw.character['stats']['resistances'].append('cold')
            fw.spells['innate'].append('breath weapon (cold)')
        else:
            fw.character['stats']['resistances'].append('poison')
            fw.spells['innate'].append('breath weapon (poison)')

    elif race == 'dwarf':
        fw.abilities['constitution']['score'] += 2
        fw.character['stats']['speed'] += 25
        fw.character['stats']['resistances'].append('poison')
        fw.character['bio']['traits'].extend(['darkvision',
                                              'dwarven resilience',
                                              'dwarven combat training',
                                              'stonecunning'])

        fw.proficiencies['languages'].extend(['common', 'dwarvish'])
        fw.proficiencies['weapons'].extend(['battleaxe', 'handaxe', 'light hammer', 'warhammer'])
        tool_profs = ["smith's tools", "brewer's supplies", "mason's tools"]
        fw.proficiencies['tools'].append(choice(tool_profs))
        
    elif race == 'elf':
        fw.abilities['dexterity']['score'] += 2
        fw.character['stats']['speed'] += 30
        fw.character['bio']['traits'].extend(['darkvision', 'keen senses', 'fey ancestry', 'trance'])
        fw.proficiencies['languages'].extend(['common', 'elvish'])
        fw.skills['perception']['proficient'] = True
    elif race == 'gnome':
        fw.abilities['intelligence']['score'] += 2
        fw.character['stats']['speed'] += 25
        fw.character['bio']['traits'].extend(['darkvision', 'gnome cunning'])
        fw.proficiencies['languages'].extend(['common', 'gnomish'])
    elif race == 'halfling':
        fw.abilities['dexterity']['score'] += 2
        fw.character['stats']['speed'] += 25
        fw.character['bio']['traits'].extend(['lucky', 'brave', 'halfling nimbleness'])
        fw.proficiencies['languages'].extend(['common', 'halfling'])
    elif race == 'half-elf':
        fw.abilities['charisma']['score'] +=2
        inc = choice(temp_abils)
        fw.abilities[inc]['score'] += 1
        temp_abils.remove(inc)
        fw.abilities[choice(temp_abils)]['score'] += 1
        fw.character['stats']['speed'] += 30
        fw.character['bio']['traits'].extend(['darkvision', 'fey ancestry'])
        if 'common' in temp_langs: temp_langs.remove('common')
        temp_langs.remove('elvish')
        fw.proficiencies['languages'].extend(['common', 'elvish', choice(temp_langs)])
        prof = choice(temp_skills)
        fw.skills[prof]['proficient'] = True
        temp_skills.remove(prof)
        fw.skills[choice(temp_skills)]['proficient'] = True
    elif race == 'half-orc':
        fw.abilities['strength']['score'] += 2
        fw.abilities['constitution']['score'] += 1
        fw.character['stats']['speed'] += 30
        fw.character['bio']['traits'].extend(['darkvision', 'menacing', 'relentless endurance', 'savage attacks'])
        fw.proficiencies['languages'].extend(['common', 'orc'])
        fw.skills['intimidation']['proficient'] = True
    elif race == 'human':
        for ability in cd.ability_list: fw.abilities[ability]['score'] += 1
        fw.character['stats']['speed'] += 30
        temp_langs.remove('common')
        fw.proficiencies['languages'].extend(['common', choice(temp_langs)])
    elif race == 'tiefling':
        fw.abilities['charisma']['score'] += 2
        fw.abilities['intelligence']['score'] += 1
        fw.character['stats']['speed'] += 30
        fw.character['stats']['resistances'].append('fire')
        fw.character['bio']['traits'].extend(['darkvision', 'hellish resistance', 'infernal legacy'])
        fw.proficiencies['languages'].extend(['common', 'infernal'])
        fw.spells['cantrips'].append('thaumaturgy')
    else:
        return 'assign_race_mods: invalid race input'


# Assign subrace properties
def assign_subrace_mods(fw):
    if len(cd.subraces[fw.character['bio']['race']]) != 0:
        subrace = cd.subraces[fw.character['bio']['race']][0]
        fw.character['bio']['subrace'] = subrace

        # dwarf
        if subrace == 'hill dwarf':
            fw.abilities['wisdom']['score'] += 1
            fw.character['bio']['traits'].append('dwarven toughness')
            fw.character['stats']['hit_points'] += 1
        
        # elf
        elif subrace == 'high elf':
            fw.abilities['intelligence']['score'] += 1
            fw.character['bio']['traits'].append('elf weapon training')
            fw.proficiencies['weapons'].extend(['longsword', 'shortsword', 'shortbow', 'longbow'])
            fw.spells['cantrips'].append(choice(sd.spell_list['wizard']['cantrips']))

        # gnome
        elif subrace == 'rock gnome':
            fw.abilities['constitution']['score'] += 1
            fw.character['bio']['traits'].extend(["artificer's lore", 'tinker'])
            fw.proficiencies['tools'].append("artisan's tools")
        
        # halfling
        elif subrace == 'lightfoot':
            fw.abilities['charisma']['score'] += 1
            fw.character['bio']['traits'].append('naturally stealthy')
    
    else:
        fw.character['bio']['subrace'] = None


# Assign various modifiers based on class
def assign_class_mods(fw):
    cls = fw.character['bio']['class']
    temp_tools = deepcopy(ed.tools)

    if cls == 'bard':
        profs = cd.skill_prof_dict['all'].copy()
    else:
        profs = cd.skill_prof_dict[cls].copy()

    if cls == 'barbarian':
        fw.character['stats']['hit_dice'] = 'd12'
        fw.character['bio']['traits'].extend(['rage', 'unarmored defense'])
        fw.character['stats']['rages'] = 2
        fw.character['stats']['rage_damage'] = 2
        fw.proficiencies['armor'].extend(['light armor', 'medium armor', 'shields'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
        fw.abilities['strength']['saving_throw']['proficient'] = True
        fw.abilities['constitution']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
    elif cls == 'bard':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(['bardic inspiration', 'spellcasting'])
        fw.proficiencies['armor'].append('light armor')
        fw.proficiencies['weapons'].extend(['simple weapons', 'hand crossbow', 'longsword', 'rapier', 'shortsword'])
        fw.proficiencies['instruments'].append('lute')
        t.select_instruments(fw, 2)
        fw.abilities['dexterity']['saving_throw']['proficient'] = True
        fw.abilities['charisma']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 2
    elif cls == 'cleric':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(['divine domain (life)', 'disciple of life', 'spellcasting'])
        fw.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
        fw.proficiencies['weapons'].append('simple weapons')
        fw.abilities['wisdom']['saving_throw']['proficient'] = True
        fw.abilities['charisma']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 2
    elif cls == 'druid':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(['druidic', 'spellcasting'])
        fw.proficiencies['armor'].extend(['light armor (nonmetal)', 'medium armor (nonmetal)', 'shields (nonmetal)'])
        fw.proficiencies['weapons'].extend(['club',
                                            'dagger',
                                            'dart',
                                            'javelin',
                                            'mace',
                                            'quarterstaff',
                                            'scimitar',
                                            'sickle',
                                            'sling',
                                            'spear'])

        fw.proficiencies['tools'].append('herbalism kit')
        fw.abilities['intelligence']['saving_throw']['proficient'] = True
        fw.abilities['wisdom']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 2
    elif cls == 'fighter':
        fw.character['stats']['hit_dice'] = 'd10'
        fw.character['bio']['traits'].extend([f'fighting style ({choice(cd.fighting_styles)})', 'second wind'])
        fw.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
        fw.abilities['strength']['saving_throw']['proficient'] = True
        fw.abilities['constitution']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
    elif cls == 'monk':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(['unarmored defense', 'martial arts'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'shortsword'])
        fw.abilities['strength']['saving_throw']['proficient'] = True
        fw.abilities['dexterity']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
    elif cls == 'paladin':
        fw.character['stats']['hit_dice'] = 'd10'
        fw.character['bio']['traits'].extend(['divine sense', 'lay on hands'])
        fw.proficiencies['armor'].extend(['light armor', 'medium armor', 'heavy armor', 'shields'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
        fw.abilities['wisdom']['saving_throw']['proficient'] = True
        fw.abilities['charisma']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
    elif cls == 'ranger':
        fw.character['stats']['hit_dice'] = 'd10'
        fw.character['bio']['traits'].extend([f'favored enemy ({t.assign_favored_enemy()})', 'natural explorer'])
        fw.proficiencies['armor'].extend(['light armor', 'medium armor', 'shields'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'martial weapons'])
        fw.abilities['strength']['saving_throw']['proficient'] = True
        fw.abilities['dexterity']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
    elif cls == 'rogue':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(['expertise', 'sneak attack', "thieves' cant"])
        fw.proficiencies['armor'].extend(['light armor'])
        fw.proficiencies['weapons'].extend(['simple weapons', 'hand crossbow', 'longsword', 'rapier', 'shortsword'])
        fw.proficiencies['tools'].append("thieves' tools")
        fw.abilities['dexterity']['saving_throw']['proficient'] = True
        fw.abilities['intelligence']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 4)
    elif cls == 'sorcerer':
        fw.character['stats']['hit_dice'] = 'd6'
        fw.character['bio']['traits'].extend(['dragon ancestor',
                                              'draconic resilience',
                                              'spellcasting',
                                              'sorcerous origin (draconic bloodline)'])

        fw.proficiencies['weapons'].extend(['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow'])
        fw.abilities['constitution']['saving_throw']['proficient'] = True
        fw.abilities['charisma']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 2
        fw.character['stats']['hit_points'] += 1

        if fw.character['bio']['race'] == 'dragonborn':
            ancestry = fw.character['bio']['subrace']
        else:
            ancestry = choice(cd.draconic_ancestries)
            fw.proficiencies['languages'].append('draconic')

    elif cls == 'warlock':
        fw.character['stats']['hit_dice'] = 'd8'
        fw.character['bio']['traits'].extend(["dark one's blessing", 'otherworldly patron (the fiend)', 'pact magic'])
        fw.proficiencies['armor'].extend(['light armor'])
        fw.proficiencies['weapons'].extend(['simple weapons'])
        fw.abilities['wisdom']['saving_throw']['proficient'] = True
        fw.abilities['charisma']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 1
        sd.spell_list['warlock']['1st_level'].extend(['burning hands', 'command'])
    elif cls == 'wizard':
        fw.character['stats']['hit_dice'] = 'd6'
        fw.character['bio']['traits'].extend(['spellcasting', 'arcane recovery'])
        fw.proficiencies['weapons'].extend(['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow'])
        fw.abilities['intelligence']['saving_throw']['proficient'] = True
        fw.abilities['wisdom']['saving_throw']['proficient'] = True
        t.splice_profs(fw, profs)
        t.select_profs(fw, profs, 2)
        fw.spells['spell_slots']['1st_level'] = 2
    else:
        return 'assign_class_mods: invalid class input'


# Assign background mods, this is completely random for SRD compliance
def assign_bg_mods(fw):
    # Create temporary lists
    temp_skills = deepcopy(cd.skill_list)
    temp_tools = deepcopy(ed.tools)
    temp_langs = deepcopy(cd.languages)

    # Remove existing skill proficiencies
    for skill in temp_skills:
        if fw.skills[skill]['proficient'] == True:
            temp_skills.remove(skill)

    # Assign two random skill proficiencies
    s1 = choice(temp_skills)
    temp_skills.remove(s1)
    s2 = choice(temp_skills)
    temp_skills.remove(s2)

    fw.character['bio']['background']['skill_prof_1'] = s1.replace('_', ' ')
    fw.character['bio']['background']['skill_prof_2'] = s2.replace('_', ' ')
    fw.skills[s1]['proficient'] = True
    fw.skills[s2]['proficient'] = True

    # Remove existing tool proficiencies
    for tool in temp_tools:
        if tool in fw.proficiencies['tools']:
            temp_tools.remove(tool)

    # Assign one random tool proficiency
    t1 = choice(temp_tools)
    fw.character['bio']['background']['tool_prof'] = t1
    fw.proficiencies['tools'].append(t1)

    # Remove existing language proficiencies
    for lang in temp_langs:
        if lang in fw.proficiencies['languages']:
            temp_langs.remove(lang)

    # Assign one random language proficiency
    l1 = choice(temp_langs)
    fw.character['bio']['background']['lang_prof'] = l1
    fw.proficiencies['languages'].append(l1)

    # Assign a random amount of gold
    fw.inventory['gold'] += randrange(5, 26, 5)


# Assign equipment based on character class
def assign_equipment(fw):
    cls = fw.character['bio']['class']
    temp_weapons_melee_simple = deepcopy(ed.weapons['melee']['simple'])
    temp_weapons_ranged_simple = deepcopy(ed.weapons['ranged']['simple'])

    if cls == 'barbarian':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['weapons'].append('two handaxes')
        else:
            temp_weapons_melee_simple.remove('handaxe')
            t.select_weapons(fw, 'melee', 'simple')
        
        fw.inventory['weapons'].append(choice(['greataxe', choice(ed.weapons['melee']['martial'])]))
        fw.inventory['weapons'].append('four javelins')
        t.unpack_gear(fw, 'explorer')

    elif cls == 'bard':
        temp_weapons_melee_simple.remove('dagger')
        fw.inventory['weapons'].append(choice(['rapier', 'longsword', choice(temp_weapons_melee_simple)]))
        fw.inventory['misc'].append(choice(fw.proficiencies['instruments']))
        fw.inventory['armor'].append('leather')
        fw.inventory['weapons'].append('dagger')
        t.unpack_gear(fw, choice(['diplomat', 'entertainer']))
    elif cls == 'cleric':
        fw.inventory['weapons'].append(choice(['mace', 'warhammer']))
        fw.inventory['armor'].append(choice(['scale mail', 'chain mail', 'leather']))
        fw.inventory['armor'].append('shield')
        fw.inventory['misc'].append('holy symbol')
        t.unpack_gear(fw, choice(['priest', 'explorer']))
    elif cls == 'druid':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['armor'].append('wooden shield')
        else:
            t.select_weapons(fw, 'random', 'simple')
        
        fw.inventory['weapons'].append(choice(['scimitar', choice(ed.weapons['melee']['simple'])]))
        fw.inventory['armor'].append('leather')
        fw.inventory['misc'].append('druidic focus')
        t.unpack_gear(fw, 'explorer')

    elif cls == 'fighter':
        x = choice([1, 2])
        y = choice([1, 2])

        if x == 1:
            fw.inventory['armor'].append('chain mail')
            fw.inventory['weapons'].append('light crossbow')
            fw.inventory['ammo'].append('20 bolts')
        else:
            fw.inventory['armor'].append('leather')
            fw.inventory['weapons'].append('longbow')
            fw.inventory['ammo'].append('20 arrows')
            fw.inventory['weapons'].append('two handaxes')

        if y == 1:
            t.select_weapons(fw, 'random', 'martial')
            fw.inventory['armor'].append('shield')
        else:
            t.select_weapons(fw, 'random', 'martial', 2)
        
        t.unpack_gear(fw, choice(['dungeoneer', 'explorer']))
        
    elif cls == 'monk':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['weapons'].append('shortsword')
        else:
            t.select_weapons(fw, 'random', 'simple')
        
        t.unpack_gear(fw, choice(['dungeoneer', 'explorer']))
        fw.inventory['weapons'].append('10 darts')

        if 'dart' in fw.inventory['weapons']:
            fw.inventory['weapons'].remove('dart')
            fw.inventory['weapons'].remove('10 darts')
            fw.inventory['weapons'].append('11 darts')

    elif cls == 'paladin':
        x = choice([1, 2])
        y = choice([1, 2])

        if x == 1:
            t.select_weapons(fw, 'random', 'martial')
            fw.inventory['armor'].append('shield')
        else:
            t.select_weapons(fw, 'random', 'martial', 2)
        
        if y == 1:
            fw.inventory['weapons'].append('five javelins')
        else: 
            t.select_weapons(fw, 'melee', 'simple')
        
        t.unpack_gear(fw, choice(['priest', 'explorer']))
        fw.inventory['armor'].append('chain mail')
        fw.inventory['misc'].append('holy symbol')

    elif cls == 'ranger':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['weapons'].append('two shortswords')
        else:
            t.select_weapons(fw, 'melee', 'simple', 2)
        
        t.unpack_gear(fw, choice(['dungeoneer', 'explorer']))
        fw.inventory['armor'].append(choice(['scale mail', 'leather']))
        fw.inventory['weapons'].append('longbow')
        fw.inventory['ammo'].append('20 arrows')

    elif cls == 'rogue':
        fw.inventory['weapons'].append('shortsword')
        fw.inventory['weapons'].append(choice(['rapier', 'shortbow']))

        if 'shortbow' in fw.inventory['weapons']:
            fw.inventory['ammo'].append('20 arrows')
        
        t.unpack_gear(fw, choice(['burglar', 'dungeoneer', 'explorer']))
        fw.inventory['armor'].append('leather')
        fw.inventory['weapons'].append('two daggers')
        fw.inventory['misc'].append("thieves' tools")

    elif cls == 'sorcerer':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['weapons'].append('light crossbow')
            fw.inventory['ammo'].append('20 bolts')
        else:
            t.select_weapons(fw, 'random', 'simple')
        
        fw.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
        fw.inventory['weapons'].append('two daggers')
        t.unpack_gear(fw, choice(['dungeoneer', 'explorer']))

        if 'dagger' in fw.inventory['weapons']:
            fw.inventory['weapons'].remove('dagger')
            fw.inventory['weapons'].remove('two daggers')
            fw.inventory['weapons'].append('three daggers')

    elif cls == 'warlock':
        x = choice([1, 2])

        if x == 1:
            fw.inventory['weapons'].append('light crossbow')
            fw.inventory['ammo'].append('20 bolts')
        else:
            t.select_weapons(fw, 'random', 'simple')
        
        fw.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
        fw.inventory['armor'].append('leather')
        fw.inventory['weapons'].append('two daggers')
        t.unpack_gear(fw, choice(['dungeoneer', 'scholar']))
        t.select_weapons(fw, 'random', 'simple')

        if 'dagger' in fw.inventory['weapons']:
            fw.inventory['weapons'].remove('dagger')
            fw.inventory['weapons'].remove('two daggers')
            fw.inventory['weapons'].append('three daggers')

    elif cls == 'wizard':
        fw.inventory['weapons'].append(choice(['quarterstaff', 'dagger']))
        fw.inventory['misc'].append(choice(['component pouch', 'arcane focus']))
        t.unpack_gear(fw, choice(['explorer', 'scholar']))
        fw.inventory['misc'].append('spellbook')
    else:
        return 'assign_equipment: invalid class input'


# Assign spells
def assign_spells(fw):
    cls = fw.character['bio']['class']

    if cls in ['barbarian', 'fighter', 'monk', 'paladin', 'ranger', 'rogue']:
        pass
    elif cls == 'bard':
        t.select_spells(fw, 2, 'cantrips')
        t.select_spells(fw, 4, '1st_level')
    elif cls == 'cleric':
        t.select_spells(fw, 3, 'cantrips')
        fw.spells['1st_level'] = sd.spell_list[cls]['1st_level']
    elif cls == 'druid':
        t.select_spells(fw, 2, 'cantrips')
        fw.spells['1st_level'] = sd.spell_list[cls]['1st_level']
    elif cls == 'sorcerer':
        t.select_spells(fw, 4, 'cantrips')
        t.select_spells(fw, 2, '1st_level')
    elif cls == 'warlock':
        t.select_spells(fw, 2, 'cantrips')
        t.select_spells(fw, 2, '1st_level')
    elif cls == 'wizard':
        t.select_spells(fw, 3, 'cantrips')
        t.select_spells(fw, 6, '1st_level')
    else:
        return 'assign_spells: invalid class input'


# Assign spellcasting ability, DC, and spell attack modifier
def assign_spellcasting_mods(fw):
    cls = fw.character['bio']['class']
    prof_bonus = fw.character['stats']['proficiency_bonus']

    if cls in ['barbarian', 'fighter', 'monk', 'paladin', 'ranger', 'rogue']:
        pass
    elif cls in ['bard', 'sorcerer', 'warlock']:
        fw.spells['spellcasting_ability'] = 'charisma'
        fw.spells['spell_save_dc'] = 8 + prof_bonus + fw.abilities['charisma']['modifier']
        fw.spells['spell_attack_bonus'] = prof_bonus + fw.abilities['charisma']['modifier']
    elif cls in ['cleric', 'druid']:
        fw.spells['spellcasting_ability'] = 'wisdom'
        fw.spells['spell_save_dc'] = 8 + prof_bonus + fw.abilities['wisdom']['modifier']
        fw.spells['spell_attack_bonus'] = prof_bonus + fw.abilities['wisdom']['modifier']
    elif cls == 'wizard':
        fw.spells['spellcasting_ability'] = 'intelligence'
        fw.spells['spell_save_dc'] = 8 + prof_bonus + fw.abilities['intelligence']['modifier']
        fw.spells['spell_attack_bonus'] = prof_bonus + fw.abilities['intelligence']['modifier']
    else:
        return 'assign_spellcasting_mods: invalid class input'


# Assign ability modifers
def assign_ability_mods(fw):
    for ability in cd.ability_list:
        fw.abilities[ability]['modifier'] = floor((fw.abilities[ability]['score'] - 10) / 2)


# Assign skill modifiers
def assign_skill_mods(fw):
    fw.skills['acrobatics']['modifier'] += fw.abilities['dexterity']['modifier']
    fw.skills['animal_handling']['modifier'] += fw.abilities['wisdom']['modifier']
    fw.skills['arcana']['modifier'] += fw.abilities['intelligence']['modifier']
    fw.skills['athletics']['modifier'] += fw.abilities['strength']['modifier']
    fw.skills['deception']['modifier'] += fw.abilities['charisma']['modifier']
    fw.skills['history']['modifier'] += fw.abilities['intelligence']['modifier']
    fw.skills['insight']['modifier'] += fw.abilities['wisdom']['modifier']
    fw.skills['intimidation']['modifier'] += fw.abilities['charisma']['modifier']
    fw.skills['investigation']['modifier'] += fw.abilities['intelligence']['modifier']
    fw.skills['medicine']['modifier'] += fw.abilities['wisdom']['modifier']
    fw.skills['nature']['modifier'] += fw.abilities['intelligence']['modifier']
    fw.skills['perception']['modifier'] += fw.abilities['wisdom']['modifier']
    fw.skills['performance']['modifier'] += fw.abilities['charisma']['modifier']
    fw.skills['persuasion']['modifier'] += fw.abilities['charisma']['modifier']
    fw.skills['religion']['modifier'] += fw.abilities['intelligence']['modifier']
    fw.skills['sleight_of_hand']['modifier'] += fw.abilities['dexterity']['modifier']
    fw.skills['stealth']['modifier'] += fw.abilities['dexterity']['modifier']
    fw.skills['survival']['modifier'] += fw.abilities['wisdom']['modifier']


# Assign saving throw modifiers
def assign_save_mods(fw):
    for ability in cd.ability_list:
        fw.abilities[ability]['saving_throw']['modifier'] += fw.abilities[ability]['modifier']


# Add proficiency bonus to saving throws
def assign_save_prof(fw):
    for ability in cd.ability_list:
        if fw.abilities[ability]['saving_throw']['proficient'] == True:
            fw.abilities[ability]['saving_throw']['modifier'] += fw.character['stats']['proficiency_bonus']


# Add proficiency bonus to skill points
def assign_skill_prof(fw):
    for skill in cd.skill_list:
        if fw.skills[skill]['proficient'] == True:
            fw.skills[skill]['modifier'] += fw.character['stats']['proficiency_bonus']


# Assign starting hit points
def assign_hp(fw):
    hit_dice = int(fw.character['stats']['hit_dice'].strip('d'))
    fw.character['stats']['hit_points'] = hit_dice + fw.abilities['constitution']['modifier']


# Add armor class
def assign_armor_class(fw):
    armor = fw.inventory['armor']
    dex_mod = fw.abilities['dexterity']['modifier']

    if 'padded' in armor:
        fw.character['stats']['armor_class'] = 11 + dex_mod
    elif 'leather' in armor:
        fw.character['stats']['armor_class'] = 11 + dex_mod
    elif 'studded leather' in armor:
        fw.character['stats']['armor_class'] = 12 + dex_mod
    elif 'hide' in armor and dex_mod <= 2:
        fw.character['stats']['armor_class'] = 12
    elif 'hide' in armor and dex_mod > 2:
        fw.character['stats']['armor_class'] = 14
    elif 'chain shirt' in armor and dex_mod <= 2:
        fw.character['stats']['armor_class'] = 13 + dex_mod
    elif 'chain shirt' in armor and dex_mod > 2:
        fw.character['stats']['armor_class'] = 15
    elif 'scale mail' in armor and dex_mod <= 2:
        fw.character['stats']['armor_class'] = 14
    elif 'scale mail' in armor and dex_mod > 2:
        fw.character['stats']['armor_class'] = 16 + dex_mod
    elif 'breastplate' in armor and dex_mod <= 2:
        fw.character['stats']['armor_class'] = 14 + dex_mod
    elif 'breastplate' in armor and dex_mod > 2:
        fw.character['stats']['armor_class'] = 16
    elif 'half plate' in armor and dex_mod <= 2:
        fw.character['stats']['armor_class'] = 15 + dex_mod
    elif 'half plate' in armor and dex_mod > 2:
        fw.character['stats']['armor_class'] = 17
    elif 'ring mail' in armor:
        fw.character['stats']['armor_class'] = 14
    elif 'chain mail' in armor:
        fw.character['stats']['armor_class'] = 16
    elif 'splint' in armor:
        fw.character['stats']['armor_class'] = 17
    elif 'plate' in armor:
        fw.character['stats']['armor_class'] = 18


# Add class specific armor resilience
def assign_unarmored_defense(fw):
    cls = fw.character['bio']['class']

    if cls == 'barbarian':
        fw.character['stats']['unarmored_defense'] = 10 + fw.abilities['dexterity']['modifier'] + fw.abilities['constitution']['modifier']
        if fw.character['stats']['unarmored_defense'] > fw.character['stats']['armor_class']:
            fw.character['stats']['armor_class'] = fw.character['stats']['unarmored_defense']
    elif cls == 'monk':
        fw.character['stats']['unarmored_defense'] = 10 + fw.abilities['dexterity']['modifier'] + fw.abilities['wisdom']['modifier']
        if fw.character['stats']['unarmored_defense'] > fw.character['stats']['armor_class']:
            fw.character['stats']['armor_class'] = fw.character['stats']['unarmored_defense']
    elif cls == 'sorcerer':
        fw.character['stats']['unarmored_defense'] = 13 + fw.abilities['dexterity']['modifier']
        if fw.character['stats']['unarmored_defense'] > fw.character['stats']['armor_class']:
            fw.character['stats']['armor_class'] = fw.character['stats']['unarmored_defense']


# Add initiative bonus
def assign_initiative(fw):
    fw.character['stats']['initiative'] = fw.abilities['dexterity']['modifier']


# Add passive perception
def assign_passive_perception(fw):
    fw.character['stats']['passive_perception'] += fw.abilities['wisdom']['modifier']


# Assign bodily attributes based on race input
def assign_body_mods(fw):
    race = fw.character['bio']['race']

    base_height = 0
    base_weight = 0
    height_mod = 0
    weight_mod = 0
    
    if race == 'dragonborn':
        fw.character['bio']['size'] = 'medium'
        base_height = 66
        base_weight = 175
        height_mod = sum(roll_dice(8, 2))
        weight_mod = sum(roll_dice(6, 2))
    elif race == 'dwarf':
        fw.character['bio']['size'] = 'medium'
        base_height = 44
        base_weight = 115
        height_mod = sum(roll_dice(4, 2))
        weight_mod = sum(roll_dice(6, 2))
    elif race == 'elf':
        fw.character['bio']['size'] = 'medium'
        base_height = 54
        base_weight = 90
        height_mod = sum(roll_dice(10, 2))
        weight_mod = roll_dice(4, 1)
    elif race == 'gnome':
        fw.character['bio']['size'] = 'small'
        base_height = 33
        base_weight = 35
        height_mod = sum(roll_dice(4, 2))
        weight_mod = 1
    elif race == 'half-elf':
        fw.character['bio']['size'] = 'medium'
        base_height = 57
        base_weight = 110
        height_mod = sum(roll_dice(8, 2))
        weight_mod = sum(roll_dice(4, 2))
    elif race == 'half-orc':
        fw.character['bio']['size'] = 'medium'
        base_height = 58
        base_weight = 140
        height_mod = sum(roll_dice(10, 2))
        weight_mod = sum(roll_dice(6, 2))
    elif race == 'halfling':
        fw.character['bio']['size'] = 'small'
        base_height = 31
        base_weight = 35
        height_mod = sum(roll_dice(4, 2))
        weight_mod = 1
    elif race == 'human':
        fw.character['bio']['size'] = 'medium'
        base_height = 56
        base_weight = 110
        height_mod = sum(roll_dice(10, 2))
        weight_mod = sum(roll_dice(4, 2))
    elif race == 'tiefling':
        fw.character['bio']['size'] = 'medium'
        base_height = 56
        base_weight = 110
        height_mod = sum(roll_dice(8, 2))
        weight_mod = sum(roll_dice(4, 2))
    else:
        return 'assign_body_type: invalid race input'

    t.body_gen(fw, base_height, base_weight, height_mod, weight_mod)


# Assign age based on race input
def assign_age(fw):
    race = fw.character['bio']['race']

    if race in ['dragonborn', 'human', 'tiefling']:
        fw.character['bio']['age'] = randint(18, 75)
    elif race == 'dwarf':
        fw.character['bio']['age'] = randint(50, 300)
    elif race == 'elf':
        fw.character['bio']['age'] = randint(100, 700)
    elif race == 'gnome':
        fw.character['bio']['age'] = randint(40, 450)
    elif race == 'halfling':
        fw.character['bio']['age'] = randint(20, 125)
    elif race == 'half-elf':
        fw.character['bio']['age'] = randint(20, 175)
    elif race == 'half-orc':
        fw.character['bio']['age'] = randint(15, 60)
    else:
        return 'assign_age: invalid race input'
