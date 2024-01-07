from header_common import *
from header_parties import *
from IDs.ID_troops import *
from IDs.ID_factions import *
from IDs.ID_map_icons import *

pmf_is_prisoner = 0x0001

#from compiler import *
####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id.
#    7.2) Minimum number of troops in the stack.
#    7.3) Maximum number of troops in the stack.
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
("none","none",icon_vaegir_knight,0,fac_commoners,merchant_personality,[]),
("rescued_prisoners","Rescued Prisoners",icon_vaegir_knight,0,fac_commoners,merchant_personality,[]),
("enemy","Enemy",icon_vaegir_knight,0,fac_undeads,merchant_personality,[]),
("hero_party","Hero Party",icon_vaegir_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed.
####################################################################################################################
("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_peasant_woman,10,20)]),
("village_defenders_rom", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_vigilia,10,20),(trp_peasant_woman,1,5)] ),
("village_defenders_east", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_eastern_slinger,10,20),(trp_peasant_woman,1,5)] ),
("village_defenders_celt", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_celtic_light_clubman,5,10),(trp_celtic_archer,1,4),(trp_celtic_skirmisher,3,6),(trp_peasant_woman,1,5)] ),
("village_defenders_cal", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_caledonian_light_clubman,5,10),(trp_caledonian_archer,1,4),(trp_caledonian_skirmisher,3,6),(trp_peasant_woman,1,5)] ),
("village_defenders_germ", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_germanic_slinger,10,20),(trp_germanic_skirmisher,2,6),(trp_peasant_woman,1,5)] ),
("village_defenders_sarm", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_sarmatian_light_spearman,10,20),(trp_peasant_woman,1,5)] ),
("village_defenders_dac", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_dacian_skirmishers,10,20),(trp_peasant_woman,1,5)] ),
("village_defenders_jew", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_judean_archer,5,10),(trp_judean_slinger,5,10),(trp_judean_light_spearman,5,10),(trp_peasant_woman,1,5)] ),
("village_defenders_bos", "Village Defenders", icon_peasant, 0, fac_commoners, merchant_personality, [(trp_bosporan_light_spearman,5,10),(trp_peasant_woman,1,5)] ),

("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

# Ryan BEGIN
("looters_2","Escaped Slaves",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[]),
("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,15,55)]),
# Ryan END
("generic_bandits","Bandit Gang",icon_axeman|carries_goods(9),0,fac_outlaws,bandit_personality,[(trp_bandit,14,30),(trp_brigand,14,30),(trp_looter,5,15),]),

("steppe_bandits","Alan Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_alans,bandit_personality,[(trp_steppe_bandit,30,45),(trp_alan_horse_archer,20,35),(trp_alan_heavy_horse_archer,15,30)]),
("taiga_bandits","Illyrian Rebels",icon_axeman|carries_goods(2),0,fac_taiga_bandits,bandit_personality,[(trp_taiga_bandit,14,58),(trp_illyrian_horseman, 3, 20), (trp_illyrian_infantry, 5, 50),]),
("desert_bandits","Arab Raiders",icon_khergit|carries_goods(30),0,fac_arabian_bandits,bandit_personality,[(trp_desert_bandit,14,68),(trp_arab_noble_cav, 5,20),]),
("forest_bandits","Iberian Rebels",icon_forest_bandit|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,24,72), (trp_mercenary_horseman, 2, 30), (trp_hispanic_infantry, 2, 50), (trp_hispanic_heavy_infantry, 1, 30),]),
("mountain_bandits","Judean Rebels",icon_mountain_bandit|carries_goods(2),0,fac_mountain_bandits,judean_rebel_personality,[(trp_mountain_bandit,4,80),(trp_judean_light_spearman,0,20)]),
("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,75),(trp_sailor,5,10)]),
("black_sea_pirates","Pirates",icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_black_sea_priate,75,110),(trp_sailor,10,25)]),

("egyptian_rebels","Egyptian Rebels",icon_axeman|carries_goods(8),0,fac_egypt,bandit_personality,[(trp_egyptian_archers,15,40),(trp_egyptian_infantry_heavy,25,60),(trp_egyptian_infantry_light,25,60)]),

("garamantes","Garamantian Raiders",icon_numider|carries_goods(30),0,fac_garamantes,bandit_personality,[(trp_sarranid_horseman,50,120),(trp_garamantien_noble_horseman,30,70)]),
("gaetuli","Gaetulian Raiders",icon_numider|carries_goods(30),0,fac_gaetuli,bandit_personality,[(trp_gaetuli_horseman,50,120),(trp_gaetuli_noble_horseman,30,70)]),
("nabatean","Nabataean Raiders",icon_khergit|carries_goods(30),0,fac_nabataea,bandit_personality,[(trp_desert_bandit,25,60),(trp_arab_noble_cav,15,30),(trp_mercenary_swordsman, 40, 90),]),
("nubian","Nubian Raiders",icon_khergit|carries_goods(30),0,fac_kush,bandit_personality,[(trp_meroe_archers,30,65),(trp_meroe_infantry,25,50),(trp_meroe_axemen,30,75),]),
("irish","Irish Raiders",icon_khergit|carries_goods(30),0,fac_irish,bandit_personality,[(trp_irish_vetran,30,65),(trp_irish_skirmisher,50,115),]),
("slavs","Slavic Raiders",icon_khergit|carries_goods(30),0,fac_slavic,bandit_personality,[(trp_slavic_vetran,30,65),(trp_slavic_skirmisher,50,115),]),
("danes","Herulian Raiders",icon_khergit|carries_goods(30),0,fac_danish,bandit_personality,[(trp_danish_vetran,30,65),(trp_danish_skirmisher,50,115),]),
("georgians","Caucasian Raiders",icon_khergit|carries_goods(30),0,fac_georgians,bandit_personality,[(trp_georgian_noble_archer,30,65),(trp_georgian_light_archer,50,115),]),
("sakas","Saka Raiders",icon_khergit|carries_goods(30),0,fac_dahae,bandit_personality,[(trp_saka_amazon,5,15),(trp_saka_heavy_cavalry,25,40),(trp_saka_horse_archer,35,55),]),

