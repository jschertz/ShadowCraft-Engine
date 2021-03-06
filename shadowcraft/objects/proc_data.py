# None should be used to indicate unknown values
# The Proc class takes these parameters:
# stat, value, duration, proc_name, default_behaviour, max_stacks=1, can_crit=True, spell_behaviour=None
# Assumed heroic trinkets have the same behaviour as the non-heroic kin.
# behaviours must have a 'default' key so that the proc is properly initialized.
allowed_procs = {
    'rogue_poison': {
        'stat': 'weird_proc',
        'value': 0,
        'duration': 0,
        'proc_name': 'rogue_poison',
        'behaviours': {'default': 'rogue_poison'}
    },
    'touch_of_the_grave': {
        'stat': 'spell_damage',
        'value': 16000,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Touch of the Grave',
        'behaviours': {'default': 'touch_of_the_grave'}
    },
    'heroic_terror_in_the_mists': {
        'stat': 'crit',
        'value': 7796,
        'duration': 20,
        'proc_name': 'Terror in the Mists',
        'behaviours': {'default': 'terror_in_the_mists'}
    },
    'terror_in_the_mists': {
        'stat': 'crit',
        'value': 6908,
        'duration': 20,
        'proc_name': 'Terror in the Mists',
        'behaviours': {'default': 'terror_in_the_mists'}
    },
    'lfr_terror_in_the_mists': {
        'stat': 'crit',
        'value': 6121,
        'duration': 20,
        'proc_name': 'Terror in the Mists',
        'behaviours': {'default': 'terror_in_the_mists'}
    },
    'heroic_bottle_of_infinite_stars': {
        'stat': 'agi',
        'value': 3653,
        'duration': 20,
        'proc_name': 'Full of Stars',
        'behaviours': {'default': 'bottle_of_infinite_stars'}
    },
    'bottle_of_infinite_stars': {
        'stat': 'agi',
        'value': 3236,
        'duration': 20,
        'proc_name': 'Full of Stars',
        'behaviours': {'default': 'bottle_of_infinite_stars'}
    },
    'lfr_bottle_of_infinite_stars': {
        'stat': 'agi',
        'value': 2866,
        'duration': 20,
        'proc_name': 'Full of Stars',
        'behaviours': {'default': 'bottle_of_infinite_stars'}
    },
    'relic_of_xuen': {
        'stat': 'agi',
        'value': 3027,
        'duration': 15,
        'proc_name': 'Relic of Xuen',
        'behaviours': {'default': 'relic_of_xuen'}
    },
    'corens_cold_chromium_coaster': {
        'stat': 'ap',
        'value': 10848,
        'duration': 10,
        'proc_name': 'Reflection of Torment',
        'behaviours': {'default': 'corens_cold_chromium_coaster'}
    },
    'searing_words': {
        'stat': 'agi',
        'value': 3386,
        'duration': 25,
        'proc_name': "Searing Words",
        'behaviours': {'default': 'searing_words'}
    },
    'windswept_pages': {
        'stat': 'haste',
        'value': 3386,
        'duration': 20,
        'proc_name': 'Windswept Pages',
        'behaviours': {'default': 'windswept_pages'}
    },
    'zen_alchemist_stone': {
        'stat': 'highest',
        'stats': ('agi', 'str', 'int'),
        'value': 4041,
        'duration': 15,
        'proc_name': 'Zen Alchemist Stone',
        'behaviours': {'default': 'zen_alchemist_stone'}
    },
    'the_gloaming_blade': {
        'stat': 'crit',
        'value': 375,
        'duration': 10,
        'max_stacks': 3,
        'proc_name': 'The Deepest Night',
        'behaviours': {'default': 'the_gloaming_blade'}
    },



    # Cata Items
    'heroic_nokaled_the_elements_of_death': {
        'stat': 'spell_damage',
        'value': 10800,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Iceblast Shadowblast Flameblast',
        'behaviours': {'default': 'nokaled_the_elements_of_death'}
    },
    'heroic_starcatcher_compass': {
        'stat': 'haste',
        'value': 3278,
        'duration': 20,
        'proc_name': 'Velocity',
        'behaviours': {'default': 'starcatcher_compass'}
    },
    'heroic_vial_of_shadows': {         # Name is a compromise to avoid conflicts
        'stat': 'physical_damage',
        'value': 17050.5,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Lightning Strike (vial hc)',
        'behaviours': {'default': 'vial_of_shadows'}
    },
    'heroic_wrath_of_unchaining': {
        'stat': 'agi',
        'value': 99,
        'duration': 10,
        'max_stacks': 10,
        'proc_name': 'Combat Trance',
        'behaviours': {'default': 'wrath_of_unchaining'}
    },
    'lfr_nokaled_the_elements_of_death': {
        'stat': 'spell_damage',
        'value': 8476,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Iceblast Shadowblast Flameblast',
        'behaviours': {'default': 'nokaled_the_elements_of_death'}
    },
    'lfr_starcatcher_compass': {
        'stat': 'haste',
        'value': 2573,
        'duration': 20,
        'proc_name': 'Velocity',
        'behaviours': {'default': 'starcatcher_compass'}
    },
    'lfr_vial_of_shadows': {            # Name is a compromise to avoid conflicts
        'stat': 'physical_damage',
        'value': 13382.5,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Lightning Strike (vial lfr)',
        'behaviours': {'default': 'vial_of_shadows'}
    },
    'lfr_wrath_of_unchaining': {
        'stat': 'agi',
        'value': 78,
        'duration': 10,
        'max_stacks': 10,
        'proc_name': 'Combat Trance',
        'behaviours': {'default': 'wrath_of_unchaining'}
    },
    'heroic_matrix_restabilizer': {     # Proc_chance is a guess and should be verified.
        'stat': 'weird_proc',
        'value': 1834,
        'duration': 30,
        'proc_name': 'Matrix Restabilized',
        'behaviours': {'default': 'matrix_restabilizer'}
    },
    'matrix_restabilizer': {            # Proc_chance is a guess and should be verified.
        'stat': 'weird_proc',
        'value': 1624,
        'duration': 30,
        'proc_name': 'Matrix Restabilized',
        'behaviours': {'default': 'matrix_restabilizer'}
    },
    'nokaled_the_elements_of_death': {
        'stat': 'spell_damage',
        'value': 9567.5,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Iceblast Shadowblast Flameblast',
        'behaviours': {'default': 'nokaled_the_elements_of_death'}
    },
    'rogue_t11_4pc': {
        'stat': 'weird_proc',
        'value': 1,
        'duration': 15,
        'proc_name': 'Deadly Scheme',
        'behaviours': {'default': 'rogue_t11_4pc'}
    },
    'starcatcher_compass': {
        'stat': 'haste',
        'value': 2904,
        'duration': 20,
        'proc_name': 'Velocity',
        'behaviours': {'default': 'starcatcher_compass'}
    },
    'swordguard_embroidery': {
        'stat': 'ap',
        'value': 'varies',
        'duration': 15,
        'proc_name': 'Swordguard Embroidery',
        'behaviours': {'default': 'swordguard_embroidery'}
    },
    'vial_of_shadows': {                # Name is a compromise to avoid conflicts
        'stat': 'physical_damage',
        'value': 15105.5,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Lightning Strike (vial n)',
        'behaviours': {'default': 'vial_of_shadows'}
    },
    'wrath_of_unchaining': {
        'stat': 'agi',
        'value': 88,
        'duration': 10,
        'max_stacks': 10,
        'proc_name': 'Combat Trance',
        'behaviours': {'default': 'wrath_of_unchaining'}
    },
    'jaws_of_retribution': {            # Legendary proc stage 1
        'stat': 'agi',
        'value': 2,
        'duration': 30,
        'max_stacks': 50,
        'proc_name': 'Suffering',
        'behaviours': {'default': 'rogue_t13_legendary_proc', 'assassination': 'rogue_t13_legendary_assassination', 'combat': 'rogue_t13_legendary_combat', 'subtlety': 'rogue_t13_legendary_subtlety'}
    },
    'maw_of_oblivion': {                # Legendary proc stage 2
        'stat': 'agi',
        'value': 5,
        'duration': 30,
        'max_stacks': 50,
        'proc_name': 'Nightmare',
        'behaviours': {'default': 'rogue_t13_legendary_proc', 'assassination': 'rogue_t13_legendary_assassination', 'combat': 'rogue_t13_legendary_combat', 'subtlety': 'rogue_t13_legendary_subtlety'}
    },
    'fangs_of_the_father': {            # Legendary proc stage 3. Given that the behaviour changes past the 30 stacks, this'll need an update
        'stat': 'agi',
        'value': 17,
        'duration': 30,
        'max_stacks': 50,
        'proc_name': 'Shadows of the Destroyer',
        'behaviours': {'default': 'rogue_t13_legendary_proc', 'assassination': 'rogue_t13_legendary_assassination', 'combat': 'rogue_t13_legendary_combat', 'subtlety': 'rogue_t13_legendary_subtlety'}
    }
}

