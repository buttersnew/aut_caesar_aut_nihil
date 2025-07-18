###################################################
# header_mission_templates.py
# This file contains declarations for mission templates
# DO NOT EDIT THIS FILE!
###################################################

from header_common import *
from header_operations import *
from header_triggers import *
from header_troops import *
from IDs.ID_scenes import *
from IDs.ID_items import *
from IDs.ID_strings import *

from header_mission_types import *

aif_group_bits    = 0
aif_group_mask    = 0xF
aif_start_alarmed = 0x00000010

grc_infantry = 0
grc_archers  = 1
grc_cavalry  = 2
grc_heroes   = 3
grc_everyone = 9

mordr_hold				= 0
mordr_follow			= 1
mordr_charge			= 2
mordr_mount				= 3
mordr_dismount			= 4
mordr_advance			= 5
mordr_fall_back			= 6
mordr_stand_closer		= 7
mordr_spread_out		= 8
mordr_use_blunt_weapons = 9
mordr_use_any_weapon    = 10
mordr_stand_ground      = 11
mordr_hold_fire         = 12
mordr_fire_at_will      = 13
mordr_retreat           = 14
mordr_use_melee_weapons	= 15
mordr_use_ranged_weapons= 16
mordr_fire_at_my_command= 17
mordr_all_fire_now		= 18
mordr_left_fire_now		= 19
mordr_middle_fire_now	= 20
mordr_right_fire_now	= 21
mordr_form_1_row		= 22
mordr_form_2_row		= 23
mordr_form_3_row		= 24
mordr_form_4_row		= 25
mordr_form_5_row		= 26

rordr_free				= 0
rordr_mount				= 1
rordr_dismount			= 2

wordr_use_any_weapon	= 0
wordr_use_blunt_weapons	= 1
wordr_use_melee_weapons	= 2
wordr_use_ranged_weapons= 3

aordr_fire_at_will      = 0
aordr_hold_your_fire    = 1

# Agent AI Simple Behaviors
aisb_hold = 0
aisb_go_to_pos = 1
aisb_mount = 2
aisb_dismount = 3
aisb_melee = 4
aisb_ranged = 5
aisb_ranged_horseback = 6
aisb_charge_horseback = 7
aisb_maneuver_horseback = 8
aisb_flock = 9
aisb_race = 10
aisb_patrol = 11
aisb_no_enemies = 12
aisb_horse_hold = 13
aisb_horse_run_away = 14

# filter flags
mtef_enemy_party         = 0x00000001
mtef_ally_party          = 0x00000002
mtef_scene_source        = 0x00000004
mtef_conversation_source = 0x00000008
mtef_visitor_source      = 0x00000010
mtef_defenders           = 0x00000040
mtef_attackers           = 0x00000080
mtef_no_leader           = 0x00000100
mtef_no_companions       = 0x00000200
mtef_no_regulars         = 0x00000400
#mtef_team_0              = 0x00001000
mtef_team_0              = 0x00001000
mtef_team_1              = 0x00002000
mtef_team_2              = 0x00003000
mtef_team_3              = 0x00004000
mtef_team_4              = 0x00005000
mtef_team_5              = 0x00006000
mtef_team_member_2       = 0x00008000
mtef_infantry_first      = 0x00010000
mtef_archers_first       = 0x00020000
mtef_cavalry_first       = 0x00040000
mtef_no_auto_reset       = 0x00080000
mtef_reverse_order       = 0x01000000
mtef_use_exact_number    = 0x02000000

mtef_leader_only         = mtef_no_companions | mtef_no_regulars
mtef_regulars_only       = mtef_no_companions | mtef_no_leader


#alter flags
af_override_weapons         = 0x0000000f
af_override_weapon_0        = 0x00000001
af_override_weapon_1        = 0x00000002
af_override_weapon_2        = 0x00000004
af_override_weapon_3        = 0x00000008
af_override_head            = 0x00000010
af_override_body            = 0x00000020
#af_override_leg             = 0x00000040
af_override_foot            = 0x00000040
af_override_gloves          = 0x00000080
af_override_horse           = 0x00000100
af_override_fullhelm        = 0x00000200

#af_override_hands           = 0x00000100
af_require_civilian         = 0x10000000

#af_override_all_but_horse   = 0x000000ff
af_override_all_but_horse   = af_override_weapons | af_override_head | af_override_body |af_override_gloves
af_override_all             = af_override_horse | af_override_all_but_horse
af_override_everything      = af_override_all | af_override_foot
af_override_outfit_1        = af_override_all_but_horse | af_override_foot

requires_third_party = 0x00000001

#mission template flags. also in mission_template.h
#use only the lower 12 bits. Upper 20 is taken up by xsize and ysize.
mtf_arena_fight         = 0x00000001 #identify enemies through team_no
mtf_team_fight          = 0x00000001 #identify enemies through team_no
mtf_battle_mode         = 0x00000002 #No inventory access
mtf_commit_casualties   = 0x00000010
mtf_no_blood            = 0x00000100
mtf_synch_inventory     = 0x00010000 #Make a backup of player inventory and restore it at mission end.



max_size = 1023
xsize_bits = 12
ysize_bits = 22
def xsize(n):
  return (n & max_size) << xsize_bits

def ysize(n):
  return (n & max_size) << ysize_bits

#Mission result flags. also in mission.h
mc_loot                 = 0x0001
mc_imprison_unconscious = 0x0002