("furor_teutonicus","Furor Teutonics",icon_kingdom_4_soldier_b|carries_goods(2),0,fac_furor_teutonicus,bandit_personality,[(trp_germanic_berserker,5,20), (trp_germanic_skirmisher,7,68), (trp_germanic_light_clubman,10,80),(trp_germanic_light_spearman,10,80)]),
("pictonen","Young Warriors",icon_kingdom_2_soldier_b|carries_goods(2),0,fac_picton,bandit_personality,[(trp_celtic_naked_swordman,15,30), (trp_celtic_skirmisher,17,48), (trp_celtic_light_clubman,10,30)]),

("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),

#SB : fix icon
("merchant_caravan","Merchant Caravan",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25),(trp_package_slave,3,10)]),
("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

("village_farmers","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[]),

("village_bosporan","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_bosporan_peasant,15,25),]),
("village_sarmatian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_sarmatian_peasant,15,25),]),
("village_judean","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_judean_peasant,15,25),]),
("village_parthian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_persian_peasant,5,15),(trp_parthian_peasant,5,10),]),
("village_persian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_persian_peasant,15,25),]),
("village_roman","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_roman_peasant,15,25),]),
("village_celtic","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_celtic_peasant,15,25),]),
("village_germanic","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_germanic_peasant,15,25),]),
("village_dacian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_dacian_peasant,15,25),]),
("village_armenian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_armenian_peasant,15,25),]),
("village_arabian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_arab_peasant,15,25),]),
("village_berber","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_berber_peasant,15,25),]),
("village_garmantian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_garamantian_peasant,15,25),]),
("village_egyptian","Villagers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_african_man,5,10),(trp_judean_peasant,10,15),]),

("spy_partners", "Unremarkable Travellers", icon_vaegir_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
("runaway_serfs","Runaway slaves",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_slave,6,7), (trp_slave_female,3,3)]),
("spy", "Ordinary Townsman", icon_vaegir_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_vaegir_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

("forager_party","Foraging Party",icon_vaegir_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("scout_party","Scouts",icon_vaegir_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
("patrol_party","Patrol",icon_vaegir_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#SB : icon change to make it stand out more
("messenger_party","Messenger",icon_flagbearer_b|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("raider_party","Raiders",icon_vaegir_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[(trp_brigand, 90,105)]),
("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40),(trp_package_slave,3,10)]),
("prisoner_train_party","Slave Train",icon_mule|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_mercenary_horseman,50,60),]),
("default_prisoners","Default Prisoners",icon_vaegir_knight,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# ("center_reinforcements","Reinforcements", icon_axeman|pf_show_faction|carries_goods(4),0,fac_commoners,escorted_merchant_personality,[]),

("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
##mercenary bands
("mercenary_guard", "Mercenary Guard", 0, 0, fac_commoners, 0,
[("trp_watchman", 30,30),("trp_caravan_guard", 15,15),("trp_mercenary_crossbowman",15,15),] ),#60
("mercenary_warband", "Mercenary Warband", 0, 0, fac_commoners, 0,
[("trp_mercenary_swordsman", 30,30),("trp_hired_blade", 15,15),("trp_mercenary_crossbowman",15,15),] ),#60
("mercenary_cav", "Mercenary Cavalry", 0, 0, fac_commoners, 0,
[("trp_mercenary_horseman", 20,20),("trp_mercenary_cavalry", 30,30),] ),#50

("mercenary_illyrian", "Illyrian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_illyrian_infantry", 40,40),("trp_illyrian_horseman", 20,20),] ),#60
("gladiatores", "Gladiatores", 0, 0, fac_commoners, 0,
[("trp_gladiator_murmillo", 20,20),("trp_gladiator_thraex", 10,10),("trp_gladiator_sagittarius", 15,15),("trp_gladiator_retiarius", 25,25),] ),#70
("mercenary_rhodos", "Mercenaries from Rhodos", 0, 0, fac_commoners, 0,
[("trp_slinger_rhodos", 60,60),] ),#60
("mercenary_kreta", "Mercenaries from Kreta", 0, 0, fac_commoners, 0,
[("trp_kreta_archer", 60,60),] ),#60
("mercenary_hispanic", "Hispanic Mercenaries", 0, 0, fac_commoners, 0,
[("trp_hispanic_infantry", 40,40),("trp_hispanic_heavy_infantry", 20,20),] ),#60
("mercenary_scythian", "Scythian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_scythian_horse_archer", 25,25),("trp_scythian_medium_cavalry", 15,15),(trp_scythian_cataphract, 10,10),] ),#50
("mercenary_alan", "Alan Mercenaries", 0, 0, fac_commoners, 0,
[("trp_steppe_bandit", 25,25),("trp_alan_heavy_horse_archer", 10,10),("trp_alan_horse_archer",15,15),] ),#50
("mercenary_celtic", "Celtic Mercenaries", 0, 0, fac_commoners, 0,
[("trp_celtic_freeman", 40,40),("trp_celtic_elite_swordsman", 20,20),] ),#60
("mercenary_irish", "Irish Mercenaries", 0, 0, fac_commoners, 0,
[("trp_irish_skirmisher", 30,30),("trp_irish_vetran", 20,20),] ),#60
("mercenary_germanic", "Germanic Mercenaries", 0, 0, fac_commoners, 0,
[("trp_germanic_hunter", 25,25),("trp_germanic_free_spearman", 20,20),("trp_germanic_free_nobleman",15,15),] ),#60
("mercenary_nightwarriors", "Night Warriors", 0, 0, fac_commoners, 0,
[("trp_germanic_nightwarrior", 40,40),("trp_germanic_hunter", 20,20),] ),#60
("mercenary_dani", "Herulian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_danish_skirmisher", 30,30),("trp_danish_vetran", 20,20),] ),#60
("mercenary_lombard", "Winnuli Mercenaries", 0, 0, fac_commoners, 0,
[("trp_lombard_skirmisher", 30,30),("trp_lombard_vetran", 20,20),] ),#60
("mercenary_slavic", "Gelonian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_slavic_skirmisher", 30,30),("trp_slavic_vetran", 20,20),] ),#60
("mercenary_persian", "Persian Hillmen", 0, 0, fac_commoners, 0,
[("trp_persian_picaxe_man", 60,60),] ),#60
("mercenary_cataphracts", "Persian Cataphracts", 0, 0, fac_commoners, 0,
[("trp_persian_noble_cav", 30,30),] ),#60
("mercenary_indian", "Indian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_indian_archer", 25,25),("trp_indian_spearman", 35,35),] ),#60
("mercenary_garamantian", "Garamantian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_sarranid_horseman", 30,30),("trp_garamantien_noble_horseman", 20,20),] ),#50
("mercenary_gaetulian", "Gaetulian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_gaetuli_horseman", 30,30),("trp_gaetuli_noble_horseman", 30,30),] ),#60
("mercenary_moreo", "Nubian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_meroe_archers", 30,30),("trp_meroe_infantry", 15,15),("trp_meroe_axemen", 15,15)] ),#60
("mercenary_egyptian", "Egyptian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_egyptian_archers", 20,20),("trp_egyptian_infantry_heavy", 20,20),("trp_egyptian_infantry_light", 20,20)] ),#60
("mercenary_arab", "Arabian Mercenaries", 0, 0, fac_commoners, 0,
[("trp_arab_noble_archers", 30,30),("trp_arab_spearmen", 30,30)] ),#60
("mercenary_arab_cav", "Arabian Cavalry Mercenaries", 0, 0, fac_commoners, 0,
[("trp_desert_bandit", 30,30),("trp_arab_noble_cav", 20,20),] ),#60
("mercenary_palmyra", "Palmyrean Mercenaries", 0, 0, fac_commoners, 0,
[("trp_palmyra_infantry", 40,40),("trp_palmyra_cataphract", 20,20),] ),#60
("mercenary_caucasia","North Caucasian Raiders",icon_khergit|carries_goods(30),0,fac_commoners,0,
[(trp_georgian_noble_archer,40,40),(trp_georgian_light_archer,20,20),]),
("mercenary_dahae","Saka Raiders",icon_khergit|carries_goods(30),0,fac_commoners,0,
[(trp_saka_horse_archer,35,35),(trp_saka_heavy_cavalry,25,25),]),
("mercenary_saka_amazon","Saka Amazons",icon_khergit|carries_goods(30),0,fac_commoners,0,
[(trp_saka_amazon,50,50)]),

("custom_infantry_retinue","Infantry retinue (custom)",icon_gray_knight,0,fac_commoners,aggressiveness_0|courage_15,
[(trp_custom_standard_bearer,1,1),(trp_custom_hornman,1,1),(trp_custom_infantry,80,80)]),
("custom_cavalry_retinue","Cavalry retinue (custom)",icon_gray_knight,0,fac_commoners,aggressiveness_0|courage_15,
[(trp_custom_standard_bearer_cav,1,1),(trp_custom_skirmisher_cav,30,30),(trp_custom_cav_barb,30,30)]),
("custom_skirmisher_retinue","Skirmisher retinue (custom)",icon_gray_knight,0,fac_commoners,aggressiveness_0|courage_15,
[(trp_custom_standard_bearer_skirmisher,1,1),(trp_custom_hornman_skirmisher,1,1),(trp_custom_skirmisher,40,40),(trp_custom_archer,40,40)]),

##town watch templates
("kingdom_1_town_watch", "Dacian Townwatch", 0, 0, fac_commoners, 0,
[(trp_dacian_light_spearman,25,25),(trp_dacian_light_swordman,15,15),(trp_dacian_skirmishers,10,10),(trp_dacian_archers, 25,25)] ),#75
("kingdom_2_town_watch", "Celtic Townwatch", 0, 0, fac_commoners, 0,
[(trp_celtic_light_clubman,25,25),(trp_celtic_light_spearman,15,15),(trp_celtic_skirmisher,10,10),(trp_celtic_archer,25,25)] ),#75
("kingdom_2_1_town_watch", "Caledonian Townwatch", 0, 0, fac_commoners, 0,
[(trp_caledonian_light_clubman,15,15),(trp_caledonian_light_spearman,25,25),(trp_caledonian_skirmisher,10,10),(trp_caledonian_archer, 25,25)] ),
("kingdom_3_town_watch", "Sarmatian Townwatch", 0, 0, fac_commoners, 0,
[(trp_sarmatian_light_spearman,30,30),(trp_sarmatian_archers,35,35)] ),#60
("kingdom_4_town_watch", "Germanic Townwatch", 0, 0, fac_commoners, 0,
[(trp_germanic_light_clubman,25,25),(trp_germanic_light_spearman,15,15),(trp_germanic_archer,15,15),(trp_germanic_skirmisher,10,10),(trp_germanic_slinger,10,10)] ),
("kingdom_5_town_watch", "Caucasian Townwatch", 0, 0, fac_commoners, 0,
[(trp_armenian_horsearcher,15,15),(trp_armenian_skrimisher,10,10),(trp_armenian_spear_levy,25,25),(trp_armenian_light_axeman,15,15),(trp_armenian_slinger,10,10)] ),
("kingdom_6_town_watch", "Persian Townwatch", 0, 0, fac_commoners, 0,
[(trp_eastern_skrimisher,15,15),(trp_eastern_light_archer,20,20),(trp_eastern_light_axeman,25,25),(trp_eastern_slinger,15,15),] ),
("kingdom_7_town_watch", "Vigilia", 0, 0, fac_commoners, 0,
[(trp_aux_vigiles_centurio,2,2),(trp_vigilia,40,40),(trp_aux_archer,25,25),(trp_aux_inf,5,5),(trp_ballistarii,5,5)] ),
("kingdom_8_town_watch", "Judean Townwatch", 0, 0, fac_commoners, 0,
[(trp_judean_light_spearman,25,25),(trp_judean_light_clubman,25,25),(trp_judean_slinger,15,15),(trp_judean_archer,10,10),] ),
("kingdom_9_town_watch", "Bosphoran Townwatch", 0, 0, fac_commoners, 0,
[(trp_sarmatian_archers,15,15),(trp_bosporan_light_spearman,45,45),(trp_bosporan_archer,15,15)] ),
("kingdom_19_town_watch", "Batavan Townwatch", 0, 0, fac_commoners, 0,
[(trp_germanic_light_clubman,25,25),(trp_germanic_light_spearman,25,25),(trp_aux_archer_batavorum,25,25)] ),

# Reinforcements
("kingdom_1_reinforcements_a", "Dacian Levies", 0, 0, fac_commoners, 0,
[(trp_dacian_light_spearman,25,25),(trp_dacian_light_swordman,25,25),(trp_dacian_skirmishers,25,25),(trp_dacian_hornman,1,1),(trp_dacian_standard_bearer,1,1)] ),#75
("kingdom_1_reinforcements_b", "Dacian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_dacian_flaxman,15,15),(trp_dacian_flaxman_heavy,15,15),(trp_dacian_archers,15,15),(trp_dacian_heavy_inf, 15,15),(trp_dacian_noble_inf,15,15),(trp_dacian_hornman,1,1),(trp_dacian_standard_bearer,1,1)] ),#76
("kingdom_1_reinforcements_c", "Dacian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_dacian_noble_cav,25,25),(trp_dacian_noble_inf,25,25),(trp_dacian_hornman,1,1),(trp_dacian_standard_bearer,1,1)] ),#51

("kingdom_2_reinforcements_a", "Celtic Levies", 0, 0, fac_commoners, 0,
[(trp_celtic_light_clubman,25,25),(trp_celtic_light_spearman,25,25),(trp_celtic_skirmisher,25,25),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),#75
("kingdom_2_reinforcements_b", "Celtic Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_celtic_archer,25,25),(trp_celtic_naked_swordman,30,30),(trp_celtic_noble_swords,20,20),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),#76
("kingdom_2_reinforcements_c", "Celtic Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_celtic_horseman,25,25),(trp_celtic_noble_swords,25,25),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),#51

("kingdom_2_1_reinforcements_a", "Caledonian Levies", 0, 0, fac_commoners, 0,
[(trp_caledonian_light_clubman,25,25),(trp_caledonian_light_spearman,25,25),(trp_caledonian_skirmisher,25,25),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),
("kingdom_2_1_reinforcements_b", "Caledonian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_caledonian_archer,25,25),(trp_caledonian_naked_swordman,30,30),(trp_caledonian_noble_swords,20,20),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),
("kingdom_2_1_reinforcements_c", "Caledonian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_caledonian_horseman,25,25),(trp_caledonian_noble_swords,25,25),(trp_celtic_hornman,1,1),(trp_celtic_standard_bearer,1,1)] ),

("kingdom_3_reinforcements_a", "Sarmatian Levies", 0, 0, fac_commoners, 0,
[(trp_sarmatian_light_spearman,35,35),(trp_sarmatian_archers,30,30)] ),#60
("kingdom_3_reinforcements_b", "Sarmatian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_sarmatian_light_horsearcher,20,20),(trp_sarmatian_light_horseman,20,20),(trp_sarmatian_heavy_horsearcher,10,10)] ),#50
("kingdom_3_reinforcements_c", "Sarmatian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_sarmatian_heavy_horseman,20,20),(trp_sarmatian_noble_horseman,20,20),(trp_sarmatian_heavy_horsearcher,5,5)] ),#45

("kingdom_4_reinforcements_a", "Germanic Levies", 0, 0, fac_commoners, 0,
[(trp_germanic_light_clubman,25,25),(trp_germanic_light_spearman,25,25),(trp_germanic_skirmisher,15,15),(trp_germanic_slinger,10,10),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),
("kingdom_4_reinforcements_b", "Germanic Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_germanic_berserker,10,10),(trp_germanic_archer,20,20),(trp_germanic_cavalry,15,15),(trp_germanic_noble_swordsman,15,15),(trp_germanic_noble_spearman,15,15),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),
("kingdom_4_1_reinforcements_b", "East-Germanic Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_slavic_vetran, 15,15),(trp_germanic_berserker,10,10),(trp_germanic_archer,20,20),(trp_slavic_skirmisher,15,15),(trp_germanic_noble_spearman,15,15),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),
("kingdom_4_reinforcements_c", "West-Germanic Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_germanic_noble_swordsman,25,25),(trp_germanic_noble_spearman,25,25),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),

("kingdom_5_reinforcements_a", "Caucasian Levies", 0, 0, fac_commoners, 0,
[(trp_armenian_skrimisher,15,15),(trp_armenian_spear_levy,25,25),(trp_armenian_light_axeman,25,25),(trp_armenian_slinger,10,10),(trp_caucasian_hornman, 1,1),(trp_caucasian_standard_bearer,1,1)] ),
("kingdom_5_reinforcements_b", "Armenian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_armenian_heavy_inf,25,25),(trp_armenian_medium_horseman,25,25),(trp_armenian_heavy_maceman,25,25),(trp_armenian_hornman,1,1),(trp_armenian_standard_bearer,1,1)] ),
("kingdom_5_reinforcements_c", "Armenian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_armenian_cataphract,15,15),(trp_armenian_horsearcher,15,15),(trp_armenian_elite_infantry,20,20),(trp_armenian_hornman,1,1),(trp_armenian_standard_bearer,1,1)] ),

("kingdom_5_1_reinforcements_b", "Caucasian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_caucasian_heavy_spearman,45,45),(trp_armenian_heavy_maceman,30,30),(trp_caucasian_hornman, 1,1),(trp_caucasian_standard_bearer,1,1)] ),
("kingdom_5_1_reinforcements_c", "Caucasian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_caucasian_medium_horsearcher,25,25),(trp_caucasian_cataphract,26,26),] ),

("kingdom_6_reinforcements_a", "Persian Levies", 0, 0, fac_commoners, 0,
[(trp_eastern_skrimisher,15,15),(trp_eastern_light_archer,20,20),(trp_eastern_light_axeman,25,25),(trp_eastern_slinger,15,15),(trp_parthian_hornman,1,1),(trp_parthian_standard_bearer,1,1)] ),
("kingdom_6_reinforcements_b", "Parthian Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_eastern_heavy_spearman,15,15),(trp_eastern_heavy_inf,20,20),(trp_eastern_horsearcher,20,20),(trp_parthian_hornman,1,1),(trp_eastern_elite_infantry,10,10),(trp_eastern_medium_horseman,10,10)] ),
("kingdom_6_reinforcements_c", "Parthian Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_eastern_cataphract,26,26),(trp_eastern_medium_horseman,10,10),(trp_eastern_horsearcher,15,15),] ),

("kingdom_7_reinforcements_a", "Turmae Auxiliarum", 0, 0, fac_commoners, 0,
[(trp_aux_cav_decurio,1,1),(trp_aux_cav,25,25),] ),
("kingdom_7_reinforcements_b", "Cohors Vigiliarum", 0, 0, fac_commoners, 0,
[(trp_aux_vigiles_centurio,1,1),(trp_aux_archer,20,20),(trp_vigilia,40,40)] ),
("kingdom_7_reinforcements_c", "Manipulus Auxiliarum", 0, 0, fac_commoners, 0,
[(trp_aux_vigiles_centurio,1,1),(trp_aux_archer,25,25),(trp_aux_inf,50,50)] ),

("kingdom_8_reinforcements_a", "Judean Levies", 0, 0, fac_commoners, 0,
[(trp_judean_light_spearman,25,25),(trp_judean_light_clubman,25,25),(trp_judean_slinger,15,15),(trp_mountain_bandit,10,10),(trp_judean_hornman,1,1),(trp_judean_standard_bearer,1,1)] ),
("kingdom_8_reinforcements_b", "Judean Retinue", 0, 0, fac_commoners, 0,
[(trp_judean_elite,35,35),(trp_judean_archer,20,20),(trp_judean_skirmisher,20,20),(trp_judean_hornman,1,1),(trp_dacian_standard_bearer,1,1)] ),
("kingdom_8_reinforcements_c", "Judean Guard", 0, 0, fac_commoners, 0,
[(trp_judean_cav,10,10),(trp_judean_hornman,1,1),(trp_dacian_standard_bearer,1,1),(trp_judean_guard, 35,35),(trp_judean_guard_archer,25,25)] ),

("kingdom_9_reinforcements_a", "Bosphoran Levies", 0, 0, fac_commoners, 0,
[(trp_sarmatian_light_spearman,20,20),(trp_bosporan_light_spearman,40,40),(trp_sarmatian_light_horsearcher,15,15),(trp_bosporan_hornman,1,1),(trp_bosporan_standard_bearer,1,1)] ),
("kingdom_9_reinforcements_b", "Bosphoran Lordly Retinue", 0, 0, fac_commoners, 0,
[(trp_bosporan_light_spearman,10,10),(trp_bosporan_elite,40,40),(trp_bosporan_archer, 25,25),(trp_bosporan_hornman,1,1),(trp_bosporan_standard_bearer,1,1)] ),
("kingdom_9_reinforcements_c", "Bosphoran Royal Retinue", 0, 0, fac_commoners, 0,
[(trp_sarmatian_light_horsearcher,10,10),(trp_sarmatian_heavy_horseman,15,15),(trp_bosporan_cav,25,25),] ),

("kingdom_19_reinforcements_a", "Romano-Germanic Levies", 0, 0, fac_commoners, 0,
[(trp_germanic_light_clubman,25,25),(trp_germanic_light_spearman,25,25),(trp_germanic_skirmisher,25,25),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),
("kingdom_19_reinforcements_b", "Romano-Germanic Cohort", 0, 0, fac_commoners, 0,
[(trp_aux_inf_batavorum,30,30),(trp_germanic_archer,10,10),(trp_aux_archer_batavorum,15,15),(trp_aux_cav_batavorum,25,25),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),
("kingdom_19_reinforcements_c", "Romano-Germanic Retinue", 0, 0, fac_commoners, 0,
[(trp_germanic_noble_spearman,25,25),(trp_germanic_noble_swordsman,25,25),(trp_germanic_hornman,1,1),(trp_germanic_standard_bearer,1,1)] ),


("steppe_bandit_lair" ,"Alan Camp",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_alans,bandit_personality,[(trp_steppe_bandit,15,30)]),
("taiga_bandit_lair","Illyrian Lair",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_taiga_bandits,bandit_personality,[(trp_taiga_bandit,15,30)]),
("desert_bandit_lair" ,"Arabic Camp",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_arabian_bandits,bandit_personality,[(trp_desert_bandit,15,30)]),
("egyptian_bandit_lair" ,"Old Egyptian Fortress",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_egypt,bandit_personality,[(trp_egyptian_infantry_light,5,10),(trp_egyptian_archers,5,10),(trp_egyptian_infantry_heavy,5,10)]),
("nabatean_lair" ,"Nabataean Camp",icon_gaetulian_town|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_nabataea,bandit_personality,[(trp_desert_bandit,15,30)]),
("nubian_lair" ,"Nubian Village",icon_village_desert|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_kush,bandit_personality,[(trp_meroe_archers,5,10),(trp_meroe_infantry,10,20)]),
("numidian_bandit_lair" ,"Garamantian Village",icon_village_desert|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_garamantes,bandit_personality,[(trp_sarranid_horseman,15,30)]),
("gaetuli_bandit_lair" ,"Gaetulian Camp",icon_gaetulian_town|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_gaetuli,bandit_personality,[(trp_gaetuli_horseman,15,30)]),
("forest_bandit_lair" ,"Hispanic Hideout",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,15,30)]),
("mountain_bandit_lair" ,"Judean Hideout",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,15,30)]),
("sea_raider_lair","Sea Raider Landing",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,30)]),
("black_sea_pirates_lair","Pirate hideout",icon_map_island|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_black_sea_priate,30,60)]),

("saka_camp","Saka Camp",icon_village_barbarian|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_dahae,bandit_personality,[(trp_saka_horse_archer,15,30)]),
("looter_lair","Kidnappers' Hideout",icon_map_bandit_lair|carries_goods(20)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,18)]),

("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,30)]),

("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,quest_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25),(trp_package_slave,3,10)]),
# #recruiter kit begin
# ("dplmc_recruiter","Recruiter",icon_flagbearer_b|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
# #recruiter kit end
##diplomacy end
("refugees","Refugees",icon_woman,0,fac_innocents,merchant_personality,[(trp_refugee,19,48)]),

("women","Peasant Women",icon_woman,0,fac_innocents,merchant_personality,[(trp_peasant_woman,8,15)]),
("sarranid_women","Peasant Women",icon_woman,0,fac_innocents,merchant_personality,[(trp_peasant_woman,3,8)]),
("khergit_women","Peasant Women",icon_woman,0,fac_innocents,merchant_personality,[(trp_peasant_woman,3,8)]),
# ("khergit_farmers","Village Traders",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),]),
# ("sarranid_farmers","Village Traders",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,5,10)]),

#first cohort
("legio_i_adjutrix_staff","Cohors Prima Legio I Adjuterix",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_i_adjutrix,160,160),(trp_aquilifer_i,1,1),(trp_vexilarius_i,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_iii_augusta_staff","Cohors Prima Legio III Augusta ",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_iii_augusta,160,160),(trp_aquilifer_iii,1,1),(trp_vexilarius_iii,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_v_alaudae_staff","Cohors Prima Legio V Alaudae",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_v_alaudae,160,160),(trp_aquilifer_v_alaudae,1,1),(trp_vexilarius_v_alaudae,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_xxi_rapax__staff","Cohors Prima Legio XXI Rapax",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xxi_rapax,160,160),(trp_aquilifer_xxi,1,1),(trp_vexilarius_xxi,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_vii_galbia_staff","Cohors Prima Legio VII Galbia",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vii_galbia,160,160),(trp_aquilifer_vii,1,1),(trp_vexilarius_vi_vict,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_vi_victrix_staff","Cohors Prima Legio VI Victrix",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vi_victrix,160,160),(trp_aquilifer_vi_vict,1,1),(trp_vexilarius_vi_vict,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_xi_claudia_staff","Cohors Prima Legio XI Claudia",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xi_claudia,160,160),(trp_aquilifer_xi,1,1),(trp_vexilarius_xi,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_xiii_gemina_staff","Cohors Prima Legio XIII Gemina",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xiii_gemina,160,160),(trp_aquilifer_xiii,1,1),(trp_vexilarius_xi,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_v_macedonia_staff","Cohors Prima Legio V Macedonica",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_v_macedonia,160,160),(trp_aquilifer_v_mac,1,1),(trp_vexilarius_v_mac,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_vi_ferrata_staff","Cohors Prima Legio VI Ferrata",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vi_ferrata,160,160),(trp_aquilifer_vi_fer,1,1),(trp_vexilarius_vi_fer,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("legio_x_fretensis_staff","Cohors Prima Legio X Fretensis",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_x_fretensis,160,160),(trp_aquilifer_x,1,1),(trp_vexilarius_x,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("praetoriani_staff","Cohors Prima Praetoriani",icon_pretorian_eques,0,fac_kingdom_7,soldier_personality,
[(trp_praetoriani_milites,160,160),(trp_aquilifer_praetoriani,1,1),(trp_vexilarius_praetoriani,1,1),(trp_centurio_east,1,1),(trp_legatus_legionis,1,1),(trp_signifer,1,1)]),
("player_legion_staff","Staff",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,
[(trp_custom_legionary,160,160),(trp_custom_aquilifer,1,1), (trp_custom_vexilarius,1,1), (trp_custom_tribunus,1,1),(trp_custom_primus_pilius,1,1),(trp_custom_signifer,1,1)]),

#standard cohort
("legio_i_adjutrix_cohors","Cohors Legio I Adjuterix",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_i_adjutrix,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1)]),#
("legio_iii_augusta_cohors","Cohors Legio III Augusta",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_iii_augusta,80,80), (trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1)]),
("legio_v_alaudae_cohors","Cohors Legio V Alaudae",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_v_alaudae,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_xxi_rapax__cohors","Cohors Legio XXI Rapax",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xxi_rapax,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1)]),
("legio_vii_galbia_cohors","Cohors Legio VII Galbia",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vii_galbia,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_vi_victrix_cohors","Cohors Legio VI Victrix",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vi_victrix,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_xi_claudia_cohors","Cohors Legio XI Claudia",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xi_claudia,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_xiii_gemina_cohors","Cohors Legio XIII Gemina",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_xiii_gemina,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_v_macedonia_cohors","Cohors Legio V Macedonica",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_v_macedonia,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_vi_ferrata_cohors","Cohors Legio VI Ferrata",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_vi_ferrata,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("legio_x_fretensis_cohors","Cohors Legio X Fretensis",icon_gray_knight,0,fac_kingdom_7,soldier_personality,
[(trp_legio_x_fretensis,80,80),(trp_centurio_west,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("praetoriani_cohors","Cohors Praetoriani",icon_pretorian_eques,0,fac_kingdom_7,soldier_personality,
[(trp_praetoriani_milites,80,80),(trp_centurio_preatoriani,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("player_cohort","cohort",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,
[(trp_custom_legionary,80,80),(trp_custom_centurio,1,1),(trp_custom_signifer,1,1),(trp_custom_cornicen,1,1)]),

#auxilia##9 inf cohorts
("cohors_aux","Cohors Auxiliarum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_signifer,1,1),(trp_cornicen,1,1),(trp_aux_centurio,1,1),(trp_aux_inf, 80, 80),]),
("cohors_alp","Cohors Alporum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_alporum, 80, 80)]),
("cohors_afr","Cohors Maurorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_maurorum, 80, 80)]),
("cohors_hisp","Cohors Hispanorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_hispanorum, 80, 80)]),
("cohors_tung","Cohors Tungrorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_tungrorum, 80, 80)]),
("cohors_gal","Cohors Gallorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_gallorum, 80, 80)]),
("cohors_bata","Cohors Batavorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_signifer,1,1),(trp_cornicen,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_batavorum, 80, 80)]),
("cohors_brit","Cohors Brittonum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_brittonum, 80, 80)]),
("cohors_thrac","Cohors Thracum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_thracum, 80, 80)]),
("cohors_jud","Cohors Petreorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_inf_petreorum, 80, 80)]),
## 6 cav alae
("ala_batavorum","Ala Batavorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius,5,5),(trp_aux_cav_batavorum, 80, 80),(trp_aux_cav_decurio,1,1),]),
("ala_asia","Ala Commagenorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius,5,5),(trp_aux_cav_commagenorum, 80, 80),(trp_aux_cav_decurio,1,1),]),
("ala_gal","Ala Gallorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius,5,5),(trp_aux_cav_gallorum, 80, 80),(trp_aux_cav_decurio,1,1),]),
("ala_syr","Ala Ituraeorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius,5,5),(trp_aux_cav_ituraeorum, 80, 80),(trp_aux_cav_decurio,1,1),]),
("ala_aux","Ala Auxiliarum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius,5,5),(trp_aux_cav, 60, 60),(trp_aux_cav_eastern, 60, 60),(trp_aux_cav_decurio,1,1),]),
("ala_preat","Ala Praetoriani",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius_praetorian,5,5),(trp_aux_cav_praetoriani, 80, 80),(trp_aux_cav_decurio,1,1),]),
("ala_preat_2","Ala Germani Corporis Custodes",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_cav_vexilarius_praetorian,5,5),(trp_aux_cav_praetoriani_2, 80, 80),(trp_aux_cav_decurio,1,1),]),
("player_aux_inf","infantry",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,
[(trp_custom_aux_cornicern,1,1),(trp_custom_aux_signifer,1,1),(trp_custom_aux_centurio,1,1),(trp_custom_aux_spear, 40,40),(trp_custom_aux_miles, 40,40)]),
("player_aux_cav","cavalry",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,
[(trp_custom_cav_of, 1,1),(trp_custom_cav_vex,5,5),(trp_custom_cav, 40,40),(trp_custom_aux_cav, 40,40)]),

("praetoriani_archer_cohors","Cohors Sagittarii Praetoriani",icon_pretorian_eques,0,fac_kingdom_7,soldier_personality,
[(trp_aux_archer_praetoriana,80,80),(trp_centurio_preatoriani,1,1),(trp_cornicen,1,1),(trp_signifer,1,1),]),
("engineer_cohort","Manipulus Ballistarium",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_ballistarii,25,25),]),
("engineer_cohort_custom","Manipulus Ballistarium (custom)",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_custom_balista,25,25),]),

("cohors_aux_archer","Cohors Auxiliarum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_signifer,1,1),(trp_cornicen,1,1),(trp_aux_centurio,1,1),(trp_aux_archer, 80,80),]),
("cohors_alp_archer","Cohors Alporum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_alporum,80,80),]),
("cohors_afr_archer","Cohors Maurorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_maurorum, 80,80),]),
("cohors_hisp_archer","Cohors Hispanorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_slinger, 80,80),]),
("cohors_tung_archer","Cohors Tungrorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_tungrorum, 80,80),]),
("cohors_gal_archer","Cohors Gallorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_gallorum, 80,80),]),
("cohors_bata_archer","Cohors Batavorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_aux_signifer,1,1),(trp_cornicen,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_batavorum, 80,80),]),
("cohors_brit_archer","Cohors Brittonum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_brittonum, 80,80),]),
("cohors_thrac_archer","Cohors Thracum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_thracum, 80,80),]),
("cohors_jud_archer","Cohors Petreorum",icon_kingdom_7_soldier_b,0,fac_kingdom_7,soldier_personality,
[(trp_cornicen,1,1),(trp_aux_signifer,1,1),(trp_aux_centurio,1,1),(trp_aux_archer_sryrorum, 80,80),]),
("player_aux_archer","infantry",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,
[(trp_custom_aux_cornicern,1,1),(trp_custom_aux_signifer,1,1),(trp_custom_aux_centurio,1,1),(trp_custom_sagitarius, 80,80)]),

##rebells begin
("germans","Germanic Revolt",icon_german1|carries_goods(50)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_germanic_noble_swordsman, 250, 350),(trp_germanic_light_clubman, 350,450),(trp_germanic_light_spearman, 350, 450),(trp_germanic_berserker, 150, 250),(trp_germanic_skirmisher, 200, 300),(trp_germanic_archer, 100, 200)]),
("brits","Celtic Revolt",icon_brit1|carries_goods(50)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_celtic_noble_swords, 250, 350),(trp_celtic_light_clubman, 350, 450),(trp_celtic_light_spearman, 350, 450),(trp_celtic_naked_swordman, 150, 250),(trp_celtic_skirmisher, 200, 300),(trp_celtic_archer, 100, 200)]),
("nomads","Tribal Revolt",icon_sarm1|carries_goods(50)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_sarmatian_noble_horseman, 250, 350),(trp_sarmatian_light_horsearcher, 350, 450),(trp_sarmatian_light_horseman, 350, 450),(trp_sarmatian_heavy_horseman, 150, 250),(trp_sarmatian_light_spearman, 200, 300),(trp_sarmatian_archers, 100, 200)]),
("cals","Caledonian Revolt",icon_brit1|carries_goods(50)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_caledonian_noble_swords, 250, 350),(trp_caledonian_light_clubman, 350, 450),(trp_caledonian_light_spearman, 350, 450),(trp_caledonian_naked_swordman, 150, 250),(trp_caledonian_skirmisher, 200, 300),(trp_caledonian_archer, 100, 200)]),

("dacians","Dacian Revolt",icon_dac1|carries_goods(50)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_dacian_noble_inf, 250, 350),(trp_dacian_light_spearman, 350, 450),(trp_dacian_light_swordman, 350, 450),(trp_dacian_noble_cav, 150, 250),(trp_dacian_skirmishers, 200, 300),(trp_dacian_archers, 100, 200)]),
#end
("jewish_revolt","Great Jewish Revolt",icon_mountain_bandit|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,550,650),(trp_kreta_archer,30,50),(trp_mercenary_swordsman, 30,50),(trp_judean_skirmisher,100,200),(trp_judean_light_clubman,100,200)]),
("slave_hideout" ,"Hideout",icon_map_bandit_lair|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[]),	#VC-1883
("player_camp","Camp",icon_camp|pf_always_visible|pf_limit_members,0,fac_player_faction,courage_15,[]),
("port","port",icon_landing_point|pf_is_static|pf_always_visible|pf_show_faction|pf_label_large|pf_hide_defenders,0, 0, 0,[]),
("ferry_port","port",icon_landing_point|pf_no_label|pf_is_static|pf_hide_defenders,0, 0, 0,[]),
("jetty_port","port",icon_landing_point|pf_no_label|pf_is_static|pf_hide_defenders,0, 0, 0,[]),
("landet_ships","your ships",icon_ship_on_land|pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship|pf_label_large,0, 0, 0,[]),
("traveller_ship","Traveller",icon_peasant|carries_goods(4)|pf_civilian,0,fac_commoners,merchant_personality,[(trp_mercenary_crossbowman,6,20),(trp_watchman, 5, 20), (trp_peasant_woman, 2, 15),]),
("slave_trader_ship","Slave Trader",icon_ship_merchant|carries_goods(3)|pf_civilian,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,2), (trp_mercenary_crossbowman,0,12), (trp_mercenary_swordsman,0,24), (trp_mercenary_horseman,4,48),]),
("sea_traders", "Traders",icon_ship_merchant|pf_is_ship|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_mercenary_swordsman,20,30),(trp_caravan_guard,5,20),(trp_hired_blade,5,10),(trp_mercenary_crossbowman,5,10),(trp_package_slave,3,10)]),
#("mine","Mine",icon_map_bandit_lair|pf_is_static|pf_hide_defenders|pf_always_visible|pf_label_small,0,fac_neutral,courage_15,[]),

("rebels","Rebels",icon_axeman|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_watchman,15,55),(trp_brigand, 12, 24),(trp_slave_rebel, 30, 70),(trp_slave_warrior, 30, 70),(trp_slave_warrior_2, 20, 40),(trp_slave_warrior_3, 10, 20),]),
("hord_siraken","Horde",icon_hord|carries_goods(2),0,fac_kingdom_12,merchant_personality,[(trp_sarmatian_light_horsearcher,150,200),(trp_sarmatian_light_horseman,46,117),(trp_sarmatian_heavy_horsearcher,10,23),(trp_sarmatian_noble_horseman,2,4),(trp_sarmatian_heavy_horseman, 7, 12),]),
("hord_roxolanen","Horde",icon_hord|carries_goods(2),0,fac_kingdom_11,merchant_personality,[(trp_sarmatian_light_horsearcher,150,200),(trp_sarmatian_light_horseman,46,117),(trp_sarmatian_heavy_horsearcher,10,23),(trp_sarmatian_noble_horseman,2,4),(trp_sarmatian_heavy_horseman, 7, 12),]),
("crucified_slaves","crucified slaves",icon_crucified_slave|pf_is_static|pf_always_visible|pf_hide_defenders|pf_no_label,0, 0, 0,[]),
("patrols_end","Patrol",icon_gray_knight,0,fac_player_faction,aggressiveness_0|courage_15,[]),
##costum player legion

("slave_revolt","Albus party",icon_axeman|carries_goods(2),0,fac_neutral,quest_personality,[(trp_brigand, 20, 25), (trp_bandit, 10, 15), (trp_slave_rebel, 50, 60),]),
("grove","Sacred Grove",icon_forest|pf_is_static|pf_hide_defenders,0,fac_neutral,soldier_personality,[]),
("latifundium","Latifundium",icon_villa_icon|pf_is_static|pf_always_visible|pf_limit_members,0,fac_neutral,soldier_personality,[]),
("parthian_exp","Expedition Force",icon_kingdom_6_soldier_b|carries_goods(200)|pf_show_faction,0,fac_commoners,rebel_personality,[(trp_eastern_heavy_inf_exp, 600, 800),(trp_eastern_heavy_spearman_exp, 600,800),(trp_eastern_light_archer_exp, 400, 500),(trp_eastern_horsearcher_exp, 400, 500),(trp_eastern_cataphract_exp, 300, 400),(trp_eastern_skrimisher_exp, 400, 500)]),

("barbarus_fleet","Barbarus Rufus fleet",icon_ship|carries_goods(9)|pf_quest_party|pf_auto_remove_in_town,0,fac_neutral,quest_personality,[(trp_sea_raider,80,120),(trp_sailor,30,50)]),
]