allowed_melee_enchants = {
    'avalanche': {
        'stat': 'spell_damage',
        'value': 500,
        'duration': 0,
        'proc_name': 'Avalanche',
        'behaviours': {'default': 'avalanche_melee', 'spell': 'avalanche_spell'}
    },
    'hurricane': {
        'stat': 'haste',
        'value': 450,
        'duration': 12,
        'proc_name': 'Hurricane',
        'behaviours': {'default': 'hurricane_melee', 'spell': 'hurricane_spell'}
    },
    'landslide': {
        'stat': 'ap',
        'value': 1000,
        'duration': 12,
        'proc_name': 'Landslide',
        'behaviours': {'default': 'landslide'}
    },
    'windsong': {
        'stat': 'random',
        'stats': ('haste', 'mastery', 'crit'),
        'value': 1500,
        'duration': 12,
        'proc_name': 'Windsong',
        'behaviours': {'default': 'windsong'}
    },
    'dancing_steel': {
        'stat': 'highest',
        'stats': ('agi', 'str'),
        'value': 1650,
        'duration': 12,
        'proc_name': 'Dancing Steel',
        'behaviours': {'default': 'dancing_steel'}
    },
    'elemental_force': {
        'stat': 'spell_damage',
        'value': 3000,
        'duration': 0,
        'proc_name': 'Elemental Force',
        'behaviours': {'default': 'elemental_force'}
    },
}

