import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from IDs.ID_factions import *
from IDs.ID_items import *
from IDs.ID_scenes import *

#from compiler import *
####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#  str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  n |= wp_firearm(x)#slings
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   n |= wp_firearm(a)#slings
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x - 20)
  n |= wp_polearm(x + 10)
  n |= wp_throwing(x - 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_9 | agi_6 | int_4 | cha_4
attrib_second_outfit = str_30 | agi_5 | int_4 | cha_4

hero_attrib = str_30 | agi_30 | int_15 | cha_20

knows_hero = knows_weapon_master_10|knows_riding_10|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_power_throw_10|knows_power_draw_10|knows_shield_10|knows_looting_10

attrib_level_6 = str_14|agi_8|int_12|cha_12|level(6)

attrib_level_12 = str_16|agi_8|int_12|cha_12|level(12)
attrib_level_12_warrior = str_17|agi_9|int_12|cha_12|level(12)

attrib_level_16 = str_16|agi_9|int_12|cha_12|level(16)
attrib_level_16_warrior = str_17|agi_10|int_12|cha_12|level(16)

attrib_level_18 = str_17|agi_9|int_12|cha_12|level(18)
attrib_level_18_warrior = str_18|agi_10|int_12|cha_12|level(18)

attrib_level_20 = str_18|agi_9|int_12|cha_12|level(20)
attrib_level_20_warrior = str_19|agi_10|int_12|cha_12|level(20)

attrib_level_23 = str_18|agi_9|int_12|cha_12|level(23)
attrib_level_23_warrior = str_19|agi_10|int_12|cha_12|level(23)

attrib_level_26 = str_19|agi_10|int_12|cha_12|level(26)
attrib_level_26_warrior = str_20|agi_11|int_12|cha_12|level(26)

attrib_level_29 = str_20|agi_10|int_12|cha_12|level(29)
attrib_level_29_warrior = str_21|agi_11|int_12|cha_12|level(29)

attrib_level_31 = str_21|agi_11|int_12|cha_12|level(31)
attrib_level_31_warrior = str_22|agi_12|int_12|cha_12|level(31)

attrib_common_lady = str_9|agi_9|int_14|cha_16|level(15)
knows_common_lady = knows_persuasion_4|knows_leadership_4|knows_first_aid_3|knows_surgery_2|knows_wound_treatment_2|knows_riding_6

#lvl6
knows_level_6 = knows_weapon_master_3|knows_ironflesh_2|knows_athletics_1|knows_power_strike_1|knows_shield_3|knows_inventory_management_10|knows_power_throw_2|knows_power_draw_2|knows_horse_archery_2
#lvl12
knows_level_12 = knows_weapon_master_5|knows_ironflesh_4|knows_athletics_1|knows_power_strike_2|knows_shield_5|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
knows_level_12_warrior = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_1|knows_power_strike_4|knows_shield_5|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
#lvl12
knows_level_16 = knows_weapon_master_6|knows_ironflesh_4|knows_athletics_2|knows_power_strike_2|knows_shield_6|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
knows_level_16_warrior = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_2|knows_power_strike_5|knows_shield_6|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
#lvl18
knows_level_18 = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_2|knows_riding_2|knows_power_strike_3|knows_shield_6|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
knows_level_18_warrior = knows_weapon_master_6|knows_ironflesh_6|knows_athletics_2|knows_riding_2|knows_power_strike_6|knows_shield_6|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
#lvl20
knows_level_20 = knows_weapon_master_6|knows_ironflesh_6|knows_athletics_3|knows_riding_3|knows_power_strike_3|knows_shield_7|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
knows_level_20_warrior = knows_weapon_master_6|knows_ironflesh_6|knows_athletics_3|knows_riding_3|knows_power_strike_6|knows_shield_7|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3
#lvl23
knows_level_23 = knows_weapon_master_7|knows_ironflesh_6|knows_athletics_3|knows_riding_3|knows_power_strike_4|knows_shield_7|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3  #40+24 / 2 +4
knows_level_23_warrior = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_3|knows_riding_3|knows_power_strike_7|knows_shield_7|knows_inventory_management_10|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_3  #40+24 / 2 +4
#lvl26
knows_level_26 = knows_weapon_master_8|knows_ironflesh_7|knows_athletics_4|knows_riding_5|knows_power_strike_5|knows_shield_8|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_3 #40+26 / 2 +6
knows_level_26_warrior = knows_weapon_master_8|knows_ironflesh_7|knows_athletics_4|knows_riding_5|knows_power_strike_7|knows_shield_8|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_3 #40+26 / 2 +6
#lvl29
knows_level_29 = knows_weapon_master_9|knows_ironflesh_8|knows_athletics_4|knows_riding_6|knows_power_strike_6|knows_shield_9|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_4 ##40+30 / 2 +8
knows_level_29_warrior = knows_weapon_master_9|knows_ironflesh_8|knows_athletics_4|knows_riding_6|knows_power_strike_8|knows_shield_9|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_4 ##40+30 / 2 +8
#lvl31
knows_level_31 = knows_weapon_master_10|knows_ironflesh_8|knows_athletics_5|knows_riding_7|knows_power_strike_7|knows_shield_10|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_4 ###40+32 / 2 +12
knows_level_31_warrior = knows_weapon_master_10|knows_ironflesh_9|knows_athletics_5|knows_riding_7|knows_power_strike_9|knows_shield_10|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_4 ###40+32 / 2 +12

knows_archer_basic = knows_weapon_master_3|knows_ironflesh_4|knows_athletics_5|knows_riding_3|knows_power_strike_2|knows_shield_2|knows_inventory_management_10|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_3
knows_archer_exp = knows_weapon_master_4|knows_ironflesh_5|knows_athletics_6|knows_riding_4|knows_power_strike_3|knows_shield_3|knows_inventory_management_10|knows_power_throw_5|knows_power_draw_5|knows_horse_archery_4
knows_archer_elit = knows_weapon_master_5|knows_ironflesh_6|knows_athletics_7|knows_riding_5|knows_power_strike_4|knows_shield_4|knows_inventory_management_10|knows_power_throw_5|knows_power_draw_6|knows_horse_archery_5

knows_archer_basic_eastern = knows_weapon_master_5|knows_ironflesh_4|knows_athletics_6|knows_riding_4|knows_power_strike_2|knows_shield_3|knows_inventory_management_10|knows_power_throw_5|knows_power_draw_5|knows_horse_archery_6
knows_archer_exp_eastern = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_7|knows_riding_5|knows_power_strike_3|knows_shield_4|knows_inventory_management_10|knows_power_throw_6|knows_power_draw_6|knows_horse_archery_8
knows_archer_elit_eastern = knows_weapon_master_7|knows_ironflesh_6|knows_athletics_7|knows_riding_6|knows_power_strike_4|knows_shield_5|knows_inventory_management_10|knows_power_throw_6|knows_power_draw_7|knows_horse_archery_10

knows_horseman_eastern = knows_weapon_master_8|knows_ironflesh_7|knows_athletics_6|knows_riding_8|knows_power_strike_4|knows_shield_5|knows_inventory_management_10|knows_power_throw_7|knows_power_draw_7|knows_horse_archery_8

knows_lord_1 = knows_weapon_master_2|knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7|knows_horse_archery_2

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2|knows_leadership_1|knows_looting_1
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_5|knows_persuasion_2
knows_tracker_npc = knows_weapon_master_1|knows_athletics_6|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2|knows_power_strike_1
knows_veteran_npc = knows_weapon_master_8|knows_athletics_8|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_8|knows_power_strike_6|knows_shield_7|knows_power_draw_2|knows_power_throw_4|knows_tactics_5|knows_leadership_7|knows_riding_4|knows_looting_2|knows_engineer_2|knows_prisoner_management_2|knows_inventory_management_3

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_22|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_24|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_26|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_28|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_30|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_weapon_master_2|knows_riding_4|knows_ironflesh_2|knows_power_strike_2|knows_athletics_3|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3|knows_horse_archery_3|knows_inventory_management_5
knight_skills_2 = knows_weapon_master_4|knows_riding_5|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_horse_archery_4|knows_inventory_management_6
knight_skills_3 = knows_weapon_master_6|knows_riding_6|knows_ironflesh_6|knows_power_strike_6|knows_athletics_5|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_horse_archery_5|knows_inventory_management_7
knight_skills_4 = knows_weapon_master_8|knows_riding_7|knows_ironflesh_8|knows_power_strike_8|knows_athletics_6|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_horse_archery_6|knows_inventory_management_8
knight_skills_5 = knows_weapon_master_10|knows_riding_8|knows_ironflesh_10|knows_power_strike_10|knows_athletics_7|knows_tactics_6|knows_prisoner_management_4|knows_leadership_9|knows_horse_archery_7|knows_inventory_management_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.

#generic faces codes
eastern_man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
eastern_man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
eastern_man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
eastern_man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
eastern_man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

eastern_man_face_younger_2 = 0x000000003f0031894deeffffffffffff00000000001efff90000000000000000
eastern_man_face_young_2   = 0x00000003bf0031894deeffffffffffff00000000001efff90000000000000000
eastern_man_face_middle_2  = 0x00000007bf0031894deeffffffffffff00000000001efff90000000000000000
eastern_man_face_old_2     = 0x0000000bff0031894deeffffffffffff00000000001efff90000000000000000
eastern_man_face_older_2   = 0x0000000fff0031894deeffffffffffff00000000001efff90000000000000000


nubian_man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nubian_man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nubian_man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nubian_man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nubian_man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nubian_man_face_younger_2 = 0x000000003f0051094deeffffffffffff00000000001efff90000000000000000
nubian_man_face_young_2   = 0x00000003bf0051094deeffffffffffff00000000001efff90000000000000000
nubian_man_face_middle_2  = 0x00000007bf0051094deeffffffffffff00000000001efff90000000000000000
nubian_man_face_old_2     = 0x0000000bff0051094deeffffffffffff00000000001efff90000000000000000
nubian_man_face_older_2   = 0x0000000fff0051094deeffffffffffff00000000001efff90000000000000000


north_african_man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
north_african_man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
north_african_man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
north_african_man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
north_african_man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000


north_african_man_face_younger_2 = 0x000000003f0051094deeffffffffffff00000000001efff90000000000000000
north_african_man_face_young_2   = 0x00000003bf0051094deeffffffffffff00000000001efff90000000000000000
north_african_man_face_middle_2  = 0x00000007bf0051094deeffffffffffff00000000001efff90000000000000000
north_african_man_face_old_2     = 0x0000000bff0051094deeffffffffffff00000000001efff90000000000000000
north_african_man_face_older_2   = 0x0000000fff0051094deeffffffffffff00000000001efff90000000000000000


barbarian_man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
barbarian_man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
barbarian_man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
barbarian_man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
barbarian_man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000


barbarian_man_face_younger_2 = 0x000000003f0053884deeffffffffffff00000000001efff90000000000000000
barbarian_man_face_young_2   = 0x00000003bf0053884deeffffffffffff00000000001efff90000000000000000
barbarian_man_face_middle_2  = 0x00000007bf0053884deeffffffffffff00000000001efff90000000000000000
barbarian_man_face_old_2     = 0x0000000bff0053884deeffffffffffff00000000001efff90000000000000000
barbarian_man_face_older_2   = 0x0000000fff0053884deeffffffffffff00000000001efff90000000000000000

reserved = 0

no_scene = 0

roman_face1 = 0x00000000ff000004364000000020000000000000001c00800000000000000000
roman_face2 = 0x000000071b00300636eeffffffffffff00000000001efff90000000000000000

nubian_face1 = 0x000000003f007140124000000020000000000000001c00800000000000000000
nubian_face2 = 0x0000000d7f0070005beeffffffffffff00000000001efff90000000000000000

african_face_younger = 0x000000003f00e000124000000020000000000000001c00800000000000000000
african_face_older	 = 0x0000000bff01028f6deeffffffffffff00000000001efff90000000000000000

african_face_female	 = 0x000000018000c042000000000000000000000000001c00000000000000000000
african_face_female2	 = 0x00000001bf00e0467fffffffffe0000000000000001fffff0000000000000000

arab_face_young  = 0x000000000010b14e364000000020000000000000001c00800000000000000000
arab_face_old	 = 0x00000009bf10d35136eeffffffffffff00000000001efff90000000000000000

arab_face_female	 = 0x0000000180008041000000000000000000000000001c00000000000000000000
arab_face_female2	 = 0x00000001bf00b0467fffffffffe0000000000000001fffff0000000000000000

parthian_face_young      = 0x000000000000a044124000000020000000000000001c00800000000000000000
parthian_face_middle	 = 0x000000003f00d2cf5beeffffffffffff00000000001efff90000000000000000

persian_face_young   = 0x000000003f00114d124000000020000000000000001c00800000000000000000
persian_face_middle	 = 0x000000003f0043516deeffffffffffff00000000001efff90000000000000000

armenian_face_young      = 0x000000002e012002124000000020000000000000001c00800000000000000000
armenian_face_middle	 = 0x000000003f01358d6deeffffffffffff00000000001efff90000000000000000

scythian_face_11        = 0x000000003f00014d364000000020000000000000001c00800000000000000000
scythian_face_12        = 0x00000000000042d136eeffffffffffff00000000001efff90000000000000000

scythian_face_21        = 0x000000000000c581244000000020000000000000001c00800000000000000000
scythian_face_22        = 0x000000003f00d0053beeffffffffffff00000000001efff90000000000000000

celtic_face_11          = 0x000000000d000041124000000020000000000000001c00800000000000000000
celtic_face_12          = 0x000000002300530b5beeffffffffffff00000000001efff90000000000000000

celtic_face_21 =          0x0000000d0b01130b224000000020000000000000001c00800000000000000000
celtic_face_22 =          0x0000000caa0135926deeffffffffffff00000000001efff90000000000000000


germanic_face_11        = 0x000000000001130a244000000020000000000000001c00800000000000000000
germanic_face_12        = 0x0000000d340135926deeffffffffffff00000000001efff90000000000000000

germanic_face_21        = 0x0000000140000101264000000020000000000000001c00800000000000000000
germanic_face_22        = 0x0000000bad00430b5beeffffffffffff00000000001efff90000000000000000

white_face_11           = 0x0000000780000001124000000020000000000000001c00800000000000000000
white_face_12           = 0x00000007bf0055d26deeffffffffffff00000000001efff90000000000000000

white_face_21           = 0x0000000780011001124000000020000000000000001c00800000000000000000
white_face_22           = 0x00000007bf0135d26deeffffffffffff00000000001efff90000000000000000

mercenary_face_greek_1 =  0x0000000000012001244000000020000000000000001c00800000000000000000
mercenary_face_greek_2 =  0x00000000000123475beeffffffffffff00000000001efff90000000000000000

bandit_face1            = 0x0000000400000001124000000020000000000000001c00800000000000000000
bandit_face2            = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

#woman faces
woman_face_1    = 0x0000000180000041000000000000000000000000001c00000000000000000000
woman_face_2    = 0x0000000a000070460fffffffffffffff00000000001c00000000000000000000

swadian_woman_face_1 = 0x0000000180000041000000000000000000000000001c00000000000000000000
swadian_woman_face_2 = 0x0000000a000070460fffffffffffffff00000000001c00000000000000000000

khergit_woman_face_1 = 0x0000000180000041000000000000000000000000001c00000000000000000000
khergit_woman_face_2 = 0x0000000a000070460fffffffffffffff00000000001c00000000000000000000

dancer_face1 = 0x0000000000000081349249249249249200000000001db6db0000000000000000
dancer_face2 = 0x00000000000071dd5b6db2db6db6db6d00000000001edb6d0000000000000000

dancer_face_african1 = 0x000000000000c041249249249249249200000000001d24920000000000000000
dancer_face_african2 = 0x000000003f00e19d5b6db6db6db6db6d00000000001edb6d0000000000000000

dancer_face_eastern1 = 0x0000000000008041249249249249249200000000001d24920000000000000000
dancer_face_eastern2 = 0x00000001bf00c0dd5b6db6db6db6db6d00000000001f5b6d0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

#more generic faces
mercenary_face_1 = white_face_11
mercenary_face_2 = white_face_12

saka_face_1 = 0x0000000000008001249249249249249200000000001d24920000000000000000
saka_face_2 = 0x00000009bf00940a5b6db6db6db6db6d00000000001edb6d0000000000000000

saka_face_female_1 = 0x000000003308608127db6db6db49b6da00000000001db49a0000000000000000
saka_face_female_2 = 0x000000003f08708a5bedb6d96db6db6a00000000001ec9240000000000000000


tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
tf_guarantee_soldier = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm

#music instuments
bosporan_standards = [itm_battle_standard]
judean_standards = [itm_battle_standard]
celtic_standards = [itm_battle_standard]
germanic_standards = [itm_battle_standard]
armenian_standards = [itm_battle_standard]
parthian_standards = [itm_battle_standard]
caucasian_standards = [itm_battle_standard]
dacian_standards = [itm_battle_standard]

bosporan_horns = [itm_horn]
judean_horns = [itm_trumpet_eastern]
celtic_horns = [itm_trumpet_celtic]
germanic_horns = [itm_horn]
armenian_horns = [itm_trumpet_eastern]
parthian_horns = [itm_trumpet_eastern]
caucasian_horns = [itm_trumpet_eastern]
dacian_horns = [itm_horn]

jew_shields_simple = [itm_eastern_shield_inf_light5,itm_eastern_shield_inf_light6,itm_eastern_shield_inf_light1,itm_eastern_shield_inf_light2,itm_eastern_shield_inf_light3,itm_eastern_shield_inf_light4]
jew_shields_large = [itm_judean_shield_large_1,itm_judean_shield_large_2,itm_judean_shield_large_3,itm_judean_shield_large_4]
jew_shields_poor = [itm_ad_mixed_round_shields_14,itm_ad_mixed_round_shields_13,itm_ad_mixed_round_shields_08,itm_ad_mixed_round_shields_07]

celtic_painted_1 = [itm_celts_painted1,itm_celts_painted2,itm_celts_painted3,
itm_celts_painted4,itm_celts_painted5,itm_celts_painted6,itm_celts_painted7,itm_celts_painted8,
itm_celts_painted9,itm_celts_painted10,itm_celts_painted11,itm_celts_painted12]

celtic_helmet_coolus_old = [itm_britton_coolus,itm_britton_coolus_2]
celtic_helmet_coolus_new = [itm_britton_coolus_new,itm_britton_coolus_new_2,itm_britton_coolus_plume]

celtic_mail_normal = [
itm_celtic_heavy1,itm_celtic_heavy2,itm_celtic_heavy3,itm_celtic_heavy4]

celtic_mail_noble = [itm_celtic_noble_1,itm_celtic_noble_2,itm_celtic_noble_3,itm_celtic_noble_4]

celtic_tunics_1 = [itm_celtic_light1,itm_celtic_light2,itm_celtic_light3,itm_celtic_light4,itm_celtic_light5,itm_celtic_light12]
celtic_tunics_2 = [itm_celtic_light6,itm_celtic_light7,itm_celtic_light8,itm_celtic_light9,itm_celtic_light10,itm_celtic_light11]

celtic_pants_1 = [itm_celtic_naked1,itm_celtic_naked2,itm_celtic_naked3,itm_celtic_naked4,itm_celtic_naked5]
celtic_pants_2 = [itm_celtic_naked6,itm_celtic_naked7,itm_celtic_naked8,itm_celtic_naked9,itm_celtic_naked10]
celtic_pants_3 = [itm_celtic_naked11,itm_celtic_naked12,itm_celtic_naked13,itm_celtic_naked14,itm_celtic_naked15]

caledonian_axes = [itm_caledonian_axe1,itm_caledonian_axe2]
celtic_axes = [itm_celtic_axe1,itm_celtic_axe2,itm_celtic_axe3,itm_celtic_axe4]
#for lords: itm_britton_helm_noble, itm_britton_helm_noble_2

celtic_swords = [itm_celtic_sowrd1,itm_celtic_sowrd2]
celtic_swords_noble = [itm_celtic_sowrd3,itm_celtic_spatha]

irish_swords = [itm_irish_sword]

celtic_spear = [itm_gallic_spear_2,itm_gallic_spear_3]

celtic_helmet_1 = [itm_britton_helm1,itm_britton_helm4,itm_britton_helm5,itm_britton_helm1_plume,itm_britton_helm4_plume,itm_britton_helm5_plume,
itm_britton_helm6,
]
celtic_helmet_2 = [itm_britton_helm2,itm_britton_helm3,itm_britton_helm2_plume,itm_britton_helm3_plume,]

caledonian_shield = [itm_pict_square_shield_1,itm_pict_square_shield_2,itm_pict_square_shield_3,itm_pict_square_shield_4,itm_pict_square_shield_5]
caledonian_shield_h = [itm_caledonian_h_shield1,itm_caledonian_h_shield2,itm_caledonian_h_shield3,itm_caledonian_h_shield4,itm_caledonian_h_shield5]

celtic_shield_long = [itm_celtic_long_shild1,itm_celtic_long_shild2, itm_celtic_long_shild3]
celtic_shield_round = [itm_celtic_round_shild1,itm_celtic_round_shild2,itm_celtic_round_shild3,itm_celtic_round_shild4]
celtic_shield_weird_1 = [itm_celtic_weird_shield_1,itm_celtic_weird_shield_6,itm_celtic_weird_shield_2,itm_celtic_weird_shield_7,itm_celtic_weird_shield_8]
celtic_shield_weird_2 = [itm_celtic_weird_shield_4,itm_celtic_weird_shield_9,itm_celtic_weird_shield_5,itm_celtic_weird_shield_10,itm_celtic_weird_shield_3]

celtic_hex_shield = [itm_celtic_shield_large1,itm_celtic_shield_large2,itm_celtic_shield_large3,itm_celtic_shield_large4,itm_celtic_shield_large5,itm_celtic_shield_large6]
celtic_oval_shield = [itm_celtic_shield_large7,itm_celtic_shield_large8,itm_celtic_shield_large9,itm_celtic_shield_large10,itm_celtic_shield_large11,itm_celtic_shield_large12]

irish_shield = [itm_irish_shield_1,itm_irish_shield_2,itm_irish_shield_3,itm_irish_shield_4]

celtic_throwing = [itm_jarid_celt,itm_throwing_spears]

celtic_bow_1 = [itm_short_bow,itm_arrows]
celtic_bow_2 = [itm_war_bow,itm_arrows]

jew_swords     = [itm_old_gladius_2]
jew_swords_old = [itm_old_gladius_1]
jew_spears = [itm_old_spear_1,itm_old_spear_2]

jew_tunics_1 = [itm_judean_tunic_4,itm_judean_tunic_5,itm_judean_tunic_6]
jew_tunics_2 = [itm_judean_tunic_1,itm_judean_tunic_2,itm_judean_tunic_3]
jew_robes = [itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b,itm_sarranid_cloth_robe_c]

jew_helm_cloth = [itm_headcloth,itm_eastern_helm1,itm_eastern_helm2,itm_eastern_helm3,itm_eastern_helm4]
jew_helm_light = [itm_roman_aux_helm_old_1, itm_roman_aux_helm_old_2,itm_roman_aux_helm_2]
jew_helm_heavy = [itm_roman_aux_helm_8,itm_roman_aux_helm_11,itm_roman_townguard_helm,itm_roman_aux_helm_3,itm_roman_aux_helm_2]
jew_boots_simple = [itm_eastern_shoe_y,itm_eastern_shoe_b,itm_eastern_shoe,itm_graves_simple]
jew_boots_heavy = [itm_centurio_east_graves,itm_centurio_west_graves,itm_graves_simple_2]

jew_mail_1  = [itm_judean_mail_4, itm_judean_mail_5, itm_judean_mail_6]
jew_mail_2  = [itm_judean_mail_1, itm_judean_mail_2, itm_judean_mail_3]
jew_scale = [itm_judean_scale_1,itm_judean_scale_2]

old_roman_roundshields = [itm_old_round_shield_1,itm_old_round_shield_2,itm_old_round_shield_3,itm_old_round_shield_4,itm_old_round_shield_5]

roman_eastern_scale = [itm_auxilia_squamata_east_1,itm_auxilia_squamata_east_3]

parthian_helm_cataphract = [itm_cataphract_helm1, itm_cataphract_helm2,itm_cataphract_helm4,itm_cataphract_helm6,itm_cataphract_helm7]
parthian_helm_sallet = [itm_cataphract_sallet_1, itm_cataphract_sallet_2]
parthian_helm_cavalry = [itm_parthian_helm_cavalry_1, itm_parthian_helm_cavalry_2,itm_parthian_helm_cavalry_3]
parthian_helm_cavalry_heavy = [itm_parthian_helm_cavalry_heavy_1, itm_parthian_helm_cavalry_heavy_2]
parthian_helm_infantry = [itm_parthian_helm_inf_1, itm_parthian_helm_inf_2]
parthian_helm_infantry_heavy = [itm_parthian_helm_inf_heavy_1, itm_parthian_helm_inf_heavy_2,itm_parthian_helm_inf_heavy_3,itm_parthian_helm_inf_heavy_4]
parthian_helm_phyrgian = [itm_phrygian_cap,itm_phrygian_cap_yellow,itm_phrygian_cap_white,itm_phrygian_cap_red,itm_phrygian_cap_black,itm_phrygian_cap_green,itm_phrygian_cap_blue,]
armenian_helm_heavy = [itm_armenian_helm_heavy_1,itm_armenian_helm_heavy_2,itm_armenian_helm_heavy_3]

persian_helm_light = [itm_perisan_headcloth_1,itm_perisan_headcloth_2,itm_perisan_headcloth_3,itm_perisan_headcloth_4]

armenian_helm_legio = [itm_armenian_helm_legion_1,itm_armenian_helm_legion_2,itm_armenian_helm_legion_3,itm_armenian_helm_legion_4]

caucasian_helm_heavy = [itm_sarmatian_heavy_helm6,itm_sarmatian_heavy_helm8,itm_bosporan_pointed_helm,itm_bosporan_pointed_helm_2]
caucasian_helm_light = [itm_bosporan_spangenhelm_3,itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4]

eastern_sword_short =[itm_dagger_parthian_1,itm_eastern_sowrd1]
eastern_swords_medium =[itm_eastern_sowrd2,itm_eastern_sowrd3]
eastern_swords_long =[itm_eastern_sowrd4,itm_eastern_sowrd5]

eastern_armor_tunics_persian = [itm_persian_tunic_1,itm_persian_tunic_2,itm_persian_tunic_3,itm_persian_tunic_4]
eastern_armor_tunics_armenian = [itm_armenian_tunic_1,itm_armenian_tunic_2,itm_armenian_tunic_3,itm_armenian_tunic_4]
eastern_armor_tunics_parthian = [itm_parthian_tunic_1,itm_parthian_tunic_2,itm_parthian_tunic_3,itm_parthian_tunic_4]
eastern_armor_furarmor = [itm_persian_sheepskin_1,itm_persian_sheepskin_2,itm_persian_sheepskin_3,itm_persian_sheepskin_4]

germanic_caps = [itm_germanic_cap_1,itm_germanic_cap_2,itm_germanic_cap_3,itm_germanic_cap_4]

germanic_armor_pants_1 = [itm_germanic_naked1,itm_germanic_naked2]
germanic_armor_pants_2 = [itm_germanic_naked5,itm_germanic_naked4]
germanic_armor_pants_3 = [itm_germanic_naked6,itm_germanic_naked7]
germanic_armor_tunics_1 = [itm_germanic_light1,itm_germanic_light2,itm_germanic_light4,itm_germanic_light10]
germanic_armor_tunics_2 = [itm_germanic_light5,itm_germanic_light6,itm_germanic_light7,itm_germanic_light11]
germanic_armor_tunics_3 = [itm_germanic_light8,itm_germanic_light9,itm_linen_tunic,itm_germanic_light11]
germanic_armor_tunics_noble_1 = [itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2]
germanic_armor_tunics_noble_2 = [itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4]
germanic_armor_fur_1 = [itm_germanic_light3,itm_germanic_medium1,itm_germanic_medium2]
germanic_armor_fur_2 = [itm_germanic_medium3,itm_germanic_medium4]
germanic_armor_fur_3 = [itm_germanic_medium5,itm_germanic_medium6]

eastern_armor_mail_parthian = [itm_parthian_mail_1,itm_parthian_mail_2]
eastern_armor_scale_parthian = [itm_parthian_scale_1,itm_parthian_scale_2]
eastern_armor_mail_armenian = [itm_armenian_mail_1,itm_armenian_mail_2]
eastern_armor_scale_armenian = [itm_armenian_scale_1,itm_armenian_scale_2]
eastern_armor_scale_heavy_1 = [itm_parthian_scale_heavy_1,itm_parthian_scale_heavy_2]

eastern_armor_cataphract = [itm_cataphract_eastern,itm_sarranid_elite_armor,itm_mamluke_mail]
eastern_armor_cataphract_lamellar = [itm_sarranid_elite_armor_2,itm_sarranid_elite_armor_3]

eastern_boots_light = [itm_eastern_shoe,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]

eastern_boots_cataphract = [itm_cataphract_boots]

eastern_shields_wicker_smallround = [itm_ad_mixed_round_shields_07,itm_ad_mixed_round_shields_08,itm_ad_mixed_round_shields_13,itm_ad_mixed_round_shields_14]

eastern_shields_wicker_armenian = [itm_scythisn_shield_inf1,itm_scythisn_shield_inf2, itm_scythisn_shield_inf3,itm_scythisn_shield_inf4]
eastern_shields_wicker = [itm_eastern_shield_inf_light6,itm_eastern_shield_inf_light5]
eastern_shields_wicker_painted = [itm_eastern_shield_inf_light7, itm_eastern_shield_inf_light8,itm_eastern_shield_inf_light9,itm_eastern_shield_inf_light10]
eastern_shields_wicker_oval = [itm_eastern_shield_inf_light1,itm_eastern_shield_inf_light2,itm_eastern_shield_inf_light3,itm_eastern_shield_inf_light4]
eastern_shields_oval_parthian_1 = [itm_eastern_shield_inf_heavy7,itm_eastern_shield_inf_heavy8,itm_eastern_shield_inf_heavy11]
eastern_shields_oval_parthian_2 = [itm_eastern_shield_inf_heavy3,itm_eastern_shield_inf_heavy4,itm_eastern_shield_inf_heavy5]
eastern_shields_oval_armenian_1 = [itm_eastern_shield_inf_heavy9,itm_eastern_shield_inf_heavy10,itm_eastern_shield_inf_heavy12]
eastern_shields_oval_armenian_2 = [itm_eastern_shield_inf_heavy1,itm_eastern_shield_inf_heavy2,itm_eastern_shield_inf_heavy6]

scythian_shields_1 = [itm_scythian_shield_cav1,itm_scythian_shield_cav5,itm_scythian_shield_cav6]
scythian_shields_2 = [itm_scythian_shield_cav2,itm_scythian_shield_cav3,itm_scythian_shield_cav4]

sarmatian_ringswords_short = [itm_sarmatian_sword_1,itm_sarmatian_sword_2,itm_sarmatian_ringsword_1,itm_sarmatian_ringsword_3]
sarmatian_ringswords_long = [itm_sarmatian_ringsword_2,itm_sarmatian_ringsword_4]

kontos = [itm_lance,itm_light_lance]
kontos_long = [itm_heavy_lance]

sarmatian_boots = [itm_sarmatian_shoes]

bosphoran_armor_tunic = [itm_bosporan_light4,itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3]
sarmatian_armor_tunic = [itm_sarmatian_light5, itm_sarmatian_light6, itm_sarmatian_light2,itm_sarmatian_light1,itm_kaftan_1,itm_kaftan_2,itm_kaftan_3]
sarmatian_armor_padded = [itm_sarmatian_light3,itm_sarmatian_light4]

sarmatian_armor_tunic_scyth_1 = [itm_scythian_light1,itm_scythian_light2,itm_sarmatian_light7]
sarmatian_armor_tunic_scyth_2 = [itm_scythian_light3,itm_scythian_light4,itm_scythian_light5]

sarmatian_armor_heavy_scyth = [itm_scythian_heavy1,itm_scythian_heavy2]

caucasian_scale = [itm_caucasian_scale_1,itm_caucasian_scale_2]
caucasian_scale_heavy = [itm_caucasian_scale_heavy_1,itm_caucasian_scale_heavy_2]
caucasian_mail = [itm_bosporan_mail_1,itm_bosporan_mail_2,itm_bosporan_mail_3]

bosphoran_armor_mail = [itm_bosporan_mail_1,itm_bosporan_mail_2,itm_bosporan_mail_3]
bosphoran_armor_mail_and_scale = [itm_bosphoran_scale_1,itm_bosphoran_scale_2]
bosphoran_armor_scale = [itm_bosphoran_scale_3,itm_bosphoran_scale_4]
sarmatian_armor_scale = [itm_sarmitian_scale_5,itm_sarmitian_scale_6,itm_sarmitian_scale_7,itm_sarmitian_scale_8]
sarmatian_armor_mail_and_scale_1 = [itm_sarmitian_scale_1,itm_sarmitian_scale_2,itm_sarmitian_scale_9]
sarmatian_armor_mail_and_scale_2 = [itm_sarmitian_scale_3,itm_sarmitian_scale_4,itm_sarmitian_scale_10]
sarmatian_armor_mail_1 = [itm_sarmitian_mail_3,itm_sarmitian_mail_4]
sarmatian_armor_mail_2 = [itm_sarmitian_mail_1,itm_sarmitian_mail_2]

sarmatian_helm_pointed = [itm_bosporan_pointed_helm,itm_bosporan_pointed_helm_2,itm_bosporan_pointed_helm_3,itm_bosporan_pointed_helm_4]
sarmatian_helm_spangen = [itm_bosporan_spangenhelm_1,itm_bosporan_spangenhelm_2,itm_bosporan_spangenhelm_3]
sarmatian_helm_nobel_1 = [itm_sarmatian_heavy_helm1,itm_sarmatian_heavy_helm2,itm_sarmatian_heavy_helm3,itm_sarmatian_heavy_helm4]
sarmatian_helm_nobel_2 = [itm_sarmatian_heavy_helm5,itm_sarmatian_heavy_helm6,itm_sarmatian_heavy_helm7,itm_sarmatian_heavy_helm8]

sarmatian_helm_cap_1 = [itm_sarmatian_cap_1,itm_sarmatian_cap_2]
sarmatian_helm_cap_2 = [itm_sarmatian_cap_3,itm_sarmatian_cap_4]

dacian_helm_normal = [itm_dacian_heavy_helm1,itm_dacian_heavy_helm5,itm_dacian_heavy_helm7,itm_dacian_heavy_helm13,itm_dacian_heavy_helm3]
dacian_helm_plume = [itm_dacian_heavy_helm8,itm_dacian_heavy_helm9,itm_dacian_heavy_helm10]
dacian_helm_decorate = [itm_dacian_heavy_helm12,itm_dacian_heavy_helm11,itm_dacian_heavy_helm4,itm_dacian_heavy_helm2,itm_dacian_heavy_helm14,itm_dacian_heavy_helm_noble_1,itm_dacian_heavy_helm_noble_2]

german_war_paint = [itm_german_body_paint_1_black,itm_german_body_paint_2_black,itm_german_body_paint_3_black,itm_german_body_paint_4_black,itm_german_body_paint_5_black]

#greek equipment nobody wants
jew_swords_greek = [itm_sword_akinakes,itm_sword_kopis,itm_sword_laconian_dagger,itm_sword_xiphos_greek]
jew_phalanx_gear = [itm_sarissa, itm_s_parma_mak_plain_16, itm_s_parma_mak_plain_15,itm_s_parma_mak_plain_14,itm_s_parma_mak_plain_13,itm_mak_helm_3,itm_mak_helm_4]
jew_linothorax = [itm_linothorax_greek1,itm_linothorax_greek2,itm_linothorax_greek3,itm_linothorax_greek4]

horse_steppe_cataphract = [itm_cataphract_horse_steppe_1,itm_cataphract_horse_steppe_2,itm_cataphract_horse_steppe_3]
horse_parth_cataphract = [itm_cataphract_horse_parthian_1,itm_cataphract_horse_parthian_2,itm_cataphract_horse_parthian_3]
horse_parth_half_cataphract = [itm_half_cataphract_horse_parthian_1,itm_half_cataphract_horse_parthian_2,itm_half_cataphract_horse_parthian_3]

horse_parth = [itm_parthian_horse_a,itm_parthian_horse_b,itm_parthian_horse_c]
horse_arab = [itm_arabian_horse_a,itm_arabian_horse_b,itm_arabian_horse_c]
horse_steppe = [itm_steppe_horse_1,itm_steppe_horse_2,itm_steppe_horse_3]
horse_normal = [itm_normal_horse_1,itm_normal_horse_2,itm_normal_horse_3]
horse_leopard = [itm_leopard_horse_1,itm_leopard_horse_3]
horse_numidian = [itm_numidian_horse_1,itm_numidian_horse_2,itm_numidian_horse_3]

items_roman_horses = [itm_horse_1,itm_horse_2,itm_horse_3,itm_horse_4,itm_horse_5,itm_horse_6,itm_horse_7,itm_horse_8,itm_horse_9]


dacian_scale_heavy = [itm_dacian_heavy1,itm_dacian_heavy2,itm_dacian_heavy5,itm_dacian_heavy6]
dacian_scale_light = [itm_dacian_medium1,itm_dacian_medium2,itm_dacian_medium3]
dacian_mail_heavy  = [itm_dacian_heavy3,itm_dacian_heavy4]
dacian_mail_light  = [itm_dacian_medium4,itm_dacian_medium5,itm_dacian_medium6]

dacian_tunic_noble_1 = [itm_dacian_noble1,itm_dacian_noble4,itm_dacian_noble5]
dacian_tunic_noble_2 = [itm_dacian_noble6,itm_dacian_noble2,itm_dacian_noble3]
dacian_tunic_1 = [itm_dacian_light1,itm_dacian_light2,itm_dacian_light3,itm_dacian_light4,itm_dacian_light9,itm_dacian_light10]
dacian_tunic_2 = [itm_dacian_light5,itm_dacian_light6,itm_dacian_light7,itm_dacian_light8,itm_dacian_light11,itm_dacian_light12]
dacian_naked_1 = [itm_dacian_naked1,itm_dacian_naked2,itm_dacian_naked3,itm_dacian_naked4]
dacian_naked_2 = [itm_dacian_naked5,itm_dacian_naked6,itm_dacian_naked7,itm_dacian_naked8]

dacian_cap = [itm_dacian_pileus_a_1,itm_dacian_pileus_a_2,itm_dacian_pileus_b_1,itm_dacian_pileus_b_2,
itm_dacian_pileus_c_1,itm_dacian_pileus_c_2]
dacian_helm_normal = [itm_dacian_heavy_helm1,itm_dacian_heavy_helm5,itm_dacian_heavy_helm7,itm_dacian_heavy_helm13,itm_dacian_heavy_helm3]
dacian_helm_plume = [itm_dacian_heavy_helm8,itm_dacian_heavy_helm9,itm_dacian_heavy_helm10]
dacian_helm_decorate = [itm_dacian_heavy_helm12,itm_dacian_heavy_helm11,itm_dacian_heavy_helm4,itm_dacian_heavy_helm2,itm_dacian_heavy_helm14,itm_dacian_heavy_helm_noble_1,itm_dacian_heavy_helm_noble_2]

dacian_sword_noble = [itm_dacian_noble_sword]
dacian_sword = [itm_dacian_ring_sword]
dacian_flax_onehanded = [itm_flax_onehanded1,itm_flax_onehanded2]
dacian_flax_twohanded_1 = [itm_flax1,itm_flax2,itm_flax3,itm_flax4,itm_flax5,itm_flax6]

dacian_spear = [itm_dacian_short_spear,itm_dacian_medium_spear]

dacian_shield_inf_1 = [itm_dacian_oval_shield_1,itm_dacian_shield_large3,itm_dacian_shield_large4,
itm_dacian_shield_large5,itm_dacian_oval_shield_5,itm_dacian_oval_shield_6,itm_dacian_medium_shield_5]
dacian_shield_inf_2 = [itm_dacian_shield_large6,itm_dacian_oval_shield_2,itm_dacian_oval_shield_3
,itm_dacian_oval_shield_4,itm_dacian_shield_large1,itm_dacian_shield_large2,itm_dacian_medium_shield_4]
dacian_shield_inf_3 = [itm_dacian_oval_shield_7,itm_dacian_oval_shield_8,itm_dacian_oval_shield_9,
itm_dacian_medium_shield_1,itm_dacian_medium_shield_2,itm_dacian_medium_shield_3,itm_dacian_oval_shield_10]
dacian_shield_round = [itm_dacian_shield_small1,itm_dacian_shield_small2,itm_dacian_shield_small3,
itm_dacian_shield_small4,itm_dacian_shield_small5,itm_dacian_shield_small6]

dacian_throwing = [itm_throwing_spears_dacian,itm_jarid]

dacian_bow_1 = [itm_arrows, itm_nomad_bow]
dacian_bow_2 = [itm_barbed_arrows, itm_khergit_bow]

desert_turbans_1 = [itm_tuareg_new_1_green,itm_tuareg_new_1_blue,itm_tuareg_new_1_red,itm_tuareg_new_1_white,
                    itm_tuareg_new_2_green,itm_tuareg_new_2_blue,itm_tuareg_new_2_red,itm_tuareg_new_2_white]

desert_turbans_2 = [itm_turban,itm_turban_2,itm_desert_turban,itm_desert_turban_2]

roman_tunic = [itm_roman_tunic_1,itm_roman_tunic_2,itm_roman_tunic_3,itm_roman_poor1,itm_roman_poor4,itm_roman_poor5,itm_roman_poor6,itm_roman_poor7,itm_roman_poor2,itm_roman_poor3]
berber_tunic = [itm_numidian_armor_1,itm_numidian_armor_2,itm_numidian_armor_3,itm_numidian_armor_5]
garamantian_tunic = [itm_garmantian_armor_3,itm_garmantian_armor_4,itm_garmantian_armor_5]
eastern_roman_tunic = [itm_judean_tunic_1,itm_judean_tunic_2,itm_judean_tunic_3,itm_judean_tunic_4,itm_judean_tunic_5,itm_judean_tunic_6]
germanic_tunic = [itm_germanic_light1,itm_germanic_light2,itm_germanic_light3,itm_germanic_light4,itm_germanic_light5,itm_germanic_light6,
                                itm_germanic_light7,itm_germanic_light8,itm_germanic_light9,itm_germanic_light10,itm_germanic_light11]
dacian_tunic = [itm_dacian_light1,itm_dacian_light2,itm_dacian_light3,itm_dacian_light4,itm_dacian_light5,itm_dacian_light6,itm_dacian_light7,
                            itm_dacian_light8,itm_dacian_light9,itm_dacian_light10,itm_dacian_light11,itm_dacian_light12]

desert_tunic = [itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b,itm_sarranid_cloth_robe_c,
                            itm_arabian_tunic_1,itm_arabian_tunic_2,itm_arabian_tunic_3]

iberian_tunic = [itm_iberian_light6,itm_iberian_light5,itm_iberian_light3,itm_iberian_light4]

nomadic_tunic = [itm_kaftan_1,itm_kaftan_2,itm_kaftan_3,itm_sarmatian_light5,itm_sarmatian_light6,itm_sarmatian_light7,itm_scythian_light1,itm_scythian_light2,itm_scythian_light3]

bosporan_tunic = [itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4]
caucasian_tunic = [itm_armenian_tunic_1,itm_armenian_tunic_2,itm_armenian_tunic_3,itm_armenian_tunic_4]
persian_tunic_sheepskin = [itm_persian_sheepskin_1,itm_persian_sheepskin_2,itm_persian_sheepskin_3,itm_persian_sheepskin_4]
persian_tunic = [itm_persian_tunic_1,itm_persian_tunic_2,itm_persian_tunic_3,itm_persian_tunic_4]
parthian_tunic = [itm_parthian_tunic_1,itm_parthian_tunic_2,itm_parthian_tunic_3,itm_parthian_tunic_4]
celtic_tunic = celtic_tunics_1+celtic_tunics_2

roman_cives      = [itm_roman_toga,itm_roman_toga_2,itm_roman_toga_3]
dacian_cives     = [itm_dacian_noble1,itm_dacian_noble2,itm_dacian_noble3,itm_dacian_noble4,itm_dacian_noble5,itm_dacian_noble6]
germanic_cives   = [itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4]
celtic_cives = [itm_celtic_light_noble_1,itm_celtic_light_noble_2,itm_celtic_light_noble_3,itm_celtic_light_noble_4]
persian_cives = [itm_sarranid_cloth_robe_fancy_1,itm_sarranid_cloth_robe_fancy_2,itm_sarranid_cloth_robe_fancy_3]
parthian_cives = [itm_sarranid_cloth_robe_fancy_1,itm_sarranid_cloth_robe_fancy_2,itm_sarranid_cloth_robe_fancy_3]
eastern_cives = [itm_sarranid_cloth_robe_fancy_1,itm_sarranid_cloth_robe_fancy_2,itm_sarranid_cloth_robe_fancy_3]
nomadic_cives = [itm_sarmatian_light1,itm_sarmatian_light2,itm_scythian_light4,itm_scythian_light5]
bosporan_cives = bosporan_tunic+nomadic_cives
caucasian_cives = caucasian_tunic
berber_cives = [itm_numidian_armor_5]
garamantian_cives = [itm_garmantian_armor_2,itm_garmantian_armor_1]

weapons_peasant_generic = [itm_shepherds_crook,itm_scythe,itm_pitch_fork,itm_sickle,itm_knife,itm_knife_2,itm_butchering_knife,itm_butchering_knife_2]
roman_weapons_peasant = [itm_roman_work_axe,itm_roman_hammer]+weapons_peasant_generic
dacian_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
celtic_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
germanic_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
parthian_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
nomadic_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
bosporan_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
caucasian_weapons_peasant = [itm_hand_axe, itm_hammer]+weapons_peasant_generic
berber_weapons_peasant = [itm_roman_work_axe, itm_roman_hammer,itm_knife,itm_knife_2,itm_butchering_knife,itm_butchering_knife_2,itm_numidian_spear_1]
garamantian_weapons_peasant = [itm_hand_axe, itm_hammer,itm_knife,itm_knife_2,itm_butchering_knife,itm_butchering_knife_2,itm_numidian_spear_1]
desert_weapons_peasant = [itm_hand_axe,itm_roman_work_axe,itm_roman_hammer,itm_hammer,itm_knife,itm_knife_2,itm_butchering_knife,itm_butchering_knife_2]

roman_foot_peasant = [itm_caligea]
berber_foot_peasant = [itm_caligea]
garamantian_foot_peasant = [itm_caligea]
eastern_foot_peasant = [itm_caligea]
germanic_foot_peasant = [itm_celtic_boots]
celtic_foot_peasant = [itm_celtic_boots]
dacian_foot_peasant = [itm_celtic_boots,itm_leather_boots]
parthian_foot_peasant = [itm_eastern_shoe,itm_leather_boots]
caucasian_foot_peasant = [itm_sarmatian_shoes,itm_eastern_shoe]
persian_foot_peasant = [itm_eastern_shoe,itm_leather_boots]
bosporan_foot_peasant = [itm_leather_boots,itm_sarmatian_shoes]
nomadic_foot_peasant = [itm_sarmatian_shoes,itm_leather_boots]

roman_foot_cives = [itm_caligea,itm_calceus_2,itm_calceus_3,itm_calceus_4]
berber_foot_cives = [itm_caligea]
garamantian_foot_cives = [itm_caligea,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]
eastern_foot_cives = [itm_caligea,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]
germanic_foot_cives = [itm_celtic_boots]
celtic_foot_cives = [itm_celtic_boots]
dacian_foot_cives = [itm_celtic_boots,itm_leather_boots]
parthian_foot_cives = [itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]
caucasian_foot_cives = [itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]
persian_foot_cives = [itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y]
bosporan_foot_cives = [itm_sarmatian_shoes]
nomadic_foot_cives = [itm_sarmatian_shoes]

roman_dress_peasant = [itm_female_1,itm_female_2,itm_female_3]
berber_dress_peasant = [itm_sarranid_common_dress,itm_sarranid_common_dress_b]
garamantian_dress_peasant = [itm_sarranid_common_dress,itm_sarranid_common_dress_b]
eastern_dress_peasant = [itm_sarranid_common_dress,itm_sarranid_common_dress_b]
nomadic_dress_peasant = [itm_female_1_barb,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb]
germanic_dress_peasant = [itm_peasant_dress,itm_female_1_barb,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb]
celtic_dress_peasant = [itm_female_1_celt,itm_female_2_celt,itm_female_3_celt,itm_female_4_celt]
dacian_dress_peasant = [itm_female_1_barb,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb]
parthian_dress_peasant = [itm_sarranid_common_dress,itm_sarranid_common_dress_b]
caucasian_dress_peasant = [itm_female_1_barb,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb]
persian_dress_peasant = [itm_sarranid_common_dress,itm_sarranid_common_dress_b]
bosporan_dress_peasant = [itm_female_1,itm_female_2,itm_female_3]

roman_dress_cives = [itm_roman_noble_dress_7,itm_roman_noble_dress_6,itm_roman_noble_dress_5,itm_roman_noble_dress_4,itm_roman_noble_dress_3,itm_roman_noble_dress_2,itm_roman_noble_dress_1]
berber_dress_cives = [itm_green_dress,itm_khergit_lady_dress,itm_khergit_lady_dress_b]
garamantian_dress_cives = [itm_green_dress,itm_khergit_lady_dress,itm_khergit_lady_dress_b]
eastern_dress_cives = [itm_green_dress,itm_khergit_lady_dress,itm_khergit_lady_dress_b]
nomadic_dress_cives = [itm_barb_femal_rich1,itm_barb_femal_rich2,itm_barb_femal_rich3,itm_barb_femal_rich5]
germanic_dress_cives = [itm_german_femal_rich_1,itm_german_femal_rich_2,itm_german_femal_rich_3,itm_german_femal_rich_4]
celtic_dress_cives = [itm_barb_femal_rich1,itm_barb_femal_rich2,itm_barb_femal_rich3,itm_barb_femal_rich5]
dacian_dress_cives = [itm_barb_femal_rich1,itm_barb_femal_rich2,itm_barb_femal_rich3,itm_barb_femal_rich5]
parthian_dress_cives = [itm_green_dress,itm_khergit_lady_dress,itm_khergit_lady_dress_b]
caucasian_dress_cives = [itm_green_dress,itm_khergit_lady_dress,itm_khergit_lady_dress_b]
persian_dress_cives = [itm_sarranid_lady_dress,itm_sarranid_lady_dress_b]
bosporan_dress_cives = [itm_barb_femal_rich1,itm_barb_femal_rich2,itm_barb_femal_rich3,itm_barb_femal_rich5]

roman_head_peasant = [itm_straw_hat,itm_mediterranean_straw_hat,itm_mediterranean_straw_hat_1,itm_mediterranean_straw_hat_2]
persian_head_peasant = [itm_perisan_headcloth_1,itm_perisan_headcloth_2,itm_perisan_headcloth_3,itm_perisan_headcloth_4,itm_headcloth]
parthian_head_peasant = [itm_phrygian_cap,itm_phrygian_cap_yellow,itm_phrygian_cap_white,itm_phrygian_cap_red,itm_phrygian_cap_black,itm_phrygian_cap_green,itm_phrygian_cap_blue]
caucasian_head_peasant = [itm_phrygian_cap,itm_phrygian_cap_yellow,itm_phrygian_cap_white,itm_phrygian_cap_red,itm_phrygian_cap_black,itm_phrygian_cap_green,itm_phrygian_cap_blue]
nomadic_head_peasant = [itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_kopfband]
dacian_head_peasant = [itm_dacian_pileus_a_1,itm_dacian_pileus_a_2,itm_dacian_pileus_c_1,itm_dacian_pileus_c_2,itm_dacian_pileus_b_1,itm_dacian_pileus_b_2]
germanic_head_peasant = [itm_germanic_cap_1,itm_germanic_cap_2,itm_germanic_cap_3,itm_germanic_cap_4]
celtic_head_peasant = [itm_black_hood,itm_simple_hood_1,itm_simple_hood_2]
bosphoran_head_peasant = [itm_black_hood,itm_simple_hood_1,itm_simple_hood_2]
desert_head_peasant = desert_turbans_1
berber_head_peasant = desert_turbans_2
garamantian_head_peasant = desert_turbans_2 + [itm_african_feather_band]

troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,[],str_4|agi_4|int_4|cha_4,wp(15),0,0x000000003f00100418a371b6da8dcaa200000000001e286b0000000000000000],
["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,[],hero_attrib,0,knows_hero,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,[],hero_attrib,0,knows_hero,0x000000018000004136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],hero_attrib,0,knows_hero|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,[],str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,[],str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1,mercenary_face_2],
["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1,mercenary_face_2],

["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_5", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [], str_9|agi_8|level(13), wp(100), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[],str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1,mercenary_face_2],

["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],

#soldiers:
#This troop is the troop marked as soldiers_begin
# ["farmer", "Rusticus", "Rustici", tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
# [itm_knife,itm_pitch_fork,itm_shepherds_crook, itm_sickle,itm_club,itm_club_2,itm_club_3,itm_stones,itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_straw_hat,itm_caligea],
# attrib_level_6, wp(100), knows_level_6, white_face_11, white_face_12 ],

["sarmatian_peasant", "Sarmatian Tribesman", "Sarmatian Tribesmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+nomadic_tunic+nomadic_foot_peasant+nomadic_head_peasant+nomadic_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, scythian_face_11, scythian_face_12 ],

["bosporan_peasant", "Bosporan Peasant", "Bosporan Peasants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+bosporan_tunic+bosporan_foot_peasant+bosporan_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, scythian_face_11, scythian_face_12 ],

["judean_peasant","Eastern Peasant","Eastern Peasants",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
[itm_sling,itm_sling_rock1]+eastern_roman_tunic+eastern_foot_peasant+roman_weapons_peasant,
attrib_level_6,wp(100),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],

["parthian_peasant","Parthian Tribesman","Parthian Tribesmen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
[itm_sling,itm_sling_rock1]+parthian_tunic+persian_tunic_sheepskin+parthian_foot_peasant+parthian_head_peasant+parthian_weapons_peasant,
attrib_level_6,wp(100),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],

["persian_peasant","Persian Peasant","Persian Peasants",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,
[itm_sling,itm_sling_rock1]+persian_tunic+persian_tunic_sheepskin+persian_foot_peasant+persian_head_peasant+parthian_weapons_peasant,
attrib_level_6,wp(100),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],

["roman_peasant", "Roman Peasant", "Roman Peasants", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+roman_tunic+roman_foot_peasant+roman_weapons_peasant+roman_head_peasant,
attrib_level_6, wp(60), knows_level_6, white_face_21, white_face_22 ],

["celtic_peasant", "Celtic Tribesman", "Celtic Tribesmen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+celtic_foot_peasant+celtic_tunic+celtic_head_peasant+celtic_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],

["germanic_peasant", "Germanic Tribesman", "Germanic Tribesmen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+germanic_foot_peasant+germanic_tunic+germanic_head_peasant+germanic_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],

["dacian_peasant", "Dacian Peasant", "Dacian Peasant", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+dacian_tunic+dacian_foot_peasant+dacian_head_peasant+dacian_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],

["armenian_peasant", "Caucasian Tribesman", "Caucasian Tribesmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+persian_tunic_sheepskin+caucasian_foot_peasant+caucasian_tunic+caucasian_head_peasant+caucasian_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, armenian_face_young, armenian_face_middle ],

["arab_peasant", "Arab Tribesman", "Arab Tribesmen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+desert_head_peasant+desert_tunic+eastern_foot_peasant+desert_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, eastern_man_face_young_1, eastern_man_face_old_2 ],

["berber_peasant", "Berber Tribesman", "Berber Tribesmen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+berber_foot_peasant+berber_tunic+berber_head_peasant+berber_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],

["garamantian_peasant", "Garamantian Tribesman", "Garamantian Tribesmen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling,itm_sling_rock1]+garamantian_foot_peasant+garamantian_tunic+garamantian_head_peasant+garamantian_weapons_peasant,
attrib_level_6, wp(100), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],


["watchman", "Mercenarius Funditor", "Mercenarii Funditores", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_sling_rock1,itm_sling,itm_sword_akinakes,itm_roman_poor1,itm_roman_poor2,itm_roman_poor4,itm_roman_poor5,itm_caligea],
attrib_level_12, wp(110), knows_level_12, white_face_11, white_face_12 ],
["caravan_guard", "Custos", "Custodes", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
[itm_caligea,itm_armenian_tunic_1,itm_bosporan_light1,itm_bosporan_light2,itm_germanic_light7]+items_roman_horses+jew_helm_light+jew_spears+jew_swords+old_roman_roundshields,
attrib_level_18, wp(115), knows_level_18, white_face_11, white_face_12 ],
["mercenary_swordsman", "Mercenarius Hastatus", "Mercenarii Hastati", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_war_spear,itm_spear,itm_cavalry_spear,itm_caligea,itm_armenian_tunic_3,itm_bosporan_light3,itm_dacian_light7,itm_dacian_light8]+old_roman_roundshields+jew_helm_light,
attrib_level_23, wp(120), knows_level_26, mercenary_face_1, mercenary_face_2 ],
["hired_blade", "Xenikos Peltastes", "Xenikoi Peltastai", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_throwing_spears_east,itm_throwing_spears_east]+eastern_shields_oval_armenian_1+eastern_shields_oval_parthian_2+eastern_sword_short+armenian_helm_heavy+eastern_armor_scale_armenian+eastern_armor_mail_parthian+eastern_boots_light,
attrib_level_26, wp(130), knows_level_23, white_face_11, white_face_12 ],
["mercenary_crossbowman", "Mercenarius Sagittarius", "Mercenarii Sagittarii", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_phrygian_cap_black,itm_phrygian_cap_green,itm_phrygian_cap_white,itm_iberian_light6,itm_iberian_light5,itm_iberian_light3,itm_iberian_light4,itm_caligea,itm_short_bow,itm_arrows,itm_mace_1,
itm_spiked_club],
attrib_level_18, wpe(100,135,135,135), knows_archer_basic, white_face_11, white_face_12 ],
["mercenary_horseman", "Mercenarius Eques", "Mercenarius Equites", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_iberian_medium1,itm_iberian_medium2,itm_iberian_medium3,itm_caligea,itm_spear,itm_javelin,itm_kopfband,itm_celtic_round_shild3]+items_roman_horses,
attrib_level_23, wp(125), knows_level_23, white_face_11, white_face_12 ],
["mercenary_cavalry", "Mercenarius Cataphractus", "Mercenarii Cataphracti", tf_mounted|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves, no_scene, reserved, fac_commoners,
[itm_heavy_lance,itm_lance,itm_cataphract_boots,itm_cataphract_helm6,itm_cataphract_helm7,itm_cataphract_eastern,itm_sarranid_elite_armor,itm_mail_mittens,itm_eastern_sowrd4]+horse_parth_cataphract,
attrib_level_31, wp(140), knows_level_31, persian_face_young, persian_face_middle ],
##new mercs from illyria:
["illyrian_horseman", "Illyrioi Hippeis", "Illyrioi Hippeis", tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_illyrian_medium3,itm_illyrian_medium4,itm_illyrian_medium5,itm_illyrian_leader_cap,itm_illyrian_hevy_helmet,itm_leather_covered_round_shield,
itm_spear,itm_war_spear,itm_kopis,itm_graves_simple_2,itm_illyrian_hevy_helmet_plume2]+horse_normal,
attrib_level_23, wp(160), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["illyrian_infantry", "Illyrioi Pezoi", "Illyrioi Pezoi", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_graves_simple,itm_illyrian_medium1,itm_illyrian_medium2,itm_iberian_light1,itm_iberian_light2,itm_illyrian_leader_cap,itm_illyrian_shield_large1,itm_illyrian_hevy_helmet,itm_illyrian_shield_large2,
itm_illyrian_shield_heavy1,itm_illyrian_shield_heavy2,itm_illyrian_shield_heavy3,itm_war_spear,itm_spear,itm_throwing_spears,itm_one_handed_war_axe_a,itm_illyrian_hevy_helmet_plume1],
attrib_level_23, wp(160), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
##rhodos
["slinger_rhodos", "Rhodios Sphendonetes", "Rhodios Sphendonetai", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_sling,itm_sling_lead,itm_graves_simple,itm_roman_poor3,itm_roman_poor5,itm_roman_poor4,itm_sword_xiphos_greek,itm_straw_hat,itm_hide_covered_round_shield],
attrib_level_16, wpe(100,170,170,170), knows_archer_basic, mercenary_face_greek_1, mercenary_face_greek_2 ],
##kreta
["kreta_archer", "Kretes Toxotes", "Kretes Toxotai", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_war_bow, itm_bodkin_arrows, itm_sword_xiphos_greek, itm_graves_simple_2, itm_subarmalis_1, itm_subarmalis_2,itm_subarmalis_3,itm_roman_poor4,itm_roman_aux_helm_7,itm_roman_aux_helm_9,
itm_ad_mixed_round_shields_01,itm_ad_mixed_round_shields_02,itm_ad_mixed_round_shields_05,itm_ad_mixed_round_shields_06],
attrib_level_29, wpe(110,170,170,170), knows_archer_elit, mercenary_face_greek_1, mercenary_face_greek_2 ],
##spain: p_town_32	p_town_30	p_town_3
["hispanic_infantry", "Scutarius", "Scutarii", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_iberian_light5,itm_iberian_light3,itm_iberian_light4,itm_iberian_light6,itm_iberian_medium2,itm_iberian_medium3,itm_iberian_medium1,itm_caligea,itm_spear,itm_javelin,
itm_kopfband,itm_celtic_round_shild3,itm_celtic_round_shild2,itm_celtic_round_shild1,itm_one_handed_war_axe_a,itm_leather_covered_round_shield, itm_footman_helmet],
attrib_level_23, wp(140), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["hispanic_heavy_infantry", "Loricati Scutarius", "Loricati Scutarii", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_iberian_heavy1, itm_iberian_heavy2,itm_iberian_medium3,itm_caligea,itm_spear,itm_kopis,itm_javelin,itm_celtic_round_shild3,itm_leather_covered_round_shield,itm_celtic_shield_large8,itm_celtic_shield_large10,itm_footman_helmet],
attrib_level_26, wp(160), knows_level_26, barbarian_man_face_younger_1, barbarian_man_face_middle_2],

#GREEK SHIT, ONLY VIA EVENT
["hoplit", "Hoplites", "Hoplitai", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [
itm_linothorax_greek1,itm_linothorax_greek2,itm_linothorax_greek3,itm_linothorax_greek4,itm_hoplon_6,itm_hoplon_5,
itm_greek_spear_1,itm_greek_spear_2, itm_graves_simple_2,itm_mak_helm_1,itm_mak_helm_2,itm_mak_helm_3,itm_mak_helm_4,
], attrib_level_29, wp(165), knows_level_29, mercenary_face_greek_1, mercenary_face_greek_2 ],
["phalanx", "Phalangit", "Phalangitai", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [
itm_linothorax_greek1,itm_linothorax_greek2,itm_linothorax_greek3,itm_linothorax_greek4,
itm_s_parma_mak_plain_16, itm_s_parma_mak_plain_15,itm_s_parma_mak_plain_14,itm_s_parma_mak_plain_13,
itm_sarissa, itm_sword_akinakes,
itm_mak_helm_1,itm_mak_helm_2,itm_mak_helm_3,itm_mak_helm_4, itm_graves_simple_2
], attrib_level_29, wp(165), knows_level_29, mercenary_face_greek_1, mercenary_face_greek_2 ],
["hoplit_2", "Epilektos", "Epilektoi", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [
itm_mail_hauberk,itm_haubergeon,itm_mail_shirt,itm_linothorax_greek4,
itm_hoplon_1,itm_hoplon_2,itm_hoplon_4,
itm_greek_spear_2,itm_greek_spear_1,
itm_mak_helm_1, itm_graves_simple_2], attrib_level_31, wp(170), knows_level_31, mercenary_face_greek_1, mercenary_face_greek_2 ],
#END GREEK SHIT END, ONLY VIA EVENT

##new stepp mercenaries (dacian and stepp) also avaible in p_town_13 p_town_16
["scythian_horse_archer", "Duna Skythike", "Duna Skythike", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,
itm_scythian_light1,itm_scythian_light2,itm_scythian_light3,itm_scythian_light4,itm_scythian_light5,
itm_scythian_shield_cav6,itm_scythian_shield_cav5,
itm_scythian_shield_cav4,itm_scythian_shield_cav3,itm_scythian_shield_cav2,itm_scythian_shield_cav1,
itm_sarmatian_bow,itm_khergit_arrows,
itm_eastern_shoe,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
itm_cavalry_spear,itm_one_handed_war_axe_a,itm_sarmatian_sword_1,
]+horse_steppe,
attrib_level_29_warrior, wpe(125,160,160,160), knows_level_29_warrior, scythian_face_11, scythian_face_12 ],

["scythian_amazon", "Amazon", "Amazones", tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_scythian_light1,itm_scythian_light2,itm_scythian_light3,itm_scythian_light4,itm_scythian_light5,
itm_scythian_shield_cav6,itm_scythian_shield_cav5,itm_kopfband,
itm_scythian_shield_cav4,itm_scythian_shield_cav3,itm_scythian_shield_cav2,itm_scythian_shield_cav1,
itm_sarmatian_bow,itm_khergit_arrows,
itm_eastern_shoe,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
itm_cavalry_spear,itm_sarmatian_ringsword_4,itm_sarmatian_ringsword_2,
]+horse_steppe,
attrib_level_29_warrior, wpe(125,160,160,160), knows_level_29_warrior, khergit_woman_face_1, khergit_woman_face_2 ],

["scythian_medium_cavalry", "Skythioi Lonchophoroi", "Skythioi Lonchophoroi", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_bosporan_spangenhelm_3,itm_scythisn_shield_inf5,itm_scythisn_shield_inf6,
 itm_eastern_shoe,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
 itm_cavalry_spear,itm_one_handed_war_axe_a,itm_sarmatian_sword_1,
]+horse_steppe+sarmatian_armor_tunic_scyth_2,
attrib_level_29_warrior, wp(165), knows_level_29_warrior, scythian_face_11, scythian_face_12 ],

["scythian_cataphract", "Kataphraktos Skythike", "Kataphraktos Skythike", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm,
no_scene, reserved, fac_culture_3,
[itm_lance,itm_eastern_shoe,itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_bosporan_pointed_helm_3,itm_bosporan_pointed_helm,
itm_one_handed_war_axe_a,itm_sarmatian_sword_1,
]+horse_steppe_cataphract+sarmatian_armor_heavy_scyth,
attrib_level_31_warrior, wp(175), knows_level_31_warrior, scythian_face_21, scythian_face_22 ],

["alan_horse_archer", "Alanna Badarai", "Alanna Badarai", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_heavy_lance,itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_alan_long_sword_ring,itm_alan_long_sword,
itm_alan_medium_1,itm_alan_medium_2,itm_alan_medium_3,itm_alan_light_1,itm_alan_light_2,itm_kaftan_1,itm_kaftan_2,itm_kaftan_3,
itm_sarmatian_shoes,
itm_alan_helm_1,itm_alan_helm_2,itm_alan_helm_3,itm_alan_helm_4,itm_alan_light_helm,
]+horse_steppe,
attrib_level_26_warrior, wp(165), knows_archer_exp_eastern, scythian_face_11, scythian_face_12 ],

["alan_heavy_horse_archer", "Alanna Leazdaettae", "Alanna Leazdaettae", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_lance,itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_alan_long_sword_ring,itm_alan_long_sword,
itm_alan_heavy_1,itm_alan_heavy_2,
itm_sarmatian_shoes,
itm_alan_helm_1,itm_alan_helm_2,itm_alan_helm_3,itm_alan_helm_4]+horse_steppe,
attrib_level_29_warrior, wp(180), knows_archer_elit_eastern, scythian_face_11, scythian_face_12 ],

##new celtic mercenaries (britannia)
["celtic_freeman", "Ambaktoi", "Ambaktoi", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_1+celtic_oval_shield+celtic_spear+celtic_helmet_coolus_old+celtic_throwing,
attrib_level_18_warrior, wp_melee(140), knows_level_18_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_elite_swordsman", "Arioi", "Arioi", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_2+celtic_mail_normal+celtic_shield_long+celtic_swords+celtic_throwing+celtic_helmet_coolus_new,
attrib_level_23_warrior, wp(150), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],
#irish
["irish_skirmisher", "Weidelos Iwerakoi", "Weidelos Iwerakoi", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_irish,
[itm_celtic_boots,itm_javelin,itm_javelin]+irish_shield+celtic_spear+celtic_tunics_1+celtic_helmet_2,
attrib_level_18_warrior, wpe(130,170,170,170), knows_archer_elit, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["irish_vetran", "Ouxseloi Iwerakoi", "Ouxseloi Iwerakoi",tf_male_barbarian| tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_irish,
[itm_celtic_boots]+celtic_throwing+celtic_helmet_2+celtic_mail_noble+celtic_mail_normal+irish_shield+irish_swords,
attrib_level_26_warrior, wp(160), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

##new germanic mercenaries (germany)
["germanic_hunter", "Sakutjanz", "Sakutjanz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_light8,itm_germanic_light7,itm_germanic_light6,itm_germanic_light5,itm_germanic_light4,itm_germanic_light9,
itm_germanic_shield_large1,itm_germanic_shield_large2,itm_cheruski_sword,itm_germanic_shield_large3,itm_germanic_shield_large4,itm_german_shortbow,itm_long_bow,itm_arrows,itm_sax1,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4],
attrib_level_18_warrior, wpe(135,160,160,160), knows_archer_basic, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_free_spearman", "Gaizoz Frije", "Gaizoz Frije", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6,itm_germanic_helm2,itm_germanic_helm3,itm_simple_germanic_shield,
itm_celtic_boots,itm_war_spear,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,itm_germanic_shield_large9,itm_germanic_helm4],
attrib_level_23_warrior, wp(170), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["germanic_nightwarrior", "Hariz Skaduganganz", "Hariz Skaduganganz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_leather_boots,itm_wolf_skin_2,itm_bear_skin_2,itm_wolf_skin_2,itm_germanic_war_spear,itm_germanic_war_spear_2,itm_germanic_war_spear_3,itm_german_night_shield_1,itm_german_night_shield_2,itm_german_night_shield_3,itm_german_night_shield_4,itm_german_night_shield_5,
itm_throwing_spears,itm_throwing_spears,itm_celtic_boots]+german_war_paint,
attrib_level_26_warrior, wpe(170,170,170,170), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["germanic_free_nobleman", "Istaevones Druthinaz", "Istaevones Druthinaz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4,
itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large2,itm_germanic_shield_hex_large3,itm_germanic_shield_hex_large4,itm_germanic_shield_hex_large5,itm_germanic_shield_hex_large6,
itm_throwing_spears,itm_throwing_spears,itm_celtic_boots,itm_germanic_war_spear_3,itm_germanic_war_spear_2,itm_germanic_war_spear],
attrib_level_26_warrior, wp(190), knows_level_26_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

#Baltic
["baltic_hunter", "Voinu", "Voinu", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_naked1,itm_germanic_naked2,itm_germanic_naked7,itm_germanic_naked4,itm_germanic_naked5,
itm_eastern_germanic_shield_1,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_3,itm_germanic_shield_large6,itm_germanic_shield_large10,
itm_germanic_war_spear_2, itm_throwing_spears, itm_throwing_spears, itm_bear_skin_1, itm_bear_skin_2],
attrib_level_26_warrior, wp(170), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["danish_skirmisher", "Stranjaz Druthiz", "Stranjaz Druthiz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_danish,
[itm_leather_boots,itm_bear_skin_1,itm_bear_skin_2,
itm_germanic_axe1,itm_throwing_spears,itm_throwing_spears,itm_throwing_spears,
itm_germanic_shield_large11,itm_germanic_shield_large10,itm_germanic_shield_large8,
itm_germanic_naked1,itm_germanic_naked2,itm_germanic_naked4,itm_germanic_naked5],
attrib_level_23_warrior, wpe(140,150,150,150), knows_archer_elit, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["danish_vetran", "Akwinaz", "Akwinaz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_danish,
[itm_leather_boots,itm_bear_skin_1,itm_bear_skin_2,itm_germanic_axe2,itm_germanic_axe3,
itm_jarid,itm_jarid,
itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large3,itm_germanic_shield_hex_large5,itm_germanic_shield_hex_large6,
itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6],
attrib_level_29_warrior, wp(160), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["lombard_skirmisher", "Winniliz Slaganz", "Winniliz Slaganz", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_leather_boots,itm_wolf_skin_1,itm_wolf_skin_2,itm_club,itm_club_2,itm_club_3,itm_throwing_spears,itm_throwing_spears,itm_germanic_light5,itm_germanic_light8,itm_germanic_light10,
itm_germanic_shield_large12,itm_germanic_shield_large9,itm_germanic_shield_large2,itm_linen_tunic,itm_germanic_shield_1,itm_germanic_shield_2],
attrib_level_26_warrior, wpe(150,160,160,160), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["lombard_vetran", "Winniliz Waipiz Wopo", "Winniliz Waipiz Wopo",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_4,
[itm_leather_boots,itm_wolf_skin_1,itm_wolf_skin_2,itm_germanic_light3,itm_rawhide_coat,itm_pelt_coat,
itm_jarid,itm_jarid,itm_germanic_war_spear_2,itm_germanic_war_spear_3,itm_germanic_war_spear,
itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large2,itm_germanic_shield_hex_large4,itm_germanic_shield_3,itm_germanic_shield_4,
],
attrib_level_29_warrior, wp(170), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["slavic_skirmisher", "Caisoz Ridanz", "Caisoz Ridanz",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet|tf_mounted|tf_guarantee_horse, no_scene, reserved, fac_slavic,
[itm_celtic_boots,itm_javelin,itm_javelin,itm_eastern_germanic_shield_1,itm_eastern_germanic_shield_3,
itm_germanic_war_spear_3,itm_fighting_axe,itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6,
]+horse_normal+sarmatian_helm_spangen,
attrib_level_23_warrior, wpe(140,150,150,150), knows_archer_elit, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["slavic_vetran", "Toutaginoi", "Toutaginoi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_slavic,
[
itm_celtic_boots,itm_sarmatian_heavy_helm2,itm_sarmatian_heavy_helm3,itm_sarmatian_heavy_helm4,
itm_eastern_germanic_shield_1,itm_eastern_germanic_shield_2,itm_eastern_germanic_shield_3,
itm_germanic_war_spear_3,itm_jarid,itm_jarid,
]+germanic_armor_fur_1+germanic_armor_fur_2+germanic_armor_fur_3,
attrib_level_29_warrior, wp(160), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["georgian_light_archer", "Moisarni", "Moisarni",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_georgians,
[itm_caucasian_spear_145,itm_caucasian_spear_174,itm_club,itm_club_2,itm_club_3,itm_caucasian_axe_1,itm_sarmatian_shoes,itm_caucasian_shield_1,itm_caucasian_shield_2,
itm_sarmatian_light6,itm_sarmatian_light7,itm_kaftan_3,itm_javelin,itm_javelin,
]+eastern_armor_furarmor+sarmatian_helm_cap_1+sarmatian_helm_cap_2,
attrib_level_23_warrior, wp(150), knows_archer_exp|knows_athletics_8, scythian_face_11, scythian_face_12 ],
["georgian_noble_archer", "Kovkasi Lernain Netadzik", "Kovkasi Lernain Netadzik",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_georgians,
[itm_caucasian_spear_145,itm_caucasian_spear_174,itm_sarmatian_sword_2,itm_caucasian_axe_1,itm_sarmatian_ringsword_1,itm_sarmatian_shoes,
itm_bosporan_pointed_helm_3,itm_bosporan_pointed_helm_2,itm_sarmitian_scale_10,itm_sarmitian_scale_9,itm_kaftan_3,itm_kaftan_2,
itm_kaftan_1,itm_strong_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_sarmatian_bow
]+sarmatian_helm_cap_2+sarmatian_helm_cap_1,
attrib_level_29_warrior, wp(170), knows_archer_elit, scythian_face_21, scythian_face_22 ],


##new Eastern mercenaries (parthia et armenia) p_town_22 p_town_10
["persian_picaxe_man", "Tabargane Eranshahr", "Tabargane Eranshahr", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_hide_covered_round_shield,itm_hide_covered_round_shield_2,itm_military_hammer,itm_throwing_spears_east,itm_throwing_spears_east]+eastern_boots_light+eastern_armor_furarmor+persian_helm_light+scythian_shields_1,
attrib_level_18, wp(140), knows_level_18, persian_face_young, persian_face_middle ],
["persian_noble_cav", "Asad Asavaran", "Asad Asavaran", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_cataphract_eastern,itm_mamluke_mail,itm_sarranid_elite_armor,itm_sarranid_mace_1,itm_cataphract_boots,
itm_persian_bow,itm_barbed_arrows,itm_lance]+horse_parth_cataphract+horse_parth_half_cataphract+parthian_helm_sallet+armenian_helm_heavy,
attrib_level_31, wpe(140,150,150,150), knows_horseman_eastern, persian_face_young, persian_face_middle ],

["saka_horse_archer", "Yukhuna Ysaninu Purma", "Yukhuna Ysaninu Purma", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_heavy_lance,itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_kaftan_1,itm_kaftan_2,itm_kaftan_3,itm_sarmatian_shoes,
itm_saka_cap_1,itm_saka_hat_1,itm_saka_cap_2,itm_saka_hat_2,itm_saka_cap_3,itm_saka_hat_3,itm_sarmatian_ringsword_1
]+horse_steppe,
attrib_level_26_warrior, wp(165), knows_archer_exp_eastern, saka_face_1, saka_face_2 ],
["saka_heavy_cavalry", "Sakaya Azaryanaka", "Sakaya Azaryanaka", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_lance,itm_alan_long_sword,itm_alan_long_sword_ring,
itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
itm_saka_helmet_1,itm_saka_helmet_2,itm_saka_helmet_3,
itm_saka_armour_1,itm_saka_armour_2,itm_saka_armour_3,itm_saka_armour_4
]+horse_steppe_cataphract,
attrib_level_29_warrior, wp(180), knows_archer_elit_eastern, saka_face_1, saka_face_2 ],
["saka_amazon", "Sakai Amazon", "Sakai Amazones", tf_mounted|tf_female|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_lance,itm_alan_long_sword,itm_alan_long_sword_ring,
itm_eastern_shoe_b,itm_eastern_shoe_r,itm_eastern_shoe_y,
itm_saka_helmet_1,itm_saka_helmet_2,itm_saka_helmet_3,
itm_saka_armour_1,itm_saka_armour_2,itm_saka_armour_3,itm_saka_armour_4,
itm_kaftan_1,itm_kaftan_2,itm_kaftan_3,itm_sarmatian_shoes,
itm_saka_cap_1,itm_saka_hat_1,itm_saka_cap_2,itm_saka_hat_2,itm_saka_cap_3,itm_saka_hat_3,itm_sarmatian_ringsword_1
]+horse_steppe_cataphract + horse_steppe,
attrib_level_29_warrior, wp(180), knows_archer_elit_eastern, saka_face_female_1, saka_face_female_2 ],

#indian
["indian_archer", "Dhanurdhara", "Dhanurdhara", tf_guarantee_boots|tf_male_eastern|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_4,
[itm_long_bow,itm_khergit_arrows,itm_indian_pants_1,itm_indian_pants,itm_caligea,itm_indian_turban_1,itm_indian_turban_2,itm_indian_turban_3,itm_indian_turban_4,itm_indian_turban_5,
itm_sword_kopis,itm_indian_shield_1,itm_indian_shield_2,itm_indian_shield_3,itm_indian_shield_4,itm_indian_shield_5],
attrib_level_18_warrior, wpe(135,160,160,160), knows_archer_basic, eastern_man_face_young_1, eastern_man_face_middle_2 ],
["indian_spearman", "Patti Kauntika", "Patti Kauntika", tf_guarantee_boots|tf_male_eastern|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_indian_pants_1,itm_indian_pants_2,itm_indian_pants,itm_caligea,itm_indian_turban_1,itm_indian_turban_2,itm_indian_turban_3,itm_indian_turban_4,itm_indian_turban_5,
itm_greek_spear_1,itm_indian_shield_1,itm_indian_shield_2,itm_indian_shield_3,itm_indian_shield_4,itm_indian_shield_5,itm_throwing_spears,itm_throwing_spears],
attrib_level_23_warrior, wp(170), knows_level_23_warrior, eastern_man_face_middle_2, eastern_man_face_old_2 ],

##new african mercenaries	avaible in: p_town_21	p_town_28	p_town_29
["sarranid_horseman","Mishteret Garamantim", "Mishteret Garamantim", tf_male_north_african|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_horse|tf_mounted, no_scene, reserved, fac_garamantes,
[itm_caligea,itm_numidian_spear_1,itm_javelin_berber,itm_headcloth,itm_garmantian_armor_3,itm_garmantian_armor_4,itm_garmantian_armor_5,itm_african_round_shield,itm_african_shield_2,itm_sarranid_felt_hat,itm_african_feather_band]+horse_numidian+desert_turbans_2,
attrib_level_18_warrior, wp_melee(165), knows_level_18_warrior, north_african_man_face_younger_1, north_african_man_face_middle_2 ],

["garamantien_noble_horseman","Dorkim Garamantim", "Dorkim Garamantim",  tf_male_north_african|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_mounted, no_scene, reserved, fac_gaetuli,
[itm_centurio_east_graves,itm_caligea,itm_garmantian_armor_1,itm_garmantian_armor_2,itm_garmantian_armor_3,itm_garmantian_armor_4,itm_sarranid_felt_hat,itm_headcloth,itm_african_shield_1,itm_african_shield_2,itm_african_feather_band,
itm_numidian_spear_2,itm_javelin_berber,itm_eastern_helm1,itm_eastern_helm2,itm_eastern_helm3,itm_eastern_helm4]+horse_numidian+desert_turbans_2,
attrib_level_23_warrior, wp_melee(185), knows_level_23_warrior, north_african_man_face_young_1, north_african_man_face_old_2 ],

["gaetuli_horseman","Parasim Maurim", "Parasim Maurim", tf_male_north_african|tf_mounted|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots, no_scene, reserved, fac_garamantes,
[itm_caligea,itm_numidian_spear_1,itm_javelin_berber,itm_numidian_armor_1,itm_numidian_armor_2,itm_numidian_armor_3,itm_leather_covered_round_shield,itm_african_round_shield,
itm_sarranid_cloth_robe_b,itm_ad_mixed_round_shields_07,itm_ad_mixed_round_shields_08,itm_sarranid_felt_hat]+horse_numidian+desert_turbans_2,
attrib_level_18_warrior, wp_melee(165), knows_level_18_warrior, north_african_man_face_younger_1, north_african_man_face_middle_2 ],

["gaetuli_noble_horseman","Thugga Maurim", "Thugga Maurim", tf_male_north_african|tf_mounted|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_gaetuli,
[itm_centurio_east_graves,itm_numidian_spear_2,itm_javelin_berber,itm_numidian_armor_1,itm_numidian_armor_3,itm_numidian_armor_4,itm_numidian_armor_5,itm_caligea,itm_eastern_helm1,itm_eastern_helm2,itm_eastern_helm3,itm_eastern_helm4,
itm_sarranid_felt_hat,itm_ad_mixed_round_shields_13,itm_ad_mixed_round_shields_14,itm_african_round_shield,itm_ad_mixed_round_shields_07,itm_ad_mixed_round_shields_08]+horse_numidian+desert_turbans_2,
attrib_level_23_warrior, wp(185), knows_level_23_warrior, north_african_man_face_young_1, north_african_man_face_old_2 ],

##new kush mercenaries avaible in: p_town_48, p_town_20
["meroe_archers", "Nassi Wir", "Nassi Wir", tf_male_black|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_kush,
[itm_bodkin_arrows,itm_gauntles_1,itm_nubian_war_bow,itm_eastern_sowrd1,itm_numidian_armor,itm_numidian_helm,itm_numidian_wig,itm_nubian_kilt_3,
itm_african_round_shield,itm_nubian_kilt_2],
attrib_level_26_warrior, wpe(145,170,170,170), knows_archer_elit_eastern, nubian_man_face_younger_1, nubian_man_face_middle_2],
["meroe_infantry", "Bilitti Sayif", "Bilitti Sayif", tf_male_black|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_kush,
[itm_throwing_spears,itm_gauntles_1,itm_throwing_spears,itm_african_shield_1,itm_african_shield_2,itm_african_shield_3,itm_numidian_wig,
itm_eastern_sowrd4,itm_eastern_sowrd1,itm_numidian_armor,itm_numidian_helm],
attrib_level_26_warrior, wp(170), knows_level_26_warrior, nubian_man_face_younger_1, nubian_man_face_middle_2 ],
["meroe_axemen", "Toog Kugur", "Toog Kugur", tf_male_black|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_kush,
[itm_nubian_kilt,itm_nubian_tunic,itm_numidian_wig,itm_numidian_helm,itm_kilt_a,itm_kilt_b,itm_kilt_c,itm_kilt_d,
itm_nubian_kite_shield_1,itm_nubian_kite_shield_2,itm_nubian_kite_shield_3,itm_nubian_kite_shield_4,itm_nubian_kite_shield_5,
itm_nubian_axe,itm_nubian_axe_2],
attrib_level_23_warrior, wp(150), knows_level_23_warrior, nubian_man_face_younger_1, nubian_man_face_old_2 ],

#Egyptian
["egyptian_archers", "Reftksote", "Reftksote", tf_male_north_african|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_egypt,
[itm_caligea,itm_short_bow,itm_bodkin_arrows,itm_old_gladius_2,itm_numidian_wig,itm_judean_tunic_5,itm_judean_tunic_4,itm_judean_tunic_2,itm_roman_poor1,itm_roman_poor2],
attrib_level_20, wpe(145,155,155,155), knows_archer_exp_eastern, north_african_man_face_younger_1, north_african_man_face_middle_2],
["egyptian_infantry_heavy", "Refbouts", "Refbouts", tf_male_north_african|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_egypt,
[itm_caligea,itm_legio_armored_caligea,itm_roman_gladius,itm_roman_gladius_2,itm_roman_gladius_3,itm_pilum,itm_auxilia_squamata_east_2,itm_auxilia_squamata_east_4,itm_auxilia_squamata_east_3,itm_auxilia_squamata_east_1,
itm_roman_aux_helm_8,itm_roman_aux_helm_11,itm_egyptian_shield_large_1,itm_egyptian_shield_large_2,itm_egyptian_shield_large_3,itm_egyptian_shield_large_4,itm_old_scutum,itm_old_scutum_2,itm_old_scutum_3,itm_old_scutum_4],
attrib_level_26, wp(160), knows_level_26, north_african_man_face_middle_1, north_african_man_face_old_2 ],
["egyptian_infantry_light", "Refqenqen", "Refqenqen",tf_male_north_african|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_egypt,
[itm_caligea,itm_hasta1,itm_pilum,itm_old_gladius_1,itm_numidian_wig,itm_judean_tunic_5,itm_judean_tunic_4,itm_judean_tunic_2,itm_roman_poor1,itm_roman_poor2,itm_egyptian_shield_large_1,itm_egyptian_shield_large_2,itm_egyptian_shield_large_3,itm_egyptian_shield_large_4,
itm_old_scutum,itm_old_scutum_2,itm_old_scutum_3,itm_old_scutum_4],
attrib_level_23, wp(140), knows_level_23,  north_african_man_face_young_1, north_african_man_face_middle_2 ],

##arabian mercenaries: p_town_19
["arab_noble_archers", "Hachar Hajar", "Hachar Hajar", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_nabataea,
[itm_arrows, itm_shortened_spear,itm_caligea,itm_arabian_bow_1,itm_arabian_bow_2,
itm_arabian_oval_shield_1,itm_arabian_oval_shield_2,itm_arabian_oval_shield_3,itm_arabian_oval_shield_4,itm_sarranid_mail_shirt,itm_arabian_armor_b,itm_desert_padded_hat_a,itm_archers_vest_2,itm_headcloth,itm_skirmisher_armor,
itm_sarranid_leather_armor,itm_centurio_east_graves]+desert_turbans_1,
attrib_level_23, wp(140), knows_level_23, eastern_man_face_middle_1, eastern_man_face_old_2 ],

["arab_spearmen", "Muqrabe", "Muqrabe", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_nabataea,
[itm_throwing_spears_east,itm_throwing_spears_east, itm_war_spear,itm_caligea,itm_arabian_tunic_1,itm_arabian_tunic_2,itm_arabian_tunic_3,
itm_arabian_oval_shield_1,itm_arabian_oval_shield_2,itm_arabian_oval_shield_3,itm_arabian_oval_shield_4,itm_arabian_armor_b,itm_skirmisher_armor,
itm_sarranid_leather_armor,itm_centurio_east_graves]+desert_turbans_1,
attrib_level_23, wp(140), knows_level_23, eastern_man_face_middle_1, eastern_man_face_old_2 ],

["desert_bandit", "Farasin", "Farasin",  tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_nabataea,
[itm_one_handed_battle_axe_a,itm_old_spear_1,itm_caligea,itm_throwing_spears,itm_throwing_spears,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_c,itm_arabian_tunic_1,itm_arabian_tunic_2,itm_arabian_tunic_3,
itm_leather_covered_round_shield,itm_ad_mixed_round_shields_14,itm_ad_mixed_round_shields_13,itm_camel]+horse_arab+desert_turbans_1,
attrib_level_18_warrior, wp_melee(155), knows_level_18_warrior, eastern_man_face_young_1, eastern_man_face_middle_2 ],

["arab_noble_cav", "Abbir Farasid", "Abbir Farasid",  tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_nabataea,
[itm_centurio_east_graves,itm_eastern_helm1,itm_eastern_helm2,itm_eastern_helm3,itm_eastern_helm4,itm_desert_padded_hat_a,itm_archers_vest_2,
itm_arabian_sword_a,itm_old_spear_2,itm_throwing_spears,itm_throwing_spears,
itm_sarranid_cavalry_robe,itm_archers_vest,itm_sarranid_mail_shirt,itm_arabian_armor_b,itm_camel,itm_ad_mixed_round_shields_15,
itm_ad_mixed_round_shields_16,itm_arabian_oval_shield_1,itm_arabian_oval_shield_2,itm_arabian_oval_shield_3,itm_arabian_oval_shield_4]+horse_arab+desert_turbans_1,
attrib_level_26, wp(150), knows_level_26, eastern_man_face_middle_1, eastern_man_face_older_2 ],

["palmyra_infantry", "Palmyraius Pedes", "Palmyraii Pedites",  tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_nabataea,
[itm_palmyran_gladius,itm_old_spear_2,itm_graves_simple_2,itm_armenian_helm_heavy_3,itm_mak_helm_3,itm_mak_helm_4,itm_throwing_spears_roman,itm_throwing_spears_roman,
itm_arabian_oval_shield_1,itm_arabian_oval_shield_2,itm_arabian_oval_shield_3,itm_arabian_oval_shield_4,itm_sarranid_cloth_robe_b,itm_sarranid_cloth_robe_c,
itm_pilos_chad,itm_palmyran_lamellar_armor,itm_palmyran_lamellar_armor_2,itm_palmyran_lamellar_armor_3]+desert_turbans_1,
attrib_level_29, wp(180), knows_level_29, eastern_man_face_young_1, eastern_man_face_middle_2 ],

["palmyra_cataphract", "Palmyraius Cataphractus", "Palmyraii Cataphracti",  tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse, no_scene, reserved, fac_nabataea,
[itm_palmyran_gladius_rich,itm_old_spear_2,itm_graves_simple_2,itm_mak_helm_3,itm_mak_helm_4,itm_old_round_shield_1,itm_old_round_shield_2,itm_old_round_shield_3,itm_old_round_shield_4,
itm_pilos_chad_2,itm_palmyran_lamellar_armor_heavy_1,itm_palmyran_lamellar_armor_heavy_2,itm_palmyran_lamellar_armor_heavy_3]+horse_arab,
attrib_level_29, wp(180), knows_level_29, eastern_man_face_middle_1, eastern_man_face_old_2 ],

["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,[],def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
##########################
#########################
#NEUE TRUPPEN
########################
########################
##hornman

["bosporan_standard_bearer", "Bosporan Standardbearer", "Bosporan Standardbearer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[]+sarmatian_boots+bosphoran_armor_mail_and_scale+sarmatian_helm_spangen+bosphoran_armor_scale+bosporan_standards,
attrib_level_31, wp_melee(210), knows_level_31, scythian_face_21, scythian_face_22 ],
["bosporan_hornman", "Bosporan Hornman", "Bosporan Hornmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_sarmatian_ringsword_4]+sarmatian_boots+bosphoran_armor_mail_and_scale+sarmatian_helm_spangen+bosphoran_armor_scale+bosporan_horns,
attrib_level_31, wp_melee(210), knows_level_31, scythian_face_21, scythian_face_22 ],

["judean_standard_bearer", "Judean Standardbearer", "Judean Standardbearers",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[]+roman_eastern_scale+jew_boots_heavy+jew_scale+jew_helm_heavy+judean_standards,
attrib_level_31, wp_melee(210), knows_level_31, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_hornman", "Judean Hornman", "Judean Hormen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[]+roman_eastern_scale+jew_boots_heavy+jew_scale+jew_helm_heavy+jew_swords+judean_horns,
attrib_level_31, wp_melee(210), knows_level_31, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["germanic_standard_bearer", "Germanic Standardbearer", "Germanic Standardbearers",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_1,itm_germanic_noble_2,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm4,
itm_germanic_helm3,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,itm_celtic_boots]+germanic_standards,
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],
["germanic_hornman", "Germanic Hornman", "Germanic Hornmen",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_1,itm_germanic_noble_2,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm4,
itm_germanic_helm3,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,
itm_sword_viking_1,itm_sword_viking_3,itm_sword_viking_4,itm_cheruski_sword,itm_celtic_boots]+germanic_horns,
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_standard_bearer", "Celtic Standardbearer", "Celtic Standardbearers",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_mail_normal+celtic_mail_noble+celtic_helmet_1+celtic_standards,
attrib_level_31_warrior, wp_melee(230), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],
["celtic_hornman", "Celtic Hornman", "Celtic Hornmen",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_mail_normal+celtic_mail_noble+celtic_helmet_1+celtic_swords_noble+celtic_horns,
attrib_level_31_warrior, wp_melee(230), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_standard_bearer", "Dacian Standardbearer", "Dacian Standardbearers",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy+dacian_standards,
attrib_level_31_warrior, wp_melee(210), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],
["dacian_hornman", "Dacian Hornman", "Dacian Hornmen",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_sword+dacian_sword_noble+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy+dacian_horns,
attrib_level_31_warrior, wp_melee(210), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["armenian_standard_bearer", "Armenian Standardbearer", "Armenian Standardbearers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[]+eastern_armor_scale_armenian+eastern_armor_mail_armenian+eastern_armor_scale_heavy_1+eastern_boots_light+armenian_helm_heavy+armenian_standards,
attrib_level_31, wp_melee(185), knows_level_31, armenian_face_young, armenian_face_middle ],
["armenian_hornman", "Armenian Hornman", "Armenian Hornmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_armenian_axe_1,itm_armenian_sword_1]+eastern_armor_scale_armenian+eastern_armor_mail_armenian+eastern_armor_scale_heavy_1+eastern_boots_light+armenian_helm_heavy+armenian_horns,
attrib_level_31, wp_melee(185), knows_level_31, armenian_face_young, armenian_face_middle ],

["caucasian_standard_bearer", "Caucasian Standardbearer", "Caucasian Standardbearers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[]+eastern_boots_light+caucasian_mail+caucasian_scale+caucasian_helm_heavy+caucasian_standards,
attrib_level_26, wp_melee(180), knows_level_26, armenian_face_young, armenian_face_middle ],
["caucasian_hornman", "Caucasian Hornman", "Caucasian Hornmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_caucasian_short_sword]+eastern_boots_light+caucasian_mail+caucasian_scale+caucasian_helm_heavy+caucasian_horns,
attrib_level_26, wp_melee(180), knows_level_26, armenian_face_young, armenian_face_middle ],

["parthian_standard_bearer", "Parthian Standardbearer", "Parthian Standardbearers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[]+eastern_boots_light+eastern_armor_mail_parthian+parthian_helm_infantry_heavy+parthian_standards,
attrib_level_26, wp_melee(180), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["parthian_hornman", "Parthian Horman", "Parthian Hornmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[]+eastern_boots_light+eastern_sword_short+eastern_armor_mail_parthian+parthian_helm_infantry_heavy+parthian_horns,
attrib_level_26, wp_melee(180), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],


# ["hornman", "Xenikos Moysikos", "Xenikoi Moysikoi", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
# [itm_leather_boots,itm_one_handed_war_axe_a,itm_bosporan_mail_2,itm_horn],
# attrib_level_18|level(40), wp_melee(130), knows_level_18, white_face_11, white_face_12],

# ##jewish troop
# ["judean_hornman", "Antolikos Moysikos", "Antolikoi Moysikoi", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
# [itm_horn]+jew_scale+jew_boots_simple+jew_helm_heavy+jew_swords,
# attrib_level_18|level(40), wp_melee(130), knows_level_18, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_light_clubman", "Judaioi Thureophores", "Judaioi Thureophoroi", tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[]+jew_boots_simple+jew_tunics_2+jew_robes+jew_helm_light+jew_swords_old+jew_spears+jew_shields_simple, attrib_level_18, wp_melee(120), knows_level_18, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_light_clubman_exp", "Judaioi Thureophores (exp)", "Judaioi Thureophoroi (exp)", tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[]+jew_boots_simple+jew_tunics_1+jew_mail_1+jew_helm_light+jew_swords_old+jew_spears+jew_shields_simple, attrib_level_20, wp_melee(140), knows_level_20, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_light_clubman_vet", "Judaioi Thureophores (vet)", "Judaioi Thureophoroi (vet)", tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_centurio_east_graves,itm_centurio_west_graves]+jew_boots_simple+jew_mail_2+jew_mail_1+jew_helm_heavy+jew_swords+jew_swords_old+jew_spears+jew_shields_large, attrib_level_23, wp_melee(160), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_light_spearman", "Ioudaioi Taxes", "Ioudaioi Taxeis", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman]+jew_boots_simple+jew_tunics_2+jew_tunics_1+jew_helm_light+jew_swords_old+jew_shields_simple, attrib_level_18, wp_melee(150), knows_level_18, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_light_spearman_exp", "Ioudaioi Taxes (exp)", "Ioudaioi Taxeis (exp)", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman]+jew_boots_simple+jew_tunics_2+jew_mail_2+jew_helm_light+jew_swords_old+jew_shields_simple, attrib_level_23, wp_melee(160), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_light_spearman_vet", "Ioudaioi Taxes (vet)", "Ioudaioi Taxeis (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_centurio_east_graves,itm_centurio_west_graves,itm_throwing_spears_roman,
itm_throwing_spears_roman]+jew_boots_simple+jew_mail_2+jew_mail_1+jew_helm_heavy+jew_swords+jew_swords_old+jew_shields_large, attrib_level_26, wp_melee(170), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_skirmisher", "Judaioi Peltastes", "Judaioi Peltastai", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman,itm_javelin]+jew_boots_simple+jew_tunics_1+jew_tunics_2+jew_helm_cloth+jew_spears+jew_shields_poor,
attrib_level_18, wpe(110,160,160,160), knows_level_18, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_skirmisher_exp", "Judaioi Peltastes (exp)", "Judaioi Peltastai (exp)", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman,itm_javelin]+jew_boots_simple+jew_tunics_1+jew_tunics_2+jew_helm_cloth+jew_shields_poor+jew_swords_old+jew_helm_light,
attrib_level_23, wpe(120,175,175,175), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_skirmisher_vet", "Judaioi Peltastes (vet)", "Judaioi Peltastai (vet)", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman,itm_javelin]+jew_boots_simple+jew_tunics_1+jew_tunics_2+old_roman_roundshields+jew_swords_old+jew_helm_light,
attrib_level_26, wpe(130,190,190,190), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_slinger", "Ioudaioi Sphendonetes", "Ioudaioi Sphendonetai", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_sling,itm_sling_rock1,itm_hide_covered_round_shield,itm_hide_covered_round_shield_2,itm_club,itm_club_2,itm_club_3]+jew_boots_simple+jew_robes+jew_tunics_1+jew_helm_cloth,
attrib_level_12, wpe(90,160,160,160), knows_archer_basic, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_slinger_exp", "Ioudaioi Sphendonetes (exp)", "Ioudaioi Sphendonetai (exp)", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_sling,itm_sling_rock1,itm_sling_lead,itm_hide_covered_round_shield,itm_hide_covered_round_shield_2]+jew_boots_simple+jew_tunics_2+jew_tunics_1+jew_swords_old+jew_helm_cloth,
attrib_level_16, wpe(100,175,175,175), knows_archer_exp, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_slinger_vet", "Ioudaioi Sphendonetes (vet)", "Ioudaioi Sphendonetai (vet)", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_sling,itm_sling_lead]+jew_boots_simple+jew_tunics_2+jew_tunics_1+jew_swords_old+jew_helm_light+old_roman_roundshields,
attrib_level_20, wpe(110,190,190,190), knows_archer_elit, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_archer", "Ioudaioi Toxotes", "Ioudaioi Toxotai", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_arrows,itm_short_bow]+jew_boots_simple+jew_tunics_1+jew_tunics_2+jew_helm_light+jew_helm_cloth+jew_swords_old,
attrib_level_12, wpe(100,160,160,160), knows_archer_basic, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_archer_exp", "Ioudaioi Toxotes (exp)", "Ioudaioi Toxotai (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_barbed_arrows,itm_nomad_bow]+jew_boots_simple+jew_tunics_1+jew_tunics_2+jew_helm_light+jew_swords_old,
attrib_level_18, wpe(110,175,175,175), knows_archer_exp, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_archer_vet", "Ioudaioi Toxotes (vet)", "Ioudaioi Toxotai (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_8,
[itm_bodkin_arrows,itm_nomad_bow]+jew_boots_simple+jew_mail_1+jew_tunics_1+jew_helm_heavy+jew_swords_old,
attrib_level_23, wpe(120,190,190,190), knows_archer_elit, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_elite", "Ioudaioi Thorakites", "Ioudaioi Thorakitai",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman]+roman_eastern_scale+jew_boots_simple+jew_boots_heavy+jew_mail_1+jew_mail_2+jew_helm_light+jew_spears+jew_shields_simple+jew_shields_large+jew_swords+jew_helm_heavy,
attrib_level_26, wp_melee(160), knows_level_26, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_elite_exp", "Ioudaioi Thorakites (exp)", "Ioudaioi Thorakitai (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman]+roman_eastern_scale+jew_boots_heavy+jew_scale+jew_mail_2+jew_helm_heavy+jew_spears+jew_shields_large+jew_swords,
attrib_level_29, wp_melee(180), knows_level_29, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_elite_vet", "Ioudaioi Thorakites (vet)", "Ioudaioi Thorakitai (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[itm_throwing_spears_roman,itm_throwing_spears_roman]+roman_eastern_scale+jew_boots_heavy+jew_scale+jew_helm_heavy+jew_shields_large+jew_swords,
attrib_level_31, wp_melee(210), knows_level_31, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_cav", "Ioudaioi Hippakontistes", "Ioudaioi Hippakontistai",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_javelin]+horse_parth+jew_boots_simple+jew_mail_2+jew_mail_1+jew_helm_light+jew_helm_heavy+jew_spears+old_roman_roundshields,
attrib_level_23, wp_melee(130), knows_level_26, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["judean_cav_exp", "Ioudaioi Hippakontistes (exp)", "Ioudaioi Hippakontistai (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_javelin]+horse_parth+jew_boots_heavy+jew_mail_2+jew_mail_1+jew_helm_heavy+jew_spears+old_roman_roundshields,
attrib_level_26, wp_melee(150), knows_level_29, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["judean_cav_vet", "Ioudaioi Hippakontistes (vet)", "Ioudaioi Hippakontistai (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_javelin]+horse_parth+jew_boots_heavy+jew_mail_1+jew_scale+jew_helm_heavy+jew_spears+old_roman_roundshields,
attrib_level_29, wp_melee(170), knows_level_31, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["judean_guard","Sebastenoi Peltastes","Sebastenoi Peltastai",tf_guarantee_soldier,0,0,fac_neutral,
[itm_throwing_spears_roman]
+jew_linothorax+jew_phalanx_gear+jew_swords_greek+jew_boots_heavy+jew_boots_simple+jew_helm_heavy
+jew_helm_light+jew_mail_1+jew_mail_2+jew_scale+jew_shields_large+jew_shields_poor+jew_swords+jew_spears,
 attrib_level_29,wp(170),knows_level_29, arab_face_young, arab_face_old],
["judean_guard_vet","Sebastenoi Peltastes","Sebastenoi Peltastai (vet)",tf_guarantee_soldier,0,0,fac_neutral,
[itm_throwing_spears_roman]
+jew_linothorax+jew_phalanx_gear+jew_swords_greek+jew_boots_heavy+jew_boots_simple+jew_helm_heavy
+jew_helm_light+jew_mail_1+jew_mail_2+jew_scale+jew_shields_large+jew_shields_poor+jew_swords+jew_spears,
 attrib_level_31_warrior,wp(190),knows_level_29_warrior, arab_face_young, arab_face_old],

["judean_guard_archer","Sebastenoi Toxotes","Sebastenoi Toxotai",tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,
[itm_throwing_spears_roman,itm_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_german_shortbow,itm_short_bow,itm_nomad_bow,itm_long_bow,
itm_strong_bow,itm_war_bow,itm_nubian_war_bow,itm_khergit_bow_2,itm_khergit_bow]
+jew_linothorax+jew_phalanx_gear+jew_swords_greek+jew_boots_heavy+jew_boots_simple+jew_helm_heavy+jew_helm_light
+jew_mail_1+jew_mail_2+jew_scale+jew_shields_large+jew_shields_poor+jew_swords+jew_spears,
 attrib_level_29,wpe(100,170,170,170),knows_archer_elit, arab_face_young, arab_face_old],
["judean_guard_archer_vet","Sebastenoi Toxotes","Sebastenoi Toxotai (vet)",tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,
[itm_throwing_spears_roman,itm_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_german_shortbow,itm_short_bow,itm_nomad_bow,itm_long_bow,
itm_strong_bow,itm_war_bow,itm_nubian_war_bow,itm_khergit_bow_2,itm_khergit_bow]
+jew_linothorax+jew_phalanx_gear+jew_swords_greek+jew_boots_heavy+jew_boots_simple+jew_helm_heavy+jew_helm_light
+jew_mail_1+jew_mail_2+jew_scale+jew_shields_large+jew_shields_poor+jew_swords+jew_spears,
 attrib_level_31_warrior,wpe(110,190,190,190),knows_archer_elit_eastern, arab_face_young, arab_face_old],

##Bosporan troops
["bosporan_light_spearman", "Entopioi", "Entopioi", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_celtic_boots,
itm_throwing_spears,itm_sarmatian_sword_2,itm_spear,itm_shortened_spear,
itm_bosphoran_shield_new_1,itm_bosphoran_shield_new_2,itm_bosphoran_shield_new_3,itm_bosphoran_shield_new_4,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
], attrib_level_23, wp_melee(150), knows_level_23, scythian_face_21, scythian_face_22 ],
["bosporan_light_spearman_exp", "Entopioi (exp)", "Entopioi (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_celtic_boots,
itm_throwing_spears,itm_sarmatian_sword_1,itm_spear,itm_shortened_spear,
itm_bosphoran_shield_new_1,itm_bosphoran_shield_new_2,itm_bosphoran_shield_new_3,itm_bosphoran_shield_new_4,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
], attrib_level_26, wp_melee(160), knows_level_26, scythian_face_21, scythian_face_22 ],
["bosporan_light_spearman_vet", "Entopioi (vet)", "Entopioi (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_celtic_boots,
itm_throwing_spears,itm_sarmatian_ringsword_1,itm_spear,itm_shortened_spear,
itm_bosphoran_shield_new_1,itm_bosphoran_shield_new_2,itm_bosphoran_shield_new_3,itm_bosphoran_shield_new_4,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
], attrib_level_29, wp_melee(170), knows_level_29, scythian_face_21, scythian_face_22 ],

["bosporan_archer", "Toxotes", "Toxotia", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_9,
[itm_celtic_boots,
itm_sarmatian_ringsword_1,
itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_light4,itm_sarmatian_light3,itm_sarmatian_light2,itm_sarmatian_light1,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
itm_scythian_shield_cav1,itm_scythian_shield_cav2,
],
attrib_level_18, wpe(100,150,150,150), knows_archer_basic_eastern, scythian_face_11, scythian_face_12 ],
["bosporan_archer_exp", "Toxotes (exp)", "Toxotia (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_9,
[
itm_celtic_boots,
itm_sarmatian_ringsword_2,
itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_light4,itm_sarmatian_light3,itm_sarmatian_light2,itm_sarmatian_light1,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
itm_scythian_shield_cav5,itm_scythian_shield_cav6,
],
attrib_level_20, wpe(110,170,170,170), knows_archer_exp_eastern, scythian_face_11, scythian_face_12 ],
["bosporan_archer_vet", "Toxotes (vet)", "Toxotia (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_9,
[
itm_celtic_boots,
itm_sarmatian_sword_1,
itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
itm_bosporan_light1,itm_bosporan_light2,itm_bosporan_light3,itm_bosporan_light4,
itm_sarmatian_light4,itm_sarmatian_light3,itm_sarmatian_light2,itm_sarmatian_light1,
itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_bosporan_spangenhelm_3,
itm_scythian_shield_cav3,itm_scythian_shield_cav4,
],
attrib_level_23, wpe(120,190,190,190), knows_archer_elit_eastern, scythian_face_11, scythian_face_12 ],

["bosporan_elite", "Bosporion Pezikon", "Bosporion Pezikon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_throwing_spears,itm_sarmatian_ringsword_4,itm_sarmatian_spear_169,
 itm_bosporan_oval_color_1,itm_bosporan_oval_color_2,itm_bosporan_oval_color_3,itm_bosporan_oval_color_4,itm_bosporan_oval_color_5,
]+sarmatian_boots+bosphoran_armor_mail+sarmatian_helm_spangen,
attrib_level_26, wp_melee(160), knows_level_26, scythian_face_21, scythian_face_22 ],
["bosporan_elite_exp", "Bosporion Pezikon (exp)", "Bosporion Pezikon (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_throwing_spears,itm_throwing_spears,itm_sarmatian_ringsword_4,itm_sarmatian_spear_169,
 itm_bosporan_oval_color_1,itm_bosporan_oval_color_2,itm_bosporan_oval_color_3,itm_bosporan_oval_color_4,itm_bosporan_oval_color_5,
]+sarmatian_boots+bosphoran_armor_mail_and_scale+bosphoran_armor_mail+sarmatian_helm_spangen,
attrib_level_29, wp_melee(180), knows_level_29, scythian_face_21, scythian_face_22 ],
["bosporan_elite_vet", "Bosporion Pezikon (vet)", "Bosporion Pezikon (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[itm_throwing_spears,itm_throwing_spears,itm_sarmatian_ringsword_4,itm_sarmatian_spear_169,
 itm_bosporan_oval_color_1,itm_bosporan_oval_color_2,itm_bosporan_oval_color_3,itm_bosporan_oval_color_4,itm_bosporan_oval_color_5,
]+sarmatian_boots+bosphoran_armor_mail_and_scale+sarmatian_helm_spangen+bosphoran_armor_scale,
attrib_level_31, wp_melee(210), knows_level_31, scythian_face_21, scythian_face_22 ],

["bosporan_cav", "Kataphraktos Sauromate", "Kataphraktos Sauromate", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[]+horse_steppe_cataphract+sarmatian_ringswords_long+sarmatian_helm_pointed+bosphoran_armor_mail_and_scale+sarmatian_armor_mail_and_scale_1+sarmatian_boots+kontos_long,
attrib_level_23, wp_melee(130), knows_level_26, scythian_face_11, scythian_face_12 ],
["bosporan_cav_exp", "Kataphraktos Sauromate (exp)", "Kataphraktos Sauromate (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[]+horse_steppe_cataphract+sarmatian_ringswords_long+sarmatian_helm_pointed+bosphoran_armor_scale+sarmatian_armor_mail_and_scale_2+sarmatian_boots+kontos_long,
attrib_level_26, wp_melee(150), knows_level_29, scythian_face_11, scythian_face_12 ],
["bosporan_cav_vet", "Kataphraktos Sauromate (vet)", "Kataphraktos Sauromate (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_9,
[]+horse_steppe_cataphract+sarmatian_ringswords_long+sarmatian_helm_pointed+sarmatian_armor_scale+bosphoran_armor_scale+sarmatian_boots+kontos_long,
attrib_level_29, wp_melee(170), knows_level_31, scythian_face_11, scythian_face_12 ],

#germanic troops
["germanic_light_clubman", "Slaganz", "Slaganz",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_club,itm_club_2,itm_club_3,itm_cheruski_ax,itm_germanic_shield_1,itm_germanic_shield_2,itm_germanic_shield_3,itm_germanic_shield_4,itm_jarid,itm_jarid]+germanic_caps+germanic_armor_tunics_2+germanic_armor_tunics_3,
attrib_level_12_warrior, wp_melee(150), knows_level_12_warrior|knows_athletics_8, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_light_clubman_exp", "Slaganz (exp)", "Slaganz (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_germanic_shield_large5,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,
itm_club,itm_club_2,itm_club_3,itm_cheruski_ax,
itm_jarid,itm_jarid]+germanic_caps+germanic_armor_tunics_1+germanic_armor_tunics_2+germanic_armor_fur_3,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior|knows_athletics_9, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_light_clubman_vet", "Slaganz (vet)", "Slaganz (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_germanic_shield_large9,itm_germanic_shield_large10,itm_germanic_shield_large11,itm_germanic_shield_large12,
itm_one_handed_battle_axe_c,itm_cheruski_ax,itm_cheruski_sword,itm_germanic_axe3,itm_fighting_axe,itm_jarid,itm_jarid,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4]+germanic_caps+germanic_armor_tunics_2+germanic_armor_tunics_1+germanic_armor_fur_1,
attrib_level_23_warrior, wp_melee(190), knows_level_23_warrior|knows_athletics_10, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_light_spearman", "Gaizafulkan Frijato", "Gaizafulkan Frijato",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_shield_1,
itm_germanic_war_spear_3,itm_germanic_war_spear_2,itm_germanic_war_spear,
itm_germanic_shield_large5,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,
itm_germanic_shortened_spear,itm_jarid,itm_jarid]+germanic_caps+germanic_armor_tunics_1+germanic_armor_tunics_3,
attrib_level_12_warrior, wp_melee(155), knows_level_12_warrior|knows_athletics_8, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_light_spearman_exp", "Gaizafulkan Frijato (exp)", "Gaizafulkan Frijato (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_shield_1,
itm_germanic_war_spear_3,itm_germanic_war_spear_2,itm_germanic_war_spear,
itm_germanic_shield_large9,itm_germanic_shield_2,itm_germanic_shield_3,itm_germanic_shield_large12,
itm_germanic_shortened_spear,itm_jarid,itm_jarid]+germanic_caps+germanic_armor_tunics_2+germanic_armor_tunics_2+germanic_armor_fur_2,
attrib_level_18_warrior, wp_melee(175), knows_level_18_warrior|knows_athletics_9, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_light_spearman_vet", "Gaizafulkan Frijato (vet)", "Gaizafulkan Frijato (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_war_spear_3,itm_germanic_war_spear_2,itm_germanic_war_spear,
itm_germanic_shield_large1,itm_germanic_shield_large2,itm_germanic_shield_large3,itm_germanic_shield_large4,
itm_germanic_shortened_spear,itm_jarid,itm_jarid,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4]+germanic_caps+germanic_armor_tunics_3+germanic_armor_tunics_1+germanic_armor_fur_1,
attrib_level_23_warrior, wp_melee(190), knows_level_23_warrior|knows_athletics_10, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_skirmisher", "Jugunthiz", "Jugunthiz",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_throwing_spears,itm_throwing_spears,itm_javelin,
itm_germanic_shield_large9,itm_germanic_shield_large10,itm_germanic_shield_large11,itm_germanic_shield_large12,
itm_club,itm_club_2,itm_club_3,
itm_celtic_boots,]+germanic_caps+germanic_armor_pants_1+germanic_armor_pants_3+germanic_armor_tunics_3,
attrib_level_12_warrior, wpe(110,140,140,140), knows_level_12_warrior|knows_athletics_8, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_skirmisher_exp", "Jugunthiz (exp)", "Jugunthiz (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_throwing_spears,itm_throwing_spears,itm_javelin,
itm_germanic_shield_large5,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,
itm_club,itm_club_2,itm_club_3,
itm_celtic_boots,]+germanic_caps+germanic_armor_pants_3+germanic_armor_pants_2+germanic_armor_tunics_2,
attrib_level_18_warrior, wpe(120,160,160,160), knows_level_18_warrior|knows_athletics_9, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_skirmisher_vet", "Jugunthiz (vet)", "Jugunthiz (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_throwing_spears,itm_throwing_spears,itm_javelin,
itm_germanic_shield_large1,itm_germanic_shield_large2,itm_germanic_shield_large3,itm_germanic_shield_large4,itm_cheruski_sword,itm_cheruski_ax,
itm_fighting_axe,itm_germanic_axe2,itm_germanic_axe1,itm_celtic_boots,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4]+germanic_caps+germanic_armor_pants_1+germanic_armor_pants_2+germanic_armor_tunics_1,
attrib_level_23_warrior, wpe(130,180,180,180), knows_level_23_warrior|knows_athletics_10, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_slinger", "Stoinowerponez", "Stoinowerponez",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_sling,
itm_club,itm_club_2,itm_club_3,itm_sling_rock1]+germanic_caps+germanic_armor_pants_1+germanic_armor_pants_2+germanic_armor_tunics_2,
attrib_level_12_warrior, wpe(100,145,145,145), knows_archer_basic|knows_athletics_8, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_slinger_exp", "Stoinowerponez (exp)", "Stoinowerponez (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_sling,
itm_club,itm_club_2,itm_club_3,itm_sling_rock1]+germanic_caps+germanic_armor_pants_2+germanic_armor_pants_3+germanic_armor_tunics_3,
attrib_level_16_warrior, wpe(110,170,170,170), knows_archer_exp|knows_athletics_9, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_slinger_vet", "Stoinowerponez (vet)", "Stoinowerponez (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_sling,
itm_club,itm_club_2,itm_club_3,itm_sling_lead]+germanic_caps+germanic_armor_pants_3+germanic_armor_pants_1+germanic_armor_tunics_1,
attrib_level_20_warrior, wpe(120,185,185,185), knows_archer_elit|knows_athletics_10, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_archer", "Sakutones", "Sakutones",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_mace_1,itm_spiked_club,itm_german_shortbow,itm_arrows]+germanic_caps+germanic_armor_pants_3+germanic_armor_pants_2+germanic_armor_tunics_1,
attrib_level_12_warrior, wpe(100,140,140,140), knows_archer_basic|knows_athletics_8, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_archer_exp", "Sakutones (exp)", "Sakutones (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_mace_1,itm_spiked_club,itm_arrows,itm_long_bow,itm_german_shortbow]+germanic_caps+germanic_armor_pants_2+germanic_armor_pants_1+germanic_armor_tunics_2,
attrib_level_18_warrior, wpe(110,160,160,160), knows_archer_exp|knows_athletics_9, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_archer_vet", "Sakutones (vet)", "Sakutones (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,
itm_germanic_axe2,itm_one_handed_battle_axe_a,itm_long_bow,itm_arrows]+germanic_caps+germanic_armor_fur_2+germanic_armor_pants_2+germanic_armor_tunics_3,
attrib_level_23_warrior,wpe(120,180,180,180), knows_archer_elit|knows_athletics_10, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_berserker", "Tiwaz Drutiz", "Tiwaz Drutiz",tf_male_barbarian|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots, no_scene, reserved, fac_culture_4,
[itm_germanic_completenaked1,itm_germanic_completenaked2,itm_germanic_completenaked3,itm_germanic_completenaked4,
itm_germanic_completenaked5,itm_germanic_completenaked6,itm_fighting_axe,itm_germanic_axe3,
itm_germanic_shield_large1,itm_germanic_shield_large3,itm_germanic_shield_large5,itm_germanic_shield_large7,itm_germanic_shield_large9,itm_germanic_shield_large11,
itm_jarid,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4,itm_celtic_boots],
attrib_level_31_warrior, wp_melee(240), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["germanic_noble_swordsman", "Druthinaz Swebusku", "Druthinaz Swebusku",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_1,itm_germanic_noble_2,itm_germanic_helm1,itm_germanic_helm2,
itm_germanic_helm3,itm_germanic_helm4,itm_germanic_shield_1,itm_germanic_shield_4,itm_germanic_shield_large2,itm_germanic_shield_large3,itm_germanic_shield_large4,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,
itm_sax1,itm_sword_viking_2,itm_cheruski_sword,itm_celtic_boots,itm_jarid],
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_noble_swordsman_exp", "Druthinaz Swebusku (exp)", "Druthinaz Swebusku (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_1,itm_germanic_noble_2,itm_germanic_helm1,itm_germanic_helm2,
itm_germanic_helm3,itm_germanic_helm4,
itm_germanic_shield_large5,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4,
itm_sax1,itm_sword_viking_2,itm_cheruski_sword,itm_celtic_boots,itm_jarid],
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_noble_swordsman_vet", "Druthinaz Swebusku (vet)", "Druthinaz Swebusku (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_1,itm_germanic_noble_2,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm4,
itm_germanic_helm3,itm_germanic_shield_1,
itm_germanic_shield_large9,itm_germanic_shield_large10,itm_germanic_shield_large11,itm_germanic_shield_large12,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,
itm_sword_viking_1,itm_sword_viking_3,itm_sword_viking_4,itm_cheruski_sword,itm_celtic_boots,itm_jarid],
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_noble_spearman", "Dugunthiz", "Dugunthiz",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_3,itm_germanic_noble_4,itm_germanic_helm1,itm_germanic_helm2,
itm_germanic_helm3,itm_celtic_boots,itm_germanic_war_spear,itm_germanic_helm4,itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4,
itm_germanic_shield_large5,itm_germanic_shield_large6,itm_germanic_shield_large7,itm_germanic_shield_large8,itm_jarid,],
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_noble_spearman_exp", "Dugunthiz (exp)", "Dugunthiz (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_3,itm_germanic_noble_4,itm_germanic_helm1,itm_germanic_helm2,
itm_germanic_helm3,itm_celtic_boots,itm_germanic_war_spear,itm_germanic_helm4,itm_germanic_noble_tunic_1,itm_germanic_noble_tunic_2,
itm_germanic_shield_large9,itm_germanic_shield_large10,itm_germanic_shield_large11,itm_germanic_shield_large12,itm_jarid,],
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_noble_spearman_vet", "Dugunthiz (vet)", "Dugunthiz (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_heavy2,itm_germanic_noble_3,itm_germanic_noble_4,itm_germanic_helm1,itm_germanic_helm2,
itm_germanic_helm3,itm_germanic_helm4,itm_germanic_shield_1,
itm_germanic_shield_4,itm_germanic_shield_large2,itm_germanic_shield_large3,itm_germanic_shield_large4,itm_germanic_noble_tunic_3,itm_germanic_noble_tunic_4,
itm_celtic_boots,itm_germanic_war_spear,itm_jarid,],
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["germanic_cavalry", "Ridanz", "Ridanz",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large2,itm_germanic_shield_hex_large3,itm_germanic_shield_hex_large4,itm_germanic_shield_hex_large5,itm_germanic_shield_hex_large6,
itm_germanic_war_spear_3,itm_germanic_war_spear_2,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4,
itm_germanic_naked1,itm_germanic_naked2,itm_germanic_naked4,itm_germanic_naked5,itm_germanic_naked6,itm_germanic_naked7,
]+horse_normal,
attrib_level_23_warrior, wp_melee(170), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_cavalry_exp", "Ridanz (exp)", "Ridanz (exp)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large2,itm_germanic_shield_hex_large3,itm_germanic_shield_hex_large4,itm_germanic_shield_hex_large5,itm_germanic_shield_hex_large6,
itm_germanic_war_spear_3,itm_germanic_war_spear_2,
itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4,
itm_germanic_light1,itm_germanic_light2,itm_germanic_light3,itm_germanic_light4,itm_germanic_light5,itm_germanic_light6,itm_germanic_light7,itm_germanic_light8,itm_germanic_light9,
]+horse_normal,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["germanic_cavalry_vet", "Ridanz (vet)", "Ridanz (vet)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_4,
[itm_celtic_boots,itm_germanic_shield_hex_large1,itm_germanic_shield_hex_large2,itm_germanic_shield_hex_large3,itm_germanic_shield_hex_large4,itm_germanic_shield_hex_large5,itm_germanic_shield_hex_large6,
itm_germanic_war_spear_3,itm_germanic_war_spear_2,
itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,itm_germanic_helm4,
itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6]+horse_normal,
attrib_level_29_warrior, wp_melee(190), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

#briton troops
["celtic_light_clubman", "Lorgowiri", "Lorgowiri",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_club,itm_club_2,itm_club_3]+celtic_tunics_1+celtic_tunics_2+celtic_oval_shield+celtic_throwing+celtic_helmet_coolus_old,
attrib_level_12_warrior, wp_melee(145), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_light_clubman_exp", "Lorgowiri (exp)", "Lorgowiri (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_club,itm_club_2,itm_club_3]+celtic_tunics_1+celtic_tunics_2+celtic_oval_shield+celtic_throwing+celtic_helmet_coolus_old,
attrib_level_18_warrior, wp_melee(165), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_light_clubman_vet", "Lorgowiri (vet)", "Lorgowiri (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_1+celtic_tunics_2+celtic_oval_shield+celtic_throwing+celtic_helmet_coolus_new+celtic_axes,
attrib_level_23_warrior, wp_melee(180), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_light_spearman", "Slegowiri", "Slegowiri",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_1+celtic_spear+celtic_tunics_2+celtic_shield_weird_1+celtic_throwing+celtic_helmet_coolus_old,
attrib_level_12_warrior, wp_melee(150), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_light_spearman_exp", "Slegowiri (exp)", "Slegowiri (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_1+celtic_spear+celtic_tunics_2+celtic_shield_weird_1+celtic_throwing+celtic_helmet_coolus_old,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_light_spearman_vet", "Slegowiri (vet)", "Slegowiri (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_tunics_1+celtic_tunics_2+celtic_shield_weird_1+celtic_spear+celtic_throwing+celtic_helmet_coolus_new,
attrib_level_23_warrior, wp_melee(190), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_naked_swordman", "Kladiwoi", "Kladiwoi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[]+celtic_painted_1+celtic_helmet_1+celtic_swords_noble+celtic_shield_long+celtic_hex_shield+celtic_throwing,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_naked_swordman_exp", "Kladiwoi (exp)", "Kladiwoi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[]+celtic_painted_1+celtic_helmet_1+celtic_swords_noble+celtic_shield_long+celtic_hex_shield+celtic_throwing,
 attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_naked_swordman_vet", "Kladiwoi (vet)", "Kladiwoi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[]+celtic_painted_1+celtic_helmet_1+celtic_swords_noble+celtic_shield_long+celtic_hex_shield+celtic_throwing,
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_skirmisher", "Gaisowiri", "Gaisowiri",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+celtic_pants_1+celtic_tunics_1+celtic_spear+celtic_throwing+celtic_shield_round+celtic_helmet_1,
attrib_level_12_warrior, wpe(110,150,150,150), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_skirmisher_exp", "Gaisowiri (exp)", "Gaisowiri(exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+celtic_pants_2+celtic_tunics_1+celtic_spear+celtic_throwing+celtic_shield_round+celtic_helmet_1,
attrib_level_18_warrior, wpe(120,170,170,170), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_skirmisher_vet", "Gaisowiri (vet)", "Gaisowiri (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+celtic_pants_3+celtic_tunics_1+celtic_spear+celtic_throwing+celtic_shield_round+celtic_helmet_1,
attrib_level_23_warrior, wpe(130,190,190,190), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_archer", "Arkwioi", "Arkwioi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_pants_3+celtic_tunics_2+celtic_axes+celtic_bow_1,
attrib_level_12_warrior, wpe(100,150,150,150), knows_archer_basic, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_archer_exp", "Arkwioi (exp)", "Arkwioi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_pants_2+celtic_tunics_2+celtic_axes+celtic_bow_1,
attrib_level_18_warrior, wpe(110,170,170,170), knows_archer_exp, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_archer_vet", "Arkwioi (vet)", "Arkwioi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_pants_1+celtic_tunics_2+celtic_axes+celtic_bow_2+celtic_helmet_coolus_old,
attrib_level_23_warrior, wpe(120,190,190,190), knows_archer_elit, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_horseman", "Markakoi Gaisowiri", "Markakoi Gaisowiri",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+horse_normal+celtic_shield_round+celtic_hex_shield+celtic_tunics_2+celtic_mail_normal+celtic_spear+celtic_swords+celtic_helmet_1+celtic_helmet_coolus_new,
attrib_level_23_warrior, wp_melee(165), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_horseman_exp", "Markakoi Gaisowiri (exp)", "Markakoi Gaisowiri (exp)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+horse_normal+celtic_shield_round+celtic_hex_shield+celtic_tunics_2+celtic_mail_normal+celtic_spear+celtic_swords+celtic_helmet_1+celtic_helmet_coolus_new,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_horseman_vet", "Markakoi Gaisowiri (vet)", "Markakoi Gaisowiri (vet)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2,
[itm_celtic_boots,itm_javelin]+horse_normal+celtic_shield_round+celtic_hex_shield+celtic_tunics_2+celtic_mail_normal+celtic_spear+celtic_swords+celtic_helmet_1+celtic_helmet_coolus_new,
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["celtic_noble_swords", "Wenoi", "Wenoi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_throwing+celtic_shield_long+celtic_shield_weird_2+celtic_mail_normal+celtic_mail_noble+celtic_helmet_1+celtic_swords_noble+celtic_swords,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_noble_swords_exp", "Wenoi (exp)", "Wenoi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_throwing+celtic_shield_long+celtic_shield_weird_1+celtic_mail_normal+celtic_mail_noble+celtic_helmet_1+celtic_swords_noble,
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["celtic_noble_swords_vet", "Wenoi (vet)", "Wenoi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_celtic_boots]+celtic_throwing+celtic_shield_long+celtic_hex_shield+celtic_mail_normal+celtic_mail_noble+celtic_helmet_1+celtic_swords_noble,
attrib_level_31_warrior, wp_melee(230), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

#caledonian troops
["caledonian_light_clubman", "Lorgowiri", "Lorgowiri",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_club,itm_club_2,itm_club_3,itm_britton_coolus_plume]+celtic_pants_2+celtic_tunics_2+caledonian_shield_h,
attrib_level_12_warrior, wp_melee(150), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_light_clubman_exp", "Lorgowiri (exp)", "Lorgowiri (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_club,itm_club_2,itm_club_3,itm_britton_coolus_plume]+celtic_pants_1+celtic_tunics_2+caledonian_shield_h,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_light_clubman_vet", "Lorgowiri (vet)", "Lorgowiri (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_club,itm_club_2,itm_club_3,itm_britton_coolus_plume]+celtic_pants_3+celtic_tunics_2+caledonian_shield_h,
attrib_level_23_warrior, wp_melee(185), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["caledonian_light_spearman", "Kombrogoi", "Kombrogoi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_britton_coolus_plume]+celtic_spear+celtic_pants_1+celtic_tunics_1+celtic_oval_shield,
attrib_level_12_warrior, wp_melee(150), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_light_spearman_exp", "Kombrogoi (exp)", "Kombrogoi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_britton_coolus_plume]+celtic_spear+celtic_pants_3+celtic_tunics_2+celtic_oval_shield,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_light_spearman_vet", "Kombrogoi (vet)", "Kombrogoi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_throwing_spears,itm_britton_coolus_plume]+celtic_spear+celtic_pants_2+celtic_tunics_1+celtic_oval_shield,
attrib_level_23_warrior, wp_melee(190), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["caledonian_naked_swordman", "Teceitos", "Teceitos",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+caledonian_axes+caledonian_shield+celtic_helmet_2+celtic_mail_normal+celtic_throwing,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_naked_swordman_exp", "Teceitos (exp)", "Teceitos (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+caledonian_axes+caledonian_shield+celtic_helmet_2+celtic_mail_normal+celtic_throwing,
 attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_naked_swordman_vet", "Teceitos (vet)", "Teceitos (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+caledonian_axes+caledonian_shield+celtic_helmet_2+celtic_mail_normal+celtic_throwing,
attrib_level_31_warrior, wp_melee(220), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["caledonian_skirmisher", "Gaisowiri", "Gaisowiri",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_2_1,
[itm_javelin,itm_javelin]+celtic_painted_1+celtic_shield_round+celtic_spear,
attrib_level_12_warrior, wpe(110,150,150,150), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_skirmisher_exp", "Gaisowiri (exp)", "Gaisowiri(exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_2_1,
[itm_javelin,itm_javelin]+celtic_painted_1+celtic_shield_round+celtic_spear,
attrib_level_18_warrior, wpe(120,170,170,170), knows_level_18_warrior, celtic_face_21, barbarian_man_face_middle_2 ],
["caledonian_skirmisher_vet", "Gaisowiri (vet)", "Gaisowiri (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_javelin,itm_javelin]+celtic_painted_1+celtic_shield_round+celtic_spear,
attrib_level_23_warrior, wpe(130,190,190,190), knows_level_23_warrior, celtic_face_21, barbarian_man_face_old_2 ],

["caledonian_archer", "Arkwioi", "Arkwioi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_club,itm_club_2,itm_club_3]+celtic_bow_1+celtic_tunics_1+celtic_tunics_2,
attrib_level_12_warrior, wpe(100,150,150,150), knows_archer_basic, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_archer_exp", "Arkwioi (exp)", "Arkwioi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_club,itm_club_2,itm_club_3]+celtic_bow_1+celtic_tunics_1+celtic_tunics_2,
attrib_level_18_warrior, wpe(110,170,170,170), knows_archer_exp, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_archer_vet", "Arkwioi (vet)", "Arkwioi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots,itm_club,itm_club_2,itm_club_3]+celtic_bow_1+celtic_tunics_1+celtic_tunics_2,
attrib_level_23_warrior, wpe(120,190,190,190), knows_archer_elit, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["caledonian_horseman", "Markakoi Trummoi", "Markakoi Trummoi",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+horse_normal+caledonian_shield_h+celtic_spear+celtic_swords+celtic_mail_normal+celtic_tunics_2+celtic_helmet_2,
attrib_level_23_warrior, wp_melee(165), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_horseman_exp", "Markakoi Trummoi (exp)", "Markakoi Trummoi (exp)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+horse_normal+caledonian_shield_h+celtic_spear+celtic_swords+celtic_mail_normal+celtic_tunics_2+celtic_helmet_2,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_horseman_vet", "Markak<<oi Trummoi (vet)", "Markakoi Trummoi (vet)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+horse_normal+caledonian_shield_h+celtic_spear+celtic_swords+celtic_mail_normal+celtic_tunics_2+celtic_helmet_2,
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["caledonian_noble_swords", "Kluddobros", "Kluddobros",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+celtic_swords_noble+celtic_throwing+caledonian_shield+caledonian_shield_h+celtic_mail_noble+celtic_mail_normal+celtic_helmet_2,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["caledonian_noble_swords_exp", "Kluddobros (exp)", "Kluddobros (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+celtic_swords_noble+celtic_throwing+caledonian_shield+caledonian_shield_h+celtic_mail_noble+celtic_mail_normal+celtic_helmet_2,
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["caledonian_noble_swords_vet", "Kluddobros (vet)", "Kluddobros (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2_1,
[itm_celtic_boots]+celtic_swords_noble+celtic_throwing+caledonian_shield+caledonian_shield_h+celtic_mail_noble+celtic_mail_normal+celtic_helmet_2,
attrib_level_31_warrior, wp_melee(230), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

#dacian troops
["dacian_light_spearman", "Daki Fyletikoi Pezoi", "Daki Fyletikoi Pezoi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_shield_inf_1+dacian_spear+dacian_cap+dacian_tunic_1+dacian_naked_1,
attrib_level_12_warrior, wp_melee(145), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_light_spearman_exp", "Daki Fyletikoi Pezoi (exp)", "Daki Fyletikoi Pezoi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_shield_inf_2+dacian_spear+dacian_cap+dacian_tunic_2+dacian_naked_2,
attrib_level_18_warrior, wp_melee(165), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_light_spearman_vet", "Daki Fyletikoi Pezoi (vet)", "Daki Fyletikoi Pezoi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_shield_inf_3+dacian_spear+dacian_cap+dacian_tunic_2+dacian_tunic_1,
attrib_level_23_warrior, wp_melee(180), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_light_swordman", "Komatai Sicaphoroi", "Komatai Sicaphoroi",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_throwing+dacian_shield_inf_3+dacian_flax_onehanded+dacian_cap+dacian_tunic_2+dacian_naked_2,
attrib_level_12_warrior, wp_melee(145), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_light_swordman_exp", "Komatai Sicaphoroi (exp)", "Komatai Sicaphoroi (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_throwing+dacian_shield_inf_2+dacian_flax_onehanded+dacian_cap+dacian_tunic_1+dacian_naked_1,
attrib_level_18_warrior, wp_melee(165), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_light_swordman_vet", "Komatai Sicaphoroi (vet)", "Komatai Sicaphoroi (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_throwing+dacian_shield_inf_1+dacian_flax_onehanded+dacian_cap+dacian_tunic_1+dacian_tunic_2,
attrib_level_23_warrior, wp_melee(180), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],


["dacian_flaxman", "Drapanai", "Drapanai",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_naked_2+dacian_tunic_noble_1+dacian_tunic_noble_2+dacian_cap+dacian_flax_twohanded_1,
attrib_level_26_warrior, wp_melee(165), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_flaxman_vet", "Drapanai (vet)", "Drapanai (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_flax_twohanded_1+dacian_helm_normal+dacian_mail_light+dacian_scale_light,
attrib_level_29_warrior, wp_melee(185), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_flaxman_heavy", "Epilektoi Drapanai", "Epilektoi Drapanai",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_flax_twohanded_1+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_31_warrior, wp_melee(190), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_noble_cav", "Daki Aristoi Hippeis", "Daki Aristoi Hippeis",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_lance]+dacian_helm_plume+dacian_mail_heavy+dacian_scale_heavy+dacian_shield_round+dacian_sword+horse_steppe,
attrib_level_26_warrior, wp_melee(160), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_noble_cav_exp", "Daki Aristoi Hippeis (exp)", "Daki Aristoi Hippeis (exp)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_lance]+dacian_helm_plume+dacian_mail_heavy+dacian_scale_heavy+dacian_shield_round+dacian_sword+dacian_sword_noble+horse_steppe,
attrib_level_29_warrior, wp_melee(180), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_noble_cav_vet", "Daki Aristoi Hippeis (vet)", "Daki Aristoi Hippeis (vet)",tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_lance]+dacian_helm_plume+dacian_mail_heavy+dacian_scale_heavy+dacian_shield_round+dacian_sword+dacian_sword_noble+horse_steppe,
attrib_level_31_warrior, wp_melee(200), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_heavy_inf", "Sarmato-Daki Toxotai", "Sarmato-Daki Toxotai",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_2+sarmatian_helm_spangen+dacian_sword+sarmatian_ringswords_short+dacian_shield_round+dacian_helm_normal+dacian_mail_light+dacian_scale_light,
attrib_level_23_warrior, wp_melee(160), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_heavy_inf_exp", "Sarmato-Daki Toxotai (exp)", "Sarmato-Daki Toxotai (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_2+sarmatian_helm_spangen+dacian_sword+sarmatian_ringswords_short+dacian_shield_round+dacian_helm_normal+dacian_mail_light+dacian_scale_light,
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_heavy_inf_vet", "Sarmato-Daki Toxotai (vet)", "Sarmato-Daki Toxotai (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_2+sarmatian_helm_spangen+dacian_sword+sarmatian_ringswords_short+dacian_shield_round+dacian_helm_normal+dacian_mail_light+dacian_scale_light,
attrib_level_29_warrior, wp_melee(200), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_noble_inf", "Ischyroi Orditon", "Ischyroi Orditon",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_sword+dacian_sword_noble+dacian_shield_inf_2+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_26_warrior, wp_melee(170), knows_level_26_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_noble_inf_exp", "Ischyroi Orditon (exp)", "Ischyroi Orditon (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_sword+dacian_sword_noble+dacian_shield_inf_1+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_29_warrior, wp_melee(190), knows_level_29_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_noble_inf_vet", "Ischyroi Orditon (vet)", "Ischyroi Orditon (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_throwing+dacian_sword+dacian_sword_noble+dacian_shield_inf_3+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_31_warrior, wp_melee(210), knows_level_31_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_skirmishers", "Daki Toxotai", "Daki Toxotai",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_1+dacian_tunic_1+dacian_tunic_2+dacian_sword+dacian_cap,
attrib_level_12_warrior, wpe(100,140,140,140), knows_level_12_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_skirmishers_exp", "Daki Toxotai (exp)", "Daki Toxotai (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_1+dacian_tunic_1+dacian_tunic_2+dacian_sword+dacian_cap,
attrib_level_18_warrior, wpe(110,160,160,160), knows_level_18_warrior, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_skirmishers_vet", "Daki Toxotai (vet)", "Daki Toxotai (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_bow_1+dacian_tunic_1+dacian_tunic_2+dacian_sword+dacian_cap,
attrib_level_23_warrior, wpe(120,180,180,180), knows_level_23_warrior, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

["dacian_archers", "Daki Akontistai", "Daki Akontistai",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_javelin,itm_javelin]+dacian_naked_1+dacian_tunic_2+dacian_shield_inf_2+dacian_spear,
attrib_level_12_warrior, wpe(110,140,140,140), knows_archer_basic, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_archers_exp", "Daki Akontistai (exp)", "Daki Akontistai (exp)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_javelin,itm_javelin]+dacian_naked_2+dacian_tunic_1+dacian_shield_inf_3+dacian_spear,
attrib_level_18_warrior, wpe(120,160,160,160), knows_archer_exp, barbarian_man_face_young_1, barbarian_man_face_middle_2 ],
["dacian_archers_vet", "Daki Akontistai (vet)", "Daki Akontistai (vet)",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots,itm_javelin,itm_javelin]+dacian_tunic_1+dacian_tunic_2+dacian_shield_inf_1+dacian_spear,
attrib_level_23_warrior, wpe(130,180,180,180), knows_archer_elit, barbarian_man_face_young_1, barbarian_man_face_old_2 ],

##castle and prison guard
["dacian_prision_guard", "Prison Guard", "Prison Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_sword+dacian_sword_noble+dacian_shield_inf_3+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["dacian_castle_guard", "Castle Guard", "Castle Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_1,
[itm_leather_boots,itm_celtic_boots]+dacian_sword+dacian_sword_noble+dacian_shield_inf_3+dacian_helm_decorate+dacian_mail_heavy+dacian_scale_heavy,
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["celtic_prison_guard", "Prison Guard", "Prison Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_britton_helm4,itm_britton_helm5,itm_britton_helm6,itm_celtic_boots,itm_celtic_shield_large1,itm_celtic_shield_large2,itm_celtic_shield_large3,itm_celtic_shield_large6,itm_celtic_sowrd1,itm_celtic_sowrd2,
itm_celtic_sowrd3,itm_celtic_heavy1,itm_celtic_heavy2,itm_celtic_heavy3,itm_celtic_heavy4],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["celtic_castle_guard", "Castle Guard", "Castle Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_2,
[itm_britton_helm4,itm_britton_helm5,itm_britton_helm6,itm_celtic_boots,itm_celtic_shield_large1,itm_celtic_shield_large2,itm_celtic_shield_large3,itm_celtic_shield_large6,itm_celtic_sowrd1,itm_celtic_sowrd2,
itm_celtic_sowrd3,itm_celtic_heavy1,itm_celtic_heavy2,itm_celtic_heavy3,itm_celtic_heavy4],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["sarmatian_prison_guard", "Prison Guard", "Prison Guards", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_bodkin_arrows,itm_scythian_heavy2,itm_scythian_shield_cav5,itm_scythian_shield_cav6,itm_scythian_shield_cav4,itm_scythian_shield_cav3,itm_light_lance,itm_sarmatian_ringsword_1,itm_sarmatian_heavy_helm6,
itm_sarmatian_heavy_helm7,itm_sarmatian_heavy_helm2,itm_sarmitian_scale_3,itm_sarmitian_scale_1,itm_sarmitian_scale_2,itm_sarmitian_scale_4,itm_celtic_boots],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_castle_guard", "Castle Guard", "Castle Guards", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_bodkin_arrows,itm_scythian_heavy2,itm_scythian_shield_cav5,itm_scythian_shield_cav6,itm_scythian_shield_cav4,itm_scythian_shield_cav3,itm_light_lance,itm_sarmatian_ringsword_2,itm_sarmatian_heavy_helm6,
itm_sarmatian_heavy_helm7,itm_sarmatian_heavy_helm2,itm_sarmitian_scale_1,itm_sarmitian_scale_2,itm_sarmitian_scale_3,itm_sarmitian_scale_4,itm_celtic_boots],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, scythian_face_21, scythian_face_22 ],

["bosporan_prison_guard", "Prison Guard", "Prison Guards", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_9,
[itm_eastern_shoe,itm_eastern_shoe_b,
itm_sarmatian_ringsword_4,itm_military_hammer,itm_sarmatian_ringsword_2,
itm_bosporan_spangenhelm_4,itm_bosporan_spangenhelm_2,itm_bosporan_spangenhelm_1,itm_bosporan_pointed_helm,itm_bosporan_pointed_helm_2,
itm_bosphoran_scale_1,itm_bosphoran_scale_2,
],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, scythian_face_11, scythian_face_12 ],
["bosporan_castle_guard", "Castle Guard", "Castle Guards", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_9,
[itm_eastern_shoe,itm_eastern_shoe_b,
itm_sarmatian_ringsword_4,itm_military_hammer,itm_sarmatian_ringsword_2,
itm_bosporan_spangenhelm_4,itm_bosporan_spangenhelm_2,itm_bosporan_spangenhelm_1,itm_bosporan_pointed_helm,itm_bosporan_pointed_helm_2,
itm_bosphoran_scale_3,itm_bosphoran_scale_4,
],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, scythian_face_21, scythian_face_22 ],

["germanic_prison_guard", "Prison Guard", "Prison Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,
itm_germanic_shield_large1,itm_germanic_shield_large3,itm_germanic_shield_large6,itm_germanic_shield_large11,itm_celtic_boots,itm_sax1,itm_sword_viking_1,itm_germanic_heavy2],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["germanic_castle_guard", "Castle Guard", "Castle Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_medium1,itm_germanic_medium2,itm_germanic_medium3,itm_germanic_medium4,itm_germanic_medium5,itm_germanic_medium6,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,
itm_germanic_shield_large1,itm_germanic_shield_large3,itm_germanic_shield_large6,itm_germanic_shield_large11,itm_celtic_boots,itm_sword_viking_4,itm_sword_viking_3,itm_germanic_heavy2],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["batava_prison_guard", "Prison Guard", "Prison Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_cetratus_aux_1,itm_cetratus_aux_batavorum_cav,itm_cetratus_aux_batavorum_inf,
itm_celtic_boots,itm_roman_gladius_2,itm_roman_aux_helm_5,itm_roman_aux_helm_8],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],
["batava_castle_guard", "Castle Guard", "Castle Guards",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_4,
[itm_germanic_heavy1,itm_germanic_helm1,itm_germanic_helm2,itm_germanic_helm3,itm_cetratus_aux_batavorum_cav,itm_cetratus_aux_batavorum_inf,
itm_celtic_boots,itm_roman_gladius_3,itm_roman_aux_helm_10,itm_roman_aux_helm_11],
attrib_level_31_warrior, wp(180), knows_level_31_warrior, barbarian_man_face_younger_1, barbarian_man_face_middle_2 ],

["eastern_prison_guard", "Prison Guard", "Prison Guards", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[]+eastern_swords_medium+eastern_shields_oval_armenian_2+eastern_shields_oval_parthian_2+eastern_armor_scale_heavy_1+eastern_boots_light+parthian_helm_sallet,
attrib_level_31, wp(180), knows_level_31_warrior, eastern_man_face_middle_1, eastern_man_face_middle_2 ],
["eastern_castle_guard", "Castle Guard", "Castle Guards", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[]+eastern_swords_medium+eastern_shields_oval_armenian_2+eastern_shields_oval_parthian_2+eastern_armor_scale_heavy_1+eastern_boots_light+parthian_helm_infantry_heavy,
attrib_level_31, wp(180), knows_level_31_warrior, eastern_man_face_middle_1, eastern_man_face_middle_2 ],

["caucasian_prison_guard", "Prison Guard", "Prison Guards", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[itm_caucasian_longsword]+eastern_shields_oval_armenian_2+sarmatian_boots+caucasian_mail+caucasian_helm_heavy+caucasian_scale_heavy,
attrib_level_31, wp(180), knows_level_31_warrior, eastern_man_face_middle_1, eastern_man_face_middle_2 ],
["caucasian_castle_guard", "Castle Guard", "Castle Guards", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[itm_caucasian_longsword]+eastern_shields_oval_armenian_2+sarmatian_boots+caucasian_mail+caucasian_helm_heavy+caucasian_scale_heavy,
attrib_level_31, wp(180), knows_level_31_warrior, eastern_man_face_middle_1, eastern_man_face_middle_2 ],

#
["roman_prison_guard", "Prison Guard", "Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_praetorian,itm_scutum_praetorian_2,itm_graves_simple,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_praetorian_hamata_1,itm_praetorian_hamata_2,itm_praetorian_hamata_3,itm_praetorian_hamata_4,itm_praetorian_helm_1,itm_praetorian_helm_2],
attrib_level_31, wp(180), knows_level_31, roman_face1, roman_face2 ],
["roman_castle_guard", "Castle Guard", "Castle Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_praetorian,itm_scutum_praetorian_2,itm_graves_simple,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_praetorian_hamata_1,itm_praetorian_hamata_2,itm_praetorian_hamata_3,itm_praetorian_hamata_4,itm_praetorian_helm_1,itm_praetorian_helm_2],
attrib_level_31, wp(180), knows_level_31, roman_face1, roman_face2 ],
["jew_prison_guard", "Prison Guard", "Prison Guard", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[]+jew_helm_heavy+jew_scale+jew_boots_heavy+jew_swords+jew_shields_large,
attrib_level_31, wp(180), knows_level_31, eastern_man_face_middle_1, eastern_man_face_middle_2 ],
["jew_castle_guard", "Castle Guard", "Castle Guard", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_8,
[]+jew_helm_heavy+jew_scale+jew_boots_heavy+jew_swords+jew_shields_large,
attrib_level_31, wp(180), knows_level_31, eastern_man_face_middle_1, eastern_man_face_middle_2 ],
##end

#sarmatian troops
["sarmatian_light_spearman", "Sauromatai Kontophoroi", "Sauromatai Kontophoroi", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_mounted|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[itm_kopfband,]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_tunic+sarmatian_armor_tunic_scyth_1+sarmatian_boots,
attrib_level_12_warrior, wp_melee(140), knows_level_12_warrior, scythian_face_21, scythian_face_22 ],
["sarmatian_light_spearman_exp", "Sauromatai Kontophoroi (exp)", "Sauromatai Kontophoroi (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_mounted|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[itm_kopfband,]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_tunic+sarmatian_armor_tunic_scyth_2+sarmatian_boots,
attrib_level_16_warrior, wp_melee(155), knows_level_16_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_light_spearman_vet", "Sauromatai Kontophoroi (vet)", "Sauromatai Kontophoroi (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_mounted|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[itm_kopfband,]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_padded+sarmatian_boots,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior, scythian_face_21, scythian_face_22 ],

["sarmatian_archers", "Sauromatai Hippotoxotai", "Sauromatai Hippotoxotai", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_kopfband,
]+horse_steppe+sarmatian_ringswords_short+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_tunic+sarmatian_armor_tunic_scyth_2+sarmatian_boots,
attrib_level_12_warrior, wpe(110,150,150,150), knows_archer_basic_eastern, scythian_face_21, scythian_face_22 ],
["sarmatian_archers_exp", "Sauromatai Hippotoxotai (exp)", "Sauromatai Hippotoxotai (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_kopfband,
]+horse_steppe+sarmatian_ringswords_short+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_padded+sarmatian_armor_tunic_scyth_1+sarmatian_boots,
attrib_level_16_warrior, wpe(120,170,170,170), knows_archer_exp_eastern, scythian_face_21, scythian_face_22 ],
["sarmatian_archers_vet", "Sauromatai Hippotoxotai (vet)", "Sauromatai Hippotoxotai (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_3,
[itm_kopfband,itm_sarmatian_bow,itm_sarmatian_arrows_2]+horse_steppe+sarmatian_ringswords_short+sarmatian_helm_cap_1+sarmatian_helm_cap_2+sarmatian_armor_padded+sarmatian_boots,
attrib_level_18_warrior, wpe(130,195,195,195), knows_archer_elit_eastern, scythian_face_21, scythian_face_22 ],

["sarmatian_light_horsearcher", "Duna Asya", "Duna Asya", tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
]+horse_steppe+kontos+sarmatian_ringswords_short+sarmatian_boots+sarmatian_armor_padded+sarmatian_armor_mail_1+sarmatian_helm_cap_1+sarmatian_helm_spangen,
attrib_level_16_warrior, wpe(125,165,165,165), knows_archer_basic_eastern, scythian_face_11, scythian_face_12 ],
["sarmatian_light_horsearcher_exp", "Duna Asya (exp)", "Duna Asya (exp)", tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,]+horse_steppe+kontos+sarmatian_ringswords_short+sarmatian_boots+sarmatian_armor_mail_2+sarmatian_armor_mail_and_scale_1+sarmatian_helm_spangen+sarmatian_helm_pointed,
attrib_level_18_warrior, wpe(140,180,180,180), knows_archer_exp_eastern, scythian_face_11, scythian_face_12 ],
["sarmatian_light_horsearcher_vet", "Duna Asya (vet)", "Duna Asya (vet)", tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,]+horse_steppe+kontos+sarmatian_ringswords_short+sarmatian_boots+sarmatian_armor_mail_2+sarmatian_armor_mail_and_scale_1+sarmatian_helm_spangen+sarmatian_helm_pointed,
attrib_level_23_warrior, wpe(155,200,200,200), knows_archer_elit_eastern, scythian_face_11, scythian_face_12 ],

["sarmatian_heavy_horsearcher", "Yasaninu Aysna", "Yasaninu Aysna", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
]+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_boots+sarmatian_armor_mail_2+sarmatian_armor_mail_and_scale_1+sarmatian_helm_nobel_1,
attrib_level_23_warrior, wpe(130,150,150,150), knows_archer_basic_eastern, scythian_face_11, scythian_face_12 ],
["sarmatian_heavy_horsearcher_exp", "Yasaninu Aysna (exp)", "Yasaninu Aysna (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
]+horse_parth_half_cataphract+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_boots+sarmatian_armor_mail_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_nobel_2,
attrib_level_26_warrior, wpe(150,165,165,165), knows_archer_exp_eastern, scythian_face_11, scythian_face_12 ],
["sarmatian_heavy_horsearcher_vet", "Yasaninu Aysna (vet)", "Yasaninu Aysna (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_culture_3,
[itm_sarmatian_bow,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,
]+horse_parth_half_cataphract+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_boots+sarmatian_armor_mail_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_nobel_2,
attrib_level_29_warrior, wpe(170,180,180,180), knows_archer_elit_eastern, scythian_face_11, scythian_face_12 ],

["sarmatian_light_horseman", "Aeldary Aemhaltae", "Aeldary Aemhaltae", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_pointed+sarmatian_helm_cap_2+sarmatian_armor_tunic_scyth_1+sarmatian_armor_tunic_scyth_2+sarmatian_boots,
attrib_level_16_warrior, wp_melee(165), knows_level_16_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_light_horseman_exp", "Aeldary Aemhaltae (exp)", "Aeldary Aemhaltae (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_pointed+sarmatian_helm_cap_2+sarmatian_armor_padded+sarmatian_boots,
attrib_level_18_warrior, wp_melee(170), knows_level_18_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_light_horseman_vet", "Aeldary Aemhaltae (vet)", "Aeldary Aemhaltae (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet, no_scene, reserved, fac_culture_3,
[]+horse_steppe+kontos+sarmatian_ringswords_long+sarmatian_helm_spangen+sarmatian_helm_pointed+sarmatian_armor_padded+sarmatian_armor_mail_2+sarmatian_boots,
attrib_level_23_warrior, wp_melee(190), knows_level_23_warrior, scythian_face_11, scythian_face_12 ],

["sarmatian_heavy_horseman", "Rauxsa-alanna Leazdaettae", "Rauxsa-alanna Leazdaettae", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_leather_gloves,]+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_23_warrior, wpe(150,155,155,155), knows_level_23_warrior, scythian_face_21, scythian_face_22 ],
["sarmatian_heavy_horseman_exp", "Rauxsa-alanna Leazdaettae (exp)", "Rauxsa-alanna Leazdaettae (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_leather_gloves]+horse_parth_half_cataphract+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_26_warrior, wpe(165,170,170,170), knows_level_26_warrior, scythian_face_21, scythian_face_22 ],
["sarmatian_heavy_horseman_vet", "Rauxsa-alanna Leazdaettae (vet)", "Rauxsa-alanna Leazdaettae (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_3,
[itm_leather_gloves]+horse_parth_half_cataphract+horse_steppe+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_29_warrior, wpe(180,185,185,185), knows_level_29_warrior, scythian_face_21, scythian_face_22 ],

["sarmatian_noble_horseman", "Sahiya Hadabara", "Sahiya Hadabara", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_gloves, no_scene, reserved, fac_culture_3,
[itm_leather_gloves]+horse_steppe_cataphract+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_nobel_1+sarmatian_helm_nobel_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_26_warrior, wpe(165,170,170,170), knows_level_26_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_noble_horseman_exp", "Sahiya Hadabara (exp)", "Sahiya Hadabara (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_gloves, no_scene, reserved, fac_culture_3,
[itm_leather_gloves]+horse_steppe_cataphract+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_nobel_1+sarmatian_helm_nobel_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_29_warrior, wpe(180,175,175,175), knows_level_29_warrior, scythian_face_11, scythian_face_12 ],
["sarmatian_noble_horseman_vet", "Sahiya Hadabara (vet)", "Sahiya Hadabara (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_polearm|tf_guarantee_horse|tf_guarantee_gloves, no_scene, reserved, fac_culture_3,
[itm_leather_gloves]+horse_steppe_cataphract+kontos_long+sarmatian_ringswords_long+sarmatian_armor_scale+sarmatian_armor_mail_and_scale_1+sarmatian_armor_mail_and_scale_2+sarmatian_helm_nobel_1+sarmatian_helm_nobel_2+sarmatian_helm_pointed+sarmatian_boots,
attrib_level_31_warrior, wpe(195,180,180,180), knows_level_31_warrior, scythian_face_11, scythian_face_12 ],

#Eastern troops
#armenian
["armenian_spear_levy", "Kafkasos Doriphoroi", "Kafkasos Doriphoroi", tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_caucasian_spear_145,itm_sarmatian_spear_169,itm_throwing_spears]+sarmatian_helm_cap_1+parthian_helm_phyrgian+eastern_armor_tunics_armenian+sarmatian_boots+eastern_shields_wicker_armenian,
attrib_level_12, wp_melee(150), knows_level_12, armenian_face_young, armenian_face_middle ],
["armenian_spear_levy_exp", "Kafkasos Doriphoroi (exp)", "Kafkasos Doriphoroi (exp)", tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_caucasian_spear_145,itm_sarmatian_spear_169,itm_throwing_spears]+sarmatian_helm_cap_2+parthian_helm_phyrgian+eastern_armor_tunics_armenian+sarmatian_boots+eastern_shields_wicker_armenian,
attrib_level_18, wp_melee(160), knows_level_18, armenian_face_young, armenian_face_middle ],
["armenian_spear_levy_vet", "Kafkasos Doriphoroi (vet)", "Kafkasos Doriphoroi (vet)", tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_caucasian_spear_145,itm_sarmatian_spear_169,itm_throwing_spears]+sarmatian_helm_cap_2+parthian_helm_phyrgian+eastern_armor_tunics_armenian+sarmatian_boots+eastern_shields_wicker_armenian,
attrib_level_23, wp_melee(170), knows_level_23, armenian_face_young, armenian_face_middle ],

["armenian_light_axeman", "Kafkasos Oresivios", "Kafkasos Oresivios", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears,itm_throwing_spears,itm_armenian_axe_1,itm_celtic_boots]+sarmatian_helm_cap_1+sarmatian_helm_cap_2+eastern_armor_furarmor+scythian_shields_1+eastern_shields_wicker_smallround+eastern_shields_wicker_armenian,
attrib_level_12, wp_melee(150), knows_level_12, armenian_face_young, armenian_face_middle ],
["armenian_light_axeman_exp", "Kafkasos Oresivios (exp)", "Kafkasos Oresivios (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears,itm_throwing_spears,itm_armenian_axe_1,itm_celtic_boots]+sarmatian_helm_cap_1+sarmatian_helm_cap_2+eastern_armor_furarmor+scythian_shields_1+eastern_shields_wicker_smallround+eastern_shields_wicker_armenian,
attrib_level_18, wp_melee(160), knows_level_18, armenian_face_young, armenian_face_middle ],
["armenian_light_axeman_vet", "Kafkasos Oresivios (vet)", "Kafkasos Oresivios (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears,itm_throwing_spears,itm_armenian_axe_1,itm_celtic_boots]+sarmatian_helm_cap_1+sarmatian_helm_cap_2+eastern_armor_furarmor+scythian_shields_1+eastern_shields_wicker_smallround+eastern_shields_wicker_armenian,
attrib_level_23, wp_melee(170), knows_level_23, armenian_face_young, armenian_face_middle ],

["armenian_skrimisher", "Kafkasos Akontistai", "Kafkasos Akontistai", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,itm_celtic_boots,itm_sarmatian_spear_169,itm_eastern_spear_168]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+eastern_armor_furarmor+sarmatian_helm_cap_2+sarmatian_helm_cap_1,
attrib_level_12, wpe(110,150,150,150), knows_level_12, parthian_face_young, armenian_face_middle ],
["armenian_skrimisher_exp", "Kafkasos Akontistai (exp)", "Kafkasos Akontistai (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,itm_celtic_boots,itm_sarmatian_spear_169,itm_eastern_spear_168]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+eastern_armor_furarmor+sarmatian_helm_cap_2+sarmatian_helm_cap_1,
attrib_level_18, wpe(120,160,160,160), knows_level_18, parthian_face_young, armenian_face_middle ],
["armenian_skrimisher_vet", "Kafkasos Akontistai (vet)", "Kafkasos Akontistai (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_armenian_war_spear,itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,itm_celtic_boots,itm_sarmatian_spear_169,itm_eastern_spear_168]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+eastern_armor_furarmor+sarmatian_helm_cap_2+sarmatian_helm_cap_1,
attrib_level_23, wpe(130,180,180,180), knows_level_23, parthian_face_young, armenian_face_middle ],

["armenian_slinger", "Kafkasos Sphendonetes", "Kafkasos Sphendonetai", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_sling_rock1,itm_sling,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+sarmatian_boots+parthian_helm_phyrgian,
attrib_level_12, wpe(90,160,160,160), knows_archer_basic, armenian_face_young, armenian_face_middle ],
["armenian_slinger_exp", "Kafkasos Sphendonetes (exp)", "Kafkasos Sphendonetai (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_sling_lead,itm_sling_rock1,itm_sling,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+sarmatian_boots+parthian_helm_phyrgian,
attrib_level_16, wpe(100,170,170,170), knows_archer_exp, armenian_face_young, armenian_face_middle ],
["armenian_slinger_vet", "Kafkasos Sphendonetes (vet)", "Kafkasos Sphendonetai (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_sling_lead,itm_sling,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_armenian+sarmatian_boots+parthian_helm_phyrgian,
attrib_level_20, wpe(110,180,180,180), knows_archer_elit, armenian_face_young, armenian_face_middle ],

["armenian_heavy_inf", "Armenikoi Legeonarioi", "Armenikoi Legeonarioi", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_short_sword,itm_jarid,itm_armenian_sword_1]+armenian_helm_legio+eastern_armor_mail_armenian+eastern_boots_light+eastern_shields_oval_armenian_1,
attrib_level_18, wp_melee(160), knows_level_18, armenian_face_young, armenian_face_middle ],
["armenian_heavy_inf_exp", "Armenikoi Legeonarioi (exp)", "Armenikoi Legeonarioi (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_short_sword,itm_jarid,itm_armenian_sword_1]+armenian_helm_legio+eastern_armor_mail_armenian+eastern_boots_light+eastern_shields_oval_armenian_2,
attrib_level_23, wp_melee(170), knows_level_23, armenian_face_young, armenian_face_middle ],
["armenian_heavy_inf_vet", "Armenikoi Legeonarioi (vet)", "Armenikoi Legeonarioi (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_short_sword,itm_jarid,itm_armenian_sword_1]+armenian_helm_legio+eastern_armor_mail_armenian+eastern_boots_light+eastern_shields_oval_armenian_1+eastern_shields_oval_armenian_2,
attrib_level_26, wp_melee(180), knows_level_26, armenian_face_young, armenian_face_middle ],

["armenian_heavy_maceman", "Armazis Dacva", "Armazis Dacva", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_throwing_spears_roman,itm_mace_3,itm_mace_2]+eastern_boots_light+eastern_armor_scale_armenian+armenian_helm_heavy+eastern_shields_oval_armenian_2,
attrib_level_18, wp_melee(160), knows_level_18, armenian_face_young, armenian_face_middle ],
["armenian_heavy_maceman_exp", "Armazis Dacva (exp)", "Armazis Dacva (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_throwing_spears_roman,itm_mace_3,itm_mace_2]+eastern_boots_light+eastern_armor_scale_armenian+armenian_helm_heavy+eastern_shields_oval_armenian_1,
attrib_level_23, wp_melee(170), knows_level_23, armenian_face_young, armenian_face_middle ],
["armenian_heavy_maceman_vet", "Armazis Dacva (vet)", "Armazis Dacva (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_throwing_spears_roman,itm_mace_3,itm_mace_2]+eastern_boots_light+eastern_armor_scale_armenian+armenian_helm_heavy+eastern_shields_oval_armenian_1+eastern_shields_oval_armenian_2,
attrib_level_26, wp_melee(180), knows_level_26, armenian_face_young, armenian_face_middle ],

["caucasian_heavy_spearman", "Kentronakan Doriphoroi", "Kentronakan Doriphoroi", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_spear_145,itm_caucasian_spear_174]+eastern_boots_light+caucasian_mail+caucasian_scale+caucasian_helm_heavy+eastern_shields_oval_armenian_1,
attrib_level_18, wp_melee(160), knows_level_18, armenian_face_young, armenian_face_middle ],
["caucasian_heavy_spearman_exp", "Kentronakan Doriphoroi (exp)", "Kentronakan Doriphoroi (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_spear_145,itm_caucasian_spear_174]+eastern_boots_light+caucasian_mail+caucasian_scale+caucasian_helm_heavy+eastern_shields_oval_armenian_2,
attrib_level_23, wp_melee(170), knows_level_23, armenian_face_young, armenian_face_middle ],
["caucasian_heavy_spearman_vet", "Kentronakan Doriphoroi (vet)", "Kentronakan Doriphoroi (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_5,
[itm_throwing_spears_east,itm_caucasian_spear_145,itm_caucasian_spear_174]+eastern_boots_light+caucasian_mail+caucasian_scale+caucasian_helm_heavy+eastern_shields_oval_armenian_1+eastern_shields_oval_armenian_2,
attrib_level_26, wp_melee(180), knows_level_26, armenian_face_young, armenian_face_middle ],

["armenian_horsearcher", "Kafkasos Hippotoxotes", "Kafkasos Hippotoxotai", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_arrows,itm_arrows]+horse_steppe+eastern_armor_tunics_armenian+parthian_helm_phyrgian+eastern_boots_light+eastern_swords_long,
attrib_level_23, wpe(120,150,150,150), knows_archer_basic_eastern, armenian_face_young, armenian_face_middle ],
["armenian_horsearcher_exp", "Kafkasos Hippotoxotes (exp)", "Kafkasos Hippotoxotai (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_khergit_arrows,itm_arrows]+horse_steppe+eastern_armor_tunics_armenian+parthian_helm_phyrgian+eastern_boots_light+eastern_swords_long+parthian_helm_cavalry,
attrib_level_26, wpe(130,165,165,165), knows_archer_exp_eastern, armenian_face_young, armenian_face_middle ],
["armenian_horsearcher_vet", "Kafkasos Hippotoxotes (vet)", "Kafkasos Hippotoxotai (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_khergit_arrows,itm_khergit_arrows]+horse_steppe+eastern_armor_tunics_armenian+eastern_boots_light+eastern_swords_long+parthian_helm_cavalry,
attrib_level_29,wpe(140,180,180,180), knows_archer_elit_eastern, armenian_face_young, armenian_face_middle ],

["caucasian_medium_horsearcher", "Asistavis", "Asistavis", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_arrows,itm_arrows,itm_caucasian_spear_174,itm_caucasian_longsword]+horse_steppe+eastern_armor_furarmor+caucasian_scale+sarmatian_boots+sarmatian_ringswords_long+caucasian_helm_light,
attrib_level_23_warrior, wpe(140,150,150,150), knows_archer_basic_eastern, armenian_face_young, armenian_face_middle ],
["caucasian_medium_horsearcher_exp", "Asistavis (exp)", "Asistavis (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_khergit_arrows,itm_arrows,itm_caucasian_spear_174,itm_caucasian_longsword]+horse_steppe+eastern_armor_furarmor+caucasian_scale+sarmatian_boots+sarmatian_ringswords_long+caucasian_helm_light,
attrib_level_26_warrior, wpe(155,165,165,165), knows_archer_exp_eastern, armenian_face_young, armenian_face_middle ],
["caucasian_medium_horsearcher_vet", "Asistavis (vet)", "Asistavis (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_5,
[itm_strong_bow,itm_khergit_arrows,itm_khergit_arrows,itm_caucasian_spear_174,itm_caucasian_longsword]+horse_steppe+eastern_armor_furarmor+caucasian_scale+sarmatian_boots+sarmatian_ringswords_long+caucasian_helm_light,
attrib_level_29_warrior,wpe(170,180,180,180), knows_archer_elit_eastern, armenian_face_young, armenian_face_middle ],

["armenian_medium_horseman", "Mkhedroba ", "Mkhedroba ", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_eastern_spear_168,itm_kartil_axe_1]+horse_parth+armenian_helm_heavy+eastern_armor_scale_armenian+eastern_armor_mail_armenian+scythian_shields_1+sarmatian_boots+sarmatian_helm_cap_1,
attrib_level_23, wp_melee(160), knows_level_23, armenian_face_young, armenian_face_middle ],
["armenian_medium_horseman_exp", "Mkhedroba  (exp)", "Mkhedroba  (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_eastern_spear_168,itm_kartil_axe_1]+horse_parth+armenian_helm_heavy+eastern_armor_mail_armenian+eastern_armor_scale_armenian+scythian_shields_1+sarmatian_boots,
attrib_level_26, wp_melee(170), knows_level_26, armenian_face_young, armenian_face_middle ],
["armenian_medium_horseman_vet", "Mkhedroba  (vet)", "Mkhedroba  (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_5,
[itm_eastern_spear_168,itm_kartil_axe_1]+horse_parth+armenian_helm_heavy+eastern_armor_mail_armenian+eastern_armor_scale_armenian+scythian_shields_1+sarmatian_boots,
attrib_level_29, wp_melee(180), knows_level_29, armenian_face_young, armenian_face_middle ],

["caucasian_cataphract", "Kafkasos Basilikoi Hippeis", "Kafkasos Basilikoi Hippeis", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_caucasian_longsword,itm_armenian_axe_1,itm_caucasian_spear_174]+horse_steppe_cataphract+caucasian_helm_heavy+caucasian_scale_heavy+caucasian_mail+sarmatian_boots+scythian_shields_2,
attrib_level_26, wp_melee(165), knows_level_26, armenian_face_young, armenian_face_middle ],
["caucasian_cataphract_exp", "Kafkasos Basilikoi Hippeis (exp)", "Kafkasos Basilikoi Hippeis (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_caucasian_longsword,itm_armenian_axe_1,itm_caucasian_spear_174]+horse_steppe_cataphract+caucasian_helm_heavy+caucasian_scale_heavy+caucasian_mail+sarmatian_boots+scythian_shields_2,
attrib_level_29, wp_melee(175), knows_level_29, armenian_face_young, armenian_face_middle ],
["caucasian_cataphract_vet", "Kafkasos Basilikoi Hippeis (vet)", "Kafkasos Basilikoi Hippeis (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_caucasian_longsword,itm_armenian_axe_1,itm_caucasian_spear_174]+horse_steppe_cataphract+caucasian_helm_heavy+caucasian_scale_heavy+caucasian_mail+sarmatian_boots+scythian_shields_2,
attrib_level_31, wp_melee(185), knows_level_31, armenian_face_young, armenian_face_middle ],

["armenian_cataphract", "Armenikoi Kataphraktoi", "Armenikoi Kataphraktoi", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+eastern_swords_long+horse_parth_cataphract+parthian_helm_cataphract+eastern_armor_cataphract+eastern_boots_cataphract+armenian_helm_heavy,
attrib_level_26, wp_melee(165), knows_level_26, armenian_face_young, armenian_face_middle ],
["armenian_cataphract_exp", "Armenikoi Kataphraktoi (exp)", "Armenikoi Kataphraktoi (exp)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+eastern_swords_long+horse_parth_cataphract+parthian_helm_cataphract+eastern_armor_cataphract+eastern_boots_cataphract+armenian_helm_heavy,
attrib_level_29, wp_melee(175), knows_level_29, armenian_face_young, armenian_face_middle ],
["armenian_cataphract_vet", "Armenikoi Kataphraktoi (vet)", "Armenikoi Kataphraktoi (vet)", tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+eastern_swords_long+horse_parth_cataphract+parthian_helm_cataphract+eastern_armor_cataphract+eastern_boots_cataphract+armenian_helm_heavy,
attrib_level_31, wp_melee(185), knows_level_31, armenian_face_young, armenian_face_middle ],

["armenian_elite_infantry", "Armenikoi Epilektoi Toxotai", "Armenikoi Epilektoi Toxotai", tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_khergit_arrows,itm_khergit_arrows,itm_strong_bow,itm_armenian_axe_1,itm_armenian_sword_1,itm_caucasian_short_sword]+eastern_armor_scale_armenian+eastern_armor_mail_armenian+eastern_boots_light+armenian_helm_heavy,
attrib_level_26, wp_melee(165), knows_level_26, armenian_face_young, armenian_face_middle ],
["armenian_elite_infantry_exp", "Armenikoi Epilektoi Toxotai (exp)", "Armenikoi Epilektoi Toxotai (exp)", tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_barbed_arrows,itm_barbed_arrows,itm_strong_bow,itm_armenian_axe_1,itm_armenian_sword_1,itm_caucasian_short_sword]+eastern_armor_scale_armenian+eastern_armor_mail_armenian+eastern_armor_scale_heavy_1+eastern_boots_light+armenian_helm_heavy,
attrib_level_29, wp_melee(175), knows_level_29, armenian_face_young, armenian_face_middle ],
["armenian_elite_infantry_vet", "Armenikoi Epilektoi Toxotai (vet)", "Armenikoi Epilektoi Toxotai (vet)", tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_5,
[itm_barbed_arrows,itm_barbed_arrows,itm_strong_bow,itm_armenian_axe_1,itm_armenian_sword_1,itm_caucasian_short_sword]+eastern_armor_scale_armenian+eastern_armor_mail_armenian+eastern_armor_scale_heavy_1+eastern_boots_light+armenian_helm_heavy,
attrib_level_31, wp_melee(185), knows_level_31, armenian_face_young, armenian_face_middle ],

#parthian
["eastern_light_archer", "Thanvare Parsig", "Thanvare Parsig",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_eastern_spear_168,itm_eastern_spear_149,itm_persian_bow,itm_arrows]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker_oval,
attrib_level_12, wpe(120,160,160,160), knows_archer_basic_eastern, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_light_archer_exp", "Thanvare Parsig (exp)", "Thanvare Parsig (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_eastern_spear_149,itm_persian_bow,itm_khergit_arrows,itm_eastern_spear_168]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker_oval,
attrib_level_18, wpe(130,170,170,170), knows_archer_exp_eastern, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_light_archer_vet", "Thanvare Parsig (vet)", "Thanvare Parsig (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_eastern_spear_149,itm_persian_bow,itm_barbed_arrows,itm_eastern_spear_168]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker_oval,
attrib_level_23, wpe(140,180,180,180), knows_archer_elit_eastern, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_light_axeman", "Gund-i Madaen", "Gund-i Madaen",tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_jarid,itm_jarid,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_eastern_spear_149,itm_eastern_spear_168]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker,
attrib_level_12, wp_melee(150), knows_level_12, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_light_axeman_exp", "Gund-i Madaen (exp)", "Gund-i Madaen (exp)",tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_jarid,itm_jarid,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_eastern_spear_149,itm_eastern_spear_168]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker_painted,
attrib_level_18, wp_melee(160), knows_level_18, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_light_axeman_vet", "Gund-i Madaen (vet)", "Gund-i Madaen (vet)",tf_male_eastern|tf_guarantee_polearm|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_jarid,itm_jarid,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_eastern_spear_149,itm_eastern_spear_168]+persian_helm_light+eastern_armor_tunics_persian+eastern_boots_light+eastern_shields_wicker_painted,
attrib_level_23, wp_melee(170), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_skrimisher", "Verkhana Kofyaren", "Verkhana Kofyaren",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,
itm_military_hammer,itm_pickaxe,itm_one_handed_war_axe_a,itm_celtic_boots]+eastern_armor_furarmor+eastern_armor_tunics_parthian+eastern_shields_wicker_smallround+scythian_shields_2+parthian_helm_phyrgian+persian_helm_light,
attrib_level_12, wpe(110,150,150,150), knows_level_12, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_skrimisher_exp", "Verkhana Kofyaren (exp)", "Verkhana Kofyaren (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,
itm_military_hammer,itm_pickaxe,itm_one_handed_war_axe_a,itm_celtic_boots]+eastern_armor_furarmor+eastern_armor_tunics_parthian+eastern_shields_wicker_smallround+scythian_shields_2+parthian_helm_phyrgian+persian_helm_light,
attrib_level_18, wpe(120,160,160,160), knows_level_18, eastern_man_face_younger_1, parthian_face_middle ],
["eastern_skrimisher_vet", "Verkhana Kofyaren (vet)", "Verkhana Kofyaren (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_throwing_spears_east,itm_javelin,
itm_military_hammer,itm_pickaxe,itm_one_handed_war_axe_a,itm_celtic_boots]+eastern_armor_furarmor+eastern_armor_tunics_parthian+eastern_shields_wicker_oval+scythian_shields_2+parthian_helm_phyrgian+persian_helm_light,
attrib_level_23, wpe(130,180,180,180), knows_level_23, eastern_man_face_younger_1, parthian_face_middle ],

["eastern_slinger", "Palkhandar", "Palkhandar",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_sling_rock1,itm_sling,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_persian+eastern_boots_light+persian_helm_light,
attrib_level_12, wpe(90,160,160,160), knows_archer_basic, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_slinger_exp", "Palkhandar (exp)", "Palkhandar (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_sling_lead,itm_sling_rock1,itm_sling,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_persian+eastern_boots_light+persian_helm_light,
attrib_level_16, wpe(100,170,170,170), knows_archer_exp, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_slinger_vet", "Palkhandar (vet)", "Palkhandar (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_sling_lead,itm_sling,itm_dagger_parthian_1,itm_dagger_parthian_2,itm_mace_1]+eastern_shields_wicker_smallround+eastern_armor_tunics_persian+eastern_boots_light+persian_helm_light,
attrib_level_20, wpe(110,180,180,180), knows_archer_elit, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_heavy_inf", "Arteshtari Pahlavig", "Arteshtari Pahlavig",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_military_hammer]+eastern_sword_short+eastern_armor_scale_parthian+parthian_helm_infantry+eastern_boots_light+eastern_shields_oval_parthian_1,
attrib_level_18, wp_melee(160), knows_level_18, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_heavy_inf_exp", "Arteshtari Pahlavig (exp)", "Arteshtari Pahlavig (exp)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_military_hammer]+eastern_sword_short+eastern_armor_scale_parthian+parthian_helm_infantry+eastern_boots_light+eastern_shields_oval_parthian_2+parthian_helm_infantry_heavy,
attrib_level_23, wp_melee(170), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_heavy_inf_vet", "Arteshtari Pahlavig (vet)", "Arteshtari Pahlavig (vet)",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_jarid,itm_military_hammer]+eastern_swords_medium+eastern_armor_scale_parthian+eastern_boots_light+eastern_shields_oval_parthian_2+parthian_helm_infantry_heavy+eastern_shields_oval_parthian_1,
attrib_level_26, wp_melee(180), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_heavy_spearman", "Shipri Tukul", "Shipri Tukul", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_eastern_spear_168,itm_eastern_spear_149]+eastern_boots_light+eastern_sword_short+eastern_armor_mail_parthian+parthian_helm_infantry+eastern_shields_oval_parthian_2,
attrib_level_18, wp_melee(160), knows_level_18, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_heavy_spearman_exp", "Shipri Tukul (exp)", "Shipri Tukul (exp)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_eastern_spear_168,itm_eastern_spear_149]+eastern_boots_light+eastern_sword_short+eastern_armor_mail_parthian+parthian_helm_infantry+eastern_shields_oval_parthian_1+parthian_helm_infantry_heavy,
attrib_level_23, wp_melee(170), knows_level_23, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_heavy_spearman_vet", "Shipri Tukul (vet)", "Shipri Tukul (vet)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_throwing_spears_east,itm_jarid,itm_eastern_spear_168,itm_eastern_spear_149]+eastern_boots_light+eastern_sword_short+eastern_armor_mail_parthian+parthian_helm_infantry_heavy+eastern_shields_oval_parthian_1+eastern_shields_oval_parthian_2,
attrib_level_26, wp_melee(180), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_horsearcher", "Shivatirei Pahlavanig", "Shivatirei Pahlavanig",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_6,
[itm_persian_bow,itm_khergit_arrows,itm_khergit_arrows]+horse_parth+eastern_armor_tunics_parthian+parthian_helm_phyrgian+eastern_boots_light+eastern_swords_long,
attrib_level_23, wpe(120,170,170,170), knows_archer_basic_eastern, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_horsearcher_exp", "Shivatirei Pahlavanig (exp)", "Shivatirei Pahlavanig (exp)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_6,
[itm_persian_bow,itm_barbed_arrows,itm_barbed_arrows]+horse_parth+eastern_armor_tunics_parthian+parthian_helm_phyrgian+eastern_boots_light+eastern_swords_long+parthian_helm_cavalry,
attrib_level_26, wpe(130,180,180,180), knows_archer_exp_eastern, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_horsearcher_vet", "Shivatirei Pahlavanig (vet)", "Shivatirei Pahlavanig (vet)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_culture_6,
[itm_persian_bow,itm_barbed_arrows,itm_barbed_arrows]+horse_parth+eastern_armor_tunics_parthian+eastern_boots_light+eastern_swords_long+parthian_helm_cavalry,
attrib_level_29,wpe(140,190,190,190), knows_archer_elit_eastern, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_medium_horseman", "Asavarani Azadan", "Asavarani Azadan",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_javelin,itm_eastern_spear_168]+horse_parth+parthian_helm_cavalry+parthian_helm_phyrgian+eastern_armor_tunics_parthian+eastern_armor_mail_parthian+eastern_swords_long+scythian_shields_1+eastern_boots_light,
attrib_level_23, wp_melee(160), knows_level_23, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_medium_horseman_exp", "Asavarani Azadan (exp)", "Asavarani Azadan (exp)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_javelin,itm_eastern_spear_168]+horse_parth+parthian_helm_cavalry+parthian_helm_cavalry_heavy+eastern_armor_mail_parthian+eastern_armor_scale_parthian+eastern_swords_long+scythian_shields_1+eastern_boots_light,
attrib_level_26, wp_melee(170), knows_level_26, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_medium_horseman_vet", "Asavarani Azadan (vet)", "Asavarani Azadan (vet)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_culture_6,
[itm_javelin,itm_eastern_spear_168]+horse_parth+parthian_helm_cavalry_heavy+eastern_armor_mail_parthian+eastern_armor_scale_parthian+eastern_swords_long+scythian_shields_1+eastern_boots_light,
attrib_level_29, wp_melee(180), knows_level_29, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_cataphract", "Pahlavanei Grivpanvar", "Pahlavanei Grivpanvar",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_6,
[itm_parthian_cataphract_axe,itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+horse_parth_cataphract+parthian_helm_sallet+parthian_helm_cataphract+eastern_armor_cataphract+eastern_armor_cataphract_lamellar+eastern_boots_cataphract,
attrib_level_26, wp_melee(165), knows_level_26, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_cataphract_exp", "Pahlavanei Grivpanvar (exp)", "Pahlavanei Grivpanvar (exp)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_6,
[itm_parthian_cataphract_axe,itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+horse_parth_cataphract+parthian_helm_sallet+parthian_helm_cataphract+eastern_armor_cataphract+eastern_armor_cataphract_lamellar+eastern_boots_cataphract,
attrib_level_29, wp_melee(175), knows_level_29, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_cataphract_vet", "Pahlavanei Grivpanvar (vet)", "Pahlavanei Grivpanvar (vet)",tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_culture_6,
[itm_parthian_cataphract_axe,itm_sarranid_mace_1,itm_mail_mittens,itm_lance,itm_heavy_lance]+horse_parth_cataphract+parthian_helm_sallet+parthian_helm_cataphract+eastern_armor_cataphract+eastern_armor_cataphract_lamellar+eastern_boots_cataphract,
attrib_level_31, wp_melee(185), knows_level_31, eastern_man_face_younger_1, eastern_man_face_old_2 ],

["eastern_elite_infantry", "Kamandaran Zhayadan", "Kamandaran Zhayadan",tf_male_eastern|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[itm_khergit_arrows,itm_khergit_bow,itm_parthian_pointed_helm,itm_heavy_wicker_1,itm_heavy_wicker_2]+eastern_swords_medium+eastern_armor_scale_heavy_1+parthian_helm_sallet+eastern_boots_light,
attrib_level_26, wp(165), knows_level_26|knows_power_draw_4, eastern_man_face_younger_1, eastern_man_face_middle_2 ],
["eastern_elite_infantry_exp", "Kamandaran Zhayadan (exp)", "Kamandaran Zhayadan (exp)",tf_male_eastern|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[itm_barbed_arrows,itm_khergit_bow,itm_parthian_pointed_helm,itm_heavy_wicker_1,itm_heavy_wicker_2]+eastern_swords_medium+eastern_armor_scale_heavy_1+parthian_helm_sallet+eastern_boots_light,
attrib_level_29, wp(175), knows_level_29|knows_power_draw_5, eastern_man_face_younger_1, eastern_man_face_old_2 ],
["eastern_elite_infantry_vet", "Kamandaran Zhayadan (vet)", "Kamandaran Zhayadan (vet)",tf_male_eastern|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_culture_6,
[itm_barbed_arrows,itm_khergit_bow,itm_parthian_pointed_helm,itm_heavy_wicker_1,itm_heavy_wicker_2]+eastern_swords_medium+eastern_armor_scale_heavy_1+parthian_helm_sallet+eastern_boots_light,
attrib_level_31, wp(185), knows_level_31|knows_power_draw_6, eastern_man_face_younger_1, eastern_man_face_old_2 ],

##die reihen folge bei den legionaren und aquilifer und vexillarius typen is wichitig
#roman legions es gibt 12 legionen im spiel
#1
["legio_i_adjutrix", "Tiro Legionis (I Adiutrix)", "Tirones Legionis (I Adiutrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_i,itm_graves_simple,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_hamata_11,itm_legion_segmentata_3,itm_1_imp_gallic_c,itm_1_imp_gallic_f_b],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#2
["legio_iii_augusta", "Tiro Legionis (III Augusta)", "Tirones Legionis (III Augusta)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_iii,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_segmentata_1,itm_legion_hamata_10,itm_1_imp_gallic_f_b_feather,itm_1_imp_gallic_f_n],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#3
["legio_v_alaudae", "Tiro Legionis (V Alaudae)", "Tirones Legionis (V Alaudae)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_v,
itm_legion_hamata_1,itm_legion_segmentata_2,itm_1_imp_gallic_f_s,itm_1_imp_gallic_g],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#4
["legio_xxi_rapax", "Tiro Legionis (XXI Rapax)", "Tirones Legionis (XXI Rapax)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xxi,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_legion_hamata_3,itm_legion_segmentata_5,itm_1_imp_gallic_h,itm_1_imp_gallic_i_ac],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#5
["legio_vii_galbia", "Tiro Legionis (VII Galbia)", "Tirones Legionis (VII Galbia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_vii_galb,
itm_legion_segmentata_cape_1,itm_legion_squamata_14,itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_i_ac_feather_plume],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#6
["legio_vi_victrix", "Tiro Legionis (VI Victrix)", "Tirones Legionis (VI Victrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_vi_vict,itm_scutum_9,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_squamata_11,itm_legion_hamata_14,itm_1_imp_gallic_i,itm_1_imp_gallic_i_feather],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#7
["legio_xi_claudia", "Tiro Legionis (XI Claudia)", "Tirones Legionis (XI Claudia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_xi,itm_graves_simple,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_1_imp_gallic_i_ac_plume,itm_1_imp_gallic_i_feather,
itm_legion_hamata_15,itm_legion_segmentata_cape_2],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#8
["legio_xiii_gemina", "Tiro Legionis (XIII Gemina)", "Tirones Legionis (XIII Gemina)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xiii,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_legion_squamata_10,itm_legion_hamata_13,itm_1_imp_gallic_i_plume,itm_1_imp_itallic_c],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#9
["legio_v_macedonia", "Tiro Legionis (V Macedonia)", "Tirones Legionis (V Macedonia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_v_mac,
itm_legion_segmentata_cape_3,itm_legion_hamata_16,itm_1_imp_itallic_d,itm_1_imp_gallic_f_s],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#10
["legio_vi_ferrata", "Tiro Legionis (VI Ferrata)", "Tirones Legionis (VI Ferrata)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_vi_ferr,itm_graves_simple,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_hamata_cape_6,itm_legion_segmentata_4,itm_1_imp_itallic_g,itm_1_imp_gallic_f_n],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#11
["legio_x_fretensis", "Tiro Legionis (X Fretensis)", "Tirones Legionis (X Fretensis)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_x,
itm_legion_hamata_cape_7,itm_legion_hamata_2,itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_c],
attrib_level_23, wp(150), knows_level_23, roman_face1, roman_face2 ],
#12
["praetoriani_milites", "Tiro Praetoriani", "Tirones Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_praetorian,itm_scutum_praetorian_2,itm_graves_simple,itm_roman_gladius_3,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_praetorian_segmentata_1,itm_praetorian_segmentata_2,itm_praetorian_segmentata_3,itm_praetorian_helm_1,itm_praetorian_helm_2],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],

["aquilifer_i", "Aquilifer (I Adiutrix)", "Aquilifer (I Adiutrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_capricorn],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_iii", "Aquilifer (III Augusta)", "Aquilifer (III Augusta)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_pegasus],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_v_alaudae", "Aquilifer (V Alaudae)", "Aquilifer (V Alaudae)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_elephant],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_xxi", "Aquilifer (XXI Rapax)", "Aquilifer (XXI Rapax)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_capricorn],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_vii", "Aquilifer (VII Galbia)", "Aquilifer (VII Galbia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_scorpion],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_vi_vict", "Aquilifer (VI Victrix)", "Aquilifer (VI Victrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_2,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_ox],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_xi", "Aquilifer (XI Claudia)", "Aquilifer (XI Claudia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_trident],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_xiii", "Aquilifer (XIII Gemina)", "Aquilifer (XIII Gemina)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_lion],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_v_mac", "Aquilifer (V Macedonia)", "Aquilifer (V Macedonia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_aquila],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_vi_fer", "Aquilifer (VI Ferrata)", "Aquilifer (VI Ferrata)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_capwolf],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_x", "Aquilifer (X Fretensis)", "Aquilifer (X Fretensis)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_bireme],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["aquilifer_praetoriani", "Aquilifer Praetoriani", "Aquilifer Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_gladius_2,itm_aquilifer_praetorian_squamata_1,itm_aquilifer_helmet,itm_aquilifer_helmet_mask,
itm_signum_praetoriani],#
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],

["vexilarius_i", "Vexillarius (I Adiutrix)", "Vexillarii (I Adiutrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_i],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_iii", "Vexillarius (III Augusta)", "Vexillarii (III Augusta)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_iii],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_v_alaudae", "Vexillarius (V Alaudae)", "Vexillarii (V Alaudae)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_v_alaudae],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_xxi", "Vexillarius (XXI Rapax)", "Vexillarii (XXI Rapax)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_xxi],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_vii", "Vexillarius (VII Galbia)", "Vexillarii (VII Galbia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_vii],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_vi_vict", "Vexillarius (VI Victrix)", "Vexillarii (VI Victrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_vi_vict],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_xi", "Vexillarius (XI Claudia)", "Vexillarii (XI Claudia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_xi],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_xiii", "Vexillarius (XIII Gemina)", "Vexillarii (XIII Gemina)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_xiii],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_v_mac", "Vexillarius (V Macedonia)", "Vexillarii (V Macedonia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_v],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_vi_fer", "Vexillarius (VI Ferrata)", "Vexillarii (VI Ferrata)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_vi],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_x", "Vexillarius (X Fretensis)", "Vexillarii (X Fretensis)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_graves_simple,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_legio_x],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],
["vexilarius_praetoriani", "Vexillarius Praetoriani", "Vexillarii Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_rich_3,itm_graves_simple,itm_vexilarius_praetorian_squamata_1,itm_vexilarius_helmet,itm_vexilarius_helmet_mask,
itm_vexilum_praetoriani,itm_vexilum_praetoriani_2],
attrib_level_31, wp(160), knows_level_31, roman_face1, roman_face2 ],

#officers
["centurio_west", "Centurio", "Centurii", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_centurio_west_graves,itm_roman_gladius_3,itm_scutum_2,itm_scutum_3,itm_scutum_4,itm_scutum_5,
itm_cenutrio_legion_hamata_3,itm_cenutrio_legion_hamata_4,itm_cenutrio_legion_squamata_3,itm_cenutrio_legion_squamata_4,
itm_centurio_helm_1,itm_centurio_helm_2,itm_centurio_helm_3],
attrib_level_31, wp(170), knows_level_31, roman_face1, roman_face2 ],
["centurio_preatoriani", "Centurio Praetoriani", "Centurii Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_centurio_praetorian_graves,itm_roman_gladius_rich_3,itm_scutum_3, itm_centurio_praetorian_squamata_1,itm_centurio_praetorian_squamata_2,
itm_praetorian_cent_helmet,itm_praetorian_cent_helmet2,itm_praetorian_cent_helmet3,itm_praetorian_cent_helmet4],
attrib_level_31, wp(170), knows_level_31, roman_face1, roman_face2 ],
["signifer", "Signifer", "Signifer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_signum_signifer,itm_graves_simple,itm_signifer_helm_1,itm_signifer_helm_2,itm_signifer_legion_squamata,itm_signifer_legion_hamata],
attrib_level_29, wp(160), knows_level_29, roman_face1, roman_face2 ],
["cornicen", "Cornicen", "Cornicines", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2,itm_f_cornu,itm_graves_simple,itm_signifer_helm_1,itm_signifer_helm_2,itm_signifer_legion_squamata,itm_signifer_legion_hamata],
attrib_level_29, wp(160), knows_level_29, roman_face1, roman_face2 ],

["legatus_legionis", "Tribunus", "Tribuni", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_rich_2,itm_officer_shield,itm_officer_shield_2,itm_officer_shield_3,
itm_musculata_legatus_6,itm_musculata_legatus_7,itm_musculata_legatus_8,itm_musculata_legatus_9,
itm_legatus_legionis_helm,itm_legatus_legionis_helm_2,itm_legatus_legionis_helm_3,itm_legio_armored_caligea]+items_roman_horses,
attrib_level_31, wp(175), knows_level_31, roman_face1, roman_face2 ],
["centurio_east", "Primus Pilus", "Primi Pili", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_11,itm_scutum_8,itm_scutum_7,itm_roman_gladius_3,itm_centurio_east_graves,
itm_cenutrio_legion_squamata_2,itm_centurio_legion_hamata_2,itm_centurio_legion_hamata_1,itm_praetorian_cent_helmet,itm_praetorian_cent_helmet2],
attrib_level_31, wp(180), knows_level_31, roman_face1, roman_face2 ],

["aux_vigiles_centurio", "Centurio Vigiliarum", "Centurii Vigiliarum", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_shield_1,itm_roman_gladius_2,itm_legion_hamata_cape_6,itm_legion_hamata_cape_7,itm_legion_hamata_cape_8,
itm_roman_aux_helm_centurio,itm_legio_armored_caligea],
attrib_level_26, wp(165), knows_level_26, roman_face1, roman_face2 ],

["aux_cav_decurio", "Decurio", "Decurii", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_shield_5,itm_roman_shield_1,itm_roman_spatha_2,itm_hasta1,itm_musculata_1,itm_musculata_2,itm_musculata_3,
itm_cav_decurio_helm,itm_cav_decurio_helm_2,itm_cav_decurio_helm_3,itm_legio_armored_caligea]+items_roman_horses,
attrib_level_29, wp(175), knows_level_29, roman_face1, roman_face2 ],
["aux_cav_vexilarius", "Vexilarius Equitem", "Vexilarii Equitem", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_signum_signifer_2,itm_roman_spatha_2,itm_graves_simple,itm_signifer_helm_1,itm_signifer_helm_2,
itm_legion_squamata_12,itm_legion_squamata_13,itm_legion_hamata_7]+items_roman_horses,
attrib_level_29, wp(160), knows_level_29, roman_face1, roman_face2 ],
["aux_cav_vexilarius_praetorian", "Vexilarius Equitem Praetoriani", "Vexilarii Equitem Praetoriani", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_2,itm_signum_signifer_2,itm_graves_simple,itm_auxiliary_cavalry_vecsilary_pretorian_helm,
itm_praetorian_hamata_2,itm_praetorian_hamata_4]+items_roman_horses,
attrib_level_31, wp(165), knows_level_31, roman_face1, roman_face2 ],

["aux_signifer", "Signifer Auxiliari", "Signifer Auxiliari", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_signum_signifer,itm_graves_simple,itm_roman_gladius_2,itm_signifer_auxilia_hamata_1,itm_signifer_helm_1,itm_signifer_helm_2],
attrib_level_29, wp(160), knows_level_29, roman_face1, roman_face2 ],
["aux_centurio", "Centurio Auxiliari", "Centurii Auxiliari", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_aux_centurio_graves,itm_roman_gladius_3,itm_cetratus_aux_1,
itm_cenutrio_aux_hamata_1,itm_cenutrio_aux_squamata_1,itm_auxilia_cent_helmet_1,itm_auxilia_cent_helmet_2,itm_auxilia_cent_helmet_3],
attrib_level_29, wp(160), knows_level_29, roman_face1, roman_face2 ],

#auxilia
["aux_cav", "Auxilia Eques", "Auxilia Equites", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_cetratus_aux_3,itm_cetratus_aux_2,itm_cetratus_aux_4,itm_hasta1,itm_roman_spatha,
itm_auxilia_cavalry_hamata_1,itm_auxilia_cavalry_hamata_2,itm_imp_aux_cav_weiler_brass_a,itm_imp_aux_cav_weiler_brass_b,itm_imp_aux_cav_weiler_brass_c]+items_roman_horses,
attrib_level_26, wp_melee(130), knows_level_26, mercenary_face_1, mercenary_face_2 ],
["aux_cav_eastern", "Auxilia Eques Orientalis", "Auxilia Equites Orientalis", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_2,itm_graves_simple,itm_cetratus_aux_6,itm_cetratus_aux_7,itm_cetratus_aux_8,itm_hasta1,
itm_auxilia_cavalry_squamata_1,itm_auxilia_cavalry_squamata_2,itm_imp_aux_cav_weiler_brass_a,itm_imp_aux_cav_weiler_brass_b,itm_imp_aux_cav_weiler_brass_c]+items_roman_horses,
attrib_level_26, wp_melee(140), knows_level_26, roman_face1, roman_face2 ],
["aux_cav_praetoriani", "Eques Praetoriani", "Eqites Praetoriani", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta1,itm_roman_spatha_2,itm_praetorian_cav_scutum,itm_graves_simple,itm_pretorian_cavalry_helm_1,
itm_praetorian_hamata_1,itm_praetorian_hamata_2,itm_praetorian_hamata_3,itm_praetorian_hamata_4]+items_roman_horses,
attrib_level_29, wp_melee(165), knows_level_29, roman_face1, roman_face2 ],
["aux_cav_praetoriani_2", "Germani Corporis Custos", "Germani Corporis Custodes", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta1,itm_roman_spatha_2,itm_praetorian_cav_scutum_2,itm_centurio_praetorian_graves,itm_pretorian_cavalry_helm_2,itm_pretorian_cavalry_helm_3,
itm_praetorian_hamata_1,itm_praetorian_hamata_3]+horse_leopard,
attrib_level_31, wp_melee(180), knows_level_31, germanic_face_11, germanic_face_12 ],
##new aux regiments:
##new aux inf:
#Alps
["aux_inf_alporum", "Miles Alpinorum", "Milites Alpinorum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta3, itm_roman_aux_helm_1, itm_graves_simple_2, itm_cetratus_aux_26, itm_cetratus_aux_16,
itm_legion_hamata_pants_long_2,itm_legion_hamata_cape_pants_long_2],
attrib_level_23, wp(150), knows_level_23, celtic_face_21, celtic_face_22 ],
["aux_archer_alporum", "Sagittarius Alpinorum", "Sagittarii Alpinorum", tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_aux_helm_1, itm_graves_simple_2,itm_roman_gladius,itm_arrows,itm_short_bow,
itm_legion_hamata_pants_long_2,itm_legion_hamata_cape_pants_long_2],
attrib_level_20, wpe(105,150,150,150), knows_archer_basic, celtic_face_21, celtic_face_22 ],

#africa
["aux_inf_maurorum", "Miles Maurorum", "Milites Maurorum", tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_3,itm_javelin_berber,itm_javelin_berber, itm_roman_aux_helm_2, itm_graves_simple_2, itm_cetratus_aux_15, itm_cetratus_aux_5,
itm_auxilia_hamata_east_1,itm_auxilia_hamata_east_2],
attrib_level_23, wp(150), knows_level_23, north_african_man_face_young_1, north_african_man_face_young_2 ],
["aux_archer_maurorum", "Funditor Maurorum", "Funditores Maurorum", tf_male_north_african|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_2, itm_roman_aux_helm_2, itm_graves_simple_2,
itm_numidian_armor_1,itm_numidian_armor_2,itm_numidian_armor_3,itm_sling,itm_sling_rock1,itm_sling_rock1]+desert_turbans_2,
attrib_level_18, wpe(105,150,150,150), knows_archer_basic, north_african_man_face_young_1, north_african_man_face_young_2 ],

#Hispania
["aux_inf_hispanorum", "Miles Hispanorum", "Milites Hispanorum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta3,itm_javelin, itm_roman_aux_helm_3, itm_graves_simple_2,itm_iberian_heavy1,itm_iberian_heavy2, itm_cetratus_aux_4, itm_cetratus_aux_3,
itm_legion_hamata_7,itm_legion_hamata_cape_3],
attrib_level_23, wp(150), knows_level_23, white_face_21, white_face_22 ],
#they use trp_aux_slinger
# ["aux_archer_hispanorum", "Sagittarius Hispanorum", "Sagittarii Hispanorum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
# [itm_roman_gladius,itm_arrows,itm_short_bow, itm_roman_aux_helm_3, itm_graves_simple_2,itm_iberian_heavy1,itm_iberian_heavy2,
# itm_legion_hamata_7,itm_legion_hamata_cape_3],
# attrib_level_20, wpe(105,150,150,150), knows_level_20, white_face_21, white_face_22 ],

#belgica
["aux_inf_tungrorum", "Miles Tungrorum", "Milites Trungrorum", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_hasta3,itm_graves_simple_2,itm_cetratus_aux_5,itm_cetratus_aux_1,itm_cetratus_aux_6,itm_cetratus_aux_7,itm_cetratus_aux_30,
itm_legion_hamata_cape_pants_long_1,itm_legion_hamata_pants_long_1,itm_1_imp_gallic_b,itm_1_imp_gallic_a,],
attrib_level_23_warrior, wp(150), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],
["aux_archer_tungrorum", "Sagittarius Tungrorum", "Sagittarii Trungrorum", tf_male_barbarian|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_graves_simple_2,itm_legion_hamata_cape_pants_long_1,itm_legion_hamata_pants_long_1,
itm_1_imp_gallic_b,itm_1_imp_gallic_a,itm_long_bow,itm_arrows,itm_arrows],
attrib_level_20_warrior, wpe(105,150,150,150), knows_archer_exp, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],

#Gallia
["aux_inf_gallorum", "Miles Gallorum", "Milites Gallorum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta3,itm_pilum,itm_pilum_2,itm_pilum_3, itm_roman_aux_helm_4,itm_roman_aux_helm_5,itm_cetratus_aux_28, itm_graves_simple_2,itm_cetratus_aux_10, itm_cetratus_aux_16,itm_cetratus_aux_18,
itm_legion_hamata_cape_pants_long_2,itm_legion_hamata_6,itm_legion_hamata_cape_2],
attrib_level_23, wp(150), knows_level_23, celtic_face_21, celtic_face_22 ],
["aux_archer_gallorum", "Sagittarius Gallorum", "Sagittarii Gallorum", tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_aux_helm_4,itm_roman_aux_helm_5, itm_graves_simple_2,itm_arrows,itm_short_bow,itm_roman_gladius,
itm_legion_hamata_cape_pants_long_2,itm_legion_hamata_6,itm_legion_hamata_cape_2],
attrib_level_20,wpe(105,150,150,150), knows_archer_basic, celtic_face_21, celtic_face_22 ],

#germania
["aux_inf_batavorum", "Miles Batavorum", "Milites Batavorum", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_hasta3,itm_graves_simple_2,itm_cetratus_aux_batavorum_inf,itm_1_imp_gallic_b,itm_1_imp_gallic_a,
itm_legion_hamata_cape_pants_long_1,itm_legion_hamata_pants_long_2],
attrib_level_23_warrior, wp(150), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],
["aux_archer_batavorum", "Sagittarius Batavorum", "Sagittarii Batavorum", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_arrows,itm_german_shortbow,itm_graves_simple_2,itm_1_imp_gallic_b,itm_1_imp_gallic_a,
itm_legion_hamata_cape_pants_long_1,itm_legion_hamata_pants_long_2],
attrib_level_20_warrior,wpe(105,150,150,150), knows_archer_exp, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],

#britannia
["aux_inf_brittonum", "Miles Brittonum", "Milites Brittonum", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta3,itm_javelin, itm_javelin, itm_roman_aux_helm_7,itm_roman_aux_helm_2, itm_graves_simple_2,itm_cetratus_aux_19,
itm_legion_hamata_cape_pants_long_3,itm_legion_hamata_cape_pants_long_4],
attrib_level_23, wp(150), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],
["aux_archer_brittonum", "Funditor Brittonum", "Funditores Brittonum", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius, itm_roman_aux_helm_7,itm_roman_aux_helm_2,itm_graves_simple_2,itm_sling,itm_sling_rock1,itm_sling_rock1,
itm_celtic_light1,itm_celtic_light12,itm_celtic_light10],
attrib_level_18,wpe(105,150,150,150), knows_archer_basic, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],

#thracia
["aux_inf_thracum", "Miles Thracum", "Milites Thracum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_hasta3,itm_roman_spatha_3,itm_javelin,itm_roman_aux_helm_6, itm_graves_simple_2,itm_cetratus_aux_20,
itm_legion_squamata_cape_pants_long_1,itm_legion_squamata_cape_pants_long_2,itm_legion_squamata_pants_long_1,itm_legion_squamata_pants_long_2],
attrib_level_23, wp(150), knows_level_23, mercenary_face_greek_1, mercenary_face_greek_2 ],
["aux_archer_thracum", "Sagittarius Thracum", "Sagittarii Thracum", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_roman_aux_helm_6, itm_graves_simple_2,itm_arrows,itm_nomad_bow,
itm_legion_squamata_cape_pants_long_1,itm_legion_squamata_cape_pants_long_2,itm_legion_squamata_pants_long_1,itm_legion_squamata_pants_long_2],
attrib_level_20,wpe(105,150,150,150), knows_archer_exp, mercenary_face_greek_1, mercenary_face_greek_2 ],

#judea
["aux_inf_petreorum", "Miles Petreorum", "Milites Petreorum", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm, no_scene, reserved, fac_culture_7,
[itm_hasta3,itm_javelin, itm_eastern_shoe_y,itm_eastern_shoe_b,itm_eastern_shoe, itm_skirmisher_armor,
itm_auxilia_squamata_east_1,itm_auxilia_squamata_east_3,
itm_turban, itm_desert_turban, itm_cetratus_aux_14],
attrib_level_23, wp(150), knows_level_23, eastern_man_face_young_1, eastern_man_face_middle_2 ],

##new aux cav
##germania
["aux_cav_batavorum", "Eques Batavorum", "Equites Batavorum", tf_male_barbarian|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_roman_spatha_2,itm_hasta1,itm_cetratus_aux_batavorum_cav,itm_1_imp_gallic_a,itm_1_imp_gallic_b,
itm_legion_squamata_cape_pants_long_1,itm_legion_squamata_pants_long_1,
itm_legion_hamata_pants_long_1,itm_legion_hamata_cape_pants_long_1]+items_roman_horses,
attrib_level_23, wp_melee(140), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],

##asia minor
["aux_cav_commagenorum", "Eques Commagenorum", "Equites Commagenorum", tf_male_eastern|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_2,itm_hasta1,itm_nomad_bow,itm_bodkin_arrows,itm_graves_simple_2,
itm_legion_squamata_12,itm_legion_squamata_13,itm_legion_squamata_cape_4,itm_legion_squamata_cape_5,
]+horse_parth+armenian_helm_heavy,
attrib_level_23, wp(145), knows_level_23, eastern_man_face_young_1, eastern_man_face_middle_2 ],

#gaul
["aux_cav_gallorum", "Eques Gallorum", "Equites Gallorum", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_2,itm_hasta1,itm_graves_simple_2,
itm_roman_aux_helm_8,itm_roman_aux_helm_9,itm_cetratus_aux_22,itm_cetratus_aux_24,
itm_legion_hamata_cape_5,itm_legion_hamata_cape_4,itm_legion_hamata_7]+items_roman_horses,
attrib_level_23, wp(140), knows_level_23, germanic_face_11, germanic_face_12 ],

#syria
["aux_cav_ituraeorum", "Eques Ituraeorum", "Equites Ituraeorum", tf_male_eastern|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha,itm_javelin,itm_javelin,itm_legio_armored_caligea,itm_sarranid_mail_shirt,itm_arabian_armor_b,
itm_roman_aux_helm_10,itm_roman_aux_helm_11,itm_cetratus_aux_27,itm_auxilia_squamata_east_1,itm_auxilia_squamata_east_3]+horse_arab,
attrib_level_23, wp(145), knows_level_23, eastern_man_face_young_1, eastern_man_face_middle_2 ],

#syria
["aux_archer_sryrorum", "Auxilia Sagittarius Syrorum", "Auxilia Sagittarii Syrorum", tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_spatha_3,itm_legion_squamata_syria_1,itm_legion_squamata_syria_2,
itm_aux_archer_syorum_helm,itm_aux_archer_syorum_helm1,itm_graves_simple,itm_graves_simple_2,
itm_persian_bow,itm_syrian_barbed_arrows],
attrib_level_23, wpe(105,170,170,170), knows_archer_exp_eastern, eastern_man_face_middle_1, eastern_man_face_old_2 ],


["aux_archer", "Auxilia Sagittarius", "Auxilia Sagittarii", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_graves_simple_2,itm_arrows,itm_nomad_bow,
itm_roman_aux_helm_8,itm_roman_aux_helm_11,itm_roman_townguard_helm,
itm_legion_squamata_5,itm_legion_squamata_6,itm_legion_squamata_7,itm_legion_squamata_8,
],
attrib_level_23, wpe(110,160,160,160), knows_archer_basic, mercenary_face_1, mercenary_face_2 ],
["aux_archer_praetoriana", "Sagittarius Praetoriani", "Sagittarii Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius_3,itm_bodkin_arrows,itm_graves_simple,itm_khergit_bow,
itm_legion_squamata_3,itm_legion_squamata_cape_1,itm_pretorian_archer_helm,
],
attrib_level_26, wpe(140,165,165,165), knows_archer_exp, roman_face1, roman_face2 ],

["aux_slinger", "Baleares Funditor", "Baleares Funditores", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_sling,itm_sling_lead,itm_aux_slinger,itm_aux_slinger_2,itm_aux_slinger_3,itm_graves_simple,itm_roman_gladius,itm_straw_hat,itm_hide_covered_round_shield_2,
itm_mediterranean_straw_hat,itm_mediterranean_straw_hat_1,itm_mediterranean_straw_hat_2],
attrib_level_16, wpe(100,170,170,170), knows_archer_basic, roman_face1, roman_face2 ],

#roman auxilia
["aux_inf", "Miles Auxiliarum", "Milites Auxiliarum", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_roman_spatha_3, itm_pilum,itm_pilum_2,itm_pilum_3,
itm_roman_aux_helm_1,itm_roman_aux_helm_2,itm_roman_aux_helm_3,itm_roman_aux_helm_4,
itm_roman_aux_helm_5,itm_roman_aux_helm_6,itm_roman_aux_helm_7,
itm_roman_aux_helm_8,itm_roman_aux_helm_9,itm_roman_aux_helm_10,itm_roman_aux_helm_11,
itm_legion_hamata_4,itm_legion_hamata_5,itm_legion_hamata_cape_1,
itm_graves_simple_2,itm_cetratus_aux_1,itm_cetratus_aux_2,itm_cetratus_aux_3],
attrib_level_23, wp(160), knows_level_23, white_face_21, white_face_22 ],

["vigilia", "Vigilia", "Vigiliae", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_roman_gladius,itm_roman_townguard_helm,
itm_graves_simple_2,itm_cetratus_aux_1,itm_cetratus_aux_2,itm_cetratus_aux_3,
itm_legion_hamata_6,itm_legion_hamata_cape_1],
attrib_level_16, wp(120), knows_level_12, white_face_21, white_face_22 ],
["vigilia_exp", "Vigilia (exp)", "Vigiliae (exp)", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_roman_townguard_helm,itm_roman_gladius,itm_graves_simple_2,itm_cetratus_aux_1,itm_cetratus_aux_2,itm_cetratus_aux_3,
itm_legion_hamata_6,itm_legion_hamata_cape_1],
attrib_level_18, wp(135), knows_level_18, white_face_11, white_face_12 ],
["vigilia_vet", "Vigilia (vet)", "Vigiliae (vet)", tf_guarantee_boots|tf_guarantee_polearm|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_culture_7,
[itm_hasta2,itm_roman_townguard_helm,itm_roman_gladius,itm_graves_simple_2,itm_cetratus_aux_1,itm_cetratus_aux_2,itm_cetratus_aux_3,
itm_legion_hamata_6,itm_legion_hamata_cape_1],
attrib_level_20, wp(145), knows_level_20, white_face_21, white_face_22 ],
["ballistarii", "Ballistarius", "Ballistarii", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_ballista,itm_ballista_bolts, itm_graves_simple,itm_graves_simple_2,
itm_subarmalis_1,itm_subarmalis_2,itm_subarmalis_3,itm_1_imp_gallic_a,itm_1_imp_gallic_b],
attrib_level_29, wpe(120,200,200,200), knows_level_29, roman_face1, roman_face2 ],

#1
["legio_i_adjutrix_exp", "Miles Legionis (I Adiutrix)", "Milites Legionis (I Adiutrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_i,itm_legio_armored_caligea,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_hamata_11,itm_legion_segmentata_3,itm_1_imp_gallic_c,itm_1_imp_gallic_f_b],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#2
["legio_iii_augusta_exp", "Miles Legionis (III Augusta)", "Milites Legionis (III Augusta)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_iii,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_segmentata_1,itm_legion_hamata_10,itm_1_imp_gallic_f_b_feather,itm_1_imp_gallic_f_n],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#3
["legio_v_alaudae_exp", "Miles Legionis (V Alaudae)", "Milites Legionis (V Alaudae)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_v,
itm_legion_hamata_1,itm_legion_segmentata_2,itm_1_imp_gallic_f_s,itm_1_imp_gallic_g],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#4
["legio_xxi_rapax_exp", "Miles Legionis (XXI Rapax)", "Milites Legionis (XXI Rapax)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xxi,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_legion_hamata_3,itm_legion_segmentata_5,itm_1_imp_gallic_h,itm_1_imp_gallic_i_ac],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#5
["legio_vii_galbia_exp", "Miles Legionis (VII Galbia)", "Milites Legionis (VII Galbia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_vii_galb,
itm_legion_segmentata_cape_1,itm_legion_squamata_14,itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_i_ac_feather_plume],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#6
["legio_vi_victrix_exp", "Miles Legionis (VI Victrix)", "Milites Legionis (VI Victrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_vi_vict,itm_scutum_9,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_squamata_11,itm_legion_hamata_14,itm_1_imp_gallic_i,itm_1_imp_gallic_i_feather],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#7
["legio_xi_claudia_exp", "Miles Legionis (XI Claudia)", "Milites Legionis (XI Claudia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_xi,itm_graves_simple,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_1_imp_gallic_i_ac_plume,itm_1_imp_gallic_i_feather,
itm_legion_hamata_15,itm_legion_segmentata_cape_2],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#8
["legio_xiii_gemina_exp", "Miles Legionis (XIII Gemina)", "Milites Legionis (XIII Gemina)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xiii,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_legion_squamata_10,itm_legion_hamata_13,itm_1_imp_gallic_i_plume,itm_1_imp_itallic_c],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#9
["legio_v_macedonia_exp", "Miles Legionis (V Macedonia)", "Milites Legionis (V Macedonia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_v_mac,
itm_legion_segmentata_cape_3,itm_legion_hamata_16,itm_1_imp_itallic_d,itm_1_imp_gallic_f_s],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#10
["legio_vi_ferrata_exp", "Miles Legionis (VI Ferrata)", "Milites Legionis (VI Ferrata)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_vi_ferr,itm_graves_simple,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,
itm_legion_hamata_cape_6,itm_legion_segmentata_4,itm_1_imp_itallic_g,itm_1_imp_gallic_f_n],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#11
["legio_x_fretensis_exp", "Miles Legionis (X Fretensis)", "Milites Legionis (X Fretensis)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_x,
itm_legion_hamata_cape_7,itm_legion_hamata_2,itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_c],
attrib_level_26, wp(170), knows_level_26, roman_face1, roman_face2 ],
#12
["praetoriani_milites_exp", "Miles Praetoriani", "Milites Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet, no_scene, reserved, fac_culture_7,
[itm_scutum_praetorian,itm_scutum_praetorian_2,itm_graves_simple,itm_roman_gladius_3,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_praetorian_segmentata_1,itm_praetorian_segmentata_2,itm_praetorian_segmentata_3,itm_praetorian_helm_1,itm_praetorian_helm_2],
attrib_level_29, wp(190), knows_level_29, roman_face1, roman_face2 ],

#1
["legio_i_adjutrix_vet", "Evocatus Legionis (I Adiutrix)", "Evocati Legionis (I Adiutrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_i,itm_legio_armored_caligea,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_7,itm_1_imp_gallic_c,itm_1_imp_gallic_f_b, itm_legion_segmentata_manica_2,itm_legion_segmentata_manica_6],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#2
["legio_iii_augusta_vet", "Evocatus Legionis (III Augusta)", "Evocati Legionis (III Augusta)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_iii,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_8,itm_1_imp_gallic_f_b_feather,itm_1_imp_gallic_f_n, itm_legion_segmentata_manica_1,itm_legion_segmentata_manica_5],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#3
["legio_v_alaudae_vet", "Evocatus Legionis (V Alaudae)", "Evocati Legionis (V Alaudae)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_v,itm_legion_segmentata_cape_6,
itm_legion_segmentata_6,itm_1_imp_gallic_f_s,itm_1_imp_gallic_g, itm_legion_segmentata_manica_4,itm_legion_segmentata_manica_8],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#4
["legio_xxi_rapax_vet", "Evocatus Legionis (XXI Rapax)", "Evocati Legionis (XXI Rapax)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xxi,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_cape_5,itm_1_imp_gallic_h,itm_1_imp_gallic_i_ac, itm_legion_segmentata_manica_3,itm_legion_segmentata_manica_7],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#5
["legio_vii_galbia_vet", "Evocatus Legionis (VII Galbia)", "Evocati Legionis (VII Galbia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_vii_galb,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_cape_1,itm_legion_squamata_14,itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_i_ac_feather_plume, itm_legion_segmentata_manica_2,itm_legion_segmentata_manica_6],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#6
["legio_vi_victrix_vet", "Evocatus Legionis (VI Victrix)", "Evocati Legionis (VI Victrix)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_vi_vict,itm_scutum_9,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_squamata_11,itm_1_imp_gallic_i,itm_1_imp_gallic_i_feather, itm_legion_segmentata_manica_1,itm_legion_segmentata_manica_5],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#7
["legio_xi_claudia_vet", "Evocatus Legionis (XI Claudia)", "Evocati Legionis (XI Claudia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_xi,itm_graves_simple,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_1_imp_gallic_i_ac_plume,itm_1_imp_gallic_i_feather,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_cape_2],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#8
["legio_xiii_gemina_vet", "Evocatus Legionis (XIII Gemina)", "Evocati Legionis (XIII Gemina)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_graves_simple,itm_scutum_legio_xiii,itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_squamata_10,itm_1_imp_gallic_i_plume,itm_1_imp_itallic_c, itm_legion_segmentata_manica_4,itm_legion_segmentata_manica_8],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#9
["legio_v_macedonia_vet", "Evocatus Legionis (V Macedonia)", "Evocati Legionis (V Macedonia)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_graves_simple,itm_scutum_legio_v_mac,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_cape_3,itm_1_imp_itallic_d,itm_1_imp_gallic_f_s, itm_legion_segmentata_manica_3,itm_legion_segmentata_manica_7],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#10
["legio_vi_ferrata_vet", "Evocatus Legionis (VI Ferrata)", "Evocati Legionis (VI Ferrata)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_scutum_legio_vi_ferr,itm_graves_simple,itm_pilum,itm_pilum_2,itm_pilum_3,itm_roman_gladius,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_legion_segmentata_cape_4,itm_1_imp_itallic_g,itm_1_imp_gallic_f_n, itm_legion_segmentata_manica_2,itm_legion_segmentata_manica_6],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#11
["legio_x_fretensis_vet", "Evocatus Legionis (X Fretensis)", "Evocati Legionis (X Fretensis)", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_roman_gladius,itm_pilum,itm_pilum_2,itm_pilum_3,itm_graves_simple,itm_scutum_legio_x,itm_legion_segmentata_cape_6,itm_legion_segmentata_6,
itm_1_imp_gallic_i_ac_feather,itm_1_imp_gallic_c, itm_legion_segmentata_manica_1,itm_legion_segmentata_manica_5],
attrib_level_29, wp(200), knows_level_29, roman_face1, roman_face2 ],
#12
["praetoriani_milites_vet", "Evocatus Praetoriani", "Evocati Praetoriani", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_culture_7,
[itm_scutum_praetorian,itm_scutum_praetorian_2,itm_graves_simple,itm_roman_gladius_3,itm_pilum,itm_pilum_2,itm_pilum_3,
itm_praetorian_segmentata_1,itm_praetorian_segmentata_2,itm_praetorian_segmentata_3,itm_praetorian_helm_1,itm_gauntles_1,itm_praetorian_helm_2],
attrib_level_31, wp(220), knows_level_31, roman_face1, roman_face2 ],
##############
##############
##############
#END###########
############

["looter", "Latro", "Latrones", tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_outlaws,
[itm_sling, itm_sling_rock1, itm_leather_boots,itm_pelt_coat,
itm_club,itm_club_2,itm_club_3,itm_spiked_club,itm_head_wrappings,itm_headcloth,itm_woolen_cap,itm_hand_axe,itm_hammer,
itm_simple_hood_1,itm_simple_hood_2,itm_generic_poor1,itm_generic_poor2],
attrib_level_6, wp(50), knows_level_6, bandit_face1, bandit_face2 ],
["bandit", "Leistes", "Leistai", tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield, no_scene, reserved, fac_outlaws,
[itm_wooden_shield,itm_hide_covered_round_shield,itm_hide_covered_round_shield_2,
itm_leather_boots,itm_rawhide_coat,itm_pelt_coat,
itm_fur_hat,itm_nomad_cap,itm_footman_helmet,itm_mace_1,itm_boar_spear,itm_hand_axe,itm_hammer,
itm_simple_hood_1,itm_simple_hood_2,itm_generic_poor1,itm_generic_poor2],
attrib_level_12, wp(80), knows_level_12, bandit_face1, bandit_face2 ],
["brigand", "Sicarius", "Sicarii", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_outlaws,
[itm_throwing_spears,itm_wooden_shield,itm_hide_covered_round_shield,itm_hide_covered_round_shield_2,
itm_leather_boots,itm_rawhide_coat,itm_pelt_coat,
itm_fur_hat,itm_nomad_cap,itm_footman_helmet,itm_hand_axe,itm_mace_1,itm_boar_spear,
itm_simple_hood_1,itm_simple_hood_2,itm_generic_poor1,itm_generic_poor2],
attrib_level_18, wp(110), knows_level_18, bandit_face1, bandit_face2 ],


["mountain_bandit", "Iudaicus Rebellis", "Iudaici Rebellis", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_culture_8,
[itm_spiked_club,itm_sling_rock1,itm_sling_lead,itm_sling,itm_caligea,itm_javelin,itm_club,itm_club_2,itm_club_3,itm_ad_mixed_round_shields_07,
itm_ad_mixed_round_shields_08,itm_old_gladius_1,itm_old_gladius_2,itm_eastern_helm1,itm_sarranid_felt_hat]+jew_tunics_1+jew_tunics_2+jew_robes,
attrib_level_16_warrior, wp(135), knows_level_16_warrior, arab_face_young, arab_face_old ],
["forest_bandit", "Hispanicus Rebellis", "Hispanici Rebellis", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_outlaws,
[itm_celtic_round_shild3,itm_celtic_round_shild2,itm_celtic_round_shild1,itm_iberian_light5,itm_iberian_light6,itm_iberian_heavy1,
itm_iberian_medium2,itm_iberian_medium3,itm_caligea,itm_spear,itm_war_spear,itm_javelin,itm_hand_axe,itm_throwing_spears,
itm_footman_helmet,itm_ad_mixed_round_shields_02,itm_ad_mixed_round_shields_01],
attrib_level_23_warrior, wpe(130,130,130,180), knows_level_23, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],
["sea_raider", "Pirata", "Piratae", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_outlaws,
[itm_short_bow,itm_arrows,itm_spear,itm_kopis,itm_kopfband,itm_iberian_light4,itm_iberian_light1,itm_armenian_tunic_1,itm_bosporan_light1,itm_caligea,itm_roman_aux_helm_old_1,itm_roman_aux_helm_old_2,
itm_hide_covered_round_shield,itm_hide_covered_round_shield_2,itm_hide_covered_round_shield_3,itm_ad_mixed_round_shields_05,itm_ad_mixed_round_shields_06
],
attrib_level_23_warrior, wp(130), knows_level_23_warrior, mercenary_face_1, mercenary_face_2 ],

#steppe bandits are now Alan raiders
["steppe_bandit", "Alanna Baragatae", "Alan Baragatae", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_outlaws,
[itm_light_lance,itm_khergit_bow_2,itm_sarmatian_arrows_1,itm_sarmatian_arrows_2,itm_alan_light_1,itm_alan_light_2,itm_kaftan_1,itm_kaftan_2,itm_kaftan_3,
itm_sarmatian_shoes,itm_alan_long_sword,itm_alan_long_sword_ring,itm_sarmatian_cap_1,itm_sarmatian_cap_2,itm_sarmatian_cap_3,itm_sarmatian_cap_4,itm_alan_light_helm,itm_alan_light_helm,
]+horse_steppe,
attrib_level_23_warrior, wp(150), knows_archer_basic_eastern, scythian_face_21, scythian_face_22 ],

["taiga_bandit", "Illyricus Sicarius", "Illyrici Sicarii", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_outlaws,
[itm_spear,itm_javelin,itm_illyrian_medium3,itm_iberian_light1,itm_iberian_light2,
itm_illyrian_medium4,itm_illyrian_medium1,itm_illyrian_shield_large1,itm_illyrian_shield_large2,
itm_illyrian_shield_heavy1,itm_illyrian_shield_heavy2,
itm_illyrian_shield_heavy3,itm_kopfband,itm_illyrian_leader_cap,itm_illyrian_hevy_helmet,itm_caligea,itm_ad_mixed_round_shields_04,itm_ad_mixed_round_shields_03],
attrib_level_23_warrior, wp(115), knows_level_23_warrior, barbarian_man_face_younger_1, barbarian_man_face_young_2 ],

["slave_warrior", "Seditiosus Servus", "Seditiosi Servi", tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_outlaws,
[itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea,itm_club,itm_club_2,itm_club_3,itm_butchering_knife,itm_torch2,itm_stones,itm_hammer,itm_warhammer],
attrib_level_16_warrior, wp_melee(135), knows_level_16_warrior, mercenary_face_1, mercenary_face_2 ],

["slave_warrior_2", "Seditiosus Pedes", "Seditiosi Pedites", tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_outlaws,
[itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea,itm_simple_thraex_shield,itm_club,itm_club_2,itm_club_3,
itm_old_gladius_2,itm_old_round_shield_1,itm_old_round_shield_2,itm_old_round_shield_3,itm_old_round_shield_4,itm_old_round_shield_5],
attrib_level_18_warrior, wp_melee(150), attrib_level_18_warrior, mercenary_face_1, mercenary_face_2 ],

["slave_warrior_3", "Seditiosus Hastatus", "Seditiosi Hastati", tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_outlaws,
[itm_roman_poor1,itm_legion_hamata_6,itm_legion_hamata_8,itm_legion_hamata_4,itm_roman_poor2,itm_caligea,itm_throwing_spears,
itm_old_spear_1,itm_old_spear_2,itm_roman_aux_helm_old_1,itm_roman_aux_helm_old_2,itm_old_scutum,itm_old_scutum_2,itm_old_scutum_3,itm_old_scutum_4],
attrib_level_20_warrior, wp_melee(165), knows_level_20_warrior, mercenary_face_1, mercenary_face_2 ],

["slave_rebel", "Seditiosus Gladiator", "Seditiosi Gladiatores", tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_outlaws,
[itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea,itm_throwing_spears,itm_flax_onehanded1,itm_throwing_spears,itm_simple_thraex_shield,itm_leather_covered_round_shield,itm_cloak_2,itm_cloak_3,
itm_old_gladius_1,itm_old_gladius_2,itm_butchering_knife,itm_torch2,itm_stones,itm_roman_aux_helm_old_1,itm_roman_aux_helm_old_2,itm_old_spear_1,itm_old_spear_2],
attrib_level_26_warrior, wp_melee(180), knows_level_26_warrior, mercenary_face_1, mercenary_face_2 ],

["slave_rebel_2", "Seditiosus Evocatus", "Seditiosi Evocati", tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_outlaws,
[itm_roman_poor1,itm_roman_poor3,itm_legion_hamata_cape_1,itm_legion_hamata_cape_2,itm_legion_hamata_cape_3,itm_graves_simple,itm_legio_armored_caligea,itm_throwing_spears_roman,itm_flax_onehanded2,itm_old_scutum,itm_old_scutum_2,itm_old_scutum_3,itm_old_scutum_4,
itm_old_gladius_1,itm_old_gladius_2,itm_roman_aux_helm_old_1,itm_roman_aux_helm_old_2,itm_roman_townguard_helm,itm_roman_aux_helm_8],
attrib_level_29_warrior, wp_melee(195), knows_level_29_warrior, mercenary_face_1, mercenary_face_2 ],

["follower_woman", "Camp Follower", "Camp Followers", tf_female|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_female_1,itm_female_2,itm_female_3,itm_female_1_celt,itm_female_2_celt,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb,itm_leather_boots,itm_celtic_boots,
itm_butchering_knife,itm_butchering_knife_2,itm_hammer,itm_hand_axe,itm_stones],
def_attrib|level(2), wp(50), knows_common, refugee_face1, refugee_face2 ],
["hunter_woman", "Hunter Woman", "Hunter Women", tf_female|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_female_1_barb,itm_female_3_celt,itm_female_4_celt,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb,itm_leather_boots,itm_celtic_boots,
itm_butchering_knife,itm_butchering_knife_2,itm_hand_axe, itm_hunting_bow, itm_arrows,itm_fur_covered_shield],
attrib_level_6, wp(85), knows_level_6, refugee_face1, refugee_face2 ],
["fighter_woman", "Camp Defender", "Camp Defenders", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_polearm, no_scene, reserved, fac_commoners,
[itm_female_3_barb,itm_female_4_barb,itm_female_1,itm_female_2,itm_female_3,itm_leather_boots,itm_celtic_boots,itm_fur_covered_shield,itm_simple_thraex_shield,
itm_butchering_knife,itm_butchering_knife_2,itm_arrows,itm_short_bow,itm_boar_spear],
attrib_level_12, wp(100), knows_level_12, refugee_face1, refugee_face2 ],
["sword_sister", "Soldier Wife", "Soldier Wifes", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
[itm_female_3,itm_female_2,itm_female_3_celt,itm_female_2_celt,itm_female_2_barb,itm_female_3_barb,itm_female_4_barb,itm_leather_boots,itm_celtic_boots,
itm_spear, itm_arrows,itm_short_bow,itm_fur_covered_shield,itm_simple_thraex_shield,itm_sword_akinakes],
attrib_level_16, wp(120), knows_level_16, refugee_face1, refugee_face2 ],

["refugee", "Refugee", "Refugees", tf_female|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_knife,itm_pitch_fork,itm_sickle,itm_hand_axe,itm_club,itm_club_2,itm_club_3,itm_hammer,itm_female_1_barb,itm_female_3_barb,itm_female_3,itm_female_3_celt,itm_leather_boots,itm_celtic_boots],
def_attrib|level(1),wp(45), knows_common, refugee_face1, refugee_face2 ],
["peasant_woman", "Peasant Woman", "Peasant Women", tf_female|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_knife,itm_pitch_fork,itm_sickle,itm_hand_axe,itm_club,itm_club_2,itm_club_3,itm_hammer,itm_female_3_celt,itm_female_1_barb,itm_female_2,itm_female_1,itm_leather_boots,itm_celtic_boots],
def_attrib|level(1),wp(40), knows_common, refugee_face1, refugee_face2 ],

["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
[itm_roman_spatha, itm_roman_tunic_2, itm_caligea,itm_horse_1],
attrib_level_20,wp(100),knows_level_20,mercenary_face_1,mercenary_face_2],

["package_slave", "Slave", "Slaves", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac_commoners,
[itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea,itm_knife,itm_butchering_knife,itm_mule_package], def_attrib|level(25), wp(30), knows_common|knows_riding_2, white_face_11, white_face_12 ],

["kidnapped_girl", "Kidnapped Girl", "Kidnapped Girls", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_leather_boots,itm_female_3],
def_attrib|level(2), wp(50), knows_common|knows_riding_2, woman_face_1, woman_face_2 ],

#This troop is the troop marked as soldiers_end and town_walkers_begin
["town_walker_1","Town_walker_begin","Town_walker_begin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[],
def_attrib|level(4),wp(60),knows_common,germanic_face_11,germanic_face_12],

["sarmatian_town_walker", "Sarmatian Noble Tribesman", "Sarmatian Noble Tribesmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_sarmatian_ringsword_1]+nomadic_cives+nomadic_foot_cives,
attrib_level_6, wp(60), knows_level_6, scythian_face_11, scythian_face_12 ],
["sarmatian_town_walker_female", "Sarmatian Noblewoman", "Sarmatian Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_sarmatian_ringsword_1]+nomadic_dress_cives+nomadic_foot_cives,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["bosporan_town_walker", "Bosporan Nobleman", "Bosporan Noblemen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_sarmatian_ringsword_1]+bosporan_cives+bosporan_foot_cives,
attrib_level_6, wp(60), knows_level_6, scythian_face_11, scythian_face_12 ],
["bosporan_town_walker_female", "Bosporan Noblewoman", "Bosporan Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_sarmatian_ringsword_1]+bosporan_dress_cives+bosporan_foot_cives,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["judean_town_walker","Eastern Townsman","Eastern Townsmen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_dagger]+eastern_cives+eastern_roman_tunic+eastern_foot_cives,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["judean_town_walker_female", "Eastern Townswoman", "Eastern Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_sarranid_head_cloth,itm_sarranid_head_cloth_b,itm_sarranid_head_cloth_c,itm_sarranid_head_cloth_d]+eastern_dress_cives+eastern_foot_cives,
attrib_level_6, wp(40), knows_level_6, arab_face_female, arab_face_female2],

["parthian_town_walker","Parthian Nobleman","Parthian Noblemen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_dagger_parthian_1,itm_dagger_parthian_2]+parthian_cives+parthian_foot_cives,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["parthian_town_walker_female","Parthian Noblewoman","Parthian Noblewomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_dagger_parthian_1,itm_dagger_parthian_2]+parthian_dress_cives+parthian_foot_cives,
attrib_level_6,wp(40),knows_level_6,woman_face_1,woman_face_2],

["persian_town_walker","Persian Nobleman","Persian Noblemen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_eastern_spear_149]+persian_cives+persian_foot_cives,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["persian_town_walker_female","Persian Noblewoman","Persian Noblewomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_eastern_spear_149]+persian_dress_cives+persian_foot_cives,
attrib_level_6,wp(40),knows_level_6,woman_face_1,woman_face_2],

["roman_town_walker", "Civis", "Civis", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger]+roman_cives+roman_foot_cives,
attrib_level_6, wp(60), knows_level_6, white_face_21, white_face_22 ],
["roman_town_walker_female", "Civis", "Civis", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_sarranid_head_cloth,itm_sarranid_head_cloth_b,itm_sarranid_head_cloth_c,itm_sarranid_head_cloth_d]+roman_dress_cives+roman_foot_peasant,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["celtic_town_walker", "Celtic Nobleman", "Celtic Noblemen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_celtic_axe1]+celtic_foot_cives+celtic_cives,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["celtic_town_walker_female", "Celtic Noblewoman", "Celtic Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_celtic_axe1]+celtic_foot_cives+celtic_dress_cives,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["germanic_town_walker", "Germanic Nobleman", "Germanic Noblemen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_germanic_axe1]+germanic_foot_cives+germanic_cives,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["germanic_town_walker_female", "Germanic Noblewoman", "Germanic Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_germanic_axe1]+germanic_foot_cives+germanic_dress_cives,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["dacian_town_walker", "Dacian Nobleman", "Dacian Noblemen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dacian_sword]+dacian_cives+dacian_foot_cives,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["dacian_town_walker_female", "Dacian Noblewoman", "Dacian Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dacian_sword]+dacian_foot_cives+dacian_dress_cives,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["armenian_town_walker", "Caucasian Nobleman", "Caucasian Noblemen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_armenian_sword_1]+caucasian_foot_cives+caucasian_cives,
attrib_level_6, wp(60), knows_level_6, armenian_face_young, armenian_face_middle ],
["armenian_town_walker_female", "Caucasian Noblewoman", "Caucasian Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_armenian_sword_1]+caucasian_foot_cives+caucasian_dress_cives,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["arab_town_walker", "Arab Nobleman", "Arab Noblemen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger]+desert_head_peasant+eastern_cives+eastern_foot_cives,
attrib_level_6, wp(60), knows_level_6, eastern_man_face_young_1, eastern_man_face_old_2 ],
["arab_town_walker_female", "Arab Noblewoman", "Arab Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_sarranid_head_cloth,itm_sarranid_head_cloth_b,itm_sarranid_head_cloth_c,itm_sarranid_head_cloth_d]+eastern_dress_cives+eastern_foot_cives,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

["berber_town_walker", "Berber Nobleman", "Berber Noblemen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_numidian_spear_1]+berber_foot_cives+berber_cives+berber_head_peasant,
attrib_level_6, wp(60), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],
["berber_town_walker_female", "Berber Noblewoman", "Berber Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_numidian_spear_1,itm_sarranid_head_cloth,itm_sarranid_head_cloth_b,itm_sarranid_head_cloth_c,itm_sarranid_head_cloth_d]+berber_foot_cives+berber_dress_cives,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

["garamantian_town_walker", "Garamantian Nobleman", "Garamantian Noblemen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_numidian_spear_1]+garamantian_foot_cives+garamantian_cives+garamantian_head_peasant,
attrib_level_6, wp(60), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],
["garamantian_town_walker_female", "Garamantian Noblewoman", "Garamantian Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dagger,itm_numidian_spear_1,itm_sarranid_head_cloth,itm_sarranid_head_cloth_b,itm_sarranid_head_cloth_c,itm_sarranid_head_cloth_d]+garamantian_foot_cives+garamantian_dress_cives,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

["boy", "Boy", "Boys", tf_boy|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea],
def_attrib|level(1)|agi_22, wp(10), knows_common|knows_athletics_8, 0x000000000400300436db6db6db6db6db00000000001db6db0000000000000000, 0x000000001000100536db6db6db6c049100000000001db6db0000000000000000 ],
["girl", "Girl", "Girls", tf_girl|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_commoners,
[itm_female_3,itm_female_1,itm_female_2,itm_caligea],
def_attrib|level(1)|agi_18, wp(10), knows_common|knows_athletics_5, 0x000000000000300136db4db6071fffff00000000001db6c00000000000000000, 0x000000000000500236db6db6db7c000000000000001dbadb0000000000000000 ],

["african_man","Nubian Tribesman", "Nubian Tribesmen", tf_male_black|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_garamantes,
[itm_knife,itm_garmantian_armor_1,itm_garmantian_armor_2,itm_garmantian_armor_3,itm_garmantian_armor_4,itm_garmantian_armor_5,itm_headcloth,itm_turban,itm_caligea,itm_numidian_armor_1,itm_numidian_armor_2,itm_numidian_armor_3,itm_numidian_armor_5],
attrib_level_6, wp(60), knows_level_6, nubian_man_face_younger_1, nubian_man_face_older_2 ],
["african_woman","Nubian Tribeswoman", "Nubian Tribeswomen", tf_female|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_garamantes,
[itm_knife,itm_sarranid_common_dress,itm_head_wrappings,itm_caligea],
attrib_level_6, wp(40), knows_riding_2, african_face_female, african_face_female2 ],

["saka_man","Saka Tribesman", "Saka Tribesmen", tf_male|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_dahae,
[itm_knife,itm_sarmatian_shoes, itm_kaftan_1, itm_kaftan_2,itm_kaftan_3,itm_saka_cap_1,itm_saka_hat_1,itm_saka_cap_2,itm_saka_hat_2,itm_saka_cap_3,itm_saka_hat_3],
attrib_level_6, wp(60), knows_level_6, saka_face_1, saka_face_2 ],
["saka_woman","Saka Tribeswoman", "Saka Tribeswomen", tf_female|tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_dahae,
[itm_saka_hat_2,itm_saka_hat_3,itm_saka_hat_1]+nomadic_dress_peasant+nomadic_foot_peasant+nomadic_weapons_peasant,
attrib_level_6, wp(40), knows_level_6, saka_face_female_1, saka_face_female_2 ],

["sarmatian_village_walker", "Sarmatian Tribesman", "Sarmatian Tribesmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+nomadic_tunic+nomadic_foot_peasant+nomadic_head_peasant+nomadic_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, scythian_face_11, scythian_face_12 ],
["sarmatian_village_walker_female", "Sarmatian Tribeswoman", "Sarmatian Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+nomadic_dress_peasant+nomadic_foot_peasant+nomadic_weapons_peasant,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["bosporan_village_walker", "Bosporan Peasant", "Bosporan Peasants", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+bosporan_tunic+bosporan_foot_peasant+bosporan_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, scythian_face_11, scythian_face_12 ],
["bosporan_village_walker_female", "Bosporan Peasant", "Bosporan Peasants", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+bosporan_dress_peasant+bosporan_foot_peasant+bosporan_weapons_peasant,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["judean_village_walker","Eastern Peasant","Eastern Peasants",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_dagger]+eastern_roman_tunic+eastern_foot_peasant+roman_weapons_peasant,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["judean_village_walker_female", "Eastern Peasant", "Eastern Peasants", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_head_wrappings,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b]+eastern_dress_peasant+eastern_foot_peasant+roman_weapons_peasant,
attrib_level_6, wp(40), knows_level_6, arab_face_female, arab_face_female2],

["parthian_village_walker","Parthian Tribesman","Parthian Tribesmen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[]+parthian_tunic+persian_tunic_sheepskin+parthian_foot_peasant+parthian_head_peasant+parthian_weapons_peasant,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["parthian_village_walker_female","Parthian Tribeswoman","Parthian Tribeswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[]+parthian_dress_peasant+parthian_foot_peasant+parthian_weapons_peasant,
attrib_level_6,wp(40),knows_level_6,woman_face_1,woman_face_2],

["persian_village_walker","Persian Peasant","Persian Peasants",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[]+persian_tunic+persian_tunic_sheepskin+persian_foot_peasant+persian_head_peasant+parthian_weapons_peasant,
attrib_level_6,wp(60),knows_level_6,eastern_man_face_younger_1,eastern_man_face_older_2],
["persian_village_walker_female","Persian Peasant","Persian Peasants",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[]+persian_dress_peasant+persian_foot_peasant+parthian_weapons_peasant,
attrib_level_6,wp(40),knows_level_6,woman_face_1,woman_face_2],

["roman_village_walker", "Roman Peasant", "Roman Peasants", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+roman_tunic+roman_foot_peasant+roman_weapons_peasant+roman_head_peasant,
attrib_level_6, wp(60), knows_level_6, white_face_21, white_face_22 ],
["roman_village_walker_female", "Roman Peasant", "Roman Peasants", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+roman_dress_peasant+roman_foot_peasant+roman_weapons_peasant,
attrib_level_6, wp(40), knows_level_6, woman_face_1, woman_face_2 ],

["celtic_village_walker", "Celtic Tribesman", "Celtic Tribesmen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_celtic_axe1]+celtic_foot_peasant+celtic_tunic+celtic_head_peasant+celtic_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["celtic_village_walker_female", "Celtic Tribeswoman", "Celtic Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_celtic_axe1]+celtic_foot_peasant+celtic_dress_peasant+celtic_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["germanic_village_walker", "Germanic Tribesman", "Germanic Tribesmen", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+germanic_foot_peasant+germanic_tunic+germanic_head_peasant+germanic_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["germanic_village_walker_female", "Germanic Tribeswoman", "Germanic Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+germanic_foot_peasant+germanic_dress_peasant+germanic_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["dacian_village_walker", "Dacian Peasant", "Dacian Peasant", tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+dacian_tunic+dacian_foot_peasant+dacian_head_peasant+dacian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, barbarian_man_face_younger_1, barbarian_man_face_older_2 ],
["dacian_village_walker_female", "Dacian Peasant", "Dacian Peasants", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+dacian_foot_peasant+dacian_dress_peasant+dacian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["armenian_village_walker", "Caucasian Tribesman", "Caucasian Tribesmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+persian_tunic_sheepskin+caucasian_foot_peasant+caucasian_tunic+caucasian_head_peasant+caucasian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, armenian_face_young, armenian_face_middle ],
["armenian_village_walker_female", "Caucasian Tribeswoman", "Caucasian Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+caucasian_foot_peasant+caucasian_dress_peasant+caucasian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, woman_face_1, woman_face_2 ],

["arab_village_walker", "Arab Tribesman", "Arab Tribesmen",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+desert_head_peasant+desert_tunic+eastern_foot_peasant+desert_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, eastern_man_face_young_1, eastern_man_face_old_2 ],
["arab_village_walker_female", "Arab Tribeswoman", "Arab Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_head_wrappings,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b]+eastern_dress_peasant+eastern_foot_peasant+desert_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

["berber_village_walker", "Berber Tribesman", "Berber Tribesmen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+berber_foot_peasant+berber_tunic+berber_head_peasant+berber_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],
["berber_village_walker_female", "Berber Tribeswoman", "Berber Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_head_wrappings,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b]+berber_foot_peasant+berber_dress_peasant+berber_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

["garamantian_village_walker", "Garamantian Tribesman", "Garamantian Tribesmen",tf_male_north_african|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+garamantian_foot_peasant+garamantian_tunic+garamantian_head_peasant+garamantian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, north_african_man_face_middle_1, north_african_man_face_older_2 ],
["garamantian_village_walker_female", "Garamantian Tribeswoman", "Garamantian Tribeswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_head_wrappings,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b]+garamantian_foot_peasant+garamantian_dress_peasant+garamantian_weapons_peasant,
attrib_level_6, wp(60), knows_level_6, arab_face_female, arab_face_female2 ],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
["spy_walker_1", "Nobleman", "Noblemen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_dacian_noble4,itm_dacian_noble5,itm_dacian_noble6,itm_celtic_boots],
def_attrib|level(4), wp(60), knows_common, white_face_11, white_face_12 ],
["spy_walker_2", "Noblewoman", "Noblewomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_leather_boots,itm_barb_femal_rich1,itm_barb_femal_rich1,itm_barb_femal_rich1,itm_barb_femal_rich1],
def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
# Ryan END
#This troop is the troop marked as spy_walkers_end
["tournament_master","Spywalkers END","Spywalkers END",tf_hero, no_scene,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],

#special slave trader
["Ramun_the_slave_trader","Ramun","Ramun",tf_hero, no_scene,reserved, fac_commoners,[itm_roman_rich3, itm_caligea],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

#special gladiators for Roman tournaments
["Xerina","Tetraites ","Tetraites ",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_caligea],
def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_10|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x0000000b3d01300925528eb8da4c06db00000000001ec62a0000000000000000],
["Dranton","Spiculus","Spiculus",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor2,itm_caligea],
def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000bbf10d012588c55bada6506db00000000001d24e20000000000000000],
["Kradus","Hermes","Hermes",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor3,itm_caligea],
def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1112c61ce06b7a1db137d200000000001cd31b0000000000000000],
["Flamma","Flamma","Flamma",tf_hero, no_scene,reserved,  fac_commoners
,[itm_roman_poor1,itm_caligea],
def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000b3f10b20b294c735ed97a24e400000000001c8a6b0000000000000000],
["Marcus_Attilius","Marcus Attilius","Marcus Attilius",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_caligea],
def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x000000002d05300445596ef85b6c06db00000000001d26d80000000000000000],
["Diocles","Appuleius Diocles","Appuleius Diocles",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_caligea],
def_attrib|str_15|agi_20|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x000000062e01200b491acdbce29658f400000000001d475c0000000000000000],
["Scorpius","Scorpus","Scorpus",tf_hero, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_caligea],
def_attrib|str_15|agi_20|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_10|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x00000007ee11100a571b75d8ab6c96db00000000001d38930000000000000000],
["tutorial_trainer","Tournament Champions END","Tournament Champions END",tf_hero, 0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],

#athletes for olympia
["athlet_1","Novice Athlet","Novice Athlets",tf_guarantee_armor|tf_guarantee_boots, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_caligea],
str_15|agi_15|int_6|cha_6|level(10),wp(120),knows_power_strike_4|knows_ironflesh_4|knows_riding_4|knows_power_throw_4|knows_athletics_4,roman_face1,roman_face2],
["athlet_2","Experienced Athlet","Experienced Athlets",tf_male_north_african|tf_guarantee_armor|tf_guarantee_boots, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_caligea],
str_17|agi_17|int_6|cha_6|level(15),wp(160),knows_power_strike_6|knows_ironflesh_6|knows_riding_6|knows_power_throw_6|knows_athletics_6,north_african_man_face_younger_1,north_african_man_face_younger_2],
["athlet_3","Famous Athlet","Famous Athlets",tf_guarantee_armor|tf_guarantee_boots, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_caligea],
str_19|agi_19|int_6|cha_6|level(20),wp(200),knows_power_strike_8|knows_ironflesh_8|knows_riding_8|knows_power_throw_8|knows_athletics_8,persian_face_young,persian_face_middle],
["athlet_4","Champion","Champions",tf_guarantee_armor|tf_guarantee_boots, no_scene,reserved,  fac_commoners,
[itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_caligea],
str_21|agi_21|int_6|cha_6|level(25),wp(240),knows_power_strike_10|knows_ironflesh_10|knows_riding_10|knows_power_throw_10|knows_athletics_10,white_face_11,white_face_12],


#special slave trader
["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x00000004718201c073191a9bb10c44eb00000000001d9b220000000000000000],

#SB : semi-random arena training rewards
["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,
[itm_roman_gladius, itm_roman_poor1,itm_caligea],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,
[itm_roman_spatha,itm_roman_toga,itm_caligea],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,
[itm_hasta1,itm_roman_poor3,itm_caligea],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,
[itm_dagger,itm_roman_toga,itm_caligea],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,
[itm_eastern_sowrd1,itm_roman_poor2,itm_caligea],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
["ransom_broker_1","Venalicius","Venalicius",tf_hero, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x000000082f0010091683adc88c6f5b2a00000000001ddb110000000000000000],

["ransom_broker_2","Doulon Emporos","Doulon Emporos",tf_hero, 0, reserved, fac_commoners,
[itm_sarranid_cloth_robe_fancy_3,itm_eastern_shoe_r],def_attrib|level(5),wp(20),knows_common,0x000000087100b20536916936daa2a86b00000000001d37680000000000000000],

["ransom_broker_3","Venalicius","Venalicius",tf_hero, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x0000000f540020011683a9c88c6f5b2a00000000001ddb310000000000000000],

["ransom_broker_4","Doulon Emporos","Doulon Emporos",tf_hero, 0, reserved, fac_commoners,
[itm_bosporan_light2,itm_eastern_shoe_y],def_attrib|level(5),wp(20),knows_common,0x00000004a300c18448936d36daa2a86b00000000001cb7680000000000000000],

["ransom_broker_5","Venalicius","Venalicius",tf_hero, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x00000007a201301236db6db6db6db6db00000000001db6db0000000000000000],

["ransom_broker_6","Doulon Emporos","Doulon Emporos",tf_hero, 0, reserved, fac_commoners,
[itm_parthian_tunic_4,itm_eastern_shoe],def_attrib|level(5),wp(20),knows_common,0x0000000a2c00700036db6db6db6db6db00000000001db6db0000000000000000],

["ransom_broker_7","Venalicius","Venalicius",tf_hero, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x00000007c10021c51683a9c88c6f5b2a00000000001ddb310000000000000000],

["ransom_broker_8","Doulon Emporos","Doulon Emporos",tf_hero, 0, reserved, fac_commoners,
[itm_sarmatian_light1,itm_eastern_shoe_b],def_attrib|level(5),wp(20),knows_common,0x0000000c8d00c08536db6db6db6db6db00000000001db6db0000000000000000],

["ransom_broker_9","Venalicius","Venalicius",tf_hero, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,0x0000000a4d0015d11683a9c88c6f5b2a00000000001ddb110000000000000000],

["ransom_broker_10","Doulon Emporos","Doulon Emporos",tf_hero, 0, reserved, fac_commoners,
[itm_dacian_noble3,itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,0x0000000d0000204d4c606d36dc7664a500000000001e5d200000000000000000],

# Tavern traveler.
["tavern_traveler_1","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dacian_noble2,itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,mercenary_face_greek_1,mercenary_face_greek_2],
["tavern_traveler_2","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dacian_noble1,itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,mercenary_face_greek_1,mercenary_face_greek_2],
["tavern_traveler_3","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dacian_noble4,itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,mercenary_face_greek_1,mercenary_face_greek_2],
["tavern_traveler_4","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_dacian_noble6,itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,mercenary_face_greek_1,mercenary_face_greek_2],

["tavern_traveler_5","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,roman_face1,roman_face2],
["tavern_traveler_6","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_poor3, itm_caligea],def_attrib|level(5),wp(20),knows_common,roman_face1,roman_face2],
["tavern_traveler_7","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_poor2, itm_caligea],def_attrib|level(5),wp(20),knows_common,roman_face1,roman_face2],

["tavern_traveler_8","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_scythian_light2, itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,scythian_face_11,scythian_face_12],

["tavern_traveler_9","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_toga,itm_caligea],def_attrib|level(5),wp(20),knows_common,roman_face1,roman_face2],

["tavern_traveler_10","Carant","Carant",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_celtic_light2, itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,celtic_face_11,celtic_face_12],
##new travellers, with so many towns we need more travellers
["tavern_traveler_11","Weljakwumo","Weljakwumo",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_minotaur_armor,itm_linen_tunic, itm_celtic_boots],def_attrib|level(5),wp(20),knows_common,celtic_face_11,celtic_face_12],

["tavern_traveler_12","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_toga, itm_caligea],def_attrib|level(5),wp(20),knows_common,persian_face_young,persian_face_middle],

["tavern_traveler_13","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_parthian_tunic_1, itm_eastern_shoe_r],def_attrib|level(5),wp(20),knows_common,persian_face_young,persian_face_middle],
["tavern_traveler_14","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_parthian_tunic_2, itm_eastern_shoe_b],def_attrib|level(5),wp(20),knows_common,arab_face_young,arab_face_old],
["tavern_traveler_15","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_armenian_tunic_1, itm_eastern_shoe],def_attrib|level(5),wp(20),knows_common,persian_face_young,persian_face_middle],

["tavern_traveler_16","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_scythian_light5, itm_eastern_shoe_y],def_attrib|level(5),wp(20),knows_common,scythian_face_21,scythian_face_22],
["tavern_traveler_17","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_scythian_light3, itm_eastern_shoe],def_attrib|level(5),wp(20),knows_common,scythian_face_21,scythian_face_22],
["tavern_traveler_18","Epelytes","Epelytes",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_scythian_light4, itm_eastern_shoe_b],def_attrib|level(5),wp(20),knows_common,scythian_face_21,scythian_face_22],

["tavern_traveler_19","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_poor1, itm_caligea],def_attrib|level(5),wp(20),knows_common,african_face_younger,african_face_older],
["tavern_traveler_20","Viator","Viator",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_roman_toga_2, itm_caligea],def_attrib|level(5),wp(20),knows_common,nubian_face1,nubian_face2],

# Tavern traveler.
["tavern_bookseller_1","Librarius","Librarius",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
[itm_roman_toga,itm_caligea,		itm_book_tactics,itm_book_persuasion,itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_training_reference,itm_book_surgery_reference]
,def_attrib|level(5),wp(20),knows_common,celtic_face_11,celtic_face_12],
["tavern_bookseller_2","Librarius","Librarius",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
[itm_roman_poor3,itm_caligea,		itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_engineering,itm_book_weapon_mastery],
def_attrib|level(5),wp(20),knows_common,white_face_11,white_face_12],
["tavern_bookseller_3","Biblos Emporos","Biblos Emporos",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
[itm_sarranid_cloth_robe_fancy_1,itm_caligea,		itm_book_tactics,itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_engineering,itm_book_weapon_mastery],
def_attrib|level(5),wp(20),knows_common,persian_face_young,persian_face_middle],
["tavern_bookseller_4","Librarius","Librarius",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
[itm_roman_poor2,itm_caligea,		itm_book_persuasion,itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_engineering,itm_book_weapon_mastery],
def_attrib|level(5),wp(20),knows_common,roman_face1,roman_face2],

# Tavern minstrel.
["tavern_minstrel_1","Bardos","Bardos",tf_hero, 0, reserved, fac_commoners,
[itm_celtic_light3, itm_celtic_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,0x0000000c440021c136e98cb49b7406db00000000001db6a10000000000000000],

["tavern_minstrel_2","Poietes","Poietes",tf_hero, 0, reserved, fac_commoners,
[itm_scythian_light1, itm_celtic_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,0x000000084000d1c636db6db6db6db6db00000000001db6cb0000000000000000],

["tavern_minstrel_3","Poietes","Poietes",tf_hero, 0, reserved, fac_commoners,
[itm_sarranid_cloth_robe_fancy_2,itm_eastern_shoe, itm_lyre],def_attrib|level(5),wp(20),knows_common,0x000000024000e5d236e14c31dfafe6db00000000001e37330000000000000000],

["tavern_minstrel_4","Poeta","Poeta",tf_hero, 0, reserved, fac_commoners,
[itm_roman_poor2,itm_caligea, itm_lyre],def_attrib|level(5),wp(20),knows_common,0x0000000c2b00200358db6f36db6db75300000000001db6db0000000000000000],

["tavern_minstrel_5","Poeta","Poeta",tf_hero, 0, reserved, fac_commoners,
[itm_roman_poor3,itm_caligea, itm_flute],def_attrib|level(5),wp(20),knows_common,0x00000009e30024c2255b54b7692da46a00000000001c9b180000000000000000],

#NPC system changes begin
#Companions
["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

["npc1","Pravare Ytarim","Pravare Ytarim",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
[itm_scythian_light2,itm_eastern_shoe,itm_one_handed_war_axe_a],
str_12|agi_15|int_12|cha_7|level(3),wp(60),
knows_tracker_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_4,0x000000017f0861433512bad6db6db74200000000001ca4840000000000000000],

["npc2","Marius Gaius","Marius Gaius", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
[itm_roman_toga,itm_caligea,itm_roman_gladius],
str_9|agi_7|int_16|cha_9|level(1),wp(40),
knows_merchant_npc|knows_trade_5|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,0x000000017f00d0012a53b5b6dba2c4db00000000001e49410000000000000000],
["npc3", "Pulchra", "Pulchra", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_female_2,itm_knife,itm_caligea],
str_6|agi_9|int_17|cha_14|level(1), wp(20),
knows_merchant_npc|knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1, 0x000000008304004158037088db85925b00000000001d00980000000000000000 ],
["npc4", "Abadutiker", "Abadutiker", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_fur_covered_shield,itm_linen_tunic,itm_war_spear,itm_celtic_boots,itm_throwing_spears,itm_one_handed_battle_axe_a],
str_16|agi_15|int_14|cha_14|level(10), wp(130),
knows_warrior_npc|knows_weapon_master_2|knows_power_strike_3|knows_riding_2|knows_athletics_2|knows_power_throw_4|knows_first_aid_1|knows_surgery_1|knows_tactics_4|knows_leadership_4, 0x00000000000d1312469ded39234db6db00000000001e475c0000000000000000 ],

["npc5","Satibarzanes","Satibarzanes",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
[itm_sarmatian_shoes, itm_kopis,itm_steppe_horse_1, itm_nomad_bow,itm_arrows,itm_kaftan_1],
str_12|agi_12|int_12|cha_7|level(5),wp(90),
knows_warrior_npc|knows_riding_4|knows_horse_archery_4|knows_power_draw_4|knows_leadership_2|knows_weapon_master_1,0x00000000bf10b18b5c6f972328324a6200000000001cd3310000000000000000],

["npc6", "Firentrix", "Firentix", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_iberian_light5,itm_caligea,itm_kopis,itm_wooden_shield],
str_12|agi_12|int_10|cha_5|level(6), wp(105),
knows_warrior_npc|knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1, 0x00000001660122c336d8951edbc7f7ff00000000001d32090000000000000000 ],

["npc7","Lavia","Lavia",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
[itm_female_2_barb,itm_leather_boots, itm_hunting_bow, itm_arrows, itm_dagger],
str_8|agi_9|int_10|cha_6|level(2),wp(80),
knows_tracker_npc|knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,0x00000000bc08e04618a17a80fbb9a6f300000000001d47930000000000000000],

["npc8", "Hildr", "Hildr", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_germanic_axe2,itm_linen_tunic,itm_celtic_boots],
str_30|agi_30|int_3|cha_3|level(23), wp(200),
knows_warrior_npc|knows_weapon_master_7|knows_power_strike_10|knows_athletics_5, 0x00000007800c004a0b897db6db6d98e300000000001cd77b0000000000000000 ],

["npc9", "Aturius Spurus", "Aturius Spurus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_roman_gladius,itm_roman_toga,itm_caligea,itm_horse_3],
str_12|agi_8|int_7|cha_8|level(2), wp(100),
knows_warrior_npc|knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1, 0x000000008c01100f491b7db6db6ed96300000000001ca4f00000000000000000 ],

["npc10", "Attaklos", "Attaklos", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_hide_covered_round_shield, itm_leather_gloves,itm_mail_hauberk,itm_graves_simple_2,itm_pickaxe,itm_war_bow,itm_khergit_arrows],
str_17|agi_11|int_9|cha_11|level(12), wp(160),
knows_warrior_npc|knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2|knows_power_draw_5, 0x00000000ff08c5c6572c91c71c8d46cb00000000001e468a0000000000000000 ],

["npc11", "Dionysia", "Dionysia", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_female_3,itm_caligea,itm_knife],
str_8|agi_11|int_16|cha_9|level(14), wp(70),
knows_merchant_npc|knows_weapon_master_1|knows_surgery_2|knows_first_aid_4|knows_wound_treatment_4|knows_ironflesh_3|knows_inventory_management_5, 0x00000000bf04505a5915aa226b4d975200000000001ea49e0000000000000000 ],

["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
[itm_roman_toga,itm_caligea, itm_dagger],
str_9|agi_7|int_18|cha_10|level(14),wp(30),
knows_merchant_npc|knows_ironflesh_1|knows_power_strike_1|knows_surgery_6|knows_wound_treatment_6|knows_first_aid_6,0x00000000ac01200e4f8ba62a9c95d36d00000000001d26250000000000000000],

["npc13", "Chanakya", "Chanakya", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_kaftan_2,itm_sarmatian_shoes,itm_horse_2,itm_lance,itm_sarmatian_ringsword_1],
str_12|agi_7|int_12|cha_8|level(3), wp(80),
knows_warrior_npc|knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1, 0x00000000ff0544885f4e9592de4e574c00000000001e369c0000000000000000 ],

["npc14", "Titus", "Titus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_roman_rich3,itm_roman_gladius,itm_caligea],
str_12|agi_8|int_11|cha_8|level(5), wp(100),
knows_warrior_npc|knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1, 0x00000001b011259144d5d1d6eb55e96a00000000001db0db0000000000000000 ],
["npc15", "Artimenus", "Artimenus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_legion_segmentata_cape_1,itm_roman_gladius],
str_16|agi_12|int_17|cha_8|level(17), wp(120),
knows_warrior_npc|knows_tactics_5|knows_engineer_8|knows_trade_3|knows_tracking_1|knows_spotting_1, 0x00000000bf1000102b4b9123594eab5300000000001d55360000000000000000 ],
["npc16", "Titocuna", "Titocuna", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_celtic_boots,itm_dagger,itm_throwing_knives,itm_female_2_celt],
str_7|agi_11|int_8|cha_7|level(2), wp(80),
knows_tracker_npc|knows_power_throw_3|knows_athletics_2|knows_power_strike_1, 0x00000000c00c1047084a6d16db65c6db00000000001c53eb0000000000000000 ],

##dialogue done
["npc17", "Anicetus", "Anicetus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_2,itm_lamellar_armor,itm_eastern_helm6,itm_armenian_sword_1,itm_hide_covered_round_shield],
str_17|agi_15|int_14|cha_18|level(24), wp(180), knows_veteran_npc|knows_prisoner_management_4, 0x0000000a400d15d16b5982b6db89b78700000000001c42250000000000000000 ],

["npc18", "Arminius", "Arminius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_1,itm_1_imp_gallic_h_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170), knows_veteran_npc, 0x00000001b608000936a38dd6eb70eaf100000000001ceb140000000000000000 ],

["npc19", "Tertius Maior", "Tertius Maior", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_2,itm_1_imp_gallic_c_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170), knows_veteran_npc, 0x0000000198092011591491269a92269400000000001cb4aa0000000000000000 ],
["npc20", "Secundus Minor", "Secundus Minor", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_3,itm_1_imp_gallic_f_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170), knows_veteran_npc, 0x000000019b09215236dc4a6b1426c91c00000000001cdb4c0000000000000000 ],
["npc21", "Drusus", "Drusus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_4,itm_1_imp_gallic_i_ac_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170), knows_veteran_npc, 0x00000001b704b0092d5d6dd2dd91d8a300000000001ee6510000000000000000 ],

["npc22", "Libertus Tiro", "Libertus Tiro", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_5,itm_1_imp_gallic_i_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170),knows_veteran_npc, 0x000000019d093008449b51c852c9b73500000000001dca920000000000000000 ],
["npc23", "Marcus Tullius", "Marcus Tullius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_6,itm_1_imp_gallic_i_ac_plume],
str_17|agi_15|int_14|cha_17|level(23), wp(170),knows_veteran_npc, 0x00000001b40035c847326e395f7648e300000000001f66c10000000000000000 ],
["npc24", "Sidonius Apollinaris", "Sidonius Apollinaris", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_7,itm_1_imp_gallic_h_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170),knows_veteran_npc, 0x00000001b60c2009368a87332254a0a100000000001e36e50000000000000000 ],
["npc25", "Sollius Modestus", "Sollius Modestus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_8,itm_1_imp_gallic_c_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170),knows_veteran_npc, 0x000000018010e00b6d2c6a44644e691600000000001e1d9d0000000000000000 ],
["npc26", "Albinus Basilius", "Albinus Basilius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_3,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_1,itm_1_imp_gallic_f_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170),knows_veteran_npc, 0x000000019c0d35844ae34f086baa3b01000000000010c6ec0000000000000000 ],
["npc27", "Lucullus Caepio", "Lucullus Caepio", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
 [itm_graves_simple,itm_sumpter_horse,itm_legion_segmentata_cape_6,itm_roman_gladius,itm_1_imp_gallic_i_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170),knows_veteran_npc, 0x00000001b904b004671435d51ba91ab300000000001ec7140000000000000000 ],
["npc28", "Anicius", "Anicius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_2,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_2,itm_1_imp_gallic_i_ac_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170),knows_veteran_npc, 0x000000018804128e34e66ec65c8956e300000000001db5930000000000000000 ],
["npc29", "Fabianus", "Fabianus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_2,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_3,itm_1_imp_gallic_h_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170), knows_veteran_npc, 0x00000001a504b14e4af481d6b24e448c00000000001734db0000000000000000 ],
["npc30", "Rombus", "Rombus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_2,itm_praetorian_cav_scutum,itm_roman_spatha,itm_hasta2,itm_legion_hamata_cape_4,itm_1_imp_gallic_c_plume],
str_17|agi_15|int_15|cha_17|level(23), wp(170), knows_veteran_npc, 0x00000001b808100939cbe544e12648a300000000001e9a820000000000000000 ],
["npc31", "Ra Karak", "Ra Karak", tf_hero|tf_unmoveable_in_party_window|tf_randomize_face, no_scene, reserved, fac_commoners,
[itm_armor_of_african_gods,itm_leather_covered_round_shield,itm_throwing_spears,itm_war_spear,itm_arabian_horse_a,itm_1_imp_gallic_f_plume,itm_caligea],
str_30|agi_20|int_9|cha_15|level(40), wp(300), knows_veteran_npc|knows_ironflesh_10|knows_power_strike_10, african_face_younger,african_face_older ],
["npc32", "Gaius Lemonius", "Gaius Lemonius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_2,itm_officer_shield_2,itm_roman_spatha,itm_hasta1,itm_khergit_elite_armor,itm_1_imp_gallic_i_plume],
str_16|agi_12|int_10|cha_10|level(10), wp(120), knows_merchant_npc|knows_warrior_npc, 0x000000000609210f2a926992a5c9364400000000001e5a960000000000000000 ],
["npc33", "Lucius Modius minor", "Lucius Modius minor", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_horse_1,itm_officer_shield,itm_roman_spatha,itm_hasta1,itm_legion_squamata_cape_3,itm_1_imp_gallic_i_ac_plume],
str_16|agi_12|int_10|cha_10|level(10), wp(120), knows_merchant_npc|knows_warrior_npc, 0x000000001c08b00f593246272370a29500000000001e17a40000000000000000 ],
["npc34", "Ligia", "Ligia", tf_hero|tf_unmoveable_in_party_window|tf_female, no_scene, reserved, fac_commoners,
[itm_dagger,itm_caligea,itm_female_2],
str_9|agi_10|int_14|cha_14|level(1), wp(60), knows_merchant_npc|knows_riding_2|knows_persuasion_4, 0x000000003f09108307dbb3f8240c32f200000000001c79250000000000000000 ],
["npc35", "Ursus", "Ursus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_roman_gladius,itm_roman_poor3],
 str_18|agi_14|int_9|cha_9|level(1), wp(80), knows_warrior_npc|knows_riding_2|knows_power_throw_3, 0x000000003f001307471c6dc6db6dc49b00000000001db6ea0000000000000000 ],
["npc36", "Marcus Vinicius", "Marcus Vinicius", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_roman_gladius,itm_legion_squamata_cape_5],
str_17|agi_15|int_16|cha_17|level(24), wp(180), knows_veteran_npc|knows_trainer_2, 0x00000002791010045b5c6d491d78b52100000000001db8cc0000000000000000 ],
["npc37", "Josephus", "Josephus", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_dagger,itm_judean_tunic_1],
str_10|agi_10|int_12|cha_16|level(8), wp(100), knows_merchant_npc|knows_surgery_2|knows_wound_treatment_2|knows_first_aid_2, 0x00000000ef05308446e277435d3749ad00000000001eb89e0000000000000000 ],
["npc38", " Elazar Bar Yochai", " Elazar Bar Yochai", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_graves_simple_2,itm_dagger,itm_judean_tunic_3],
str_16|agi_14|int_10|cha_12|level(10), wp(125), knows_warrior_npc|knows_trade_4|knows_wound_treatment_2|knows_first_aid_2|knows_riding_5|knows_persuasion_4, 0x000000014310c00836dd6d48e497258100000000001dd7010000000000000000 ],

# daughter of hludwig
["mathildiz","Mathildiz","Mathildiz",tf_female|tf_hero,0,0,fac_commoners,
[itm_celtic_boots, itm_female_3_barb],
attrib_common_lady,wp(100),knows_common_lady,0x000000018000405a0b9b6ca6db4ab6dd00000000001c65ca0000000000000000],

#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["kingdom_1_lord", "Rex Scorilo", "Scorilo", tf_hero, no_scene, reserved, fac_kingdom_1,
[itm_ring_1,itm_dacian_noble1,itm_dacian_heavy1,itm_dacian_shield_small5,itm_dacian_heavy_helm_noble_1,itm_dacian_noble_sword,itm_celtic_boots,itm_steppe_horse_3], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_5, 0x000000057f10d30936db6db6db6db6db00000000001db6db0000000000000000 ],
["kingdom_2_lord", "Ri Calgacus", "Calgacus", tf_hero, no_scene, reserved, fac_kingdom_2,
[itm_ring_2,itm_horse_1,itm_celtic_boots,itm_celtic_heavy4,itm_celtic_light_noble_4,itm_celtic_round_shild4,itm_celtic_sowrd3,itm_britton_helm_noble_2], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_4, 0x00000008a21133c93b486c14d95403ef00000000001db6d90000000000000000 ],

["kingdom_3_lord", "Tiberius Julius Rhescuporis", "Tiberius Julius Rhescuporis", tf_hero, no_scene, reserved, fac_kingdom_3,
[itm_ring_2,itm_cataphract_horse_steppe_2,itm_eastern_shoe_r,itm_bosporan_light2,itm_scythian_shield_cav2,itm_bosphoran_scale_3,itm_bosporan_pointed_helm_4,itm_sarmatian_ringsword_3],
knight_attrib_5, wp(320), knight_skills_5|knows_trainer_5, 0x0000000d000051c144987246db6daadb00000000001d16db0000000000000000 ],

["kingdom_4_lord", "Kuningaz Berengar", "Berengar", tf_hero, no_scene, reserved, fac_kingdom_4,
[itm_ring_3,itm_germanic_noble_8,itm_germanic_helm3,itm_danish_longsword,itm_germanic_shield_large10,itm_graves_simple_2,itm_germanic_noble_tunic_1], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_5, 0x0000000c001113473e128cb2996db6db00000000001ff8200000000000000000, ],
["kingdom_5_lord", "Shah Trdat", "Trdat", tf_hero, no_scene, reserved, fac_kingdom_5,
[itm_ring_2,itm_cataphract_boots,itm_cataphract_eastern,itm_cataphract_sallet_1,itm_mail_mittens,itm_parthian_cataphract_axe,itm_lance,itm_cataphract_horse_parthian_1,itm_sarranid_cloth_robe_fancy_2,itm_eastern_shoe_r], knight_attrib_4, wp(270), knight_skills_4|knows_trainer_5,
0x0000000abf10b10f36dd2ec6d96db6cb00000000001db72b0000000000000000 ],
["kingdom_6_lord", "Shahan Shah Vologaeses Arsacid", "Vologaeses Arsacid", tf_hero, no_scene, reserved, fac_kingdom_6,
[itm_ring_1,itm_mamluke_mail,itm_mail_mittens,itm_cataphract_boots,itm_cataphract_horse_parthian_2,itm_eastern_sowrd3,itm_crown_shah,itm_sarranid_cloth_robe_fancy_2,itm_eastern_shoe_r],
knight_attrib_4, wp(270), knight_skills_5|knows_trainer_5, 0x00000006fd0042851713b2451a6e32f0000000000005b91c0000000000000000 ],
["kingdom_7_lord", "Nero Claudius", "Nero Claudius", tf_hero, no_scene, reserved, fac_kingdom_7,
[itm_ring_1,itm_calceus_3,itm_laurel_gold,itm_roman_rich_emperor,itm_roman_legatus_helm,itm_musculata_legatus_3,itm_legio_armored_caligea_2,itm_roman_gladius_rich_2,itm_leopard_horse_2,itm_officer_shield],
knight_attrib_2, wp(100), knight_skills_2, 0x00000001b90800113adb91996245299900000000001e5a6d0000000000000000 ],

["kingdom_8_lord", "Ri Egan", "Egan", tf_hero, no_scene, reserved, fac_kingdom_8,
[itm_ring_2,itm_horse_1,itm_celtic_boots,itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_round_shild4,itm_celtic_sowrd3,itm_britton_helm_noble], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_4, 0x0000000b000c23c32d748dd2522aa8eb00000000001de66a0000000000000000 ],
["kingdom_9_lord", "Ri Trahern", "Trahern", tf_hero, no_scene, reserved, fac_kingdom_9,
[itm_ring_3,itm_horse_2,itm_celtic_boots,itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_round_shild4,itm_celtic_sowrd3,itm_britton_helm_noble], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_4, 0x000000048000d05136db6db6db6db6db00000000001db6db0000000000000000 ],
["kingdom_10_lord", "Ri Venutius", "Venutius", tf_hero, no_scene, reserved, fac_kingdom_10,
[itm_ring_2,itm_horse_1,itm_celtic_boots,itm_celtic_heavy4,itm_celtic_light_noble_3,itm_celtic_round_shild4,itm_celtic_sowrd3,itm_britton_helm_noble], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_4, 0x0000000de905104371c090095b5409ff00000000001c00a00000000000000000 ],

["kingdom_11_lord", "Batesa Farzoy", "Farzoy", tf_hero, no_scene, reserved, fac_kingdom_11,
[itm_ring_2,itm_cataphract_horse_steppe_3,itm_eastern_shoe_b,itm_sarmatian_light4,itm_scythian_shield_cav3,itm_sarmatian_heavy_helm4,itm_sarmitian_scale_6,itm_sarmatian_ringsword_3], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_5, 0x000000001308634318d43248da85b85800000000000962e70000000000000000 ],
["kingdom_12_lord", "Batesa Zorsines", "Zorsines", tf_hero, no_scene, reserved, fac_kingdom_12,
[itm_ring_2,itm_cataphract_horse_steppe_1,itm_eastern_shoe_y,itm_sarmatian_light2,itm_scythian_shield_cav2,itm_sarmatian_heavy_helm5,itm_sarmitian_scale_4,itm_sarmatian_ringsword_4], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_5, 0x000000003908028e42da99a523af151c00000000001cb4e40000000000000000 ],

["kingdom_13_lord", "Kuningaz Assi", "Assi", tf_hero, no_scene, reserved, fac_kingdom_13,
[itm_ring_2,itm_germanic_noble_6,itm_germanic_helm4,itm_sword_viking_2,itm_germanic_shield_large10,itm_graves_simple_2,itm_germanic_noble_tunic_1], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_5, 0x00000001801121845913a6eb34ad949c00000000000fb6cb0000000000000000, ],
["kingdom_14_lord", "Kuningaz Ballomar", "Ballomar", tf_hero, no_scene, reserved, fac_kingdom_14,
[itm_ring_3,itm_germanic_noble_7,itm_germanic_helm_noble,itm_sword_viking_3,itm_germanic_shield_large10,itm_graves_simple_2,itm_germanic_noble_tunic_2], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_5, 0x000000018b05115148e1663aabb2dd6b000000000009b7e10000000000000000, ],
["kingdom_15_lord", "Kuningaz Lambert", "Lambert", tf_hero, no_scene, reserved, fac_kingdom_15,
[itm_ring_3,itm_germanic_noble_9,itm_germanic_helm_noble,itm_sword_viking_2,itm_germanic_shield_large10,itm_graves_simple_2,itm_germanic_noble_tunic_3], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_5, 0x00000001840c1343425c50cdd395c81f00000000001d9b620000000000000000, ],
["kingdom_16_lord", "Kuningaz Rigobert", "Rigobert", tf_hero, no_scene, reserved, fac_kingdom_16,
[itm_ring_1,itm_germanic_noble_6,itm_germanic_helm4,itm_sword_viking_3,itm_germanic_shield_large10,itm_graves_simple_2,itm_germanic_noble_tunic_4], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_5, 0x00000001841003543ca651c4d47524ea00000000001950840000000000000000, ],

["kingdom_17_lord", "Melech Hanan ben Hanan", "Hanan ben Hanan", tf_hero, no_scene, reserved, fac_kingdom_17,
[itm_ring_2,itm_judean_scale_2,itm_eastern_shoe_r,itm_arabian_horse_b,itm_eastern_sowrd5,itm_eastern_helm6,itm_eastern_shield_inf_heavy6,itm_sarranid_cloth_robe_fancy_2], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_4, 0x00000000240cb2c325296a30246add3100000000001dab2d0000000000000000 ],

["kingdom_18_lord", "Batesa Banadaspus", "Banadaspus", tf_hero, no_scene, reserved, fac_kingdom_18,
[itm_ring_2,itm_cataphract_horse_steppe_2,itm_eastern_shoe_r,itm_sarmatian_light3,itm_scythian_shield_cav1,itm_sarmatian_heavy_helm6,itm_sarmitian_scale_5,itm_sarmatian_ringsword_4], knight_attrib_5, wp(320), knight_skills_5|knows_trainer_5, 0x000000003908028e42da99a523af151c00000000001cb4e40000000000000000 ],

["kingdom_19_lord", "Gaius Julius Civilis", "Gaius Julius Civilis", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_3,itm_musculata_3,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_3],  knight_attrib_3,wp(200),knight_skills_3, 0x000000000005318d251b89d69d71d96c00000000001da8d30000000000000000, ],

["kingdom_20_lord", "Shah Mihdrat", "Mihdrat", tf_hero, no_scene, reserved, fac_kingdom_20,
[itm_sarmatian_shoes,itm_caucasian_scale_heavy_2,
itm_sarmatian_heavy_helm6,itm_mail_mittens,itm_caucasian_longsword,itm_caucasian_spear_174,itm_cataphract_horse_parthian_1,
itm_sarranid_cloth_robe_fancy_2,itm_ring_2,itm_eastern_shoe_r],
knight_attrib_5, wp(270), knight_skills_5, 0x000000000005318d251b89d69d71d96c00000000001da8d30000000000000000, ],

["kingdom_21_lord", "Shah  Oroezes", "Oroezes", tf_hero, no_scene, reserved, fac_kingdom_21,
[itm_cataphract_boots,itm_cataphract_eastern,
itm_cataphract_sallet_1,itm_mail_mittens,itm_parthian_cataphract_axe,itm_lance,itm_cataphract_horse_parthian_3,
itm_sarranid_cloth_robe_fancy_2,itm_ring_2,itm_eastern_shoe_r],
knight_attrib_4, wp(270), knight_skills_4, 0x000000000005318d251b89d69d71d96c00000000001da8d30000000000000000, ],

["kingdom_22_lord", "Basileus Aristarchus", "Aristarchus", tf_hero, no_scene, reserved, fac_kingdom_22,
[itm_sarmatian_shoes,itm_caucasian_scale_heavy_1,
itm_bosporan_pointed_helm,itm_mail_mittens,itm_caucasian_longsword,itm_caucasian_spear_174,itm_cataphract_horse_parthian_3,
itm_sarranid_cloth_robe_fancy_2,itm_ring_2,itm_eastern_shoe_r],
knight_attrib_3, wp(270), knight_skills_3, 0x000000000005318d251b89d69d71d96c00000000001da8d30000000000000000, ],

["kingdom_23_lord", "Malko Ma'nu, son of Abgar", "Ma'nu, son of Abgar", tf_hero, no_scene, reserved, fac_kingdom_23,
[itm_cataphract_boots,itm_cataphract_eastern,
itm_cataphract_sallet_1,itm_mail_mittens,itm_parthian_cataphract_axe,itm_lance,itm_cataphract_horse_parthian_2,
itm_sarranid_cloth_robe_fancy_2,itm_ring_2,itm_eastern_shoe_r],
knight_attrib_1, wp(270), knight_skills_1, 0x000000000005318d251b89d69d71d96c00000000001da8d30000000000000000, ],

["knight_1_1", "Dacian Lord", "Avizina", tf_hero, no_scene, reserved, fac_kingdom_1,
[itm_horse_1,itm_dacian_heavy1,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5, wp(230), knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000 ],
["knight_1_2", "Dacian Lord", "Bastiza", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_2,itm_dacian_heavy2,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_2,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5,wp(240),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000],
["knight_1_3", "Dacian Lord", "Charnabon", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_3,itm_dacian_heavy3,itm_dacian_shield_large4,itm_dacian_heavy_helm12,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000],
["knight_1_4", "Dacian Lord", "Dadas", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_1,itm_dacian_heavy4,itm_dacian_shield_large4,itm_dacian_heavy_helm4,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000],
["knight_1_5", "Dacian Lord", "Damanais", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_2,itm_dacian_heavy5,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_4,wp(200),knight_skills_4|knows_trainer_5, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000],
["knight_1_6", "Dacian Lord", "Dapyx", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_3,itm_dacian_heavy6,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_2,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000],
["knight_1_7", "Dacian Lord", "Moskon", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_1,itm_dacian_heavy1,itm_dacian_shield_large4,itm_dacian_heavy_helm12,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000],
["knight_1_8", "Dacian Lord", "Rhemaxos", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_2,itm_dacian_heavy2,itm_dacian_shield_large4,itm_dacian_heavy_helm4,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_4,wp(250),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000],

#Swadian younger knights
["knight_1_9", "Dacian Lord", "Roles", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_3,itm_dacian_heavy3,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_noble_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_3,wp(160),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000],
["knight_1_10", "Dacian Lord", "Rubobostes", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_1,itm_dacian_heavy4,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_2,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_3,wp(190),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000],
["knight_1_11", "Dacian Lord", "Thiadicem", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_2,itm_dacian_heavy5,itm_dacian_shield_large4,itm_dacian_heavy_helm12,itm_dacian_noble_sword,itm_celtic_boots,itm_dacian_noble1],
 knight_attrib_3,wp(220),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000],
["knight_1_12", "Dacian Lord", "Thiamarkos", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_3,itm_dacian_heavy6,itm_dacian_shield_large4,itm_dacian_heavy_helm4,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
  knight_attrib_3,wp(130),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000],
["knight_1_13", "Dacian Lord", "Tsiru", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_1,itm_dacian_heavy1,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_noble_sword,itm_celtic_boots,itm_dacian_noble1],
knight_attrib_2,wp(160),knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000],
["knight_1_14", "Dacian Lord", "Gebeleixis", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_2,itm_dacian_heavy2,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_2,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
  knight_attrib_2,wp(190),knight_skills_3|knows_trainer_5, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000],
["knight_1_15", "Dacian Lord", "Zyraxes", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_3,itm_dacian_heavy3,itm_dacian_shield_large4,itm_dacian_heavy_helm12,itm_dacian_noble_sword,itm_celtic_boots,itm_dacian_noble1],
   knight_attrib_4,wp(140),knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000],
["knight_1_16", "Dacian Lord", "Pieporus", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_2,itm_dacian_heavy4,itm_dacian_shield_large4,itm_dacian_heavy_helm4,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
 knight_attrib_1,wp(130),knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000],
["knight_1_17", "Dacian Lord", "Oroles", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_1,itm_dacian_heavy5,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_ring_sword,itm_celtic_boots,itm_dacian_noble1],
   knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000],
["knight_1_18", "Dacian Lord", "Natoporus", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_steppe_horse_3,itm_dacian_heavy6,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_2,itm_dacian_sword,itm_celtic_boots,itm_dacian_noble1],
  knight_attrib_3,wp(210),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000],
["knight_1_19", "Dacian Lord", "Cotiso", tf_hero, 0, reserved,  fac_kingdom_1,
[itm_horse_1,itm_dacian_heavy6,itm_dacian_shield_large4,itm_dacian_heavy_helm_noble_1,itm_dacian_ring_sword,itm_celtic_boots,itm_dacian_noble1],
 knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000],

["knight_2_1", "Celtic Lord", "Acco", tf_hero, no_scene, reserved, fac_kingdom_2,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1], knight_attrib_1, wp(130), knight_skills_1|knows_trainer_3, 0x0000000c7f0131c33d986c0292ada53500000000001cc1180000000000000000 ],
["knight_2_2", "Celtic Lord", "Carvilius", tf_hero, 0, reserved,  fac_kingdom_2,
[itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_2],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000aff0005ce49918b46a98e176400000000001d95a40000000000000000],
["knight_2_3", "Celtic Lord", "Bellicianus", tf_hero, 0, reserved,  fac_kingdom_2,
[itm_celtic_heavy4,itm_celtic_light_noble_3,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],     knight_attrib_3,wp(190),knight_skills_3, 0x00000007bf1131c546a388a320b4c86000000000001d48d30000000000000000],
["knight_2_4", "Celtic Lord", "Cunobelinus", tf_hero, 0, reserved,  fac_kingdom_2,
[itm_celtic_heavy4,itm_celtic_light_noble_4,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_2],    knight_attrib_4,wp(220),knight_skills_4, 0x000000003f0805c748c272540d8ab65900000000001d34e60000000000000000],
["knight_2_5", "Celtic Lord", "Venutius", tf_hero, 0, reserved,  fac_kingdom_2,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],       knight_attrib_5,wp(250),knight_skills_5, 0x00000004a201300836db6db6db4c031400000000001d46cc0000000000000000],

["knight_3_1", "Bosporan Lord", "Airawanta", tf_hero, no_scene, reserved, fac_kingdom_3,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light1,itm_bosphoran_scale_1,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],
knight_attrib_1, wp(130), knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x0000000de408118f2b1c6f5711712b1200000000001d47110000000000000000 ],

["knight_3_2", "Bosporan Lord",  "Achaios", tf_hero, 0, reserved,  fac_kingdom_3, [itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light2,itm_bosphoran_scale_2,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x000000002e0811515c64b5e71c715b6200000000001e53230000000000000000],
["knight_3_3", "Bosporan Lord",  "Demokritos", tf_hero, 0, reserved,  fac_kingdom_3, [itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light3,itm_bosphoran_scale_3,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000005112344270b2d371c652c9300000000001928ec0000000000000000],
["knight_3_4", "Bosporan Lord", "Pleistarchos", tf_hero, 0, reserved,  fac_kingdom_3,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light4,itm_bosphoran_scale_4,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],
knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x0000000a9508100e2b1c6f5711712b1200000000001c17110000000000000000],

["knight_3_5", "Bosporan Lord",  "Phylarkhos", tf_hero, 0, reserved,  fac_kingdom_3, [itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light1,itm_bosphoran_scale_1,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x00000000390412c35b2e0ce6ae292ae400000000001db7230000000000000000],
["knight_3_6", "Bosporan Lord", "Priyadeve", tf_hero, 0, reserved,  fac_kingdom_3, [itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light2,itm_bosphoran_scale_2,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x000000002304c2113f22a9a6ae3624da00000000001d570b0000000000000000],
["knight_3_7", "Bosporan Lord","Uposathe", tf_hero, 0, reserved,  fac_kingdom_3,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light3,itm_bosphoran_scale_3,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],
knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x00000000110055cf44987246db6daadb00000000001d16db0000000000000000],

["knight_3_8", "Bosporan Lord", "Philon", tf_hero, 0, reserved,  fac_kingdom_3,
[itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_bosporan_light4,itm_bosphoran_scale_4,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_scythian_shield_cav2],
knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x000000001c0c50106214c4a672b5d4d700000000001c26590000000000000000],


["knight_4_1", "Germanic Lord", "Tancram", tf_hero, no_scene, reserved, fac_kingdom_4,
[itm_celtic_boots,itm_danish_longsword,itm_germanic_shield_1,itm_germanic_noble_8,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_1], knight_attrib_1|str_30, wp(130), knight_skills_1|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000c80011300340eb0351159392d00000000001eb75a0000000000000000,  ],
["knight_4_2", "Germanic Lord", "Sunger", tf_hero, 0, reserved,  fac_kingdom_4,
[itm_celtic_boots,itm_danish_longsword,itm_germanic_shield_2,itm_germanic_noble_7,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_2],  knight_attrib_2|str_30,wp(160),knight_skills_2|knows_trainer_3|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x00000009a111130368e294c4e9a5985b00000000001db2a10000000000000000, ],
["knight_4_3", "Germanic Lord", "Marcwald", tf_hero, 0, reserved,  fac_kingdom_4,
[itm_celtic_boots,itm_danish_longsword,itm_germanic_shield_3,itm_germanic_noble_8,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_3],  knight_attrib_3|str_30,wp(190),knight_skills_3|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000783051204245a314b744b30a400000000001eb2a90000000000000000, ],
["knight_4_4", "Germanic Lord", "Hraugmund", tf_hero, 0, reserved,  fac_kingdom_4,
[itm_celtic_boots,itm_danish_longsword,itm_germanic_shield_4,itm_germanic_noble_8,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_4],  knight_attrib_4|str_30,wp(210),knight_skills_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x00000005081115ca3d6954066a8939a300000000001e399b0000000000000000, ],
["knight_4_4_1", "Germanic Lord", "Teutomer", tf_hero, 0, reserved,  fac_kingdom_4,
[itm_celtic_boots,itm_danish_longsword,itm_germanic_shield_large5,itm_germanic_noble_7,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_1],  knight_attrib_4|str_30,wp(210),knight_skills_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000b1f1021c538cd8d35124ca25100000000001e1b920000000000000000, ],


["knight_5_1", "Iberian Lord", "Abulites", tf_hero, no_scene, reserved, fac_kingdom_20,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_2], knight_attrib_1, wp(130), knight_skills_1|knows_trainer_3,
0x0000000ebf0d30913adcbaa5ac9a34a200000000001ca2d40000000000000000,  ],
["knight_5_9", "Iberian Lord", "Mithradates", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_3,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_2],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5,
0x00000004bf0535c1033149551c4724a100000000001e39a40000000000000000, ],

["knight_5_19", "Iberian Lord", "Ariabignes", tf_hero, 0, reserved,  fac_kingdom_20,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_2],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5,
0x00000004bf04d5cc092ab732d9adb44c00000000001e072c0000000000000000, ],


["knight_5_2", "Albanian Lord", "Arsites", tf_hero, 0, reserved,  fac_kingdom_21,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_1,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4,
0x0000000e390cc00e29136db45a75251300000000001f16930000000000000000, ],
["knight_5_10", "Albanian Lord", "Mithrobuzanes", tf_hero, 0, reserved,  fac_kingdom_21,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4,
0x00000004b501100416db6db6db6c92db00000000001d24e90000000000000000, ],
["knight_5_17", "Albanian Lord", "Anaphes", tf_hero, 0, reserved,  fac_kingdom_21,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_1,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_2],     knight_attrib_2,wp(150),knight_skills_2,
0x00000003ff10d01134de6eb6db6db6db00000000001ca68b0000000000000000, ],

["knight_5_3", "Kolchian Lord", "Artochmes", tf_hero, 0, reserved,  fac_kingdom_22,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_3,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_2],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, ],
["knight_5_12", "Kolchian Lord", "Orxines", tf_hero, 0, reserved,  fac_kingdom_22,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_3,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, ],
["knight_5_18", "Kolchian Lord", "Arbupales", tf_hero, 0, reserved,  fac_kingdom_22,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_3,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(180),knight_skills_3,
0x000000067f0cd103355e6fb6db4ca6db00000000001cb6e90000000000000000, ],

["knight_5_4", "Armenian Lord", "Barzanes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, ],
["knight_5_5", "Armenian Lord", "Chorienes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_1,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_2], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, ],
["knight_5_6", "Armenian Lord", "Harmamitres", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_3,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_1,wp(130),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, ],
["knight_5_7", "Armenian Lord", "Ithamitres", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_2],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, ],
["knight_5_8", "Armenian Lord", "Masistes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_1,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, ],

["knight_5_11", "Armenian Lord", "Okontobates", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_1,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_2],    knight_attrib_1,wp(130),knight_skills_1,
0x000000043f0c34c64752adb6eb3228d500000000001c955c0000000000000000, ],
["knight_5_13", "Armenian Lord", "Pharasmanes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_2],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, ],
["knight_5_14", "Armenian Lord", "Phrasaortes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_1,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, ],
["knight_5_15", "Armenian Lord", "Rhoisakes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_boots,itm_mail_mittens,itm_cataphract_eastern,itm_armenian_helm_heavy_3,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_2], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, ],
["knight_5_16", "Armenian Lord", "Sisamnes", tf_hero, 0, reserved,  fac_kingdom_5,
[itm_lance,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_boots,itm_mail_mittens,itm_sarranid_elite_armor,itm_armenian_helm_heavy_2,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, ],

["knight_6_1", "Osrhoenian Lord", "Achaimenes", tf_hero, no_scene, reserved, fac_kingdom_23, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3], knight_attrib_1, wp(130), knight_skills_1|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000,  ],
["knight_6_9", "Osrhoenian Lord", "Kophenes", tf_hero, 0, reserved,  fac_kingdom_23, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, ],
["knight_6_17", "Osrhoenian Lord", "Spitamenes", tf_hero, 0, reserved,  fac_kingdom_23, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_2,wp(150),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, ],

["knight_6_2", "Parthian Lord", "Ariobarzanes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000df809000044cb68b92b8d3b1d00000000001dd71e0000000000000000, ],
["knight_6_3", "Parthian Lord", "Artabazos", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(190),knight_skills_3, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, ],
["knight_6_4", "Parthian Lord", "Artostes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_4,wp(220),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, ],
["knight_6_5", "Parthian Lord", "Autophradates", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3], knight_attrib_5,wp(250),knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, ],
["knight_6_6", "Parthian Lord", "Belesys", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_1,wp(130),knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, ],
["knight_6_7", "Parthian Lord", "Dataphernes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_2,wp(160),knight_skills_2, 0x000000001508c24133227e37ab46da9d000000000017a7150000000000000000, ],
["knight_6_8", "Parthian Lord", "Histanes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, ],
["knight_6_10", "Parthian Lord", "Kyros", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000004bf04f1d16ce99256b4ad4b3300000000001d392c0000000000000000, ],
["knight_6_11", "Parthian Lord", "Mazaios", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, ],
["knight_6_12", "Parthian Lord", "Ordanes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, ],
["knight_6_13", "Parthian Lord", "Ochos", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(190),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, ],
["knight_6_14", "Parthian Lord", "Pherendates", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_4,wp(220),knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, ],
["knight_6_15", "Parthian Lord", "Prexaspes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3], knight_attrib_5,wp(250),knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, ],

["knight_6_16", "Parthian Lord", "Sataspes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_1,wp(120),knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, ],
["knight_6_18", "Parthian Lord", "Arses", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_parthian_cataphract_axe,itm_cataphract_horse_parthian_3,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_y,itm_sarranid_cloth_robe_fancy_3],    knight_attrib_3,wp(180),knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, ],
["knight_6_19", "Parthian Lord", "Baryaxes", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_1,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_b,itm_sarranid_cloth_robe_fancy_3],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, ],
# ["knight_6_20", "Parthian Lord", "Mardonios", tf_hero, 0, reserved,  fac_kingdom_6, [itm_cataphract_boots,itm_sarranid_mace_1,itm_cataphract_horse_parthian_2,itm_cataphract_helm6,itm_mamluke_mail,itm_mail_mittens,itm_eastern_shoe_r,itm_sarranid_cloth_robe_fancy_3],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, ],

["knight_2_6", "Celtic Lord", "Adiatuanus", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_1],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000d4100205038da7157aa4e430a00000000001da8bc0000000000000000, ],
["knight_2_7", "Celtic Lord", "Bellovesus", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_2],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c0f111046335ba9390b2d277500000000001d89300000000000000000, ],
["knight_2_8", "Celtic Lord", "Cassivellaunus", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_celtic_heavy4,itm_celtic_light_noble_3,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x0000000900043401234b8da2cdd248db00000000001d369c0000000000000000, ],
["knight_2_9", "Celtic Lord", "Diviciacus", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_celtic_heavy4,itm_celtic_light_noble_4,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_2],    knight_attrib_4,wp(230),knight_skills_4, 0x00000007160514c7136469c4d9b159ad00000000001e28f10000000000000000, ],
["knight_2_10", "Celtic Lord", "Prasutagus", tf_hero, 0, reserved,  fac_kingdom_8,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_1],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_5, 0x000000001f00200a36db6db6db6db6db00000000000db6db0000000000000000, ],

["knight_2_11", "Celtic Lord", "Adminius", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_2],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000c4008204436acd6991b74d69d00000000001e476c0000000000000000, ],
["knight_2_12", "Celtic Lord", "Boduognatus", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_1],    knight_attrib_2,wp(170),knight_skills_2, 0x000000098a0510872509d5d53944c6a300000000001d5b320000000000000000, ],
["knight_2_13", "Celtic Lord", "Cattulanus", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_celtic_heavy4,itm_celtic_light_noble_3,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_2],     knight_attrib_3,wp(190),knight_skills_3, 0x000000088904104a392230cb926d56ca00000000001da69b0000000000000000, ],
["knight_2_14", "Celtic Lord", "Divico", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_celtic_heavy4,itm_celtic_light_noble_4,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_1],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x00000005c00414cd471bd104b375b52c00000000001dd5220000000000000000, ],
["knight_2_15", "Celtic Lord", "Segovax", tf_hero, 0, reserved,  fac_kingdom_9,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_2],       knight_attrib_5,wp(250),knight_skills_5, 0x00000004a500100f3b6bb02965d6eb7400000000001dd72c0000000000000000, ],

["knight_2_16", "Celtic Lord", "Aiorix", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],   knight_attrib_1,wp(120),knight_skills_1, 0x0000000fc000100239233512e287391d00000000001db7200000000000000000, ],
["knight_2_17", "Celtic Lord", "Boiorix", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_celtic_heavy4,itm_celtic_light_noble_3,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_2],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000b400c2387374bd010ddd2a4ab00000000001e32cc0000000000000000, ],
["knight_2_18", "Celtic Lord", "Cartorites", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_celtic_heavy4,itm_celtic_light_noble_4,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],    knight_attrib_3,wp(180),knight_skills_3, 0x00000008400010423d9b6d4a92ada53500000000001cc1180000000000000000, ],
["knight_2_19", "Celtic Lord", "Drappes", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_celtic_heavy4,itm_celtic_light_noble_1,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble,itm_horse_2],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x00000005c00025c136db6db6db6db6db00000000001db6db0000000000000000, ],
["knight_2_20", "Celtic Lord", "Immanuentius", tf_hero, 0, reserved,  fac_kingdom_10,
[itm_celtic_heavy4,itm_celtic_light_noble_2,itm_celtic_boots,itm_celtic_round_shild3,itm_celtic_sowrd2,itm_britton_helm_noble_2,itm_horse_1],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x000000048000200e36db6db6db6db6db00000000000db6db0000000000000000, ],

["knight_3_9", "Siracian Lord","Ambare", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_3,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000002704c2015b1559326eaea2ac00000000001dbda20000000000000000, ],
["knight_3_10", "Siracian Lord","Kentarske", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_1,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_5|knows_power_draw_4, 0x000000001e11120736e5b9aae3564a9c00000000000a4af40000000000000000, ],
["knight_3_12", "Siracian Lord", "Uttaraphalguni", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_4,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x000000000a10b205175dbabb0cd656e2000000000012945d0000000000000000, ],
["knight_3_13", "Siracian Lord","Kercapiske", tf_hero, 0, reserved,  fac_kingdom_11,
[itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_5,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x000000001500b2cd42a350b6922e4a1400000000000e9d5a0000000000000000, ],

["knight_3_15", "Roxolanian Lord", "Amratodane", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_1,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x000000002b091591321b4d58e451497500000000001e430e0000000000000000, ],
["knight_3_16", "Roxolanian Lord","Kereptanne", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_2,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x000000000c0c53432daf6dbd264636d5000000000019646c0000000000000000, ],
["knight_3_18", "Roxolanian Lord", "Varddhane", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_cataphract_horse_steppe_1,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_4,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x000000002704d51126e391490b6a472c00000000001d28b20000000000000000, ],
["knight_3_19", "Roxolanian Lord","Anande", tf_hero, 0, reserved,  fac_kingdom_12,
[itm_cataphract_horse_steppe_2,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_5,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000005043187252beddb5b4e132b00000000001ec5140000000000000000, ],


["knight_3_11", "Iazyges Lord", "Punaiyse", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_2,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x000000002f0cd1d1405a28b2e381688a00000000001eb6f30000000000000000, ],
["knight_3_14", "Iazyges Lord",  "Punaraksite", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_6,itm_sarmatian_heavy_helm7,itm_khergit_bow_2,itm_bodkin_arrows,itm_lance],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000190d21c3290cb13a9a712ae200000000001d48a10000000000000000, ],
["knight_3_17", "Iazyges Lord", "Punyamitre", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_3,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x000000002c052107489269bb1d45290b00000000001e14ed0000000000000000, ],
["knight_3_20", "Iazyges Lord","Kimne", tf_hero, 0, reserved,  fac_kingdom_18,
[itm_cataphract_horse_steppe_3,itm_sarmatian_ringsword_rich_1,itm_celtic_boots,itm_sarmatian_light1,itm_sarmitian_scale_6,itm_sarmatian_heavy_helm7,itm_khergit_bow,itm_bodkin_arrows,itm_lance],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x00000000250412ce30f485c91baa196b00000000001db8c90000000000000000, ],


["knight_4_5", "Germanic Lord", "Ambri", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_leather_boots,itm_germanic_axe3,itm_eastern_germanic_shield_1,itm_germanic_noble_6,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_1], knight_attrib_5,wp(250),knight_skills_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, ],
["knight_4_6", "Germanic Lord", "Aktumer", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_leather_boots,itm_sword_viking_3,itm_eastern_germanic_shield_2,itm_germanic_noble_4,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_2],   knight_attrib_1,wp(130),knight_skills_1|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, ],
["knight_4_7", "Germanic Lord", "Chariovalda", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_leather_boots,itm_sword_viking_1,itm_eastern_germanic_shield_3,itm_germanic_noble_3,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_3],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, ],
["knight_4_8", "Germanic Lord", "Hariowald", tf_hero, 0, reserved,  fac_kingdom_13,
[itm_leather_boots,itm_sword_viking_2,itm_eastern_germanic_shield_2,itm_germanic_noble_1,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_4],   knight_attrib_3,wp(190),knight_skills_3|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, ],

["knight_4_9", "Germanic Lord", "Arbomund", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_leather_boots,itm_sax1,itm_germanic_shield_large10,itm_germanic_noble_1,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_1],  knight_attrib_4|str_30,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, ],
["knight_4_10", "Germanic Lord", "Baldogais", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_leather_boots,itm_sax1,itm_germanic_shield_large2,itm_germanic_noble_2,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_2],  knight_attrib_5|str_30,wp(250),knight_skills_5|knows_trainer_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, ],
["knight_4_11", "Germanic Lord", "Eidric", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_leather_boots,itm_sax1,itm_germanic_shield_large3,itm_germanic_noble_3,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_3], knight_attrib_1|str_30,wp(140),knight_skills_1|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, ],
["knight_4_12", "Germanic Lord", "Gundmar", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_leather_boots,itm_sax1,itm_germanic_shield_large4,itm_germanic_noble_4,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_4],  knight_attrib_2|str_30,wp(200),knight_skills_2|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, ],
["knight_4_12_1", "Germanic Lord", "Bauto", tf_hero, 0, reserved,  fac_kingdom_14,
[itm_leather_boots,itm_sax1,itm_germanic_shield_large6,itm_germanic_noble_6,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_1],  knight_attrib_2|str_30,wp(200),knight_skills_2|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x000000000004024b49734de5a4c6356200000000001ea6a30000000000000000, ],

["knight_4_13", "Germanic Lord", "Ingbald", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_leather_boots,itm_germanic_axe3,itm_germanic_shield_large4,itm_germanic_noble_6,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_2],  knight_attrib_3|str_30,wp(250),knight_skills_3|knows_trainer_3|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, ],
["knight_4_14", "Germanic Lord", "Eidgais", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_leather_boots,itm_sword_viking_1,itm_germanic_shield_large7,itm_germanic_noble_7,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_3],  knight_attrib_4|str_30,wp(200),knight_skills_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, ],
["knight_4_15", "Germanic Lord", "Geric", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_leather_boots,itm_sword_viking_2,itm_germanic_shield_large8,itm_germanic_noble_8,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_4], knight_attrib_5|str_30,wp(290),knight_skills_5|knows_trainer_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, ],
["knight_4_16", "Germanic Lord", "Siglaik", tf_hero, 0, reserved,  fac_kingdom_15,
[itm_leather_boots,itm_sword_viking_3,itm_germanic_shield_large5,itm_germanic_noble_9,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_1],   knight_attrib_1|str_30,wp(120),knight_skills_1|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x000000099700124239233512e287391d00000000001db7200000000000000000, ],

["knight_4_17", "Germanic Lord", "Sigric", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_leather_boots,itm_sword_viking_3,itm_germanic_shield_1,itm_germanic_noble_6,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_2],   knight_attrib_2|str_30,wp(150),knight_skills_2|knows_trainer_4|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, ],
["knight_4_18", "Germanic Lord", "Tramric", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_leather_boots,itm_sword_viking_2,itm_germanic_shield_2,itm_germanic_noble_7,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_3],   knight_attrib_3|str_30,wp(180),knight_skills_3|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, ],
["knight_4_19", "Germanic Lord", "Waldmund", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_leather_boots,itm_sword_viking_1,itm_germanic_shield_3,itm_germanic_noble_8,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_4],  knight_attrib_4|str_30,wp(210),knight_skills_4|knows_trainer_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, ],
["knight_4_20", "Germanic Lord", "Walrauc", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_leather_boots,itm_germanic_axe3,itm_germanic_shield_4,itm_germanic_noble_9,itm_germanic_helm_noble,itm_jarid,itm_germanic_noble_tunic_1],  knight_attrib_5|str_30,wp(240),knight_skills_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, ],
["knight_4_21", "Germanic Lord", "Eidgast", tf_hero, 0, reserved,  fac_kingdom_16,
[itm_leather_boots,itm_germanic_axe3,itm_germanic_shield_large12,itm_germanic_noble_6,itm_germanic_helm4,itm_jarid,itm_germanic_noble_tunic_2],  knight_attrib_5|str_30,wp(240),knight_skills_5|knows_power_strike_10|knows_power_throw_10|knows_trainer_5, 0x0000000005012243245d6ae5236e35d200000000001e28cd0000000000000000, ],
##jews
["knight_17_1", "Judean Lord", "Joshua ben Gamla", tf_hero, no_scene, reserved, fac_kingdom_17,
[itm_judean_scale_1,itm_legio_armored_caligea,itm_arabian_horse_b,itm_roman_spatha,itm_eastern_helm5,itm_old_round_shield_3,itm_sarranid_cloth_robe_fancy_3,itm_eastern_shoe_b], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_4, 0x000000003108b2854954aca89135a96600000000000e12eb0000000000000000,  ],
["knight_17_2", "Judean Lord", "Eleazar ben Hanania", tf_hero, no_scene, reserved, fac_kingdom_17,
[itm_judean_scale_2,itm_legio_armored_caligea,itm_arabian_horse_b,itm_roman_spatha_2,itm_eastern_helm5,itm_old_round_shield_4,itm_sarranid_cloth_robe_fancy_3,itm_eastern_shoe_r], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_4, 0x000000001d10c20d16ee77529375369500000000001eb68e0000000000000000,  ],
["knight_17_3", "Judean Lord", "Simon bar Giora", tf_hero, no_scene, reserved, fac_kingdom_17,
[itm_judean_mail_6,itm_legio_armored_caligea,itm_arabian_horse_b,itm_roman_spatha_3,itm_eastern_helm5,itm_old_round_shield_5,itm_sarranid_cloth_robe_fancy_3,itm_eastern_shoe_y], knight_attrib_5, wp(420), knight_skills_5|knows_trainer_4, 0x000000002008d20e1d32a8f95a6adacb00000000001f48dd0000000000000000,  ],

["knight_19_1", "Batava Lord", "Brinno", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_cav_decurio_helm,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_10,itm_legio_armored_caligea,itm_officer_shield_3,itm_calceus_3,itm_roman_toga],  knight_attrib_5,wp(300),knight_skills_5, 0x000000000001640a5a4a61531a55ba9d00000000001eb1b50000000000000000, ],
["knight_19_2", "Batava Lord", "Julius Tutor", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_2,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_5,wp(300),knight_skills_5, 0x000000000701724b329571b71b6da72a00000000001e33630000000000000000, ],
["knight_19_3", "Batava Lord", "Julius Classicus", tf_hero, 0, reserved,  fac_kingdom_19,
[itm_cav_decurio_helm_3,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield_3,itm_calceus_3,itm_roman_toga],  knight_attrib_5,wp(300),knight_skills_5, 0x000000000a0193cd329571b71b6da72a00000000001e33630000000000000000, ],

###legatus legionis
["legatus_1", "Legatus Lucius Calpurnius Licinianus", "	Lucius Calpurnius Licinianus", tf_hero, no_scene, reserved, fac_kingdom_7,
[itm_legatus_legionis_helm_2,itm_roman_spatha_rich,itm_horse_1,itm_musculata_legatus_1,itm_centurio_west_graves,itm_officer_shield,itm_calceus_3,itm_roman_rich1], knight_attrib_5, wp(240), knight_skills_5, 0x000000003301300862127002a231b8db00000000001cd2810000000000000000,  ],
["legatus_2", "Legatus Q. Sulpicius Camerinus", "Q. Sulpicius Camerinus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_3,itm_roman_spatha_rich_2,itm_horse_2,itm_musculata_legatus_2,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_calceus_2,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000002801200c629197eae94db36100000000001ed4150000000000000000, ],
["legatus_3", "Legatus Aulus Germanicus Vitellius", "Aulus Germanicus Vitellius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_4,itm_roman_spatha_rich_3,itm_horse_3,itm_musculata_legatus_3,itm_centurio_west_graves,itm_officer_shield_3,itm_calceus_4,itm_roman_rich3],  knight_attrib_5,wp(240),knight_skills_5, 0x00000002700130076ed8959ad9b02d9b00000000001c26490000000000000000, ],
["legatus_4", "Legatus Aulus Alienus Caecina", "Aulus Alienus Caecina", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_rich_2,itm_parthian_horse_a,itm_musculata_legatus_4,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_rich1],  knight_attrib_2,wp(180),knight_skills_2, 0x000000003f011003555594286b5018da00000000001ca8890000000000000000, ],
["legatus_5", "Legatus Mamercus Cornelius", "Mamercus Cornelius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_2,itm_roman_spatha_rich,itm_parthian_horse_b,itm_musculata_legatus_5,itm_centurio_west_graves,itm_officer_shield_2,itm_calceus_2,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000015f10300e596191b6db6db6db00000000001d234a0000000000000000, ],
["legatus_6", "Legatus Servius Cornelius", "Servius Cornelius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_3,itm_roman_spatha_rich_2,itm_parthian_horse_c,itm_musculata_legatus_6,itm_legio_armored_caligea_2,itm_officer_shield_3,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000017d08d0054b632cb49d70c4ab00000000001ec39b0000000000000000, ],
["legatus_7", "Legatus Sextus Fabius", "Sextus Fabius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_4,itm_roman_spatha_rich_3,itm_arabian_horse_a,itm_musculata_legatus_7,itm_centurio_west_graves,itm_officer_shield,itm_calceus_4,itm_roman_rich1],  knight_attrib_5,wp(240),knight_skills_5, 0x00000000030000042914c92ad9c64af400000000001d42d30000000000000000, ],
["legatus_8", "Legatus P. Fabius Pio", "P. Fabius Pio", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_rich,itm_arabian_horse_b,itm_musculata_legatus_8,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000001610c003271a2e2365312b1e00000000001db8e20000000000000000, ],
["legatus_9", "Legatus Salvius Otho Titianus", "Salvius Otho Titianus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_2,itm_roman_spatha_rich_2,itm_horse_1,itm_musculata_legatus_9,itm_centurio_west_graves,itm_officer_shield_3,itm_calceus_2,itm_roman_rich3],  knight_attrib_3,wp(200),knight_skills_3, 0x000000047f1120043b5a6e2a217a464a00000000001cb98c0000000000000000, ],
["legatus_10", "Legatus Caesennius Paetus", "Caesennius Paetus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_3,itm_roman_spatha_rich_3,itm_horse_2,itm_musculata_legatus_10,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_rich1],  knight_attrib_4,wp(220),knight_skills_4, 0x000000001a0c10022a9c8d5d3bd5b75300000000001cdae30000000000000000, ],
["legatus_11", "Legatus T. Flavius Vespasianus", "T. Flavius Vespasianus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_4,itm_roman_spatha_rich_2,itm_leopard_horse_2,itm_musculata_legatus_1,itm_centurio_west_graves,itm_officer_shield_2,itm_calceus_4,itm_roman_rich2],  knight_attrib_5,wp(240),knight_skills_5, 0x00000000040010044d0392231b48e89300000000001e455c0000000000000000, ],
["legatus_12", "Legatus Kaeso Flavius", "Kaeso Flavius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_3,itm_roman_spatha_rich,itm_leopard_horse_2,itm_musculata_legatus_2,itm_centurio_praetorian_graves,itm_officer_shield_3,itm_calceus_3,itm_roman_rich3],  knight_attrib_5,wp(240),knight_skills_5, 0x0000000031042009271a894d1c4e9ad200000000000837640000000000000000, ],

["aux_commander_1", "Kaeso Sentius", "Kaeso Sentius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha_rich,itm_parthian_horse_a,itm_musculata_legatus_3,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000001300108f46dc5650d275a4e200000000001165240000000000000000, ],
["aux_commander_2", "Marcus Pontius", "Marcus Pontius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha_rich_2,itm_parthian_horse_b,itm_musculata_legatus_4,itm_legio_armored_caligea_2,itm_officer_shield,itm_caligea,itm_roman_toga_2],  knight_attrib_5,wp(240),knight_skills_5, 0x00000000371065d1170c984514d1acb400000000001e2d230000000000000000, ],
["aux_commander_3", "Tertius Paccius", "Tertius Paccius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_3,itm_roman_spatha_rich_3,itm_parthian_horse_c,itm_musculata_legatus_5,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_3],  knight_attrib_1,wp(180),knight_skills_1, 0x000000003204c58334e49638e2d2d93100000000000b27670000000000000000, ],
#related to poppaea: half brother
["aux_commander_12", "Cornelius Scipio Asiaticus", "Cornelius Scipio Asiaticus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_3,itm_roman_spatha_rich_2,itm_parthian_horse_c,itm_musculata_legatus_6,itm_legio_armored_caligea_2,itm_officer_shield,itm_caligea,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x0000000b400110013d9c54d85b6db6db00000000001ea6db0000000000000000, ],

["statthalter_1", "Preator Lucius Sulpicius", "Lucius Sulpicius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_rich,itm_horse_1,itm_musculata_legatus_7,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_2,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x00000000290125c84d528eca6a2c93db00000000001d626a0000000000000000, ],
["statthalter_2", "Preator Servius Sulpicius", "Servius Sulpicius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_rich_2,itm_horse_2,itm_musculata_legatus_8,itm_graves_simple_2,itm_officer_shield,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000d00d010118806e21d42e24c00000000001d23210000000000000000, ],
["statthalter_3", "Preator Lucius Vitellius", "Lucius Vitellius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha_rich_3,itm_horse_3,itm_musculata_legatus_9,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_4,itm_roman_rich2],  knight_attrib_5,wp(240),knight_skills_5, 0x00000008f40134c950948ed8e820096200000000001f4a010000000000000000, ],
["statthalter_4", "Preator Aulus Petronianus Vitellius", "Aulus Petronianus Vitellius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_rich,itm_horse_1,itm_musculata_legatus_10,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000025b0130046ed89596d9a02d9b00000000001c06710000000000000000, ],
["statthalter_5", "Preator Primus Cornelius", "Primus Cornelius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha_rich_2,itm_horse_2,itm_musculata_legatus_2,itm_graves_simple_2,itm_officer_shield,itm_calceus_2,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000039f1055c45b625a852cac9b2d00000000001f47120000000000000000, ],
["statthalter_6", "Preator Secundus Cornelius", "Secundus Cornelius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_rich_3,itm_horse_3,itm_musculata_legatus_1,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_3,itm_roman_rich2],  knight_attrib_2,wp(180),knight_skills_2, 0x000000015f10300d5b21961b34a8455b00000000001e96aa0000000000000000, ],
["statthalter_7", "Preator Manius Fabius", "Manius Fabius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha_rich,itm_horse_2,itm_musculata_legatus_3,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_4,itm_roman_rich3],  knight_attrib_1,wp(180),knight_skills_1, 0x0000000007103002492a2a398851a6da00000000001e38e40000000000000000, ],
["statthalter_8", "Preator Titus Fabius", "Titus Fabius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_rich_2,itm_horse_1,itm_musculata_legatus_4,itm_graves_simple_2,itm_officer_shield,itm_calceus_3,itm_roman_rich2],  knight_attrib_2,wp(180),knight_skills_2, 0x000000001e04c009370b7a152548d57c00000000001e22f30000000000000000, ],
["statthalter_9", "Preator Marcus Salvius Otho", "Marcus Salvius Otho", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_rich_3,itm_leopard_horse_2,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield,itm_caligea,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000003a0d1002475c6ca6db6dd4db00000000001da6d20000000000000000, ],
["statthalter_10", "Preator Gnaeus Salvius Otho", "Gnaeus Salvius Otho", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha_rich,itm_horse_1,itm_musculata_legatus_6,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_calceus_2,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000001f01100838a3acc2f26a5ee400000000001d59620000000000000000, ],
["statthalter_11", "Preator Flavius Sabinus minor", "Flavius Sabinus minor", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_7,itm_graves_simple_2,itm_officer_shield,itm_calceus_3,itm_roman_rich2],  knight_attrib_5,wp(240),knight_skills_5, 0x000000003410001147128de71b8596ce00000000001e49360000000000000000, ],
["statthalter_11_1", "Preator Abronius Hostius", "Abronius Hostius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_8,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_4,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x00000000140c435136db6db6db6db6db00000000000db6db0000000000000000, ],
["statthalter_11_2", "Preator Caerellius Falminius", "Caerellius Falminius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_9,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000003a0c35835a356ec6dc8a570600000000001dc8a20000000000000000, ],
["statthalter_11_3", "Preator Laenius Matius", "Laenius Matius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_2,itm_horse_1,itm_musculata_legatus_10,itm_graves_simple_2,itm_officer_shield,itm_caligea,itm_roman_rich2],  knight_attrib_2,wp(180),knight_skills_2, 0x0000000020112004692132c5236ddbb500000000001e24e40000000000000000, ],
["statthalter_12", "Preator Hostus Flavius", "Hostus Flavius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_1,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_2,itm_roman_rich2],  knight_attrib_1,wp(180),knight_skills_1, 0x000000003304300e52ea9119210d3b2500000000001da2a30000000000000000, ],
["senator_1", "Proconsul Ocella Sulpicius Galba", "Ocella Sulpicius Galba", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_2,itm_leopard_horse_2,itm_musculata_legatus_2,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_rich3],  knight_attrib_2,wp(180),knight_skills_2, 0x0000000eb101200953c992fca30c975100000000001d2b2a0000000000000000, ],
["senator_2", "Consul Aulus Vitellius", "Aulus Vitellius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_3,itm_graves_simple_2,itm_officer_shield,itm_calceus_4,itm_roman_rich_vitellius],  knight_attrib_3,wp(200),knight_skills_3, 0x0000000af601300927701af12c2c0fac00000000001feb1a0000000000000000, ],
["senator_3", "Proconsul P. Cornelius Scipio", "P. Cornelius Scipio", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_4,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x0000000af110500954a25a852cac9b2d00000000001ea7220000000000000000, ],
["senator_4", "Consul Primus Fabius", "Primus Fabius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_3,itm_horse_2,itm_musculata_legatus_5,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_calceus_2,itm_roman_rich3],  knight_attrib_5,wp(240),knight_skills_5, 0x000000000308d003085a0e45a33b6adc00000000001e574d0000000000000000, ],
["senator_5", "Proconsul Lucius Salvius Otho", "Lucius Salvius Otho", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_3,itm_horse_1,itm_musculata_legatus_6,itm_graves_simple_2,itm_officer_shield,itm_calceus_3,itm_roman_rich2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000047f1120043b5a6e2a217a464a00000000001cb98c0000000000000000, ],
["senator_6", "Proconsul T. Flavius Sabinus", "T. Flavius Sabinus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha_2,itm_horse_1,itm_musculata_legatus_7,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_4,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x0000000dce051009691150a72485072b00000000001dad110000000000000000, ],
["senator_7", "Proconsul Marcus maior Flavius", "Marcus maior Flavius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_3,itm_horse_2,itm_musculata_legatus_8,itm_legio_armored_caligea_2,itm_officer_shield,itm_calceus_3,itm_roman_toga_2],  knight_attrib_2,wp(180),knight_skills_3, 0x0000000747001009299495eaeb75d51400000000001da7930000000000000000, ],

#other commanders
["aux_commander_4", "Quartus Mallius", "Quartus Mallius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_1,itm_musculata_1,itm_legio_armored_caligea_2,itm_officer_shield,itm_caligea,itm_roman_toga],  knight_attrib_2,wp(180),knight_skills_2, 0x0000000020012584536d7cc56288e6ab00000000001233e30000000000000000, ],
["aux_commander_5", "Decimus Lucilius", "Decimus Lucilius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha_3,itm_horse_2,itm_musculata_2,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_2],  knight_attrib_3,wp(200),knight_skills_3, 0x000000003d0852ce57a44d4d1c4c511100000000001634d60000000000000000, ],
["aux_commander_6", "Spurius Gabinius", "Spurius Gabinius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha,itm_horse_3,itm_musculata_3,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_caligea,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000001a0815d16641b5cd626533a300000000000b28610000000000000000, ],
["aux_commander_7", "Gallus Duilius", "Gallus Duilius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_1,itm_musculata_1,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga],  knight_attrib_5,wp(240),knight_skills_5, 0x000000003b0531c35caac9331a9138b200000000000aa4d30000000000000000, ],
["aux_commander_8", "Quintus Fabricius", "Quintus Fabricius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha,itm_horse_2,itm_musculata_2,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_caligea,itm_roman_toga_2],  knight_attrib_2,wp(180),knight_skills_2, 0x000000001e0d34054ad999b664326aee00000000000e294c0000000000000000, ],
["aux_commander_9", "Secundus Ateius", "Secundus Ateius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_3,itm_musculata_3,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_3],  knight_attrib_3,wp(200),knight_skills_3, 0x0000000001091307359a89c9a176b2d6000000000015b4a50000000000000000, ],
["aux_commander_10", "Primus Asinius", "Primus Asinius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha,itm_parthian_horse_a,itm_musculata_1,itm_legio_armored_caligea_2,itm_officer_shield,itm_caligea,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x00000000170c6485550b7532d48ce71b00000000001322e40000000000000000, ],
["aux_commander_11", "Marcus Secundus Dulius", "Marcus Secundus Dulius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_parthian_horse_b,itm_musculata_2,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_2],  knight_attrib_5,wp(240),knight_skills_5, 0x000000000f10214c28b3ca5adaa1a40a000000000004b25c0000000000000000, ],
["aux_commander_13", "Vetus Africanus", "Vetus Africanus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha_3,itm_parthian_horse_a,itm_musculata_3,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga],  knight_attrib_3,wp(200),knight_skills_3, 0x000000002104c586489b96d6eb6ae51900000000000f68a10000000000000000, ],
["aux_commander_14", "Lucius Rimolus", "Lucius Rimolus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_arabian_horse_a,itm_musculata_1,itm_legio_armored_caligea_2,itm_officer_shield_2,itm_caligea,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000911314926e586d891914b1a00000000001da76c0000000000000000, ],
["aux_commander_15", "Sextus L. Totul", "Sextus L. Totul", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_3,itm_roman_spatha,itm_arabian_horse_b,itm_musculata_2,itm_centurio_east_graves,itm_officer_shield,itm_caligea,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x00000000340cb591099371389d76b2a300000000001f44d30000000000000000, ],

["statthalter_new_1", "Marcus Cocceius Nerva", "Marcus Cocceius Nerva", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_1,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_2,itm_roman_toga_3],  knight_attrib_3,wp(200),knight_skills_3, 0x000000003f00300b49dc556b222db6ec00000000001e37240000000000000000, ],
["statthalter_new_2", "L. Verginius Rufus", "L. Verginius Rufus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_2,itm_legio_armored_caligea,itm_officer_shield_2,itm_caligea,itm_roman_toga_2],  knight_attrib_5,wp(240),knight_skills_5, 0x000000000909114e5f1176b2f261676d00000000001e3ae30000000000000000, ],
["statthalter_new_3", "L. Asinius Verrucosus", "L. Asinius Verrucosus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_3,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_4", "Q. Petillius Cerialis", "Q. Petillius Cerialis", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_3,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_4,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_5", "Caesius Nasica", "Caesius Nasica", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_6", "G. Suetonius Paulinus", "G. Suetonius Paulinus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha_3,itm_horse_1,itm_musculata_legatus_6,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_7", "G. Alpinus Classicianus", "G. Alpinus Classicianus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_7,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_8", "P. Petronius Turpilianus", "P. Petronius Turpilianus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_8,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_9", "Aulus Marius Celsus", "Aulus Marius Celsus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_9,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_10", "Aulus Ducenius Geminus", "Aulus Ducenius Geminus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_10,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["statthalter_new_11", "Fonteius Capito", "Fonteius Capito", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_1,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],

["aux_commander_new_1", "Marcus Ambivulus", "Marcus Ambivulus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_2,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_2", "Baebius Massa", "Baebius Massa", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_2,itm_horse_2,itm_musculata_legatus_3,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_3", "Caius Largennius", "Caius Largennius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_4,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_4", "Calpurnius Fabatus", "Calpurnius Fabatus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_5", "G. Caristanius Fronto", "G. Caristanius Fronto", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_6,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_6", "Cassius Chaerea", "Cassius Chaerea", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_3,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_7,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_7", "Claudius Labeo", "Claudius Labeo", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_8,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_8", "Lucius Clodius Macer", "Lucius Clodius Macer", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_9,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_9", "Gnaeus Pinarius", "Gnaeus Pinarius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_10,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_10", "Bantius Caelius", "Bantius Caelius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_1,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_11", "Canutius Didius", "Canutius Didius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_3,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_2,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_12", "Durmius Hirrius", "Durmius Hirrius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_2,itm_roman_spatha_2,itm_horse_3,itm_musculata_legatus_3,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_13", "Falcidius Marius", "Falcidius Marius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm,itm_roman_spatha,itm_horse_1,itm_musculata_legatus_4,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_14", "Fufius Ranius", "Fufius Ranius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm,itm_roman_spatha,itm_horse_2,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_15", "Iunius Talius", "Iunius Talius", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_cav_decurio_helm_2,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_6,itm_legio_armored_caligea,itm_officer_shield_2,itm_calceus_3,itm_roman_toga_2],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_16", "Nymphidius Sabinus", "Nymphidius Sabinus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_5,itm_roman_spatha_rich_2,itm_horse_2,itm_musculata_legatus_5,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_3,itm_roman_toga_3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_17", "Cornelius Laco", "Cornelius Laco", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_roman_legatus_helm_4,itm_roman_spatha_rich_2,itm_horse_1,itm_musculata_legatus_4,itm_legio_armored_caligea,itm_officer_shield,itm_calceus_3,itm_roman_rich3],  knight_attrib_4,wp(220),knight_skills_4, 0x000000000a0114c45b6ead5d3d9a449200000000001a52da0000000000000000, ],
["aux_commander_new_18", "Titus Vespasianus", "Titus Vespasianus", tf_hero, 0, reserved,  fac_kingdom_7,
[itm_legatus_legionis_helm_3,itm_roman_spatha_rich_3,itm_leopard_horse_1,itm_musculata_legatus_10,itm_centurio_west_graves,itm_officer_shield_3,itm_calceus_2,itm_roman_rich2],  knight_attrib_4,wp(300),knight_skills_4, 0x00000009bf01100918a31eebfc8c0fa000000000001fa9180000000000000000, ],
#Royal family members
["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [],     attrib_common_lady,wp(50),knows_common_lady,0x000000055910204107632d675a92b92d00000000001e45620000000000000000],

#Swadian ladies - eight mothers, eight daughters, four sisters
["kingdom_1_lady_1","Dacian Lady","Duccidava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [ itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000055910204107632d675a92b92d00000000001e45620000000000000000],
["kingdom_1_lady_2","Dacian Lady","Rescuturme",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000054f08104232636aa90d6e194b00000000001e43130000000000000000],
["kingdom_1_lady_3","Dacian Lady","Zina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000018f0410464854c742db74b52200000000001d448b0000000000000000],
["kingdom_1_lady_4","Dacian Lady","Petriturme",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000000204204629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_l_lady_5","Dacian Lady","Zinai",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_6","Dacian Lady","Oriza",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000000d0820411693b142ca6a271a00000000001db6920000000000000000],
["kingdom_1_lady_7","Dacian Lady","Roibana",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_8","Dacian Ladyl","Zindurme",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000001900004542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_1_lady_9","Dacian Lady","Raina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_10","Dacian Lady","Sanziana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000003a00204646a129464baaa6db00000000001de7a00000000000000000],
["kingdom_1_lady_11","Dacian Lady","Claria",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_12","Dacian Lady","Eccana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000003f04104148d245d6526d456b00000000001e3b350000000000000000],
["kingdom_l_lady_13","Dacian Lady","Rescuturme Durasa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_14","Dacian Lady","Zina Komoza",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000003a0c3043358a56d51c8e399400000000000944dc0000000000000000],
["kingdom_1_lady_15","Dacian Lady","Boadila Zinnica",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_16","Dacian Lady","Duccidava Tiata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000003b080043531e8932e432bb5a000000000008db6a0000000000000000],
["kingdom_1_lady_17","Dacian Lady","Petriturme Rholica",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x00000000000c004446e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_1_lady_18","Dacian Lady","Piepora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x0000000000083046465800000901161200000000001e38cc0000000000000000],
["kingdom_1_lady_19","Dacian Lady","Moskosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1],
["kingdom_1_lady_20","Dacian Lady","Tiata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_2],

#Vaegir ladies
["kingdom_2_lady_1","Celtic Lady","Aife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x0000000ca611405a588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_2","Celtic Lady","Cingetessa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x0000000a000c204401f80e36b4259b9300000000001c01c70000000000000000],
["kingdom_2_lady_3","Celtic Lady","Vassura",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000007bf08204b782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_4","Celtic Lady","Allauna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000005d108205b38db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_5","Celtic Lady","Rhiannon",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000001c11620a588caf17142ab93d00000000001ddfa40000000000000000],


["kingdom_3_lady_1","Bosporan Lady","Ampratasene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_eastern_shoe],
attrib_common_lady,wp(50),knows_common_lady, 0x0000000b110c021336eea720567644b200000000001d3b590000000000000000],

["kingdom_3_lady_2","Bosporan Lady","Gepaepyris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [   itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000002c0850462ce4d246b38e632e00000000001d52910000000000000000],

["kingdom_3_lady_3","Bosporan Lady","Arjuna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady, khergit_woman_face_2],

["kingdom_3_lady_4","Bosporan Lady","Demetria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [itm_celtic_boots],
attrib_common_lady,wp(50),knows_common_lady,0x00000000100c004536e9a720567644b200000000001d3b590000000000000000],

["kingdom_3_lady_5","Bosporan Lady","Eurydike",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [   itm_eastern_shoe],     attrib_common_lady,wp(50),knows_common_lady,0x0000000c2e086042471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_6","Bosporan Lady","Apollonia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [    itm_celtic_boots],     attrib_common_lady,wp(50),knows_common_lady,0x000000002e086002471c91c8aa2a130b00000000001d48a40000000000000000],

["kingdom_3_lady_7","Bosporan Lady","Julia Nephoris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [        itm_eastern_shoe],
attrib_common_lady,wp(50),knows_common_lady,0x000000097f0c514e38636d3ee92a6b2200000000001ec7e40000000000000000],

["kingdom_3_lady_8","Bosporan Lady","Sudarsane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_celtic_boots],
attrib_common_lady,wp(50),knows_common_lady,0x000000003f0c509a38636d3ee92a6b2200000000001cd5e40000000000000000],


["kingdom_4_lady_1","Germanic Lady","Eidburg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [itm_eastern_shoe_r],     attrib_common_lady,wp(50),knows_common_lady,0x0000000c0b10020a274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_2","Germanic Lady","Actihild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [itm_eastern_shoe_b],     attrib_common_lady,wp(50),knows_common_lady,0x0000000a6310004564d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_3","Germanic Lady","Gundhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,[itm_eastern_shoe_r], attrib_common_lady,wp(50),knows_common_lady,0x00000007c00c021669a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_4","Germanic Lady","Sigihild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [itm_eastern_shoe_b], attrib_common_lady,wp(50),knows_common_lady,0x000000050000005d1564d196e2aa279400000000001dc4ed0000000000000000],

["kingdom_5_lady_1","Iberian Lady","Amastris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [itm_eastern_shoe_y],     attrib_common_lady,wp(50),knows_common_lady,
0x0000000a3f0020d616ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_9","Iberian Lady","Artazostre",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [        itm_eastern_shoe_b],     attrib_common_lady,wp(50),knows_common_lady,
0x00000005ff00204b16ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_18","Armenian Lady","Surena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [itm_eastern_shoe_y],     attrib_common_lady,wp(50),knows_common_lady,
0x000000067008a21322d432cf6d4a2ae300000000001d37a10000000000000000],

["kingdom_5_lady_2","Albanian Lady","Barsine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [itm_eastern_shoe_r],     attrib_common_lady,wp(50),knows_common_lady,
0x0000000b830891d422d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_lady_10","Albanian Lady","Parmys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [        itm_eastern_shoe_y],     attrib_common_lady,wp(50),knows_common_lady,
0x00000005a409305b22d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_lady_19","Armenian Lady","Artashidala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [    itm_eastern_shoe_r], attrib_common_lady,wp(50),knows_common_lady,
0x00000003f900a0ca364dd8aa5475d76400000000001db8d30000000000000000],

["kingdom_5_lady_3","Kolchian Lady","Rinu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22,  [itm_eastern_shoe_b], attrib_common_lady,wp(50),knows_common_lady,
0x00000009bf002116364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_12","Armenian Lady","Sisygambis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [    itm_eastern_shoe_b], attrib_common_lady,wp(50),knows_common_lady,0x00000005bf00305a4123dae69e8e48e200000000001e08db0000000000000000],

["kingdom_5_lady_4","Armenian Lady","Arystone",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [itm_eastern_shoe_y], attrib_common_lady,wp(50),knows_common_lady,0x000000057a0000414123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_lady_5","Armenian Lady","Amytis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_eastern_shoe_r],     attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1],
["kingdom_5_lady_6","Armenian Lady","Damaspia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [     itm_eastern_shoe_b],     attrib_common_lady,wp(50),knows_common_lady,0x0000000d7f0402035913aa236b4d975a00000000001eb69c0000000000000000],
["kingdom_5_lady_7","Armenian Lady","Vashti",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [      itm_eastern_shoe_y], attrib_common_lady,wp(50),knows_common_lady,0x0000000cf9002052364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_8","Armenian Lady","Rhoxane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [      itm_eastern_shoe_r], attrib_common_lady,wp(50),knows_common_lady,0x0000000b0a00020a4123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_lady_11","Kolchian Lady","Artakama",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22,  [   itm_eastern_shoe_r], attrib_common_lady,wp(50),knows_common_lady,
0x00000005ff002051364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_13","Armenian Lady","Artystone",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [        itm_eastern_shoe_y],     attrib_common_lady,wp(50),knows_common_lady,0x00000005ff00305816ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_14","Armenian Lady","Parysatis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [        itm_eastern_shoe_r],     attrib_common_lady,wp(50),knows_common_lady,0x000000043009629722d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_lady_15","Armenian Lady","Artanis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [    itm_eastern_shoe_b], attrib_common_lady,wp(50),knows_common_lady,0x0000000640010052364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_16","Armenian Lady","Atossa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [    itm_eastern_shoe_y], attrib_common_lady,wp(50),knows_common_lady,0x000000067a00305c4123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_lady_17","Armenian Lady","Phaedymia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_eastern_shoe_r],     attrib_common_lady,wp(50),knows_common_lady,
0x00000003e900324d16ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_20","Armenian Lady","Menida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [    itm_eastern_shoe_y], attrib_common_lady,wp(50),knows_common_lady,0x00000004af00d2144123dae69e8e48e200000000001e08db0000000000000000],

#Sarranid ladies
["kingdom_6_lady_1","Osrhoenian Lady","Stateira",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady,0x000000055910204107632d675a92b92d00000000001e45620000000000000000],
["kingdom_6_lady_9","Osrhoenian Lady","Ifar Mihranid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,
[itm_eastern_shoe_y],    attrib_common_lady,wp(50),knows_common_lady, 0x00000004bf0030dc154bae396351c51a00000000001c92890000000000000000],

["kingdom_6_lady_2","Parthian Lady","Vashti Arkhid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady,0x0000000e3f0841cc32636aa90d6e194b00000000001e43130000000000000000],
["kingdom_6_lady_3","Parthian Lady","Theoxene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_y],attrib_common_lady,wp(50),knows_common_lady,0x000000018f0410464854c742db74b52200000000001d448b0000000000000000],
["kingdom_6_lady_4","Parthian Lady","Orypetis Pacorid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe],attrib_common_lady,wp(50),knows_common_lady,0x000000000204204629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_6_lady_5","Parthian Lady","Mandane Savacid",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_6","Parthian Lady","Vardanidala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_y],    attrib_common_lady,wp(50),knows_common_lady,0x000000000d0820411693b142ca6a271a00000000001db6920000000000000000],
["kingdom_6_lady_7","Parthian Lady","Karinidisa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_8","Parthian Lady","Gobryasidisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady,0x000000001900004542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_6_lady_10","Parthian Lady","Chosroidaya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady,0x000000043a0041d646a129464baaa6db00000000001c67a00000000000000000],
["kingdom_6_lady_11","Parthian Lady","Dula Bagabignid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady, 0x00000005800030dc000000000000000000000000001c00000000000000000000],
["kingdom_6_lady_12","Parthian Lady","Rhoxane Cambysid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_y],    attrib_common_lady,wp(50),knows_common_lady,0x000000067f058213000000000000000000000000001c00000000000000000000],
["kingdom_6_lady_13","Parthian Lady","Sisygambis Smerdid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady, 0x00000006a100b28d154bae396351c51a00000000001c92890000000000000000],
["kingdom_6_lady_14","Parthian Lady","Zandina Suren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady,0x000000053a0c3050358a5ff53c8e399400000000001d44dc0000000000000000],
["kingdom_6_lady_15","Parthian Lady","Lulya Karinid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_y],    attrib_common_lady,wp(50),knows_common_lady, 0x000000048010305a124925124928924900000000001c92890000000000000000],
["kingdom_6_lady_16","Parthian Lady","Aridisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady,0x00000004bb083219530e8932e432bb5a00000000001cdb6a0000000000000000],
["kingdom_6_lady_17","Parthian Lady","Orontidisa Arsacid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r],    attrib_common_lady,wp(50),knows_common_lady,0x00000004800c020e46e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_6_lady_18","Parthian Lady","Savacidisa Arsacid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_y],    attrib_common_lady,wp(50),knows_common_lady,0x000000057f08a0ca465800000901161200000000001e38cc0000000000000000],
["kingdom_6_lady_19","Parthian Lady","Artakamasa Arsacid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_b],    attrib_common_lady,wp(50),knows_common_lady, 0x00000005cb1030d9124925124928924900000000001c92890000000000000000],
["kingdom_6_lady_20","Parthian Lady","Suridisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
[itm_eastern_shoe_r,itm_parthian_female_hat],    attrib_common_lady,wp(50),knows_common_lady, 0x000000002c0033161fb496ddb662dbad00000000001c12890000000000000000],

#dear manci, I had to adjust this face :D
#0x0000000702007316701b560510e9c92f00000000001d55930000000000000000
#manci face: 0x0000000000007316725d560d10a1b6db00000000001eb49a0000000000000000
["kingdom_7_lady_1","Poppaea Sabina","Poppaea Sabina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_female_crown,itm_female_caligea_gold], attrib_common_lady,wp(50),knows_common_lady,0x0000000780007316701b540553e9bb2e00000000001e45d80000000000000000],

["kingdom_7_lady_2","Statilia Messalina","Statilia Messalina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000a4604b2cc495d91c60a8747ec00000000001e1c9c0000000000000000],
##die alten (12)
["kingdom_7_lady_3","Aemilia Lepida","	Aemilia Lepida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000d2700530449f04c7f492a156500000000001c61d20000000000000000],
["kingdom_7_lady_4","Sulpicia Drusilla","Sulpicia Drusilla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000d7300304501c01dffe806726a00000000001c51f00000000000000000],
["kingdom_7_lady_5","Galeria Fundana","Galeria Fundana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000fe70402033b5bda574690269d00000000001d985a0000000000000000],
["kingdom_7_lady_6","Vitellia Aula","Vitellia Aula",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000ab308214433a47248e971b46100000000001eb5190000000000000000],
["kingdom_7_lady_7","Messalina Tertia","Messalina Tertia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000b2f0860410b00988d6111986200000000001cb3d80000000000000000],
["kingdom_7_lady_8","Cornelia Maxima","Cornelia Maxima",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000d8804209a12e1b248eb3216db00000000001e490a0000000000000000],

#glatzkopf
["kingdom_7_lady_9","Fabrica","Fabrica",tf_hero|tf_female|tf_unmoveable_in_party_window|tf_randomize_face,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady, swadian_woman_face_1, swadian_woman_face_2],

["kingdom_7_lady_10","Fabia Horatia","Fabia Horatia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000004310c19057117648e097cadd00000000000f18930000000000000000],
["kingdom_7_lady_11","Albia Terentia","Albia Terentia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000dac0c51d9466062596569cceb00000000001d391a0000000000000000],
["kingdom_7_lady_0","Flavia Sabina","Flavia Sabina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000005d0d730a36eb52c72c8da09500000000000d34df0000000000000000],
["kingdom_7_lady_12","Valeria Victrix","Valeria Victrix",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady, 0x0000000ccb0001081b2d6ebb5c8d291100000000001c92890000000000000000],
["kingdom_7_lady_13","Vespasia Polla","Vespasia Polla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000004208d25026a66bb58dadd7aa00000000001ab3a20000000000000000],
##die jungen (12)
#glatzkopf
["kingdom_7_lady_14","Sulpicia Achaica","Sulpicia Achaica",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x00000000330031cd2d0a3cef8a022aa500000000001d55ca0000000000000000],

["kingdom_7_lady_15","Coponia","Coponia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000000000415352c45c14a225b46b00000000001c71e80000000000000000  ],
["kingdom_7_lady_16","Vitellia Tertia","Vitellia Tertia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000003c04005b055bda574690269d00000000001ce0400000000000000000 ],
["kingdom_7_lady_17","Iunia Triaria","Iunia Triaria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x0000000ab90462d94fc11c5e080db6db00000000001fe1f80000000000000000],
["kingdom_7_lady_18","Cornelia Secunda","Cornelia Secunda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000002408619302023c8d6111986200000000001c62180000000000000000],
["kingdom_7_lady_19","Cornelia Quinta","Cornelia Quinta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000002a0830434b66b15705adc0e300000000001dca9b0000000000000000],
##glatzkopf
["kingdom_7_lady_20","Fabia Pia","Fabia Pia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000051204210e773cf6d554b1d32b00000000001ea4180000000000000000],

["kingdom_7_lady_21","Fabia Aura","Fabia Aura",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000002a08b01816845e194995a56300000000001c71e00000000000000000],
["kingdom_7_lady_22","Salvia Minor","Salvia Minor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady, 0x00000001b601715336db6db6db6db6db00000000001db6db0000000000000000],
["kingdom_7_lady_23","Plautilla","Plautilla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady, 0x00000005a80021141b2d6ebb5c8d291100000000001c92890000000000000000],
["kingdom_7_lady_24","Flavia Vespasia","Flavia Vespasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x00000005b8054295270a722cad2dc6eb00000000001d47640000000000000000],
["kingdom_7_lady_25","Flavia Victrix","Flavia Victrix",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_caligea], attrib_common_lady,wp(50),knows_common_lady,0x000000007c08908338e38ce88a8f357500000000001921910000000000000000],

["kingdom_7_lady_26", "Abronia Tullia", "Abronia Tullia", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_eastern_shoe_r], def_attrib|level(4), wp(60), knows_common_lady, 0x000000053f0040d6493dd2db6db2eba400000000001e4b640000000000000000],

["kingdom_7_lady_27", "Domitilla", "Domitilla", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_eastern_shoe_r], def_attrib|level(4), wp(60), knows_common_lady, 0x000000053f0040d6493dd2db6db2eba400000000001e4b640000000000000000],
["kingdom_7_lady_28", "Domitilla minor", "Domitilla minor", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_eastern_shoe_r], def_attrib|level(4), wp(60), knows_common_lady, 0x000000053f0040d6493dd2db6db2eba400000000001e4b640000000000000000],

["kingdom_7_lady_new_1", "Cocceia Prima", "Cocceia Prima", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_caligea], def_attrib|level(4), wp(60), knows_common_lady, 0x00000006ae00204b24ecaeb9236a570a00000000001db91a0000000000000000],
["kingdom_7_lady_new_2", "Verginia Aurora", "Verginia Aurora", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_caligea], def_attrib|level(4), wp(60), knows_common_lady, 0x000000079200009224ecaeb9236a570a00000000001db91a0000000000000000],
["kingdom_7_lady_new_3", "Asinia Stulta", "Asinia Stulta", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_caligea], def_attrib|level(4), wp(60), knows_common_lady, 0x00000005c500d21a24ecaeb9236a570a00000000001db91a0000000000000000],
["kingdom_7_lady_new_4", "Verania Gemina", "Verania Gemina", tf_hero|tf_female|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_7, [itm_caligea], def_attrib|level(4), wp(60), knows_common_lady, 0x0000000029107244373d9238dd69292a00000000001d56dd0000000000000000],

["kingdom_2_lady_6","Celtic Lady","Airmed",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000d400c20432aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_7","Celtic Lady","Conna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000bd108d041782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_8","Celtic Lady","Vinoma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000007a808004a38db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_9","Celtic Lady","Alatucca",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000006d010d05a588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_10","Celtic Lady","Andraste",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000008c00c11992aa5ae36b4259b9300000000001da6a50000000000000000],

["kingdom_2_lady_11","Celtic Lady","Banna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000bc8080045782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_12","Celtic Lady","Catia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000095008804638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_13","Celtic Lady","Vorvena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000809115055588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_14","Celtic Lady","Aessicunia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000054f0cf05d2aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_15","Celtic Lady","Iouga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000050008d20d782a6cc4ecae4d1e00000000001eb6e30000000000000000],

["kingdom_2_lady_16","Celtic Lady","Billica",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000b4008005a3fff39d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_17","Celtic Lady","Carssouna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000b1110d044588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_18","Celtic Lady","Urca Veloriga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000009140cb0592aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_19","Celtic Lady","Bodicacia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000005d308020a782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_20","Celtic Lady","Cartimandua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_celtic_boots], attrib_common_lady|str_15|agi_15,wp(150),knows_common_lady|knows_leadership_9|knows_tactics_6,0x000000045009020c38db99d89eccbd3500000000001ec91d0000000000000000],

["kingdom_3_lady_9","Siracian Lady","Arunavati",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000001940c3046019c925165d1129b00000000001d13240000000000000000],
["kingdom_3_lady_10","Siracian Lady","Canca",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady,0x000000002c0860462ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_12","Siracian Lady","Purnaya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady,0x000000002a0c504348a28f2a54aa391c00000000001e46d10000000000000000],
["kingdom_3_lady_13","Siracian Lady","Santa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x0000000b2e085002471c91c8aa2a130b00000000001d48a40000000000000000],


["kingdom_3_lady_14","Iazyges Lady","Sumagati",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady, khergit_woman_face_1],
["kingdom_3_lady_11","Iazyges Lady","Maya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000019b083045389591941379b8d100000000001e63150000000000000000],
["kingdom_3_lady_17","Iazyges Lady", "Kosthile",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady,0x00000001a700304265cb6db15d6db6da00000000001f82180000000000000000],
["kingdom_3_lady_20","Iazyges Lady","Sumaise",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [ itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000006a0c504348a28f2a54aa391c00000000001e46d10000000000000000],

["kingdom_3_lady_15","Roxolanian Lady","Upatisye",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady, khergit_woman_face_2],
["kingdom_3_lady_16","Roxolanian Lady","Yasaraksite",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000001ad003041628c54b05d2e48b200000000001d56e60000000000000000],
["kingdom_3_lady_18","Roxolanian Lady","Raknaska",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000006c0860462ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_19","Roxolanian Lady","Vasisthe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_eastern_shoe], attrib_common_lady,wp(50),knows_common_lady,0x00000000320c30423ce23a145a8f27a300000000001ea6dc0000000000000000],

["kingdom_4_lady_5","Germanic Lady","Aschild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000054b100043274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_6","Germanic Lady","Eidhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [ itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000058610004664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_7","Germanic Lady","Hildborg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000c004469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_8","Germanic Lady","Ingiburg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13,  [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000000421564d196e2aa279400000000001dc4ed0000000000000000],

["kingdom_4_lady_9","Germanic Lady","Baldhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000054b100043274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_10","Germanic Lady","Casthild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000058610004664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_11","Germanic Lady","Eidwalda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000c004469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_12","Germanic Lady","Hramburga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000000421564d196e2aa279400000000001dc4ed0000000000000000],

["kingdom_4_lady_13","Germanic Lady","Richild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000054b100043274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_14","Germanic Lady","Castiburga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000058610004664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_15","Germanic Lady","Gerrhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000c004469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_16","Germanic Lady","Thusnelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000001150c1469b6ec291b36ce900000000001e5a5c0000000000000000],

["kingdom_4_lady_17","Germanic Lady","Sunhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000054b100043274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_18","Germanic Lady","Theothild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [itm_leather_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000058610004664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_19","Germanic Lady","Aschilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,  [itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x00000000000c004469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_20","Germanic Lady","Thurishilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [itm_leather_boots],attrib_common_lady,wp(50),knows_common_lady,0x00000000000000421564d196e2aa279400000000001dc4ed0000000000000000],

["kingdom_19_lady_1","GermanicLady","Veleda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,[itm_celtic_boots], attrib_common_lady,wp(50),knows_common_lady,0x000000018804611b3a1b71d8db57346e00000000001f1b120000000000000000],

##special ladies
["gwenhwyfar", "Gwenhwyfar", "Gwenhwyfar", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_celtic_boots,itm_dagger,itm_female_4_celt], str_10|agi_8|int_18|cha_20|level(10),
wp(80),knows_merchant_npc|knows_surgery_8|knows_wound_treatment_7|knows_first_aid_7|knows_athletics_1|knows_power_strike_2,
0x000000000f00408a0f6a1c26d54e991400000000001da71b0000000000000000 ],

["thestia_tomitia", "Thestia Domitia", "Thestia Domitia", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners,
[itm_caligea,itm_female_3], str_8|agi_8|int_14|cha_18|level(5), wp(80),knows_merchant_npc,
0x000000003f0050cc76013d20304fed5b00000000001da71d0000000000000000],

["antonia","Claudia Antonia","Claudia Antonia",tf_female|tf_hero,0,0,fac_commoners,
[itm_roman_noble_dress_7,itm_caligea],
attrib_level_12,wp(100),knows_level_12,0x0000000abe0052ce32c17d332ac2b6be00000000001eb20b0000000000000000],

["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

#Seneschals
["town_1_seneschal", "Praefectus", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_caligea, itm_roman_toga], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_2_seneschal", "Praefectus", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_3_seneschal", "Praefectus", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_4_seneschal", "Praefectus", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_5_seneschal", "Praefectus", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_6_seneschal", "Praefectus", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_7_seneschal", "Praefectus", "{!}Town7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_8_seneschal", "Praefectus", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_9_seneschal", "Praefectus", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_10_seneschal", "Praefectus", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_11_seneschal", "Praefectus", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_12_seneschal", "Praefectus", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_caligea, itm_roman_toga], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_13_seneschal", "Praefectus", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_caligea, itm_roman_toga],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_14_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_15_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_16_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_17_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_18_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_19_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_20_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_21_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_22_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_23_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_24_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_25_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_26_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_27_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_28_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_29_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_30_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_31_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_32_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_33_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_34_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_35_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_36_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_37_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_38_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_39_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_40_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_41_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_42_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_43_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_44_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_45_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_46_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_47_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_48_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["town_49_seneschal", "Praefectus", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_toga],     def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],

["castle_1_seneschal", "Praefectus Castrorum", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor4],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_2_seneschal", "Praefectus Castrorum", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_3_seneschal", "Praefectus Castrorum", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_4_seneschal", "Praefectus Castrorum", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_5_seneschal", "Praefectus Castrorum", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_6_seneschal", "Praefectus Castrorum", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_7_seneschal", "Praefectus Castrorum", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_8_seneschal", "Praefectus Castrorum", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_9_seneschal", "Praefectus Castrorum", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_10_seneschal", "Praefectus Castrorum", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_11_seneschal", "Praefectus Castrorum", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_12_seneschal", "Praefectus Castrorum", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_13_seneschal", "Praefectus Castrorum", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_14_seneschal", "Praefectus Castrorum", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_15_seneschal", "Praefectus Castrorum", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_16_seneschal", "Praefectus Castrorum", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_17_seneschal", "Praefectus Castrorum", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_18_seneschal", "Praefectus Castrorum", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_19_seneschal", "Praefectus Castrorum", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_20_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_21_seneschal", "Praefectus Castrorum", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_22_seneschal", "Praefectus Castrorum", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_23_seneschal", "Praefectus Castrorum", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_24_seneschal", "Praefectus Castrorum", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_25_seneschal", "Praefectus Castrorum", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_26_seneschal", "Praefectus Castrorum", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_27_seneschal", "Praefectus Castrorum", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_28_seneschal", "Praefectus Castrorum", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_29_seneschal", "Praefectus Castrorum", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor3], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_30_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_31_seneschal", "Praefectus Castrorum", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_32_seneschal", "Praefectus Castrorum", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_33_seneschal", "Praefectus Castrorum", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_34_seneschal", "Praefectus Castrorum", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_35_seneschal", "Praefectus Castrorum", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_36_seneschal", "Praefectus Castrorum", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_37_seneschal", "Praefectus Castrorum", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_38_seneschal", "Praefectus Castrorum", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor1],    def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_39_seneschal", "Praefectus Castrorum", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_caligea, itm_roman_poor5], def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_40_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_41_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_42_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_43_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_44_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_45_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_46_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_47_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_48_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_49_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_50_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_51_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_52_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_53_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_54_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_55_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_56_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_57_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_58_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_59_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_60_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_61_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_62_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_63_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_64_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_65_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_66_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor1],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_67_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor2],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_68_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_69_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_70_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_71_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor6],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_72_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor7],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_73_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor7],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_74_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor6],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_75_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_76_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor5],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_77_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor4],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_78_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_79_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],
["castle_80_seneschal", "Praefectus Castrorum", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[	 itm_caligea, itm_roman_poor3],   def_attrib|level(2),wp(20),knows_common, roman_face1, roman_face2],

#Arena Masters
["town_1_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d1b08130b3753a6ace28eb76300000000001e59330000000000000000],
["town_2_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000081b10010d44ad31275a34c8cc00000000001db50c0000000000000000],
["town_3_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000cab0810095a14a6b89a4db32b00000000000f56ce0000000000000000],
["town_4_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000da801300c216470c67e49291c00000000001d4d580000000000000000],
["town_5_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000e280415d236e6937ad9a9672500000000001cd76a0000000000000000],
["town_6_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a8400d0093362b646a189192300000000001ee4d30000000000000000],
["town_7_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000ebb0d32c157bcb9885bdda6ea00000000001db6cc0000000000000000],
["town_8_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c9300b08f192bb5b74b96cd1100000000001d388b0000000000000000],
["town_9_arena_master", "Auctor","{!}Auctor",tf_hero, 0,reserved,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008030c048c656d5b3991aed52c000000000013576c0000000000000000],
["town_10_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000de905150e052c6e66d466c72a00000000001ec91d0000000000000000],
["town_11_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000083d0c31cf457435a35456acd300000000001d45220000000000000000],
["town_12_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bf10d22c358cb95a72ab5789a00000000000946c90000000000000000],
["town_13_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000cee11151126aad5bb944aa6dc00000000001d37640000000000000000],
["town_14_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000dd004d1481b5371a7247546eb00000000000e46e40000000000000000],
["town_15_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d2a09224b475357577610a90b00000000001c169c0000000000000000],
["town_16_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b730011c33693ae59248e4a5600000000001dd8d90000000000000000],
["town_17_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d110030042689c8baad75a4da00000000001d2ad80000000000000000],
["town_18_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000ccd0c3289491bd63adc0d392d00000000001db6db0000000000000000],
["town_19_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008370cc583591d89cb148d94ea00000000001e54340000000000000000],
["town_20_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d740ce00817194d572e7922b400000000001dbb6d0000000000000000],
["town_21_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000e0710b4cb5aa5993acfcd19ab00000000000aa8dd0000000000000000],
["town_22_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c1f10e411369b93138a4e945c00000000001e26da0000000000000000],
["town_23_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008c00011c548ab89c4e955ca6500000000001dd76d0000000000000000],
["town_24_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000097c09128c49a399db15653a5b00000000001e372b0000000000000000],
["town_25_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b3f0021833ae5aaa6a28a68d500000000001cc9480000000000000000],
["town_26_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d7e0925113761d9291dcdd75d00000000001c38cc0000000000000000],
["town_27_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008400cb14338a2715b23aebae500000000001e8af30000000000000000],
["town_28_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c8c08b3812b0b8d5b5be91c9a000000000011d9520000000000000000],
["town_29_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a9a0101882715b8d8e2a94b4f00000000001dc7200000000000000000],
["town_30_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d260d259168d46d2b1b4a27a600000000001eab150000000000000000],
["town_31_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000086600c0115a634deb1a49562300000000001cc8b20000000000000000],
["town_32_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000086509340d4ba945590e52135d00000000001f3b2a0000000000000000],
["town_33_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000f201130512f8b6a595eba24da00000000001e58d00000000000000000],
["town_34_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000097a08110e56ed6e16e226c6dc00000000001cb7730000000000000000],
["town_35_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d3f000184271aaeda6c8d5aaa00000000001d33500000000000000000],
["town_36_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d630c150854d2a7276528489a00000000000928ad0000000000000000],
["town_37_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008b608020138a3aeb8b5715c6c00000000001d37130000000000000000],
["town_38_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000f0d10048946ed6ed6dcd098f400000000001e69450000000000000000],
["town_39_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000ad710e1845269a958db92d8a500000000001d42d30000000000000000],
["town_40_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d6504b1cb44ed94c95d4d148a00000000001dcca40000000000000000],
["town_41_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000aaa10348e4cca2122d469d6e800000000001e6ad60000000000000000],
["town_42_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bd30c21894923cad911891b3300000000001dd4bb0000000000000000],
["town_43_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000081c0d340c4453cdeead563ab500000000001d589c0000000000000000],
["town_44_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000e5e08005038e17613b449caa400000000001d3adc0000000000000000],
["town_45_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009010011c3169a39c726a5429d00000000001d13200000000000000000],
["town_46_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000092608058404b3aa5a6a46b72900000000001e37630000000000000000],
["town_47_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000088400c1d136ed47d6cda5b72a00000000001ee6d90000000000000000],
["town_48_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c8004e15223aa6da7b545369b00000000001e4c9c0000000000000000],
["town_49_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000f7f0001c3290c36ec5c4dc66400000000001eb6f90000000000000000],
["town_50_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000ff60d75ce422173661bad2f0a00000000001d47930000000000000000],
["town_51_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000000cb54537238e36fa98b8a2000000000011a29b0000000000000000],
["town_52_arena_master","Auctor","{!}Auctor",tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000000600408d3c966e3d1aadacdc00000000001674ab0000000000000000],

# Armor Merchants
#arena_masters_end = zendar_armorer

["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000054a00224b590a6ac7122dd6db00000000001e36a30000000000000000],
["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000025b00208734e48f4b5955272600000000001ca6ec0000000000000000],
["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000046104b003669c51fd112e97650000000000062cda0000000000000000],
["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a050c01042ae9c9b6d26ec4e4000000000005a9150000000000000000],
["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000079b0c43d2289b71a7dcd2c52300000000001d22dc0000000000000000],
["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002220010044a6b524412ca44e500000000001d591a0000000000000000],
["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000073811144117ad72c32c93251d00000000001eb5a50000000000000000],
["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000c8c00314a332551a498adc98b00000000001ca6540000000000000000],
["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b9e00124734924e19744e689400000000001da5120000000000000000],
["town_10_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b2e1121836d669796b44dc71b00000000001236ad0000000000000000],
["town_11_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000d909118728b54a0aaa6a4d0c00000000001e38da0000000000000000],
["town_12_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002900001833724693692759d1b00000000001d28a90000000000000000],
["town_13_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a1e0d23cf486c8e371db2a09400000000001e2d5b0000000000000000],
["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002b41161c6271c74196b05552a000000000009549e0000000000000000],
["town_15_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000099d00230768e236b16d35471300000000001d1db40000000000000000],
["town_16_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008af0011c744d9724462b6471600000000001ca7230000000000000000],
["town_17_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000007c800d090161b712b2229a8dc00000000001da9940000000000000000],
["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000030f0c6004371296c9156d56dd000000000004b76a0000000000000000],
["town_19_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000764086543152c756d9d6d376300000000001cb8d30000000000000000],
["town_20_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000ec0d04c838662b451d8e489b00000000001cd4f40000000000000000],
["town_21_armorer","Armorer", "{!}Armorer",  tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000fc08c58f14ceb1c75384c6a900000000001a66af0000000000000000],
["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000179003043169c4e48d589d4e400000000001e254e0000000000000000],
["town_23_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002c61020c24b4b5646e4ad391b00000000001eb6c20000000000000000],
["town_24_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000004160111c1472b2ccb1a7146e200000000001cbcd30000000000000000],
["town_25_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000ae08820656dc8b476b75a51d00000000001d566d0000000000000000],
["town_26_armorer","Armorer", "{!}Armorer",  tf_hero|		   tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000037c083309365487390aae36ea00000000001e627c0000000000000000],
["town_27_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000008b1050484375ae2b236cc51c00000000000e36d40000000000000000],
["town_28_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000007c108f18438e248b72375498d00000000001e48d30000000000000000],
["town_29_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000a704a2cd191971c70b8e689500000000001d36e40000000000000000],
["town_30_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000006660d100146ea11c6f2924a6200000000001e49130000000000000000],
["town_31_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000025b08c09643a4919d5c92d25d00000000001cb6a30000000000000000],
["town_32_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000060d086187368c2cd6ca35a8d2000000000011939c0000000000000000],
["town_33_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a7f09120929127946eb8eb69e00000000001ce59a0000000000000000],
["town_34_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000fe04b5105333ae2ae430e79d00000000001566ce0000000000000000],
["town_35_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000006590d300d177570ac9d6e46db00000000000d385e0000000000000000],
["town_36_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000009fb11158a56e395b970f94c5100000000001cc89c0000000000000000],
["town_37_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000033b0ca00204f269dd928a38dc00000000001ea6e90000000000000000],
["town_38_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000035b000144490c3238e452c93300000000001d57550000000000000000],
["town_39_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000034d0cc20c5a54b24ba34928a500000000000db2b30000000000000000],
["town_40_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000027808300332f16c9762aa3cd200000000001da9240000000000000000],
["town_41_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000097d11324d475db4db2232e4ca00000000001d4b120000000000000000],
["town_42_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000036f0550c455628c690a537aab00000000001fb7030000000000000000],
["town_43_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000c420111c8352bca9cee8e3d6100000000001de2e40000000000000000],
["town_44_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a0e011510490fd638538f591b0000000000113b4f0000000000000000],
["town_45_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b0711258f2d6235c8e586491d00000000001d47050000000000000000],
["town_46_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000008000004236d54f395449d4e200000000001dc6ed0000000000000000],
["town_47_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000081604c345266e8988a48d4ad200000000000e44e40000000000000000],
["town_48_armorer","Armorer", "{!}Armorer",  tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002ba0442164663b1a85d91eaf300000000001110da0000000000000000],
["town_49_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000007f31014015a758e36e5b0b9230000000000061d250000000000000000],
["town_50_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ed05358d472d76e98b2a98dd00000000001e36610000000000000000],
["town_51_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000001b0cb58d47233632d915c87500000000000e3ae30000000000000000],
["town_52_armorer","Armorer", "{!}Armorer",  tf_hero|tf_is_merchant,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000000c08b2c5052352b74e55b70b00000000000c96d80000000000000000],

# Weapon merchants
["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000009501619a16d3294b6a32c56b00000000001c3ade0000000000000000],
["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a3901140f292d50ab5d99a51500000000001dccac0000000000000000],
["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000ae70c3592345cb23c6456095300000000001d18890000000000000000],
["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000480851114ada8b246491ca6600000000001c59120000000000000000],
["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000007580022ca18ca6a54e56cb97200000000001dc91a0000000000000000],
["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000001bc00600c265454c51b895b6d00000000001dc6cc0000000000000000],
["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b7300258d355c6a14eb8e42ab00000000001e495d0000000000000000],
["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000001eb04a0016366b1c3748f371200000000001e29610000000000000000],
["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000064b113206387395975bb1972e00000000001ebd9b0000000000000000],
["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000001810124e47552917178e972300000000001cdaf40000000000000000],
["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000a240420cf14b57246a455b98a00000000001db9240000000000000000],
["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000cb90003c17954ada764864eb400000000000f425c0000000000000000],
["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b1a10420f37216dca9c9934e400000000001e531d0000000000000000],
["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008d80135481b0a2c671d723c6400000000001dc2cc0000000000000000],
["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000aa300330742eb79970c69c49c00000000001dba5a0000000000000000],
["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000aff05118c16ac71d73434992600000000001db6930000000000000000],
["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002fa0402c247324dd923d9e91300000000001da4eb0000000000000000],
["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002fd10d241672c52a3232a5ad20000000000066aab0000000000000000],
["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000003f01328238da24c6cb2e892b00000000001d3acc0000000000000000],
["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000081200e14a190baa392b2d936a00000000001e455b0000000000000000],
["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000a601020054e3d146d9ced6ae00000000001d3f230000000000000000],
["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000074210c34c19ae7a46aa31394b00000000001e28650000000000000000],
["town_23_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000026108324f54d9c55953a936d300000000001d9c920000000000000000],
["town_24_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000009d5002445572a71a6db6e386d00000000001e59920000000000000000],
["town_25_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000077a00128242ce2e22dd6995ab00000000001d48930000000000000000],
["town_26_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000043f0d13055a5a9519b425c8e500000000001e148c0000000000000000],
["town_27_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000e790d228f371b78c90dd53ce300000000001edc9a0000000000000000],
["town_28_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000e70042953ae571b49e45b56600000000001e5a330000000000000000],
["town_29_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000c9c00704a2c9c45ded375472c00000000001da71c0000000000000000],
["town_30_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000001d20c058437137132cbc6494500000000000eb28e0000000000000000],
["town_31_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000c7c05100a389bb0e4e44d8f2b00000000001db6ea0000000000000000],
["town_32_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000000a10b004530e4cc6a345ba0b000000000005b4dd0000000000000000],
["town_33_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000310c300b64dab2394c5688db00000000000638720000000000000000],
["town_34_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000003e104511132bb4aca5389c6db00000000000a2b5c0000000000000000],
["town_35_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000004b605258f5b1191c895691aad00000000001e5a960000000000000000],
["town_36_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000c261114c312acb757218c8ab200000000001d54320000000000000000],
["town_37_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000004ae04038e3764b2c8992c44dc0000000000123b230000000000000000],
["town_38_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b931034c944e456c4b289e8cc00000000001e34f30000000000000000],
["town_39_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000003f600624226948e04e68538c300000000001de6ca0000000000000000],
["town_40_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000015e09115546d5519913b2468b00000000000e6b9d0000000000000000],
["town_41_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000092a08d04f52954dd8a322ca9400000000000a36ae0000000000000000],
["town_42_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000cb10032433923adc88c32fb5b00000000001d2d930000000000000000],
["town_43_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c409329269b3bb51646e3b5a000000000019a4d40000000000000000],
["town_44_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000b9900118546c345a76c89449d00000000001d5d250000000000000000],
["town_45_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000002580c03c7132e51c92349dd1200000000001ef6eb0000000000000000],
["town_46_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000003c00002c2471dad190492bbbb00000000001dd55d0000000000000000],
["town_47_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000025608f20e38ec35dad2b2955b00000000001e290c0000000000000000],
["town_48_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000007150060074a926d049c8adb1100000000001e376c0000000000000000],
["town_49_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000000c01571b5406e94651a49d00000000001f15210000000000000000],
["town_50_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000fc400244658a5464693b8ef13000000000009d72b0000000000000000],
["town_51_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000000508f289491c8dcbdd71395a000000000016c3150000000000000000],
["town_52_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero| tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000003f0d204d2ccd3714ac69b7ac00000000001db3570000000000000000],

#Tavern keepers entry 9

["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c8e0013073b0c25b4da96d91300000000001ce9130000000000000000],
["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000060910d19158b39944ea95a8da00000000001e4b2c0000000000000000],
["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000037400721649516e3359a93a6a000000000012c5550000000000000000],
["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000046204d192589a8d1b0ea9b723000000000019c32d0000000000000000],
["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000002a311200a6b654a1addb1bb2d00000000001e57550000000000000000],
["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000001bf10a3170b6b7138ab2eaa6400000000001f5cb30000000000000000],
["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000025608225c46657532598f3cb200000000000d4add0000000000000000],
["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009ba10050b34b38666d972ecd000000000001d92e60000000000000000],
["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000091170072a9c25b6e4adf4a900000000000f34950000000000000000],
["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000355101216589c51c59646472c000000000007da9b0000000000000000],
["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000017005709c29248dea95d1975a00000000000ebcf30000000000000000],
["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000062b0001c848b22b38d445d32c00000000000616d30000000000000000],
["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000008c042243594972446b7236dd000000000012d2db0000000000000000],
["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000063208145146eb5199a485c75900000000000d48e30000000000000000],
["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000001400cd281195a50e29451c52300000000001dd8950000000000000000],
["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000009a1044914ce3751a820ecad600000000001cbcdd0000000000000000],
["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000de1052d72aa2327b29474cd500000000000a5c250000000000000000],
["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bba09245143a5cec71a32653200000000001eb6eb0000000000000000],
["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000036304010532e971146dceb6c100000000001da6c30000000000000000],
["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000aed0cb0012d4cb224f4cd56ad0000000000123cdb0000000000000000],
["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000013a10321149252a3694b2b8dc00000000001347160000000000000000],
["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000091d10f4c116a2cd37964e58eb00000000001da71b0000000000000000],
["town_23_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009091013d009b3c9155472b5e400000000001d17530000000000000000],
["town_24_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a1e01130a3ae6ccc6e6772ab000000000001d3b130000000000000000],
["town_25_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000003100c32473d0b9228e18238dc00000000001f371d0000000000000000],
["town_26_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000055200418426db4dc5588b696400000000001c364a0000000000000000],
["town_27_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000000b10321166dcc4c6ec71189500000000000a965c0000000000000000],
["town_28_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000071800c5912287d6172995c6cd00000000001dbb5c0000000000000000],
["town_29_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000097e0d01d116aa6646e1b052e2000000000015e76e0000000000000000],
["town_30_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000008300304113228998d295a52a00000000001e288b0000000000000000],
["town_31_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000ea0111ca6b248a48e3b1a68c00000000001ea90a0000000000000000],
["town_32_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c9408118d3b81ae2d0a71476700000000001a251b0000000000000000],
["town_33_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000004680c31834cd54dc71a32d71500000000001e46a60000000000000000],
["town_34_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000001590830093ceba99b28a9c69e00000000001f18eb0000000000000000],
["town_35_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000071e0933cf285ca6a9627316d200000000000a26dd0000000000000000],
["town_36_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000061b0d25c5332376b96d74cb640000000000093aa30000000000000000],
["town_37_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000001b701730864d247bd0b85caaa00000000001e548a0000000000000000],
["town_38_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c0400d5c6275055c54c8b58a10000000000023ad10000000000000000],
["town_39_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000004200c5872c5b48b76305325300000000000db7190000000000000000],
["town_40_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000bc10b04465914db8947a4b2a00000000000e48d20000000000000000],
["town_41_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000007b600119126a26d273396c85e00000000001d13920000000000000000],
["town_42_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000861133c1546b35274151b19a00000000001d37240000000000000000],
["town_43_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008c51134093b5a73252a4de4d500000000001d67230000000000000000],
["town_44_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000090532924a549538db76a76200000000001f99510000000000000000],
["town_45_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000006c100128616dd8952d24f389200000000001e17530000000000000000],
["town_46_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_female, 0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000001ce04d2114e9bb05993db150b00000000001d44fc0000000000000000],
["town_47_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000084d0ce01148da5266fc8e34e1000000000009a5950000000000000000],
["town_48_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c4700e34b4733cad29972e72400000000001a37690000000000000000],
["town_49_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000005c30123054b2400bb516eb7ea00000000001ddb5a0000000000000000],
["town_50_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000000320132c6125c696ba449cb2400000000001da6610000000000000000],
["town_51_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d7f00e1d14a9c9ac89ba2366200000000001dc74c0000000000000000],
["town_52_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero,  0,0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d6b0550862ca3ab25b495bcdd00000000001d4a630000000000000000],

#Goods Merchants # entry 9

["town_1_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000054b05228d4964b3294bd9396400000000001d485a0000000000000000],
["town_2_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a970c000354e574b2d36b3b0900000000001e1acb0000000000000000],
["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000002530012d526a88ec4a2d02d110000000000093c9a0000000000000000],
["town_4_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d860041913b6446455daca29f00000000001de4930000000000000000],
["town_5_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000006ef10300a5d7472a6e28f297500000000001e25130000000000000000],
["town_6_merchant", "Mamertinus Crachus","Mamertinus Crachus",tf_hero|tf_is_merchant, 0,0, fac_commoners,[itm_roman_rich2,itm_caligea],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000100c40096759cab76bc757ac00000000001ec55d0000000000000000],
["town_7_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000088d0833455522accb1bad16d600000000000a58950000000000000000],
["town_8_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a8a10125156a3ad58a34ec62300000000001e27630000000000000000],
["town_9_merchant", "Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000c8905228e4959a9b7ab8ecc9400000000001e26dc0000000000000000],
["town_10_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000050610d34528e588a69239465c00000000001a148a0000000000000000],
["town_11_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000c29001201395286d51551cb2c00000000001e49980000000000000000],
["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000002cc052197245ecf36734db8a3000000000012095e0000000000000000],
["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000000a909531163a9a95ad21248ab000000000008a8e40000000000000000],
["town_14_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a3d10d181254b4f3b236a665c000000000006c8920000000000000000],
["town_15_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000007841011cb24a36630ab964664000000000011ca6d0000000000000000],
["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000001a041088289c86a8c945b96400000000000628a20000000000000000],
["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000030b0552d448d25b329269c65d00000000001336dc0000000000000000],
["town_18_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ced1125cf22d4b6c869223b1a0000000000158b620000000000000000],
["town_19_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a4b10b2065d1bd136336d9cae0000000000091d550000000000000000],
["town_20_merchant","Bastet","{!}Bastet",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000003f0000c31f315dbfe979af2400000000001c204d0000000000000000],
["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000000560440551b9451a91b91b4ac00000000001ca8e30000000000000000],
["town_22_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d970c31d0278aae1b1e91c8ea00000000001e4b570000000000000000],
["town_23_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000009800011c23693ae59248e4a5600000000001dd8d90000000000000000],
["town_24_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000b120c02c54393563a6c9ac75e00000000001e591b0000000000000000],
["town_25_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000005b705140e3b1b8f366c69669600000000001e54e30000000000000000],
["town_26_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3e0c124b2965d626e376bda900000000001ec0e20000000000000000],
["town_27_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000002350c9056195c652ba398c69a000000000011b69b0000000000000000],
["town_28_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000efc08c5822523b719564d352b00000000001a39b20000000000000000],
["town_29_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f9408e18834cd5545366e46e400000000001eb4a20000000000000000],
["town_30_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d2d0015c23523577aa346529500000000001cb5100000000000000000],
["town_31_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000009df05310f2a66ad4b55ceb65500000000001d54940000000000000000],
["town_32_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000029d04c243155e4d46b371c6e500000000000959650000000000000000],
["town_33_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000004480d110d1d6a325ceec89b2d00000000001e355a0000000000000000],
["town_34_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3f0c128f18e62edb9d6ed79500000000001dbd120000000000000000],
["town_35_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d0b103344375b8b26d345a91a00000000001dc8d60000000000000000],
["town_36_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000cc210224d2a9234b35392169c00000000001d9b5d0000000000000000],
["town_37_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000008e60915843b9496cb5268cced00000000001e870a0000000000000000],
["town_38_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000000b304a1125ad371c31286646c00000000000e13dc0000000000000000],
["town_39_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000004b710c24f3970cca6a391c8e5000000000019671a0000000000000000],
["town_40_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000040d04321123666f196d4cd763000000000008e90d0000000000000000],
["town_41_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e7e0412921aad2e4894cd342300000000001ebaea0000000000000000],
["town_42_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000204090204179c75db33a634e5000000000009629a0000000000000000],
["town_43_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000b1b0c050265a997581471a45b00000000001152630000000000000000],
["town_44_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000001a2040246392551385389b623000000000009331c0000000000000000],
["town_45_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e060125c5151ca546dc6e431300000000000976130000000000000000],
["town_46_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000007700d12cd5365b53b1b693968000000000015b9550000000000000000],
["town_47_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000002d04a18f18e22dc45a2cc69500000000001cba650000000000000000],
["town_48_merchant","Sinue Migdue","{!}Sinue Migdue", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb90471c9369492c91c7124e200000000001ca28b0000000000000000],
["town_49_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a860d22484ad932b6b16ab68b00000000000a45650000000000000000],
["town_50_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000002e11124e52e329d51991a69500000000001eb95a0000000000000000],
["town_51_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d6d00628449abae354b319ba2000000000009b9620000000000000000],
["town_52_merchant","Merchant","{!}Merchant", tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4c08b349251a56272679b7b100000000001e57320000000000000000],

# Horse Merchants
["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_is_merchant|tf_female,    0, 0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000008d20ca24c28d26a53319749eb00000000001935530000000000000000],
["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008cc011343355d873864a9aae30000000000066a630000000000000000],
["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c40431c614896ee4a4aad9ec000000000019d84a0000000000000000],
["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c20c31c43722b66a222dbd2a00000000001ea7250000000000000000],
["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_is_merchant|tf_female,    0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008cc045107575a5226cc74d2ec00000000001dc52e0000000000000000],
["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c1112004486d6a4b6c89a90c00000000001d48e40000000000000000],
["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fb011145292184a5cc71b791000000000005b2e40000000000000000],
["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008d500c1cd53132f34ea6a18e300000000001235350000000000000000],
["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_is_merchant,     0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c004040a269db24d146d390a00000000001fb9140000000000000000],
["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f409421318c352a8d592ea9900000000000dcb2c0000000000000000],
["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c90c218427246de252b4e4ce00000000001db91a0000000000000000],
["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008cd00230d04ed75b9642de9b400000000001ecadc0000000000000000],
["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f60012ce49926e22ed2ab6ec00000000001cb89a0000000000000000],
["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f909108334e38d38e399555c00000000001155920000000000000000],
["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c004008e29294e249d973ad900000000001e371c0000000000000000],
["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ca0d21112d2690e49a6ab76e00000000000b371a0000000000000000],
["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ff1123d152938e379a0ea8ee00000000001ea7250000000000000000],
["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fa0821d83d1eadc65a7644e400000000000db5620000000000000000],
["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008d608c5c7252352ec92bb289b00000000001e5c8b0000000000000000],
["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008cc10610c3a5c91d72189d76e00000000001d559b0000000000000000],
["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f700e4093d2d91d49b29361a0000000000019ce50000000000000000],
["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fb0832d634e1aa1b2545d6cc00000000001244a50000000000000000],
["town_23_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c011415c00f3723b1e8db91d00000000001ca84b0000000000000000],
["town_24_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c308228f489d8d406d8dab1200000000001236930000000000000000],
["town_25_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f210c0864b5d50abdc4e3b3100000000000ac9630000000000000000],
["town_26_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008d210528f1acbaa3734ba64a300000000001e93920000000000000000],
["town_27_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ca0cb1104add8657da9bc51900000000000988cc0000000000000000],
["town_28_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c90440061addd1552aa8ecab00000000001e16d80000000000000000],
["town_29_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008e00c425416da2ab689a9a17400000000001e3abf0000000000000000],
["town_30_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c00cc450236342a56aaa950c00000000001dcacb0000000000000000],
["town_31_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x000000066a09504a6b5d2f33a376335300000000001ed6e40000000000000000],
["town_32_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c40124061ae9a536e261c2a900000000001cc4d50000000000000000],
["town_33_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c20432571cd992871b4daa9200000000001138e30000000000000000],
["town_34_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fe10300953226e3ce37698a400000000001db9520000000000000000],
["town_35_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c100608e2864519cd0a639110000000000115e8e0000000000000000],
["town_36_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f41090031882d934cadd7d1c00000000001db72b0000000000000000],
["town_37_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fe0c010924e579eae597588b00000000001ed4d20000000000000000],
["town_38_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c30c5155481a4e151dbaab2b00000000000abc510000000000000000],
["town_39_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ea00a141385a9536e28dd2a1000000000009c55e0000000000000000],
["town_40_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f208c20b586a6acb15a5b31400000000001dc85c0000000000000000],
["town_41_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008e304208c074eb5bb24b1baf400000000001126b50000000000000000],
["town_42_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008ee0cb18462eaaec6ae6566eb00000000001dcb990000000000000000],
["town_43_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008dc09404a68d44550dc8da35200000000000f38d40000000000000000],
["town_44_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008c600120356e389c99c2b455b00000000000948d40000000000000000],
["town_45_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008cb08d18d66b39028f22a48f300000000001e99220000000000000000],
["town_46_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008d704d097355269cb75ae192a000000000005a8e30000000000000000],
["town_47_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008fa10b4ca5ce4654b63ccc8ad000000000015da6c0000000000000000],
["town_48_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant|tf_female,  0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008dc0c308c38db90a71db5b32300000000001f59150000000000000000],
["town_49_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000008f510224f631932cb7b8b157100000000001cd51c0000000000000000],
["town_50_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x00000000100434424b1a2cbd1392552a00000000001d15240000000000000000],
["town_51_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000d4700600e4ae1c9ebec92c6f900000000000dd3220000000000000000],
["town_52_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_is_merchant,   0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10,0x0000000d7208f5d146526c84dbd6c68b0000000000093b100000000000000000],

#Town Mayors    #itm_linen_tunic itm_linen_tunic itm_linen_tunic itm_linen_tunic itm_linen_tunic itm_rich_outfit
["town_1_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008e300030136939222d592a95c00000000001dbb250000000000000000],
["town_2_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000078400020832d9512aad6e372300000000001dcb5a0000000000000000],
["town_3_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b740d11ce44db91b79b48b0fd00000000001dc6a30000000000000000],
["town_4_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008fa01200f239b2dc72a69c38b00000000001e63120000000000000000],
["town_5_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a3d00100942db4cb7608534e300000000001e58d60000000000000000],
["town_6_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000003708c011573442d9656cb4d900000000001db8dc0000000000000000],
["town_7_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000871092203372bb13a549502d100000000001e4c820000000000000000],
["town_8_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c1b08d54542eb2192e2b8166900000000001e34dc0000000000000000],
["town_9_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000aed0022c6391b55c69ed4ad6400000000001d9b8c0000000000000000],
["town_10_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008ab0061c92aea95352690b4cd000000000019c3eb0000000000000000],
["town_11_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008870003022b5a2a28d2a9b53400000000001d936b0000000000000000],
["town_12_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000ba000230539102e22d4ad9ca200000000001e2d140000000000000000],
["town_13_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000086f0d128f159d76a4d9cab53400000000001e3a740000000000000000],
["town_14_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a7610224167aa2c9da46d491b00000000001dbb150000000000000000],
["town_15_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b840d128f46ec6d468c4db56200000000001d9b120000000000000000],
["town_16_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008a300118246dc693b348e3d2600000000001d47540000000000000000],
["town_17_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009610041823b9274b6a18d9b1900000000001dc7130000000000000000],
["town_18_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b7f0c23cb18e25254dba626f300000000001e3b6b0000000000000000],
["town_19_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000087f053589471c31a6a264b65c00000000001eb6ee0000000000000000],
["town_20_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c0604b4d144e3463526894ba600000000001dc2dc0000000000000000],
["town_21_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a250071c928eb69c762aab75b00000000001e471b0000000000000000],
["town_22_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008eb10c1c35b1bcab4946e3249000000000017188c0000000000000000],
["town_23_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008c00002835719264a8bb5e6db00000000001d97590000000000000000],
["town_24_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c8b005307492388ab0451b6e400000000001e17250000000000000000],
["town_25_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000cbf0011d24b4c795ae576250b00000000001d479c0000000000000000],
["town_26_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008ef00320a56da5602e38ae99400000000001db9630000000000000000],
["town_27_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bd510d184392e31c912b1c7a300000000001ccb210000000000000000],
["town_28_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008f50ce44b18a6afc3244d472d00000000001da6a10000000000000000],
["town_29_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b261071002761a927a26e551200000000001da8d30000000000000000],
["town_30_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000aa7000182332945e45db4f725000000000005a4b30000000000000000],
["town_31_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000086a01144424dc6db71cd63c5c00000000001dd6a20000000000000000],
["town_32_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b2a09124b46d112d71b7a196b00000000001da91b0000000000000000],
["town_33_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000be911101256b554dd952a993300000000001d416c0000000000000000],
["town_34_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009eb11200f38cc8d34dd9994ab000000000011cd2b0000000000000000],
["town_35_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000836001289551ab1369c02474500000000001924e60000000000000000],
["town_36_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bbf1001cf34ba9926f54dbc1a00000000001ec69a0000000000000000],
["town_37_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000009560c25884514b1c322d24522000000000006c65e0000000000000000],
["town_38_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a2b01144616bcc73b1b643b1a00000000001daca20000000000000000],
["town_39_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000be800b29048a68e8912710b64000000000002cce30000000000000000],
["town_40_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bb704c51114d34eb8f490a4f600000000001ef7a30000000000000000],
["town_41_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000083f0d25cb291e8a4b238e3ba400000000001e49230000000000000000],
["town_42_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000c821112c55978a5c93455a52300000000000dcad40000000000000000],
["town_43_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a0f0921454ba275298a8dbb2400000000001dc49a0000000000000000],
["town_44_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b480c234b1b6162205b8e6a9000000000001d545c0000000000000000],
["town_45_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000a470d11d00a1b4e44638e4d9200000000001e37750000000000000000],
["town_46_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x00000008160012092b5952a51349272300000000001ea4de0000000000000000],
["town_47_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000b0c0cb2814ae995289d6dc76900000000000ed29a0000000000000000],
["town_48_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000bdd10b4114b5699c69c9134b300000000001dd4cc0000000000000000],
["town_49_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000aec04234d53138d37b4481b3200000000001eb3220000000000000000],
["town_50_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x000000002108334e5cdd3e389a21270c00000000001244d30000000000000000],
["town_51_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d7f0c200d22968ea8deb12ada00000000001d26630000000000000000],
["town_52_mayor", "Magister Civium", "{!}Magister Civium", tf_hero, 0,reserved,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common,0x0000000d710cb58e54e49a271b4ab96b00000000001e2cdb0000000000000000],
#Village elders
["village_1_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4e092302568b7748ed72c8d200000000001d326e0000000000000000],
["village_2_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e1304b14139626a685a59d92a00000000001b39640000000000000000],
["village_3_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e470531c8561c96685b94ecca00000000001dd48a0000000000000000],
["village_4_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d380d200e24d9ce38ddae6b0c00000000001e38ac0000000000000000],
["village_5_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ec40121cd4b4890c29d6d510d00000000001e4cee0000000000000000],
["village_6_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f6c00b1843713a5a45c76d4d300000000001cb7a90000000000000000],
["village_7_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ea208650222dc38b29d4d18a300000000001f16e40000000000000000],
["village_8_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e2e0521c838e5af57252dacae00000000001d4b020000000000000000],
["village_9_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000cfc05234425259a37216abb2900000000001ce72b0000000000000000],
["village_10_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000da404225067638ddd2176b25a000000000005a4b50000000000000000],
["village_11_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e350d12834d146e19186db32100000000001dc7320000000000000000],
["village_12_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dbd0022022a943a54d96c365400000000001e3d180000000000000000],
["village_13_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3e08341046e36d590c88b29e00000000001634e90000000000000000],
["village_14_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4404034f4961cedad56e5b9b00000000001145230000000000000000],
["village_15_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d160811444eac45a89a4ab96000000000001e572b0000000000000000],
["village_16_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e050c230e3ac9c5dc5b8e64ac00000000000da94c0000000000000000],
["village_17_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e4d00414439d98ebc6c85471500000000001d45280000000000000000],
["village_18_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d43000247129a51a66a4db6d500000000001eae8b0000000000000000],
["village_19_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ed004428114538e4a963495a100000000001289d40000000000000000],
["village_20_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d200d144525443638f4bb34ea00000000000d0af30000000000000000],
["village_21_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f820d120d32616e6bf289c78500000000001e946b0000000000000000],
["village_22_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d5a11124d3b4971d7a46a391b000000000014c4a10000000000000000],
["village_23_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000df110050d4c9cb65b53a72b7300000000001ebc9d0000000000000000],
["village_24_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e440d144544a687495cce3953000000000009365c0000000000000000],
["village_25_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dd408344d199a658a6daed89a00000000001d36f40000000000000000],
["village_26_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e1e0031813753a62b34658b4b00000000001d47110000000000000000],
["village_27_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d000c5144155ad2a71d664ad100000000001635190000000000000000],
["village_28_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ee300214356e36e4b2e6f471200000000000ab7640000000000000000],
["village_29_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eee0011852a9390c55dada71a00000000001dbd210000000000000000],
["village_30_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d6308124e368b49a52469495300000000001da55a0000000000000000],
["village_31_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f7104300b39538e396b76abcd00000000000cc4d50000000000000000],
["village_32_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f89102082275bb629243236d900000000001198890000000000000000],
["village_33_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e320031c53961b566eddadb2500000000001e29e00000000000000000],
["village_34_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e4e000204291b4e55a08f696400000000001c36c80000000000000000],
["village_35_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d2c0c315118ea324764724b0d00000000001c69330000000000000000],
["village_36_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d810051443b095634e496aaa500000000001e47900000000000000000],
["village_37_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0d00418439a579c8646d36d300000000001e47690000000000000000],
["village_38_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000df408000b36f6544c7569bae40000000000189d5b0000000000000000],
["village_39_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000df700014426db95d124d2b90900000000001db7310000000000000000],
["village_40_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000db000000447a1ef4951b6475b00000000001cd6e90000000000000000],
["village_41_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ddc0021c224d17138a29598e300000000001e25590000000000000000],
["village_42_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f8b0534914b6b2ec86591b4dd000000000016a98e0000000000000000],
["village_43_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dfc0c0582431148995451674d00000000001e1ae30000000000000000],
["village_44_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3a111583669488c6e449a6cb00000000001dad320000000000000000],
["village_45_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e26111008170c92d69c4c992c00000000001cd8d40000000000000000],
["village_46_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d630001c3571d7acb1eb9b79b00000000001d59910000000000000000],
["village_47_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d7d05100959f332d75970924a00000000001cc8f40000000000000000],
["village_48_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d940040013b64cfd5afaad50b00000000001dab890000000000000000],
["village_49_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fa00124910ae28e375d71cb5d00000000000e37900000000000000000],
["village_50_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ea00051c3170cce296289442b00000000001e35590000000000000000],
["village_51_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000de010610e5ccbde391a76b0a6000000000015a6a20000000000000000],
["village_52_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3300b2c9492a491b524aeca600000000001258e30000000000000000],
["village_53_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d5b10e19049158ac6638598ac00000000001e52550000000000000000],
["village_54_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3e004182271c71952555b8ea00000000001d3b190000000000000000],
["village_55_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f8808114f1ad34ecb5a6fe6260000000000093ad30000000000000000],
["village_56_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e46112251245a8aeae44d489b000000000015b4ed0000000000000000],
["village_57_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3b0d200b56da71c6e27145ab00000000001e34db0000000000000000],
["village_58_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000daf09300e26d38696e3cd391d000000000011a6e90000000000000000],
["village_59_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e4101130d48e3aeda5372366900000000001e37130000000000000000],
["village_60_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000edd1020093663324b1b6ec0ab00000000001dc9230000000000000000],
["village_61_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d60101247272995c7146ed6da000000000008caa50000000000000000],
["village_62_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dc9003043391b8b4d5b9448db00000000001dbb210000000000000000],
["village_63_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dc7004183388b7ab4e34ec8d900000000001dbad80000000000000000],
["village_64_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ee310014f34d2e43b354a38cb00000000000e39350000000000000000],
["village_65_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e900d13c66962ce484c6eaae2000000000006b6550000000000000000],
["village_66_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d1810030d449e696ca175e72b0000000000173b130000000000000000],
["village_67_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4b0c134c16986ab6ac85bb2f00000000000b66e50000000000000000],
["village_68_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d320d134f5894d93d31b198da00000000001e98a40000000000000000],
["village_69_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0108610d0ca39b352492b320000000000015e8da0000000000000000],
["village_70_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e9e003009296a71eb2329c6ea00000000001f4cdd0000000000000000],
["village_71_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eff08034743743626ee49c8b000000000001eb8e20000000000000000],
["village_72_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ef6003043351b4e4b5492e99b00000000001dd9180000000000000000],
["village_73_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d000042ce292a95c96354e4ab000000000011e4960000000000000000],
["village_74_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f150000c34766b73cda6e46a100000000001e45110000000000000000],
["village_75_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d540404ca3913525b59cf48e400000000000598d30000000000000000],
["village_76_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d7b00258f1b154a645c70b92d00000000000966d40000000000000000],
["village_77_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000de400014429147a3cfd95b72c00000000001d5b200000000000000000],
["village_78_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d0810534d6921b0c55acda4b300000000001dcae20000000000000000],
["village_79_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0004358d596a61c959d646f600000000001ebd600000000000000000],
["village_80_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ff10001c3258b57ea99b24c9600000000001c37190000000000000000],
["village_81_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e8608350434b3b2cb74cb36c4000000000010bd6b0000000000000000],
["village_82_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e230125c446ee8cc71a4cc770000000000016c7a40000000000000000],
["village_83_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4800818f3b1c4a3d8f71879900000000000d1add0000000000000000],
["village_84_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dd20d2450369a71c8c4a6c92100000000000748f30000000000000000],
["village_85_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f8e0031c4275acecb5e70c6ec00000000001cc2c90000000000000000],
["village_86_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d9900d58318caae1b89d1665c00000000000da9710000000000000000],
["village_87_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d2a1060c42d354a2476a7451300000000001529af0000000000000000],
["village_88_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d2700331064d4d54b4b72c91000000000001ed49d0000000000000000],
["village_89_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f110031c72b9b92b6d4492ce300000000001e57b00000000000000000],
["village_90_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f6200324e1cadb2c6ccb5c4db00000000001259130000000000000000],
["village_91_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e240131835b512d19227622f6000000000009b71b0000000000000000],
["village_92_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0d0822c3389696292e95394a000000000015c7d60000000000000000],
["village_93_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d301125912254c5a6dd3142dc00000000001ea25c0000000000000000],
["village_94_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000efb0021433953b4da4d5936af00000000001d19280000000000000000],
["village_95_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb000d2cd43a394cda6b0b4de000000000019b9590000000000000000],
["village_96_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb000b1c329ead1552a8a24a200000000001dc7610000000000000000],
["village_97_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e4800654f48db65c25d6e465400000000001ca91a0000000000000000],
["village_98_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d070020413aa3ad4b1d72571500000000001d5b290000000000000000],
["village_99_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f7700048d2522a6a9548dd96800000000001de5640000000000000000],
["village_100_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e6505258418d6412564924b1a000000000009d92c0000000000000000],
["village_101_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d370012042ba159ba4bcf2ada00000000001ddb090000000000000000],
["village_102_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ed604f2101a9ca93cd9ca4d7300000000001eb42c0000000000000000],
["village_103_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d6a0cc403459acecd3352791c00000000001ec9240000000000000000],
["village_104_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d5d01050f5d6a615c912dc7a500000000001dcc660000000000000000],
["village_105_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e7408448e652429d8e3cda85c00000000001f152a0000000000000000],
["village_106_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e2c00718028dd9148db6e486300000000001db7910000000000000000],
["village_107_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d49093104471550d8b34f295400000000001e2cca0000000000000000],
["village_108_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f710011c52763cab953a6392300000000001e4f290000000000000000],
["village_109_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d5708428d4713508ad35626a300000000000e39660000000000000000],
["village_110_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eda003201339d71472cd6ba9c00000000001e5b690000000000000000],
["village_111_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4500020525136a372379c79b00000000001e6b510000000000000000],
["village_112_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e000521cf4ad96cc6f2d4995400000000001e59140000000000000000],
["village_113_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ec20532862916d6156791d75200000000001eb5110000000000000000],
["village_114_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e0008130638dcd2c5522f9b2400000000001c93760000000000000000],
["village_115_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e450823d017134acb23914b2b00000000000a67620000000000000000],
#village 116 I turned into a castle
["village_117_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb20512c84baa93b56491b729000000000010e9550000000000000000],
["village_118_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eac044289495a89c3935512d600000000001652e20000000000000000],
#village 119 I turned into a castle
["village_120_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d7e00020246dc31f9226ebb1500000000001d35400000000000000000],
["village_121_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e6304854444a49247548ded550000000000122ccb0000000000000000],
["village_122_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dde08d29157a66648c392951400000000000d2b620000000000000000],
["village_123_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f1411121229147723eba95a5f00000000001217150000000000000000],
["village_124_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e70003203269b926662aea75b00000000001dd9180000000000000000],
["village_125_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f5f044291186262a36cb72d1d000000000009a6da0000000000000000],
["village_126_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb70011c135128d36a49ab4d500000000001ca7180000000000000000],
["village_127_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f1600314626a992e96c9218e900000000001d46e90000000000000000],
["village_128_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e270cd00416eb48572596472400000000000db7650000000000000000],
["village_129_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f770cd203548e4d954c66cd1900000000001a4adc0000000000000000],
["village_130_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eda0132cd476e79d8ab49909900000000001ca6d60000000000000000],
["village_131_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eb51041d14d9b493921d25b2b00000000000c96dd0000000000000000],
["village_132_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f5800008e522c74b6ec8599a3000000000012cae60000000000000000],
["village_133_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dde1110ca2724b12d66865ad300000000000a32a40000000000000000],
["village_134_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d1910b5873a718942dc6f2ccd00000000000d89230000000000000000],
["village_135_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f430021023b622dd755b6ab1d00000000001ac8f20000000000000000],
["village_136_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d0d0031c329618dc8a5b9445d00000000001d39300000000000000000],
["village_137_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ee90020044da59edd266f291900000000001dd95b0000000000000000],
["village_138_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d0b08c34f5b1a6a92d971cc9a00000000000b146c0000000000000000],
["village_139_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4f09120746ac6e98956a8a9b00000000000540d30000000000000000],
["village_140_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f1b0040c22c894d373d7246e300000000001cc9200000000000000000],
["village_141_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f640041813924661d0aad475d00000000001dd7100000000000000000],
["village_142_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e37002144255c6e530d70bb9900000000001dd4d00000000000000000],
["village_143_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000de60c42455a2b56b763eea6d100000000001d9e960000000000000000],
["village_144_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e330532d15af6acc81c6a24cb00000000001259a50000000000000000],
["village_145_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e5f0000042b53b1c55c92392300000000001d7b600000000000000000],
["village_146_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d750001032722cca4d345c92c00000000001cc9110000000000000000],
["village_147_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e5200318154ab2a3894b1e4cd00000000001d94db0000000000000000],
["village_148_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f8304d1cb14db8e39694d57580000000000162b420000000000000000],
["village_149_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eb201228e3b23b6da254ecb1300000000001e5a9b0000000000000000],
["village_150_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dbf111003589d6668f285e25e00000000001daae30000000000000000],
["village_151_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dfe0005d024aab226ce75d6e300000000001dac950000000000000000],
["village_152_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f6b05100e34a58e171a7bd8ea00000000001f3a660000000000000000],
["village_153_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb900d004252352b4caa6472300000000001e37180000000000000000],
["village_154_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f3f1010092ad171c91372596400000000001c238d0000000000000000],
["village_155_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d951062c636fb8e5af3860e9f00000000001d591d0000000000000000],
["village_156_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000da30000842b1b4ccba4bee72300000000001e15090000000000000000],
["village_157_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e810d14ca1b6a6db6ab95c69a00000000001e56540000000000000000],
["village_158_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e8404118642a46ab91bb27c9f00000000001e3c560000000000000000],
["village_159_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dc70011c2359a933cb541c90a00000000001da3090000000000000000],
["village_160_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4904225166dcb1c32c0940ea000000000015291d0000000000000000],
["village_161_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e5700420126cb2dd52a6e384a00000000001dc9600000000000000000],
["village_162_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dfb0021423b496e48a155671c00000000001db9a10000000000000000],
["village_163_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fa2003182274b4bd90d91cade00000000001d55190000000000000000],
["village_164_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f050d258546dab14868ce359100000000001da6a50000000000000000],
["village_165_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f5e0c25482b0a754f1c8cd6dd00000000001199750000000000000000],
["village_166_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4f0020044692492d668e4c7100000000001d1b580000000000000000],
["village_167_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3504118f1b2c73371272346d00000000001e14a50000000000000000],
["village_168_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f4210910a25626a9653b9b6ad000000000011ba990000000000000000],
["village_169_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ed90041c5495a6ee7a44a4b4d00000000001dc5580000000000000000],
["village_170_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ee50061083645b4eaec91b91200000000001cb7b00000000000000000],
["village_171_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dfd0002012b138dbaf262155b00000000001d2ae00000000000000000],
["village_172_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3600418129096f6b238e67ab00000000001e34910000000000000000],
["village_173_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3a04348354cc8cb9f4f4b8db00000000001f58940000000000000000],
["village_174_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d0100020324d56eb6d29958ea00000000001ecba800000000000000002],
["village_175_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3100254b32db86a8d1adba9400000000001dc8940000000000000000],
["village_176_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dca001145391465d7657224dc00000000001ec9480000000000000000],
["village_177_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4b0031c5365499bd2cab36a400000000001dd6d00000000000000000],
["village_178_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eda00244a351bb1165a3aca8a00000000001d17ec0000000000000000],
["village_179_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000de000120a3b5db2b931aca70d00000000000d35710000000000000000],
["village_180_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d140d21cf5b2e95e2ee6eb92a00000000001e20770000000000000000],
["village_181_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d170d234233226ec69821b8d400000000001dcb160000000000000000],
["village_182_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000cf604004a5ad84e56e449bd7300000000001ea50c0000000000000000],
["village_183_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e7300040b48cc8a46bb4a586500000000001ed7630000000000000000],
["village_184_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e840d229055ad6a45632dc6e900000000000e44ee0000000000000000],
["village_185_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dcd00114527533134dd452b6b00000000001d25390000000000000000],
["village_186_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3c09124e30dbaec953a5448b000000000015a31c0000000000000000],
["village_187_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e8b0045010552b2db6f92a0dd00000000001234d20000000000000000],
["village_188_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000edc0d11d234ca96465c29bd2200000000001d33230000000000000000],
["village_189_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0110441227634da8ecda5b2c000000000012372b0000000000000000],
["village_190_elder","Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e400d33c5179b8534e232672200000000001d999a0000000000000000],
["village_191_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d1e0932102e9dad96ca88cae200000000001e1b310000000000000000],
["village_192_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d8711124b26dbaad55a6da30b00000000001ee30d0000000000000000],
["village_193_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f460d340427ddca4b13d49d1500000000001e56dc0000000000000000],
["village_194_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d000c1282372471356d8d396400000000001e57510000000000000000],
["village_195_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f9400118417136e68e975a2a200000000001cc5000000000000000000],
["village_196_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d190932d22c1a55d399399b2300000000001e4b230000000000000000],
["village_197_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e8704018e285c71bb5a7535b3000000000009cada0000000000000000],
["village_198_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d700d228d6ee64d190c4dd8d300000000001e4b600000000000000000],
["village_199_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb60cf18758dc8d422339c8ac00000000001e3aee0000000000000000],
["village_200_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e291122094a6275398b5138e30000000000056d6c0000000000000000],
["village_201_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dcf0cb3c1493271b28b45ad1d000000000011c90b0000000000000000],
["village_202_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d87005202395496ab5c65c92900000000001d59590000000000000000],
["village_203_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dbe08400f3c626e376b6dd71e00000000000638590000000000000000],
["village_204_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d8010c1d124d96cea6692b36200000000000e445d0000000000000000],
["village_205_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d1901258928dd7092e17a971900000000001c2d650000000000000000],
["village_206_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fad00e14033930da5154dd8cc00000000001e238c0000000000000000],
["village_207_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e99007285172b8cac64ade8de00000000001e37180000000000000000],
["village_208_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fc005229247645a456495392300000000001d6aa40000000000000000],
["village_209_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d8d0c51425d0cb168eb51bd1200000000001dc9730000000000000000],
["village_210_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e7900300f548970c412714ace00000000001d32de0000000000000000],
["village_211_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000df200149153a366d714c644cc00000000001ea4ec0000000000000000],
["village_212_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4600e14128918a095b51a5640000000000093c920000000000000000],
["village_213_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d3c00b08138d1c2e2bdaa5b1d00000000001de7e90000000000000000],
["village_214_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eec006104291a7254cba5c88200000000001d27510000000000000000],
["village_215_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000da100300336d57134de654b7400000000001c46d00000000000000000],
["village_216_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f0c1060c34911aa286c55e49a00000000001dd92e0000000000000000],
["village_217_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fff0412095622adca526a491d00000000001d67ad0000000000000000],
["village_218_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eb404b09154ac8de8cc91b96500000000001dcc540000000000000000],
["village_219_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f550062c4281db23e95acbf3400000000001cc2b50000000000000000],
["village_220_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ee500d2863b9689e8a368e492000000000010bb320000000000000000],
["village_221_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ed500314e22dc8f44e38b4524000000000012ed6a0000000000000000],
["village_222_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dd708018736658d571b76e6db00000000000d98e50000000000000000],
["village_223_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d471111c336e47434d452570c00000000001c249b0000000000000000],
["village_224_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ec60d130f5b0ec9bb936b5c2900000000000d38cb0000000000000000],
["village_225_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e400811c136e466c71d25c37500000000001e68c40000000000000000],
["village_226_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d9d0912c5551ba8a4daa65ca3000000000011469a0000000000000000],
["village_227_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000ef600b5084a61db30eb0ed70a00000000000dc25a0000000000000000],
["village_228_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000f60050344315391b9dba9e84300000000001d575a0000000000000000],
["village_229_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fb104c144359d509a649198d5000000000011d68b0000000000000000],
["village_230_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000002510d58f46c572c39cb1b96200000000001ebae40000000000000000],
["village_231_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000076411658e36db6db6db6db6db00000000001db6db0000000000000000],
["village_232_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dcb10329104dc6932998a24ab00000000001da5330000000000000000],
["village_233_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000de911321136c965b363b1a2e300000000001c92920000000000000000],
["village_234_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000e3f0d110b6a134e46e5a9371e00000000001d12e50000000000000000],
["village_235_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000fff0d2348349a51c14ff998e900000000001cbaa40000000000000000],
["village_236_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000eae0041831aa4b237ab71c75300000000001cc35b0000000000000000],
["village_237_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000db705158247216e099d8db8d100000000001f496b0000000000000000],
["village_238_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000a3f001451779b7346d849e4ad00000000001ecbcd0000000000000000],
["village_239_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000076c0d22d03ae99149eb70395b00000000001e081b0000000000000000],
["village_240_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000075f00320b27228aa52595949600000000001192a40000000000000000],
["village_241_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000770091282344d4a5f1c864a5c00000000001db5330000000000000000],
["village_242_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d2f0404d11485a9a6ea2e688b00000000001e46f20000000000000000],
["village_243_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000df2103343568bc9b303b1baeb00000000001ee4cd0000000000000000],
["village_244_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000007450cc4101cca4a3b63793a9900000000001d13730000000000000000],
["village_245_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000dbf0d1191255d51e322b603ac00000000001e33940000000000000000],
["village_246_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000007400ce202249476aaa36ed74300000000001ec8da0000000000000000],
["village_247_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x000000002100b1c64d556d38e1ca36a200000000001728d10000000000000000],
["village_248_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d500961873ae87132deb24cfc00000000001e6ce30000000000000000],
["village_249_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d440544c33e5b869b14ae4ca5000000000015a9330000000000000000],
["village_250_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d720cd5071b29ae6b23add924000000000012d6e40000000000000000],
["village_251_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d490902ca271985275186569900000000001e13640000000000000000],
["village_252_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d7d0cb1d12834506c2393c72d00000000001e28cc0000000000000000],
["village_253_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d4400834c1bacd1c92c2eab2400000000001741220000000000000000],
["village_254_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d6b00d1c33d2a6da7377ae30c00000000000ecb0a0000000000000000],
["village_255_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d690cb142429b2ddb196a56ad00000000001f46e10000000000000000],
["village_256_elder", "Local_Leader", "{!}village_1_elder",tf_hero|tf_is_merchant, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0x0000000d660931c1446dee38db915b1a00000000001dece60000000000000000],

# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

#Used for player enterprises
["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x000000000a1013ce56938e4865313762000000000009b5190000000000000000],
["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x000000041100254e355489c69a4a374c00000000001e98eb0000000000000000],
["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x000000002d003009270c552c696da51400000000001e3aca0000000000000000],
["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x00000000290cd18854ab79185d91ab2100000000001e56db0000000000000000],
["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x00000009d100118a0919d318ea45a86200000000001eb94b0000000000000000],
["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x00000009e205344e54e1c4168835b2e400000000001ed5520000000000000000],
["town_12_master_craftsman", "{!}Town 12 Craftsman", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(2),wp(20),knows_common, 0x00000009c80c120b08ac6ab364b156e200000000001eb85c0000000000000000],
["town_13_master_craftsman", "{!}Town 13 Craftsman", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],  def_attrib|level(2),wp(20),knows_common, 0x00000009ee04125244ed2f1d244956d200000000000ad31d0000000000000000],
["town_14_master_craftsman", "{!}Town 14 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
["town_15_master_craftsman", "{!}Town 15 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000007430c01d244e28aa72252131900000000001f571b0000000000000000],
["town_16_master_craftsman", "{!}Town 16 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000771011152695a4daa9caea68b00000000000de11b0000000000000000],
["town_17_master_craftsman", "{!}Town 17 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000007601062c424f253bcdb75d75d00000000001148cc0000000000000000],
["town_18_master_craftsman", "{!}Town 18 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000e4b00b2c25b5d92bbb4b618f300000000000ddaa50000000000000000],
["town_19_master_craftsman", "{!}Town 19 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
["town_20_master_craftsman", "{!}Town 20 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
["town_21_master_craftsman", "{!}Town 21 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002911034d36f2c894d295897400000000000d386a0000000000000000],
["town_22_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
["town_23_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000a08d44b47555618e452970b0000000000125ad30000000000000000],
["town_24_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000311231038f169caadc9d35b00000000001d3acc0000000000000000],
["town_25_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000150914472ba369ea9c64376300000000001e48a30000000000000000],
["town_26_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003c0832433712972354496d9300000000001e44dc0000000000000000],
["town_27_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003f10134c570b75595382e56c00000000001f34b50000000000000000],
["town_28_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000e10550c4ba2b1bad349b75c00000000001d95010000000000000000],
["town_29_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000300f5c169b2ca34dcb2b71b00000000001d345c0000000000000000],
["town_30_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000180c71c0573e6e66e49add6b00000000001e31a20000000000000000],
["town_31_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000030cb14336e3645d128f5a2100000000001e48ab0000000000000000],
["town_32_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001a08d44632e3565899aa56ea00000000001d59230000000000000000],
["town_33_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002609154b372cba194b556af200000000001cb4e90000000000000000],
["town_34_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000038051003395cae28dcaa96e600000000001d365b0000000000000000],
["town_35_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000009100589334d94b49d56bcb100000000001197560000000000000000],
["town_36_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000030c614456d34de8da5b38a400000000001ec7630000000000000000],
["town_37_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003b0515826aaf29cb5a6dcf6d00000000001d36db0000000000000000],
["town_38_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003208644134a472d6934ab4dc00000000001e95690000000000000000],
["town_39_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002401058528e643675d5538db00000000001f28e20000000000000000],
["town_40_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001c10424436d5f13c14273d1400000000001cf68c0000000000000000],
["town_41_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003f0d329239146dc8e3aedc9b00000000001e68ec0000000000000000],
["town_42_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002c04118747756617528d6a7c00000000001d868c0000000000000000],
["town_43_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001309130d4b1e75293e6d969200000000001ee9150000000000000000],
["town_44_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000015011288391caf490bd2371300000000001dc8b30000000000000000],
["town_45_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x0000000000100341481b6e2893b1c66a00000000001d6b130000000000000000],
["town_46_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000003d0d2008669c25b5559246c200000000001f55120000000000000000],
["town_47_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x00000000200cb18a5723b1a3148dc45500000000001dab920000000000000000],
["town_48_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000d08e14b47a36aa46333366200000000001d34d90000000000000000],
["town_49_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000000d051290543149e66d3226ad00000000001d329b0000000000000000],
["town_50_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000002f10b341396b4a6c9b53445900000000001e26c90000000000000000],
["town_51_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001f1083883704a9a4a2ba24a400000000001d231b0000000000000000],
["town_52_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],    def_attrib|level(2),wp(20),knows_common, 0x000000001204d344659ab1a712ae5b1600000000001de3360000000000000000],

# Chests
["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_jewelry,itm_arminius_spatha,itm_arminius_mask],def_attrib|level(18),wp(60),knows_common,0],
["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral, [itm_dagger],def_attrib|level(18),wp(60),knows_common, 0],
#SB : move samurai back to Rivacheg (other chests were inaccessible
["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_dragon_arrows, itm_dragon, itm_temple_gold, itm_temple_gold, itm_jewelry, itm_silver, itm_silver, itm_silver, itm_ivory],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_temple_gold,itm_temple_gold,itm_temple_gold,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_ivory,itm_ivory,itm_ivory,itm_ivory,itm_khopesh1],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_velvet],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_4","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_wine,itm_wine,itm_raw_grapes,itm_aegis,itm_maske],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_5","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_gallic_spear_4,itm_jewelry],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_6","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_caesars_sword,itm_jewelry],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_7","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_velvet],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_8","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_velvet],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_9","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt,itm_salt],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_10","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_temple_gold],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_11","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_temple_gold],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_12","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_velvet,itm_laurel_gold,itm_laurel_silver,itm_roman_rich_emperor,itm_roman_rich_emperor_2],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_13","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_velvet,itm_female_crown,itm_roman_female_augusta,itm_roman_female_augusta_2,itm_seiden_dress],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_14","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_temple_gold,itm_temple_gold],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_15","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver,itm_silver],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_16","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry,itm_temple_gold],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_17","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_jewelry, itm_parthian_female_hat],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["bonus_chest_18","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_female_slave1,itm_female_slave2,itm_female_slave3,itm_female_slave4],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts.
["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],

["province_array","{!}province_array","{!}province_array",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],

#used for racing games and olympia
["temp_array_olympia_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
["temp_array_olympia_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
["temp_array_olympia_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
["olympia_participants","{!}olympia_participants","{!}olympia_participants",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10, 0],
##END racing games and olympia

["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

# Add Extra Quest NPCs below this point
["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,
[],attrib_level_12,wp(60),knows_level_6, white_face_21, white_face_22],
["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
[],def_attrib|level(4),wp(60),knows_common,white_face_21,white_face_22],
["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
[],def_attrib|level(4),wp(60),knows_common,white_face_11,white_face_12],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_linen_tunic, itm_caligea, itm_roman_poor1,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5, itm_roman_poor2, itm_dagger, itm_roman_gladius],def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,white_face_11,white_face_12],

#SB : adjust drunk swords, 1 from each faction type
["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[],attrib_level_16,wp(120),knows_level_12,bandit_face1,bandit_face2],

["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_bosporan_light4,itm_caligea,itm_dagger,itm_cloak],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],

["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_neutral,[itm_generic_poor2,itm_simple_hood_2,itm_leather_boots,itm_horse_2,itm_leather_gloves,itm_dagger],def_attrib|agi_11|level(20),wp(130),knows_common,white_face_21,white_face_22],

["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_generic_poor2,itm_simple_hood_2,itm_leather_boots,itm_horse_1,itm_leather_gloves,itm_dagger],def_attrib|agi_11|level(10),wp(130),knows_common,white_face_21,white_face_22],

["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,[itm_robe,itm_black_hood,itm_celtic_boots],def_attrib|level(4),wp(60),knows_common,woman_face_1,woman_face_2],
["temporary_minister","Minister Septimus Homunculus","Minister Septimus Homunculus",
tf_hero,0,reserved,fac_commoners,[itm_roman_toga,itm_caligea],def_attrib|level(4),wp(60),knows_common,0x0000000ffe012009072b2dd2b3aa371d00000000001de95d0000000000000000],

["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

# ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#Player history array
["log_array_entry_type",   "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_entry_time",   "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_actor",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_center_object","{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_troop_object", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],
["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, white_face_11, white_face_12],

["quick_battle_troop_1", "Eques", "Eques", tf_hero, no_scene, reserved, fac_gladiators, [itm_graves_simple_2,itm_hasta2,itm_eastern_sowrd1,itm_horse_3,itm_simple_thraex_shield,itm_iberian_light6,itm_tourney_helm_green], str_9|agi_15|int_12|cha_12|level(15), wpex(109,33,132,15,32,100), knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_3, 0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000 ],
["quick_battle_troop_2", "Gladiatrix", "Gladiatrix", tf_female|tf_hero, no_scene, reserved, fac_gladiators, [itm_tourney_helm_red,itm_eastern_sowrd1,itm_arena_shield_green], str_12|agi_14|int_11|cha_18|level(22), wpex(182,113,112,159,82,115), knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4|knows_power_throw_5, woman_face_1, woman_face_2 ],
["quick_battle_troop_3", "Thraex", "Thraex", tf_hero, no_scene, reserved, fac_gladiators, [itm_graves_simple_2,itm_flax_onehanded1,itm_leather_covered_round_shield,itm_arena_armor_blue,itm_tourney_helm_green], str_18|agi_16|int_12|cha_11|level(24), wpex(90,152,102,31,33,34), knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6|knows_power_throw_6, 0x000000018000324428db8a431491472400000000001e44a90000000000000000 ],
["quick_battle_troop_4", "Retiarius", "Retiarius", tf_hero, no_scene, reserved, fac_gladiators, [itm_graves_simple_2,itm_arena_armor_green,itm_dagger,itm_dreizack2], str_18|agi_15|int_12|cha_12|level(24), wpex(130,150,130,30,50,90), knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6|knows_power_throw_7, 0x000000081700205434db6df4636db8e400000000001db6e30000000000000000,  ],
["quick_battle_troop_5", "Murmillo", "Murmillo", tf_hero, no_scene, reserved, fac_gladiators, [itm_graves_simple_2,itm_roman_gladius,itm_arena_shield_blue,itm_arena_armor_red,itm_tourney_helm_yellow], str_15|agi_15|int_12|cha_12|level(21), wpex(110,130,110,80,15,110), knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5|knows_power_throw_8, 0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, ],
["quick_battle_troop_6", "Sagittarius", "Sagittarius", tf_hero, no_scene, reserved, fac_gladiators, [itm_tourney_helm_red,itm_dagger,itm_arena_armor_yellow,itm_arrows,itm_persian_bow,itm_graves_simple_2], str_12|agi_15|int_15|cha_9|level(18), wpex(70,70,100,140,15,100), knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_strike_2|knows_ironflesh_2|knows_power_throw_9, 0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000,  ],

["quick_battle_troop_7", "Spartacus", "Spartacus", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_roman_gladius,itm_roman_spatha,itm_simple_thraex_shield,itm_legion_hamata_cape_1,itm_graves_simple_2,itm_horse_3,itm_hasta3], str_30|agi_30|int_15|cha_12|level(21), wpex(300,300,300,300,300,300), knows_horse_archery_2|knows_riding_2|knows_athletics_10|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_10|knows_ironflesh_10|knows_power_throw_10, 0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000,  ],
["quick_battle_troop_8", "Boudica", "Boudica", tf_female|tf_hero, no_scene, reserved, fac_kingdom_1, [itm_horse_1,itm_celtic_sowrd2,itm_celtic_round_shild2,itm_war_spear,itm_leather_boots,itm_celtic_light8], str_30|agi_30|int_12|cha_12|level(18), wpex(200,200,200,200,200,200), knows_ironflesh_10|knows_horse_archery_2|knows_riding_6|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2|knows_power_throw_10, 0x00000000000010423ba971aa93c5b16900000000001d985a0000000000000000,  ],
["quick_battle_troop_9", "Germanicus", "Germanicus", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_roman_gladius,itm_roman_spatha,itm_officer_shield,itm_roman_legatus_helm,itm_musculata_legatus_3,itm_graves_simple_2,itm_horse_3], str_30|agi_20|int_12|cha_14|level(26), wpex(230,230,230,230,230,230), knows_horse_archery_2|knows_riding_6|knows_athletics_7|knows_shield_6|knows_weapon_master_9|knows_power_draw_7|knows_power_strike_3|knows_ironflesh_4|knows_power_throw_10, 0x000000002c00300918a371ff9a8dcaa200000000001e286b0000000000000000,  ],
["quick_battle_troop_10", "Jugurtha", "Jugurtha", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_armor_of_african_gods,itm_caligea,itm_leather_covered_round_shield,itm_throwing_spears,itm_war_spear,itm_arabian_horse_a,itm_1_imp_gallic_f_plume], str_30|agi_20|int_14|cha_20|level(28), wpex(200,200,200,200,200,200), knows_ironflesh_10|knows_power_strike_10|knows_riding_10|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5|knows_power_throw_10, 0x000000003f0072ca379b6e976c97b2f100000000001cbccb0000000000000000,  ],

["global_variables","trp_global_variables","trp_global_variables", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

###QUEST CHARACTERS
["roman_start_merchant", "Gaius Lucarius", "Gaius Lucarius", tf_hero|tf_male, 0, reserved, fac_kingdom_7, [itm_roman_toga, itm_caligea, itm_roman_gladius],
def_attrib|level(10),wp(100),knows_common, 0x000000055d00c00446e476a6d632c66200000000001ee7540000000000000000],
["superbus", "Superbus", "Superbus", tf_hero, 0, reserved, fac_kingdom_5, [itm_roman_poor1, itm_caligea, itm_roman_gladius],
attrib_level_26,wp(100),knows_level_26, 0x00000000351020124761fcfd1daf4d9600000000001f7f3e0000000000000000, 0x00000000351020124761fcfd1daf4d9600000000001f7f3e0000000000000000],
["avaritia", "Avaritia", "Avaritia", tf_hero|tf_female, 0, reserved, fac_kingdom_1, [itm_caligea, itm_female_2],
def_attrib|level(2),wp(5),knows_common, 0x000000003f00e00256107de16c6de35900000000001d21d70000000000000000, 0x000000003f00e00256107de16c6de35900000000001d21d70000000000000000],
["quest_miles", "Miles", "Miles", tf_hero, 0, reserved, fac_kingdom_2,
[itm_roman_poor1, itm_caligea, itm_roman_gladius],
attrib_level_26,wp(140),knows_level_26, 0x00000000301010033e9170badabac95d00000000001f16620000000000000000, 0x00000000301010033e9170badabac95d00000000001f16620000000000000000],
["quest_primus_pilus", "Primus Pilus", "Primus Pilus", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3,
[itm_officer_shield,itm_roman_gladius,itm_cenutrio_legion_squamata_1,itm_centurio_east_graves,itm_centurio_helm_1],
attrib_level_31,wp(160),knows_level_31, roman_face1, roman_face2],
["quest_centurio_primus", "Centurio Primi Ordinis", "Centurio primi Ordinis", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6,
[itm_officer_shield,itm_roman_gladius,itm_cenutrio_legion_hamata_4,itm_centurio_east_graves,itm_centurio_helm_2],
attrib_level_31,wp(160),knows_level_31, roman_face1, roman_face2],
["quest_tiro","Tiro","Tiro",tf_hero|tf_randomize_face, 0,0, fac_commoners,[],
attrib_level_23,wp(20),knows_inventory_management_10,roman_face1, roman_face2],

##STARTING QUEST CHARACTER
["looter_leader", "Robber", "Looters", tf_hero|tf_male, no_scene, reserved, fac_outlaws,
[itm_hand_axe,itm_rawhide_coat,itm_leather_boots,itm_stones], def_attrib|level(4), wp(20), knows_common, 0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2 ],
["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,[itm_roman_poor4,itm_caligea],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000000320410022d2595495491afa400000000001d9ae30000000000000000,mercenary_face_2],

##DIPLOMACY STAFF MEMEMBER
["dplmc_chamberlain", "Quaestor", "Quaestor", tf_male|tf_hero, no_scene, reserved, fac_commoners,
[], def_attrib|level(10), wp(40), knows_inventory_management_10, 0x0000000a8a10d00437248ca3aeaa269c00000000001dd7ad0000000000000000 ],

["dplmc_constable", "Custos Publicus", "Custos Publicus", tf_male|tf_hero, no_scene, reserved, fac_commoners,
[], knight_attrib_4, wp_melee(200), knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4, 0x00000001810d115138968dc64c6da56100000000001e38a50000000000000000 ],

["dplmc_chancellor", "Censor", "Censor", tf_male|tf_hero, no_scene, reserved, fac_commoners,
[], def_attrib|level(10), wp(40), knows_inventory_management_10, 0x0000000196043009571252b6d1712ae200000000001d15330000000000000000 ],

["dplmc_messenger", "Messenger", "Messengers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral,
[itm_roman_townguard_helm,itm_roman_spatha,itm_horse_2,itm_legion_squamata_13,itm_graves_simple_2], def_attrib|agi_21|int_30|cha_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7, celtic_face_21, celtic_face_22 ],

["dplmc_scout", "Scout", "Scouts", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral,
[itm_graves_simple,itm_legion_hamata_7,itm_roman_townguard_helm,itm_roman_spatha,itm_horse_2], def_attrib|agi_21|int_30|cha_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7, germanic_face_11, germanic_face_12 ],


# # recruiter kit begin
# ["dplmc_recruiter", "Recruiter", "Recruiter", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral,
# [itm_roman_townguard_helm,itm_graves_simple_2,itm_legion_hamata_cape_4,itm_roman_spatha,itm_horse_2], def_attrib|agi_21|int_30|cha_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7, white_face_11, white_face_12 ],
# # recruiter kit end
##diplomacy end


["slave", "Male Slave", "Male Slaves", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_roman_poor1,itm_roman_poor3,itm_roman_poor2,itm_caligea,itm_knife,itm_butchering_knife], def_attrib|level(25), wp(30), knows_common|knows_riding_2, white_face_11, white_face_12 ],
["slave_mine", "Male Slave", "Male Slaves", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves, no_scene, reserved, fac_commoners, [itm_roman_poor1,itm_roman_poor2,itm_caligea,itm_pickaxe_work], def_attrib|level(25), wp(30), knows_common|knows_riding_2, white_face_21, white_face_22 ],
["slave_female", "Female Slave", "Female Slaves", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_female_1_barb,itm_female_2_barb,itm_female_3_barb,itm_female_1,itm_female_2,itm_female_3,itm_caligea,itm_knife,itm_butchering_knife], def_attrib|level(15), wp(30), knows_common|knows_riding_2, woman_face_1, woman_face_2 ],

###orgie, for pleasure and bacchus
["orgie_fem1","Salvation","Salvation",tf_female|tf_hero,0,0,fac_commoners,
[itm_female_slave3,itm_female_slave4,itm_female_slave2,itm_nothing_legs],def_attrib|level(5),wp(30),knows_common|knows_riding_2,dancer_face1,dancer_face2],

["orgie_fem2","Participant in an orgy","Participants in an orgy",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_female_slave3,itm_female_slave4,itm_female_slave2,itm_nothing_legs],def_attrib|level(5),wp(30),knows_common|knows_riding_2,dancer_face_african1,dancer_face_african2],

["orgie_fem3","Participant in an orgy","Participants in an orgy",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_female_slave3,itm_female_slave4,itm_female_slave2,itm_nothing_legs],def_attrib|level(5),wp(30),knows_common|knows_riding_2,dancer_face_eastern1,dancer_face_eastern2],

["orgie_fem4","Incontinentia Buttocks","Incontinentia Buttocks",tf_female|tf_hero,0,0,fac_commoners,
[itm_new_dress_4,itm_female_caligea_gold],def_attrib|level(5),wp(30),knows_common|knows_riding_2,dancer_face1,dancer_face2],

["orgie_male1","Participant in an orgy","Participants in an orgy",tf_male|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_caligea,itm_roman_toga,itm_roman_poor2,itm_roman_poor1,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5],def_attrib|level(5),wp(30),knows_common|knows_riding_2,white_face_21,white_face_22],

["dancer1","Dancer","Dancers",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_female_slave3,itm_female_slave4,itm_female_slave2,itm_nothing_legs],def_attrib|level(5),wp(30),knows_common|knows_riding_2,
  dancer_face_african1,dancer_face_african2],

["orgie_male1_kissing","Noble","Noble",tf_male|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_sarranid_cloth_robe_fancy_1,itm_sarranid_cloth_robe_fancy_2,itm_sarranid_cloth_robe_fancy_3,itm_caligea],def_attrib|level(5),wp(30),knows_common|knows_riding_2,white_face_11,white_face_12],

["orgie_fem_kissing","Dancer","Dancer",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
[itm_female_slave2,itm_female_slave3,itm_female_slave4,itm_nothing_legs],def_attrib|level(5),wp(30),knows_common|knows_riding_2,dancer_face_eastern1,dancer_face_eastern2],

######
["tavern_npc1", "Tavern Patron", "Tavern Patrons", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral,
[itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_roman_poor2,itm_roman_poor1,itm_caligea,itm_celtic_boots], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2, white_face_11, white_face_12 ],
["tavern_npc1_afr", "Tavern Patron", "Tavern Patrons", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral,
[itm_judean_tunic_1,itm_judean_tunic_2,itm_judean_tunic_3,itm_judean_tunic_4,itm_judean_tunic_5,itm_judean_tunic_6,itm_sarranid_cloth_robe,itm_sarranid_felt_hat,itm_caligea,itm_leather_boots], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2, african_face_younger, african_face_older ],
["tavern_npc1_arab", "Tavern Patron", "Tavern Patrons", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral,
[itm_sarranid_cloth_robe_b,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_c,itm_headcloth,itm_caligea,itm_celtic_boots,itm_arabian_tunic_1,itm_arabian_tunic_2,itm_arabian_tunic_3], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2, arab_face_young, arab_face_old ],
["whore","Lupa","Lupae",tf_female|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
[itm_caligea,itm_roman_lupa_dress,itm_roman_lupa_dress_2,itm_roman_lupa_dress_3],def_attrib|level(12),wp(100),knows_common,girl_face1,girl_face2],
["groupie","Groupie","Groupies",tf_female|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
[itm_caligea,itm_roman_lupa_dress,itm_roman_lupa_dress_2,itm_roman_lupa_dress_3],def_attrib|level(12),wp(100),knows_common,girl_face1,girl_face2],

["guest", "Civis", "Civis", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+roman_cives+roman_foot_peasant,
def_attrib|level(4), wp(60), knows_common, roman_face1, roman_face2 ],
["guest_female", "Civis", "Civis", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[]+roman_foot_peasant+roman_dress_cives,
def_attrib|level(4), wp(60), knows_common, woman_face_1, woman_face_2 ],

["roman_priest_female","Sacerdos","Sacerdotes", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
[itm_roman_noble_shawl_1,itm_roman_noble_shawl_2,itm_roman_noble_shawl_3,itm_roman_noble_shawl_4,itm_roman_noble_shawl_5]+roman_foot_peasant+roman_dress_cives,
def_attrib|level(4), wp(60), knows_common, woman_face_1, woman_face_2 ],
["roman_priest","Sacerdos","Sacerdotes",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
[itm_simple_hood_4]+roman_foot_cives+roman_cives,
def_attrib|level(5),wp(30),knows_common,roman_face1,roman_face2],
["jewish_priest","Kohen","Kohanim",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_caligea, itm_robe],def_attrib|level(5),wp(60),knows_common,eastern_man_face_old_1,eastern_man_face_older_2],
["christian_priest","Priest","Priests",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_caligea, itm_robe],def_attrib|level(5),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["norse_priest","Gudjaen","Gudjaeniz",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_celtic_boots, itm_germanic_light1, itm_germanic_light2,itm_germanic_light5, itm_germanic_light9, itm_sax1],
attrib_level_12,wp(150),knows_level_12,barbarian_man_face_old_1,barbarian_man_face_older_2],
["celtic_druid","Draid","Draoidhean",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_celtic_boots,itm_celtic_sowrd2,itm_celtic_sowrd1,itm_celtic_sowrd3, itm_celtic_light8,itm_celtic_light1,itm_celtic_light2,itm_celtic_light3,itm_celtic_light4,itm_celtic_light5,itm_celtic_light6,itm_celtic_light7],
attrib_level_12,wp(100),knows_level_12,barbarian_man_face_old_1,barbarian_man_face_older_2],
["dacian_priest","Dacian Priest","Dacian Priest",tf_male_barbarian|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_celtic_boots, itm_dacian_light11, itm_dacian_light10,itm_dacian_light5, itm_dacian_light3, itm_dacian_sword],
attrib_level_12,wp(100),knows_level_12,barbarian_man_face_old_1,barbarian_man_face_older_2],
["sarmatian_priest","Sky-Priest","Sky-Priest",tf_male|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_sarmatian_shoes, itm_kaftan_1, itm_kaftan_2,itm_kaftan_3, itm_sarmatian_cap_2, itm_sarmatian_cap_1, itm_sarmatian_ringsword_1],
attrib_level_12,wp(100),knows_level_12,scythian_face_11,scythian_face_12],
["caucasian_priest","Kadagi","Kadagi",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_sarmatian_shoes, itm_caucasian_axe_1] + caucasian_dress_peasant,
attrib_level_12,wp(100),knows_level_12, woman_face_1, woman_face_2],
["armenian_priest","Priest","Priest",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_sarmatian_shoes, itm_armenian_axe_1] + eastern_armor_tunics_armenian,
attrib_level_12,wp(100),knows_level_12,eastern_man_face_young_1,eastern_man_face_older_2],
["persian_priest","Mobad","Mobad",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_eastern_shoe_b,itm_eastern_shoe_r,itm_dagger_parthian_1,itm_dagger_parthian_2] + eastern_armor_tunics_persian,
attrib_level_12,wp(100),knows_level_12,eastern_man_face_young_1,eastern_man_face_older_2],
["arabian_priest","Afkal","Afkal",tf_male_eastern|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
[itm_eastern_shoe_b,itm_eastern_shoe_r, itm_dagger] + desert_tunic,
attrib_level_12,wp(100),knows_level_12,eastern_man_face_young_1,eastern_man_face_older_2],
["berber_priest","Berber Priest","Berber Priest",tf_guarantee_boots|tf_guarantee_armor|tf_male_north_african,0,0,fac_commoners,
[itm_caligea, itm_dagger] + berber_cives,
attrib_level_12,wp(100),knows_level_12,north_african_man_face_middle_1,north_african_man_face_older_2],
["garamantian_priest","Ammon Priest","Ammon Priest",tf_guarantee_boots|tf_guarantee_armor|tf_male_north_african,0,0,fac_commoners,
[itm_caligea, itm_dagger] + garamantian_cives,
attrib_level_12,wp(100),knows_level_12,north_african_man_face_middle_1,north_african_man_face_older_2],
["nubian_priest","Ammon Priest","Ammon Priest",tf_guarantee_boots|tf_guarantee_armor|tf_male_black,0,0,fac_commoners,
[itm_caligea, itm_dagger] + garamantian_cives,
attrib_level_12,wp(100),knows_level_12,nubian_man_face_old_1, nubian_man_face_older_2],

["healer", "Physican", "Physicans", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners,
[itm_caligea,itm_robe], def_attrib|str_15|level(4), wp(60), knows_common, white_face_11, white_face_12 ],
["healer_2", "Physican", "Physicans", tf_hero|tf_randomize_face, no_scene, reserved, fac_commoners,
[itm_caligea,itm_robe], def_attrib|str_15|level(4), wp(60), knows_common, white_face_21, white_face_22 ],
["guest_sitting", "Civis", "Civis", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_poor1,itm_roman_poor2,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_roman_toga],
def_attrib|level(4), wp(60), knows_common, white_face_11, white_face_12 ],

["norse_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_deserters,
[itm_dacian_naked5,itm_dacian_naked6,itm_dacian_naked7,itm_dacian_naked8,itm_dacian_naked3,itm_dacian_pileus_a_1,itm_dacian_pileus_a_2,itm_dacian_pileus_b_1,itm_dacian_pileus_b_2,itm_dacian_shield_small5,itm_dacian_shield_small6,itm_dacian_shield_small4,itm_dacian_sword,itm_flax_onehanded1,itm_flax_onehanded2,itm_leather_boots],
attrib_level_26, wp(160), knows_level_26, mercenary_face_greek_1, mercenary_face_greek_2 ],
["briton_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_deserters,
[itm_leather_boots,itm_celtic_light6,itm_celtic_light7,itm_celtic_light8,itm_celtic_light2,itm_celtic_light1,itm_celtic_axe4,itm_celtic_long_shild1,itm_celtic_long_shild3,itm_celtic_long_shild2,itm_celtic_round_shild2],
attrib_level_26, wp(160), knows_level_26, celtic_face_11, celtic_face_12 ],
["saxon_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_deserters,
[itm_steppe_horse_1,itm_sarmatian_light3,itm_sarmatian_light4,itm_sarmatian_light2,itm_sarmatian_light1,itm_kopfband,itm_scythian_shield_cav2,itm_scythian_shield_cav3,itm_sarmatian_ringsword_1,itm_bodkin_arrows,itm_persian_bow,itm_eastern_shoe]+sarmatian_helm_spangen,
attrib_level_26, wp(160), knows_level_26, scythian_face_21, scythian_face_22 ],
["scotch_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_deserters,
[itm_celtic_boots,itm_germanic_light4,itm_germanic_light7,itm_germanic_naked6,itm_germanic_axe1,itm_germanic_axe3,itm_germanic_shield_large10,itm_germanic_shield_large11,itm_germanic_shield_large6,itm_germanic_shield_large2,itm_war_spear,itm_throwing_spears],
attrib_level_26, wp(160), knows_level_26, germanic_face_11, germanic_face_12],
["angle_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm, no_scene, reserved, fac_deserters,
[itm_throwing_spears_east,itm_military_hammer]+eastern_boots_light+eastern_armor_furarmor+parthian_helm_phyrgian+scythian_shields_2+eastern_sword_short,
attrib_level_26, wp(160), knows_level_26, persian_face_young, persian_face_middle ],
["irish_deserter", "Deserter", "Deserters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_deserters,
[itm_roman_gladius,itm_hasta2,itm_roman_townguard_helm,itm_graves_simple_2,itm_legion_hamata_cape_5,itm_cetratus_aux_3,itm_cetratus_aux_7,itm_cetratus_aux_5],
attrib_level_26, wp(160), knows_level_26, roman_face1, roman_face2 ],
["asturias_veteran", "Ghost", "Ghosts", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners,
[itm_caligea,itm_dagger,itm_roman_poor1,itm_roman_poor2], knight_attrib_5|level(31), wp(380), knows_level_31, white_face_21, white_face_22 ],

["greek_scholar", "Archippus the Scholar", "Archippus the Scholars", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x0000000e3f00d20136db8db6db6db7ef00000000001e005a0000000000000000],
["roman_scholar", "Marcus Gaius Cassius", "Marcus Gaius Cassius", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x00000008ff00300956dd95b6db6db6db00000000001c82a20000000000000000],
["military_adviser", "Titus Livius, Military Adviser", "Titus Livius", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x00000007d90c300854ed49a74b46c79e00000000000347200000000000000000],
["financial_adviser", "Primus Horatius, Financial Adviser", "Primus Horatius", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x00000007e4083011571db5f4ac9ab2ea00000000000f450e0000000000000000],
["diplomatic_adviser", "Servius Sextus, Political Adviser", "Servius Sextus", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x00000007ee0c10093b25d9ad65023aa600000000001e36d30000000000000000],

["diplomat_parthia", "Arsaces", "Diplomats", tf_hero, no_scene, reserved, fac_kingdom_6,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x000000074000c21137547356db6db6db00000000001db0db0000000000000000],
["diplomat_eastern", "Kashta", "Diplomats", tf_hero, no_scene, reserved, fac_neutral,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x000000003f0070005cdc7407dfefe6db00000000001e0edc0000000000000000],
["diplomat_africa", "Gar Daram Senur", "Diplomats", tf_hero, no_scene, reserved, fac_garamantes,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x00000003bf0070005adb6d9396aff6db00000000001db6d30000000000000000],
["diplomat_india", "Kanishka", "Diplomats", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common,  0x000000003f00b08e36db6db6db6db6db00000000001db6db0000000000000000],
["housholder", "Housekeeper", "Housekeepers", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_rich1,itm_roman_rich2,itm_roman_toga], def_attrib|level(4), wp(60), knows_common, 0x000000018000301234dd6eb6db6db6db00000000001c94db0000000000000000],

#this are lists
["player_camp_chest_1","player_camp_chest_1","player_camp_chest_1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
["player_camp_chest_2","player_camp_chest_2","player_camp_chest_2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
["player_camp_chest_3","player_camp_chest_3","player_camp_chest_3",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(180),knows_inventory_management_10,0],
["player_camp_chest_end","player_camp_chest_end","player_camp_chest_end",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],

#ancient heroes
["sisyphus", "Sisyphus", "Sisyphus", tf_hero, no_scene, reserved, fac_commoners,
[itm_ancient_helm_light,itm_roman_poor4], def_attrib|level(4), wp(60), knows_common,
0x00000000020032446d63ae5b0e7759a400000000001e48c50000000000000000],
["herakles", "Herakles", "Herakles", tf_hero, no_scene, reserved, fac_commoners,
[itm_throwing_spears,itm_ancient_boots_heavy,itm_ancient_plate_armor2,itm_aslans_fur,itm_ancient_axe,itm_ancient_shield,itm_leather_gloves],
hero_attrib|level(50), wp(400), knows_hero, 0x00000005bc0c028f1d1b8dc7254ea49d00000000001d98740000000000000000],
["achilleus", "Achilleus", "Achilleus", tf_hero, no_scene, reserved, fac_commoners,
[itm_throwing_spears,itm_leather_gloves,itm_ancient_boots_heavy,itm_aslans_fur,itm_ancient_plate_armor,itm_ancient_spear,itm_ancient_shield,itm_ancient_sword],
hero_attrib|level(50), wp(600), knows_hero, 0x000000003a080291346c69a85e6d2a9c00000000001e5b5b0000000000000000],
["agamemnon", "Agamemnon", "Agamemnon", tf_hero, no_scene, reserved, fac_commoners,
[itm_throwing_spears,itm_leather_gloves,itm_ancient_helm_heavy,itm_ancient_boots_heavy,itm_ancient_shield,itm_ancient_axe,itm_ancient_plate_armor],
hero_attrib|level(50), wp(210), knows_hero, 0x0000000afb04034e36db6db6db6db6db00000000001db6db0000000000000000],
["odysseus", "Odysseus", "Odysseus", tf_hero, no_scene, reserved, fac_commoners,
[itm_throwing_spears,itm_leather_gloves,itm_caligea,itm_ancient_helm_light,itm_ancient_leather_armor,itm_ancient_sword,itm_leather_covered_round_shield],
hero_attrib|level(50), wp(230), knows_hero, 0x0000000d7f00d1811aeb9b02e22edbd500000000001e41230000000000000000],
["wahrsager", "Teiresias", "Teiresias", tf_hero, no_scene, reserved, fac_commoners,
[itm_caligea,itm_roman_poor2],
def_attrib|level(50), wp(60), knows_common, 0x0000000ff71123454509a549946e27a200000000001da9630000000000000000],
["doccinga_torturador","Torturer","Torturers",tf_hero|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,
[itm_caligea,itm_roman_poor1,itm_wooden_stick,],
attrib_level_29,wp(200),knows_level_29,0x00000001a400520836db6db6db6db6db00000000001db6db0000000000000000],
#ancient heroes END

##christians start
["petronius","Petronius","Petronius", tf_hero,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor2],def_attrib|level(18),wp(60),knows_common, 0x0000000186041181261d72d8d45ac32e00000000001ca30b0000000000000000],
["memercius","Memercius","Memercius", tf_hero,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor1],def_attrib|level(18),wp(60),knows_common, 0x00000001bc00b00f592475576376d2b200000000001e391c0000000000000000],
["muscullus","Musculus","Muscullus", tf_hero,0,reserved,fac_commoners,[itm_caligea,itm_roman_toga],def_attrib|level(18),wp(60),knows_common, 0x00000004ca053004196172465db0d82b00000000001db72d0000000000000000],
["christ","Stranger","Stranger", tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor2,itm_roman_poor1,itm_roman_poor3,itm_roman_poor4,itm_roman_poor5,itm_knife,itm_knife_2,itm_dagger],def_attrib|level(18),wp(60),knows_common,white_face_11, white_face_12],

["christ_fem","Stranger","Stranger", tf_guarantee_armor|tf_guarantee_boots|tf_female,0,reserved,fac_commoners,[itm_caligea,itm_female_1,itm_female_2,itm_female_3,itm_female_4_barb,itm_knife,itm_knife_2,itm_dagger],def_attrib|level(18),wp(60),knows_common,woman_face_1, woman_face_2],
##christian end
##special merchants

["merchant1","Ogolus the tailor","Ogolus the tailor", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_toga],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x000000000e04c008592253a72311b2d900000000001f59640000000000000000],
["merchant2","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor2],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x00000000031071821569caa4da28b76400000000001d56dc0000000000000000],
["merchant3","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor1],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x000000003810748416cd8ac8b299e92500000000001dd8da0000000000000000],
["merchant4","Gaius Marius","Gaius Marius", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_toga],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x000000003505210f5c937e38dc65366100000000001c94f10000000000000000],
##jerusalem tempel merchants
["merchant5","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_sarranid_cloth_robe_b],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x000000003e0cf0c4262255195bceac9a00000000000e48a60000000000000000],
["merchant6","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_sarranid_cloth_robe],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x000000002808740e3975aea8cb6da6a200000000001124640000000000000000],
["merchant7","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_robe],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x0000000033006181191ba738dc8dab2d00000000001113340000000000000000],
["merchant8","Merchant","Merchants", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_indian_pants,itm_indian_turban_3],
def_attrib|level(18),wp(60),knows_inventory_management_10,0x0000000033006181191ba738dc8dab2d00000000001113340000000000000000],

["prisoner","Prisoner","Prisoners",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[],
def_attrib|level(5),wp(30),knows_common, white_face_11,white_face_22],

#pyramids begin
["kasius","Kasius","Kasius",tf_hero,0,0,fac_commoners,[itm_roman_spatha, itm_graves_simple_2, itm_roman_townguard_helm, itm_auxilia_squamata_east_4],
attrib_level_31,wp(190),knows_level_31,0x00000001bf0c029156db6dd5cc8f372400000000001dc2a00000000000000000],
["orchon","Orchon","Orchon",tf_hero,0,0,fac_commoners,[itm_kopis,itm_legion_hamata_cape_7,itm_roman_aux_helm_10, itm_eastern_shoe],
attrib_level_29,wp(190),knows_level_29,0x000000018a04b249555c89b9244cc69400000000001b36cd0000000000000000],
#pyramids end

#mine in villages
["mine_boss","Foreman","Foremen",tf_is_merchant|tf_hero,0,0,fac_commoners,[itm_caligea, itm_linen_tunic],
def_attrib|level(5),wp(230),knows_common,0x0000000e130131c136db6db6db6db6db00000000001db6db0000000000000000],

#delphi oracle
["pythia","Pythia","Pythia", tf_female|tf_hero, no_scene, reserved, fac_commoners, [itm_roman_noble_dress_5,itm_caligea],
def_attrib|level(4), wp(60), knows_common, 0x00000000000040d408db7434dbe5b6e400000000001c77240000000000000000],
["lykos","Lykos","Lykos", tf_hero, no_scene, reserved, fac_commoners, [itm_caligea, itm_roman_poor1],
def_attrib|level(4), wp(60), knows_common,0x000000018705124e41134abb658eb99d00000000001d3aab0000000000000000],
["organiser","Eystachus","Eystachus", tf_hero, no_scene, reserved, fac_commoners, [itm_caligea, itm_roman_toga],
def_attrib|level(4), wp(60), knows_common,0x00000001aa0510113d6e86c8dee85d6500000000001d01240000000000000000],
#delphi oracle END

#player villa slots begin
["housholder2", "Marcus Tertius", "Marcus Tertius", tf_hero, no_scene, reserved, fac_commoners, [itm_caligea,itm_roman_toga],
def_attrib|level(4), wp(60), knows_common, 0x00000001b804b5442574746aad91b71400000000000e251f0000000000000000 ],
["household_villa","{!}household_possessions_villa","{!}household_possessions_villa",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],
def_attrib|level(4),wp(60),knows_inventory_management_10, 0],
["array_villa_feast","{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],
def_attrib|level(4),wp(40),knows_inventory_management_10, bandit_face1, bandit_face2],
#player villa slots end
###five guests, slot 1 to 5 is for guests, solt 6 for meal, slot 7 for musican, slot 8 for dancers, slot 9 timer

##minor faction troops and kings begin
["slavic_king", "Karovit", "Karovit", tf_hero, no_scene, reserved, fac_slavic,
[itm_celtic_boots,itm_sarmatian_heavy_helm8,itm_jarid,itm_germanic_shield_large11,itm_sarmitian_scale_6,itm_sword_viking_2],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x000000003f0513053b848ae75b8f69e300000000001e9ae30000000000000000, arab_face_old],
["danish_king", "Arluf", "Arluf", tf_hero, no_scene, reserved, fac_danish,
[itm_celtic_boots,itm_germanic_helm3,itm_jarid,itm_germanic_shield_large12,itm_germanic_noble_1,itm_sword_viking_4],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x0000000011040341669cc9584db19af400000000001ec76b0000000000000000, arab_face_old],
["irish_king", "Mogha", "Mogha", tf_hero, no_scene, reserved, fac_irish,
[itm_celtic_boots,itm_celtic_heavy1,itm_irish_sword,itm_irish_shield_3,itm_britton_helm_noble_2,itm_jarid,itm_jarid],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x00000007000c2345552271c66176192500000000001f48e40000000000000000, arab_face_old],
["nubian_king", "Amanitore", "Amanitore", tf_hero|tf_female, no_scene, reserved, fac_kush,
[itm_centurio_east_graves,itm_sarranid_cavalry_robe,itm_eastern_sowrd3,itm_kush_crown,itm_bodkin_arrows,itm_nubian_war_bow,itm_african_shield_3],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x000000083f08e30c4a117d04387d28db00000000001cb5aa0000000000000000, arab_face_old],
["arabian_king", "Malik Malichus", "Malik Malichus", tf_hero|tf_randomize_face, no_scene, reserved, fac_nabataea,
[itm_camel,itm_centurio_east_graves,itm_sarranid_cavalry_robe,itm_sarranid_cavalry_sword,itm_eastern_helm6,itm_arrows,itm_arabian_bow_2],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, arab_face_young, arab_face_old ],
["garamantian_king", "Gadarat", "Gadarat", tf_hero|tf_randomize_face, no_scene, reserved, fac_garamantes,
[itm_centurio_east_graves,itm_garmantian_armor_1,itm_headcloth,itm_kopis,itm_african_round_shield],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, african_face_younger, african_face_older ],
["gaetulian_king", "Takfarin", "Takfarin", tf_hero|tf_randomize_face, no_scene, reserved, fac_gaetuli,
[itm_numidian_horse_2,itm_centurio_east_graves, itm_numidian_armor_4,itm_sarranid_felt_hat,itm_sarranid_mace_1,itm_ad_mixed_round_shields_14],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, african_face_younger, african_face_older ],
["georgian_king", "Khachik", "Khachik", tf_hero, no_scene, reserved, fac_georgians,
[itm_sarmatian_shoes,itm_caucasian_longsword,itm_strong_bow,itm_bodkin_arrows,itm_bosporan_pointed_helm_3,
itm_sarmitian_scale_9],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x000000003f0513053b848ae75b8f69e300000000001e9ae30000000000000000, arab_face_old],
["saka_king", "Skunxa the Great", "Skunxa the Great", tf_hero, no_scene, reserved, fac_dahae,
[itm_eastern_shoe_r,itm_saka_armour_2,itm_saka_helmet_2,itm_lance, itm_alan_long_sword_ring, itm_cataphract_horse_steppe_2],
attrib_level_31_warrior, wp(250), knows_level_31_warrior, 0x000000064000939036eb723ad38ddcdc00000000001dd6db0000000000000000, arab_face_old],

["gaetulian_queen", "Farina", "Farina", tf_hero|tf_female|tf_randomize_face, no_scene, reserved, fac_gaetuli,
[itm_eastern_shoe_r,itm_sarranid_lady_dress],
def_attrib|level(4), wp(60), knows_common, african_face_female, african_face_female2 ],
["arabian_queen", "Sheikha Shaqilath", "Sheikha Shaqilath", tf_hero|tf_female|tf_randomize_face, no_scene, reserved, fac_nabataea,
[itm_eastern_shoe_b,itm_sarranid_lady_dress_b],
def_attrib|level(4), wp(60), knows_common, arab_face_female, arab_face_female2 ],
["garamantian_queen", "Darta", "Darta", tf_hero|tf_female, no_scene, reserved, fac_garamantes,
[itm_eastern_shoe_y,itm_sarranid_lady_dress_b],
def_attrib|level(4), wp(60), knows_common, 0x000000003f0080161c92bd7ee271689900000000001f34dc0000000000000000 ],

["arab_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_eastern_shoe,itm_archers_vest_2],
def_attrib|level(18),wp(60),knows_inventory_management_10,arab_face_young, arab_face_old],
["arab_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_sarranid_cloth_robe,itm_caligea],
def_attrib|level(18),wp(60),knows_inventory_management_10,arab_face_young, arab_face_old],


["african_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_leather_boots,itm_garmantian_armor_1],
def_attrib|level(18),wp(60),knows_inventory_management_10,african_face_younger, african_face_older],
["african_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_numidian_armor_2,itm_caligea],
def_attrib|level(18),wp(60),knows_inventory_management_10,african_face_younger, african_face_older],

["caucasian_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_sarmatian_shoes,itm_persian_sheepskin_1],
def_attrib|level(18),wp(60),knows_inventory_management_10,scythian_face_11, scythian_face_12],
["caucasian_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_sarmatian_shoes,itm_kaftan_3],
def_attrib|level(18),wp(60),knows_inventory_management_10,scythian_face_21, scythian_face_22],

["germanic_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_celtic_boots,itm_germanic_light1],
def_attrib|level(18),wp(60),knows_inventory_management_10,germanic_face_11, germanic_face_12],
["germanic_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_celtic_boots,itm_linen_tunic],
def_attrib|level(18),wp(60),knows_inventory_management_10,germanic_face_21, germanic_face_22],

["celtic_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_celtic_boots,itm_celtic_light1],
def_attrib|level(18),wp(60),knows_inventory_management_10,celtic_face_11, celtic_face_12],
["celtic_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_celtic_boots,itm_celtic_naked11],
def_attrib|level(18),wp(60),knows_inventory_management_10,celtic_face_21, celtic_face_22],

["saka_richmerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_eastern_shoe_b,itm_kaftan_3],
def_attrib|level(18),wp(60),knows_inventory_management_10,saka_face_1, saka_face_2],
["saka_poormerchant","Merchant","Merchants", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_sarmatian_shoes,itm_kaftan_1],
def_attrib|level(18),wp(60),knows_inventory_management_10,saka_face_1, saka_face_2],


["saka_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,
[itm_kaftan_2,itm_eastern_shoe_r,itm_saka_hat_3],
def_attrib|level(18),wp(60),knows_common,saka_face_1, saka_face_2],
["african_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_sarranid_cloth_robe_b,itm_eastern_shoe],
def_attrib|level(18),wp(60),knows_common,african_face_younger, african_face_older],
["arab_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_robe,itm_eastern_shoe],
def_attrib|level(18),wp(60),knows_common,arab_face_young, arab_face_old],
["celtic_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_celtic_boots,itm_celtic_light1],
def_attrib|level(18),wp(60),knows_common,celtic_face_11, celtic_face_12],
["germanic_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_celtic_boots,itm_germanic_light6],
def_attrib|level(18),wp(60),knows_common,germanic_face_11, germanic_face_12],
["caucasian_tavernkeeper","Tavernkeeper","Tavernkeepers", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_sarmatian_shoes,itm_kaftan_2],
def_attrib|level(18),wp(60),knows_common,scythian_face_11, scythian_face_12],
["nurse_african","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,[itm_robe,itm_caligea],
def_attrib|level(4),wp(60),knows_common,african_face_female,african_face_female2],
##minor faction troops and kings END

#trader in slave market
["slave_trader","Doulon Emporos","Douloi Emporoi", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_poor4],
def_attrib|level(18),wp(60),knows_common,white_face_11, white_face_12],

["gladiator_euqes","Eques","Eques",tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_gladiators,
[itm_graves_simple_2,itm_hasta2,itm_eastern_sowrd1,itm_arabian_horse_b,itm_simple_thraex_shield,itm_iberian_light6,itm_tourney_helm_green],
str_18|agi_18|level(23),wp(150),knows_common,mercenary_face_1,mercenary_face_2],
["gladiator_murmillo","Murmillo","Murmillo",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_gladiators,
[itm_graves_simple_2,itm_roman_gladius,itm_arena_shield_blue,itm_arena_armor_red,itm_tourney_helm_yellow],
str_30|agi_12|level(23),wp(160),knows_common,mercenary_face_1,mercenary_face_2],
["gladiator_thraex","Thraex","Thraex",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_gladiators,
[itm_graves_simple_2,itm_flax_onehanded1,itm_leather_covered_round_shield,itm_arena_armor_blue,itm_tourney_helm_green],
str_20|agi_16|level(23),wp(180),knows_common,mercenary_face_1,mercenary_face_2],
["gladiator_retiarius","Retiarius","Retiarius",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_gladiators,
[itm_graves_simple_2,itm_arena_armor_green,itm_dagger,itm_dreizack2],
str_15|agi_30|level(23),wp(160),knows_common,mercenary_face_1,mercenary_face_2],
["gladiator_gladiatrix","Gladiatrix","Gladiatrix",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_female|tf_guarantee_shield,no_scene,reserved,fac_gladiators,
[itm_tourney_helm_red,itm_eastern_sowrd1,itm_arena_shield_green],
str_30|agi_25|level(23),wp(160),knows_common,woman_face_1,woman_face_2],
["gladiator_sagittarius","Sagittarius","Sagittarius",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,no_scene,reserved,fac_gladiators,
[itm_graves_simple_2,itm_tourney_helm_red,itm_dagger,itm_arena_armor_yellow,itm_arrows,itm_persian_bow],
str_17|agi_25|level(23),wp(160),knows_common|knows_power_draw_4,woman_face_1,woman_face_2],

["martial","Marcus Valerius Martialis","Marcus Valerius Martialis",tf_hero,no_scene,reserved,fac_commoners,
[itm_caligea,itm_roman_toga],
str_12|agi_12|int_20|cha_25|level(25),wp(60),knows_common|knows_riding_3|knows_persuasion_10|knows_trade_3,0x00000003f000101136db6db6db6db6db00000000001db6db0000000000000000],
["iuvenal","Decimus Iunius Iuvenalis","Decimus Iunius Iuvenalis",tf_hero,no_scene,reserved,fac_commoners,
[itm_caligea,itm_roman_toga],
str_12|agi_12|int_20|cha_25|level(25),wp(60),knows_common|knows_riding_3|knows_persuasion_10|knows_trade_3,0x0000000a7f0010047ed96ddf668ebcdd00000000001db6db0000000000000000],
#used for rename of month
["bard_end","New Month","New Month",tf_hero,no_scene,reserved,fac_commoners,
[],
def_attrib|level(5),wp(60),knows_common,0x0000000a7f0010047ed96ddf668ebcdd00000000001db6db0000000000000000],

["commander_barracks","Praetor","Praetor",tf_hero|tf_is_merchant|tf_randomize_face,no_scene,reserved,fac_commoners,
[itm_graves_simple_2,itm_roman_aux_helm_1, itm_roman_gladius, itm_legion_hamata_cape_8],
attrib_level_26,wp(120),knows_level_26,roman_face1,roman_face2],

##used for players legion, to store the name
["players_legion","Legio XXII Deiotariana","Legio XXII Deiotariana",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],
["players_aux_cav","Ala Italica","Ala Italica",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],
["players_aux_inf","Cohors Germania","Cohors Germania",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],

["players_infantry","Infantry Retinue","Infantry Retinue",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],
["players_cavalry","Cavalry Retinue","Cavalry Retinue",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],
["players_skirmisher","Skirmisher Retinue","Skirmisher Retinue",tf_hero,no_scene,reserved,fac_commoners,
[],def_attrib|level(5),wp(60),knows_common,roman_face1,roman_face2],
##number 13 is now players legion, for slot_troop_legion
#slot one of trp_players_legion controlls if the legion has been founded or not

###########################################################################################################################################################################################################################################################################################################
###### Custom Troops begin##### Custom Troops begin##### Custom Troops begin##### Custom Troops begin######
###########################################################################################################

### OTHER CUSTOM TROOPS NON ROMAN
["custom_infantry","Footman (custom)","Footmen (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_23, wp(140), knows_level_23,roman_face1,roman_face2],
["custom_infantry_equip","Footman (custom)","Footmen (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_infantry_exp","Footman (exp) (custom)","Footmen (exp) (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_26,wp(160),knows_level_26,roman_face1,roman_face2],
["custom_infantry_exp_equip","Footman (exp) (custom)","Footmen (exp) (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_infantry_vet","Footman (vet) (custom)","Footmen (vet) (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(180),knows_level_29,roman_face1,roman_face2],
["custom_infantry_vet_equip","Footman (vet) (custom)","Footmen (vet) (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_standard_bearer","Standardbearer (custom)","Standardbearers (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1, roman_face2],
["custom_standard_bearer_equip","Standardbearer (custom)","Standardbearers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_hornman","Hornman (custom)","Hornmen (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_hornman_equip","Hornman (custom)","Hornmen (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cav_barb","Melee Cavalry (custom)", "Melee Cavalry (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
attrib_level_26, wp_melee(130),knows_level_26,roman_face1,roman_face2],
["custom_cav_barb_equip","Melee Cavalry (custom)","Melee Cavalry (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cav_barb_vet","Melee Cavalry (vet) (custom)", "Melee Cavalry (vet) (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
attrib_level_29, wp_melee(170),knows_level_29,roman_face1,roman_face2],
["custom_cav_barb_vet_equip","Melee Cavalry (vet) (custom)","Melee Cavalry (vet) (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_standard_bearer_cav","Cavalry Standardbearer (custom)","Cavalry Standardbearers (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1, roman_face2],
["custom_standard_bearer_cav_equip","Cavalry Standardbearer (custom)","Cavalry Standardbearers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_skirmisher_cav","Skirmisher Cavalry (custom)", "Skirmisher Cavalry (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
 attrib_level_26,wpe(100,150,150,150),knows_archer_exp_eastern,roman_face1,roman_face2],
["custom_skirmisher_cav_equip","Skirmisher Cavalry (custom)","Skirmisher Cavalry (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_skirmisher_cav_vet","Skirmisher Cavalry (vet) (custom)", "Skirmisher Cavalry (vet) (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
 attrib_level_29,wpe(140,170,170,170),knows_archer_elit,roman_face1,roman_face2],
["custom_skirmisher_cav_vet_equip","Skirmisher Cavalry (vet) (custom)","Skirmisher Cavalry (vet) (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],


["custom_skirmisher","Skirmisher (custom)", "Skirmishers (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_23,wp(150),knows_level_23,roman_face1,roman_face2],
["custom_skirmisher_equip","Skirmisher (custom)","Skirmishers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_skirmisher_vet","Skirmisher (custom)", "Skirmishers (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_26,wp(170),knows_level_26,roman_face1,roman_face2],
["custom_skirmisher_vet_equip","Skirmisher (custom)","Skirmishers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_archer","Archer (custom)", "Archers (custom)", tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,[],
 attrib_level_23,wpe(100,150,150,150),knows_archer_exp,roman_face1,roman_face2],
["custom_archer_equip","Archer (custom)","Archers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_archer_vet","Archer (vet) (custom)", "Archers (vet) (custom)", tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,[],
 attrib_level_26,wpe(100,170,170,170),knows_archer_elit,roman_face1,roman_face2],
["custom_archer_vet_equip","Archer (vet) (custom)","Archers (vet) (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_standard_bearer_skirmisher","Skirmisher Standardbearer (custom)","Skirmisher Standardbearers (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1, roman_face2],
["custom_standard_bearer_skirmisher_equip","Skirmisher Standardbearer (custom)","Skirmisher Standardbearers (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_hornman_skirmisher","Skirmisher Hornman (custom)","Skirmisher Hornmen (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_hornman_skirmisher_equip","Hornman (custom)","Hornmen (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

################### CUSTOM LEGION

["custom_legionary","Tiro Legionis (custom)","Tirones Legionis (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_23, wp(140), knows_level_23,roman_face1,roman_face2],
["custom_legionary_equip","Tiro Legionis (custom)","Tirones Legionis (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_graves_simple_2,itm_roman_gladius,itm_pilum,itm_scutum_1,itm_legion_segmentata_4,itm_1_imp_gallic_f_n],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_legionary_exp","Miles Legionis (custom)","Milites Legionis (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_26,wp(160),knows_level_26,roman_face1,roman_face2],
["custom_legionary_exp_equip","Miles Legionis (custom)","Milites Legionis (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_graves_simple_2,itm_roman_gladius,itm_pilum,itm_scutum_1,itm_legion_segmentata_cape_1,itm_1_imp_gallic_f_n],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_legionary_vet","Evocatus Legionis (custom)","Evocati Legionis (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(180),knows_level_29,roman_face1,roman_face2],
["custom_legionary_vet_equip","Evocatus Legionis (custom)","Evocati Legionis (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_graves_simple_2,itm_roman_gladius,itm_pilum,itm_scutum_1,itm_legion_segmentata_cape_4,itm_1_imp_gallic_f_plume],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_centurio","Centurio (custom)","Centurii (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1,roman_face2],
["custom_centurio_equip","Centurio (custom)","Centurii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_graves_simple_2,itm_roman_gladius,itm_officer_shield_2,itm_centurio_legion_hamata_1,itm_centurio_helm_2],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aquilifer","Aquilifer (custom)","Aquilifer (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1, roman_face2],
["custom_aquilifer_equip","Aquilifer (custom)","Aquilifer (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_aquilifer_legion_squamata_1,itm_aquilifer_helmet_mask,itm_graves_simple,itm_roman_gladius,itm_aquila6],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_signifer","Signifer (custom)","Signifer (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_signifer_equip","Signifer (custom)","Signifer (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_signifer_legion_hamata,itm_graves_simple,itm_signum_signifer,itm_signifer_helm_1,itm_roman_gladius],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_vexilarius","Vexilarius (custom)","Vexilarii (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(160),knows_level_31,roman_face1,roman_face2],
["custom_vexilarius_equip","Vexilarius (custom)","Vexilarii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_graves_simple,itm_vexilum_legio_xx_dei,itm_roman_gladius,itm_vexilarius_legion_hamata_1,itm_vexilarius_helmet_mask],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_tribunus","Tribunus (custom)","Tribuni (custom)",tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(175),knows_level_31,roman_face1,roman_face2],
["custom_tribunus_equip","Tribunus (custom)","Tribuni (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_officer_shield_2,itm_graves_simple_2,itm_musculata_2,itm_roman_gladius,itm_legatus_legionis_helm_2],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_primus_pilius","Primus Pilus (custom)", "Primi Pili (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_31,wp(185),knows_level_31,roman_face1,roman_face2],
["custom_primus_pilius_equip","Primus Pilus (custom)","Primi Pili (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_scutum_1,itm_roman_gladius,itm_centurio_legion_hamata_1,itm_graves_simple_2,itm_centurio_helm_1],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cornicen","Cornicen (custom)", "Cornicines (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_cornicen_equip","Cornicen (custom)","Cornicines (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_f_cornu,itm_roman_gladius,itm_graves_simple_2,itm_signifer_auxilia_hamata_1,itm_signifer_helm_1],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_cornicern","Cornicen Auxiliari (custom)", "Cornicines Auxiliari (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_aux_cornicern_equip","Cornicen Auxiliari (custom)","Cornicines Auxiliari (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_f_cornu,itm_roman_gladius,itm_graves_simple_2,itm_signifer_auxilia_hamata_1,itm_signifer_helm_2],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cav_vex","Vexilarius Equitem (custom)", "Vexilarii Equitem (custom)", tf_guarantee_soldier|tf_mounted,0,0,fac_neutral,[],
 attrib_level_29,wp(160),knows_level_29,roman_face1,roman_face2],
["custom_cav_vex_equip","Vexilarius Equitem (custom)","Vexilarii Equitem (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_horse_3,itm_roman_spatha,itm_graves_simple_2,itm_signifer_auxilia_hamata_1,itm_signum_signifer,itm_signifer_helm_1],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cav_of","Decurio (custom)", "Decurii (custom)", tf_guarantee_soldier|tf_mounted,0,0,fac_neutral,[],
 attrib_level_29,wp(170),knows_level_29,roman_face1,roman_face2],
["custom_cav_of_equip","Decurio (custom)","Decurii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_horse_3, itm_graves_simple_2,itm_roman_spatha,itm_officer_shield_2,itm_musculata_1,itm_legatus_legionis_helm_2],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_centurio","Centurio Auxiliari (custom)", "Centurii Auxiliari (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_29, wp(160), knows_level_29,roman_face1,roman_face2],
["custom_aux_centurio_equip","Centurio Auxiliari (custom)","Centurii Auxiliari (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_aux_centurio_graves,itm_roman_gladius,itm_cetratus_aux_3,itm_auxilia_cent_helmet_1],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_signifer","Signifer Auxiliari (custom)", "Signifer Auxiliari (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
attrib_level_29, wp(160), knows_level_29,roman_face1,roman_face2],
["custom_aux_signifer_equip","Signifer Auxiliari (custom)","Signifer Auxiliari (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_signum_signifer,itm_graves_simple,itm_roman_gladius,itm_signifer_auxilia_hamata_1,itm_signifer_helm_1],
def_attrib|int_30|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_cav","Auxilia Eques (custom)", "Auxilia Equites (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
attrib_level_26, wp_melee(135),knows_level_26,roman_face1,roman_face2],
["custom_aux_cav_equip","Auxilia Eques (custom)","Auxilia Equites (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_horse_3,itm_horse_2,itm_auxilia_cavalry_squamata_2,itm_graves_simple,itm_cetratus_aux_7,itm_cetratus_aux_8,itm_hasta2,itm_roman_spatha,itm_imp_aux_cav_weiler_brass_a],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_cav","Auxilia Equites Sagittarius (custom)", "Auxilia Equites Sagittarii (custom)", tf_guarantee_soldier|tf_guarantee_ranged|tf_mounted,0,0,fac_neutral,[],
 attrib_level_26,wpe(100,160,160,160),knows_archer_exp_eastern,roman_face1,roman_face2],
["custom_cav_equip","Auxilia Equites Sagittarius (custom)","Auxilia Equites Sagittarii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_horse_3,itm_roman_aux_helm_2,itm_roman_spatha,itm_graves_simple_2,itm_legion_hamata_5,itm_arrows,itm_persian_bow],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_spear","Auxilia Hastatus (custom)", "Auxilia Hastati (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_23,wp(150),knows_level_23,roman_face1,roman_face2],
["custom_aux_spear_equip","Auxilia Hastatus (custom)","Auxilia Hastati (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_hasta2,itm_legion_hamata_8,itm_roman_aux_helm_1,itm_cetratus_aux_7,itm_graves_simple_2,itm_1_imp_gallic_a],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_aux_miles","Auxilia Miles (custom)", "Auxilia Milites (custom)", tf_guarantee_soldier,0,0,fac_neutral,[],
 attrib_level_23,wp(150),knows_level_23,roman_face1,roman_face2],
["custom_aux_miles_equip","Auxilia Miles (custom)","Auxilia Milites (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_roman_spatha,itm_legion_hamata_9,itm_cetratus_aux_7,itm_graves_simple_2,itm_pilum,itm_1_imp_gallic_a],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_balista","Ballistarius (custom)", "Ballistarii (custom)", tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,[],
attrib_level_29, wpe(120,200,200,200), knows_level_29,roman_face1,roman_face2],
["custom_balista_equip","Ballistarius (custom)","Ballistarii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_roman_gladius,itm_ballista,itm_ballista_bolts, itm_subarmalis_1,itm_graves_simple_2,itm_1_imp_gallic_a],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_sagitarius","Sagittarius (custom)", "Sagittarii (custom)", tf_guarantee_soldier|tf_guarantee_ranged,0,0,fac_neutral,[],
 attrib_level_23,wpe(100,170,170,170),knows_archer_exp,roman_face1,roman_face2],
["custom_sagitarius_equip","Sagittarius (custom)","Sagittarii (custom)",tf_hero|tf_inactive,0,0,fac_neutral,
[itm_roman_spatha,itm_legion_hamata_4,itm_roman_aux_helm_2,itm_short_bow,itm_arrows,itm_graves_simple_2],
def_attrib|int_29|level(30),wp(60),knows_inventory_management_10,0],

["custom_troops_end","na","na",0,0,0,fac_neutral,[itm_velvet],def_attrib|level(1),wp(60),knows_common,roman_face1, roman_face2],

["inventory_backup","Inventory","Inventory",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
#####################################################################
# Custom Troops end
##########################################################################################################################################################################################################################################################

#second outfit
["pseudo_troop_end","Second Outfit","pseudo_troop_end",tf_hero,no_scene,reserved,fac_commoners,[],
attrib_second_outfit,0,knows_riding_10|knows_power_draw_10|knows_shield_10|knows_power_throw_10,0],
#follower party inventory
["follower_party_mules",  "follower_party_mules","follower_party_mules",tf_hero|tf_unmoveable_in_party_window|tf_is_merchant, 0,reserved,  fac_neutral,[],
def_attrib|level(5),wp(220),knows_inventory_management_10, 0x000000002704d20f36db6db6db6db6db00000000001db6db0000000000000000],

#senate feature
["senator","Senator","Senators",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
[itm_caligea,itm_calceus,itm_calceus_4,itm_calceus_3,itm_calceus_2,itm_roman_toga,itm_dagger],
str_12|agi_12|int_20|cha_25|level(5),wp(30),knows_common|knows_riding_3|knows_persuasion_10|knows_trade_3,0x00000000ff00000436db6db6db6db6db00000000001db6db0000000000000000,0x000000071b00300636db6db6db6db6db00000000001db6db0000000000000000],
["senator_dummy","Speaker","Speakers",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_neutral,
[itm_calceus_3,itm_roman_toga],
str_12|agi_12|int_20|cha_25|level(25),wp(30),knows_common,0x00000000ff00000436db6db6db6db6db00000000001db6db0000000000000000,0x000000071b00300636db6db6db6db6db00000000001db6db0000000000000000],
#senate feature end

##sailors improve party speed on water
["sailor", "Nauta", "Nautae", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, no_scene, reserved, fac_neutral,
[itm_arrows,itm_hunting_bow,itm_javelin,itm_kopis,itm_iberian_light4,itm_iberian_light1,itm_armenian_tunic_1,itm_roman_poor1,itm_roman_poor2,itm_caligea],
attrib_level_16, wp(110), knows_level_16, white_face_11, white_face_12 ],

###troops for latifundiae system
["teacher","Magister Ludi","Magister Ludi",tf_hero,0,0,fac_neutral,
[itm_caligea,itm_roman_toga],def_attrib|level(5),wp(30),knows_common,0x0000000c8b00101238dd8d3cda6db7ff00000000001d285a0000000000000000],

["administrator","Administrator","Administrator",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_toga],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000ead0021051683a9c88c6f5b2a00000000001ddb270000000000000000],

["grape_master","Master of Grapes","Master of Grapes",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],
def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000b1100420136db6db6db6db6db00000000001db6db0000000000000000],

["wine_master","Master of Wine","Master of Wine",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000fc00062101683aafc8c6f5b2a00000000001ddb310000000000000000],

["oil_master","Master of Oil","Master of Oil",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000d5f00b10350de6f74db6db6db00000000001c12db0000000000000000],

["olives_master","Master of Olives","Master of Olives",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x000000036e0015ce36db6db6db6db6db00000000001eeadb0000000000000000],

["smith_master","Blacksmith","Blacksmith",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|str_15|level(5),wp(30),knows_inventory_management_10,0x0000000f1b00c0093b596db6db6dbbb200000000001ca2db0000000000000000],

["cattle_master","Cattle Master","Cattle Master",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x000000000001101036db6db6db6db6db00000000001db6db0000000000000000],

["butcher_master","Butcher","Butcher",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000aa00040011683a9c88c6f5b2a00000000001ddb310000000000000000],

["fish_master","Master of Fish","Master of Fish",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000b000023c71683a9c88c6f5b2a00000000001ddb310000000000000000],

["fruit_master","Master of Fruit","Master of Fruit",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x00000000360070003a1b6cb3df6ff6db00000000001f6cdb0000000000000000],

["grain_master","Master of Grain","Master of Grain",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_roman_poor1,itm_caligea],def_attrib|level(5),wp(30),knows_inventory_management_10,0x000000016800b5cf1683a9c88c4ec92a00000000001e48f40000000000000000],

["master_baker","Baker","Baker",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000cff0000041683a9c88c6f5b2a00000000001ca7310000000000000000],

["master_pottery","Potter Master","Potter Master",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000fff0020091683a9c88c6f5b2a00000000001ddb210000000000000000],

["master_sheep","Shepherd","Shepherd",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000a400023ca1683a9c88c6f5b2a00000000001ddb310000000000000000],

["master_breeder","Master Breeder","Master Breeder",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000a070121c31683a9c88c6f5b2a00000000001cbb110000000000000000],

["master_cheeser","Master Cheeser","Master Cheeser",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000b230010c22c8389c88c6f5b2a00000000001c010b0000000000000000],

["master_tanner","Master Tanner","Master Tanner",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x0000000f9600310f31db9ef6e36db6db00000000001db62b0000000000000000],

["master_weaver","Master Weaver","Master Weaver",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_caligea,itm_roman_poor2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x000000083f01300836db6db69a2db6d900000000001dd8da0000000000000000],

["master_inn","Innkeeper","Innkeeper",tf_hero|tf_is_merchant|tf_female,0,0,fac_neutral,
[itm_caligea,itm_female_3],def_attrib|level(5),wp(30),knows_inventory_management_10,0x00000000c900004d3d666f4b95a89b1100000000001e261b0000000000000000],

["master_merchant","Merchant","Merchant",tf_hero|tf_is_merchant|tf_female,0,0,fac_neutral,
[itm_caligea,itm_female_3],def_attrib|level(5),wp(30),knows_inventory_management_10,0x000000025c00409a3d666f4b95a89b1100000000001e261b0000000000000000],

["master_silk","Master of Silk","Master of Silk",tf_hero|tf_is_merchant,0,0,fac_neutral,
[itm_eastern_shoe,itm_sarranid_cloth_robe_fancy_2],def_attrib|level(5),wp(30),knows_inventory_management_10,0x00000009c000900136db6db6db6db6db00000000000db6db0000000000000000],

#Courtiers
["courtier", "Courtier", "Courtiers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_caligea,itm_calceus,itm_calceus_4,itm_calceus_3,itm_calceus_2,itm_roman_toga,itm_roman_toga_2,itm_roman_toga_3],
def_attrib|level(4), wp(60), knows_common, roman_face1, roman_face2 ],
["courtier_female", "Courtier", "Courtiers", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_roman_noble_dress_5,itm_roman_noble_dress_6,itm_roman_noble_dress_7,itm_caligea],
def_attrib|level(4), wp(60), knows_common, woman_face_1, woman_face_2],

["courtier_locusta", "Locusta", "Locusta", tf_female|tf_hero, no_scene, reserved, fac_commoners,
[itm_roman_noble_dress_5,itm_female_caligea_gold],
def_attrib|level(4), wp(60), knows_common, 0x000000000001020736db6db6db6db6db00000000001db6db0000000000000000 ],
["courtier_crispinilla", "Calvia Crispinilla", "Calvia Crispinilla", tf_female|tf_hero, no_scene, reserved, fac_commoners,
[itm_roman_noble_dress_6,itm_female_caligea_gold],
def_attrib|level(4), wp(60), knows_common, 0x000000003f0041cd36db6db6db6db6db00000000001db6db0000000000000000],
#ENd courtiers

##athenan school
["director_akademia", "Philo", "Philo", tf_hero, no_scene, reserved, fac_kingdom_7,
[itm_caligea,itm_roman_toga],
knight_attrib_5, wp(250), knight_skills_5, 0x0000000c9700d34e3cdb6e966971acdc00000000001e6d230000000000000000 ],
#director of alexandrian library
["alexandrian_library","Tiberius Claudius Balbilus","Tiberius Claudius Balbilus", tf_hero|tf_is_merchant,0,reserved,fac_commoners,[itm_roman_rich2,itm_caligea],
hero_attrib|level(18),wp(60),knows_inventory_management_10,0x00000008770120092c56921b62b528e200000000001d371b0000000000000000, 0x00000008770120092c56921b62b528e200000000001d371b0000000000000000],

#animal troops
["elephant", "Elephant", "elephants", tf_elephant|tf_mounted|tf_guarantee_horse, no_scene, reserved, fac_neutral,
[itm_wild_elephant],
knight_attrib_5, wp(250), knight_skills_5, 0x0000000c9700d34e3cdb6e966971acdc00000000001e6d230000000000000000 ],
["wild_cat", "Lion", "lions", tf_wild_cat|tf_mounted|tf_guarantee_horse, no_scene, reserved, fac_neutral,
[itm_wild_lion],
knight_attrib_5, wp(250), knight_skills_5, 0x0000000c9700d34e3cdb6e966971acdc00000000001e6d230000000000000000 ],
["wild_cat_2", "Leopard", "leopards", tf_wild_cat|tf_mounted|tf_guarantee_horse, no_scene, reserved, fac_neutral,
[itm_wild_lion_2],
knight_attrib_5, wp(250), knight_skills_5, 0x0000000c9700d34e3cdb6e966971acdc00000000001e6d230000000000000000 ],
["wolf", "Wolf", "wolves", tf_wolf|tf_mounted|tf_guarantee_horse, no_scene, reserved, fac_neutral,
[itm_animal_wolf],
knight_attrib_5, wp(250), knight_skills_5, 0x0000000c9700d34e3cdb6e966971acdc00000000001e6d230000000000000000 ],
###End animals

#for banking
["argentarius","Argentarius","Argentarius", tf_hero|tf_randomize_face|tf_is_merchant,0,reserved,fac_commoners,[itm_caligea,itm_roman_toga],
def_attrib|level(18),wp(60),knows_common,white_face_11, white_face_12],

##Funny supplicants
["suppliciant", "Supplicant", "Supplicantw", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_caligea],
def_attrib|level(4), wp(60), knows_common, mercenary_face_1, mercenary_face_2 ],
["suppliciant_female", "Supplicant", "Supplicantw", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_caligea],
def_attrib|level(4), wp(60), knows_common, woman_face_1, woman_face_2 ],
##END supplicants

##QUEST Characters
["minotau","Minotaur","Minotaur",tf_male|tf_hero,0,0,fac_commoners,
[itm_ancient_axe,itm_minotaur_armor],
hero_attrib,wp(300),knows_hero,0x000000003f0020007fffdfffffefffff00000000001fffbf0000000000000000],

["desperatius", "Gaius Desperatius", "Gaius Desperatius", tf_hero, no_scene, reserved, fac_neutral,
[itm_graves_simple,itm_roman_gladius_2,itm_military_tunic_1],
knight_attrib_3, wp(150), knight_skills_3, 0x00000000210c600b374cc7b8998d9d9400000000001eba970000000000000000 ],
["tristitia", "Gaia Tristitia", "Gaia Tristitia", tf_hero|tf_female, no_scene, reserved, fac_neutral,
[itm_caligea, itm_female_3],
def_attrib|level(1), wp(50), knows_common, 0x000000072a08c0d536db6db6db6db6db00000000000db6db0000000000000000 ],

#wlods adventure characters
["wlodowiecus", "Wlodowiecus", "Wlodowiecus", tf_hero, no_scene, reserved, fac_neutral,
[itm_legio_armored_caligea,itm_roman_gladius_3,itm_legion_hamata_cape_7,itm_roman_aux_helm_2,itm_officer_shield_2],
knight_attrib_5, wp(300), knight_skills_5, 0x000000098708021239228db8dc8a46e400000000001d54ed0000000000000000 ],
["olivarius", "Olivarius", "Olivarius", tf_hero, no_scene, reserved, fac_neutral,
[itm_graves_simple,itm_dagger,itm_roman_poor4],
knight_attrib_5, wp(300), knight_skills_5, 0x000000003808108a65a496edb4e4c96200000000001eb4a60000000000000000 ],
["hadrianus", "Hadrianus Pavel", "Hadrianus Pavel", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral,
[itm_legio_armored_caligea,itm_linothorax_greek3,itm_kopis,itm_mak_helm_1,itm_hoplon_1],
knight_attrib_5, wp(300), knight_skills_5|knows_inventory_management_10, 0x000000003f00108136db6db6db6db6db00000000001db6db0000000000000000 ],
["mancinellus", "Mancinellus", "Mancinellus", tf_hero, no_scene, reserved, fac_neutral,
[itm_legio_armored_caligea,itm_roman_spatha_3, itm_hasta2,itm_legion_hamata_cape_8,itm_cetratus_aux_30],
knight_attrib_5, wp(300), knight_skills_5, 0x000000018000d5c436db6db6db6db6db00000000000db6db0000000000000000 ],
["varus", "Varus", "Varus", tf_hero, no_scene, reserved, fac_neutral,
[itm_old_gladius_2,itm_legio_armored_caligea,itm_legion_hamata_cape_4,itm_roman_aux_helm_11,itm_old_round_shield_2],
knight_attrib_5, wp(300), knight_skills_5,  0x000000003f00159236db6db6db6db6db00000000001db6db0000000000000000],
["old_mercenary", "Old Mercenary", "Old Mercenary", tf_hero, no_scene, reserved, fac_neutral,
[itm_celtic_boots,itm_celtic_heavy3,itm_britton_helm2,itm_celtic_long_shild3,itm_celtic_sowrd3],
knight_attrib_5, wp(300), knight_skills_5,  0x0000000cee11214556dc6dc9256ecae300000000001da8db0000000000000000],

["yaaba", "Yaaba", "Yaaba", tf_hero|tf_female|tf_randomize_face|tf_is_merchant, no_scene, reserved, fac_gaetuli,
[itm_eastern_shoe_r,itm_sarranid_lady_dress],
def_attrib|level(4), wp(60), knows_common, african_face_female, african_face_female2 ],

["bacchus", "Dionysus", "Dionysus", tf_hero, no_scene, reserved, fac_neutral,
[itm_sarranid_cloth_robe_fancy_2, itm_maske,itm_female_caligea_gold],
knight_attrib_5, wp(300), knight_skills_5, 0x0000000004011143589d69571ceabea1000000000015b7350000000000000000 ],

["thusnelda", "Thusnelda the beautiful", "Thusnelda the beautiful", tf_hero|tf_female, no_scene, reserved, fac_neutral,
[itm_caligea, itm_female_3_barb],
def_attrib|level(1), wp(50), knows_common, 0x000000000004631c6c249c425c6e48eb00000000001dd7930000000000000000 ],

["tigellinus", "Ophonius Tigellinus", "Ophonius Tigellinus", tf_hero, no_scene, reserved, fac_kingdom_7,
[itm_legatus_legionis_helm_2,itm_roman_spatha,itm_horse_3,itm_musculata_legatus_3,itm_centurio_west_graves,itm_officer_shield,itm_caligea,itm_roman_rich1],
knight_attrib_5, wp(250), knight_skills_5, 0x000000002404b00970d46db6dc72452300000000001db6db0000000000000000 ],

["gaius_petronius", "Gaius Petronius", "Gaius Petronius", tf_hero, no_scene, reserved, fac_kingdom_7,
[itm_caligea,itm_roman_rich3],
knight_attrib_5, wp(250), knight_skills_5, 0x000000068a0cc0091adc85d7547259ac00000000001d956a0000000000000000 ],

["ybor", "Ybor", "Ybor", tf_hero, no_scene, reserved, fac_neutral,
[itm_celtic_boots,itm_germanic_noble_tunic_1,itm_germanic_helm4,itm_germanic_shield_4,itm_danish_longsword],
knight_attrib_5, wp(250), knight_skills_5,  0x00000000090d13520d19a8b76369986a00000000001d931d0000000000000000],
["agio", "Agio", "Agio", tf_hero, no_scene, reserved, fac_neutral,
[itm_celtic_boots,itm_germanic_noble_tunic_2,itm_germanic_helm4,itm_germanic_shield_3,itm_danish_longsword],
knight_attrib_5, wp(250), knight_skills_5,  0x000000001c0c23485a6251269a52550a00000000001dd8dc0000000000000000],
["gambara", "Gambara", "Gambara", tf_hero|tf_female, no_scene, reserved, fac_neutral,
[itm_celtic_boots, itm_german_femal_rich_1],
def_attrib|level(40), wp(50), knows_common, 0x0000000fc011800a5b0ab1d531d65b1c00000000001f56210000000000000000 ],

["octavia","Octavia","Octavia",tf_hero|tf_female, no_scene, reserved, fac_neutral, [itm_caligea,itm_roman_noble_dress_7],
def_attrib|level(21), wp(50), knows_common, 0x000000002b049316249b4eecf36a3ef200000000001f3b0c0000000000000000],
["seneca","Seneca","Seneca",tf_hero,0,reserved,fac_neutral,[itm_roman_toga,itm_caligea],
def_attrib|level(18),wp(60),knows_common,0x0000000bff0030096ae271ab23add92600000000001e49530000000000000000],
["paulina","Pompeia Paulina","Pompeia Paulina",tf_hero|tf_female,0,reserved,fac_neutral,[itm_caligea,itm_female_2],
def_attrib|level(18),wp(60),knows_common,0x0000000a330080ce38ee8e3adbadb6db00000000001dfd9d0000000000000000],
["agent_parthian","Suspicious Parthian","Suspicious Parthian",tf_hero,0,reserved,fac_neutral,[itm_eastern_shoe_r,itm_parthian_tunic_2,itm_scythian_shield_cav2,itm_eastern_sowrd5,itm_phrygian_cap],
attrib_level_20,wp(180),knows_level_20,0x000000052301328436db6db6db6db6db00000000001db6db0000000000000000],
["invidia","Pulchra Invidia","Pulchra Invidia",tf_hero|tf_female,0,reserved,fac_neutral,[itm_caligea,itm_roman_noble_dress_5],
def_attrib|level(18),wp(60),knows_common,0x000000001400708678f34dc54db1b95c0000000000111b260000000000000000],
["sporus","Sporus","Sporus",tf_hero,0,reserved,fac_neutral,[itm_caligea,itm_roman_rich3],
def_attrib|level(18),wp(60),knows_common,0x000000000001100736db8c96a26dc09b00000000001db64b0000000000000000],

["pupienus","Pupienus Maximus","Pupienus Maximus",tf_hero,0,reserved,fac_neutral,[itm_caligea,itm_roman_toga],
def_attrib|level(18),wp(60),knows_merchant_npc,0x000000003f0430116a9b95dae30da91500000000001dfb350000000000000000],
#plinius
["plinius_elder",  "Plinius Secundus ","Plinius Secundus ",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_roman_toga,itm_caligea],
lord_attrib,wp(150),knight_skills_3, 0x000000074a01310137589258db8c04db00000000001da84b0000000000000000],

["solus",  "Solus Monachus","Solus Monachus",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_roman_toga,itm_caligea],
lord_attrib,wp(150),knight_skills_3, 0x0000000b3f043591468db9a90772caaa00000000001f4d140000000000000000],

["albus","Albus","Albus",tf_hero, no_scene, reserved, fac_neutral,
[itm_roman_gladius,itm_roman_spatha,itm_simple_thraex_shield,itm_auxilia_cavalry_hamata_1,itm_graves_simple_2,itm_horse_3,itm_hasta3,itm_roman_aux_helm_1],
attrib_level_31_warrior, wpex(300,300,300,300,300,300), knows_level_31_warrior, 0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000],
["amorus","Amorus Valentinus","Amorus Valentinus",tf_hero, no_scene, reserved, fac_neutral,
[itm_roman_gladius,itm_roman_toga,itm_caligea],
str_10|agi_10|int_15|cha_22|level(21), wp(50), knows_common, 0x00000000120cb4915f232d2d5d89a6f4000000000005d8ca0000000000000000],
["lucia","Lucia Sabina","Lucia Sabina",tf_hero|tf_female, no_scene, reserved, fac_neutral,
[itm_caligea,itm_roman_noble_dress_3],
str_10|agi_10|int_15|cha_22|level(21), wp(50), knows_common, 0x0000000fc205330c56ccd4e4ab894aa300000000001f38f10000000000000000],
["paulus","Paulus","Paulus",tf_hero, no_scene, reserved, fac_neutral,
[itm_roman_poor1,itm_caligea],
str_10|agi_10|int_15|cha_22|level(21), wp(50), knows_common, 0x0000000fff0c3282131a8ec21171367400000000001dc76d0000000000000000],
["petrus","Petrus","Petrus",tf_hero, no_scene, reserved, fac_neutral,
[itm_roman_poor2,itm_caligea],
str_10|agi_10|int_15|cha_22|level(21), wp(50), knows_common, 0x0000000ff900d34745a372429c6a38ad00000000001eb6d40000000000000000],

["lucillus","Lucillus","Lucillus",tf_guarantee_armor|tf_guarantee_boots, no_scene, reserved, fac_neutral,
[itm_dagger,itm_roman_toga, itm_caligea],
str_10|agi_10|int_15|cha_22|level(21), wp(50), knows_common, 0x000000057e042002249249249144a49200000000001d24920000000000000000, 0x000000057e0420045b6db6db75d6db6d00000000001e496d0000000000000000 ],

["diggus","Biggus Dickus","Biggus Dickus",tf_male|tf_hero,0,0,fac_commoners,[itm_roman_toga,itm_caligea],
def_attrib|level(5),wp(30),knows_common,0x000000002801200900108046bfff6fff00000000001c00060000000000000000],
["bannerlord","HOLY SOON","HOLY SOON",tf_male|tf_hero,0,0,fac_commoners,[itm_sarranid_mail_shirt,itm_felt_steppe_cap],
hero_attrib|level(43),wp(300),knows_hero,0x000000003c0c60521fffbfaf7f6945b400000000001f53720000000000000000],
["billy","Billy the Beagle","The Beagle Billy",tf_male|tf_hero|tf_guarantee_all,0,0,fac_commoners,
[itm_camel,itm_nothing_body,itm_nothing_head,itm_nothing_legs,itm_nothing_hands],
def_attrib|level(5),wp(30),knows_common|knows_riding_10,0x000000000910749254d2855b254d6b9100000000001e98830000000000000000],
["witch","Hagatusja Hunna","Hagatusja Hunna",tf_female|tf_hero,0,0,fac_commoners,
[itm_robe,itm_knife],
def_attrib|level(43),wp(300),knows_level_31,0x000000013f00009d44893245652d465900000000001d98a30000000000000000],

["scandia","Wikkon","Wikkon",tf_male|tf_hero,0,0,fac_commoners,
[itm_germanic_completenaked2,itm_one_handed_battle_axe_c, itm_germanic_shield_large12,itm_throwing_spears,itm_throwing_spears],
hero_attrib,wp(300),knows_hero,0x0000000cc900134f36db6db6db6db6db00000000001db6f00000000000000000],
["fortuna","Fortuna","Fortuna", tf_hero|tf_female,0,reserved,fac_commoners,[itm_caligea,itm_female_3],
hero_attrib|level(43),wp(300),knows_hero,0x0000000004087311101a4d891af5f6fb00000000001c05d00000000000000000],
["fake_nero","Nero Augustus","Nero Augustus",tf_male|tf_hero,0,0,fac_commoners,
[itm_legatus_legionis_helm,itm_legio_armored_caligea,itm_augustus_armor,itm_ancient_spatha,itm_officer_shield_2],
hero_attrib,wp(300),knows_hero,0x00000001b90800113adb91996245299900000000001e5a6d0000000000000000],

#sussus
["sussus_amogus", "Sussus Amogus", "Sussus Amogus", tf_guarantee_all, no_scene, reserved, fac_outlaws,
[itm_leather_boots,itm_scale_armor,itm_old_gladius_1,itm_old_round_shield_1,itm_roman_aux_helm_old_2],
attrib_level_12, wp(60), knows_level_12, bandit_face1, bandit_face2 ],

##quest about elysium start
["drunken_sailor","Drunken Sailor","Drunken Sailor",tf_male|tf_hero,0,0,fac_commoners,
[itm_roman_poor3,itm_caligea,itm_kopfband,itm_kopis],
attrib_level_18,wp(150),knows_level_18,0x000000075a00d1832a9b6e3ab42ed95400000000001ca9190000000000000000],

#random idio
["random_idiot","Chulainn Makasius Aurelianus","Chulainn Makasius Aurelianus",tf_male|tf_hero,0,0,fac_commoners,
[itm_roman_poor2,itm_caligea],
attrib_level_12,wp(10),knows_level_12,0x00000000000930425b6eb74d75bb3b3e00000000001ed6da0000000000000000],

["desiderius","Desiderius","Desiderius",tf_male|tf_hero,0,0,fac_commoners,
[itm_roman_rich_emperor,itm_female_caligea_gold],
attrib_level_18,wp(150),knows_level_18,0x0000000003001004371a7db6db6db6db00000000001db6db0000000000000000],
["odius","Odius","Odius",tf_male|tf_hero,0,0,fac_commoners,
[itm_roman_rich_emperor,itm_female_caligea_gold],
attrib_level_18,wp(150),knows_level_18,0x000000000300b011271a7db6dc7236e300000000001dcac40000000000000000],
["amalia","Animalia","Animalia",tf_female|tf_hero,0,0,fac_commoners,
[itm_roman_femal_rich1_new,itm_female_caligea_gold],
attrib_level_18,wp(150),knows_level_18,0x00000001460c7159641b7ca4dbea37a300000000001c38cb0000000000000000],
["fiducia","Fiducia","Fiducia",tf_female|tf_hero,0,0,fac_commoners,
[itm_roman_femal_rich1_new,itm_female_caligea_gold],
attrib_level_18,wp(150),knows_level_18,0x00000000230c20ce0b527d351be1c12300000000001c360e0000000000000000],

["alexander","Megas Alexandros","Megas Alexandros",tf_hero,0,0,fac_commoners,
[itm_roman_rich_emperor,itm_caligea,itm_laurel_gold],
attrib_level_18,wp(150),knows_level_18,0x000000000c00c0012b637d86e46258e500000000001e296b0000000000000000],
["caesar","Gaius Julius Caesar","Gaius Julius Caesar",tf_hero,0,0,fac_commoners,
[itm_roman_toga_2,itm_caligea,itm_laurel_wearth],
attrib_level_18,wp(150),knows_level_18,0x0000000dbf00200936dbb23ae46db76300000000001db6db0000000000000000],
["aeneas","Aeneas","Aeneas",tf_hero,0,0,fac_commoners,
[itm_roman_toga,itm_caligea],
attrib_level_18,wp(150),knows_level_18,0x000000003f08124416cc6f197291d4dd00000000001d20a20000000000000000],

["agrippina","Agrippina","Agrippina",tf_female|tf_hero,0,0,fac_commoners,
[itm_female_3,itm_caligea,itm_roman_gladius],
attrib_level_31_warrior,wp(300),knows_level_31_warrior,0x0000000d0000824445938da32d81a32200000000001ed4c40000000000000000],
["sittius","Sittius Afer","Sittius Afer",tf_hero|tf_is_merchant,0,0,fac_commoners,
[itm_roman_toga,itm_caligea,itm_roman_gladius],
attrib_level_31_warrior,wp(300),knows_level_31_warrior,0x000000003f0c300b7e0087ffffe0003f00000000001c7e070000000000000000],

["greek_philosopher","Kados Gigantos","Kados Gigantos",tf_hero,0,0,fac_commoners,
[itm_roman_toga,itm_caligea],
attrib_level_18,wp(150),knows_level_18,0x000000003f00218471db4e36f4adbfff00000000001cb4e00000000000000000],
["roman_philosopher","Gigacus Chadus","Gigacus Chadus",tf_hero,0,0,fac_commoners,
[itm_roman_toga,itm_caligea],
attrib_level_18,wp(150),knows_level_18,0x000000003f08400b71db8dbbe36fffff00000000001ca6a00000000000000000],

["joesph_arimatrea","Joseph of Arimathea","Joseph of Arimathea",tf_hero,0,0,fac_commoners,
[itm_generic_poor2,itm_caligea],
attrib_level_18,wp(150),knows_level_18,0x0000000ff60ce3473d366a66df98dc2c00000000001cb8e60000000000000000],

["old_man","Old Man","Old Man",tf_hero|tf_randomize_face|tf_male_north_african,0,0,fac_commoners,
[itm_generic_poor1,itm_caligea],
attrib_level_12,wp(100),knows_level_12, north_african_man_face_old_1, north_african_man_face_older_2],

["amokos","Amokos Impostos","Amokos Impostos",tf_hero,0,0,fac_commoners,
[itm_roman_poor1,itm_caligea],
attrib_level_12,wp(100),knows_level_12, 0x000000002411338075cf4dc863ce66d300000000001c37fd0000000000000000],

["claudia","Claudia Urgulanallia","Claudia Urgulanallia",tf_female|tf_hero,0,0,fac_commoners,
[itm_female_2,itm_caligea],
attrib_level_12,wp(100),knows_level_12,0x0000000ce810218337505e3650f3473c00000000001c589a0000000000000000],
###END quest characters

["circus_1", "Acrobat", "Acrobat", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_roman_poor3]+roman_foot_peasant,
def_attrib|level(4), wp(60), knows_common, roman_face1, roman_face2 ],
["circus_2", "Acrobat", "Acrobat", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_roman_poor3]+roman_foot_peasant,
def_attrib|level(4), wp(60), knows_common, roman_face1, roman_face2 ],
["circus_3", "Acrobat", "Acrobat", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners,
[itm_roman_poor3]+roman_foot_peasant,
def_attrib|level(4), wp(60), knows_common, roman_face1, roman_face2 ],

["ascetic","Ascetic","Ascetic",tf_hero,0,0,fac_commoners,
[itm_generic_poor1,itm_leather_boots],
attrib_level_12,wp(100),knows_level_12, 0x0000000f3f10334758e9c5cee5735bad00000000001ed91d0000000000000000],

["alwisus","Alwisus","Alwisus",tf_hero,0,0,fac_commoners,
[itm_germanic_light5,itm_celtic_boots],
attrib_level_12,wp(100),knows_level_12, 0x000000000e0c33517cdc94f85b6db6db00000000001fd9e70000000000000000],

["hludwig","Hludwig","Hludwig",tf_male|tf_hero,0,0,fac_commoners,
[itm_celtic_boots, itm_pelt_coat, itm_germanic_axe3, itm_throwing_spears, itm_eastern_germanic_shield_2, itm_bear_skin_2],
hero_attrib,wp(300),knows_hero,0x0000000fc00d114d75a8aab6db6db6db00000000001c06790000000000000000],
# son of hludwig
["ekkebert","Ekkebert","Ekkebert",tf_male|tf_hero,0,0,fac_commoners,
[itm_celtic_boots, itm_rawhide_coat, itm_germanic_axe2, itm_throwing_spears, itm_eastern_germanic_shield_3, itm_bear_skin_1],
hero_attrib,wp(300),knows_hero,0x00000006400d138775a8aab6db6db6db00000000001c06790000000000000000],
# son of hludwig
["egino","Egino","Egino",tf_male|tf_hero,0,0,fac_commoners,
[itm_celtic_boots, itm_rawhide_coat, itm_germanic_axe2, itm_throwing_spears, itm_eastern_germanic_shield_3, itm_bear_skin_1],
hero_attrib,wp(300),knows_hero,0x00000000000d100438db8836536db6db00000000001c86490000000000000000],

#Pamphile of Epidaurus
["pamphile","Pamphile","Pamphile",tf_female|tf_hero,0,0,fac_commoners,
[itm_roman_noble_dress_7_fat, itm_caligea],
attrib_level_12,wp(100),knows_level_12,0x000000003f00b04549981ff8e0e978b900000000001de8dc0000000000000000],

["zarinaia","Zarinaia","Zarinaia",tf_female|tf_hero,0,0,fac_commoners,
[itm_saka_dress,itm_saka_crown],
attrib_level_12,wp(100),knows_level_12,0x00000000000c731307d106390c6606ec00000000001c45330000000000000000],

# wlod 4
["han_footman", "Han Footman", "Han Footmen", tf_male|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
[itm_chinese_cap_1,itm_chinese_cap_2, itm_chinese_shield_1, itm_chinese_shield_2, itm_chinese_sword, itm_chinese_light_1,itm_chinese_light_2, itm_leather_boots],
attrib_level_26, wp(160), knows_level_26, saka_face_1, saka_face_2],
["han_hallbard_man", "Han Spearman", "Han Spearmen", tf_male|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
[itm_chinese_cap_1,itm_chinese_cap_2, itm_chinese_hallbard, itm_chinese_light_1,itm_chinese_light_2, itm_leather_boots],
attrib_level_26, wp(160), knows_level_26, saka_face_1, saka_face_2],
["han_heavy_hallbard_man", "Han Heavy Spearman", "Han Heavy Spearmen", tf_male|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet, no_scene, reserved, fac_commoners,
[itm_chinese_cap_1,itm_chinese_cap_2, itm_chinese_helm_heavy,itm_chinese_heavy_1, itm_chinese_hallbard, itm_leather_boots],
attrib_level_29, wp(190), knows_level_29, saka_face_1, saka_face_2],

["turakina","Turakina","Turakina",tf_female|tf_hero,0,0,fac_commoners,
[itm_leather_boots, itm_alan_light_1, itm_war_spear,  itm_sarmatian_bow, itm_sarmatian_arrows_2],
attrib_level_16_warrior,wp(150),knows_level_16_warrior,0x00000001bf00b09a37cf9d0edb5120db00000000001c10d30000000000000000],
["lybian","The Libyan","The Libyan",tf_male|tf_hero,0,0,fac_commoners,
[itm_caligea, itm_roman_toga_2],
hero_attrib,wp(300),knows_hero,0x000000003f0cb5cf36db8e83b36db6db00000000001c801b0000000000000000],
["chinese_commander","Commander Lin Lee Shen Shen","Commander Lin Lee Shen Shen",tf_male|tf_hero,0,0,fac_commoners,
[itm_leather_boots, itm_leather_gloves, itm_chinese_helm_heavy, itm_chinese_shield_1, itm_chinese_sword, itm_chinese_heavy_1],
hero_attrib,wp(300),knows_hero,0x000000003f0c901036db6db6db6db6db00000000000db6db0000000000000000],
["temur","Temur, Tuqi King of the Right","Temur, Tuqi King of the Right",tf_male|tf_hero,0,0,fac_commoners,
[itm_leather_boots, itm_kaftan_2, itm_sarmatian_bow, itm_sarmatian_arrows_1, itm_sarmatian_ringsword_1],
hero_attrib,wp(300),knows_hero,0x000000093f0c838737df6db6db6db6db00000000001ca6db0000000000000000],
["taichar","Taichar Khan","Taichar Khan",tf_male|tf_hero,0,0,fac_commoners,
[itm_leather_boots, itm_kaftan_1, itm_sarmatian_bow, itm_sarmatian_arrows_2, itm_sarmatian_ringsword_2],
hero_attrib,wp(300),knows_hero,0x0000000bff0ca385315f8db6db6db6db00000000001efa120000000000000000],
["xiao","Xiao Qiu","Xiao Qiu",tf_male|tf_hero,0,0,fac_commoners,
[itm_leather_boots, itm_alan_light_2],
hero_attrib,wp(300),knows_hero,0x000000093f0c901036db6db6db6db6db00000000000db6db0000000000000000],

["troops_end", "END", "END", 0, no_scene, reserved, fac_dark_knights, [], def_attrib, wp(0), knows_common,0x00000000000c311b712cf5b6db6db6db00000000001db6d80000000000000000],

]#end of file
#Troop upgrade declarations
##roman upgrades
upgrade(troops,"custom_legionary","custom_legionary_exp")
upgrade(troops,"custom_legionary_exp","custom_legionary_vet")

upgrade(troops,"legio_i_adjutrix","legio_i_adjutrix_exp")
upgrade(troops,"legio_i_adjutrix_exp","legio_i_adjutrix_vet")

upgrade(troops,"legio_iii_augusta","legio_iii_augusta_exp")
upgrade(troops,"legio_iii_augusta_exp","legio_iii_augusta_vet")

upgrade(troops,"legio_v_alaudae","legio_v_alaudae_exp")
upgrade(troops,"legio_v_alaudae_exp","legio_v_alaudae_vet")

upgrade(troops,"legio_v_macedonia","legio_v_macedonia_exp")
upgrade(troops,"legio_v_macedonia_exp","legio_v_macedonia_vet")

upgrade(troops,"legio_vi_ferrata","legio_vi_ferrata_exp")
upgrade(troops,"legio_vi_ferrata_exp","legio_vi_ferrata_vet")

upgrade(troops,"legio_vi_victrix","legio_vi_victrix_exp")
upgrade(troops,"legio_vi_victrix_exp","legio_vi_victrix_vet")

upgrade(troops,"legio_vii_galbia","legio_vii_galbia_exp")
upgrade(troops,"legio_vii_galbia_exp","legio_vii_galbia_vet")

upgrade(troops,"legio_x_fretensis","legio_x_fretensis_exp")
upgrade(troops,"legio_x_fretensis_exp","legio_x_fretensis_vet")

upgrade(troops,"legio_xi_claudia","legio_xi_claudia_exp")
upgrade(troops,"legio_xi_claudia_exp","legio_xi_claudia_vet")

upgrade(troops,"legio_xiii_gemina","legio_xiii_gemina_exp")
upgrade(troops,"legio_xiii_gemina_exp","legio_xiii_gemina_vet")

upgrade(troops,"legio_xxi_rapax","legio_xxi_rapax_exp")
upgrade(troops,"legio_xxi_rapax_exp","legio_xxi_rapax_vet")

upgrade(troops,"praetoriani_milites","praetoriani_milites_exp")
upgrade(troops,"praetoriani_milites_exp","praetoriani_milites_vet")

upgrade(troops,"bosporan_archer","bosporan_archer_exp")
upgrade(troops,"bosporan_archer_exp","bosporan_archer_vet")

upgrade(troops,"bosporan_cav","bosporan_cav_exp")
upgrade(troops,"bosporan_cav_exp","bosporan_cav_vet")

upgrade(troops,"bosporan_elite","bosporan_elite_exp")
upgrade(troops,"bosporan_elite_exp","bosporan_elite_vet")

upgrade(troops,"bosporan_light_spearman","bosporan_light_spearman_exp")
upgrade(troops,"bosporan_light_spearman_exp","bosporan_light_spearman_vet")

upgrade(troops,"judean_guard_archer","judean_guard_archer_vet")
upgrade(troops,"judean_guard","judean_guard_vet")

upgrade(troops,"judean_archer","judean_archer_exp")
upgrade(troops,"judean_archer_exp","judean_archer_vet")

upgrade(troops,"judean_light_clubman","judean_light_clubman_exp")
upgrade(troops,"judean_light_clubman_exp","judean_light_clubman_vet")

upgrade(troops,"judean_light_spearman","judean_light_spearman_exp")
upgrade(troops,"judean_light_spearman_exp","judean_light_spearman_vet")

upgrade(troops,"judean_cav","judean_cav_exp")
upgrade(troops,"judean_cav_exp","judean_cav_vet")

upgrade(troops,"judean_elite","judean_elite_exp")
upgrade(troops,"judean_elite_exp","judean_elite_vet")

upgrade(troops,"judean_slinger","judean_slinger_exp")
upgrade(troops,"judean_slinger_exp","judean_slinger_vet")

upgrade(troops,"judean_skirmisher","judean_skirmisher_exp")
upgrade(troops,"judean_skirmisher_exp","judean_skirmisher_vet")

upgrade2(troops,"mountain_bandit","judean_light_clubman", "judean_light_spearman")

# upgrade(troops,"farmer","watchman")
# upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
# upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
# upgrade(troops,"mercenary_swordsman","hired_blade")
# upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade2(troops,"bandit","brigand","mercenary_swordsman")
# upgrade2(troops,"egyptian_infantry_light","egyptian_infantry_heavy","egyptian_archers")

# upgrade(troops,"manhunter","slave_driver")

# upgrade(troops,"slave_driver","slave_hunter")
# upgrade(troops,"slave_hunter","slave_crusher")
# upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")

upgrade(troops,"steppe_bandit","alan_horse_archer")
upgrade(troops,"alan_horse_archer","alan_heavy_horse_archer")

upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"slave_female","refugee")
upgrade(troops,"slave","slave_warrior")
upgrade(troops,"slave_warrior","slave_warrior_2")
upgrade(troops,"slave_warrior_2","slave_warrior_3")

upgrade(troops,"slave_rebel","slave_rebel_2")

upgrade(troops,"germanic_light_clubman","germanic_light_clubman_exp")
upgrade(troops,"germanic_light_spearman","germanic_light_spearman_exp")
upgrade(troops,"germanic_skirmisher","germanic_skirmisher_exp")
upgrade(troops,"germanic_slinger","germanic_slinger_exp")
upgrade(troops,"germanic_archer","germanic_archer_exp")
upgrade(troops,"germanic_noble_swordsman","germanic_noble_swordsman_exp")
upgrade(troops,"germanic_noble_swordsman_exp","germanic_noble_swordsman_vet")
upgrade(troops,"germanic_noble_spearman","germanic_noble_spearman_exp")
upgrade(troops,"germanic_noble_spearman_exp","germanic_noble_spearman_vet")
upgrade(troops,"germanic_cavalry","germanic_cavalry_exp")

upgrade(troops,"celtic_light_clubman","celtic_light_clubman_exp")
upgrade(troops,"celtic_light_spearman","celtic_light_spearman_exp")
upgrade(troops,"celtic_skirmisher","celtic_skirmisher_exp")
upgrade(troops,"celtic_archer","celtic_archer_exp")
upgrade(troops,"celtic_horseman","celtic_horseman_exp")
upgrade(troops,"celtic_naked_swordman","celtic_naked_swordman_exp")
upgrade(troops,"celtic_naked_swordman_exp","celtic_naked_swordman_vet")
upgrade(troops,"celtic_noble_swords","celtic_noble_swords_exp")
upgrade(troops,"celtic_noble_swords_exp","celtic_noble_swords_vet")

upgrade(troops,"caledonian_light_clubman","caledonian_light_clubman_exp")
upgrade(troops,"caledonian_light_spearman","caledonian_light_spearman_exp")
upgrade(troops,"caledonian_skirmisher","caledonian_skirmisher_exp")
upgrade(troops,"caledonian_archer","caledonian_archer_exp")
upgrade(troops,"caledonian_horseman","caledonian_horseman_exp")
upgrade(troops,"caledonian_naked_swordman","caledonian_naked_swordman_exp")
upgrade(troops,"caledonian_naked_swordman_exp","caledonian_naked_swordman_vet")
upgrade(troops,"caledonian_noble_swords","caledonian_noble_swords_exp")
upgrade(troops,"caledonian_noble_swords_exp","caledonian_noble_swords_vet")

upgrade(troops,"dacian_archers","dacian_archers_exp")
upgrade(troops,"dacian_skirmishers","dacian_skirmishers_exp")
upgrade(troops,"dacian_light_spearman","dacian_light_spearman_exp")
upgrade(troops,"dacian_light_swordman","dacian_light_swordman_exp")
upgrade(troops,"sarmatian_archers","sarmatian_archers_exp")
upgrade(troops,"sarmatian_light_spearman","sarmatian_light_spearman_exp")
upgrade(troops,"sarmatian_light_horsearcher","sarmatian_light_horsearcher_exp")
upgrade(troops,"sarmatian_light_horsearcher_exp","sarmatian_light_horsearcher_vet")
upgrade(troops,"sarmatian_light_horseman","sarmatian_light_horseman_exp")
upgrade(troops,"sarmatian_light_horseman_exp","sarmatian_light_horseman_vet")
upgrade(troops,"sarmatian_heavy_horseman","sarmatian_heavy_horseman_exp")
upgrade(troops,"sarmatian_heavy_horseman_exp","sarmatian_heavy_horseman_vet")
upgrade(troops,"sarmatian_noble_horseman","sarmatian_noble_horseman_exp")
upgrade(troops,"sarmatian_noble_horseman_exp","sarmatian_noble_horseman_vet")
upgrade(troops,"sarmatian_heavy_horsearcher","sarmatian_heavy_horsearcher_exp")
upgrade(troops,"sarmatian_heavy_horsearcher_exp","sarmatian_heavy_horsearcher_vet")
upgrade(troops,"dacian_flaxman","dacian_flaxman_vet")
upgrade(troops,"dacian_flaxman_vet","dacian_flaxman_heavy")
upgrade(troops,"dacian_noble_cav","dacian_noble_cav_exp")
upgrade(troops,"dacian_noble_cav_exp","dacian_noble_cav_vet")
upgrade(troops,"dacian_noble_inf","dacian_noble_inf_exp")
upgrade(troops,"dacian_noble_inf_exp","dacian_noble_inf_vet")

upgrade(troops,"armenian_elite_infantry","armenian_elite_infantry_exp")
upgrade(troops,"armenian_elite_infantry_exp","armenian_elite_infantry_vet")

upgrade(troops,"armenian_heavy_inf","armenian_heavy_inf_exp")
upgrade(troops,"armenian_heavy_inf_exp","armenian_heavy_inf_vet")

upgrade(troops,"armenian_heavy_maceman","armenian_heavy_maceman_exp")
upgrade(troops,"armenian_heavy_maceman_exp","armenian_heavy_maceman_vet")

upgrade(troops,"caucasian_heavy_spearman","caucasian_heavy_spearman_exp")
upgrade(troops,"caucasian_heavy_spearman_exp","caucasian_heavy_spearman_vet")

upgrade(troops,"armenian_skrimisher","armenian_skrimisher_exp")
upgrade(troops,"armenian_skrimisher_exp","armenian_skrimisher_vet")

upgrade(troops,"armenian_slinger","armenian_slinger_exp")
upgrade(troops,"armenian_slinger_exp","armenian_slinger_vet")

upgrade(troops,"armenian_light_axeman","armenian_light_axeman_exp")
upgrade(troops,"armenian_light_axeman_exp","armenian_light_axeman_vet")

upgrade(troops,"armenian_spear_levy","armenian_spear_levy_exp")
upgrade(troops,"armenian_spear_levy_exp","armenian_spear_levy_vet")

upgrade(troops,"armenian_medium_horseman","armenian_medium_horseman_exp")
upgrade(troops,"armenian_medium_horseman_exp","armenian_medium_horseman_vet")

upgrade(troops,"armenian_cataphract","armenian_cataphract_exp")
upgrade(troops,"armenian_cataphract_exp","armenian_cataphract_vet")

upgrade(troops,"armenian_horsearcher","armenian_horsearcher_exp")
upgrade(troops,"armenian_horsearcher_exp","armenian_horsearcher_vet")

upgrade(troops,"eastern_light_archer","eastern_light_archer_exp")
upgrade(troops,"eastern_heavy_inf","eastern_heavy_inf_exp")
upgrade(troops,"eastern_heavy_inf_exp","eastern_heavy_inf_vet")
upgrade(troops,"eastern_heavy_spearman","eastern_heavy_spearman_exp")
upgrade(troops,"eastern_heavy_spearman_exp","eastern_heavy_spearman_vet")
upgrade(troops,"eastern_cataphract","eastern_cataphract_vet")
upgrade(troops,"eastern_cataphract_vet","eastern_cataphract_exp")
upgrade(troops,"eastern_horsearcher","eastern_horsearcher_exp")
upgrade(troops,"eastern_horsearcher_exp","eastern_horsearcher_vet")
upgrade(troops,"eastern_medium_horseman","eastern_medium_horseman_exp")
upgrade(troops,"eastern_medium_horseman_exp","eastern_medium_horseman_vet")
upgrade(troops,"eastern_light_axeman","eastern_light_axeman_exp")
upgrade(troops,"eastern_skrimisher","eastern_skrimisher_exp")
upgrade(troops,"eastern_slinger","eastern_slinger_exp")
upgrade(troops,"germanic_light_clubman_exp","germanic_light_clubman_vet")
upgrade(troops,"germanic_light_spearman_exp","germanic_light_spearman_vet")
upgrade(troops,"germanic_skirmisher_exp","germanic_skirmisher_vet")
upgrade(troops,"germanic_slinger_exp","germanic_slinger_vet")
upgrade(troops,"germanic_archer_exp","germanic_archer_vet")
upgrade(troops,"germanic_cavalry_exp","germanic_cavalry_vet")

upgrade(troops,"celtic_light_clubman_exp","celtic_light_clubman_vet")
upgrade(troops,"celtic_light_spearman_exp","celtic_light_spearman_vet")
upgrade(troops,"celtic_skirmisher_exp","celtic_skirmisher_vet")
upgrade(troops,"celtic_archer_exp","celtic_archer_vet")
upgrade(troops,"celtic_horseman_exp","celtic_horseman_vet")

upgrade(troops,"caledonian_light_clubman_exp","caledonian_light_clubman_vet")
upgrade(troops,"caledonian_light_spearman_exp","caledonian_light_spearman_vet")
upgrade(troops,"caledonian_skirmisher_exp","caledonian_skirmisher_vet")
upgrade(troops,"caledonian_archer_exp","caledonian_archer_vet")
upgrade(troops,"caledonian_horseman_exp","caledonian_horseman_vet")

upgrade(troops,"dacian_light_spearman_exp","dacian_light_spearman_vet")
upgrade(troops,"dacian_light_swordman_exp","dacian_light_swordman_vet")
upgrade(troops,"dacian_skirmishers_exp","dacian_skirmishers_vet")
upgrade(troops,"dacian_archers_exp","dacian_archers_vet")
upgrade(troops,"sarmatian_light_spearman_exp","sarmatian_light_spearman_vet")
upgrade(troops,"sarmatian_archers_exp","sarmatian_archers_vet")
upgrade(troops,"eastern_light_archer_exp","eastern_light_archer_vet")
upgrade(troops,"eastern_light_axeman_exp","eastern_light_axeman_vet")
upgrade(troops,"eastern_skrimisher_exp","eastern_skrimisher_vet")
upgrade(troops,"eastern_slinger_exp","eastern_slinger_vet")
upgrade(troops,"vigilia","vigilia_exp")
upgrade(troops,"vigilia_exp","vigilia_vet")
# upgrade(troops,"vigilia_vet","aux_inf")
# #upgrade(troops,"aux_inf","ballistarii")
upgrade2(troops,"looter","bandit","slave_rebel")
# upgrade(troops,"sarranid_horseman","garamantien_noble_horseman")
# upgrade(troops,"gaetuli_horseman","gaetuli_noble_horseman")
# upgrade(troops,"desert_bandit","arab_noble_cav")
# # upgrade(troops,"aux_cav_praetoriani","aux_cav_praetoriani_2")

upgrade(troops,"eastern_elite_infantry","eastern_elite_infantry_exp")
upgrade(troops,"eastern_elite_infantry_exp","eastern_elite_infantry_vet")

upgrade(troops,"dacian_heavy_inf","dacian_heavy_inf_exp")
upgrade(troops,"dacian_heavy_inf_exp","dacian_heavy_inf_vet")

upgrade(troops,"caucasian_medium_horsearcher","caucasian_medium_horsearcher_exp")
upgrade(troops,"caucasian_medium_horsearcher_exp","caucasian_medium_horsearcher_vet")

upgrade(troops,"caucasian_cataphract","caucasian_cataphract_exp")
upgrade(troops,"caucasian_cataphract_exp","caucasian_cataphract_vet")

upgrade(troops,"custom_infantry","custom_infantry_exp")
upgrade(troops,"custom_infantry_exp","custom_infantry_vet")

upgrade(troops,"custom_cav_barb","custom_cav_barb_vet")
upgrade(troops,"custom_skirmisher_cav","custom_skirmisher_cav_vet")

upgrade(troops,"custom_skirmisher","custom_skirmisher_vet")
upgrade(troops,"custom_archer","custom_archer_vet")