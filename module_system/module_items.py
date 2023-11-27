from module_constants import *
from IDs.ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

import math
#from compiler import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################


#weight formula
#"Divide armour value by 10 and raise the result to its square"

def get_head_weight(armor):
  weight = (0.001*armor*armor+math.log(armor))/2.0
  return weight

def get_armor_weight(armor):
  weight = (armor/10.0)*(armor/10.0)
  return weight

def get_shield_weight(armor, width, height):
  if height == 0:
    width = width/2
    area = 3.14 * width * width
  else:
    area = width * height
  weight = armor*armor*area*0.000001
  return weight

def get_w_weight(length):
  weight = 0.018 * length
  return weight

def get_axe_weight(length):
  weight = 0.025 * length
  return weight

def get_mace_weight(length):
  weight = 0.022 * length
  return weight

def get_2hmace_weight(length):
  weight = 0.08 * length
  return weight

def get_1hmace_speed(length):
  weight = get_mace_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_1haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_2haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_2hmace_speed(length):
  weight = get_2hmace_weight (length)
  speed = 105 - (weight*weight*weight)
  return (int) (round(speed))

def get_1hw_speed(length):
  weight = get_w_weight (length)
  speed = 105 - (weight*weight*weight)
  return (int) (round(speed))

def get_2hw_speed(length):
  weight = get_w_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_polew_speed(length):
  weight = get_w_weight (length)
  speed = 107 - (weight*weight)
  return (int) (round(speed))

def get_w_price (length, weight, speed, damage_cut, damage_thrust):

  damage = damage_thrust + damage_cut
  price = (damage*damage) * speed * (length) / (weight * 100)
  price = price * price
  price = price /10000000
  return (int) (round(price))

def get_polarm_price (length, weight, speed, damage_cut, damage_thrust):

  damage = damage_thrust + damage_cut
  price = (damage*damage) * speed * (length*2/3) / (weight * 100)
  price = price * price
  price = price /20000000
  return (int) (round(price))

def get_barmour_price (body_a, leg_a):
  price = 3*(body_a + leg_a)*(body_a + leg_a)/2#/new_weight
  if body_a < 30:
    price = price - price/3
  if body_a >= 30 and body_a < 50:
    price = price - price/5
  if body_a < 35: #tom reduce - basic armor should be almost free
	price = price/3
  return (int) (round(price))

# def tier_6_body_armor_price:
  # price = get_barmour_price(25, 72, 31)
  # return price

def get_footwear_price (armour):
  price = armour * 31
  if armour < 30:
	price = price/4
  return (int(round(price)))

def get_headgear_price (armour):
  price = (armour ** 2)*5/7
  if armour < 25:
    price = price - price/4
  return (int(round(price)))

def get_gloves_price (armour):
  price = 10 * armour ** 2
  return (int(round(price)))

def get_shield_price (armour, width, height):
  if height == 0:
    width = width/2
    area = 3.14 * width * width
  else:
    area = width * height
  price = (area * armour*armour*armour)/1000000
  price = price*6
  return (int(round(price)))

shield_armor_t1 = 19
shield_armor_t2 = 22
shield_armor_t3 = 26
shield_armor_t4 = 29

shield_hitpoints_t1 = 310
shield_hitpoints_t2 = 340
shield_hitpoints_t3 = 375
shield_hitpoints_t4 = 400

#
#armor types:
#naked (only pants)
naked_price = get_barmour_price(2,2)
naked_armor = weight(get_armor_weight(4))|abundance(80)|head_armor(0)|body_armor(2)|leg_armor(2)|difficulty(0)

#naked with Cape
naked_cape_price = get_barmour_price(6,4)
naked_cape_armor = weight(get_armor_weight(10))|abundance(80)|head_armor(0)|body_armor(6)|leg_armor(4)|difficulty(0)

#pants (half naked
pants_price = get_barmour_price(1,9)
pants_armor = weight(get_armor_weight(10))|abundance(120)|head_armor(0)|body_armor(1)|leg_armor(9)|difficulty(0)

#pants with fur
pants_fur_price = get_barmour_price(10,15)
pants_fur_armor = weight(get_armor_weight(20))|abundance(120)|head_armor(20)|body_armor(10)|leg_armor(15)|difficulty(0)

#pants with shirt
pants_shirt_price = get_barmour_price(10,9)
pants_shirt_armor = weight(get_armor_weight(19))|abundance(120)|head_armor(0)|body_armor(10)|leg_armor(9)|difficulty(0)

#pants with shirt and Cape
pants_shirt_cape_price = get_barmour_price(13,10)
pants_shirt_cape_armor = weight(get_armor_weight(23))|abundance(120)|head_armor(0)|body_armor(13)|leg_armor(10)|difficulty(0)

#pants with medium armor
pants_medium_armor_price = get_barmour_price(20,9)
pants_medium_armor_armor = weight(get_armor_weight(29))|abundance(110)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(6)

#pants with stronger medium armor
pants_medium_armor_2_price = get_barmour_price(32,12)
pants_medium_armor_2_armor = weight(get_armor_weight(44))|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(7)

#pants with linothorax
pants_linothorax_price = get_barmour_price(44,10)
pants_linothorax_armor = weight(get_armor_weight(54))|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(10)|difficulty(6)

#armored pants with linothorax
pants_armored_linothorax_price = get_barmour_price(48,18)
pants_armored_linothorax_armor = weight(get_armor_weight(67))|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8)

#tunic with light armor
tunic_light_armor_price = get_barmour_price(20,3)
tunic_light_armor_armor = weight(get_armor_weight(23))|abundance(110)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(6)

#pants with light armor is now the same as pants with medium armor

#cataphract
cataphract_price = get_barmour_price(56,15)
cataphract_armor = weight(get_armor_weight(75))|abundance(70)|head_armor(0)|body_armor(56)|leg_armor(15)|difficulty(18)

#pants with mail/scale
pants_with_mail_price = get_barmour_price(46,10)
pants_with_mail_armor = weight(get_armor_weight(56))|abundance(110)|head_armor(0)|body_armor(46)|leg_armor(10)|difficulty(10)

#pants with mail/scale + fur (only one currently)
mail_fur_price = get_barmour_price(50,10)
mail_fur_armor = weight(get_armor_weight(60))|abundance(110)|head_armor(5)|body_armor(50)|leg_armor(10)|difficulty(14)

#heavy/noble armor
noble_mail_price = get_barmour_price(50,10)
noble_mail_armor = weight(get_armor_weight(60))|abundance(90)|head_armor(0)|body_armor(50)|leg_armor(10)|difficulty(12)


#sarmatian scale armor
scale_armor_price = get_barmour_price(48,10)
scale_armor_armor = weight(get_armor_weight(58))|abundance(90)|head_armor(0)|body_armor(48)|leg_armor(10)|difficulty(12)
# #sarmatian heavy scale armor
# scale_armor_heavy_price = get_barmour_price(48,25)
# scale_armor_heavy_armor = weight(get_armor_weight(70))|abundance(90)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(14)

#simple tunic
tunic_armor_price = get_barmour_price(7,3)
tunic_armor_armor = weight(get_armor_weight(10))|abundance(110)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0)

#simple robe
robe_armor_price = get_barmour_price(7,9)
robe_armor_armor = weight(get_armor_weight(16))|abundance(120)|head_armor(0)|body_armor(7)|leg_armor(9)|difficulty(0)

#roman toga / eastern rich
toga_a_noble_armor_price = get_barmour_price(20,20)##price should be higher, because its expansive clothing
toga_a_noble_armor = weight(get_armor_weight(13))|abundance(75)|head_armor(0)|body_armor(7)|leg_armor(6)|difficulty(0)

#roman rich
roman_rich_armor_price = get_barmour_price(40,25)##price should be higher, because its expansive clothing
roman_rich_armor = weight(get_armor_weight(13))|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(6)|difficulty(0)

#bandit fur armor
bandit_armor_price = get_barmour_price(27,10)
bandit_armor = weight(get_armor_weight(40))|abundance(30)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(6)

#linothorax greek
linothorax_armor_price = get_barmour_price(44,1)
linothorax_armor = weight(get_armor_weight(45))|abundance(85)|head_armor(0)|body_armor(44)|leg_armor(1)|difficulty(6)

#breastplate iron
breastplate_iron_armor_price = get_barmour_price(48,1)
breastplate_iron_armor = weight(get_armor_weight(53))|abundance(85)|head_armor(0)|body_armor(48)|leg_armor(5)|difficulty(10)

#breastplate leather
breastplate_leather_armor_price = get_barmour_price(32,5)
breastplate_leather_armor = weight(get_armor_weight(37))|abundance(85)|head_armor(0)|body_armor(32)|leg_armor(5)|difficulty(6)

#simple dress
dress_armor_price = get_barmour_price(5,5)
dress_armor = weight(get_armor_weight(10))|abundance(85)|head_armor(0)|body_armor(5)|leg_armor(5)|difficulty(0)

#roman rich dress
rich_dress_r_armor_price = get_barmour_price(40,25)
rich_dress_r_armor = weight(get_armor_weight(12))|abundance(30)|head_armor(0)|body_armor(5)|leg_armor(5)|difficulty(0)

#barbarian rich dress
rich_dress_b_armor_price = get_barmour_price(30,15)
rich_dress_b_armor = weight(get_armor_weight(10))|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(5)|difficulty(0)

#roman scale
roman_scale_armor_price = get_barmour_price(45,11)
roman_scale_armor = weight(get_armor_weight(56))|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(11)|difficulty(7)
#roman mail
roman_mail_armor_price = get_barmour_price(43,10)
roman_mail_armor = weight(get_armor_weight(53))|abundance(80)|head_armor(0)|body_armor(43)|leg_armor(10)|difficulty(7)
#roman mail heavy
roman_mail_heavy_armor_price = get_barmour_price(48,11)
roman_mail_heavy_armor = weight(get_armor_weight(59))|abundance(75)|head_armor(0)|body_armor(48)|leg_armor(11)|difficulty(9)
#roman light
roman_light_armor_price = get_barmour_price(30,9)
roman_light_armor = weight(get_armor_weight(39))|abundance(80)|head_armor(0)|body_armor(30)|leg_armor(9)|difficulty(6)
#roman segementata
roman_segementata_armor_price = get_barmour_price(49,12)
roman_segementata_armor = weight(get_armor_weight(61))|abundance(75)|head_armor(0)|body_armor(49)|leg_armor(12)|difficulty(9)
#roman segementata
roman_segementata_heavy_armor_price = get_barmour_price(50,14)
roman_segementata_heavy_armor = weight(get_armor_weight(64))|abundance(75)|head_armor(0)|body_armor(50)|leg_armor(14)|difficulty(9)

roman_segementata_heavy2_armor_price = get_barmour_price(53,14)
roman_segementata_heavy2_armor = weight(get_armor_weight(67))|abundance(75)|head_armor(0)|body_armor(53)|leg_armor(14)|difficulty(9)
#roman centurio
roman_centurio_armor_price = get_barmour_price(51,13)
roman_centurio_armor = weight(get_armor_weight(64))|abundance(75)|head_armor(0)|body_armor(51)|leg_armor(13)|difficulty(9)
#roman legate
roman_legate_armor_price = get_barmour_price(52,14)
roman_legate_armor = weight(get_armor_weight(65))|abundance(75)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(10)

#helm types:
#super light head (like this ugly bandit shit)
light_super_head_price = get_headgear_price(6)
light_super_head = weight(get_head_weight(6))|abundance(80)|head_armor(6)|difficulty(0)

#light head (like phrygian)
phrygian_head_price = get_headgear_price(12)
phrygian_head = weight(get_head_weight(12))|abundance(90)|head_armor(12)|difficulty(0)
#crown
crown_head_price = 25000
crown_head = weight(get_head_weight(15))|head_armor(10)|difficulty(0)
#light helm
light_head_price = get_headgear_price(30)
light_head = weight(get_head_weight(30))|abundance(100)|head_armor(30)|difficulty(3)
#medium helm
medium_head_price = get_headgear_price(42)
medium_head = weight(get_head_weight(42))|abundance(80)|head_armor(42)|difficulty(6)
#heavy/noble helm
heavy_head_price = get_headgear_price(48)
heavy_head = weight(get_head_weight(48))|abundance(70)|head_armor(48)|difficulty(9)
#cataphract helm
cataphract_head_price = get_headgear_price(51)
cataphract_head = weight(get_head_weight(51))|abundance(50)|head_armor(51)|difficulty(12)

#aux helm
aux_head_price = get_headgear_price(43)
aux_head = weight(get_head_weight(43))|abundance(80)|head_armor(43)|difficulty(7)

#legion helm
legio_head_price = get_headgear_price(45)
legio_head = weight(get_head_weight(45))|abundance(70)|head_armor(45)|difficulty(8)
#centurio helm
centurio_head_price = get_headgear_price(47)
centurio_head = weight(get_head_weight(47))|abundance(60)|head_armor(47)|difficulty(8)

#helm with fur (signifer)
signifer_head_price = get_headgear_price(49)
signifer_head = weight(get_head_weight(49))|abundance(50)|head_armor(43)|body_armor(6)|difficulty(8)

#just fur
fur_head_price = get_headgear_price(15)
fur_head = weight(get_head_weight(15))|abundance(50)|head_armor(10)|body_armor(5)|difficulty(8)

#legate helm
legate_head_price = get_headgear_price(48)
legate_head = weight(get_head_weight(48))|abundance(50)|head_armor(48)|difficulty(8)

#foot armor types:
#light/civilian
#medium (fur)
#heavy
#cataphract

#horse types:
#packhorse
#horse
#armored horse
#mule
#camel

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_ring   = imodbit_rusty | imodbit_battered | imodbit_crude |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive)

items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!

