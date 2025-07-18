from header_common import *

###################################################
# header_troops.py
# This file contains declarations for troops
# DO NOT EDIT THIS FILE!
###################################################

#Troop flags
tf_male           = 0
tf_female         = 1
tf_boy			  = 2
tf_girl		      = 3
tf_elephant       = 4
tf_wild_cat       = 5
tf_wolf           = 6
tf_male_barbarian        = 7
tf_male_black            = 8
tf_male_eastern          = 9
tf_male_north_african    = 10

troop_type_mask   = 0x0000000f
tf_hero              = 0x00000010
tf_inactive          = 0x00000020
tf_unkillable        = 0x00000040
tf_allways_fall_dead = 0x00000080
tf_no_capture_alive  = 0x00000100
tf_mounted           = 0x00000400 #Troop's movement speed on map is determined by riding skill.
tf_is_merchant       = 0x00001000 #When set, troop does not equip stuff he owns
tf_randomize_face    = 0x00008000 #randomize face at the beginning of the game.

tf_guarantee_boots            = 0x00100000
tf_guarantee_armor            = 0x00200000
tf_guarantee_helmet           = 0x00400000
tf_guarantee_gloves           = 0x00800000
tf_guarantee_horse            = 0x01000000
tf_guarantee_shield           = 0x02000000
tf_guarantee_ranged           = 0x04000000
tf_unmoveable_in_party_window = 0x10000000

tf_disable_sounds             = 0x00010000 #disable agent related sounds, but not voices. useful for animals
tf_guarantee_polearm          = 0x08000000

# Character attributes...
ca_strength     = 0
ca_agility      = 1
ca_intelligence = 2
ca_charisma     = 3

wpt_one_handed_weapon = 0
wpt_two_handed_weapon = 1
wpt_polearm           = 2
wpt_archery           = 3
wpt_crossbow          = 4
wpt_throwing          = 5
wpt_firearm           = 6


#personality modifiers:
# courage 8 means neutral
courage_4  = 0x0004
courage_5  = 0x0005
courage_6  = 0x0006
courage_7  = 0x0007
courage_8  = 0x0008
courage_9  = 0x0009
courage_10 = 0x000A
courage_11 = 0x000B
courage_12 = 0x000C
courage_13 = 0x000D
courage_14 = 0x000E
courage_15 = 0x000F

aggresiveness_1  = 0x0010
aggresiveness_2  = 0x0020
aggresiveness_3  = 0x0030
aggresiveness_4  = 0x0040
aggresiveness_5  = 0x0050
aggresiveness_6  = 0x0060
aggresiveness_7  = 0x0070
aggresiveness_8  = 0x0080
aggresiveness_9  = 0x0090
aggresiveness_10 = 0x00A0
aggresiveness_11 = 0x00B0
aggresiveness_12 = 0x00C0
aggresiveness_13 = 0x00D0
aggresiveness_14 = 0x00E0
aggresiveness_15 = 0x00F0

is_bandit        = 0x0100
#-----------------------------------
#these also in sentences.py
tsf_site_id_mask = 0x0000ffff
tsf_entry_mask   = 0x00ff0000
tsf_entry_bits   = 16

def entry(n):
  return (((n) << tsf_entry_bits) & tsf_entry_mask)
#-------------------------------------

str_3            = bignum | 0x00000003
str_4            = bignum | 0x00000004
str_5            = bignum | 0x00000005
str_6            = bignum | 0x00000006
str_7            = bignum | 0x00000007
str_8            = bignum | 0x00000008
str_9            = bignum | 0x00000009
str_10           = bignum | 0x0000000a
str_11           = bignum | 0x0000000b
str_12           = bignum | 0x0000000c
str_13           = bignum | 0x0000000d
str_14           = bignum | 0x0000000e
str_15           = bignum | 0x0000000f
str_16           = bignum | 0x00000010
str_17           = bignum | 0x00000011
str_18           = bignum | 0x00000012
str_19           = bignum | 0x00000013
str_20           = bignum | 0x00000014
str_21           = bignum | 0x00000015
str_22           = bignum | 0x00000016
str_23           = bignum | 0x00000017
str_24           = bignum | 0x00000018
str_25           = bignum | 0x00000019
str_26           = bignum | 0x0000001a
str_27           = bignum | 0x0000001b
str_28           = bignum | 0x0000001c
str_29           = bignum | 0x0000001d
str_30           = bignum | 0x0000001e

agi_3            = bignum | 0x00000300
agi_4            = bignum | 0x00000400
agi_5            = bignum | 0x00000500
agi_6            = bignum | 0x00000600
agi_7            = bignum | 0x00000700
agi_8            = bignum | 0x00000800
agi_9            = bignum | 0x00000900
agi_10           = bignum | 0x00000a00
agi_11           = bignum | 0x00000b00
agi_12           = bignum | 0x00000c00
agi_13           = bignum | 0x00000d00
agi_14           = bignum | 0x00000e00
agi_15           = bignum | 0x00000f00
agi_16           = bignum | 0x00001000
agi_17           = bignum | 0x00001100
agi_18           = bignum | 0x00001200
agi_19           = bignum | 0x00001300
agi_20           = bignum | 0x00001400
agi_21           = bignum | 0x00001500
agi_22           = bignum | 0x00001600
agi_23           = bignum | 0x00001700
agi_24           = bignum | 0x00001800
agi_25           = bignum | 0x00001900
agi_26           = bignum | 0x00001a00
agi_27           = bignum | 0x00001b00
agi_28           = bignum | 0x00001c00
agi_29           = bignum | 0x00001d00
agi_30           = bignum | 0x00001e00