# The _set_behaviour method takes these parameters:
# trigger, icd, proc_chance=False, ppm=False, on_crit=False, on_procced_strikes=True
# You can't set a value for both 'ppm' and 'proc_chance': one must be False
# Allowed triggers are: 'all_spells_and_attacks', 'all_damaging_attacks',
# 'all_attacks', 'strikes', 'auto_attacks', 'damaging_spells', 'all_spells',
# 'healing_spells', 'all_periodic_damage', 'bleeds', 'spell_periodic_damage'
# and 'hots'. The trigger 'all_melee_attacks' is sugar for 'all_attacks'.
behaviours = {
    'rogue_poison': {
        'icd': 0,
        'proc_chance': 1,
        'trigger': 'all_attacks'
    },
    'touch_of_the_grave': {
        'icd': 20,
        'proc_chance': .20,
        'trigger': 'all_attacks'
    },
    # weapon procs
    'dancing_steel': {
        'icd': 0,
        'ppm': 1,
        'trigger': 'all_melee_attacks'
    },
    'windsong': {
        'real_ppm':True,
        'icd': 0,
        'ppm': 2,
        'trigger': 'all_attacks'
    },
    'elemental_force': {
        'real_ppm':True,
        'icd': 0,
        'ppm': 10,
        'trigger': 'all_attacks'
    },
    # 5.0 Procs
    'bottle_of_infinite_stars': {
        'icd': 45,
        'proc_chance': .15,
        'trigger': 'all_attacks'
    },
    'corens_cold_chromium_coaster': {       # ICD is a guesstimate
        'icd': 50,
        'proc_chance': .10,
        'trigger': 'all_attacks',
        'on_crit': True
    },
    'relic_of_xuen': {
        'icd': 55,
        'proc_chance': .2,
        'trigger': 'all_melee_attacks',
        'on_crit': True
    },
    'searing_words': {
        'icd': 85,
        'proc_chance': .45,
        'trigger': 'all_attacks',
        'on_crit': True
    },
    'terror_in_the_mists':{
        'icd': 105,
        'proc_chance': .15,
        'trigger': 'all_attacks'
    },
    'windswept_pages': {
        'icd': 65,
        'proc_chance': .15,
        'trigger': 'all_attacks',
    },
    'zen_alchemist_stone': {                # ICD is a guesstimate
        'icd': 55,
        'proc_chance': .25,
        'trigger': 'all_attacks',
    },
    'the_gloaming_blade': {                 # PPM/ICD is a guess and should be verified.
        'icd': 0,
        'ppm': 1,
        'trigger': 'all_attacks',
    },



    # Cata Procs
    'avalanche_melee': {
        'icd': 0,
        'ppm': 5,
        'trigger': 'all_attacks'
    },
    'avalanche_spell': {                    # As per EnhSim and SimCraft
        'icd': 10,
        'proc_chance': .25,
        'trigger': 'all_periodic_damage'
    },
    'hurricane_melee': {                    # Completely guessing at proc behavior.
        'icd': 0,
        'ppm': 1,
        'trigger': 'all_spells_and_attacks',
    },
    'hurricane_spell': {
        'icd': 45,
        'proc_chance': .15,
        'trigger': 'all_spells'
    },
    'landslide': {                          # Completely guessing at proc behavior.
        'icd': 0,
        'ppm': 1,
        'trigger': 'all_attacks'
    },
    'matrix_restabilizer': {                # Proc_chance is a guess and should be verified.
        'icd': 105,
        'proc_chance': .1,
        'trigger': 'all_attacks'
    },
    'nokaled_the_elements_of_death': {
        'icd': None,
        'proc_chance': .07,
        'trigger': 'all_attacks',
        'on_procced_strikes': False
    },
    'rogue_t11_4pc': {
        'icd': None,
        'proc_chance': .01,
        'trigger': 'auto_attacks'
    },
    'starcatcher_compass': {
        'icd': 115,
        'proc_chance': .15,
        'trigger': 'all_attacks'
    },
    'swordguard_embroidery': {
        'icd': 55,
        'proc_chance': .15,
        'trigger': 'all_attacks'
    },
    'vial_of_shadows': {                    # ICD should be verified.
        'icd': 25,
        'proc_chance': .15,
        'trigger': 'all_attacks'
    },
    'wrath_of_unchaining': {                # ICD should be verified.
        'icd': None,
        'proc_chance': 1,
        'trigger': 'all_attacks'
    },
    'rogue_t13_legendary_proc': {           # Must toggle behaviour to any of the other three, this one will trigger an exception.
        'icd': None,
        'proc_chance': 0,
        'trigger': 'all_attacks'
    },
    'rogue_t13_legendary_assassination': {
        'icd': None,
        'proc_chance': .23159,
        'trigger': 'all_attacks'
    },
    'rogue_t13_legendary_combat': {
        'icd': None,
        'proc_chance': .09438,
        'trigger': 'all_attacks'
    },
    'rogue_t13_legendary_subtlety': {
        'icd': None,
        'proc_chance': .28223,
        'trigger': 'all_attacks'
    }
}