["tutorial_spear", "Spear", [("roman_spear_117",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(117)|swing_damage(19 , pierce) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["tutorial_club", "Club", [("germanic_club_1",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(60)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(60)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows","Arrows", [("arrow",0),("flying_arena_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back,
0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
["tutorial_crossbow", "Ballista", [("ballista",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife,
0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Tutorial Saddle Horse", [("roman_horse_9",0)], itp_type_horse, 0,
0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Shield", [("s_etruscan_scutum_old_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff_swup",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,
9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff_swup",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

["tutorial_sword", "Wooden Gladius", [("training_gladius",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_next_item_as_melee, itc_gladius,
10 , weight(3.0)|difficulty(9)|spd_rtng(100) | weapon_length(55)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_none ],
["tutorial_sword_2", "Wooden Gladius", [("training_gladius",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack,
itc_gladius_2,
10 , weight(3.0)|difficulty(9)|spd_rtng(100) | weapon_length(55)|swing_damage(25 , blunt) | thrust_damage(20 ,  blunt),imodbits_none ],

# #####
["tutorial_dagger","Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],

["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword,
3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
["heavy_practice_sword","Practice Falx", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
["practice_dagger","Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(48)|swing_damage(15 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["practice_axe", "Short Sword", [("sword_akinakes",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
900 , weight(1.4)|difficulty(0)|spd_rtng(99) | weapon_length(50)|swing_damage(24 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [] ],
["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
["arena_sword", "Onehanded Falx", [("falx58_one",0)], itp_type_one_handed_wpn|itp_primary, itc_cleaver|itc_parry_onehanded|itcf_carry_sword_left_hip,2394 , weight(1.5)|spd_rtng(99) | weapon_length(58)|swing_damage(28 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [] ],
["arena_sword_two_handed",  "Falx", [("falx110",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,1123 , weight(2.9)|spd_rtng(83) | weapon_length(105)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [] ],
["arena_lance",         "Spear", [("roman_spear_117",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_spear,140 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(117)|swing_damage(17 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [] ],
["practice_staff","Practice Staff", [("wooden_staff_swup",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(128)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
["practice_lance","Trident", [("trident135",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|spd_rtng(90) | weapon_length(135)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm, [], [] ],
["practice_shield","Practice Shield", [("s_etruscan_scutum_old_white",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
["practice_javelin", "Practice Javelins", [("javelin_new",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(60) | weapon_length(75), imodbits_thrown],
["practice_javelin_melee", "practice_javelin_melee", [("javelin_new",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_spear, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger_new",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger_new",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
["practice_horse","Practice Horse", [("roman_horse_9",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_arena_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
["practice_javelin_amo4", "Practice Pila", [("roman_pilum_training",0)], itp_type_thrown |itp_primary,itcf_throw_javelin, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(2) | weapon_length(75), imodbits_thrown],
["practice_boots", "Practice Boots", [("leather_boots_a",0)], itp_type_foot_armor|itp_civilian|itp_attach_armature,0,
90 , weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],

["arena_shield_red", "Scutum", [("s_etruscan_scutum_old_red",0)], itp_type_shield|itp_wooden_parry|itp_merchandise, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2,50,85), weight(get_shield_weight(shield_armor_t2,50,85))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(100)|shield_width(50)|shield_height(85),imodbits_shield,[],[fac_culture_7] ],
["arena_shield_blue", "Scutum", [("s_etruscan_scutum_old_brown",0)], itp_type_shield|itp_wooden_parry|itp_merchandise, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2,50,85), weight(get_shield_weight(shield_armor_t2,50,85))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(100)|shield_width(50)|shield_height(85),imodbits_shield,[],[fac_culture_7] ],
["arena_shield_green", "Scutum", [("s_etruscan_scutum_old_green",0)], itp_type_shield|itp_wooden_parry|itp_merchandise, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2,50,85), weight(get_shield_weight(shield_armor_t2,50,85))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(100)|shield_width(50)|shield_height(85),imodbits_shield,[],[fac_culture_7] ],
["arena_shield_yellow", "Scutum", [("s_etruscan_scutum_old_white",0)], itp_type_shield|itp_wooden_parry|itp_merchandise, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2,50,85), weight(get_shield_weight(shield_armor_t2,50,85))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(100)|shield_width(50)|shield_height(85),imodbits_shield,[],[fac_culture_7] ],

["arena_armor_red", "Loincloth with Manica", [("gladiator6",0)], itp_type_body_armor  |itp_force_show_body|itp_attach_armature|itp_merchandise ,0,
tunic_light_armor_price, tunic_light_armor_armor, imodbits_armor,[],[fac_culture_7] ],
["arena_armor_blue", "Loincloth with Manica", [("gladiator",0)], itp_type_body_armor  |itp_force_show_body|itp_attach_armature|itp_merchandise ,0,
tunic_light_armor_price , tunic_light_armor_armor, imodbits_armor,[],[fac_culture_7] ],
["arena_armor_green", "Loincloth with Manica", [("gladiator1",0)], itp_type_body_armor  |itp_force_show_body|itp_attach_armature|itp_merchandise ,0,
tunic_light_armor_price , tunic_light_armor_armor, imodbits_armor,[],[fac_culture_7] ],
["arena_armor_yellow", "Loincloth with Manica", [("gladiator7",0)], itp_type_body_armor  |itp_force_show_body|itp_attach_armature|itp_merchandise ,0,
tunic_light_armor_price , tunic_light_armor_armor, imodbits_armor,[],[fac_culture_7] ],

["tourney_helm_red", "Gladiator Helm", [("gladiator_helm",0)], itp_type_head_armor|itp_merchandise,0,
heavy_head_price, heavy_head, imodbits_plate,[],[fac_culture_7] ],
["tourney_helm_blue", "Gladiator Helm", [("gladiator_helm3",0)], itp_type_head_armor|itp_merchandise,0,
heavy_head_price, heavy_head, imodbits_plate,[],[fac_culture_7] ],
["tourney_helm_green", "Gladiator Helm", [("gladiator_helm4",0)], itp_type_head_armor|itp_merchandise,0,
heavy_head_price, heavy_head, imodbits_plate,[],[fac_culture_7] ],
["tourney_helm_yellow", "Gladiator Helm", [("gladiator_helm9",0)], itp_type_head_armor|itp_merchandise,0,
heavy_head_price, heavy_head, imodbits_plate,[],[fac_culture_7] ],

##gold
["temple_gold","Gold", [("tradegood_gold_trophy",0)],			itp_type_goods,			0,
10000,weight( 10)|abundance(1),imodbits_none],

# A treatise on The Method of Mechanical Theorems Archimedes
#This book must be at the beginning of readable books
["book_tactics","History of the Peloponnesian War", [("scroll_2",0)], itp_type_book, 0,
4000,weight(2)|abundance(100),imodbits_none],
["book_persuasion","Rhetorica ad Herennium", [("scroll_1",0)], itp_type_book, 0,
5000,weight(2)|abundance(100),imodbits_none],
["book_leadership","The Life of Alexander the Great", [("scroll_2",0)], itp_type_book, 0,
4200,weight(2)|abundance(100),imodbits_none], #cambiar chief
["book_intelligence","Paedeia", [("scroll_3",0)], itp_type_book, 0,
6900,weight(2)|abundance(100),imodbits_none],
["book_trade","Oeconomica", [("scroll_3",0)], itp_type_book, 0,
6100,weight(2)|abundance(100),imodbits_none],
["book_weapon_mastery", "Polity of the Lacedaemonians", [("scroll_2",0)], itp_type_book, 0,
4200,weight(2)|abundance(100),imodbits_none],
["book_engineering","De architectura", [("scroll_1",0)], itp_type_book, 0,
4300,weight(2)|abundance(100),imodbits_none],
["book_economy","Rerum rusticarum libri tres", [("scroll_1",0)], itp_type_book, 0,
5000,weight(2)|abundance(100),imodbits_none],
["book_gallic_wars","De bello Gallico", [("scroll_1",0)], itp_type_book, 0,
3900,weight(2)|abundance(100),imodbits_none],
["book_love","Ars Amatoria", [("scroll_1",0)], itp_type_book, 0,
4100,weight(2)|abundance(100),imodbits_none],
["book_sorrows","Tristia", [("scroll_1",0)], itp_type_book, 0,
5000,weight(2)|abundance(100),imodbits_none],
["book_odysseus","Odusia", [("scroll_1",0)], itp_type_book, 0,
4200,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
["book_wound_treatment_reference","De Materia Medica", [("scroll_1",0)], itp_type_book, 0,
3500,weight(2)|abundance(100),imodbits_none],
["book_training_reference","Epitoma Rei Militaris", [("scroll_3",0)], itp_type_book, 0,
3500,weight(2)|abundance(100),imodbits_none],
["book_surgery_reference","Synopsis of Aelius Galenus", [("scroll_1",0)], itp_type_book, 0,
3500,weight(2)|abundance(100),imodbits_none],
["book_pathfinding","Tabula Mundi of Pomponius Mela", [("map_item",0)], itp_type_book, 0,
4000,weight(2)|abundance(100),imodbits_none],
["book_first_aid","Corpus Hippocraticum", [("scroll_3",0)], itp_type_book, 0,
4000,weight(2)|abundance(100),imodbits_none],

#other trade goods (first one is spice)
["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0,
880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],

["amber","Amber", [("tradegood_amber",0)],itp_merchandise|itp_type_goods,0,
1200,weight(7)|abundance(80),imodbits_none],
["perfume","Perfume", [("roman_palace_jug_2",0)],itp_merchandise|itp_type_goods,0,
5000,weight(1)|abundance(60),imodbits_none],
["incense","Incense", [("roman_palace_jug",0)],itp_merchandise|itp_type_goods,0,
600,weight(1)|abundance(60),imodbits_none],

["ivory","Ivory", [("tradegood_walrusIvory",0)],itp_merchandise|itp_type_goods,0,
2100,weight(7)|abundance(80),imodbits_none],
["silver","Silver", [("tradegood_silver",0)],itp_merchandise|itp_type_goods,0,
800,weight(7)|abundance(90),imodbits_none],
["stone","Stone", [("tradegood_stone",0)],itp_merchandise|itp_type_goods,0,
104,weight(60)|abundance(100),imodbits_none],
["timber","Timber", [("tradegood_wood",0)],itp_merchandise|itp_type_goods,0,
300,weight(60)|abundance(100),imodbits_none],
["soapstone","Soapstone", [("tradegood_soapastone",0)],itp_merchandise|itp_type_goods,0,
320,weight(40)|abundance(90),imodbits_none],
["jewelry","Jewellery", [("tradegood_jewelry",0)],itp_merchandise|itp_type_goods,0,
3500,weight( 5)|abundance(80), imodbits_none],

["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0,
255,weight(50)|abundance(120),imodbits_none],

["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0,
900,weight(100)|abundance(60)|max_ammo(40),imodbits_none],

["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0,
200,weight(100)|abundance(90),imodbits_none],

["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0,
 300,weight(80)|abundance(90),imodbits_none],
["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0,
500,weight(80)|abundance(90),imodbits_none],

["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0,
260,weight(80)|abundance(90),imodbits_none],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0,
500,weight(80)|abundance(90),imodbits_none],

["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0,
1200,weight(60)|abundance(80),imodbits_none],
["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0,
400,weight(20)|abundance(80),imodbits_none],
["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0,
2050,weight(80)|abundance(30),imodbits_none],

["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,
528,weight(120)|abundance(60),imodbits_none],
["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0,
810,weight(100)|abundance(90),imodbits_none],

["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0,
240,weight(80)|abundance(90),imodbits_none],
["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0,
440,weight(80)|abundance(90),imodbits_none],

["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
240,weight(80)|food_quality(10)|max_ammo(60),imodbits_none],
["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0,
782,weight(80)|abundance(90),imodbits_none],
["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0,
440,weight(60)|abundance(60)|max_ammo(60),imodbits_none],
["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0,
240,weight(60)|abundance(70)|max_ammo(80),imodbits_none],

#foods (first one is smoked_fish)
["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
130,weight(60)|abundance(110)|food_quality(50)|max_ammo(100),imodbits_none],
["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
150,weight(50)|abundance(110)|food_quality(40)|max_ammo(80),imodbits_none],
["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
440,weight(40)|abundance(110)|food_quality(40)|max_ammo(80),imodbits_none],
["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
170,weight(40)|abundance(110)|food_quality(40)|max_ammo(125),imodbits_none],
["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
60,weight(45)|abundance(110)|food_quality(40)|max_ammo(120),imodbits_none],
["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
170,weight(60)|abundance(100)|food_quality(70)|max_ammo(150),imodbits_none],
["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
88,weight(80)|abundance(110)|food_quality(40)|max_ammo(120),imodbits_none],
["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0,
140,weight(20)|abundance(90)|food_quality(10)|max_ammo(60),imodbits_none], #x2 for wine
["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0,
180,weight(20)|abundance(90)|food_quality(10)|max_ammo(60),imodbits_none], #x3 for oil
["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0,
60,weight(60)|abundance(220)|food_quality(40)|max_ammo(200),imodbits_none],
["rice","African Rice", [("wheat_sack",0)], itp_type_goods|itp_consumable, 0,
40,weight(60)|abundance(220)|food_quality(40)|max_ammo(200),imodbits_none],

["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
190,weight(80)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none],
["horse_meat2","Horse Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
250,weight(80)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none],
["venison","Game Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
300,weight(80)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none],
["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
100,weight(120)|abundance(110)|food_quality(40)|max_ammo(160),imodbits_none],
["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
140,weight(40)|abundance(110)|food_quality(75)|max_ammo(40),imodbits_none],
["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
170,weight(60)|abundance(100)|food_quality(75)|max_ammo(70),imodbits_none],
["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,
300,weight(50)|abundance(110)|food_quality(40)|max_ammo(80),imodbits_none],

# Quest Items
["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0,
96,weight(40)|abundance(70),imodbits_none],
["the_lost_eagle","Eagle of the Seventheen Legion", [("roman_aquila5",0)], itp_type_goods|itp_unique, 0,
96,weight(10)|abundance(70),imodbits_none],
["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0,
46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0,
31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
["sumpter_horse","Packhorse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0,
1034,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|
horse_speed(35)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
["horse_light_a","Packhorse", [("horse_light_a",0)], itp_merchandise|itp_type_horse, 0,
1034,abundance(90)|hit_points(100)|body_armor(8)|difficulty(2)|
horse_speed(35)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
["horse_light_b","Packhorse", [("horse_light_b",0)], itp_merchandise|itp_type_horse, 0,
1034,abundance(90)|hit_points(100)|body_armor(8)|difficulty(2)|
horse_speed(35)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
["horse_light_c","Packhorse", [("horse_light_c",0)], itp_merchandise|itp_type_horse, 0,
1034,abundance(90)|hit_points(100)|body_armor(8)|difficulty(2)|
horse_speed(35)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],

#normal horses
["normal_horse_1","Horse", [("normal_horse_1",0)], itp_merchandise|itp_type_horse, 0,
2200,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(42)|horse_maneuver(42)|horse_charge(11)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["normal_horse_2","Horse", [("normal_horse_2",0)], itp_merchandise|itp_type_horse, 0,
2200,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(42)|horse_maneuver(42)|horse_charge(11)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["normal_horse_3","Horse", [("normal_horse_3",0)], itp_merchandise|itp_type_horse, 0,
2200,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(42)|horse_maneuver(42)|horse_charge(11)|horse_scale(105),imodbits_horse_basic|imodbit_champion],

#roman horses
["horse_1","Horse", [("roman_horse_9",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_2","Horse", [("roman_horse_1",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_3","Horse", [("roman_horse_5",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_4","Horse", [("roman_horse_2",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_5","Horse", [("roman_horse_3",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_6","Horse", [("roman_horse_4",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_7","Horse", [("roman_horse_6",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_8","Horse", [("roman_horse_7",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],
["horse_9","Horse", [("roman_horse_8",0)], itp_merchandise|itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(43)|horse_maneuver(44)|horse_charge(12)|horse_scale(105),imodbits_horse_basic|imodbit_champion],

#numidian horses, they are smaller, thus less damage
["numidian_horse_1","Numidian Horse", [("horse_light_a1",0)], itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(98),imodbits_horse_basic|imodbit_champion],
["numidian_horse_2","Numidian Horse", [("horse_light_b1",0)], itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(98),imodbits_horse_basic|imodbit_champion],
["numidian_horse_3","Numidian Horse", [("horse_light_c1",0)], itp_type_horse, 0,
2700,abundance(70)|hit_points(115)|body_armor(11)|difficulty(3)|
horse_speed(44)|horse_maneuver(44)|horse_charge(10)|horse_scale(98),imodbits_horse_basic|imodbit_champion],

#stepp horse
["steppe_horse_1","Steppe Horse", [("steppe_horse_1",0)], itp_merchandise|itp_type_horse, 0,
2500,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(43)|horse_maneuver(55)|horse_charge(11)|horse_scale(98),imodbits_horse_basic, [], [fac_culture_3,fac_culture_9]],
["steppe_horse_2","Steppe Horse", [("steppe_horse_2",0)], itp_merchandise|itp_type_horse, 0,
2500,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(43)|horse_maneuver(55)|horse_charge(11)|horse_scale(98),imodbits_horse_basic, [], [fac_culture_3,fac_culture_9]],
["steppe_horse_3","Steppe Horse", [("steppe_horse_3",0)], itp_merchandise|itp_type_horse, 0,
2500,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(43)|horse_maneuver(55)|horse_charge(11)|horse_scale(98),imodbits_horse_basic, [], [fac_culture_3,fac_culture_9]],
["cataphract_horse_steppe_1","Armored Horse", [("steppe_cataphract_1",0)], itp_merchandise|itp_type_horse, 0,
4650,abundance(40)|hit_points(125)|body_armor(42)|difficulty(4)|
horse_speed(40)|horse_maneuver(50)|horse_charge(27)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_3,fac_culture_5,fac_culture_9]],
["cataphract_horse_steppe_2","Armored Horse", [("steppe_cataphract_2",0)], itp_merchandise|itp_type_horse, 0,
4650,abundance(40)|hit_points(125)|body_armor(42)|difficulty(4)|
horse_speed(40)|horse_maneuver(50)|horse_charge(27)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_3,fac_culture_5,fac_culture_9]],
["cataphract_horse_steppe_3","Armored Horse", [("steppe_cataphract_3",0)], itp_merchandise|itp_type_horse, 0,
4650,abundance(40)|hit_points(125)|body_armor(42)|difficulty(4)|
horse_speed(40)|horse_maneuver(50)|horse_charge(27)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_3,fac_culture_5,fac_culture_9]],

#desert horse
["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0,
2550,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5, fac_culture_6,fac_culture_8]],
["arabian_horse_b","Desert Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0,
2550,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5, fac_culture_6,fac_culture_8]],
["arabian_horse_c","Desert Horse", [("arabian_horse_c",0)], itp_merchandise|itp_type_horse, 0,
2550,abundance(80)|hit_points(115)|body_armor(10)|difficulty(3)|
horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5, fac_culture_6,fac_culture_8]],

#parthian
["parthian_horse_a","Parthian Horse", [("parthian_horse_a",0)], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5]],
["parthian_horse_b","Parthian Horse", [("parthian_horse_b",0)], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5]],
["parthian_horse_c","Parthian Horse", [("parthian_horse_c",0),], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5]],
["cataphract_horse_parthian_1","Armored Horse", [("parthian_cataphract_1",0)], itp_merchandise|itp_type_horse, 0,
4800,abundance(40)|hit_points(125)|body_armor(45)|difficulty(4)|
horse_speed(39)|horse_maneuver(45)|horse_charge(30)|horse_scale(99),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],
["cataphract_horse_parthian_2","Armored Horse", [("parthian_cataphract_2",0)], itp_merchandise|itp_type_horse, 0,
4800,abundance(40)|hit_points(125)|body_armor(45)|difficulty(4)|
horse_speed(39)|horse_maneuver(45)|horse_charge(30)|horse_scale(99),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],
["cataphract_horse_parthian_3","Armored Horse", [("parthian_cataphract_3",0)], itp_merchandise|itp_type_horse, 0,
4800,abundance(40)|hit_points(125)|body_armor(45)|difficulty(4)|
horse_speed(39)|horse_maneuver(45)|horse_charge(30)|horse_scale(99),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],
["half_cataphract_horse_parthian_1","Half-Armored Horse", [("parthian_halfcataphract_1",0)], itp_merchandise|itp_type_horse, 0,
3800,abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|
horse_speed(41)|horse_maneuver(47)|horse_charge(25)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],
["half_cataphract_horse_parthian_2","Half-Armored Horse", [("parthian_halfcataphract_2",0)], itp_merchandise|itp_type_horse, 0,
3800,abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|
horse_speed(41)|horse_maneuver(47)|horse_charge(25)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],
["half_cataphract_horse_parthian_3","Half-Armored Horse", [("parthian_halfcataphract_3",0)], itp_merchandise|itp_type_horse, 0,
3800,abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|
horse_speed(41)|horse_maneuver(47)|horse_charge(25)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_5,fac_culture_6]],

# noble roman horses
["leopard_horse_1","Horse", [("horse_leopard",0),], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5,fac_culture_7]],
["leopard_horse_2","Horse", [("horse_leopard_white",0),], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5,fac_culture_7]],
["leopard_horse_3","Horse", [("horse_leopard_black",0),], itp_merchandise|itp_type_horse, 0,
3100,abundance(80)|hit_points(120)|body_armor(12)|difficulty(3)|
horse_speed(44)|horse_maneuver(50)|horse_charge(13)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_culture_6,fac_culture_8,fac_culture_5,fac_culture_7]],

# test chariot
# ["war_chariot_horse","War Chariot", [("chariot2",0)], itp_type_horse, 0,
# 4800,abundance(40)|hit_points(125)|body_armor(45)|difficulty(4)|
# horse_speed(39)|horse_maneuver(45)|horse_charge(30)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [
# ], []],
# ["war_chariot","War Chariot", [("chariot2_2",0)], itp_type_horse, 0,
# 4800,abundance(40)|hit_points(125)|body_armor(45)|difficulty(4)|
# horse_speed(39)|horse_maneuver(45)|horse_charge(30)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [
# (ti_on_init_item, [
# (store_trigger_param_1, ":agent"),
# (agent_get_position, pos22, ":agent"),
# (set_spawn_position, pos22),
# (spawn_horse, "itm_war_chariot_horse"),
# (assign, ":horse", reg0),
# ]),
# ], []],

##camels
["camel","Camel", [("camel",0)], itp_merchandise|itp_type_horse, 0,
1000,abundance(90)|hit_points(130)|body_armor(14)|difficulty(2)|
horse_speed(33)|horse_maneuver(40)|horse_charge(32)|horse_scale(120),imodbits_horse_basic,[], [fac_culture_6,fac_culture_8]],

#donkeys and mules
["donkey_mount","Donkey", [("donkey_mount",0)], itp_merchandise|itp_type_horse, 0,
400,abundance(85)|hit_points(50)|body_armor(5)|difficulty(0)|
horse_speed(32)|horse_maneuver(33)|horse_charge(7)|horse_scale(79),imodbits_horse_basic],
["donkey_mount2","Donkey", [("donkey_mount2",0)], itp_merchandise|itp_type_horse, 0,
400,abundance(85)|hit_points(50)|body_armor(5)|difficulty(0)|
horse_speed(32)|horse_maneuver(33)|horse_charge(7)|horse_scale(79),imodbits_horse_basic],
["mule","Mule", [("mule",0)], itp_merchandise|itp_type_horse, 0,
520,abundance(75)|hit_points(60)|body_armor(7)|difficulty(0)|
horse_speed(35)|horse_maneuver(35)|horse_charge(8)|horse_scale(86),imodbits_horse_basic],
["mule_package","Package Mule", [("mule_package",0)], itp_merchandise|itp_type_horse, 0,
520,abundance(75)|hit_points(60)|body_armor(7)|difficulty(0)|
horse_speed(28)|horse_maneuver(35)|horse_charge(4)|horse_scale(86),imodbits_horse_basic],
#horses end here,

["arrows", "Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical,
100, weight(2)|abundance(130)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(40), imodbits_missile ],
["khergit_arrows", "Elite Arrows", [("arrow_b",0),("flying_arrow_b",ixmesh_flying_ammo),("quiver_b",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
200, weight(1.7)|abundance(30)|weapon_length(95)|thrust_damage(4,pierce)|max_ammo(35), imodbits_missile ],
["barbed_arrows", "Barbed Arrows", [("barbed_arrow",0),("flying_barbed_arrow",ixmesh_flying_ammo),("quiver_d",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
300, weight(1.4)|abundance(70)|weapon_length(95)|thrust_damage(5,pierce)|max_ammo(30), imodbits_missile ],
["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_piercing_arrow",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
400,weight(1.4)|abundance(50)|weapon_length(91)|thrust_damage(6,pierce)|max_ammo(30),imodbits_missile],
["poisoned_arrows", "Poisoned  Arrows", [("barbed_arrow",0),("flying_barbed_arrow",ixmesh_flying_ammo),("quiver_d",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_right_vertical,
300, weight(1.7)|abundance(30)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(35), imodbits_missile, [],
[fac_culture_2,fac_culture_2_1,fac_culture_4,fac_culture_3] ],

["syrian_barbed_arrows", "Syrian Barbed Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("sagitarius_roman_arrow_quiver",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
300, weight(1.4)|abundance(70)|weapon_length(95)|thrust_damage(5,pierce)|max_ammo(30), imodbits_missile ],
["sarmatian_arrows_1","Sarmatian Barbed Arrows", [("piercing_arrow",0),("piercing_arrow",ixmesh_flying_ammo),("roman_quiver_1", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
100,weight(1.7)|abundance(80)|weapon_length(95)|thrust_damage(5,pierce)|max_ammo(35),imodbits_missile, [],[fac_culture_3,fac_culture_9]],
["sarmatian_arrows_2","Sarmatian Barbed Arrows", [("piercing_arrow",0),("piercing_arrow",ixmesh_flying_ammo),("roman_quiver_2", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_right_vertical,
100,weight(1.7)|abundance(80)|weapon_length(95)|thrust_damage(5,pierce)|max_ammo(35),imodbits_missile, [],[fac_culture_3,fac_culture_9]],


["sling_rock1", "Sling Rocks", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)],itp_type_bullets|itp_default_ammo|itp_merchandise, 0,
20,weight(2)|abundance(90)|weapon_length(3)|thrust_damage(5,blunt)|max_ammo(40),imodbit_large_bag],
["sling_lead", "Sling Lead", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo)],itp_type_bullets|itp_merchandise, 0,
50,weight(1.5)|abundance(90)|weapon_length(3)|thrust_damage(9,blunt)|max_ammo(20),imodbit_large_bag],
["ballista_bolts","Ballista Ammunition", [("ballista_bolt",0),("ballista_bolt",ixmesh_flying_ammo),("ballista_bolt_bag", ixmesh_carry),("ballista_bolt_bag", ixmesh_carry|imodbit_large_bag)],
itp_type_bolts|itp_can_penetrate_shield|itp_can_knock_down|itp_default_ammo, itcf_carry_quiver_right_vertical,
50,weight(2)|abundance(90)|weapon_length(55)|thrust_damage(25,pierce)|max_ammo(25),imodbits_missile, [], [fac_culture_7] ],

# ["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0,
# robe_armor_price, robe_armor_armor, imodbits_cloth,
# [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], ],
# ["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0,
# light_super_head_price, light_super_head,imodbits_cloth ],

# ARMOR BEGIN
#handwear
["leather_gloves","Leather Gloves", [("glovevambrace_set1_L",0)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,
get_gloves_price(2), weight(0.25)|abundance(80)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0,
get_gloves_price(4), weight(0.5)|abundance(60)|body_armor(4)|difficulty(0),imodbits_armor,[], [fac_culture_5,fac_culture_6,fac_culture_8]],
["gauntles_1","Gauntlets", [("scale_gauntlets_a_L",0),("scale_gauntlets_a_Lx", ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,
get_gloves_price(4), weight(0.5)|abundance(60)|body_armor(4)|difficulty(0),imodbits_armor,[], [fac_culture_5,fac_culture_6,fac_culture_8,fac_culture_7]],
["gauntles_2","Gauntlets", [("scale_gauntlets_b_L",0),("scale_gauntlets_b_Lx", ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,
get_gloves_price(4), weight(0.5)|abundance(60)|body_armor(4)|difficulty(0),imodbits_armor,[], [fac_culture_5,fac_culture_6,fac_culture_8,fac_culture_7]],

["ring_1","Gold Ring", [("ring_L",0),("inv_ring", ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
get_gloves_price(4), weight(0.1)|abundance(10)|body_armor(1)|difficulty(0),imodbits_ring,[], []],
["ring_2","Silver Ring", [("ring1_L",0),("inv_ring1", ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
get_gloves_price(3), weight(0.1)|abundance(15)|body_armor(1)|difficulty(0),imodbits_ring,[], []],
["ring_3","Bronze Ring", [("ring2_L",0),("inv_ring2", ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
get_gloves_price(2), weight(0.1)|abundance(20)|body_armor(1)|difficulty(0),imodbits_ring,[], []],


# ["manica_1","Manica", [("a_copper_manica_L",0),("a_copper_manica_Rx", ixmesh_inventory),], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,
# get_gloves_price(8), weight(0.1)|abundance(20)|body_armor(8)|difficulty(6),imodbits_ring,[], []],
# ["manica_2","Manica", [("a_metal_manica_L",0),("a_metal_manica_Rx", ixmesh_inventory),], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,
# get_gloves_price(8), weight(0.1)|abundance(20)|body_armor(8)|difficulty(6),imodbits_ring,[], []],

#roman military items
#officers
["aquilifer_legion_squamata_1", "Lorica Squamata (Aquilifer)", [("aquilifer_legion_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["aquilifer_legion_squamata_2", "Lorica Squamata (Aquilifer)", [("aquilifer_legion_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["aquilifer_praetorian_squamata_1", "Lorica Squamata (Aquilifer)", [("aquilifer_praetorian_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["cenutrio_legion_squamata_1", "Lorica Hamata (Centurio)", [("cenutrio_legion_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_legion_squamata_2", "Lorica Hamata (Centurio)", [("cenutrio_legion_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_legion_squamata_3", "Lorica Hamata (Centurio)", [("cenutrio_legion_squamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_legion_squamata_4", "Lorica Hamata (Centurio)", [("cenutrio_legion_squamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["centurio_legion_hamata_1", "Lorica Hamata (Centurio)", [("centurio_legion_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["centurio_legion_hamata_2", "Lorica Hamata (Centurio)", [("centurio_legion_hamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_legion_hamata_3", "Lorica Hamata (Centurio)", [("cenutrio_legion_hamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_legion_hamata_4", "Lorica Hamata (Centurio)", [("cenutrio_legion_hamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["centurio_praetorian_squamata_1", "Lorica Hamata (Centurio)", [("centurio_praetorian_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["centurio_praetorian_squamata_2", "Lorica Hamata (Centurio)", [("centurio_praetorian_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_aux_squamata_1", "Lorica Hamata (Centurio)", [("cenutrio_aux_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["cenutrio_aux_hamata_1", "Lorica Hamata (Centurio)", [("cenutrio_aux_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_hamata_1", "Lorica Hamata with Subarmalis", [("legion_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_10", "Lorica Hamata with Subarmalis", [("legion_hamata_10",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_11", "Lorica Hamata with Subarmalis", [("legion_hamata_11",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_13", "Lorica Hamata with Subarmalis", [("legion_hamata_13",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_14", "Lorica Hamata with Subarmalis", [("legion_hamata_14",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_15", "Lorica Hamata with Subarmalis", [("legion_hamata_15",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_16", "Lorica Hamata with Subarmalis", [("legion_hamata_16",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_2", "Lorica Hamata with Subarmalis", [("legion_hamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_3", "Lorica Hamata with Subarmalis", [("legion_hamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_hamata_4", "Lorica Hamata", [("legion_hamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_5", "Lorica Hamata", [("legion_hamata_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_6", "Lorica Hamata", [("legion_hamata_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_7", "Lorica Hamata", [("legion_hamata_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_8", "Lorica Hamata", [("legion_hamata_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_9", "Lorica Hamata", [("legion_hamata_9",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["auxilia_cavalry_hamata_1", "Lorica Hamata", [("auxilia_cavalry_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_cavalry_hamata_2", "Lorica Hamata", [("auxilia_cavalry_hamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_hamata_east_1", "Lorica Hamata with Cape", [("auxilia_hamata_east_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_hamata_east_2", "Lorica Hamata", [("auxilia_hamata_east_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_pants_long_3", "Lorica Hamata with Cape", [("legion_hamata_cape_pants_long_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_pants_long_4", "Lorica Hamata with Cape", [("legion_hamata_cape_pants_long_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_hamata_cape_1", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_2", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_3", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_hamata_cape_4", "Lorica Hamata with Cape", [("legion_hamata_cape_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_5", "Lorica Hamata with Cape", [("legion_hamata_cape_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_hamata_cape_6", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_7", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_hamata_cape_8", "Lorica Hamata with Cape and Subarmalis", [("legion_hamata_cape_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["praetorian_hamata_1", "Lorica Hamata Praetoriani with Cape", [("praetorian_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["praetorian_hamata_2", "Lorica Hamata Praetoriani", [("praetorian_hamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["praetorian_hamata_3", "Lorica Hamata Praetoriani with Cape", [("praetorian_hamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["praetorian_hamata_4", "Lorica Hamata Praetoriani", [("praetorian_hamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_segmentata_1", "Lorica Segmentata", [("legion_segmentata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_2", "Lorica Segmentata", [("legion_segmentata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_3", "Lorica Segmentata", [("legion_segmentata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_4", "Lorica Segmentata", [("legion_segmentata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_5", "Lorica Segmentata", [("legion_segmentata_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_segmentata_6", "Lorica Segmentata with Subarmalis", [("legion_segmentata_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_7", "Lorica Segmentata with Subarmalis", [("legion_segmentata_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_8", "Lorica Segmentata with Subarmalis", [("legion_segmentata_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_segmentata_manica_1", "Lorica Segmentata with Subarmalis and Manica", [("legion_segmentata_manica_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_2", "Lorica Segmentata with Subarmalis and Manica", [("legion_segmentata_manica_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_3", "Lorica Segmentata with Subarmalis and Manica", [("legion_segmentata_manica_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_4", "Lorica Segmentata with Subarmalis and Manica", [("legion_segmentata_manica_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],

["legion_segmentata_manica_5", "Lorica Segmentata with Subarmalis, Cape and Manica", [("legion_segmentata_manica_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_6", "Lorica Segmentata with Subarmalis, Cape and Manica", [("legion_segmentata_manica_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_7", "Lorica Segmentata with Subarmalis, Cape and Manica", [("legion_segmentata_manica_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],
["legion_segmentata_manica_8", "Lorica Segmentata with Subarmalis, Cape and Manica", [("legion_segmentata_manica_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy2_armor_price, roman_segementata_heavy2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_3"),]),], [fac_culture_7] ],

["legion_segmentata_cape_1", "Lorica Segmentata with Cape", [("legion_segmentata_cape_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_cape_2", "Lorica Segmentata with Cape", [("legion_segmentata_cape_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_cape_3", "Lorica Segmentata with Cape", [("legion_segmentata_cape_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_armor_price, roman_segementata_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_segmentata_cape_4", "Lorica Segmentata with Cape and Subarmalis", [("legion_segmentata_cape_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_cape_5", "Lorica Segmentata with Cape and Subarmalis", [("legion_segmentata_cape_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_segmentata_cape_6", "Lorica Segmentata with Cape and Subarmalis", [("legion_segmentata_cape_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["auxilia_cavalry_squamata_1", "Lorica Squamata", [("auxilia_cavalry_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_cavalry_squamata_2", "Lorica Squamata", [("auxilia_cavalry_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_1", "Lorica Squamata", [("legion_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_2", "Lorica Squamata", [("legion_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_3", "Lorica Squamata", [("legion_squamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_4", "Lorica Squamata", [("legion_squamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_5", "Lorica Squamata", [("legion_squamata_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_6", "Lorica Squamata", [("legion_squamata_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_7", "Lorica Squamata", [("legion_squamata_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_8", "Lorica Squamata", [("legion_squamata_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_9", "Lorica Squamata", [("legion_squamata_9",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["auxilia_squamata_east_1", "Lorica Squamata Orientalis", [("auxilia_squamata_east_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_squamata_east_2", "Lorica Squamata Orientalis", [("auxilia_squamata_east_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_squamata_east_3", "Lorica Squamata Orientalis", [("auxilia_squamata_east_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["auxilia_squamata_east_4", "Lorica Squamata Orientalis", [("auxilia_squamata_east_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["oriental_squamata_1", "Lorica Squamata Orientalis", [("oriental_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["oriental_squamata_2", "Lorica Squamata Orientalis", [("oriental_squamata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["oriental_squamata_3", "Lorica Squamata Orientalis", [("oriental_squamata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["oriental_squamata_4", "Lorica Squamata Orientalis", [("oriental_squamata_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],


["legion_squamata_10", "Lorica Squamata with Subarmalis", [("legion_squamata_10",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_11", "Lorica Squamata with Subarmalis", [("legion_squamata_11",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_12", "Lorica Squamata with Subarmalis", [("legion_squamata_12",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_13", "Lorica Squamata with Subarmalis", [("legion_squamata_13",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_14", "Lorica Squamata with Subarmalis", [("legion_squamata_14",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_squamata_cape_1", "Lorica Squamata with Cape", [("legion_squamata_cape_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_cape_2", "Lorica Squamata with Cape", [("legion_squamata_cape_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_cape_3", "Lorica Squamata with Cape", [("legion_squamata_cape_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["legion_squamata_cape_4", "Lorica Squamata with Cape and Subarmalis", [("legion_squamata_cape_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["legion_squamata_cape_5", "Lorica Squamata with Cape and Subarmalis", [("legion_squamata_cape_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["musculata_1", "Lorica Musculata with Cape", [("musculata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_2", "Lorica Musculata with Cape", [("musculata_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_3", "Lorica Musculata with Cape", [("musculata_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_centurio_armor_price, roman_centurio_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["musculata_legatus_1", "Lorica Musculata with Cape", [("musculata_legatus_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_2", "Lorica Musculata with Cape", [("musculata_legatus_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_3", "Lorica Musculata with Cape", [("musculata_legatus_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_4", "Lorica Musculata with Cape", [("musculata_legatus_4",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_5", "Lorica Musculata with Cape", [("musculata_legatus_5",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_6", "Lorica Musculata with Cape", [("musculata_legatus_6",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_7", "Lorica Musculata with Cape", [("musculata_legatus_7",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_8", "Lorica Musculata with Cape", [("musculata_legatus_8",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_9", "Lorica Musculata with Cape", [("musculata_legatus_9",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["musculata_legatus_10", "Lorica Musculata with Cape", [("musculata_legatus_10",0)], itp_type_body_armor|itp_covers_legs,0,
roman_legate_armor_price, roman_legate_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["signifer_auxilia_hamata_1", "Lorica Hamata (Signifer)", [("signifer_auxilia_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["signifer_legion_squamata", "Lorica Squamata (Signifer)", [("signifer_legion_squamata",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["signifer_legion_hamata", "Lorica Hamata (Signifer)", [("signifer_legion_hamata",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["vexilarius_legion_hamata_1", "Lorica Hamata (Vexilarius)", [("vexilarius_legion_hamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],
["vexilarius_praetorian_squamata_1", "Lorica Hamata (Vexilarius)", [("vexilarius_praetorian_squamata_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]),], [fac_culture_7] ],

["praetorian_segmentata_1", "Lorica Segmentata Praetoriani", [("praetorian_segmentata_1",0)], itp_type_body_armor|itp_covers_legs, 0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor, imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["praetorian_segmentata_2", "Lorica Segmentata Praetoriani", [("praetorian_segmentata_2",0)], itp_type_body_armor|itp_covers_legs, 0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor, imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["praetorian_segmentata_3", "Lorica Segmentata Praetoriani", [("praetorian_segmentata_3",0)], itp_type_body_armor|itp_covers_legs, 0,
roman_segementata_heavy_armor_price, roman_segementata_heavy_armor, imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],

["subarmalis_1", "Subarmalis", [("subarmalis_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["subarmalis_2", "Subarmalis", [("subarmalis_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["subarmalis_3", "Subarmalis", [("subarmalis_3",0),], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],

["military_tunic_1", "Military Tunic", [("military_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["military_tunic_2", "Military Tunic", [("military_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["military_tunic_3", "Military Tunic", [("military_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],
["military_tunic_4", "Military Tunic", [("military_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_light_armor_price, roman_light_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing"),]), ], [fac_culture_7] ],

["aux_slinger", "Funditores Tunic", [("slinger_south",0)], itp_type_body_armor|itp_covers_legs,0,
roman_light_armor_price, roman_light_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_culture_7] ],

["aux_slinger_2", "Funditores Tunic", [("slinger_south_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_light_armor_price, roman_light_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_culture_7] ],

["aux_slinger_3", "Funditores Tunic", [("slinger_south_3",0)], itp_type_body_armor|itp_covers_legs,0,
roman_light_armor_price, roman_light_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_culture_7] ],

["legion_squamata_cape_pants_long_1", "Lorica Squamata with Cape", [("legion_squamata_cape_pants_long_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_squamata_cape_pants_long_2", "Lorica Squamata with Cape", [("legion_squamata_cape_pants_long_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["legion_squamata_pants_long_1", "Lorica Squamata", [("legion_squamata_pants_long_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_squamata_pants_long_2", "Lorica Squamata", [("legion_squamata_pants_long_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_scale_armor_price, roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["legion_squamata_syria_1", "Lorica Squamata Syria", [("legion_squamata_syria_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_squamata_syria_2", "Lorica Squamata Syria", [("legion_squamata_syria_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["legion_hamata_cape_pants_long_1", "Lorica Hamata with Cape", [("legion_hamata_cape_pants_long_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_hamata_cape_pants_long_2", "Lorica Hamata with Cape", [("legion_hamata_cape_pants_long_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_hamata_pants_long_1", "Lorica Hamata", [("legion_hamata_pants_long_1",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
["legion_hamata_pants_long_2", "Lorica Hamata", [("legion_hamata_pants_long_2",0)], itp_type_body_armor|itp_covers_legs,0,
roman_mail_armor_price, roman_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],
###END ROMAN ARMOURY


#Garamantian
["garmantian_armor_1", "Garamantian Loincloth with Leopardskin", [("garmantian_armor_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["garmantian_armor_2", "Garamantian Loincloth with Leopardskin", [("garmantian_armor_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["garmantian_armor_3", "Garamantian Loincloth with Leathercoat", [("garmantian_armor_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["garmantian_armor_4", "Garamantian Loincloth with Leathercoat", [("garmantian_armor_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),]),], [] ],
["garmantian_armor_5", "Garamantian Loincloth", [("garmantian_armor_5",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),]),], [] ],

["numidian_armor", "Nubian Loincloth", [("nubian_shirtless",0)], itp_unique|itp_type_body_armor|itp_force_show_body|itp_attach_armature|itp_civilian,0,
1500, weight(1)|head_armor(0)|body_armor(5)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], [] ],
["numidian_armor_1", "Berber Tunic", [("berber_tunic_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_roman_slinger"),],),], [] ],
["numidian_armor_2", "Berber Tunic", [("berber_tunic_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_roman_slinger"),],),], [] ],
["numidian_armor_3", "Berber Tunic", [("berber_tunic_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_roman_slinger"),],),], [] ],
["numidian_armor_4", "Berber Mail Shirt with Leopardskin", [("berber_tunic_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
breastplate_iron_armor_price, breastplate_iron_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_armor_merc"),],),], [] ],
["numidian_armor_5", "Berber Tunic with Leopardskin", [("berber_tunic_5",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_armor_merc"),],),], [] ],

["nubian_tunic", "Nubian Tunic", [("nubian_tunic",0)], itp_unique|itp_type_body_armor|itp_civilian|itp_covers_legs,0,
tunic_armor_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_roman_slinger"),],),], [] ],
["nubian_kilt", "Nubian Loincloth", [("nubian_kilt",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["nubian_kilt_2", "Nubian Loincloth with Leopardskin", [("nubian_kilt_2",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["nubian_kilt_3", "Nubian Leopard Loincloth", [("nubian_kilt_3",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["kilt_a", "Loincloth", [("kilt_a",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["kilt_b", "Loincloth", [("kilt_b",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["kilt_c", "Loincloth", [("kilt_c",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],
["kilt_d", "Loincloth", [("kilt_d",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),],),], [] ],

##indian
["indian_pants", "Eastern Loincloth", [("indian_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),
(store_trigger_param_1, ":agent"),
(store_trigger_param_2, ":troop_no"),
(try_begin),
    (agent_is_active, ":agent"),
	(neq, ":troop_no", "trp_player"),
	(neq, ":troop_no", "trp_slave"),
	(neq, ":troop_no", "trp_slave_mine"),
	(store_random_in_range, ":r", 0, 5),
	(try_begin),
		(lt, ":r", 3),
		(str_clear, s2),
		(cur_item_add_mesh, "str_o_greek_fibule_2"),
		(store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
		(str_store_string, s2, ":rand"),
		(cur_item_add_mesh, s2),
	(try_end),
(try_end),]),], [fac_culture_6] ],
["indian_pants_1", "Eastern Loincloth", [("indian_tunic_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor, imodbits_cloth, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),
(store_trigger_param_1, ":agent"),
(store_trigger_param_2, ":troop_no"),
(try_begin),
    (agent_is_active, ":agent"),
	(neq, ":troop_no", "trp_player"),
	(neq, ":troop_no", "trp_slave"),
	(neq, ":troop_no", "trp_slave_mine"),
	(store_random_in_range, ":r", 0, 5),
	(try_begin),
		(lt, ":r", 3),
		(str_clear, s2),
		(cur_item_add_mesh, "str_o_greek_fibule_2"),
		(store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
		(str_store_string, s2, ":rand"),
		(cur_item_add_mesh, s2),
	(try_end),
(try_end),]),], [fac_culture_6] ],
["indian_pants_2", "Eastern Loincloth with Breastplate", [("indian_tunic_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
breastplate_iron_armor_price, breastplate_iron_armor, imodbits_armor, [(ti_on_init_item,[
(call_script, "script_init_pants_long"),
(store_trigger_param_1, ":agent"),
(store_trigger_param_2, ":troop_no"),
(try_begin),
    (agent_is_active, ":agent"),
	(neq, ":troop_no", "trp_player"),
	(neq, ":troop_no", "trp_slave"),
	(neq, ":troop_no", "trp_slave_mine"),
	(store_random_in_range, ":r", 0, 5),
	(try_begin),
		(lt, ":r", 3),
		(str_clear, s2),
		(cur_item_add_mesh, "str_o_greek_fibule_2"),
		(store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
		(str_store_string, s2, ":rand"),
		(cur_item_add_mesh, s2),
	(try_end),
(try_end),]),], [fac_culture_6] ],

##############
##############
##############
#barbarian naked
["celtic_naked1", "Celtic Trousers", [("ad_caped_trousers_celtic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor, imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked2", "Celtic Trousers", [("ad_caped_trousers_celtic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked3", "Celtic Trousers", [("ad_caped_trousers_celtic_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],

["celtic_naked4", "Celtic Trousers", [("ad_trousers_celtic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked5", "Celtic Trousers", [("ad_trousers_celtic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked6", "Celtic Trousers", [("ad_trousers_celtic_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked7", "Celtic Trousers", [("ad_trousers_celtic_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked8", "Celtic Trousers", [("ad_trousers_celtic_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked9", "Celtic Trousers", [("ad_trousers_celtic_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked10", "Celtic Trousers", [("celtscape1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked11", "Celtic Trousers", [("celtscape2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked12", "Celtic Trousers", [("celtscape3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked13", "Celtic Trousers", [("celtsl1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked14", "Celtic Trousers", [("celtsl2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],
["celtic_naked15", "Celtic Trousers", [("celtsl3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [], [fac_culture_2,fac_culture_2_1, fac_culture_1] ],

#celtic light
["celtic_light1", "Celtic Shirt with Cape", [("ad_longsleeveshirt_celtic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [

    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),
    ]),

], [fac_culture_2,fac_culture_2_1] ],
["celtic_light2", "Celtic Shirt with Cape", [("ad_longsleeveshirt_celtic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),
    ]),
], [fac_culture_2,fac_culture_2_1] ],
["celtic_light3", "Celtic Shirt", [("ad_longsleeveshirt_celtic_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light4", "Celtic Shirt with Cape", [("ad_longsleeveshirt_celtic_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_2,fac_culture_2_1] ],
["celtic_light5", "Celtic Shirt with Cape", [("ad_longsleeveshirt_celtic_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_2,fac_culture_2_1] ],
["celtic_light6", "Celtic Shirt", [("ad_longsleeveshirt_celtic_06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light7", "Celtic Shirt", [("ad_longsleeveshirt_celtic_07",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light8", "Celtic Shirt", [("ad_longsleeveshirt_celtic_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light9", "Celtic Shirt", [("ad_longsleeveshirt_celtic_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light10", "Celtic Shirt", [("ad_longsleeveshirt_celtic_10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light11", "Celtic Shirt", [("ad_longsleeveshirt_celtic_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light12", "Celtic Shirt", [("ad_longsleeveshirt_celtic_12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],

["celtic_light_noble_1", "Celtic Noble Shirt with Cape", [("ad_longsleeveshirt_celtic_11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light_noble_2", "Celtic Noble Shirt with Cape", [("ad_longsleeveshirt_celtic_09",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light_noble_3", "Celtic Noble Shirt with Cape", [("ad_longsleeveshirt_celtic_08",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_light_noble_4", "Celtic Noble Shirt with Cape", [("ad_longsleeveshirt_celtic_12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],

#celtic heavy
["celtic_heavy1", "Celtic Hamata", [("celtic_mail_ws_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_heavy2", "Celtic Hamata", [("celtic_mail_ws_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_heavy3", "Celtic Hamata", [("celtic_mail_ws_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_heavy4", "Celtic Hamata", [("celtic_mail_ws_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
roman_mail_heavy_armor_price, roman_mail_heavy_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_noble_1", "Celtic Noble Hamata", [("celtic_noble_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_noble_2", "Celtic Noble Hamata", [("celtic_noble_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_noble_3", "Celtic Noble Hamata", [("celtic_noble_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],
["celtic_noble_4", "Celtic Noble Hamata", [("celtic_noble_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_2,fac_culture_2_1] ],

#celts painted
["celts_painted1", "Painted Body", [("war_paint_two",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_price, naked_armor, imodbits_cloth, [], [fac_culture_2,fac_culture_2_1] ],
["celts_painted2", "Painted Body", [("war_paintus",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted3", "Painted Body", [("war_paintus_3",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted4", "Painted Body", [("war_paintus_4",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted5", "Painted Body", [("war_paintus_7",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_price, naked_armor, imodbits_cloth, [], [fac_culture_2,fac_culture_2_1] ],
["celts_painted6", "Painted Body", [("war_paintus_8",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted7", "Painted Body", [("war_paintus_10",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted8", "Painted Body", [("war_paintus_11",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_price, naked_armor, imodbits_cloth, [], [fac_culture_2,fac_culture_2_1] ],
["celts_painted9", "Painted Body", [("2celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),
], [fac_culture_2,fac_culture_2_1] ],
["celts_painted10", "Painted Body", [("3celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_cape_price,naked_cape_armor, imodbits_cloth, [    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end), ]),], [fac_culture_2,fac_culture_2_1] ],
["celts_painted11", "Painted Body", [("5celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_price, naked_armor, imodbits_cloth, [], [fac_culture_2,fac_culture_2_1] ],
["celts_painted12", "Painted Body", [("6celtbody",0)],itp_unique|itp_type_body_armor  |itp_covers_legs ,0,
naked_price, naked_armor, imodbits_cloth, [], [fac_culture_2,fac_culture_2_1] ],

["dacian_naked1", "Dacian Trousers", [("ad_trousers_dacian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked2", "Dacian Trousers", [("ad_trousers_dacian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked3", "Dacian Trousers", [("ad_trousers_dacian_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked4", "Dacian Trousers", [("dacishirtless1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked5", "Dacian Trousers", [("dacishirtless2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked6", "Dacian Trousers", [("dacishirtless3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked7", "Dacian Trousers", [("dacishirtless4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_naked8", "Dacian Trousers", [("dacishirtless5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],

#dacian light
["dacian_light1", "Dacian Tunic", [("dccloth1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light2", "Dacian Tunic", [("dccloth2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light3", "Dacian Tunic", [("dccloth3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light4", "Dacian Tunic", [("dccloth4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light5", "Dacian Tunic", [("dccloth5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light6", "Dacian Tunic", [("dccloth6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
#dacian cloths
["dacian_light7", "Dacian Tunic", [("dac_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light8", "Dacian Tunic", [("dac_tunic1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light9", "Dacian Tunic with Cape", [("dac_tunic2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],

["dacian_light10", "Dacian Tunic with Cape", [("dac_tunic3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light11", "Dacian Tunic", [("dac_tunic4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),

(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_light12", "Dacian Tunic", [("dac_tunic5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_1", "str_capes_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
#dacian noble cloth
["dacian_noble1", "Dacian Tunic with Cape", [("bastarn_noble_tunic7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [

    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_1] ],
["dacian_noble2", "Dacian Tunic with Cape", [("bastarn_noble_tunic8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_1] ],
["dacian_noble3", "Dacian Tunic with Cape", [("bastarn_noble_tunic9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[(store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_1] ],
["dacian_noble4", "Dacian Tunic", [("bastarn_noble_tunic7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_noble5", "Dacian Tunic", [("bastarn_noble_tunic8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_noble6", "Dacian Tunic", [("bastarn_noble_tunic9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],

#dacian medium
["dacian_medium1", "Dacian Squamata", [("dcstudded1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_medium2", "Dacian Squamata", [("dcstudded2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_medium3", "Dacian Squamata", [("dcstudded3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price,pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_medium4", "Dacian Hamata", [("dcstudded4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price,pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_medium5", "Dacian Hamata", [("dcstudded5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_medium6", "Dacian Hamata", [("dcstudded6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price,pants_with_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],

#dacian heavy
["dacian_heavy1", "Dacian Noble Squamata", [("dcchain1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_heavy2", "Dacian Noble Squamata", [("dcchain2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_heavy3", "Dacian Noble Hamata", [("dcchain3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_heavy4", "Dacian Noble Hamata", [("dcchain4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_heavy5", "Dacian Noble Squamata", [("dcchain5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],
["dacian_heavy6", "Dacian Noble Squamata", [("dcchain6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_1] ],


["germanic_completenaked1", "Germanic Pants with Bearskin", [("germloincloth1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_completenaked2", "Germanic Pants with Bearskin", [("germloincloth2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_completenaked3", "Germanic Pants with Bearskin", [("germloincloth3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_completenaked4", "Germanic Pants with Bearskin", [("germloincloth4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_completenaked5", "Germanic Pants with Wolfskin", [("germloincloth5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_completenaked6", "Germanic Pants with Wolfskin", [("germloincloth6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_fur_price, pants_fur_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],


#germanic
["germanic_naked1", "Germanic Trousers", [("ad_caped_trousers_germanic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_naked2", "Germanic Trousers", [("ad_caped_trousers_germanic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_naked4", "Germanic Trousers", [("gmcshirtls1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_naked5", "Germanic Trousers", [("gmcshirtls2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_naked6", "Germanic Trousers", [("gmcshirtls3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],
["germanic_naked7", "Germanic Trousers", [("gmcshirtls4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_pants_long_german"),]),], [fac_culture_4] ],

["german_body_paint_1_black", "Germanic Painted Body", [("german_body_paint_1_black",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],
["german_body_paint_2_black", "Germanic Painted Body", [("german_body_paint_2_black",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],
["german_body_paint_3_black", "Germanic Painted Body", [("german_body_paint_3_black",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],
["german_body_paint_4_black", "Germanic Painted Body", [("german_body_paint_4_black",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],
["german_body_paint_5_black", "Germanic Painted Body", [("german_body_paint_5_black",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_price, pants_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],

#germanic light
["germanic_noble_tunic_1", "Germanic Noble Tunic with Cape", [("germanic_noble_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_4"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_4] ],
["germanic_noble_tunic_2", "Germanic Noble Tunic with Cape", [("germanic_noble_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_3"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_4] ],
["germanic_noble_tunic_3", "Germanic Noble Tunic with Cape", [("germanic_noble_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_2"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_4] ],
["germanic_noble_tunic_4", "Germanic Noble Tunic with Cape", [("germanic_noble_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [
    (ti_on_init_item,[
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_celt_cape_noble_1"),
    (else_try),
        (store_random_in_range, ":rand", "str_celt_cape_noble_1", "str_capes_noble_end"),
        (str_store_string, s2, ":rand"),
        (cur_item_add_mesh, s2),
    (try_end),
    (call_script, "script_init_eastern_troop"),]),
], [fac_culture_4] ],

["germanic_light1", "Germanic Tunic", [("ad_longsleeveshirt_germanic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light2", "Germanic Tunic", [("ad_longsleeveshirt_germanic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light3", "Germanic Tunic", [("ad_longsleeveshirt_germanic_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [], [fac_culture_4] ],
["germanic_light4", "Germanic Tunic", [("ad_longsleeveshirt_germanic_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4]],
["germanic_light5", "Germanic Tunic", [("germanshirt1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light6", "Germanic Tunic", [("germanshirt2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],

["germanic_light7", "Germanic Tunic", [("germanshirt3",0)],
itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light8", "Germanic Tunic", [("germanshirt4",0)],
itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light9", "Germanic Tunic", [("germanshirt5",0)],
itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light10", "Germanic Tunic", [("germanshirt6",0)],
itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_light11", "Germanic Tunic with Cape", [("germanshirt7",0)],
itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_cape_price, pants_shirt_cape_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],

#germanic medium
["germanic_medium1", "Germanic Fur Armor", [("grsmalshirt7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_medium2", "Germanic Fur Armor", [("grsmalshirt8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_medium3", "Germanic Fur Armor", [("grsmalshirt1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_medium4", "Germanic Fur Armor", [("grsmalshirt2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_medium5", "Germanic Fur Armor", [("grsmalshirt3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_medium6", "Germanic Fur Armor", [("grsmalshirt4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],


#germanic heavy
["germanic_heavy1", "Germanic Hamata", [("grsmalshirt5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price,pants_with_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
["germanic_heavy2", "Germanic Hamata", [("grsmalshirt6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price,pants_with_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_4] ],
# ["byrnie", "Germanic Hamata", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# pants_with_mail_price,pants_with_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],

["germanic_noble_1", "Germanic Hamata", [("BL_VikingByrnie01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price,noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_2", "Germanic Hamata", [("BL_VikingByrnie03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price,noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_3", "Germanic Hamata", [("BL_VikingByrnie05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price,noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_4", "Germanic Hamata", [("BL_VikingByrnie06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price,noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
# ["germanic_noble_5", "Germanic Hamata", [("BL_VikingByrnie09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# noble_mail_price,noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_6", "Germanic Hamata with Wolfskin", [("berserker_noble",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
mail_fur_price, mail_fur_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_7", "Germanic Hamata with Cloak", [("berserker_noble_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price, noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_8", "Germanic Hamata with Bearskin", [("berserker_noble_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
mail_fur_price, mail_fur_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],
["germanic_noble_9", "Germanic Hamata with Cloak", [("berserker_noble_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
noble_mail_price, noble_mail_armor, imodbits_armor, [(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[fac_culture_4] ],

#alan items
["alan_light_1", "Kaftan", [("alan_vest_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_light_2", "Kaftan", [("alan_vest_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_medium_1", "Alan Lamellar Armour", [("alan_lamellar_vest_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_2_price, pants_medium_armor_2_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_medium_2", "Alan Lamellar Armour", [("alan_lamellar_vest_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_2_price, pants_medium_armor_2_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_medium_3", "Alan Lamellar Armour", [("alan_lamellar_vest_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_2_price, pants_medium_armor_2_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_heavy_1", "Alan Heavy Lamellar Armor", [("alan_lamellar_armour_full",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_armored_linothorax_price, pants_armored_linothorax_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

["alan_heavy_2", "Alan Heavy Lamellar Armor", [("alan_lamellar_armour_full_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_armored_linothorax_price, pants_armored_linothorax_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_3]  ],

#sarmatian light
["kaftan_1", "Kaftan", [("alan_kaftan_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["kaftan_2", "Kaftan", [("alan_kaftan_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["kaftan_3", "Kaftan", [("alan_kaftan_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["sarmatian_light1", "Sarmatian Clothing", [("ad_light_sarmatian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    ]),
    ], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_light2", "Sarmatian Clothing", [("ad_light_sarmatian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_light3", "Sarmatian Padded Clothing", [("ad_padded_sarmatian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_light4", "Sarmatian Padded Clothing", [("ad_padded_sarmatian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth ,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    ]),
], [fac_culture_3,fac_culture_9,fac_culture_5]],
["sarmatian_light5", "Sarmatian Clothing", [("ad_light_sarmatian_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_light6", "Sarmatian Clothing", [("ad_light_sarmatian_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_light7", "Sarmatian Clothing", [("ad_light_sarmatian_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["sarmitian_mail_1", "Sarmatian Mail Armor", [("sarmatian_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_mail_2", "Sarmatian Mail Armor", [("sarmatian_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_mail_3", "Sarmatian Mail Armor", [("sarmatian_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_mail_4", "Sarmatian Mail Armor", [("sarmatian_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["saka_armour_1", "Saka Lamellar Armour", [("saka_armour_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_dahae] ],
["saka_armour_2", "Saka Lamellar Armour", [("saka_armour_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_dahae] ],
["saka_armour_3", "Saka Lamellar Armour", [("saka_armour_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_dahae] ],
["saka_armour_4", "Saka Lamellar Armour", [("saka_armour_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_dahae] ],

["sarmitian_scale_1", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_2", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_3", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_4", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["sarmitian_scale_9", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_10", "Sarmatian Mail with Scale Armor", [("sarmatian_mail_and_scale_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["sarmitian_scale_5", "Sarmatian Scale Armor", [("sarmatian_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_6", "Sarmatian Scale Armor", [("sarmatian_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_7", "Sarmatian Scale Armor", [("sarmatian_scale_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmitian_scale_8", "Sarmatian Scale Armor", [("sarmatian_scale_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

#scythian
["scythian_light1", "Scythian Clothing", [("ad_scythian_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_light2", "Scythian Clothing", [("ad_scythian_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_light3", "Scythian Clothing", [("ad_scythian_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_light4", "Scythian Clothing", [("ad_scythian_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_light5", "Scythian Clothing", [("ad_scythian_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_heavy1", "Scythian Scale Armor", [("ad_linothorax_heavy_scythian_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_armored_linothorax_price,pants_armored_linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

["scythian_heavy2", "Scythian Scale Armor", [("ad_linothorax_heavy_scythian_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_armored_linothorax_price,pants_armored_linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_9] ],

#bosporan
["bosporan_light1", "Bosporan Clothing", [("bosphoran_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_white_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end), ]),
    ], [fac_culture_9] ],
["bosporan_light2", "Bosporan Clothing", [("bosphoran_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_red_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end), ]),
    ], [fac_culture_9] ],
["bosporan_light3", "Bosporan Clothing", [("bosphoran_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_blue_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end),
    ]),
    ], [fac_culture_3] ],
["bosporan_light4", "Bosporan Clothing", [("bosphoran_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"), ]),
    ], [fac_culture_9] ],
["bosphoran_scale_1", "Bosphoran Mail with Scale Armor", [("bosphoran_mail_and_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["bosphoran_scale_2", "Bosphoran Mail with Scale Armor", [("bosphoran_mail_and_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["bosphoran_scale_3", "Bosphoran Scale Armor", [("bosphoran_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["bosphoran_scale_4", "Bosphoran Scale Armor", [("bosphoran_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["bosporan_mail_1", "Bosporan Mail Armor", [("bosphoran_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),
    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_red_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (neq, ":troop", "trp_player"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end),

]),], [fac_culture_9] ],
["bosporan_mail_2", "Bosporan Mail Armor", [("bosphoran_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),

    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_purple_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (neq, ":troop", "trp_player"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end),]),
], [fac_culture_9] ],
["bosporan_mail_3", "Bosporan Mail Armor", [("bosphoran_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),

    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop"),
    (try_begin),
        (eq, ":troop", "trp_player"),
        (cur_item_add_mesh, "str_a_greek_cape_red_2"),
        (cur_item_add_mesh, "str_o_greek_fibule_2"),
    (else_try),
        (agent_is_active, ":agent"),
        (neq, ":troop", "trp_player"),
        (store_random_in_range, ":r", 0, 100),
        (try_begin),
            (lt, ":r", 65),
            (str_clear, s2),
            (store_random_in_range, ":rand", "str_a_greek_cape_blue_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
        (try_end),
    (try_end),

]),], [fac_culture_9] ],

##caucasian
["caucasian_scale_heavy_1", "Caucasian Heavy Scale Armor", [("caucasian_scale_heavy_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["caucasian_scale_heavy_2", "Caucasian Heavy Scale Armor", [("caucasian_scale_heavy_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["caucasian_scale_1", "Caucasian Scale Armor", [("caucasian_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

["caucasian_scale_2", "Caucasian Scale Armor", [("caucasian_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_3,fac_culture_9,fac_culture_5] ],

##armenian
["armenian_tunic_1", "Armenian Tunic", [("armenian_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_5]  ],
["armenian_tunic_2", "Armenian Tunic", [("armenian_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_5]  ],
["armenian_tunic_3", "Armenian Tunic", [("armenian_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_5]  ],
["armenian_tunic_4", "Armenian Tunic", [("armenian_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_5]  ],

["armenian_mail_1", "Armenian Mail Armor", [("armenian_lamellar_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_linothorax_price, pants_linothorax_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["armenian_mail_2", "Armenian Mail Armor", [("armenian_lamellar_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_linothorax_price, pants_linothorax_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["armenian_scale_1", "Armenian Scale Armor", [("armenian_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["armenian_scale_2", "Armenian Scale Armor", [("armenian_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],

["persian_sheepskin_1", "Tunic with Sheepskin", [("persian_sheepskin_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6, fac_culture_5]  ],
["persian_sheepskin_2", "Tunic with Sheepskin", [("persian_sheepskin_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6, fac_culture_5]  ],
["persian_sheepskin_3", "Tunic with Sheepskin", [("persian_sheepskin_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6, fac_culture_5]  ],
["persian_sheepskin_4", "Tunic with Sheepskin", [("persian_sheepskin_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6, fac_culture_5]  ],

#persian
["persian_tunic_1", "Persian Tunic", [("persian_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_persian"),]),
], [fac_culture_6]  ],
["persian_tunic_2", "Persian Tunic", [("persian_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_persian"),]),
], [fac_culture_6]  ],
["persian_tunic_3", "Persian Tunic", [("persian_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_persian"),]),
], [fac_culture_6]  ],
["persian_tunic_4", "Persian Tunic", [("persian_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_persian"),]),
], [fac_culture_6]  ],

#parthian
["parthian_tunic_1", "Parthian Tunic", [("parthian_tunic_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6]  ],
["parthian_tunic_2", "Parthian Tunic", [("parthian_tunic_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6]  ],
["parthian_tunic_3", "Parthian Tunic", [("parthian_tunic_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6]  ],
["parthian_tunic_4", "Parthian Tunic", [("parthian_tunic_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
pants_shirt_price, pants_shirt_armor,imodbits_cloth, [
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),
], [fac_culture_6]  ],

["parthian_mail_1", "Parthian Mail Armor", [("parthian_lamellar_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_linothorax_price, pants_linothorax_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["parthian_mail_2", "Parthian Mail Armor", [("parthian_lamellar_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_linothorax_price, pants_linothorax_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],

["parthian_scale_1", "Parthian Scale Armor", [("parthian_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["parthian_scale_2", "Parthian Scale Armor", [("parthian_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],

["parthian_scale_heavy_1", "Parthian Heavy Scale Armor", [("parthian_heavy_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["parthian_scale_heavy_2", "Parthian Heavy Scale Armor", [("parthian_heavy_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],

#cataphract armor
["cataphract_eastern", "Cataphract Scale Armor", [("armor_cataphract_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
cataphract_price, cataphract_armor,imodbits_armor, [], [fac_culture_6, fac_culture_5]  ],
["sarranid_elite_armor", "Cataphract Scale Armor", [("armor_cataphract_2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
cataphract_price, cataphract_armor,imodbits_armor, [], [fac_culture_5, fac_culture_6] ],
["sarranid_elite_armor_2", "Cataphract Lamellar Armor", [("armor_cataphract_3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
cataphract_price, cataphract_armor,imodbits_armor, [], [fac_culture_5, fac_culture_6] ],
["sarranid_elite_armor_3", "Cataphract Lamellar Armor", [("armor_cataphract_4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
cataphract_price, cataphract_armor,imodbits_armor, [], [fac_culture_5, fac_culture_6] ],
["mamluke_mail", "Cataphract Mail Armor", [("sarranid_elite_cavalary",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs,0,
cataphract_price, cataphract_armor,imodbits_armor, [], [fac_culture_5, fac_culture_6] ],

#illyrian medium armor
["illyrian_medium1", "Illyrian Armor", [("ad_celto_illyrian_armours_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["illyrian_medium2", "Illyrian Armor", [("ad_celto_illyrian_armours_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["illyrian_medium3", "Illyrian Armor", [("ad_celto_illyrian_armours_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_medium_armor_price, pants_medium_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_set_roman_clothing_2"),]),], [fac_culture_7] ],

["illyrian_medium4", "Illyrian Armor", [("ad_illyrian_tunic_round_pectoral_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

["illyrian_medium5", "Illyrian Armor", [("ad_illyrian_tunic_round_pectoral_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

#illyrian light
["iberian_light1", "Illyrian Tunic", [("ad_illyrian_tunic_armours_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

["iberian_light2", "Illyrian Tunic", [("ad_illyrian_tunic_armours_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

#ibarian tunic
["iberian_light6", "Iberian Tunic", [("ad_iberian_tunic_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

["iberian_light5", "Iberian Tunic", [("ad_iberian_tunic_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

["iberian_light3", "Iberian Tunic", [("ad_iberian_tunic_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

["iberian_light4", "Iberian Tunic", [("ad_iberian_tunic_04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

#ibarian heavy
["iberian_heavy1", "Iberian Armor", [("ad_iberian_scale_vest_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

["iberian_heavy2", "Iberian Armor", [("ad_iberian_scale_vest_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7] ],

#ibarian medium armor
["iberian_medium1", "Iberian Armor", [("ad_iberian_tunic_round_pectoral_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

["iberian_medium2", "Iberian Armor", [("ad_iberian_tunic_round_pectoral_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

["iberian_medium3", "Iberian Armor", [("ad_iberian_tunic_round_pectoral_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
tunic_light_armor_price, tunic_light_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7]  ],

#arabian
["arabian_tunic_1", "Arabian Tunic", [("arabian_cloth_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7,fac_culture_6,fac_culture_8] ],
["arabian_tunic_2", "Arabian Tunic", [("arabian_cloth_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7,fac_culture_6,fac_culture_8] ],
["arabian_tunic_3", "Arabian Tunic", [("arabian_cloth_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7,fac_culture_6,fac_culture_8] ],

["arabian_armor_b", "Arabian Lamella Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_linothorax_price,pants_linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8]],

["sarranid_mail_shirt", "Arabian Lamella Armor", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_linothorax_price,pants_linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

#palmyran stuff
["palmyran_lamellar_armor", "Palmyrene Lamellar Armor", [("palmyran_lamellar_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["palmyran_lamellar_armor_2", "Palmyrene Lamellar Armor", [("palmyran_lamellar_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["palmyran_lamellar_armor_3", "Palmyrene Lamellar Armor", [("palmyran_lamellar_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],

["palmyran_lamellar_armor_heavy_1", "Heavy Palmyrene Lamellar Armor", [("palmyran_lamellar_armor_heavy",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["palmyran_lamellar_armor_heavy_2", "Heavy Palmyrene Lamellar Armor", [("palmyran_lamellar_armor_heavy_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
["palmyran_lamellar_armor_heavy_3", "Heavy Palmyrene Lamellar Armor", [("palmyran_lamellar_armor_heavy_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
noble_mail_price, noble_mail_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_6, fac_culture_5]  ],
#end palmyran stuff

#judean
["judean_tunic_1", "Eastern Tunic", [("judean_tunic_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["judean_tunic_2", "Eastern Tunic", [("judean_tunic_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["judean_tunic_3", "Eastern Tunic", [("judean_tunic_3",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["judean_tunic_4", "Eastern Tunic", [("judean_tunic_4",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["judean_tunic_5", "Eastern Tunic", [("judean_tunic_5",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["judean_tunic_6", "Eastern Tunic", [("judean_tunic_6",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],

["judean_mail_1", "Judean Hamata", [("judean_mail_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_mail_2", "Judean Hamata", [("judean_mail_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_mail_3", "Judean Hamata", [("judean_mail_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_mail_4", "Judean Hamata", [("judean_mail_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_mail_5", "Judean Hamata", [("judean_mail_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_mail_6", "Judean Hamata", [("judean_mail_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],

["judean_scale_1", "Judean Squamata", [("judean_scale_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],
["judean_scale_2", "Judean Squamata", [("judean_scale_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
pants_with_mail_price, pants_with_mail_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),
]),], [fac_culture_8] ],

#Tunics and generic clothing
["linen_tunic", "Linen Tunic", [("shirt_a",0)],itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
tunic_armor_price,tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,
[
(call_script, "script_init_eastern_troop"),
]),] ],

["robe", "Priest Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
robe_armor_price,robe_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),] ),] ],

#generic poor
["generic_poor1", "Dirty Cloths", [("poor_cloth_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [] ],
["generic_poor2", "Dirty Cloths", [("poor_cloth_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_rich"),]),], [] ],

#roman poor
["roman_tunic_1", "Tunic with Cape", [("roman_tunic_new_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_simple"),]),], [fac_culture_7,fac_culture_8] ],
["roman_tunic_2", "Tunic with Cape", [("roman_tunic_new_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_simple"),]),], [fac_culture_7,fac_culture_8] ],
["roman_tunic_3", "Tunic with Cape", [("roman_tunic_new_3",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_simple"),]),], [fac_culture_7,fac_culture_8] ],

["roman_poor1", "Simple Tunic", [("ad_roman_tunic_01",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],

["roman_poor4", "Simple Tunic", [("new_tunic_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),],),], [fac_culture_7,fac_culture_8] ],

["roman_poor5", "Simple Tunic", [("new_tunic_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],

["roman_poor6", "Simple Tunic", [("new_tunic_a_1",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
8 , weight(2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0) ,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],
["roman_poor7", "Simple Tunic", [("new_tunic_a_2",0),], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],

["roman_poor2", "Simple Tunic", [("ad_roman_tunic_02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_poor"),]),], [fac_culture_7,fac_culture_8] ],

["roman_poor3", "Simple Tunic", [("toga_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
tunic_armor_price, tunic_armor_armor,imodbits_cloth,
[(ti_on_init_item,[
    (store_trigger_param_1, ":agent"),
    (store_trigger_param_2, ":troop_no"),
    (try_begin),
        (agent_is_active, ":agent"),
        (neq, ":troop_no", "trp_player"),
        (neq, ":troop_no", "trp_slave"),
        (neq, ":troop_no", "trp_slave_mine"),
        (neq, ":troop_no", "trp_circus_1"),
        (neq, ":troop_no", "trp_circus_2"),
        (neq, ":troop_no", "trp_circus_3"),
        (str_clear, s1),
        (store_random_in_range, ":string", "str_chiton_red", "str_chiton_end"),
        (str_store_string, s1, ":string"),
        (cur_item_set_material, s1, 0),
        (store_random_in_range, ":r", 0, 6),
        (try_begin),
            (lt, ":r", 4),
            (str_clear, s2),
            (cur_item_add_mesh, "str_o_greek_fibule_2"),
            (store_random_in_range, ":rand", "str_a_greek_cape_purple_2", "str_cape_end"),
            (str_store_string, s2, ":rand"),
            (cur_item_add_mesh, s2),
        (try_end),
    (try_end),
    (call_script, "script_init_roman_slinger"),
]),], [fac_culture_7,fac_culture_8] ],

["roman_toga", "Toga", [("cavalry_toga",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,
[(ti_on_init_item,[  (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_roman_rich"),    ]), ], [fac_culture_7] ],

["roman_toga_2", "Toga", [("cavalry_toga_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,
[(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_roman_rich"),]),], [fac_culture_7] ],

["roman_toga_3", "Toga", [("cavalry_toga_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,

[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_roman_rich"),]),], [fac_culture_7] ],

#roman rich
["roman_rich1", "Fancy Toga", [("aristocrats_cloth_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price,roman_rich_armor,imodbits_none,
[(ti_on_init_item,[(call_script, "script_init_roman_rich2"),]),], [fac_culture_7] ],

["roman_rich2", "Fancy Toga", [("aristocrats_cloth_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price,roman_rich_armor,imodbits_none,
[(ti_on_init_item,[(call_script, "script_init_roman_rich2"),]),], [fac_culture_7] ],

["roman_rich3", "Fancy Toga", [("aristocrats_cloth_03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price,roman_rich_armor,imodbits_none, [(ti_on_init_item,
[(call_script, "script_init_roman_rich2"),]),], [fac_culture_7] ],

["roman_noble_dress_1", "Roman Noble Dress", [("roman_noble_dress_pink",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_2", "Roman Noble Dress", [("roman_noble_dress_blue",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_3", "Roman Noble Dress", [("roman_noble_dress_yellow",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_4", "Roman Noble Dress", [("roman_noble_dress_green",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_5", "Roman Noble Dress", [("roman_noble_dress_red",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_6", "Roman Noble Dress", [("roman_noble_dress_blue2",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["roman_noble_dress_7", "Roman Noble Dress", [("roman_noble_dress_pink2",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],

["roman_femal_rich1_new", "Fancy Dress", [("new_dress_noble_1",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],
["roman_femal_rich2_new", "Fancy Dress", [("new_dress_noble_2",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],
["roman_femal_rich3_new", "Fancy Dress", [("new_dress_noble_3",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],

#new dresses for roman noble ladies during feasts
["new_dress_1", "Fancy Dress", [("new_dress",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_new"),]), ],[fac_culture_7] ],
["new_dress_2", "Fancy Dress", [("new_dress_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_new"),]), ],[fac_culture_7] ],
["new_dress_3", "Fancy Dress", [("new_dress_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_new"),]), ],[fac_culture_7] ],
["new_dress_4", "Fancy Dress", [("new_dress_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_new"),]), ],[fac_culture_7] ],

#germanic dresses
["german_femal_rich_1", "Germanic Noble Dress", [("germanic_dress_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ],[fac_culture_4] ],
["german_femal_rich_2", "Germanic Noble Dress", [("germanic_dress_brown",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ],[fac_culture_4] ],
["german_femal_rich_3", "Germanic Noble Dress", [("germanic_dress_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ],[fac_culture_4] ],
["german_femal_rich_4", "Germanic Noble Dress", [("germanic_dress_yellow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ],[fac_culture_4] ],

#barb rich female
["barb_femal_rich1", "Noble Dress", [("womans_noble_chiton2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["barb_femal_rich2", "Noble Dress", [("womans_noble_chiton3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["barb_femal_rich3", "Noble Dress", [("womans_noble_chiton4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["barb_femal_rich5", "Noble Dress", [("womans_noble_chiton6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

##lupa dresses
["roman_lupa_dress", "Dress", [("commoner_dress",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none, [
(ti_on_init_item,[
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],
["roman_lupa_dress_2", "Dress", [("commoner_dress_2",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none, [
(ti_on_init_item,[
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],
["roman_lupa_dress_3", "Dress", [("commoner_dress_3",0)], itp_merchandise|itp_type_body_armor|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none, [
(ti_on_init_item,[
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],

#generic barbarian dresses
["female_1", "Dress", [("womans_chiton",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["female_2", "Dress", [("womans_chiton1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["female_3", "Dress", [("womans_chiton2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms"),]), ], ],

["female_1_celt", "Dress", [("pictishdress2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], [fac_culture_2,fac_culture_2_1] ],

["female_2_celt", "Dress", [("pictishdress3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], [fac_culture_2,fac_culture_2_1] ],

["female_3_celt", "Dress", [("pictishdress1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], [fac_culture_2,fac_culture_2_1] ],

["female_4_celt", "Dress", [("pictishdressverde",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], [fac_culture_2,fac_culture_2_1] ],

["peasant_dress", "Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], ],

#briton dresses
["female_1_barb", "Dress", [("briton_dress_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], ],

["female_2_barb", "Dress", [("briton_dress_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], ],

["female_3_barb", "Dress", [("briton_dress_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], ],

["female_4_barb", "Dress", [("briton_dress_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]),], ],
#end briton dresses

#eastern dresses
["green_dress", "Eastern Noble Dress", [("green_dress",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms_sarmatian"),]), ], [fac_culture_2,fac_culture_2_1] ],

["khergit_lady_dress", "Eastern Noble Dress", [("khergit_lady_dress",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms_sarmatian"),]), ], [fac_culture_3]],

["khergit_lady_dress_b", "Eastern Noble Dress", [("khergit_lady_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_arms_sarmatian"),]), ], [fac_culture_3]],

["sarranid_lady_dress", "Eastern Noble Dress", [("sarranid_lady_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], [fac_culture_5, fac_culture_6,fac_culture_8]],

["sarranid_lady_dress_b", "Eastern Noble Dress", [("sarranid_lady_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
rich_dress_b_armor_price,rich_dress_b_armor,imodbits_none,
 [(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], [fac_culture_5, fac_culture_6,fac_culture_8]],

#eastern commoner dresses
["sarranid_common_dress", "Eastern Dress", [("sarranid_common_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], [fac_culture_5, fac_culture_6,fac_culture_8]],

["sarranid_common_dress_b", "Eastern Dress", [("sarranid_common_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
dress_armor_price,dress_armor,imodbits_none,
[(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], [fac_culture_5, fac_culture_6,fac_culture_8]],

#more generic eastern armoury
["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
robe_armor_price,robe_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),] ],

["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
robe_armor_price,robe_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),] ],

["sarranid_cloth_robe_c", "Worn Robe", [("sar_robe_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
robe_armor_price,robe_armor_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),] ],

["sarranid_cloth_robe_fancy_1", "Noble Robe", [("easterncoat4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8]  ],

["sarranid_cloth_robe_fancy_2", "Noble Robe", [("easterncoat1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8]  ],

["sarranid_cloth_robe_fancy_3", "Noble Robe", [("easterncoat2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
toga_a_noble_armor_price, toga_a_noble_armor,imodbits_none,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8]  ],

["skirmisher_armor", "Eastern Leather Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["archers_vest", "Eastern Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["archers_vest_2", "Eastern Padded Vest", [("arabian_robe_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["sarranid_leather_armor", "Eastern Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_medium_armor_2_price,pants_medium_armor_2_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["sarranid_cavalry_robe", "Eastern Mail Armor", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
pants_linothorax_price,pants_linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

###GREEK SHIT, use fac_minor_kingdoms_end for greek culture
["linothorax_greek1", "Greek Linothorax", [("a_linothorax_v3",0)], itp_type_body_armor  |itp_covers_legs ,0,
linothorax_armor_price,linothorax_armor,imodbits_armor,
 [(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_minor_kingdoms_end] ],
["linothorax_greek2", "Greek Linothorax", [("a_linothorax_v2",0)], itp_type_body_armor  |itp_covers_legs ,0,
linothorax_armor_price,linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_minor_kingdoms_end]  ],
["linothorax_greek3", "Greek Linothorax", [("a_linothorax",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,
linothorax_armor_price,linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_minor_kingdoms_end]  ],
["linothorax_greek4", "Greek Linothorax", [("a_parmenion",0)], itp_type_body_armor  |itp_covers_legs ,0,
linothorax_armor_price,linothorax_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_roman_slinger"),]),], [fac_minor_kingdoms_end]  ],
##END GREEK SHIT

["rawhide_coat", "Fur Armor", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
bandit_armor_price,bandit_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[] ],

["pelt_coat", "Fur armor", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
bandit_armor_price,bandit_armor,imodbits_cloth,[(ti_on_init_item,[(call_script, "script_init_eastern_troop"),]),],[] ],

["mail_shirt", "Heavy Armor", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_iron_armor_price,breastplate_iron_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),], [fac_culture_7,fac_culture_5,fac_culture_6,fac_culture_8] ],

["mail_hauberk", "Heavy Armor", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_iron_armor_price,breastplate_iron_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),] ),], [fac_culture_7,fac_culture_5,fac_culture_6,fac_culture_8]],

["haubergeon", "Heavy Armor", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_iron_armor_price,breastplate_iron_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),] ),], [fac_culture_7,fac_culture_5,fac_culture_6,fac_culture_8] ],

["lamellar_armor", "Scale Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
roman_scale_armor_price,roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),],),],[fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8]  ],

["khergit_elite_armor", "Scale Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
roman_scale_armor_price,roman_scale_armor,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),],),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
roman_scale_armor_price,roman_scale_armor,imodbits_armor,[
(ti_on_init_item,[(call_script, "script_init_eastern_troop"),],)
],[fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8,fac_culture_9] ],

["banded_armor", "Leather Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_leather_armor_price,breastplate_leather_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["banded_armor_2", "Leather Armor", [("banded_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_leather_armor_price,breastplate_leather_armor,imodbits_cloth,
 [(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["banded_armor_3", "Leather Armor", [("banded_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
breastplate_leather_armor_price,breastplate_leather_armor,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
################## END OF ARMOURS
##################################################################################################################################################################

##################################################################################################################################################################
################## BEGIN OF HELMETS
["phrygian_cap", "Phrygian Cap", [("parthian_phyrian",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_yellow", "Yellow Phrygian Cap", [("parthian_phyrian_yello",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_white", "White Phrygian Cap", [("parthian_phyrian_white",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_red", "Red Phrygian Cap", [("parthian_phyrian_red",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_black", "Black Phrygian Cap", [("parthian_phyrian_black",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_green", "Green Phrygian Cap", [("parthian_phyrian_green",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_7,fac_culture_6,fac_culture_5]],
["phrygian_cap_blue", "Blue Phrygian Cap", [("parthian_phyrian_blue",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth,[],[fac_culture_7,fac_culture_6,fac_culture_5]],

#alan
["alan_light_helm", "Alan Helm", [("alan_light_helm",0)], itp_merchandise| itp_type_head_armor ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_3] ],
["alan_helm_1", "Alan Lamellar Helm", [("alan_lamellar_1",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3] ],
["alan_helm_2", "Alan Lamellar Helm", [("alan_lamellar_2",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3] ],
["alan_helm_3", "Alan Lamellar Helm", [("alan_lamellar_3",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3] ],
["alan_helm_4", "Alan Lamellar Helm", [("alan_lamellar_4",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3] ],

#sarmatian
["saka_cap_1", "White Saka Cap", [("saka_cap_1",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],
["saka_hat_1", "White Saka Hat", [("saka_hat_1",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],
["saka_cap_2", "Blue Saka Cap", [("saka_cap_2",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],
["saka_hat_2", "Blue Saka Hat", [("saka_hat_2",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],
["saka_cap_3", "Red Saka Cap", [("saka_cap_3",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],
["saka_hat_3", "Red Saka Hat", [("saka_hat_3",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_dahae]],

["saka_helmet_1", "Red Saka Helmet", [("saka_helmet_1",0)],itp_merchandise|itp_type_head_armor,0,
medium_head_price,medium_head,imodbits_cloth, [],[fac_dahae]],
["saka_helmet_2", "Blue Saka Helmet", [("saka_helmet_2",0)],itp_merchandise|itp_type_head_armor,0,
medium_head_price,medium_head,imodbits_cloth, [],[fac_dahae]],
["saka_helmet_3", "Yellow Saka Helmet", [("saka_helmet_3",0)],itp_merchandise|itp_type_head_armor,0,
medium_head_price,medium_head,imodbits_cloth, [],[fac_dahae]],

["sarmatian_cap_1", "Sarmatian Cap", [("sarmatian_cap_1",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_3,fac_culture_9,fac_culture_5]],
["sarmatian_cap_2", "Sarmatian Cap", [("sarmatian_cap_2",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_3,fac_culture_9,fac_culture_5]],
["sarmatian_cap_3", "Sarmatian Cap", [("sarmatian_cap_3",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [],[fac_culture_3,fac_culture_9,fac_culture_5]],
["sarmatian_cap_4", "Sarmatian Cap", [("sarmatian_cap_4",0)],itp_merchandise|itp_type_head_armor,0,
phrygian_head_price,phrygian_head,imodbits_cloth,[],[fac_culture_3,fac_culture_9,fac_culture_5]],
["sarmatian_heavy_helm1", "Sarmatian Noble Helm", [("bospor_heavy_helm",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm2", "Sarmatian Noble Helm", [("bospor_heavy_helm1",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm3", "Sarmatian Noble Helm", [("bospor_heavy_helm2",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm4", "Sarmatian Noble Helm", [("bospor_heavy_helm3",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm5", "Sarmatian Noble Helm", [("bospor_noble_helm",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm6", "Sarmatian Noble Helm", [("bospor_noble_helm1",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm7", "Sarmatian Noble Helm", [("bospor_noble_helm2",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],
["sarmatian_heavy_helm8", "Sarmatian Noble Helm", [("bospor_noble_helm3",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_3,fac_culture_9,fac_culture_5] ],

#bosporan
["bosporan_spangenhelm_1", "Sarmatian Spangenhelm", [("bosporan_spangenhelm_cheek",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_spangenhelm_2", "Sarmatian Spangenhelm", [("bosporan_spangenhelm_aven",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_spangenhelm_3", "Sarmatian Spangenhelm", [("bosporan_spangenhelm__aventail_3",0)], itp_merchandise| itp_type_head_armor ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_spangenhelm_4", "Sarmatian Spangenhelm", [("bosporan_spangenhelm__aventail_2",0)], itp_merchandise| itp_type_head_armor ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_pointed_helm", "Sarmatian Pointed Helm", [("bosporan_pointed_helm",0),], itp_merchandise|itp_type_head_armor,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_pointed_helm_2", "Sarmatian Pointed Helm", [("bosporan_pointed_helm_2",0),], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_pointed_helm_3", "Sarmatian Pointed Helm", [("bosporan_pointed_helm2",0),], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["bosporan_pointed_helm_4", "Sarmatian Pointed Helm", [("bosporan_pointed_helm3",0),], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],

["kopfband", "Bandana", [("sarmat_bandeau",0)], itp_merchandise| itp_type_head_armor|itp_doesnt_cover_hair ,0,
light_super_head_price,light_super_head,imodbits_plate, [], [fac_culture_3] ],
["african_feather_band", "Bandana with Feathers", [("african_feather_band",0)], itp_type_head_armor|itp_doesnt_cover_hair ,0,
light_super_head_price,light_super_head,imodbits_plate, [], [] ],
["numidian_helm", "Nubian Earings", [("nubian_helmet",0)], itp_unique|itp_type_head_armor|itp_civilian,0,
100, weight(0.1)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], []  ],
["numidian_wig", "Nubian Wig", [("wig_nubian_bl",0)], itp_type_head_armor|itp_civilian|itp_covers_beard,0,
100, weight(0.2)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], []  ],

#dacian
["dacian_pileus_a_1", "Dacian Cap", [("dacian_pileus_a_1",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_pileus_a_2", "Dacian Cap", [("dacian_pileus_a_2",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_pileus_c_1", "Dacian Cap", [("dacian_pileus_c_1",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_pileus_c_2", "Dacian Cap", [("dacian_pileus_c_2",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_pileus_b_1", "Dacian Cap", [("dacian_pileus_b_1",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_pileus_b_2", "Dacian Cap", [("dacian_pileus_b_2",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["dacian_heavy_helm1", "Dacian Helm", [("dac_helm",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm2", "Dacian Helm", [("dac_helm1",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm3", "Dacian Helm", [("dac_helm3",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm4", "Dacian Noble Helm", [("dac_helm4",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm5", "Dacian Helm", [("dac_noble_helm",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm_noble_1", "Dacian Noble Helm", [("dac_helm_noble",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm_noble_2", "Dacian Noble Helm", [("dac_noble_helm1",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm7", "Dacian Helm", [("dac_noble_helm2",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm8", "Dacian Helm with Plume", [("dac_noble_helm3",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm9", "Dacian Helm with Plume", [("dac_noble_helm4",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm10", "Dacian Helm with Plume", [("dac_noble_helm5",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm11", "Dacian Helm", [("dac_noble_helm6",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm12", "Dacian Helm", [("dac_noble_helm7",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm13", "Dacian Helm", [("dac_noble_helm8",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],
["dacian_heavy_helm14", "Dacian Helm", [("dac_noble_helm9",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_1] ],

#germanic
["germanic_cap_1", "Germanic Cap", [("germanic_cap_1",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_4]],
["germanic_cap_2", "Germanic Cap", [("germanic_cap_2",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1]],
["germanic_cap_3", "Germanic Cap", [("germanic_cap_3",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1]],
["germanic_cap_4", "Germanic Cap", [("germanic_cap_4",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_1] ],
["germanic_helm_noble", "Germanic Noble Helmet", [("german_helm_noble",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair|itp_fit_to_head|itp_attach_armature,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_4] ],
["germanic_helm1", "Germanic Helmet", [("german_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair|itp_fit_to_head|itp_attach_armature,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_4] ],
["germanic_helm2", "Old Roman Helmet", [("german_helm1",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_4] ],
["germanic_helm3", "Old Roman Helmet", [("german_helm4",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_4] ],
["germanic_helm4", "Old Roman Helmet", [("germanic_helm_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_4] ],
["wolf_skin_1", "Wolfskin", [("wolf_skin_1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
fur_head_price,fur_head,imodbits_armor, [], [] ],
["wolf_skin_2", "Wolfskin", [("wolf_skin_2",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
fur_head_price,fur_head,imodbits_armor, [], [] ],
["bear_skin_1", "Bearskin", [("bear_skin_1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
fur_head_price,fur_head,imodbits_armor, [], [] ],
["bear_skin_2", "Bearskin", [("bear_skin_2",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
fur_head_price,fur_head,imodbits_armor, [], [] ],

#GREEK SHIT, use fac_minor_kingdoms_end for greek culture
["mak_helm_1", "Phrygian Helm", [("h3_mak2",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["mak_helm_2", "Phrygian Helm", [("h3_mak2b1",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["mak_helm_3", "Phrygian Helm", [("h3_mak2c",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["mak_helm_4", "Phrygian Helm", [("h3_mak2d",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["boeotian_cheeks", "Boetian Helm", [("h_boeotian_cheeks",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
legio_head_price,legio_head,imodbits_plate,[], [fac_minor_kingdoms_end] ],
["boeotian_1", "Boetian Helm", [("h_boiotian",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
aux_head_price,aux_head,imodbits_plate,[], [fac_minor_kingdoms_end] ],
["boeotian_2", "Boetian Helm", [("h_boiotian_plume",0)], itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0,
aux_head_price,aux_head ,imodbits_plate,[], [fac_minor_kingdoms_end] ],
#GREEK SHIT END
#Illyrian shit
["illyrian_hevy_helmet_plume2", "Ancient Illyrian Helmet", [("h_illyrian_t2_v2_2",0)], itp_type_head_armor   ,0,
light_head_price,light_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["illyrian_hevy_helmet_plume1", "Ancient Illyrian Helmet", [("h_illyrian_t2_v2_1",0)], itp_type_head_armor   ,0,
light_head_price,light_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["illyrian_hevy_helmet", "Ancient Illyrian Helmet", [("h_illyrian_t2_v2",0)], itp_type_head_armor   ,0,
light_head_price,light_head,imodbits_plate, [], [fac_minor_kingdoms_end] ],
["illyrian_leader_cap", "Illyrian Padded Coif", [("illyrian_helm",0)], itp_type_head_armor, 0,
light_head_price,light_head,imodbits_cloth ],
#end illyrian shit

#indian
["indian_turban_1", "Indian Turban", [("indian_turban",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6] ],
["indian_turban_2", "Indian Turban", [("indian_turban_green",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6] ],
["indian_turban_3", "Indian Turban", [("indian_turban_red",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6] ],
["indian_turban_4", "Indian Turban", [("turban_gray",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6] ],
["indian_turban_5", "Indian Turban", [("turban_orange",0)],itp_merchandise|itp_type_head_armor|itp_covers_hair,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6] ],

#celtic
["britton_helm1", "Britton Helm", [("celtic_helm_port",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm2", "Britton Helm", [("celtic_helm_conical",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm3", "Britton Helm", [("celtic_helm_conical_2",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm4", "Britton Helm", [("celtic_helm_montefortino_iron",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm5", "Britton Helm", [("celtic_helm_montefortino_brass",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm1_plume", "Britton Helm with Plume", [("celtic_helm_port_plume_black",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm2_plume", "Britton Helm with Plume", [("celtic_helm_with_plume_conical",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm3_plume", "Britton Helm with Plume", [("celtic_helm_with_plume_conical_2",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm4_plume", "Britton Helm with Plume", [("celtic_helm_with_plume_montefortino_iron",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm5_plume", "Britton Helm with Plume", [("celtic_helm_with_plume_montefortino_brass",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm6", "Britton Helm", [("brit_mayrick_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_coolus", "Britton Old Helm", [("british_coolus",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_coolus_2", "Britton Old Helm with Plume", [("british_coolus_plume",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_coolus_new", "Britton Helm", [("british_coolus_2",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_coolus_new_2", "Britton Helm with Plume", [("british_coolus_2_plume",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_coolus_plume", "Britton Helm", [("brit_coolus_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm_noble", "Britton Noble Helm", [("brit_waterloo_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],
["britton_helm_noble_2", "Britton Noble Helm", [("celtic_helm_boar_feather_white",0)], itp_merchandise| itp_type_head_armor|itp_covers_hair ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_2,fac_culture_2_1]  ],

#parthian
["cataphract_helm1", "Cataphract Helm", [("parf_havy_helm",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["cataphract_helm2", "Cataphract Helm", [("parf_havy_helm10",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["cataphract_helm4", "Cataphract Helm", [("parf_havy_helm4",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["cataphract_helm6", "Cataphract Helm", [("parf_havy_helm8",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["cataphract_helm7", "Cataphract Helm", [("parf_havy_helm9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["sarranid_veiled_helmet", "Cataphract Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
cataphract_head_price,cataphract_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["cataphract_sallet_1", "Parthian Sallet", [("parthian_sallet_1",0),("parthian_sallet_1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["cataphract_sallet_2", "Parthian Sallet", [("parthian_sallet_2",0),("parthian_sallet_2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_pointed_helm", "Parthian Pointed Helm", [("parthian_helm_1",0)], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_9,fac_culture_3] ],
["parthian_helm_inf_heavy_1", "Parthian Hellenistic Helm", [("parthian_helmet_1",0),("parthian_helmet_1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_inf_heavy_2", "Parthian Hellenistic Helm", [("parthian_helmet_2",0),("parthian_helmet_2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_inf_heavy_3", "Parthian Hellenistic Helm", [("parthian_helmet_3",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_inf_heavy_4", "Parthian Hellenistic Helm", [("parthian_helmet_4",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_inf_1", "Parthian Hellenistic Helm", [("parthian_helmet_1_light",0),("parthian_helmet_1_light_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_inf_2", "Parthian Hellenistic Helm", [("parthian_helmet_2_light",0),("parthian_helmet_2_light_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_cavalry_1", "Parthian Phyrgian Helm", [("parthian_kedaris_1",0),], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_cavalry_2", "Parthian Phyrgian Helm", [("parthian_kedaris_3",0),("parthian_kedaris_3_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_cavalry_3", "Parthian Phyrgian Helm", [("parthian_kedaris_4",0),("parthian_kedaris_4_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_cavalry_heavy_1", "Parthian Phyrgian Helm", [("parthian_kedaris_2",0),("parthian_kedaris_2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["parthian_helm_cavalry_heavy_2", "Parthian Phyrgian Helm", [("parthian_kedaris_5",0),("parthian_kedaris_5_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

#armenian
["armenian_helm_legion_1", "Armeno-Roman Helm", [("armenian_coolus_1",0),], itp_merchandise| itp_type_head_armor ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_legion_2", "Armeno-Roman Helm", [("armenian_coolus_2",0),], itp_merchandise| itp_type_head_armor ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_legion_3", "Armeno-Roman Helm with Plume", [("armenian_coolus_3",0),], itp_merchandise| itp_type_head_armor ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_legion_4", "Armeno-Roman Helm with Plume", [("armenian_coolus_4",0),], itp_merchandise| itp_type_head_armor ,0,
legio_head_price,legio_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_heavy_1", "Pointed Helm", [("armenian_helm",0),], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_heavy_2", "Pointed Helm", [("armenian_helm_2",0),], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["armenian_helm_heavy_3", "Pointed Helm", [("armenian_helm_3",0),], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

#arabian/syrian
["pilos_chad", "Syrian Helm", [("chad_pilos",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["pilos_chad_2", "Syrian Helm", [("chad_pilos2",0)], itp_merchandise| itp_type_head_armor ,0,
heavy_head_price,heavy_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

#generic eastern
["sarranid_felt_hat", "Eastern Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_5, fac_culture_6,fac_culture_8] ],
["eastern_helm1", "Eastern Felt Hat", [("ude_helm4",0)], itp_merchandise| itp_type_head_armor ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["eastern_helm2", "Eastern Felt Hat", [("ude_helm5",0)], itp_merchandise| itp_type_head_armor ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["eastern_helm3", "Eastern Felt Hat", [("ude_helm6",0)], itp_merchandise| itp_type_head_armor ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["eastern_helm4", "Eastern Felt Hat", [("ude_helm7",0)], itp_merchandise| itp_type_head_armor ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["eastern_helm5", "Eastern Helm", [("ude_helm8",0)], itp_merchandise| itp_type_head_armor ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],
["eastern_helm6", "Eastern Helm", [("ude_helm9",0)], itp_merchandise| itp_type_head_armor ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

##roman helms
#auxiliar helmets
["roman_townguard_helm", "Galea", [("gallic_helmet_brass_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_1", "Galea Gallorum with plume", [("gallic_a_plume",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_2", "Galea Gallorum", [("coolus_c",0),], itp_merchandise|itp_type_head_armor|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_centurio", "Galea Gallorum Centurio", [("coolus_c_centurio",0),], itp_merchandise|itp_type_head_armor|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],

["roman_aux_helm_3", "Galea Gallorum", [("gallic_a_plume_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_4", "Galea Gallorum with plume", [("gallic_a_plume_3",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_5", "Galea", [("gallic_helmet_iron_4",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_6", "Galea", [("gallic_helmet_iron_1",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_7", "Galea", [("gallic_helmet_iron_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_8", "Galea", [("gallic_helmet_brass_1",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_9", "Galea", [("coolus_helmet_iron_1",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_10", "Galea", [("coolus_helmet_iron_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_11", "Galea", [("coolus_helmet_brass_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
aux_head_price,aux_head,imodbits_plate, [], [fac_culture_7] ],

["aux_archer_syorum_helm", "Galea Syrorum", [("syrian_auxiliary_helmet_1",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["aux_archer_syorum_helm1", "Galea Syrorum", [("syrian_auxiliary_helmet_2",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],

["imp_aux_cav_weiler_brass_c", "Galea", [("imp_aux_cav_weiler_brass_c",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["imp_aux_cav_weiler_brass_b", "Galea", [("imp_aux_cav_weiler_brass_b",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["imp_aux_cav_weiler_brass_a", "Galea", [("imp_aux_cav_weiler_brass_a",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],

["imp_aux_cav_weiler_brass_mask_c", "Galea with Mask", [("imp_aux_cav_weiler_brass_mask_c",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["imp_aux_cav_weiler_brass_mask_b", "Galea with Mask", [("imp_aux_cav_weiler_brass_mask_b",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["imp_aux_cav_weiler_brass_mask_a", "Galea with Mask", [("imp_aux_cav_weiler_brass_mask_a",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],

["1_imp_gallic_b", "Galea", [("1_Imp_Gallic_B",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_a", "Galea", [("1_Imp_Gallic_A",0)],  itp_merchandise|itp_type_head_armor,0,
aux_head_price,aux_head,imodbits_armor, [], [fac_culture_7] ],

["roman_aux_helm_old_1", "Old Gallea", [("coolus_helmet_brass_old_1",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_7] ],
["roman_aux_helm_old_2", "Old Gallea", [("coolus_helmet_brass_old_2",0),], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_7] ],
#auxiliar helms end

#legate helms begin
["roman_legatus_helm", "Cassis with Plume", [("helm_praetorian_cavalry23",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_2", "Cassis with Plume", [("helm_praetorian_cavalry23_2",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_3", "Cassis with Plume", [("new_legatus_helm_6",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_4", "Cassis with Plume", [("new_legatus_helm_7",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_5", "Cassis with Plume", [("new_legatus_helm_8",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],

["roman_legatus_helm_6", "Cassis with Plume", [("helm_praetorian_cavalry23_3",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_7", "Cassis with Plume", [("helm_praetorian_cavalry24",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_8", "Cassis with Plume", [("helm_praetorian_cavalry24_2",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],
["roman_legatus_helm_9", "Cassis with Plume", [("helm_praetorian_cavalry24_3",0)], itp_merchandise|itp_type_head_armor ,0,
legate_head_price,legate_head,imodbits_plate, [], [fac_culture_7] ],

["legatus_legionis_helm", "Cassis with Plume", [("legatus_west_new_helm",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head,imodbits_armor, [], [fac_culture_7] ],
["legatus_legionis_helm_2", "Cassis with Plume", [("legatus_west_new_helm_2",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head,imodbits_armor, [], [fac_culture_7] ],
["legatus_legionis_helm_3", "Cassis with Plume", [("legatus_west_new_helm_3",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head,imodbits_armor, [], [fac_culture_7] ],
["legatus_legionis_helm_4", "Cassis with Plume", [("rome_helm_general",0)],  itp_merchandise|itp_type_head_armor,0,
legate_head_price,legate_head,imodbits_armor, [], [fac_culture_7] ],
["cav_decurio_helm", "Cassis with Plume", [("decurion_cavalry_helm",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head ,imodbits_armor, [], [fac_culture_7] ],
["cav_decurio_helm_2", "Cassis with Plume", [("decurion_cavalry_helm_2",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head ,imodbits_armor, [], [fac_culture_7] ],
["cav_decurio_helm_3", "Cassis with Plume", [("decurion_cavalry_helm_3",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legate_head_price,legate_head ,imodbits_armor, [], [fac_culture_7] ],
#legate helms end

#begin new helms
["1_imp_gallic_c", "Galea", [("1_imp_gallic_c",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_b", "Galea", [("1_imp_gallic_f_b",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_n", "Galea", [("1_imp_gallic_f_n",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_s", "Galea", [("1_imp_gallic_f_s",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_h", "Galea", [("1_imp_gallic_h",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_g", "Galea", [("1_imp_gallic_g",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_plume", "Galea with Plume", [("1_imp_gallic_i_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_ac_plume", "Galea with Plume", [("1_imp_gallic_i_ac_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_b_feather", "Galea with Feathers", [("1_imp_gallic_f_b_feather",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i", "Galea", [("1_imp_gallic_i",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_feather", "Galea with Feathers", [("1_imp_gallic_i_feather",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_ac_feather", "Galea with Feathers", [("1_imp_gallic_i_ac_feather",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_ac", "Galea", [("1_imp_gallic_i_ac",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_itallic_c", "Galea", [("1_imp_itallic_c",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_itallic_d", "Galea", [("1_imp_itallic_d",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_itallic_g", "Galea", [("1_imp_itallic_g",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_h_plume", "Galea with Plume", [("1_imp_gallic_h_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_c_plume", "Galea with Plume", [("1_imp_gallic_c_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_plume", "Galea with Plume", [("1_imp_gallic_f_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_b_feather_plume", "Galea with Plume", [("1_imp_gallic_f_b_feather_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_b_feather_plume_2", "Galea with Plume", [("1_imp_gallic_f_b_feather_plume_2",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_f_b_feather_plume_3", "Galea with Plume", [("1_imp_gallic_f_b_feather_plume_3",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_gallic_i_ac_feather_plume", "Galea with Plume", [("1_imp_gallic_i_ac_feather_plume",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_itallic_d_mask", "Galea with Mask", [("1_imp_itallic_d_mask",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["1_imp_itallic_g_mask", "Galea with Mask", [("1_imp_itallic_g_mask",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],

#centurio and praetorian helmets
["praetorian_helm_2", "Galea with Plume", [("praetorian_helm_2",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_helm_1", "Galea with Plume", [("praetorian_helm_1",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_helm_mask_1", "Galea with Plume", [("praetorian_helm_mask_1",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["auxilia_cent_helmet_3", "Galea with Plume", [("auxilia_cent_helmet_3",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["auxilia_cent_helmet_2", "Galea with Plume", [("auxilia_cent_helmet_2",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["auxilia_cent_helmet_1", "Galea with Plume", [("auxilia_cent_helmet_1",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["centurio_helm_3", "Galea with Plume", [("centurio_helm_3",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["centurio_helm_2", "Galea with Plume", [("centurio_helm_2",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["centurio_helm_1", "Galea with Plume", [("centurio_helm_1",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_cent_helmet4", "Galea with Plume", [("praetorian_cent_helmet4",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_cent_helmet3", "Galea with Plume", [("praetorian_cent_helmet3",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_cent_helmet2", "Galea with Plume", [("praetorian_cent_helmet2",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["praetorian_cent_helmet", "Galea with Plume", [("praetorian_cent_helmet",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],

["pretorian_archer_helm", "Galea", [("pretorian_archer_helm",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["pretorian_cavalry_helm_1", "Galea", [("pretorian_cavalry_helm_1",0)],  itp_merchandise|itp_type_head_armor,0,
legio_head_price,legio_head,imodbits_armor, [], [fac_culture_7] ],
["pretorian_cavalry_helm_2", "Galea with Mask", [("pretorian_cavalry_helm_2",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["pretorian_cavalry_helm_3", "Galea with Mask", [("pretorian_cavalry_helm_3",0)],  itp_merchandise|itp_type_head_armor,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],
["auxiliary_cavalry_vecsilary_pretorian_helm", "Galea with Leopardskin", [("auxiliary_cavalry_vecsilary_pretorian_helm",0)],  itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
centurio_head_price,centurio_head,imodbits_armor, [], [fac_culture_7] ],

#signifer etc helmets
["signifer_helm_2", "Galea with Wolfskin", [("signifer_helm_2",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
["signifer_helm_1", "Galea with Wolfskin", [("signifer_helm_1",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
["aquilifer_helmet", "Galea with Lionskin", [("aquilifer_helmet",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
["aquilifer_helmet_mask", "Galea with Lionskin", [("aquilifer_helmet_mask",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
["vexilarius_helmet", "Galea with Bearskin", [("vexilarius_helmet",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
["vexilarius_helmet_mask", "Galea with Bearskin", [("vexilarius_helmet_mask",0)],  itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
signifer_head_price,signifer_head,imodbits_armor, [], [fac_culture_7] ],
###END new helms

#mediterranean straw hats
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
light_super_head_price,light_super_head,imodbits_cloth],
["mediterranean_straw_hat", "Straw Hat", [("mediterranean_straw_hat",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
light_super_head_price,light_super_head,imodbits_cloth],
["mediterranean_straw_hat_1", "Straw Hat", [("mediterranean_straw_hat_1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
light_super_head_price,light_super_head,imodbits_cloth],
["mediterranean_straw_hat_2", "Straw Hat", [("mediterranean_straw_hat_2",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
light_super_head_price,light_super_head,imodbits_cloth],

#eastern head cloth
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["head_wrappings","Head Wrapping",[("head_wrapping_nc",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["perisan_headcloth_1","Persian Head Wrapping",[("perisan_headcloth_1",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick,[],[fac_culture_6]],
["perisan_headcloth_2","Persian Head Wrapping",[("perisan_headcloth_2",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick,[],[fac_culture_6]],
["perisan_headcloth_3","Persian Head Wrapping",[("perisan_headcloth_3",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick,[],[fac_culture_6]],
["perisan_headcloth_4","Persian Head Wrapping",[("perisan_headcloth_4",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick,[],[fac_culture_6]],

##hoods
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
phrygian_head_price,phrygian_head,imodbits_cloth],
["simple_hood_1", "Hood", [("hood_simple",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["simple_hood_2", "Hood", [("hood_simple_2",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["simple_hood_3", "Hood", [("hood_simple_3",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["simple_hood_4", "Hood", [("hood_simple_4",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["black_hood", "Black Hood", [("hood_black_nc",0)], itp_type_head_armor|itp_merchandise|itp_civilian,0,
light_super_head_price, light_super_head,imodbits_cloth ],

##cloaks
["cloak", "Cloak", [("cloak_1",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["cloak_2", "Cloak", [("cloak_simple_1",0),("cloak_simple_1_inv", ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["cloak_3", "Cloak", [("cloak_simple_2",0),("cloak_simple_2_inv", ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["cloak_4", "Cloak", [("cloak_simple_3",0),("cloak_simple_3_inv", ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["cloak_5", "Cloak", [("cloak_simple_4",0),("cloak_simple_4_inv", ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],

#crap helms
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
phrygian_head_price,phrygian_head,imodbits_cloth ],
["nomad_cap", "Fur Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
phrygian_head_price,phrygian_head,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
phrygian_head_price,phrygian_head,imodbits_cloth ],
["footman_helmet", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0,
light_head_price,light_head,imodbits_plate ],

#eastern/desert
["turban", "Desert Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["turban_2", "Desert Turban", [("tuareg_open_green",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["desert_turban_2", "Desert Turban", [("tuareg_blue",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_1_green", "Desert Turban", [("tuareg_new_1_green",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_1_blue", "Desert Turban", [("tuareg_new_1_blue",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_1_red", "Desert Turban", [("tuareg_new_1_red",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_1_white", "Desert Turban", [("tuareg_new_1_white",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_2_green", "Desert Turban", [("tuareg_new_2_green",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_2_blue", "Desert Turban", [("tuareg_new_2_blue",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_2_red", "Desert Turban", [("tuareg_new_2_red",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["tuareg_new_2_white", "Desert Turban", [("tuareg_new_2_white",0)], itp_merchandise| itp_type_head_armor   ,0,
phrygian_head_price,phrygian_head,imodbits_cloth, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

["desert_padded_hat_a", "Padded Cap", [("padded_hat_a",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["sarranid_warrior_cap", "Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["sarranid_helmet1", "Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
light_head_price,light_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],
["sarranid_mail_coif", "Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0,
medium_head_price,medium_head,imodbits_plate, [], [fac_culture_7, fac_culture_5, fac_culture_6,fac_culture_8] ],

#female headclothing start
["flower_crown", "Flower crown", [("flower_crown",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,],
["khergit_lady_hat", "Sarmatian Lady Hat", [("khergit_lady_hat",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],
["khergit_lady_hat_b", "Sarmatian Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian|itp_doesnt_cover_hair,0,
light_super_head_price,light_super_head,imodbits_cloth ],

["new_sarranid_head_cloth", "Veil", [("new_tulbent",0)],  itp_merchandise|itp_type_head_armor |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],
["new_sarranid_head_cloth_2", "Veil", [("new_tulbent_2",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],
["new_sarranid_head_cloth_3", "Veil", [("new_tulbent_3",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],

["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_merchandise|itp_type_head_armor |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],
["sarranid_head_cloth_c", "Lady Head Cloth", [("tulbent_blue",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],
["sarranid_head_cloth_d", "Lady Head Cloth", [("tulbent_red",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[
(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])],[]],

["roman_noble_shawl_1", "Roman Shal", [("roman_noble_shawl_1",0)],  itp_merchandise|itp_type_head_armor|itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])], [fac_culture_7]],
["roman_noble_shawl_2", "Roman Shal", [("roman_noble_shawl_2",0)],  itp_merchandise|itp_type_head_armor|itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])], [fac_culture_7]],
["roman_noble_shawl_3", "Roman Shal", [("roman_noble_shawl_3",0)],  itp_merchandise|itp_type_head_armor|itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])], [fac_culture_7]],
["roman_noble_shawl_4", "Roman Shal", [("roman_noble_shawl_4",0)],  itp_merchandise|itp_type_head_armor|itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])], [fac_culture_7]],
["roman_noble_shawl_5", "Roman Shal", [("roman_noble_shawl_5",0)],  itp_merchandise|itp_type_head_armor|itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,[(ti_on_init_item, [
(store_random_in_range, ":hair", "str_hair_1", "str_hair_end"),
(cur_item_add_mesh, ":hair"),
])], [fac_culture_7]],

["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_fit_to_head,0,
light_super_head_price,light_super_head,imodbits_cloth,],
###################### female headclothing end
######################################################################################################################################################################################################

######################################################################################################################################################################################################
###################### boots

["celtic_boots",  "Simple Boots", [("boots",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(6),weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
get_footwear_price(20), weight(1.15)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],

["sarmatian_shoes", "Sarmatian Boots", [("sarmatian_shoes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
get_footwear_price(20), weight(1.15)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth, [], [fac_culture_5,fac_culture_3] ],

##Roman Civilian
["female_caligea_gold",  "Golden Caliga", [("caligea_civil_gold",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
get_footwear_price(200), weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_none, [], [fac_culture_7] ],

["caligea",  "Civilian Caliga", [("caligea_civil",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(12), weight(0.5)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

["calceus",  "Calceus", [("caligea_boots",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(12), weight(0.5)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["calceus_2",  "Fancy Calceus", [("caligea_expensive_white",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(14), weight(0.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["calceus_3",  "Fancy Calceus", [("caligea_expensive_red",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(14), weight(0.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["calceus_4",  "Fancy Calceus", [("caligea_expensive_yellow",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,
get_footwear_price(14), weight(0.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

##Roman military
["legio_armored_caligea_2", "Decorated Caliga with Ocrea", [("caligea_legatus_new",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(32), weight(1.5)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],
["legio_armored_caligea_2_winter", "Decorated Caliga with Ocrea (winter)", [("caligea_legatus_new_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(32), weight(1.7)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],

["legio_armored_caligea", "Caliga with Ocrea", [("armored_graves_1",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(30), weight(1.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["legio_armored_caligea_winter", "Caliga with Ocrea (winter)", [("armored_graves_1_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(30), weight(1.7)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

["centurio_west_graves", "Caliga with Ocrea", [("centurio_east_graves",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(31), weight(1.5)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],
["centurio_west_graves_winter", "Caliga with Ocrea (winter)", [("centurio_east_graves_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(31), weight(1.7)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],

["centurio_east_graves", "Caliga with Ocrea", [("centurion_south_graves",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(31), weight(1.5)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["centurio_east_graves_winter", "Caliga with Ocrea (winter)", [("centurion_south_graves_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(31), weight(1.7)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

["centurio_praetorian_graves", "Decorated Caliga with Ocrea", [("praetorian_centurion_graves",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(32), weight(1.5)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["centurio_praetorian_graves_winter", "Decorated Caliga with Ocrea (winter)", [("praetorian_centurion_graves_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(32), weight(1.7)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

["aux_centurio_graves", "Caliga with Ocrea", [("hispan_option_graves",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(30), weight(1.5)|abundance(65)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],
["aux_centurio_graves_winter", "Caliga with Ocrea (winter)", [("hispan_option_graves_winter",0)], itp_type_foot_armor | itp_attach_armature,0,
get_footwear_price(30), weight(1.7)|abundance(65)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],

["graves_simple", "Military Caliga", [("caligea_civil_military",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
get_footwear_price(16), weight(0.6)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],
["graves_simple_winter", "Military Caliga (winter)", [("graves_simple_winter",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
get_footwear_price(16), weight(0.7)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7] ],

["graves_simple_2", "Military Calceus", [("caligea_expensive",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
get_footwear_price(16), weight(0.6)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],
["graves_simple_2_winter", "Military Calceus (winter)", [("graves_simple_2_winter",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
get_footwear_price(16), weight(0.7)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_culture_7]  ],

###Eastern show
["eastern_shoe", "Eastern Shoes", [("eastern_shoe_brown",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
get_footwear_price(12), weight(0.5)|abundance(85)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [],[fac_culture_3,fac_culture_5, fac_culture_6,fac_culture_8,fac_culture_7] ],
["eastern_shoe_b", "Eastern Shoes", [("eastern_shoe_blue",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
get_footwear_price(14), weight(0.5)|abundance(85)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_3,fac_culture_5, fac_culture_6,fac_culture_8,fac_culture_7] ],
["eastern_shoe_r", "Eastern Shoes", [("eastern_shoe_red",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
get_footwear_price(14), weight(0.5)|abundance(85)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_3,fac_culture_5, fac_culture_6,fac_culture_8,fac_culture_7] ],
["eastern_shoe_y", "Eastern Shoes", [("eastern_shoe_yellow",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
get_footwear_price(14), weight(0.5)|abundance(85)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_culture_3,fac_culture_5, fac_culture_6,fac_culture_8,fac_culture_7] ],
#cataphract shoes
["cataphract_boots", "Eastern Cataphract Boots", [("cataphract",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,
get_footwear_price(41), weight(5.5)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(41)|difficulty(0) ,imodbits_armor, [], [fac_culture_5, fac_culture_6,fac_culture_8] ],

################################################################################################################################################################################
# BOOTS END AND ARMOR END
################################################################################################################################################################################

################################################################################################################################################################################
# WEAPONS BEGIN
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
get_w_price(62, get_mace_weight(62), get_1hmace_speed(62), 13, 0),
weight(get_mace_weight(62))|difficulty(6)|spd_rtng(get_1hmace_speed(62))|weapon_length(62)|swing_damage(13,blunt)|thrust_damage(0,pierce),imodbits_none ],

# TOOLS
["hammer","Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
get_w_price(40, get_mace_weight(40), get_1hmace_speed(40), 24, 0),
weight(get_mace_weight(40))|difficulty(7)|spd_rtng(get_1hmace_speed(40))|weapon_length(40)|swing_damage(24,blunt)|thrust_damage(0,pierce),imodbits_mace ],
#roman hammer
["roman_hammer",  "Hammer", [("roman_hammer_45",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar,
get_w_price(45, get_mace_weight(45), get_1hmace_speed(45), 24, 0),
weight(get_mace_weight(45))|difficulty(8)|spd_rtng(105) | weapon_length(45)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_culture_7,fac_culture_8,fac_culture_9]  ],
#Roman hatchet
["roman_work_axe", "Hatchet", [("roman_work_axe_55",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 get_w_price(55, get_mace_weight(55), get_1hmace_speed(55), 24, 0),
 weight(get_axe_weight(55))|difficulty(2)|spd_rtng(92) | weapon_length(55)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_7,fac_culture_8,fac_culture_9] ],

["hand_axe",         "Hand Axe", [("hatchet_swup",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(48,get_axe_weight(48),get_1haxe_speed(48),27,10),
weight(get_axe_weight(48))|difficulty(5)|spd_rtng(get_1haxe_speed(48)) | weapon_length(48)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sickle",         "Sickle", [("sickle_swup",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry|itp_wooden_parry, itc_cleaver,
get_w_price(47,get_w_weight(47),get_1hw_speed(47),22,0),
weight(get_w_weight(47))|difficulty(4)|spd_rtng(get_1hw_speed(47)) | weapon_length(47)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_swup",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
get_w_price(46,get_w_weight(46),get_1hw_speed(46),15,10),
weight(get_w_weight(46))|difficulty(3)|spd_rtng(get_1hw_speed(46)) | weapon_length(46)|swing_damage(15 , cut) | thrust_damage(10 ,  pierce),imodbits_sword ],
["knife_2",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
get_w_price(46,get_w_weight(46),get_1hw_speed(46),15,10),
weight(get_w_weight(46))|difficulty(3)|spd_rtng(get_1hw_speed(46)) | weapon_length(46)|swing_damage(15 , cut) | thrust_damage(10 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),10,15),
weight(get_w_weight(60))|difficulty(5)|spd_rtng(get_1hw_speed(60)) | weapon_length(60)|swing_damage(17 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
["butchering_knife_2", "Butchering Knife", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
get_w_price(35,get_w_weight(35),get_1hw_speed(35),24,0),
weight(get_w_weight(35))|difficulty(5)|spd_rtng(get_1hw_speed(35)) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_sword],


##two handed hammers
["maul",         "Great Hammer", [("maul_b",0)], itp_no_blur|itp_crush_through|itp_bonus_against_shield|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi,
  120 , weight(10)|difficulty(11)|spd_rtng(87) | weapon_length(69)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Great Hammer", [("maul_c",0)], itp_no_blur|itp_crush_through|itp_bonus_against_shield|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi,
  180 , weight(11)|difficulty(12)|spd_rtng(86) | weapon_length(69)|swing_damage(41, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_no_blur|itp_crush_through|itp_bonus_against_shield|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi,
  320 , weight(12)|difficulty(14)|spd_rtng(83) | weapon_length(68)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# TOOLS END

# GENERIC AXES
["fighting_axe", "Fighting Axe", [("fighting_ax_new",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(76,get_axe_weight(76),get_1haxe_speed(76),29,10),
weight(get_axe_weight(76))|difficulty(9)|spd_rtng(get_1haxe_speed(76)) | weapon_length(76)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("tveirhendr_danox",0)], itp_no_blur|itp_extra_penetration|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
get_w_price(92,get_axe_weight(92),get_2haxe_speed(92),36,10),
weight(get_axe_weight(92))|abundance(60)|difficulty(13)|spd_rtng(get_2haxe_speed(92)) | weapon_length(92)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],
["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(71,get_axe_weight(71),get_1haxe_speed(71),27,10),
weight(get_axe_weight(71))|abundance(60)|difficulty(9)|spd_rtng(get_1haxe_speed(71))|weapon_length(71)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(73,get_axe_weight(73),get_1haxe_speed(73),28,10),
weight(get_axe_weight(73))|abundance(60)|difficulty(9)|spd_rtng(get_1haxe_speed(73))|weapon_length(73)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],
# END GENERIC AXES

#clubs
["club",         "Club", [("germanic_club_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
get_w_price(60, get_mace_weight(60), get_1hmace_speed(60), 23, 0),
weight(get_mace_weight(60))|difficulty(6)|spd_rtng(get_1hmace_speed(60))|weapon_length(60)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["club_2",         "Club", [("germanic_club_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
get_w_price(70, get_mace_weight(60), get_1hmace_speed(60), 23, 0),
weight(get_mace_weight(60))|difficulty(6)|spd_rtng(get_1hmace_speed(60))|weapon_length(60)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["club_3",         "Club", [("germanic_club_3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
get_w_price(77, get_mace_weight(77), get_1hmace_speed(77), 23, 0),
weight(get_mace_weight(77))|difficulty(6)|spd_rtng(get_1hmace_speed(77))|weapon_length(77)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["spiked_club",         "Spiked Club", [("spiked_club_swup",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 24, 4),
weight(get_mace_weight(70))|difficulty(9)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(24 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 24, 4),
weight( get_mace_weight(70))|difficulty(9)|spd_rtng(get_1hmace_speed(70))|weapon_length(70)|swing_damage(24 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

#maces
["spiked_mace","Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 28, 10),
weight(get_mace_weight(70))|difficulty(10)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mace_2","Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 29, 10),
weight(get_mace_weight(70))|difficulty(10)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3","Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 29, 10),
weight(get_mace_weight(70))|difficulty(10)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_mace_1","Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(73, get_mace_weight(73), get_1hmace_speed(73), 30, 10),
weight(get_mace_weight(73))|difficulty(10)|spd_rtng(get_1hmace_speed(73))|weapon_length(73)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

#pickaxes
["pickaxe",         "Pickaxe", [("rusty_pick_swup",0)], itp_no_blur|itp_extra_penetration|itp_bonus_against_shield|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 27, 10),
weight(get_mace_weight(70))|difficulty(9)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Pickaxe", [("czekan_b",0)], itp_no_blur|itp_extra_penetration|itp_bonus_against_shield|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
get_w_price(70, get_mace_weight(70), get_1hmace_speed(70), 30, 10),
weight(get_mace_weight(70))|difficulty(9)|spd_rtng(get_1hmace_speed(70)) | weapon_length(70)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
#############

############
#weapons

##CELTIC
["celtic_sowrd1", "Celtic Shortsword", [("celtic_sword72",0),("celtic_sword72_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(72, get_w_weight(72), get_1hw_speed(72), 27, 24),
weight(get_w_weight(72))|difficulty(8)|spd_rtng(get_1hw_speed(72))|weapon_length(72)|swing_damage(27 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_sowrd2", "Celtic Sword", [("celtic_sword92",0),("celtic_sword92_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(92, get_w_weight(92), get_1hw_speed(92), 28, 25),
weight(get_w_weight(92))|difficulty(9)|spd_rtng(get_1hw_speed(92))|weapon_length(92)|swing_damage(28 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_sowrd3", "Celtic War Sword", [("celtic_sword97",0),("celtic_sword97_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(97, get_w_weight(97), get_1hw_speed(97), 28, 26),
weight(get_w_weight(97))|difficulty(10)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], [fac_culture_2,fac_culture_2_1] ],
["celtic_spatha", "Celtic Spatha", [("celtic_spatha",0),("celtic_spatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(83, get_w_weight(83), get_1hw_speed(83), 29, 25),
weight(get_w_weight(83))|difficulty(10)|spd_rtng(get_1hw_speed(83)) | weapon_length(83)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_culture_2,fac_culture_2_1] ],

["irish_sword", "Irish Noble Sword", [("irish_sword",0),("irish_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(54, get_w_weight(54), get_1hw_speed(54), 25, 28),
weight(get_w_weight(54))|difficulty(8)|spd_rtng(get_1hw_speed(54)) | weapon_length(54)|swing_damage(25 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high, [], [fac_culture_2] ],

["caledonian_axe1", "Onehanded Caledonian Axe", [("brit_handaxe",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(71,get_axe_weight(71),get_1haxe_speed(71),27,10),
weight(get_axe_weight(71))|difficulty(9)|spd_rtng(get_1haxe_speed(71)) | weapon_length(71)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2_1] ],
["caledonian_axe2", "Onehanded Caledonian Axe", [("brit_hatchet",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(68,get_axe_weight(68),get_1haxe_speed(68),27,10),
weight(get_axe_weight(68))|difficulty(9)|spd_rtng(get_1haxe_speed(68)) | weapon_length(68)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2_1] ],

["celtic_axe1", "Onehanded Celtic Axe", [("picton_2axe69",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(69,get_axe_weight(69),get_1haxe_speed(69),27,10),
weight(get_axe_weight(69))|difficulty(9)|spd_rtng(get_1haxe_speed(69)) | weapon_length(69)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_axe2", "Onehanded Celtic Axe", [("picton_2axe92",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(57,get_axe_weight(57),get_1haxe_speed(57),29,10),
weight(get_axe_weight(57))|difficulty(8)|spd_rtng(get_1haxe_speed(57)) | weapon_length(57)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_axe3", "Onehanded Celtic Axe", [("picton_axe52",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(52,get_axe_weight(52),get_1haxe_speed(52),29,10),
weight(get_axe_weight(52))|difficulty(9)|spd_rtng(get_1haxe_speed(52))|weapon_length(52)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_axe4", "Onehanded Celtic Axe", [("picton_axe53",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise| itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(69,get_axe_weight(69),get_1haxe_speed(69),28,10),
weight(get_axe_weight(69))|difficulty(9)|spd_rtng(get_1haxe_speed(69)) | weapon_length(69)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_2,fac_culture_2_1] ],

["gallic_spear_2","Short Celtic Spear", [("gallic_spear_2", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_offset_lance|itp_no_blur, itc_spear,
get_polarm_price(132,get_w_weight(132),get_polew_speed(132),17,30),
weight(get_w_weight(132))|difficulty(7)|abundance(100)|spd_rtng(get_polew_speed(132))|weapon_length(132)|thrust_damage(30, pierce)|swing_damage(30, pierce), imodbits_polearm, [], [fac_culture_2,fac_culture_2_1]],

["gallic_spear_3","Celtic Spear", [("gallic_spear_3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_offset_lance|itp_no_blur, itc_spear,
get_polarm_price(156,get_w_weight(156),get_polew_speed(156),17,30),
weight(get_w_weight(156))|difficulty(9)|abundance(100)|spd_rtng(get_polew_speed(156))|weapon_length(156)|thrust_damage(30, pierce)|swing_damage(30, pierce), imodbits_polearm, [], [fac_culture_2,fac_culture_2_1]],
#END Celtic

##GREEK SHIT, use fac_minor_kingdoms_end for greek culture
["sword_akinakes", "Akinakes", [("sword_akinakes",0)], itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
get_w_price(52, get_w_weight(52), get_1hw_speed(52), 25, 25),
weight(get_w_weight(52))|difficulty(8)|spd_rtng(get_1hw_speed(52))|weapon_length(52)|swing_damage(25,cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_minor_kingdoms_end] ],

["sword_kopis", "Kopis", [("sword_kopis",0)], itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
get_w_price(63, get_w_weight(63), get_1hw_speed(63), 27, 20),
weight(get_w_weight(63))|difficulty(9)|spd_rtng(get_1hw_speed(63)) | weapon_length(63)|swing_damage(27 , cut)|thrust_damage(20 ,  pierce),imodbits_sword_high, [], [fac_minor_kingdoms_end] ],

["sword_laconian_dagger", "Makhaira", [("sword_laconian_dagger",0)], itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
get_w_price(49, get_w_weight(49), get_1hw_speed(49), 28, 21),
weight(get_w_weight(49))|difficulty(8)|spd_rtng(get_1hw_speed(49)) | weapon_length(49)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], [fac_minor_kingdoms_end] ],

["sword_xiphos_greek", "Xiphos", [("sword_xiphos_greek",0)], itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
get_w_price(75, get_w_weight(75), get_1hw_speed(75), 28, 23),
weight(get_w_weight(75))|difficulty(9)|spd_rtng(get_1hw_speed(75)) | weapon_length(75)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_minor_kingdoms_end] ],

["sarissa",         "Sarissa", [("macedoniansarissa",0)], itp_type_polearm|itp_merchandise|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_primary|itp_secondary|itp_no_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_pike,
get_polarm_price(400,get_w_weight(400),get_polew_speed(315),18,27),
weight(get_w_weight(400))|difficulty(14)|spd_rtng(get_polew_speed(315)) | weapon_length(400)|swing_damage(25 , pierce) | thrust_damage(25 ,  pierce),imodbits_polearm, [], [fac_minor_kingdoms_end] ],
##END GREEK SHIT

# SEPCIAL
["kopis", "Kopis", [("thracian_sword68",0),("thracian_sword68_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(68,get_w_weight(68),get_1hw_speed(68),30,15),
weight(get_w_weight(68))|difficulty(7)|spd_rtng(get_1hw_speed(68)) | weapon_length(68)|swing_damage(30 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high, [], [fac_culture_1,fac_culture_7,fac_culture_6,fac_culture_8,fac_culture_5] ],

["dreizack1",         "Fork", [("trident135",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff,
get_polarm_price(135,get_w_weight(135),get_polew_speed(135),10,35),
weight(get_w_weight(135))|difficulty(9)|spd_rtng(get_polew_speed(135)) | weapon_length(135)|swing_damage(10, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],

["dreizack2",         "Fork", [("trident165",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff,
get_polarm_price(165,get_w_weight(165),get_polew_speed(165),15,33),
weight(get_w_weight(165))|difficulty(9)|spd_rtng(get_polew_speed(165)) | weapon_length(165)|swing_damage(15, blunt) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],
# END SPECIAL

# PARTHIAN
["dagger_parthian_1",         "Parthian Dagger", [("caucasian_dagger_2_60",0),("caucasian_dagger_2_60_scab",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),10,20),
weight(get_w_weight(60))|difficulty(3)|spd_rtng(get_1hw_speed(60)) | weapon_length(60)|swing_damage(18 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high, [], [fac_culture_5,fac_culture_6] ],
["dagger_parthian_2",         "Parthian Dagger", [("caucasian_dagger_1_42",0),("caucasian_dagger_1_42_scab",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itcf_force_64_bits|itcf_thrust_onehanded|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(42,get_w_weight(42),get_1hw_speed(42),10,20),
weight(get_w_weight(42))|difficulty(3)|spd_rtng(get_1hw_speed(42)) | weapon_length(42)|swing_damage(20 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], [fac_culture_5,fac_culture_6] ],

["parthian_cataphract_axe", "Parthian Axe", [("karianaxe",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(84,get_axe_weight(84),get_1haxe_speed(84),29,10),
weight(get_axe_weight(84))|abundance(50)|difficulty(10)|spd_rtng(get_1haxe_speed(84)) | weapon_length(84)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5,fac_culture_6] ],
# END PARTHIAN

# EASTERN
["eastern_sowrd1", "Eastern Shortsword", [("east_sword68",0),("east_sword68_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(68, get_w_weight(68), get_1hw_speed(68), 21, 26),
weight(get_w_weight(68))|difficulty(9)|spd_rtng(get_1hw_speed(68)) | weapon_length(68)|swing_damage(21 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

["eastern_sowrd2", "Eastern Sword", [("east_sword87",0),("east_sword87_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(87, get_w_weight(87), get_1hw_speed(87), 26, 22),
weight(get_w_weight(87))|difficulty(10)|spd_rtng(get_1hw_speed(87))|weapon_length(87)|swing_damage(26 , cut)|thrust_damage(22 ,  pierce),imodbits_sword_high, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

["eastern_sowrd3", "Eastern Sword", [("east_sword87_1",0),("east_sword87_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(87, get_w_weight(87), get_1hw_speed(87), 26, 22),
weight(get_w_weight(87))|difficulty(10)|spd_rtng(get_1hw_speed(87))|weapon_length(87)|swing_damage(26 , cut)|thrust_damage(22 ,  pierce),imodbits_sword_high, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

["eastern_sowrd4", "Eastern War Sword", [("east_sword95_1",0),("east_sword95_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(95, get_w_weight(95), get_1hw_speed(95), 28, 19),
weight(get_w_weight(95))|difficulty(10)|spd_rtng(get_1hw_speed(95)) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

["eastern_sowrd5", "Eastern War Sword", [("east_sword95_2",0),("east_sword95_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(95, get_w_weight(95), get_1hw_speed(95), 28, 19),
weight(get_w_weight(95))|difficulty(10)|spd_rtng(get_1hw_speed(95)) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_culture_6,fac_culture_8, fac_culture_5] ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(200,get_w_weight(200),get_polew_speed(200),16,28),
weight(get_w_weight(200))|difficulty(10)|spd_rtng(get_polew_speed(200)) | weapon_length(200)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm, [], [fac_culture_5, fac_culture_6,fac_culture_8]  ],

["eastern_spear_149",         "Eastern Spear", [("eastern_spear_149",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(149,get_w_weight(149),get_polew_speed(149),17,30),
weight(get_w_weight(149))|difficulty(7)|spd_rtng(get_polew_speed(149)) | weapon_length(149)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_5, fac_culture_6,fac_culture_8] ],
["eastern_spear_168",         "Eastern Spear", [("eastern_spear_168",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(168,get_w_weight(168),get_polew_speed(168),17,30),
weight(get_w_weight(127))|difficulty(7)|spd_rtng(get_polew_speed(168)) | weapon_length(168)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_5, fac_culture_6,fac_culture_8] ],
# END EASTERN

#Dacian
["dacian_noble_sword", "Dacian Noble Spatha", [("dacian_noble_spatha",0),("dacian_noble_spatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(97, get_w_weight(97), get_1hw_speed(97), 29, 20),
weight(get_w_weight(97))|difficulty(10)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["dacian_ring_sword", "Dacian Ringsword", [("dacian_long_sword",0),("dacian_long_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(97, get_w_weight(97), get_1hw_speed(97), 27, 15),
weight(get_w_weight(97))|difficulty(10)|spd_rtng(get_1hw_speed(97)) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax_onehanded1", "Onehanded Falx", [("falx58_one",0)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_cleaver|itc_parry_onehanded,
get_w_price(58, get_w_weight(58), get_1hw_speed(58), 28, 10),
weight(get_w_weight(58))|difficulty(9)|spd_rtng(get_1hw_speed(58))|weapon_length(58)|swing_damage(28 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax_onehanded2", "Onehanded Falx", [("falx60_one",0)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_cleaver|itc_parry_onehanded,
get_w_price(60, get_w_weight(60), get_1hw_speed(60), 28, 10),
weight(get_w_weight(60))|difficulty(9)|spd_rtng(get_1hw_speed(60)) | weapon_length(60)|swing_damage(28 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1]  ],

["flax1",         "Falx", [("falx105",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(105, get_axe_weight(105), get_2hw_speed(105), 35, 18),
weight(get_axe_weight(105))|difficulty(20)|spd_rtng(get_2hw_speed(105))|weapon_length(105)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax2",         "Falx", [("falx109",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(109, get_axe_weight(109), get_2hw_speed(109), 35, 18),
weight(get_axe_weight(109))|difficulty(20)|spd_rtng(get_2hw_speed(109)) | weapon_length(109)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax3",         "Falx", [("falx110",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(110, get_axe_weight(110), get_2hw_speed(110), 35, 18),
weight(get_axe_weight(110))|difficulty(20)|spd_rtng(get_2hw_speed(110))|weapon_length(110)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax4",         "Falx", [("falx74",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(74, get_axe_weight(74), get_2hw_speed(74), 34, 18),
weight(get_axe_weight(74))|difficulty(20)|spd_rtng(get_2hw_speed(74))|weapon_length(74)|swing_damage(34 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax5",         "Falx", [("falx75",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(75, get_axe_weight(75), get_2hw_speed(75), 34, 18),
weight(get_axe_weight(75))|difficulty(20)|spd_rtng(get_2hw_speed(75)) | weapon_length(75)|swing_damage(34 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["flax6",         "Falx", [("falx85",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi,
get_w_price(85, get_axe_weight(85), get_2hw_speed(85), 34, 18),
weight(get_axe_weight(85))|difficulty(20)|spd_rtng(get_2hw_speed(85)) | weapon_length(85)|swing_damage(34 , cut) | thrust_damage(10 ,  pierce),imodbits_sword_high, [], [fac_culture_1] ],

["dacian_sword", "Kopis", [("thracian_sword75",0),("thracian_sword75_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(75,get_w_weight(75),get_1hw_speed(75),29,16),
weight(get_w_weight(75))|difficulty(8)|spd_rtng(get_1hw_speed(75)) | weapon_length(75)|swing_damage(29 , cut) | thrust_damage(16 ,  pierce),imodbits_sword_high, [], [fac_culture_1,fac_culture_7,fac_culture_6,fac_culture_8,fac_culture_5] ],

["dacian_short_spear",         "Dacian Spear", [("dacian_short_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(127,get_w_weight(127),get_polew_speed(127),17,30),
weight(get_w_weight(127))|difficulty(7)|spd_rtng(get_polew_speed(127)) | weapon_length(127)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_1] ],
["dacian_medium_spear",         "Dacian Spear", [("dacian_medium_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(135,get_w_weight(135),get_polew_speed(135),17,30),
weight(get_w_weight(127))|difficulty(7)|spd_rtng(get_polew_speed(135)) | weapon_length(135)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_1] ],
#End dacian

#Germanic
["cheruski_sword",  "Germanic Shortsword", [("ancient_germanic_sword",0),("ancient_germanic_sword_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(77, get_w_weight(77), get_1hw_speed(77), 27, 13),
weight(get_w_weight(77))|difficulty(9)|spd_rtng(get_1hw_speed(77))|weapon_length(77)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_culture_4] ],

["cheruski_ax",         "Germanic Axe", [("axe_c",0),("axe_c_carry",ixmesh_carry),], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(60, get_axe_weight(60), get_1haxe_speed(60), 28, 10),
weight(get_axe_weight(60))|difficulty(9)|spd_rtng(get_1haxe_speed(60))|weapon_length(60)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4] ],

["germanic_axe1", "Germanic Axe", [("einhendi_vendelox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(50,get_axe_weight(50),get_1haxe_speed(50),28,10),
weight(get_axe_weight(50))|difficulty(7)|spd_rtng(get_1haxe_speed(50)) | weapon_length(50)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4] ],

["germanic_axe2", "Germanic Axe", [("einhendi_hedmarkrox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(52,get_axe_weight(52),get_1haxe_speed(52),29,10),
weight(get_axe_weight(52))|difficulty(7)|spd_rtng(get_1haxe_speed(52))|weapon_length(52)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4] ],

["germanic_axe3", "Germanic Axe", [("einhendi_haloygox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(66,get_axe_weight(66),get_1haxe_speed(66),30,10),
weight(get_axe_weight(66))|difficulty(8)|spd_rtng(get_1haxe_speed(66))|weapon_length(66)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4] ],

["battle_axe","Battle Axe", [("tveirhendr_hedmarkox",0)], itp_no_blur|itp_extra_penetration|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
get_w_price(93,get_axe_weight(93),get_2haxe_speed(93),36,10),
weight(get_axe_weight(93))|abundance(60)|difficulty(13)|spd_rtng(get_2haxe_speed(93)) | weapon_length(93)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],

["one_handed_war_axe_b", "One Handed War Axe", [("hoggox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(48,get_axe_weight(48),get_1haxe_speed(48),28,10),
weight(get_axe_weight(48))|abundance(60)|difficulty(9)|spd_rtng(get_1haxe_speed(48))|weapon_length(48)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],

["one_handed_battle_axe_b", "One Handed Battle Axe", [("einhendi_danox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(67,get_axe_weight(67),get_1haxe_speed(67),29,10),
weight(get_axe_weight(67))|abundance(60)|difficulty(9)|spd_rtng(get_1haxe_speed(67)) | weapon_length(67)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4]  ],

["one_handed_battle_axe_c", "One Handed Battle Axe", [("einhendi_breithofudox",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(71,get_axe_weight(71),get_1haxe_speed(71),29,10),
weight(get_axe_weight(71))|abundance(60)|difficulty(9)|spd_rtng(get_1haxe_speed(71)) | weapon_length(71)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_4] ],

["danish_longsword", "Rich Germanic Longsword", [("danish_longsword",0),("danish_longsword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_cleaver|itc_parry_onehanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(85, get_w_weight(85), get_1hw_speed(85), 30, 20),
weight(get_w_weight(85))|abundance(10)|difficulty(10)|spd_rtng(get_1hw_speed(85))|weapon_length(85)|swing_damage(30 , cut)|thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_culture_4] ],

["sword_viking_1", "Germanic Spatha", [("germanic_spatha_1",0),("germanic_spatha_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(83,get_w_weight(83),get_1hw_speed(83),28,20),
weight(get_w_weight(83))|abundance(60)|difficulty(10)|spd_rtng(get_1hw_speed(83)) | weapon_length(83)|swing_damage(27 , cut) | thrust_damage(12 ,  pierce),imodbits_sword_high, [], [fac_culture_4] ],

["sword_viking_2", "Germanic Spatha", [("germanic_spatha_2",0),("germanic_spatha_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(83,get_w_weight(83),get_1hw_speed(83),28,20),
weight(get_w_weight(83))|abundance(60)|difficulty(10)|spd_rtng(get_1hw_speed(83)) | weapon_length(83)|swing_damage(27 , cut) | thrust_damage(12 ,  pierce),imodbits_sword_high, [], [fac_culture_4] ],

["sword_viking_3", "Germanic Spatha", [("roman_spatha_common_1",0),("roman_spatha_common_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(83,get_w_weight(83),get_1hw_speed(83),28,20),
weight(get_w_weight(83))|abundance(60)|difficulty(10)|spd_rtng(get_1hw_speed(83)) | weapon_length(83)|swing_damage(27 , cut) | thrust_damage(12 ,  pierce),imodbits_sword_high, [], [fac_culture_4] ],

["sword_viking_4", "Germanic Spatha", [("rich_spatha",0),("rich_spatha_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
30000,weight(get_w_weight(93))|difficulty(9)|spd_rtng(get_1hw_speed(93))|weapon_length(93)|swing_damage(28,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [] ],

["sax1", "Germanic Shortsword", [("ancient_germanic_sword_2",0),("ancient_germanic_sword_scab_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(76,get_w_weight(76),get_1hw_speed(76),28,15),
weight(get_w_weight(76))|difficulty(4)|abundance(100)|spd_rtng(get_1hw_speed(76)) | weapon_length(76)|swing_damage(28 , cut) | thrust_damage(15 ,  pierce),imodbits_sword,[], [fac_culture_4] ],

["germanic_war_spear",         "Germanic Spear", [("spjot",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(71,get_w_weight(119),get_polew_speed(119),18,29),
weight(get_w_weight(119))|difficulty(8)|spd_rtng(get_polew_speed(119))|weapon_length(119)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_4] ],
["germanic_war_spear_2", "Germanic Spear", [("langr_bryntvari",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(170,get_w_weight(170),get_polew_speed(170),15,29),
weight(get_w_weight(170))|difficulty(9)|spd_rtng(get_polew_speed(170)) | weapon_length(170)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_4] ],
["germanic_war_spear_3", "Germanic Spear", [("spjotkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(170,get_w_weight(170),get_polew_speed(170),15,30),
weight(get_w_weight(170))|difficulty(9)|spd_rtng(get_polew_speed(170)) | weapon_length(170)|swing_damage(30, pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_4] ],

["germanic_shortened_spear",         "Germanic Shortened Spear", [("krokaspjott2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(126,get_w_weight(126),get_polew_speed(126),16,28),
weight(get_w_weight(126))|difficulty(7)|spd_rtng(get_polew_speed(126)) | weapon_length(126)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm,[],[fac_culture_4] ],
#End Germanic

#Nubian
["nubian_axe", "Nubian Axe", [("nubian_axe",0)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_no_blur, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(68,get_axe_weight(68),get_1haxe_speed(68),28,10),
weight(get_axe_weight(68))|abundance(50)|difficulty(10)|spd_rtng(get_1haxe_speed(68)) | weapon_length(68)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5] ],
["nubian_axe_2", "Nubian Axe", [("nubian_axe_2",0)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_no_blur, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(55,get_axe_weight(55),get_1haxe_speed(55),28,10),
weight(get_axe_weight(55))|abundance(50)|difficulty(10)|spd_rtng(get_1haxe_speed(55)) | weapon_length(55)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5] ],

["numidian_spear_2",         "Numidian War Spear", [("numidian_spear_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(167,get_w_weight(167),get_polew_speed(167),17,30),
weight(get_w_weight(167))|difficulty(7)|spd_rtng(get_polew_speed(167)) | weapon_length(167)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["numidian_spear_1",         "Numidian Spear", [("numidian_spear_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(142,get_w_weight(142),get_polew_speed(142),17,28),
weight(get_w_weight(142))|difficulty(7)|spd_rtng(get_polew_speed(142)) | weapon_length(142)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],
#End nubian

#Caucasian
["kartil_axe_1", "Kartilian Axe", [("kartil_axe_1",0)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_no_blur, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(67,get_axe_weight(67),get_1haxe_speed(67),29,10),
weight(get_axe_weight(67))|abundance(50)|difficulty(10)|spd_rtng(get_1haxe_speed(67)) | weapon_length(67)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_culture_5] ],

["caucasian_axe_1", "Caucasian Axe", [("caucasian_axe_1",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(56,get_axe_weight(56),get_1haxe_speed(56),28,10),
weight(get_axe_weight(56))|difficulty(7)|spd_rtng(get_1haxe_speed(56)) | weapon_length(56)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,[],[fac_culture_5] ],

["armenian_axe_1", "Armenian Axe", [("armenian_axe_1",0)], itp_no_blur|itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
get_w_price(59,get_axe_weight(59),get_1haxe_speed(59),29,10),
weight(get_axe_weight(59))|difficulty(7)|spd_rtng(get_1haxe_speed(59)) | weapon_length(59)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe,[],[fac_culture_5] ],

["armenian_sword_1", "Armenian Ringsword", [("armenian_sword_1",0),("armenian_sword_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(76,get_w_weight(76),get_1hw_speed(76),28,22),
weight(get_w_weight(76))|abundance(60)|difficulty(8)|spd_rtng(get_1hw_speed(76)) | weapon_length(76)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], [fac_culture_5] ],

["caucasian_short_sword", "Caucasian Ringsword", [("caucasian_short_sword",0),("caucasian_short_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),29,20),
weight(get_w_weight(60))|abundance(60)|difficulty(8)|spd_rtng(get_1hw_speed(60)) | weapon_length(60)|swing_damage(29 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], [fac_culture_5] ],

["caucasian_longsword", "Caucasian Longsword", [("caucasian_longsword",0),("caucasian_longsword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(75,get_w_weight(75),get_1hw_speed(75),28,23),
weight(get_w_weight(75))|abundance(75)|difficulty(9)|spd_rtng(get_1hw_speed(75)) | weapon_length(75)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_culture_5] ],

["armenian_war_spear",         "Armenian War Spear", [("armenian_war_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(160,get_w_weight(160),get_polew_speed(160),17,29),
weight(get_w_weight(160))|difficulty(7)|spd_rtng(get_polew_speed(160)) | weapon_length(160)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_5] ],

["caucasian_spear_174",         "Caucasian Spear", [("caucasian_spear_174",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(174,get_w_weight(174),get_polew_speed(174),17,29),
weight(get_w_weight(174))|difficulty(7)|spd_rtng(get_polew_speed(174)) | weapon_length(174)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_5] ],

["caucasian_spear_145",         "Caucasian Spear", [("caucasian_spear_145",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(145,get_w_weight(145),get_polew_speed(145),17,28),
weight(get_w_weight(145))|difficulty(7)|spd_rtng(get_polew_speed(145)) | weapon_length(145)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm, [], [fac_culture_5] ],
#End Caucasian

# ROMAN
["dagger",         "Puggio", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_no_parry, itcf_force_64_bits|itcf_thrust_onehanded|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(37,get_w_weight(37),get_1hw_speed(37),10,20),
weight(get_w_weight(37))|difficulty(3)|spd_rtng(get_1hw_speed(37)) | weapon_length(37)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["roman_spatha", "Spatha", [("roman_cav_sword_95",0),("roman_cav_sword_95_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(95,get_w_weight(95),get_1hw_speed(95),27,13),
weight(get_w_weight(95))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(95))|weapon_length(95)|swing_damage(27,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_spatha_2", "Spatha", [("roman_cav_sword_97",0),("roman_cav_sword_97_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(97,get_w_weight(97),get_1hw_speed(97),27,13),
weight(get_w_weight(97))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(97))|weapon_length(97)|swing_damage(27,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_spatha_3", "Spatha", [("roman_cav_sword_92",0),("roman_cav_sword_92_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(92,get_w_weight(92),get_1hw_speed(92),27,13),
weight(get_w_weight(92))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(92))|weapon_length(92)|swing_damage(27,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_spatha_rich", "Spatha", [("roman_rich_cav_sword_95",0),("roman_rich_cav_sword_95_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(95,get_w_weight(95),get_1hw_speed(95),27,13),
weight(get_w_weight(95))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(95))|weapon_length(95)|swing_damage(28,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_spatha_rich_2", "Spatha", [("roman_rich_cav_sword_97",0),("roman_rich_cav_sword_97_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(97,get_w_weight(97),get_1hw_speed(97),27,13),
weight(get_w_weight(97))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(97))|weapon_length(97)|swing_damage(28,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_spatha_rich_3", "Spatha", [("roman_rich_cav_sword_92",0),("roman_rich_cav_sword_92_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(92,get_w_weight(92),get_1hw_speed(92),27,13),
weight(get_w_weight(92))|difficulty(9)|abundance(70)|spd_rtng(get_1hw_speed(92))|weapon_length(92)|swing_damage(28,cut)|thrust_damage(13,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_gladius", "Gladius", [("roman_gladius_57",0),("roman_gladius_57_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(58,get_w_weight(58),get_1hw_speed(58),19,30),
weight(get_w_weight(58))|difficulty(7)|abundance(70)|spd_rtng(get_1hw_speed(58))|weapon_length(58)|swing_damage(30,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [],
 [fac_culture_7] ],#
["roman_gladius_melee", "Gladius", [("roman_gladius_57",0),("roman_gladius_57_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(58,get_w_weight(58),get_1hw_speed(58),19,30),
weight(get_w_weight(58))|difficulty(7)|spd_rtng(get_1hw_speed(58))|weapon_length(58)|swing_damage(19,cut)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],

###old gladius##############################################################################################################################################################################
["old_gladius_2", "Old Gladius", [("old_gladius_2",0),("old_gladius_2_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(79,get_w_weight(79),get_1hw_speed(79),16,25),
weight(get_w_weight(79))|difficulty(7)|spd_rtng(get_1hw_speed(79))|abundance(85)|weapon_length(79)|swing_damage(25,pierce)|thrust_damage(25,pierce), imodbits_sword_high, [], [fac_culture_7,fac_culture_8] ],#
["old_gladius_2_melee", "Old Gladius", [("old_gladius_2",0),("old_gladius_2_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(79,get_w_weight(79),get_1hw_speed(79),16,25),
weight(get_w_weight(79))|difficulty(7)|spd_rtng(get_1hw_speed(79))|weapon_length(79)|swing_damage(16,cut)|thrust_damage(25,pierce), imodbits_sword_high, [], [fac_culture_7,fac_culture_8] ],

["old_gladius_1", "Old Gladius", [("old_gladius_1",0),("old_gladius_1_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(80,get_w_weight(80),get_1hw_speed(80),23,15),
weight(get_w_weight(80))|difficulty(7)|spd_rtng(get_1hw_speed(80))|abundance(90)|weapon_length(80)|swing_damage(23,cut)|thrust_damage(15,pierce), imodbits_sword_high, [], [fac_culture_7,fac_culture_8] ],
###old gladius END##############################################################################################################################################################################

["roman_gladius_2", "Gladius", [("roman_gladius_58",0),("roman_gladius_58_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(59,get_w_weight(59),get_1hw_speed(59),19,30),
weight(get_w_weight(59))|difficulty(7)|spd_rtng(get_1hw_speed(59))|abundance(70)|weapon_length(59)|swing_damage(30,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],
["roman_gladius_2_melee", "Gladius", [("roman_gladius_58",0),("roman_gladius_58_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(59,get_w_weight(59),get_1hw_speed(59),19,30),
weight(get_w_weight(59))|difficulty(7)|spd_rtng(get_1hw_speed(59))|weapon_length(59)|swing_damage(19,cut)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_gladius_rich_2", "Gladius", [("roman_rich_gladius_58",0),("roman_rich_gladius_58_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(59,get_w_weight(59),get_1hw_speed(59),19,30),
weight(get_w_weight(59))|difficulty(7)|spd_rtng(get_1hw_speed(59))|abundance(70)|weapon_length(59)|swing_damage(30,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],
["roman_gladius_rich_2_melee", "Gladius", [("roman_rich_gladius_58",0),("roman_rich_gladius_58_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(59,get_w_weight(59),get_1hw_speed(59),19,30),
weight(get_w_weight(59))|difficulty(7)|spd_rtng(get_1hw_speed(59))|weapon_length(59)|swing_damage(19,cut)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_gladius_3", "Gladius", [("roman_gladius_59",0),("roman_gladius_59_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),19,30),
weight(get_w_weight(60))|difficulty(7)|spd_rtng(get_1hw_speed(60))|weapon_length(60)|abundance(70)|swing_damage(30,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],
["roman_gladius_3_melee", "Gladius", [("roman_gladius_59",0),("roman_gladius_59_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),19,30),
weight(get_w_weight(60))|difficulty(7)|spd_rtng(get_1hw_speed(60))|weapon_length(60)|swing_damage(19,cut)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["roman_gladius_rich_3", "Gladius", [("roman_rich_gladius_59",0),("roman_rich_gladius_59_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee,
itc_gladius|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),19,30),
weight(get_w_weight(60))|difficulty(7)|spd_rtng(get_1hw_speed(60))|weapon_length(60)|abundance(70)|swing_damage(30,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],
["roman_gladius_rich_3_melee", "Gladius", [("roman_rich_gladius_59",0),("roman_rich_gladius_59_scabbard",ixmesh_carry)], itp_extra_penetration|itp_type_one_handed_wpn|itp_primary,
itc_gladius_2|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
get_w_price(60,get_w_weight(60),get_1hw_speed(60),19,30),
weight(get_w_weight(60))|difficulty(7)|spd_rtng(get_1hw_speed(60))|weapon_length(60)|swing_damage(19,cut)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_culture_7] ],

["hasta1",         "Long Hasta", [("roman_spear_178",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(178,get_w_weight(178),get_polew_speed(178),19,30),
weight(get_w_weight(178))|difficulty(9)|spd_rtng(get_polew_speed(178)) | weapon_length(178)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],

["hasta2",         "Hasta", [("roman_spear_135",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(135,get_w_weight(135),get_polew_speed(135),18,30),
weight(get_w_weight(135))|difficulty(8)|spd_rtng(get_polew_speed(135)) | weapon_length(135)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],

["hasta3",         "Short Hasta", [("roman_spear_117",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(117,get_w_weight(117),get_polew_speed(117),17,29),
weight(get_w_weight(117))|difficulty(7)|spd_rtng(get_polew_speed(117)) | weapon_length(117)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],
# END ROMAN

#palmyrean gladius
["palmyran_gladius", "Palmyrene Gladius", [("palmyran_gladius2",0),("palmyran_gladius_scabbard2",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,
itc_gladius_2|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(68,get_w_weight(68),get_1hw_speed(68),26,19),
weight(get_w_weight(68))|difficulty(7)|spd_rtng(get_1hw_speed(68))|abundance(50)|weapon_length(68)|swing_damage(26,cut)|thrust_damage(19,pierce), imodbits_sword_high, [], [fac_culture_7,fac_culture_8] ],
["palmyran_gladius_rich", "Noble Palmyrene Gladius", [("palmyran_gladius",0),("palmyran_gladius_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,
itc_gladius_2|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(68,get_w_weight(68),get_1hw_speed(68),27,20),
weight(get_w_weight(68))|difficulty(7)|spd_rtng(get_1hw_speed(68))|abundance(50)|weapon_length(68)|swing_damage(27,cut)|thrust_damage(20,pierce), imodbits_sword_high, [], [fac_culture_7,fac_culture_8] ],

##ARABIAN
["arabian_sword_a",         "Eastern Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(100,get_w_weight(100),get_1hw_speed(100),26,19),
weight(get_w_weight(100))|difficulty(9)|spd_rtng(get_1hw_speed(100)) | weapon_length(100)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_6,fac_culture_8] ],

["arabian_sword_b",         "Eastern Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(100,get_w_weight(100),get_1hw_speed(100),27,19),
weight(get_w_weight(100))|difficulty(9)|spd_rtng(get_1hw_speed(100)) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_6,fac_culture_8] ],

["sarranid_cavalry_sword",         "Eastern Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(106,get_w_weight(106),get_1hw_speed(106),28,19),
weight(get_w_weight(106))|difficulty(10)|spd_rtng(get_1hw_speed(106)) | weapon_length(106)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_6,fac_culture_8] ],

["arabian_sword_d",         "Eastern Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(100,get_w_weight(100),get_1hw_speed(100),29,20),
weight(get_w_weight(100))|difficulty(9)|spd_rtng(get_1hw_speed(100)) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_6,fac_culture_8] ],
#END ARABIAN

##ALAN AND NOMADIC
["alan_long_sword",   "Alan Longsword", [("alan_long_sword",0),("alan_long_sword_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(115,get_w_weight(115),get_1hw_speed(115),29,20),
weight(get_w_weight(115))|difficulty(8)|spd_rtng(get_1hw_speed(115)) | weapon_length(115)|swing_damage(29 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high, [],[fac_culture_3] ],

["alan_long_sword_ring",   "Alan Longsword", [("alan_long_sword_ring",0),("alan_long_sword_ring_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(115,get_w_weight(115),get_1hw_speed(115),29,20),
weight(get_w_weight(115))|difficulty(8)|spd_rtng(get_1hw_speed(115)) | weapon_length(115)|swing_damage(29 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high, [],[fac_culture_3] ],

["sarmatian_sword_2",   "Sarmatian Short Ringsword", [("sarmatian_sax",0),("sarmatian_sax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(63,get_w_weight(63),get_1hw_speed(63),26,21),
weight(get_w_weight(63))|difficulty(8)|spd_rtng(get_1hw_speed(63)) | weapon_length(63)|swing_damage(26 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],

["sarmatian_ringsword_1",   "Sarmatian Short Ringsword", [("sarmatian_shortsword_2",0),("sarmatian_shortsword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(62,get_w_weight(62),get_1hw_speed(62),27,17),
weight(get_w_weight(62))|difficulty(8)|spd_rtng(get_1hw_speed(62)) | weapon_length(62)|swing_damage(27 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],
["sarmatian_ringsword_2",   "Sarmatian Long Ringsword", [("sarmatian_shortsword_3",0),("sarmatian_shortsword_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(95,get_w_weight(95),get_1hw_speed(95),27,17),
weight(get_w_weight(95))|difficulty(8)|spd_rtng(get_1hw_speed(95)) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],
["sarmatian_ringsword_3",   "Sarmatian Long Ringsword", [("ringsword_long",0),("ringsword_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(91,get_w_weight(91),get_1hw_speed(91),27,17),
weight(get_w_weight(91))|difficulty(8)|spd_rtng(get_1hw_speed(91)) | weapon_length(91)|swing_damage(27 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],
["sarmatian_ringsword_4",   "Sarmatian Long Ringsword", [("ringsword_short",0),("ringsword_short_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(91,get_w_weight(91),get_1hw_speed(91),28,19),
weight(get_w_weight(91))|difficulty(8)|spd_rtng(get_1hw_speed(91)) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],

["sarmatian_ringsword_rich_1",   "Sarmatian Rich Ringsword", [("sarmatian_ringsword_rich",0),("sarmatian_ringsword_rich_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(98,get_w_weight(98),get_1hw_speed(98),29,19),
weight(get_w_weight(98))|difficulty(8)|spd_rtng(get_1hw_speed(98)) | weapon_length(98)|swing_damage(29 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],

["sarmatian_sword_1",   "Short Sword", [("sarmat_sword66",0),("sarmat_sword66scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
get_w_price(64,get_w_weight(64),get_1hw_speed(64),26,21),
weight(get_w_weight(64))|difficulty(8)|spd_rtng(get_1hw_speed(64)) | weapon_length(64)|swing_damage(26 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [],[fac_culture_5,fac_culture_3] ],

["sarmatian_spear_169",         "Sarmatian Spear", [("sarmatian_spear_169",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(169,get_w_weight(169),get_polew_speed(169),17,30),
weight(get_w_weight(127))|difficulty(7)|spd_rtng(get_polew_speed(169)) | weapon_length(169)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_culture_3] ],
# END NOMADIC

## GENERIC Polearms
["scythe","Scythe", [("scythe_new",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,
get_polarm_price(182,get_w_weight(182),get_polew_speed(182),23,10),
weight(get_w_weight(182))|difficulty(10)|spd_rtng(get_polew_speed(182)) | weapon_length(182)|swing_damage(23 , cut) | thrust_damage(10 ,  pierce),imodbits_polearm ],

["pitch_fork","Pitch Fork", [("pitchfork23",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry|itp_has_upper_stab|itp_no_blur,itc_staff,
get_polarm_price(154,get_w_weight(154),get_polew_speed(154),14,19),
weight(get_w_weight(154))|difficulty(7)|spd_rtng(get_polew_speed(154)) | weapon_length(154)|swing_damage(14 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],

["shepherds_crook",         "Shepherds Crook", [("shepherds_crook",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack|itp_no_blur, itc_staff|itcf_carry_sword_back,
get_polarm_price(134,get_w_weight(134),get_polew_speed(134),19,10),
weight(get_w_weight(134))|difficulty(6)|spd_rtng(get_polew_speed(134)) | weapon_length(128)|swing_damage(19 , blunt)| thrust_damage(10 ,  blunt),imodbits_polearm ],

["staff",         "Staff", [("wooden_staff_swup",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack|itp_no_blur, itc_staff|itcf_carry_sword_back,
get_polarm_price(128,get_w_weight(128),get_polew_speed(128),18,19),
weight(get_w_weight(128))|difficulty(6)|spd_rtng(get_polew_speed(128)) | weapon_length(128)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],

["quarter_staff", "Quarter Staff", [("quarter_staff_swup",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack|itp_no_blur, itc_staff|itcf_carry_sword_back,
get_polarm_price(137,get_w_weight(137),get_polew_speed(137),20,20),
weight(get_w_weight(137))|difficulty(7)|spd_rtng(get_polew_speed(137)) | weapon_length(137)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],

["iron_staff",         "Iron Staff", [("iron_staff_swup",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_no_blur, itc_staff|itcf_carry_sword_back,
get_polarm_price(129,get_w_weight(129),get_polew_speed(129),24,24),
 weight(get_w_weight(129))|difficulty(7)|spd_rtng(get_polew_speed(129)) | weapon_length(129)|swing_damage(24 , blunt) | thrust_damage(24 ,  blunt),imodbits_polearm ],

["boar_spear","Boar Spear", [("german_hunting_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur|itp_is_pike,itc_staff,
get_polarm_price(157,get_w_weight(157),get_polew_speed(157),26,23),
weight(get_w_weight(157))|difficulty(9)|spd_rtng(get_polew_speed(157)) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["old_spear_1",         "Hasta", [("spear_4_133",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(133,get_w_weight(133),get_polew_speed(133),18,29),
weight(get_w_weight(133))|difficulty(8)|spd_rtng(get_polew_speed(133)) | weapon_length(133)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],

["old_spear_2",         "Hasta", [("spear_6_154",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_no_blur, itc_spear,
get_polarm_price(154,get_w_weight(154),get_polew_speed(154),17,29),
weight(get_w_weight(154))|difficulty(7)|spd_rtng(get_polew_speed(154)) | weapon_length(154)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_7] ],

["shortened_spear",         "Shortened Spear", [("svia2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(120,get_w_weight(120),get_polew_speed(120),16,28),
weight(get_w_weight(120))|difficulty(7)|spd_rtng(get_polew_speed(120)) | weapon_length(120)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],

["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(145,get_w_weight(145),get_polew_speed(145),16,29),
weight(get_w_weight(145))|difficulty(9)|spd_rtng(get_polew_speed(145))|weapon_length(145)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm ],

["war_spear",         "War Spear", [("hoggkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(122,get_w_weight(122),get_polew_speed(122),17,30),
weight(get_w_weight(122))|difficulty(7)|spd_rtng(get_polew_speed(122)) | weapon_length(122)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["cavalry_spear",         "Long Spear", [("langr_svia",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(180,get_w_weight(180),get_polew_speed(180),16,30),
weight(get_w_weight(180))|difficulty(10)|spd_rtng(get_polew_speed(180)) | weapon_length(180)|swing_damage(30 , pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["greek_spear_1",         "Spear", [("greek_spear_doru_steel",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(160,get_w_weight(160),get_polew_speed(160),17,29),
weight(get_w_weight(160))|difficulty(9)|spd_rtng(get_polew_speed(160)) | weapon_length(160)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_7, fac_culture_5, fac_culture_6] ],

["greek_spear_2",         "Spear", [("greek_spear_doru_2_steel",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(170,get_w_weight(170),get_polew_speed(170),17,29),
weight(get_w_weight(170))|difficulty(9)|spd_rtng(get_polew_speed(170)) | weapon_length(170)|swing_damage(29 , pierce) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_culture_7, fac_culture_5, fac_culture_6] ],
# END GENERIC POLARMS

## KONTOS
["light_lance",         "Kontos", [("spear_b_2-75m",0)], itp_couchable|itp_two_handed|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(270,get_w_weight(270),get_polew_speed(270),18,28),
weight(get_w_weight(270))|difficulty(9)|spd_rtng(get_polew_speed(270)) | weapon_length(270)|swing_damage(27 , pierce) | thrust_damage(27 ,  pierce),imodbits_polearm ],

["heavy_lance",         "Long Kontos", [("spear_f_2-9m",0)], itp_couchable|itp_two_handed|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(350,get_w_weight(350),get_polew_speed(300),18,29),
weight(get_w_weight(350))|difficulty(10)|spd_rtng(get_polew_speed(300)) | weapon_length(350)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],

["lance",         "Kontos", [("spear_d_2-8m",0)], itp_couchable|itp_two_handed|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry|itp_is_pike|itp_has_upper_stab|itp_no_blur, itc_spear,
get_polarm_price(270,get_w_weight(270),get_polew_speed(270),18,29),
weight(get_w_weight(270))|difficulty(9)|spd_rtng(get_polew_speed(270)) | weapon_length(270)|swing_damage(28 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],
## END KONTOS

# SHIELDS BEGIN, Weapons END
["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 40, 0),
weight(get_shield_weight(shield_armor_t1,40,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(100)|shield_width(40)|abundance(20),imodbits_shield ],

#generic round shields
["ad_mixed_round_shields_01",         "Round Shield", [("ad_mixed_round_shields_01",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [] ],
["ad_mixed_round_shields_02",         "Round Shield", [("ad_mixed_round_shields_02",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [] ],
["ad_mixed_round_shields_03",         "Round Shield", [("ad_mixed_round_shields_03",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 50, 0),
weight(get_shield_weight(shield_armor_t1,50,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(50),imodbits_shield, [], [] ],
["ad_mixed_round_shields_04",         "Round Shield", [("ad_mixed_round_shields_04",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 50, 0),
weight(get_shield_weight(shield_armor_t1,50,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(50),imodbits_shield, [], [] ],
["ad_mixed_round_shields_05",         "Round Shield", [("ad_mixed_round_shields_05",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 48, 0),
weight(get_shield_weight(shield_armor_t1,48,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(48),imodbits_shield, [], [] ],
["ad_mixed_round_shields_06",         "Round Shield", [("ad_mixed_round_shields_06",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 48, 0),
weight(get_shield_weight(shield_armor_t1,48,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(48),imodbits_shield, [], [] ],
["ad_mixed_round_shields_07",         "Round Shield", [("ad_mixed_round_shields_07",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 48, 0),
weight(get_shield_weight(shield_armor_t1,48,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(48),imodbits_shield, [], [] ],
["ad_mixed_round_shields_08",         "Round Shield", [("ad_mixed_round_shields_08",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 47, 0),
weight(get_shield_weight(shield_armor_t1,47,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(47),imodbits_shield, [], [] ],
["ad_mixed_round_shields_13",         "Round Shield", [("ad_mixed_round_shields_13",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 50, 0),
weight(get_shield_weight(shield_armor_t1,50,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(50),imodbits_shield, [], [] ],
["ad_mixed_round_shields_14",         "Round Shield", [("ad_mixed_round_shields_14",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 49, 0),
weight(get_shield_weight(shield_armor_t1,49,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(49),imodbits_shield, [], [] ],
["ad_mixed_round_shields_15",         "Round Shield", [("ad_mixed_round_shields_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 30, 0),
weight(get_shield_weight(shield_armor_t1,30,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(30),imodbits_shield, [], [] ],
["ad_mixed_round_shields_16",         "Round Shield", [("ad_mixed_round_shields_16",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 30, 0),
weight(get_shield_weight(shield_armor_t1,30,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(30),imodbits_shield, [], [] ],


#bosporan shields
["bosphoran_shield_new_1", "Bosporan Thuros", [("bosphoran_shield_new_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 28, 50),
weight(get_shield_weight(shield_armor_t2,28,50))|abundance(100)|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(28)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],
["bosphoran_shield_new_2", "Bosporan Thuros", [("bosphoran_shield_new_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 28, 50),
weight(get_shield_weight(shield_armor_t2,28,50))|abundance(100)|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(28)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],
["bosphoran_shield_new_3", "Bosporan Thuros", [("bosphoran_shield_new_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 28, 50),
weight(get_shield_weight(shield_armor_t2,28,50))|abundance(100)|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(28)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],
["bosphoran_shield_new_4", "Bosporan Thuros", [("bosphoran_shield_new_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 28, 50),
weight(get_shield_weight(shield_armor_t2,28,50))|abundance(100)|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(28)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],

["bosporan_oval_color_1", "Heavy Bosporan Thuros", [("juice_oval_shield_blue",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3, 30, 50),
weight(get_shield_weight(shield_armor_t3,30,50))|abundance(100)|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(30)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],

["bosporan_oval_color_2", "Heavy Bosporan Thuros", [("juice_oval_shield_red",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3, 30, 50),
weight(get_shield_weight(shield_armor_t3,30,50))|abundance(100)|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(30)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9]],

["bosporan_oval_color_3", "Heavy Bosporan Thuros", [("juice_oval_shield_yellow",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3, 30, 50),
weight(get_shield_weight(shield_armor_t3,30,50))|abundance(100)|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(30)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9]],

["bosporan_oval_color_4", "Heavy Bosporan Thuros", [("juice_oval_shield_green",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3, 30, 50),
weight(get_shield_weight(shield_armor_t3,30,50))|abundance(100)|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(30)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],

["bosporan_oval_color_5", "Heavy Bosporan Thuros", [("juice_oval_shield_leather",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3, 30, 50),
weight(get_shield_weight(shield_armor_t3,30,50))|abundance(100)|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(30)|shield_height(50)|abundance(80),imodbits_shield,
[], [fac_culture_9] ],

# caucasian
["caucasian_shield_1", "North Caucasian Wicker Shield", [("caucasian_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 25, 66),
weight(get_shield_weight(shield_armor_t2,25,66))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(25)|shield_height(66),imodbits_shield,
[], [fac_culture_5] ],
["caucasian_shield_2", "North Caucasian Wicker Shield", [("caucasian_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 25, 66),
weight(get_shield_weight(shield_armor_t2,25,66))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(25)|shield_height(66),imodbits_shield,
[], [fac_culture_5] ],


##GREEK SHIT us fac_minor_kingdoms_end for greek culture
["hoplon_1", "Old Hoplon", [("s_hoplon10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3, 75, 0),
weight(get_shield_weight(shield_armor_t3,75,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(75),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["hoplon_2", "Old Hoplon", [("s_hoplon11",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3, 75, 0),
weight(get_shield_weight(shield_armor_t3,75,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(75),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["hoplon_4", "Old Hoplon", [("s_hoplon7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3, 75, 0),
weight(get_shield_weight(shield_armor_t3,75,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(75),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["hoplon_5", "Old Hoplon", [("s_hoplon8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3, 75, 0),
weight(get_shield_weight(shield_armor_t3,75,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(75),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["hoplon_6", "Old Hoplon", [("s_hoplon9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3, 75, 0),
weight(get_shield_weight(shield_armor_t3,75,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(75),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["s_parma_mak_plain_16", "Old Parma", [("s_parma_mak_plain_16",0)], itp_type_shield|itp_wooden_parry, itcf_carry_buckler_left,
get_shield_price(shield_armor_t3, 37, 0),
weight(get_shield_weight(shield_armor_t3,37,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(37),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["s_parma_mak_plain_15", "Old Parma", [("s_parma_mak_plain_15",0)], itp_type_shield|itp_wooden_parry, itcf_carry_buckler_left,
get_shield_price(shield_armor_t3, 37, 0),
weight(get_shield_weight(shield_armor_t3,37,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(37),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["s_parma_mak_plain_14", "Old Parma", [("s_parma_mak_plain_14",0)], itp_type_shield|itp_wooden_parry, itcf_carry_buckler_left,
get_shield_price(shield_armor_t3, 37, 0),
weight(get_shield_weight(shield_armor_t3,37,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(37),imodbits_shield, [], [fac_minor_kingdoms_end] ],

["s_parma_mak_plain_13", "Old Parma", [("s_parma_mak_plain_13",0)], itp_type_shield|itp_wooden_parry, itcf_carry_buckler_left,
get_shield_price(shield_armor_t3, 37, 0),
weight(get_shield_weight(shield_armor_t3,37,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(37),imodbits_shield, [], [fac_minor_kingdoms_end] ],
##END GREEK SHIT

# north african shields
["african_shield_1",         "African Shield", [("african_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 83),
weight(get_shield_weight(shield_armor_t2,40,83))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(83),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["african_shield_2",         "African Shield", [("african_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 38, 91),
weight(get_shield_weight(shield_armor_t2,38,91))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(38)|shield_height(91),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["african_shield_3",         "African Shield", [("african_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 85),
weight(get_shield_weight(shield_armor_t2,40,85))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(85),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["african_round_shield",         "African Round Shield", [("african_round_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 49, 0),
weight(get_shield_weight(shield_armor_t1,49,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(49),imodbits_shield, [], [] ],

#nubian
["nubian_kite_shield_1",         "Nubian Heater Shield", [("nubian_kite_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 90),
weight(get_shield_weight(shield_armor_t2,40,90))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(92)|shield_width(30)|shield_height(40)|abundance(10),imodbits_shield, [],
[]  ],
["nubian_kite_shield_2",         "Nubian Heater Shield", [("nubian_kite_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 90),
weight(get_shield_weight(shield_armor_t2,40,90))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(92)|shield_width(30)|shield_height(40)|abundance(10),imodbits_shield, [],
[]  ],
["nubian_kite_shield_3",         "Nubian Heater Shield", [("nubian_kite_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 90),
weight(get_shield_weight(shield_armor_t2,40,90))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(92)|shield_width(30)|shield_height(40)|abundance(10),imodbits_shield, [],
[]  ],
["nubian_kite_shield_4",         "Nubian Heater Shield", [("nubian_kite_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 90),
weight(get_shield_weight(shield_armor_t2,40,90))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(92)|shield_width(30)|shield_height(40)|abundance(10),imodbits_shield, [],
[]  ],
["nubian_kite_shield_5",         "Nubian Heater Shield", [("nubian_kite_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 90),
weight(get_shield_weight(shield_armor_t2,40,90))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(92)|shield_width(30)|shield_height(40)|abundance(10),imodbits_shield, [],
[]  ],

# eastern shields
["eastern_shield_inf_light1",         "Light Eastern Shield", [("eovalspineless1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 83),
weight(get_shield_weight(shield_armor_t2,40,83))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(83)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["eastern_shield_inf_light2",         "Light Eastern Shield", [("eovalspineless2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 83),
weight(get_shield_weight(shield_armor_t2,40,83))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(83)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["eastern_shield_inf_light3",         "Light Eastern Shield", [("eovalspineless3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 83),
weight(get_shield_weight(shield_armor_t2,40,83))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(83)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["eastern_shield_inf_light4",         "Light Eastern Shield", [("eovalspineless4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t2, 40, 83),
weight(get_shield_weight(shield_armor_t2,40,83))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(40)|shield_height(83)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["heavy_wicker_1",         "Eastern Shield", [("heavy_wicker_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 130),
weight(get_shield_weight(shield_armor_t3,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["heavy_wicker_2",         "Eastern Shield", [("heavy_wicker_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 130),
weight(get_shield_weight(shield_armor_t3,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(70),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light5",         "Eastern Shield", [("wicker1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light6",         "Eastern Shield", [("wicker2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light7",         "Eastern Shield", [("wicker3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light8",         "Eastern Shield", [("wicker4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light9",         "Eastern Shield", [("wicker5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_light10",         "Eastern Shield", [("wicker6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2, 55, 130),
weight(get_shield_weight(shield_armor_t2,55,130))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t2)|spd_rtng(90)|shield_width(55)|shield_height(130)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy1",         "Eastern Shield", [("efoval1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy2",         "Eastern Shield", [("efoval2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy3",         "Eastern Shield", [("efoval3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy4",         "Eastern Shield", [("efoval4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy5",         "Eastern Shield", [("efoval5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy6",         "Eastern Shield", [("efoval6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy7",         "Eastern Shield", [("efoval7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy8",         "Eastern Shield", [("efoval8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy9",         "Eastern Shield", [("efoval9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy10",         "Eastern Shield", [("efovala",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy11",         "Eastern Shield", [("efovalb",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

["eastern_shield_inf_heavy12",         "Eastern Shield", [("efovalc",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

# EASTERN CAVALRY
["scythian_shield_cav1",         "Light Shield", [("alx1scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

["scythian_shield_cav2",         "Light Shield", [("alx2scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

["scythian_shield_cav3",         "Light Shield", [("alx3scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

["scythian_shield_cav4",         "Light Shield", [("alx4scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

["scythian_shield_cav5",         "Light Shield", [("alx5scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

["scythian_shield_cav6",         "Light Shield", [("alx6scythshield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(70),imodbits_shield, [], [fac_culture_5,fac_culture_6] ],

# indian shields
["indian_shield_1",         "Eastern Shield", [("indian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 40, 90),
weight(get_shield_weight(shield_armor_t3,40,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(92)|shield_width(40)|shield_height(90)|abundance(10),imodbits_shield, [],
[fac_culture_6]  ],
["indian_shield_2",         "Eastern Shield", [("indian_shield_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 40, 90),
weight(get_shield_weight(shield_armor_t3,40,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(92)|shield_width(40)|shield_height(90)|abundance(10),imodbits_shield, [],
[fac_culture_6]  ],
["indian_shield_3",         "Eastern Shield", [("indian_shield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 40, 90),
weight(get_shield_weight(shield_armor_t3,40,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(92)|shield_width(40)|shield_height(90)|abundance(10),imodbits_shield, [],
[fac_culture_6]  ],
["indian_shield_4",         "Eastern Shield", [("indian_shield_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 40, 90),
weight(get_shield_weight(shield_armor_t3,40,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(92)|shield_width(40)|shield_height(90)|abundance(10),imodbits_shield, [],
[fac_culture_6]  ],
["indian_shield_5",         "Eastern Shield", [("indian_shield_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 40, 90),
weight(get_shield_weight(shield_armor_t3,40,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(92)|shield_width(40)|shield_height(90)|abundance(10),imodbits_shield, [],
[fac_culture_6]  ],

# celtic shields
["pict_square_shield_1","Celtic Shield", [("pict_shield_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
300, weight(2.5)|abundance(100)|body_armor(12)|hit_points(300)|spd_rtng(85)|shield_width(30)|shield_height(50), imodbits_shield, [], [fac_culture_2,fac_culture_2_1]],
["pict_square_shield_2","Celtic Shield", [("pict_shield_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
300, weight(2.5)|abundance(100)|body_armor(12)|hit_points(300)|spd_rtng(85)|shield_width(30)|shield_height(50), imodbits_shield, [], [fac_culture_2,fac_culture_2_1]],
["pict_square_shield_3","Celtic Shield", [("pict_shield_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
300, weight(2.5)|abundance(100)|body_armor(12)|hit_points(300)|spd_rtng(85)|shield_width(30)|shield_height(50), imodbits_shield, [], [fac_culture_2,fac_culture_2_1]],
["pict_square_shield_4","Celtic Shield", [("pict_shield_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
300, weight(2.5)|abundance(100)|body_armor(12)|hit_points(300)|spd_rtng(85)|shield_width(30)|shield_height(50), imodbits_shield, [], [fac_culture_2,fac_culture_2_1]],
["pict_square_shield_5","Celtic Shield", [("pict_shield_5", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
300, weight(2.5)|abundance(100)|body_armor(12)|hit_points(300)|spd_rtng(85)|shield_width(30)|shield_height(50), imodbits_shield, [], [fac_culture_2,fac_culture_2_1]],

["caledonian_h_shield1", "Caledonian H Shield", [("vae_h_shield1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_culture_2_1]],
["caledonian_h_shield2", "Caledonian H Shield", [("vae_h_shield2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_culture_2_1]],
["caledonian_h_shield3", "Caledonian H Shield", [("vae_h_shield3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_culture_2_1]],
["caledonian_h_shield4", "Caledonian H Shield", [("vae_h_shield4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_culture_2_1]],
["caledonian_h_shield5", "Caledonian H Shield", [("vae_h_shield5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  345 , weight(3)|hit_points(300)|body_armor(4)|spd_rtng(75)|shield_width(50)|difficulty(1),imodbits_shield,
[], [fac_culture_2_1]],

["celtic_long_shild1",         "Long Celtic Shield", [("long_celtic_shield2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 43, 99),
weight(get_shield_weight(shield_armor_t3,41,99))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(41)|shield_height(99)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_long_shild2",         "Long Celtic Shield", [("long_celtic_shield3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 41, 99),
weight(get_shield_weight(shield_armor_t3,41,99))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(41)|shield_height(99)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_long_shild3",         "Long Celtic Shield", [("long_celtic_shield4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 41, 99),
weight(get_shield_weight(shield_armor_t3,41,99))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(41)|shield_height(99)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_round_shild1",         "Celtic Round Shield", [("ad_mixed_round_shields_09",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 55, 0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_round_shild2",         "Celtic Round Shield", [("ad_mixed_round_shields_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 55, 0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_round_shild3",         "Celtic Round Shield", [("ad_mixed_round_shields_11",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 55, 0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_round_shild4",         "Celtic Round Shield", [("ad_mixed_round_shields_12",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 55, 0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(55)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_weird_shield_1",  "Celtic Shield", [("celtic_weird_shield_1", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_2",  "Celtic Shield", [("celtic_weird_shield_2", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_3",  "Celtic Shield", [("celtic_weird_shield_3", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_4",  "Celtic Shield", [("celtic_weird_shield_4", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_5",  "Celtic Shield", [("celtic_weird_shield_5", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],

["celtic_weird_shield_6",  "Celtic Shield", [("celtic_shield_1", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_7",  "Celtic Shield", [("celtic_shield_2", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_8",  "Celtic Shield", [("celtic_shield_3", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_9",  "Celtic Shield", [("celtic_shield_4", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],
["celtic_weird_shield_10",  "Celtic Shield", [("celtic_shield_5", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t2,38,58))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield, [], [fac_culture_2,fac_culture_2_1]  ],

["celtic_shield_large1",         "Celtic Shield", [("celtic_hex_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large2",         "Celtic Shield", [("celtic_hex_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large3",         "Celtic Shield", [("celtic_hex_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large4",         "Celtic Shield", [("celtic_hex_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large5",         "Celtic Shield", [("celtic_hex_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large6",         "Celtic Shield", [("celtic_hex_shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large7",         "Celtic Shield", [("e1ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large8",         "Celtic Shield", [("e2ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large9",         "Celtic Shield", [("e3ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large10",         "Celtic Shield", [("e4ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large11",         "Celtic Shield", [("e5ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["celtic_shield_large12",         "Celtic Shield", [("e6ovalscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(80),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

["irish_shield_1",         "Irish Shield", [("ad_pict_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(80)|abundance(70),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],
["irish_shield_2",         "Irish Shield", [("ad_pict_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(80)|abundance(70),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],
["irish_shield_3",         "Irish Shield", [("ad_pict_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(80)|abundance(70),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],
["irish_shield_4",         "Irish Shield", [("ad_pict_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(80)|abundance(70),imodbits_shield, [], [fac_culture_2,fac_culture_2_1] ],

# DACIAN
["dacian_oval_shield_1",         "Dacian Shield", [("dacian_oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_2",         "Dacian Shield", [("dacian_oval_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_3",         "Dacian Shield", [("dacian_oval_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_4",         "Dacian Shield", [("dacian_oval_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_5",         "Dacian Shield", [("dacian_oval_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_6",         "Dacian Shield", [("dacian_oval_shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_7",         "Dacian Shield", [("dacian_oval_shield_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_8",         "Dacian Shield", [("dacian_oval_shield_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_9",         "Dacian Shield", [("dacian_oval_shield_9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_oval_shield_10",         "Dacian Shield", [("dacian_oval_shield_10",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_medium_shield_1",         "Dacian Shield", [("dacian_medium_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_medium_shield_2",         "Dacian Shield", [("dacian_medium_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_medium_shield_3",         "Dacian Shield", [("dacian_medium_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_medium_shield_4",         "Dacian Shield", [("dacian_medium_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
["dacian_medium_shield_5",         "Dacian Shield", [("dacian_medium_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 55, 70),
weight(get_shield_weight(shield_armor_t3,55,70))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(55)|shield_height(70)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large1",         "Dacian Shield", [("alx1dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large2",         "Dacian Shield", [("alx2dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large3",         "Dacian Shield", [("alx3dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large4",         "Dacian Shield", [("alx4dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large5",         "Dacian Shield", [("alx5dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_large6",         "Dacian Shield", [("alx6dacilarge",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3, 50, 93),
weight(get_shield_weight(shield_armor_t3,50,93))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(93)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small1",         "Dacian Round Shield", [("alx1dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small2",         "Dacian Round Shield", [("alx2dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small3",         "Dacian Round Shield", [("alx3dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small4",         "Dacian Round Shield", [("alx4dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small5",         "Dacian Round Shield", [("alx5dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],

["dacian_shield_small6",         "Dacian Round Shield", [("alx6dacismall",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2, 50, 0),
weight(get_shield_weight(shield_armor_t2,50,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(50)|abundance(80),imodbits_shield, [], [fac_culture_1] ],
# END DACIAN

# SCYTHIAN
["scythisn_shield_inf5",         "Scythian Shield", [("alx5scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(70),imodbits_shield, [], [fac_culture_3] ],

["scythisn_shield_inf6",         "Scythian Shield", [("alx6scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(70),imodbits_shield, [], [fac_culture_3] ],

# ARMENIAN
["scythisn_shield_inf1",         "Armenian Shield", [("alx1scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(80),imodbits_shield, [], [fac_culture_5] ],

["scythisn_shield_inf2",         "Armenian Shield", [("alx2scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(80),imodbits_shield, [], [fac_culture_5] ],

["scythisn_shield_inf3",         "Armenian Shield", [("alx3scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(80),imodbits_shield, [], [fac_culture_5] ],

["scythisn_shield_inf4",         "Armenian Shield", [("alx4scythinf",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,85),
weight(get_shield_weight(shield_armor_t3,50,85))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(85)|abundance(80),imodbits_shield, [], [fac_culture_5] ],

# GERMANIC
["eastern_germanic_shield_1",         "East Germanic Shield", [("eastern_germanic_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],
["eastern_germanic_shield_2",         "East Germanic Shield", [("eastern_germanic_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,90),
weight(get_shield_weight(shield_armor_t3,50,90))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(90)|abundance(80),imodbits_shield, [], [fac_culture_4] ],
["eastern_germanic_shield_3",         "East Germanic Shield", [("eastern_germanic_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,40,83),
weight(get_shield_weight(shield_armor_t3,40,83))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(85)|shield_width(40)|shield_height(83)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large1",         "Germanic Shield", [("e1german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large2",         "Germanic Shield", [("e2german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large3",         "Germanic Shield", [("e3german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large4",         "Germanic Shield", [("e4german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large5",         "Germanic Shield", [("e5german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large6",         "Germanic Shield", [("e6german",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_1",         "Germanic Shield", [("germanic_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_2",         "Germanic Shield", [("germanic_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_3",         "Germanic Shield", [("germanic_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_4",         "Germanic Shield", [("germanic_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,43,86),
weight(get_shield_weight(shield_armor_t3,43,86))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(43)|shield_height(86)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["german_night_shield_1","Germanic Long Shield", [("german_night_shield_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t4,70,55),
weight(get_shield_weight(shield_armor_t4,70,55))|abundance(100)|body_armor(shield_armor_t4)|hit_points(shield_hitpoints_t4)|spd_rtng(90)|shield_height(70)|shield_width(55), imodbits_shield, [], [fac_culture_4]],
["german_night_shield_2","Germanic Long Shield", [("german_night_shield_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t4,70,55),
weight(get_shield_weight(shield_armor_t4,70,55))|abundance(100)|body_armor(shield_armor_t4)|hit_points(shield_hitpoints_t4)|spd_rtng(90)|shield_height(70)|shield_width(55), imodbits_shield, [], [fac_culture_4]],
["german_night_shield_3","Germanic Long Shield", [("german_night_shield_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t4,70,55),
weight(get_shield_weight(shield_armor_t4,70,55))|abundance(100)|body_armor(shield_armor_t4)|hit_points(shield_hitpoints_t4)|spd_rtng(90)|shield_height(70)|shield_width(55), imodbits_shield, [], [fac_culture_4]],
["german_night_shield_4","Germanic Long Shield", [("german_night_shield_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t4,70,55),
weight(get_shield_weight(shield_armor_t4,70,55))|abundance(100)|body_armor(shield_armor_t4)|hit_points(shield_hitpoints_t4)|spd_rtng(90)|shield_height(70)|shield_width(55), imodbits_shield, [], [fac_culture_4]],
["german_night_shield_5","Germanic Long Shield", [("german_night_shield_5", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t4,70,55),
weight(get_shield_weight(shield_armor_t4,70,55))|abundance(100)|body_armor(shield_armor_t4)|hit_points(shield_hitpoints_t4)|spd_rtng(90)|shield_height(70)|shield_width(55), imodbits_shield, [], [fac_culture_4]],

["germanic_shield_large7",         "Germanic Shield", [("e1larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large8",         "Germanic Shield", [("e2larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large9",         "Germanic Shield", [("e3larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large10",         "Germanic Shield", [("e4larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large11",         "Germanic Shield", [("e5larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_large12",         "Germanic Shield", [("e6larscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,47,95),
weight(get_shield_weight(shield_armor_t3,47,95))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(47)|shield_height(95)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large1",         "Germanic Shield", [("e1hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large2",         "Germanic Shield", [("e2hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large3",         "Germanic Shield", [("e3hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large4",         "Germanic Shield", [("e4hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large5",         "Germanic Shield", [("e5hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["germanic_shield_hex_large6",         "Germanic Shield", [("e6hexscutum",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,45,97),
weight(get_shield_weight(shield_armor_t3,45,97))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(97)|abundance(80),imodbits_shield, [], [fac_culture_4] ],

["simple_germanic_shield",  "Simple Germanic Shield", [("shield_kite_n", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,32,85),
weight(get_shield_weight(shield_armor_t1,32,85))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(70)|shield_width(32)|shield_height(85),imodbits_shield,[],[fac_culture_4] ],
# END GERMANIC SHIELDS

## ARABIAN
["arabian_oval_shield_1",         "Arabian Shield", [("eastern_oval_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(60),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["arabian_oval_shield_2",         "Arabian Shield", [("eastern_oval_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(60),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["arabian_oval_shield_3",         "Arabian Shield", [("eastern_oval_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(60),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],
["arabian_oval_shield_4",         "Arabian Shield", [("eastern_oval_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,50,100),
weight(get_shield_weight(shield_armor_t3,50,100))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(100)|abundance(60),imodbits_shield, [], [fac_culture_6,fac_culture_8, fac_culture_5]  ],

# ILLYRIAN
["illyrian_shield_large1",         "Illyrian Shield", [("esquareillyrian1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2,49,99),
weight(get_shield_weight(shield_armor_t3,49,99))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(49)|shield_height(99)|abundance(10),imodbits_shield, [], [fac_culture_7] ],

["illyrian_shield_large2",         "Illyrian Shield", [("esquareillyrian2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t2,49,99),
weight(get_shield_weight(shield_armor_t3,49,99))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(95)|shield_width(49)|shield_height(99)|abundance(10),imodbits_shield, [], [fac_culture_7] ],

["illyrian_shield_heavy1",         "Illyrian Shield", [("illyethureos1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,45,87),
weight(get_shield_weight(shield_armor_t3,45,87))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(87)|abundance(10),imodbits_shield, [], [fac_culture_7] ],

["illyrian_shield_heavy2",         "Illyrian Shield", [("illyethureos2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,45,87),
weight(get_shield_weight(shield_armor_t3,45,87))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(87)|abundance(10),imodbits_shield, [], [fac_culture_7] ],

["illyrian_shield_heavy3",         "Illyrian Shield", [("illyethureos3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
get_shield_price(shield_armor_t3,45,87),
weight(get_shield_weight(shield_armor_t3,45,87))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(45)|shield_height(87)|abundance(10),imodbits_shield, [], [fac_culture_7] ],

# barbarian battle standards
["battle_standard","Battle Standard", [("roman_spear_banner",0)],itp_type_polearm|itp_cant_use_on_horseback|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_pike,700,
 weight(1.5)|spd_rtng(84) |abundance(5)| weapon_length(155)|swing_damage(25,blunt) | thrust_damage(15,blunt),imodbits_polearm,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_flag_pole_new", ":agent_no", ":troop_no")])]],


# generic scutum
["old_scutum", "Old Scutum",   [("old_roman_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,55,108),
weight(get_shield_weight(shield_armor_t3,55,108))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(20),imodbits_shield, [],[fac_culture_7]],
["old_scutum_2", "Old Scutum",   [("old_roman_scutum_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,55,108),
weight(get_shield_weight(shield_armor_t3,55,108))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(20),imodbits_shield, [],[fac_culture_7]],
["old_scutum_3", "Old Scutum",   [("old_roman_scutum_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,55,108),
weight(get_shield_weight(shield_armor_t3,55,108))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(20),imodbits_shield, [],[fac_culture_7]],
["old_scutum_4", "Old Scutum",   [("old_roman_scutum_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,55,108),
weight(get_shield_weight(shield_armor_t3,55,108))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(20),imodbits_shield, [],[fac_culture_7]],

# OLD ROMAN ROUND SHIELDS
["old_round_shield_5", "Old Roman Round Shield", [("old_round_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3,30,0),
weight(get_shield_weight(shield_armor_t3,30,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(30),imodbits_shield ],
["old_round_shield_4", "Old Roman Round Shield", [("old_round_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3,30,0),
weight(get_shield_weight(shield_armor_t3,30,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(30),imodbits_shield ],
["old_round_shield_3", "Old Roman Round Shield", [("old_round_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3,30,0),
weight(get_shield_weight(shield_armor_t3,30,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(30),imodbits_shield ],
["old_round_shield_2", "Old Roman Round Shield", [("old_round_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3,30,0),
weight(get_shield_weight(shield_armor_t3,30,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(30),imodbits_shield ],
["old_round_shield_1", "Old Roman Round Shield", [("old_round_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t3,30,0),
weight(get_shield_weight(shield_armor_t3,30,0))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(97)|shield_width(30),imodbits_shield ],

# ROMAN round shields
["roman_shield_1",         "Round Shield", [("roman_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],
["roman_shield_2",         "Round Shield", [("roman_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],
["roman_shield_3",         "Round Shield", [("roman_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],
["roman_shield_4",         "Round Shield", [("roman_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],
["roman_shield_5",         "Round Shield", [("roman_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],
["roman_shield_6",         "Round Shield", [("roman_shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1, 46, 0),
weight(get_shield_weight(shield_armor_t1,46,0))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(95)|shield_width(46),imodbits_shield, [], [fac_culture_7] ],

##roman signum
#legionszeichen
["signum_bireme", "Birem Signum", [("birem_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_capricorn", "Capricorn Signum", [("capricorn_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_capwolf", "Wolf Signum", [("capwolf_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_elephant", "Elephant Signum", [("elep_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_lion", "Lion Signum", [("lion_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_ox", "Ox Signum", [("ox_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_pegasus", "Pegasus Signum", [("pegasus_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_scorpion", "Scorpion Signum", [("scorpio_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_praetoriani", "Preatorian Signum", [("signum_pretoriana",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["signum_trident", "Trident Signum", [("trident_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##auqila
["aquila", "Aquila", [("eagle_imago",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["aquila3", "Aquila", [("roman_aquila2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["aquila4", "Aquila", [("roman_aquila3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 ,weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["aquila5", "Aquila", [("roman_aquila4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["aquila6", "Aquila", [("roman_aquila5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

#chortenzeichen fur centurie
["signum_signifer", "Signum", [("roman_signifero_signum",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["signum_signifer_2", "Signum", [("signum_new_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

#vexlia
["vexilum_legio_xiii", "Vexilum XIII", [("roman_vexillum_GemIII",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_vi", "Vexilum VI", [("roman_vexillum_LegVIferr",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_x", "Vexilum X", [("roman_vexillum_LegXFerr",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xi", "Vexilum XI", [("roman_vexillum_LegXIcla",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_vii", "Vexilum VII", [("roman_vexillum_VIIGalba",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xxi", "Vexilum XXI", [("roman_vexillum_XXIrap",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_i", "Vexilum I", [("roman_vexillum_adiutrix",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_iii", "Vexilum III", [("roman_vexillum_augustaIII",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_vi_vict", "Vexilum VI Victrix", [("roman_vexillum_legVIvix",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_v", "Vexilum V Macedonia", [("roman_vexillum_macedonicaV",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_praetoriani", "Vexilum Praetoriani", [("roman_vexillum_praetorian",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_v_alaudae", "Vexilum V Alaudae", [("roman_vexillum_alaudaeV",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["vexilum_praetoriani_2", "Vexilum Praetoriani", [("roman_vexillum_praetorian_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_praetoriani_3", "Vexilum Praetoriani", [("roman_vexillum_praetorian_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

["vexilum_legio_viiii_hisp", "Vexilum IX Hispania", [("standard_leg_hisp",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xx_val", "Vexilum XX Valeria Victrix", [("standard_leg_val",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xx_dei", "Vexilum XXII Deiotariana", [("standard_leg_xxii",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xx_prim", "Vexilum XXII Primigenia", [("standard_leg_xxiiprim",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xiv", "Vexilum I Parthica", [("standard_leg_i_parthica",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xv", "Vexilum XV Apollinaris", [("standard_leg_xv_ap",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_i_germ", "Vexilum I Germanica", [("standard_leg_igerm",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xvigal", "Vexilum XVI Gallica", [("standard_leg_xvigal",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_ful", "Vexilum XII Fulminata", [("standard_leg_ful",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_scy", "Vexilum IV Scythica", [("standard_leg_scy",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_italica", "Vexilum II Italica", [("standard_leg_italica",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_xxx_ulp", "Vexilum XXX Ulpia Victrix", [("standard_leg_xxx_upl",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_minerva", "Vexilum I Minerva", [("standard_leg_minevra",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_amogus", "Vexilum LXIX Amogus", [("standard_leg_amogus",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_biggus", "Vexilum CDXX Biggus Dickus", [("standard_leg_biggus",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["vexilum_legio_testiculus", "Vexilum XXX Testiculus", [("standard_leg_testiculus",0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
42 , weight(3)|hit_points(960)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],

##roman shields
["scutum_legio_i", "Legio I Scutum",   [("legio_i_adiutrix_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_iii", "Legio III Scutum",   [(" legio_iii_augusta_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_xxi", "Legio XXI Scutum",   [("legio_rapaxxi_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_v", "Legio V Scutum",   [("legio_v_alaudae_scutumm" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_v_mac", "Legio V mac. Scutum",   [("legio_v_macedonica_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_vi_ferr", "Legio VI Ferrata Scutum",   [(" legio_vi_ferr_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_vii_galb", "Legio VII  Scutum",   [(" legio_vi_galb_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_vi_vict", "Legio VI Victrix Scutum",   [("legio_vi_victrix_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_x", "Legio X Scutum",   [(" legio_x_fretensis_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_xi", "Legio XI Scutum",   [(" legio_xi_claudia_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_legio_xiii", "Legio XIII Scutum",   [(" legio_xiii_gemina_scutum" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_praetorian", "Praetoriani Scutum",   [(" praetorian_cohort_scutumm" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_praetorian_2", "Praetoriani Scutum",   [(" praetorian_cohort_scutumm_red" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_batavorum_cav", "Cetratus",   [(" auxiliary_cavalry_bataviorum_cetratus" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_1", "Cetratus",   [("cetratus1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_2", "Cetratus",   [("cetratus2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_3", "Cetratus",   [("cetratus3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_4", "Cetratus",   [("cetratus4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_5", "Cetratus",   [("cetratus5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_6", "Cetratus",   [("cetratus6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_7", "Cetratus",   [("cetratus7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_8", "Cetratus",   [("cetratus8" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],


["cetratus_aux_9", "Cetratus",   [("oval_cav_hispa" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_10", "Cetratus",   [("roman_shield_xx" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_11", "Cetratus",   [("oval_decurion" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_12", "Cetratus",   [("griffon" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_13", "Cetratus",   [("roman_scutum_aux1" ,0)],itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_14", "Cetratus",   [("roman_shield_auxscut" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_15", "Cetratus",   [("roman_shield_centeagleboss" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_16", "Cetratus",   [("roman_shield_II" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_17", "Cetratus",   [("lion" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_18", "Cetratus",   [("roman_shield_xxiide" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_19", "Cetratus",   [("scutum_gemina" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_20", "Cetratus",   [("roman_shield_ix" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_21", "Cetratus",   [("roman_shield_vipf" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_22", "Cetratus",   [("4lightning" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_23", "Cetratus",   [("blue" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_24", "Cetratus",   [("roman_shield_cent2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_25", "Cetratus",   [("roman_shield_ovalg" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_26", "Cetratus",   [("roman_shield_yellow" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_27", "Cetratus",   [("roman_shield_cent1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_28", "Cetratus",   [("cohors_gaul" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_29", "Cetratus",   [("cetratus_pret" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_30", "Cetratus",   [("cohors_lingon" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["cetratus_aux_batavorum_inf", "Cetratus",   [("cohort_bataviorum_cetratus" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,50,98),
weight(get_shield_weight(shield_armor_t3,50,98))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(50)|shield_height(98)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["praetorian_cav_scutum", "Scutum Preatoriani Eques",   [("praetorian_cavalry_scutum" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,44,88),
weight(get_shield_weight(shield_armor_t4,44,88))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(44)|shield_height(88)|abundance(30),imodbits_shield, [],[fac_culture_7]],
["praetorian_cav_scutum_2", "Scutum Preatoriani Eques",   [("praetorian_cavalry_scutum_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,44,88),
weight(get_shield_weight(shield_armor_t4,44,88))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(44)|shield_height(88)|abundance(30),imodbits_shield, [],[fac_culture_7]],

["officer_shield", "Parma",   [("roman_noble_shielde1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t4,53,0),
weight(get_shield_weight(shield_armor_t4,53,0))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(87)|shield_width(53)|abundance(30),imodbits_shield, [],[fac_culture_7]],

["officer_shield_2", "Parma",   [("roman_noble_shielde2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t4,53,0),
weight(get_shield_weight(shield_armor_t4,53,0))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(87)|shield_width(53)|abundance(30),imodbits_shield, [],[fac_culture_7]],

["officer_shield_3", "Parma",   [("roman_noble_shielde3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t4,53,0),
weight(get_shield_weight(shield_armor_t4,53,0))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(87)|shield_width(53)|abundance(30),imodbits_shield, [],[fac_culture_7]],

["scutum_1", "Scutum",   [("scutum_4lightning" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_2", "Scutum",   [("scutum_roman_shield_yellow" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_3", "Scutum",   [("scutum_blue" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_4", "Scutum",   [("roman_shield_boss" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_5", "Scutum",   [("scutum_roman_shield_cent1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_6", "Scutum",   [("scutum_roman_shield_cent2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_7", "Scutum",   [("roman_default" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_8", "Scutum",   [("scutum_griffon" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_9", "Scutum Legio VI Victrix",   [("scutum_roman_shield_vipf" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_10", "Scutum Legio XXII Primigenia",   [("scutum_roman_shield_xxiip" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_11", "Scutum",   [("scutum_lion" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_12", "Scutum Legio IX Hispania",   [("trident" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_13", "Scutum Legio XX",   [("scutum_xx" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_14", "Scutum Legio XIIII Gemina",   [("scutum_gemina_large" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_15", "Scutum Legio XXII Deiotariana",   [("scutum_roman_shield_xxiide" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_deitoriana", "Legio XXII Scutum",   [(" legio_deitoriana" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_16", "Scutum Legio XIIII Gemina",   [("roman_shield_scutum_xiiii" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_17", "Scutum",   [("roman_shield_new_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_18", "Scutum",   [("roman_shield_new_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_19", "Scutum",   [("roman_shield_new_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_20", "Scutum",   [("roman_shield_new_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_21", "Scutum",   [("scutum_roman_shield_new1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_22", "Scutum",   [("scutum_roman_shield_new2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],
# END ROMAN SHIELDS

# JUDEAN SCUTUM
["judean_shield_large_1", "Judean Scutum",   [(" judean_shield_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_8]],
["judean_shield_large_2", "Judean Scutum",   [(" judean_shield_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_8]],
["judean_shield_large_3", "Judean Scutum",   [(" judean_shield_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_8]],
["judean_shield_large_4", "Judean Scutum",   [(" judean_shield_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_8]],

# EGYPTIAN SCUTUM
["egyptian_shield_large_1", "Egyptian Scutum",   [(" egyptian_shield_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[]],
["egyptian_shield_large_2", "Egyptian Scutum",   [(" egyptian_shield_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[]],
["egyptian_shield_large_3", "Egyptian Scutum",   [(" egyptian_shield_3" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[]],
["egyptian_shield_large_4", "Egyptian Scutum",   [(" egyptian_shield_4" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[]],

# SPECIAL SCUTUM
["cetratus_christian", "Christian Cetratus",   [("scutum_christian2" ,0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],
["cetratus_mithras", "Mithras Cetratus",   [("scutum_mithras2" ,0)], itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t3,44,88),
weight(get_shield_weight(shield_armor_t3,44,88))|hit_points(shield_hitpoints_t3)|body_armor(shield_armor_t3)|spd_rtng(90)|shield_width(44)|shield_height(88)|abundance(60),imodbits_shield, [],[fac_culture_7]],

["scutum_christian_1", "Christian Scutum",   [("scutum_christian3" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],
["scutum_mithras_1", "Mithras Scutum",   [("scutum_mithras3" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,49,95),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(49)|shield_height(95)|abundance(10),imodbits_shield, [],[fac_culture_7]],

["scutum_christian_2", "Christian Scutum",   [("scutum_christian" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],
["scutum_mithras_2", "Mithras Scutum",   [("scutum_mithras" ,0)], itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
get_shield_price(shield_armor_t4,55,108),
weight(get_shield_weight(shield_armor_t4,55,108))|hit_points(shield_hitpoints_t4)|body_armor(shield_armor_t4)|spd_rtng(85)|shield_width(55)|shield_height(108)|abundance(10),imodbits_shield, [],[fac_culture_7]],

# OTHER GENERIC SHIELDS
["simple_thraex_shield", "Simple Shield", [("thraex_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,40,50),
weight(get_shield_weight(shield_armor_t1,40,50))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(100)|shield_width(40)|shield_height(50),imodbits_shield ],

["fur_covered_shield",  "Simple Shield", [("shield_kite_m", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t1,38,58),
weight(get_shield_weight(shield_armor_t1,38,58))|hit_points(shield_hitpoints_t1)|body_armor(shield_armor_t1)|spd_rtng(70)|shield_width(38)|shield_height(58),imodbits_shield ],

["leather_covered_round_shield", "Leather Covered Round Shield", [("leathershield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,55,0),
weight(get_shield_weight(shield_armor_t2,55,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(97)|shield_width(55),imodbits_shield ],

["hide_covered_round_shield", "Simple Round Shield", [("pirat1_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,40,0),
weight(get_shield_weight(shield_armor_t2,40,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(97)|shield_width(40),imodbits_shield ],

["hide_covered_round_shield_2", "Round Shield", [("pirat2_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,40,0),
weight(get_shield_weight(shield_armor_t2,40,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(97)|shield_width(40),imodbits_shield ],

["hide_covered_round_shield_3", "Round Shield", [("pirat3_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
get_shield_price(shield_armor_t2,30,0),
weight(get_shield_weight(shield_armor_t2,30,0))|hit_points(shield_hitpoints_t2)|body_armor(shield_armor_t2)|spd_rtng(97)|shield_width(30),imodbits_shield ],

##missle weapons BEGIN

#generic missles
["javelin",         "Javelins", [("javelin_new",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, abundance(90)|weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(26) | thrust_damage(26 ,  pierce)|max_ammo(5)|weapon_length(75)|accuracy(90),imodbits_thrown ],
["jarid",         "Heavy Throwing Spears", [("bryntvari2",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
500 , abundance(70)|weight(3)|difficulty(3)|spd_rtng(80)|shoot_speed(23) | thrust_damage(31 ,  pierce)|max_ammo(2)|weapon_length(100)|accuracy(90),imodbits_thrown ], #cambiado chief
["throwing_spears",         "Throwing Spears", [("atgeirr1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(28 ,  pierce)|max_ammo(3)|weapon_length(85)|accuracy(90),imodbits_thrown ], #cambiado chief

#african
["javelin_berber",         "Berber Javelins", [("javelin_x",0),("javelin_x_carry", ixmesh_carry)], itp_type_thrown|itp_primary|itp_secondary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
310, abundance(90)|weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(27) | thrust_damage(27 ,  pierce)|max_ammo(5)|weapon_length(65)|accuracy(90),imodbits_thrown ],

#eastern
["throwing_spears_east",         "Throwing Spears", [("eastern_throwing_spear",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(29 ,  pierce)|max_ammo(4)|weapon_length(108)|accuracy(90),imodbits_thrown ], #cambiado chief

#dacian
["throwing_spears_dacian",         "Dacian Throwing Spears", [("dacian_heavy_javelin",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(29 ,  pierce)|max_ammo(4)|weapon_length(85)|accuracy(90),imodbits_thrown, [],[fac_culture_1] ], #cambiado chief

#germanic
["throwing_spears_germanic",         "Germanic Throwing Spears", [("spear_finished_2",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(29 ,  pierce)|max_ammo(4)|weapon_length(125)|accuracy(90),imodbits_thrown, [],[fac_culture_1] ], #cambiado chief

#celtic
["jarid_celt",         "Heavy Throwing Spears", [("celtic_throwing_spear",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
500 , abundance(70)|weight(3)|difficulty(3)|spd_rtng(80)|shoot_speed(23) | thrust_damage(31 ,  pierce)|max_ammo(2)|weapon_length(123)|accuracy(95),imodbits_thrown, [],[fac_culture_2,fac_culture_2_1] ], #cambiado chief

#roman
["throwing_spears_roman",         "Throwing Spears", [("roman_jav",0)], itp_extra_penetration|itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(29 ,  pierce)|max_ammo(4)|weapon_length(85)|accuracy(90),imodbits_thrown, [],[fac_culture_4,fac_culture_5,fac_culture_6,fac_culture_7,fac_culture_8,fac_culture_9] ], #cambiado chief
["pilum", "Pilum", [("roman_pilum_100",0)], itp_extra_penetration|itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_throw_javelin,
500, abundance(70)|weight(2)|difficulty(3)|spd_rtng(80)|shoot_speed(25)|thrust_damage(33,pierce)|max_ammo(1)|weapon_length(100)|accuracy(90), imodbits_thrown, [
], [fac_culture_7] ],
["pilum_2", "Heavy Pilum", [("roman_pilum_100_h",0)], itp_extra_penetration|itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_throw_javelin,
500, abundance(70)|weight(2)|difficulty(4)|spd_rtng(80)|shoot_speed(25)|thrust_damage(35,pierce)|max_ammo(1)|weapon_length(100)|accuracy(90), imodbits_thrown, [
], [fac_culture_7] ],
["pilum_3", "Pilum", [("roman_pilum_87",0)], itp_extra_penetration|itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_throw_javelin,
500,  abundance(70)|weight(2)|difficulty(3)|spd_rtng(80)|shoot_speed(25)|thrust_damage(33,pierce)|max_ammo(1)|weapon_length(87)|accuracy(90), imodbits_thrown, [
], [fac_culture_7] ],

#generic bows
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone,
1,  abundance(60)|weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(10 ,  blunt)|max_ammo(20)|weapon_length(8)|accuracy(98),imodbit_large_bag ],
["throwing_knives", "Throwing Knives", [("throwing_knife_new",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,
100,  abundance(60)|weight(1.2)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(15,  cut)|max_ammo(20)|weapon_length(0)|accuracy(99),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger_new",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,
200,  abundance(60)|weight(1.2)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(20,  cut)|max_ammo(20)|weapon_length(0)|accuracy(99),imodbits_thrown ],
["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
17 ,  abundance(80)|weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(46) | thrust_damage(23 ,  pierce)|accuracy(99),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
58 ,  abundance(80)|weight(1)|difficulty(1)|spd_rtng(86) | shoot_speed(48) | thrust_damage(25 ,  pierce  )|accuracy(99),imodbits_bow ],

#barbarian bows
["german_shortbow",         "Short Bow", [("german_shortbow",0),("german_shortbow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
65 ,  abundance(80)|weight(1)|difficulty(1)|spd_rtng(86) | shoot_speed(48) | thrust_damage(26 ,  pierce  )|accuracy(99),imodbits_bow ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
145 , abundance(60)|weight(1.75)|difficulty(3)|spd_rtng(70) | shoot_speed(61) | thrust_damage(28 ,  pierce)|accuracy(96),imodbits_bow,[],[fac_culture_7,fac_culture_4,fac_culture_2,fac_culture_2_1,fac_culture_1] ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
728 ,  abundance(50)|weight(1.65)|difficulty(4)|spd_rtng(71) | shoot_speed(59) | thrust_damage(31 ,pierce)|accuracy(96),imodbits_bow,[],[fac_culture_7,fac_culture_2,fac_culture_2_1] ],

#arabian bow
["arabian_bow_1",         "Arabian Bow", [("arabian_bow_1",0),("arabian_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 ,  abundance(70)|weight(1.25)|difficulty(2)|spd_rtng(92) | shoot_speed(49) | thrust_damage(26 ,  pierce)|accuracy(98),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6,fac_culture_1] ],
["arabian_bow_2",         "Arabian Bow", [("arabian_bow_2",0),("arabian_case_2", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 ,  abundance(70)|weight(1.25)|difficulty(2)|spd_rtng(92) | shoot_speed(49) | thrust_damage(26 ,  pierce)|accuracy(98),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6,fac_culture_1] ],

# sarmatian bows
["nomad_bow",         "Composite Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 ,  abundance(70)|weight(1.25)|difficulty(2)|spd_rtng(92) | shoot_speed(49) | thrust_damage(26 ,  pierce)|accuracy(98),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6,fac_culture_1] ],
["khergit_bow",         "Composite Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , abundance(60)|weight(1.25)|difficulty(3)|spd_rtng(82) | shoot_speed(51) | thrust_damage(28 ,pierce)|accuracy(96),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6] ],

["persian_bow",         "Composite Bow", [("persian_bow_1",0),("persian_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , abundance(60)|weight(1.25)|difficulty(3)|spd_rtng(82) | shoot_speed(51) | thrust_damage(28 ,pierce)|accuracy(96),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6] ],

["khergit_bow_2",         "Composite Bow", [("steppe_bow_1",0),("steppe_bow_1_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
437 , abundance(60)|weight(1.25)|difficulty(3)|spd_rtng(82) | shoot_speed(51) | thrust_damage(29 ,pierce)|accuracy(97),imodbits_bow,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6] ],

["sarmatian_bow",         "Composite Bow", [("sarmatian_bow_small",0),("sarmatian_case_1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
437 , abundance(50)|weight(1.25)|difficulty(3)|spd_rtng(80) | shoot_speed(53) | thrust_damage(29 ,pierce)|accuracy(96),imodbit_cracked | imodbit_bent | imodbit_masterwork,[],[fac_culture_7,fac_culture_3,fac_culture_5,fac_culture_6] ],

["strong_bow",         "Caucasian Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , abundance(60)|weight(1.25)|difficulty(3)|spd_rtng(82) | shoot_speed(51) | thrust_damage(27 ,pierce)|accuracy(97),imodbits_bow,[],[fac_culture_5] ],

#nubian bow
["nubian_war_bow",         "Nubian Long Bow", [("nubian_bow",0),("nubian_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
730 ,  abundance(50)|weight(1.65)|difficulty(4)|spd_rtng(71) | shoot_speed(59) | thrust_damage(31 ,pierce)|accuracy(97),imodbits_bow,[],[] ],

#slings
["sling", "Sling", [("sling_2",0)],itp_type_pistol |itp_merchandise|itp_primary|itp_secondary|itp_cant_use_on_horseback ,itcf_shoot_pistol,
50,  abundance(90)|weight(0.5)|difficulty(0)|spd_rtng(100) | shoot_speed(69) | thrust_damage(28 ,blunt)|max_ammo(1)|accuracy(99),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

#ballista
["ballista_mounted", "Mounted Ballista", [("ballista_mounted",0)], itp_extra_penetration|itp_type_crossbow |itp_primary|itp_two_handed,itcf_shoot_crossbow,
10830 , weight(8)|difficulty(18)|spd_rtng(43) | shoot_speed(68) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(99),imodbits_crossbow, [], [] ],
["ballista", "Ballista", [("ballista",0),("ballista_carry",ixmesh_carry)], itp_merchandise|itp_can_knock_down|itp_extra_penetration|itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_use_on_horseback|itp_cant_reload_while_moving,itcf_shoot_crossbow|itcf_carry_crossbow_back,
6830 , abundance(30)|weight(10)|difficulty(20)|spd_rtng(17) | shoot_speed(78) | thrust_damage(500 ,pierce)|max_ammo(1)|accuracy(100),imodbits_crossbow, [], [fac_culture_7] ],
##missle weapons end
##TORCH
["torch",         "Torch", [("torch_item",0)], itp_type_shield|itp_shield_no_parry|itp_force_attach_left_hand|itp_merchandise, 0,
10, weight(2.5)|hit_points(30)|body_armor(1)|spd_rtng(82)|weapon_length(0),0,
[(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30), ])]],
["torch2", "Torch", [("torch_b",0)], itp_type_shield|itp_merchandise, 0,
10,weight(1)|abundance(90)|hit_points(60)|spd_rtng(0)|shield_width(1), 0,
[(ti_on_init_item, [(set_position_delta,22,37.5,-5.7),(particle_system_add_new, "psys_torch_fire_2"),(particle_system_add_new, "psys_torch_smoke"),(set_position_delta,28,39,-6.9),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),]],

# ["roman_cloak_1","Experimental cloak as glove", [("roman_cloak_L",0),("roman_cloak_inv", ixmesh_inventory)], itp_attach_armature|itp_unique|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
# get_gloves_price(2), weight(0.1)|abundance(20)|body_armor(1)|difficulty(0),imodbits_cloth,[], []],

##for musicans
["horn","Horn",[("horn",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_merchandise,0,
1000,weight(2.0)|abundance(20),0,[],[fac_culture_1,fac_culture_2,fac_culture_2_1,fac_culture_3,fac_culture_4]],
["trumpet_celtic","Carnyx",[("trumpet_celtic",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_merchandise,0,
1000,weight(2.0)|abundance(20),0,[],[fac_culture_1,fac_culture_2,fac_culture_2_1,fac_culture_3,fac_culture_4]],
["trumpet_eastern","Trumpet",[("trumpet_eastern",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_merchandise,0,
1000,weight(2.0)|abundance(20),0,[],[fac_culture_1,fac_culture_2,fac_culture_2_1,fac_culture_3,fac_culture_4]],
["f_cornu", "Cornu", [("f_cornu",0),("cornu_carry_spear",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_spear,
400, weight(2.75)|difficulty(0)|spd_rtng(40)|weapon_length(125)|swing_damage(0,cut)|thrust_damage(0,pierce), imodbits_sword_high ],

["lyre","Lyre",[("dedal_liraL",0)],		itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
100,weight(1),0],
["lute","Lute",[("dedal_lutniaL",0)],	itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
100,weight(1),0],
["flute","Flute",[("flute_hand_L",0)],	itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
50,weight(1),0],
## for ministrels end

##stuff for wedding
["keys", "Ring of Keys", [("bride_crown",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3"),
    ]),
], [fac_culture_7] ],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0,
1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
##stuff for wedding end

##special siege weapons
["greek_fire", "Vulcani ignis", [("oil_greek_fire",0)], itp_merchandise|itp_type_thrown|itp_can_penetrate_shield|itp_can_knock_down|itp_bonus_against_shield|itp_crush_through|itp_no_pick_up_from_ground|itp_primary|itp_remove_item_on_use ,itcf_throw_axe,
7000 , weight(5.0)|difficulty(3)|spd_rtng(70)|shoot_speed(14)|thrust_damage(65 ,  blunt)|max_ammo(1)|weapon_length(0),imodbits_missile,
[
(ti_on_missile_hit, # when missile hits
   [
  (try_begin),
    (this_or_next|multiplayer_is_server),
    (neg|game_in_multiplayer_mode),
    (store_trigger_param_1, ":shooter"),
    (copy_position, pos63, pos1),
    (set_fixed_point_multiplier, 1),
    (try_for_agents,":agent",pos63, 3), # search all agents in 3 meters
      (agent_is_alive,":agent"),
      (agent_get_team, ":grenadiers_team", ":shooter"),
      (agent_get_team, ":targets_team", ":agent"),
      (teams_are_enemies, ":grenadiers_team", ":targets_team"),
      (agent_set_animation, ":agent", "anim_rider_fall_roll"),
      (agent_deliver_damage_to_agent, ":shooter", ":agent", 150),
      (try_begin),
        (get_player_agent_no, ":player_agent"),
        (eq, ":agent", ":player_agent"),
        (display_message, "@Recieved damage from fire!", color_terrible_news),
      (try_end),
    (try_end),
  (try_end),
   ]),
(ti_on_missile_hit,
   [
    (particle_system_burst, "psys_fireplace_fire_big", pos1, 100),
    (particle_system_burst, "psys_village_fire_big", pos1, 7),
	  (particle_system_burst, "psys_village_fire_smoke_big", pos1, 50),
   ]),]],
["stones_siege","Large Stone", [("siegestone",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground|itp_can_knock_down|itp_can_penetrate_shield|itp_remove_item_on_use|itp_merchandise, itcf_throw_axe,
50, weight(3)|abundance(20)|difficulty(4)|spd_rtng(70) | shoot_speed(14) | thrust_damage(50 ,  blunt)|max_ammo(2)|weapon_length(14),imodbits_none, #chief cambiado
[
    (ti_on_missile_hit,
      [
	  (try_begin),
		#Solid Round Script
        #pos1 - Missile hit position
        #param_1 - Shooter agent
      (this_or_next|multiplayer_is_server),
      (neg|game_in_multiplayer_mode),
      (store_trigger_param_1,":shooter"),
      (set_fixed_point_multiplier, 100),
      (copy_position, pos63, pos1),
      (particle_system_burst,"psys_piedra_dust",pos1,1),
      (try_for_agents,":agent",pos63,100),
        (agent_is_alive,":agent"),
        (agent_get_team, ":grenadiers_team", ":shooter"),
        (agent_get_team, ":targets_team", ":agent"),
        (teams_are_enemies, ":grenadiers_team", ":targets_team"),
        (neq,":agent",":shooter"),
        (agent_deliver_damage_to_agent,":shooter",":agent", 50),
        (play_sound,"snd_shield_broken"),
      (try_end),
    (try_end),
]),]],
##special siege weapons end

##other legendary items and treasures
["hercules_club","Donar's club", [("hercules_club",0)], itp_unique|itp_type_one_handed_wpn| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
50000,weight(10)|difficulty(20)|spd_rtng(70)|weapon_length(55)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["celtic_carnyx","Golden Carnyx", [("celtic_carnyx",0)], itp_unique, 0,
50000,weight(5.0)|abundance(0)|max_ammo(1),imodbits_none],
["dacian_treasure","Treasure of the Gaete", [("dacian_treasure",0)], itp_unique, 0,
100000,weight(20)|abundance(0)|max_ammo(1),imodbits_none],
["menorah","Golden Menorah", [("menorah",0)], itp_unique, 0,
50000,weight(15)|abundance(0)|max_ammo(1),imodbits_none],
["scythian_bong","Golden Bong", [("totally_not_temp_scythian_bong",0)], itp_unique, 0,
25000,weight(1.0)|abundance(0)|max_ammo(1),imodbits_none],

##special perfume
["perfume_special","Roses of Egypt", [("roman_palace_plate_2",0)],itp_unique|itp_type_goods,0,
15000,weight(1)|abundance(60),imodbits_none],

# Neros lyre
["lyre_rich","Golden Lyre",[("lyre_neroL",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
4000,weight(1),0],

##special items
#crown
["kush_crown", "Crown of Kush", [("kush_crown",0)],itp_unique|itp_type_head_armor|itp_civilian,0,
crown_head_price,crown_head,imodbits_none],
["parthian_female_hat", "Crown of Babylon", [("parthian_female_hat",0)],itp_unique|itp_type_head_armor|itp_civilian,0,
crown_head_price,crown_head,imodbits_none],
["crown_shah", "Crown of Persia", [("crown_eastern",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,
crown_head_price,crown_head,imodbits_none],
["laurel_gold", "Golden Laurel", [("laurel_gold",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,
crown_head_price,crown_head,imodbits_none],
["female_crown", "Golden Crown", [("female_crown",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,
crown_head_price,crown_head,imodbits_none],
["laurel_silver", "Silver Laurel", [("laurel_silver",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,
crown_head_price,crown_head,imodbits_none],
["pharaoh_crown", "Pschent ", [("pharaoh",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_attach_armature|itp_fit_to_head,0,
crown_head_price,crown_head,imodbits_none],

##bonus item
["pilos_ultimate", "Pilos", [("pilos_ultimate",0)], itp_unique|itp_type_head_armor |itp_covers_beard ,0,
medium_head_price,medium_head,imodbits_plate, [], [] ],
["felt_steppe_cap", "Strange Cap", [("noel_helmet",0)], itp_unique|itp_type_head_armor   ,0,
1 , weight(0.5)|abundance(100)|head_armor(1)|body_armor(1)|leg_armor(1) ,imodbits_cloth ],
["laurel_wearth", "Wearth of Laurels", [("raw_laurel",0)], itp_unique|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0,
1 , weight(0.1)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["minotaur_armor", "Stinky fur", [("fur_cape_4",0)], itp_unique| itp_type_body_armor |itp_force_show_body|itp_attach_armature|itp_civilian  ,0,
1, weight(42)|head_armor(0)|body_armor(1)|leg_armor(0)|difficulty(3) ,imodbits_armor, [],  ],

##amors arrow
["cupid_arrow","Cupid's arrow", [("flying_arrow",0)], itp_unique, 0,
15000,weight(0.5)|abundance(0)|max_ammo(1),imodbits_none],

["mithras","Mithras Statue", [("mithras_final",0),("mithras_final_inv",ixmesh_inventory)], itp_unique, 0,
100000,weight(150)|abundance(0)|max_ammo(1),imodbits_none],

["mirror_poppaea","Mirror", [("nothing",0),("mirror_poppaea",ixmesh_inventory)], itp_unique, 0,
100000,weight(150)|abundance(0)|max_ammo(1),imodbits_none],


["allat","Statue of Al-Lat", [("goddess_of_fertility",0),("goddess_of_fertility_inv",ixmesh_inventory)], itp_unique, 0,
250000,weight(150)|abundance(0)|max_ammo(1),imodbits_none],

["holy_grail","Cup of Chrestos", [("cup",0),], itp_unique, 0,
10,weight(0.25)|abundance(0)|max_ammo(1),imodbits_none],

#special germanic sword
["danish_longsword_2", "Ancient Germanic Longsword", [("danish_longsword_2",0),("danish_longsword_2_scab", ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary, itc_cleaver|itc_parry_onehanded|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
25000,
weight(get_w_weight(85))|difficulty(14)|spd_rtng(get_1hw_speed(85))|weapon_length(85)|swing_damage(34 , cut)|thrust_damage(0 ,  pierce),imodbits_sword_high, [], [] ],

#arminius items
["arminius_mask", "Decorated Galea", [("1_imperial_weiler",0)],itp_type_head_armor|itp_unique,0,
30000, weight(8)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_armor ],
["arminius_spatha", "Decorated Spatha", [("arminius_spatha",0),("arminius_spatha_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
30000,weight(get_w_weight(93))|difficulty(9)|spd_rtng(get_1hw_speed(93))|weapon_length(93)|swing_damage(29,cut)|thrust_damage(14,pierce), imodbits_sword_high, [], [] ],

##legendary bows
["thunder",         "Thunder", [("kritan_bow",0)], itp_unique|itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow,
50000 , weight(1.25)|difficulty(5)|spd_rtng(90) | shoot_speed(70) | thrust_damage(35 ,pierce)|accuracy(97),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["dragon",         "Dragon", [("parf_bow",0)], itp_unique|itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow,
50000 , weight(1.25)|difficulty(5)|spd_rtng(90) | shoot_speed(70) | thrust_damage(35 ,pierce)|accuracy(97),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["african_longbow",         "Nyame's Wrath", [("african_longbow2",0),("african_longbow2_carry",ixmesh_carry)], itp_unique|itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
25000 , weight(1.75)|difficulty(6)|spd_rtng(70) | shoot_speed(75) | thrust_damage(36 ,  pierce)|accuracy(96),imodbits_bow,[],[] ],

["dragon_arrows", "Dragon Arrows", [("parf_arrow",0),("parf_arrow_flying",ixmesh_flying_ammo),("parf_quiver",ixmesh_carry)], itp_unique|itp_type_arrows, itcf_carry_quiver_back_right,
3500, weight(3)|abundance(50)|weapon_length(91)|thrust_damage(7,pierce)|max_ammo(25), imodbits_missile ],
["thunder_arrows", "Thunder Arrows", [("kritan_arrow",0),("kritan_arrow_flying",ixmesh_flying_ammo),("kritan_arrow_qui",ixmesh_carry)], itp_unique|itp_type_arrows, itcf_carry_quiver_back_right,
3500, weight(3)|abundance(50)|weapon_length(91)|thrust_damage(7,pierce)|max_ammo(25), imodbits_missile ],


##legendary bows end

["linothorax_alexander", "Alexanders Linothorax", [("a_alexander",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0,
linothorax_armor_price,linothorax_armor,imodbits_armor,
 [(ti_on_init_item,[(call_script, "script_init_eastern_troop_2"),]),], [] ],

["alexanders_helm", "Alexanders Helm", [("h_hephaistion",0)], itp_unique| itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
15000, weight(2.5)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["armor_of_african_gods", "Strong Hamata with Lionskin", [("coat_of_the_gods",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_replaces_helm ,0,
15000, weight(4)|abundance(100)|head_armor(40)|body_armor(50)|leg_armor(10)|difficulty(25) ,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_roman_simple"),]),] ],

##egypt
["khopesh1", "Khopesh", [("Khopesh1",0)], itp_type_one_handed_wpn|itp_unique|itp_primary, itc_cleaver|itc_parry_onehanded|itcf_carry_sword_left_hip,
10000, weight(1.6)|difficulty(10)|spd_rtng(99)|weapon_length(90)|swing_damage(31 , cut)|thrust_damage(5,pierce),imodbits_sword_high ],

#jerusalem
["holy_lance",         "Hasta Longini", [("roman_spear_178",0)], itp_type_polearm|itp_offset_lance|itp_unique| itp_primary|itp_wooden_parry|itp_no_blur, itc_spear,
5000 , weight(2.5)|difficulty(12)|spd_rtng(100) | weapon_length(178)|swing_damage(36 , pierce) | thrust_damage(36 ,  pierce),imodbits_polearm, [], [] ],
#spain
["gallic_spear_4","Olyndicus Spear", [("gallic_spear_4", 0)], itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur, itc_spear,
4000, weight(2)|difficulty(12)|spd_rtng(100)|weapon_length(165)|thrust_damage(34, pierce)|swing_damage(34, pierce), imodbits_polearm, []],

##augustus things
["ancient_spatha", "Decorated Spatha", [("ancient_spatha",0),("ancient_spatha_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary,
itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
6000,weight(get_w_weight(87))|difficulty(9)|spd_rtng(get_1hw_speed(87))|weapon_length(87)|swing_damage(29,cut)|thrust_damage(14,pierce), imodbits_sword_high, [], [] ],

["augustus_armor", "Lorica Musculata Augusti", [("armor_augustus",0)], itp_unique| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
150000, weight(42)|head_armor(0)|body_armor(55)|leg_armor(12)|difficulty(16) ,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),],  ],

#quests
["aslans_fur", "Aslan's Fur", [("aslans_fur",0)], itp_unique | itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_doesnt_cover_hair,0,
30000, weight(5)|head_armor(30)|body_armor(20)|leg_armor(5)|difficulty(10) ,imodbits_cloth, [], [] ],

["ancient_helm_light", "Ancient Helm", [("lplume_helm1",0)], itp_unique | itp_type_head_armor,0,
30000, weight(5)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth, [], [] ],

["ancient_helm_heavy", "Ancient Helm", [("btusk_helm2",0)], itp_unique|itp_type_head_armor,0,
60000, weight(8)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate, [], [] ],

["ancient_boots_heavy", "Ancient Armored Caliga", [("brgreaves1",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
25000, weight(4)|head_armor(0)|body_armor(0)|leg_armor(34)|difficulty(12) ,imodbits_plate ],

["ancient_plate_armor", "Ancient Plate Armor", [("corselet1",0)], itp_unique| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
100000, weight(42)|head_armor(0)|body_armor(55)|leg_armor(12)|difficulty(19) ,imodbits_armor,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),],  ],

["ancient_plate_armor2", "Ancient Plate Armor", [("corselet2",0)], itp_unique| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
100000, weight(42)|head_armor(0)|body_armor(55)|leg_armor(12)|difficulty(19) ,imodbits_armor,
[(ti_on_init_item,[
(call_script, "script_init_armor_merc"),]),], [] ],

["ancient_leather_armor", "Ancient Leather Armor", [("lcuirass1",0)], itp_unique| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
70000 , weight(25)|head_armor(0)|body_armor(46)|leg_armor(6)|difficulty(12) ,imodbits_cloth,
[(ti_on_init_item,[(call_script, "script_init_armor_merc"),]),],  ],

["ancient_spear", "Ancient Spear", [("spear1",0)], itp_type_polearm|itp_offset_lance|itp_unique| itp_primary|itp_wooden_parry|itp_has_upper_stab|itp_no_blur, itc_spear,
25000 , weight(5)|difficulty(12)|spd_rtng(101) | weapon_length(160)|swing_damage(36 , pierce) | thrust_damage(36 ,  pierce),imodbits_polearm ],

["ancient_axe", "Ancient Axe", [("braxe1",0)], itp_type_one_handed_wpn|itp_unique| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry|itp_no_blur, itc_scimitar|itcf_carry_axe_left_hip,
50000, weight(5)|difficulty(17)|spd_rtng(80) | weapon_length(65)|swing_damage(38, cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["ancient_sword", "Ancient Shortsword", [("shortsword1",0),("shortsword1_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_unique|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
50000, weight(2.5)|difficulty(10)|spd_rtng(95)|weapon_length(70)|swing_damage(33,cut)|thrust_damage(33,pierce), imodbits_sword_high, [], [] ],

# ["perseus_sword", "Perseus Sword", [("perseus_sword",0),], itp_type_one_handed_wpn|itp_unique|itp_primary, itc_longsword,
# 50000, weight(2.5)|difficulty(10)|spd_rtng(95)|weapon_length(70)|swing_damage(33,cut)|thrust_damage(33,pierce), imodbits_sword_high, [], [] ],

["ancient_shield", "Ancient Shield", [("brshield1",0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
60000, weight(6)|hit_points(800)|body_armor(shield_armor_t4)|spd_rtng(90)|shield_width(60)|difficulty(4),imodbits_shield ],

["anti_fooling_paint","Farbius anti-fouling paint", [("ale_barrel",0)], itp_unique|itp_type_goods, 0,
10000,weight(120)|max_ammo(200),imodbits_none],

["aegis", "Aegis", [("aegis",0)], itp_unique|itp_type_shield|itp_wooden_parry, 0,
60000,weight(8)|hit_points(1000)|body_armor(shield_armor_t4)|spd_rtng(90)|shield_width(110)|difficulty(5),imodbits_shield ],

["caesars_sword", "Crocea Mors", [("roman_rich_gladius_57",0),("roman_rich_gladius_57_scabbard",ixmesh_carry)],
itp_type_one_handed_wpn|itp_unique|itp_primary|itp_next_item_as_melee|itp_extra_penetration, itc_gladius|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
25000, weight(1.3)|difficulty(10)|spd_rtng(99)|weapon_length(59)|swing_damage(33,pierce)|thrust_damage(33,pierce), imodbits_sword_high, [], [] ],

["caesars_sword_melee", "Crocea Mors", [("roman_rich_gladius_57",0),("roman_rich_gladius_57_scabbard",ixmesh_carry)],
itp_type_one_handed_wpn|itp_unique|itp_primary, itc_gladius_2|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,
25000, weight(1.3)|difficulty(10)|spd_rtng(99)|weapon_length(59)|swing_damage(21,cut)|thrust_damage(33,pierce), imodbits_sword_high, [], [] ],
##special items end

["maske", "Mask with Cloak", [("maske",0)],itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_unique,0,
5000 , weight(3)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor ],

#vitellius
["roman_rich_vitellius", "Toga Overweight Edition", [("aristocrats_cloth_vitellius",0)],itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price,roman_rich_armor,imodbits_cloth, [], [] ],

["roman_noble_dress_7_fat", "Roman Noble Dress Overweight Edition", [("roman_noble_dress_pink2_fat",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms3_fat"),
    ]),
], [fac_culture_7] ],

##wild animals for hunting
["animal_boar","Boar", [("boar",0),("boar_2",imodbit_cracked)],	itp_disable_agent_sounds, 0,
10,abundance(10)|hit_points(45)|body_armor(18)|difficulty(0)|horse_speed(55)|horse_maneuver(150)|horse_charge(30)|horse_scale(70),imodbits_horse_basic],
["animal_dear","Dear", [("dear_1",0),("dear_2",imodbit_cracked)],	itp_disable_agent_sounds, 0,
10,abundance(10)|hit_points(90)|body_armor(12)|difficulty(0)|horse_speed(45)|horse_maneuver(46)|horse_charge(20)|horse_scale(90),imodbits_horse_basic],

["animal_wolf","Wolf", [("wolf",0),],	itp_disable_agent_sounds|itp_type_horse, 0,
10, abundance(10)|body_armor(20)|difficulty(1)|hit_points(50)|horse_maneuver(70)|horse_speed(47)|horse_charge(30)|horse_scale(75), imodbits_horse_basic, []],
["wild_elephant","Wild Elephant", [("wild_elephant", 0)], itp_disable_agent_sounds|itp_type_horse, 0,
10, abundance(10)|body_armor(53)|difficulty(1)|hit_points(500)|horse_maneuver(40)|horse_speed(30)|horse_charge(1500)|horse_scale(200), imodbits_horse_basic, []],
["wild_lion","Lion", [("berber_lion", 0)], itp_disable_agent_sounds|itp_type_horse, 0,
10, abundance(10)|body_armor(25)|difficulty(1)|hit_points(250)|horse_maneuver(60)|horse_speed(45)|horse_charge(50)|horse_scale(105), imodbits_horse_basic, []],
["wild_lion_2","Leopard", [("leopard", 0)], itp_disable_agent_sounds|itp_type_horse, 0,
10, abundance(10)|body_armor(25)|difficulty(1)|hit_points(250)|horse_maneuver(65)|horse_speed(50)|horse_charge(40)|horse_scale(96), imodbits_horse_basic, []],
##wild animals for hunting end

["female_slave1", "Dancers Outfit", [("slave_roba",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],

["female_slave2", "Dancers Outfit", [("slave_roba1",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],
["female_slave3", "Dancers Outfit", [("slave_roba2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],
["female_slave4", "Dancers Outfit", [("slave_roba3",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],

##augusta dresses
["roman_female_augusta", "Fancy Dress", [("new_dress_augusta",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
roman_rich_armor_price*3,rich_dress_r_armor,imodbits_none, [
(ti_on_init_item,[
    (cur_item_add_mesh, "str_braclets_3"),
    (cur_item_add_mesh, "str_braclets_4"),
    (cur_item_add_mesh, "str_braclets_2"),
    (call_script, "script_init_dress_arms2"), ]),
], [fac_culture_7] ],
["roman_female_augusta_2", "Dress", [("new_dress_augusta_3",0)], itp_unique|itp_type_body_armor|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],

["saka_dress", "Saka Royal Dress", [("saka_dress",0)], itp_unique|itp_type_body_armor|itp_covers_legs,0,
roman_rich_armor_price*3,rich_dress_r_armor,imodbits_none,
 [(ti_on_init_item,[  (call_script, "script_init_dress_no_arms"),]), ], []],
["saka_crown", "Saka Crown", [("saka_crown",0)], itp_unique|itp_type_head_armor,0,
15000, weight(2.5)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["seiden_dress", "Silk Dress", [("new_dress_augusta_2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
rich_dress_r_armor_price,rich_dress_r_armor,imodbits_none,
[(ti_on_init_item,[(cur_item_add_mesh, "str_braclets_2"),
(call_script, "script_init_dress_boobs_new"),
]), ],[] ],

#emperor tunics
["roman_rich_emperor", "Toga Picta", [("aristocrats_cloth_pruple",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price*2,roman_rich_armor,imodbits_none, [(ti_on_init_item,
[(call_script, "script_init_roman_rich2"),]),], [fac_culture_7] ],
["roman_rich_emperor_2", "Toga Picta", [("aristocrats_cloth_pruple_2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
roman_rich_armor_price*2,roman_rich_armor,imodbits_none, [(ti_on_init_item,
[(call_script, "script_init_roman_rich2"),]),], [fac_culture_7] ],

##item for tavern goers
["dedal_kufel","Cup",[("dedal_kufelL",0)],	itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand|itp_civilian,0,
1,weight(1),0],
##item for tavern goers end
##invisible items
["nothing_body", "nothing", [("nothing_rig",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["nothing_head", "nothing", [("nothing_rig",0)],  itp_type_head_armor |itp_covers_head |itp_civilian |itp_attach_armature,0,
1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nothing_legs", "nothing", [("nothing_rig",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["nothing_hands","nothing",[("nothing",0)],	itp_type_hand_armor,0,0,weight(1),0],
##invisible items end
["banner_background1","Banner", [("background_banner_01",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none, [
(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),
(store_trigger_param_2, ":troop_no"),
(call_script, "script_shield_item_set_banner", "tableau_custom_banner_default", ":agent_no", ":troop_no")])]],
["banner_background2","Banner", [("background_banner_02",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none, [
(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),
(store_trigger_param_2, ":troop_no"),
(call_script, "script_shield_item_set_banner", "tableau_custom_banner_default", ":agent_no", ":troop_no")])]],

##for min workers
["pickaxe_work","Pickaxe",[("pickaxe_work2_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],

##for min workers end

["guard_hasta","Hasta and Scutum",[("guard_hasta_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],
["guard_scutum","Scutum",[("guard_scutum_L",0)],itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand,0,0,weight(1),0],

##For olympia
["throwing_spears_olymp",         "Throwing Spears", [("atgeirr1",0)], itp_type_thrown|itp_primary|itp_secondary|itp_bonus_against_shield ,itcf_throw_javelin,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(25) | thrust_damage(28 ,  pierce)|max_ammo(1)|weapon_length(85)|accuracy(100),imodbits_thrown,
[(ti_on_missile_hit, # when missile hits
   [
    (store_trigger_param_1, ":stepper"),

    (set_fixed_point_multiplier, 1),
    (agent_get_position,pos2,":stepper"),
    (get_distance_between_positions,reg19,pos1,pos2),
    (agent_get_troop_id, ":troop", ":stepper"),
    (str_store_troop_name, s1, ":troop"),
    (display_message, "@{s1} has thrown his spear {reg19} units far."),
    (troop_set_slot, "trp_temp_array_a", ":stepper", reg19),

    (try_begin),
      (gt, reg19, "$temp3"),
      (assign, "$temp2", ":stepper"),
      (assign, "$temp3", reg19),
    (try_end),
    (val_add, "$temp4", 1),
   ]),
] ], #cambiado chief
["discus",         "Discus", [("discus",0)], itp_type_thrown|itp_primary|itp_secondary ,itcf_throw_knife,
425 , abundance(80)|weight(2)|difficulty(2)|spd_rtng(85)|shoot_speed(11) | thrust_damage(28 ,  blunt)|max_ammo(1)|weapon_length(85)|accuracy(100),imodbits_thrown,
[(ti_on_missile_hit, # when missile hits
   [
    (store_trigger_param_1, ":stepper"),

    (set_fixed_point_multiplier, 1),
    (agent_get_position,pos2,":stepper"),
    (get_distance_between_positions,reg19,pos1,pos2),
    (agent_get_troop_id, ":troop", ":stepper"),
    (str_store_troop_name, s1, ":troop"),
    (display_message, "@{s1} has thrown his spear {reg19} units far."),
    (troop_set_slot, "trp_temp_array_a", ":stepper", reg19),

    (try_begin),
      (gt, reg19, "$temp3"),
      (assign, "$temp2", ":stepper"),
      (assign, "$temp3", reg19),
    (try_end),
    (val_add, "$temp4", 1),
   ]),
] ], #cambiado chief
["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],##important for find item cheat, everything after this wont appear in find items cheat

]
append_noswing_items(items)