int_3            = bignum | 0x00030000
int_4            = bignum | 0x00040000
int_5            = bignum | 0x00050000
int_6            = bignum | 0x00060000
int_7            = bignum | 0x00070000
int_8            = bignum | 0x00080000
int_9            = bignum | 0x00090000
int_10           = bignum | 0x000a0000
int_11           = bignum | 0x000b0000
int_12           = bignum | 0x000c0000
int_13           = bignum | 0x000d0000
int_14           = bignum | 0x000e0000
int_15           = bignum | 0x000f0000
int_16           = bignum | 0x00100000
int_17           = bignum | 0x00110000
int_18           = bignum | 0x00120000
int_19           = bignum | 0x00130000
int_20           = bignum | 0x00140000
int_21           = bignum | 0x00150000
int_22           = bignum | 0x00160000
int_23           = bignum | 0x00170000
int_24           = bignum | 0x00180000
int_25           = bignum | 0x00190000
int_26           = bignum | 0x001a0000
int_27           = bignum | 0x001b0000
int_28           = bignum | 0x001c0000
int_29           = bignum | 0x001d0000
int_30           = bignum | 0x001e0000


cha_3            = bignum | 0x03000000
cha_4            = bignum | 0x04000000
cha_5            = bignum | 0x05000000
cha_6            = bignum | 0x06000000
cha_7            = bignum | 0x07000000
cha_8            = bignum | 0x08000000
cha_9            = bignum | 0x09000000
cha_10           = bignum | 0x0a000000
cha_11           = bignum | 0x0b000000
cha_12           = bignum | 0x0c000000
cha_13           = bignum | 0x0d000000
cha_14           = bignum | 0x0e000000
cha_15           = bignum | 0x0f000000
cha_16           = bignum | 0x10000000
cha_17           = bignum | 0x11000000
cha_18           = bignum | 0x12000000
cha_19           = bignum | 0x13000000
cha_20           = bignum | 0x14000000
cha_21           = bignum | 0x15000000
cha_22           = bignum | 0x16000000
cha_23           = bignum | 0x17000000
cha_24           = bignum | 0x18000000
cha_25           = bignum | 0x19000000
cha_26           = bignum | 0x1a000000
cha_27           = bignum | 0x1b000000
cha_28           = bignum | 0x1c000000
cha_29           = bignum | 0x1d000000
cha_30           = bignum | 0x1e000000

level_mask       = 0x000000FF
level_bits       = 32

def level(v):
  if (v > level_mask):
    v = level_mask
  return (bignum|v) << level_bits
  
def_attrib = str_5 | agi_5 | int_4 | cha_4

# Weapon proficiencies:
one_handed_bits = 0
two_handed_bits = 10
polearm_bits    = 20
archery_bits    = 30
crossbow_bits   = 40
throwing_bits   = 50
firearm_bits    = 60

num_weapon_proficiencies = 7
def wp_one_handed(x):
  return (((bignum | x) & 0x3FF) << one_handed_bits)
def wp_two_handed(x):
  return (((bignum | x) & 0x3FF) << two_handed_bits)
def wp_polearm(x):
  return (((bignum | x) & 0x3FF) << polearm_bits)
def wp_archery(x):
  return (((bignum | x) & 0x3FF) << archery_bits)
def wp_crossbow(x):
  return (((bignum | x) & 0x3FF) << crossbow_bits)
def wp_throwing(x):
  return (((bignum | x) & 0x3FF) << throwing_bits)
def wp_firearm(x):
  return (((bignum | x) & 0x3FF) << firearm_bits)

def find_troop(troops,troop_id):
  result = -1
  num_troops = len(troops)
  i_troop = 0
  while (i_troop < num_troops) and (result == -1):
    troop = troops[i_troop]
    if (troop[0] == troop_id):
      result = i_troop
    else:
      i_troop += 1
  return result



def upgrade(troops,troop1_id,troop2_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  if (troop1_no == -1):
    print "Error with upgrade def: Unable to find troop1-id: " + troop1_id
  elif (troop2_no == -1):
    print "Error with upgrade def: Unable to find troop2-id: " + troop2_id
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, 0]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, 0]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, 0]
    else:
      cur_troop[14:14] = [troop2_no, 0]
      

def upgrade2(troops,troop1_id,troop2_id,troop3_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  troop3_no = find_troop(troops,troop3_id)
  if (troop1_no == -1):
    print "Error with upgrade2 def: Unable to find troop1-id: " + troop1_id
  elif (troop2_no == -1):
    print "Error with upgrade2 def: Unable to find troop2-id: " + troop2_id
  elif (troop3_no == -1):
    print "Error with upgrade2 def: Unable to find troop3-id: " + troop3_id
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, troop3_no]
    else:
      cur_troop[14:14] = [troop2_no, troop3_no]
