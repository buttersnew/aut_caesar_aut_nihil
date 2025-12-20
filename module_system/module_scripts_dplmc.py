# -*- coding: cp1254 -*-
from __future__ import absolute_import
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_sounds import *
from module_info_pages import *
from IDs.ID_animations import *
from IDs.ID_info_pages import *
from IDs.ID_scene_props import *
from IDs.ID_party_templates import *
from header_presentations import *
from module_items import items
from module_factions import dplmc_factions_begin, dplmc_factions_end, dplmc_non_generic_factions_begin

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts_dplmc = [
####################################################################################
#
# Autoloot Scripts begin
# ---------------------------------------------------
####################################################################################

###################################
# Can a troop qualify to use this item?
# Returns 1 = yes, 0 = no.
("dplmc_troop_can_use_item",[
    (store_script_param, ":troop", 1),
    (store_script_param, ":item", 2),
    (store_script_param, ":item_modifier", 3),

    # (item_get_slot, ":difficulty", ":item", dplmc_slot_item_difficulty),
    (item_get_difficulty, ":difficulty", ":item"),
    (item_get_type, ":type", ":item"),
    (try_begin),
        (eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
    (else_try),
        (eq, ":item_modifier", imod_stubborn),
        (val_add, ":difficulty", 1),
    (else_try),
        (eq, ":item_modifier", imod_timid),
        (val_sub, ":difficulty", 1),
    (else_try),
        (eq, ":item_modifier", imod_heavy),
        (neq, ":type", itp_type_horse), #heavy horses don't increase difficulty
        (val_add, ":difficulty", 1),
    (else_try),
        (eq, ":item_modifier", imod_strong),
        (val_add, ":difficulty", 2),
    (else_try),
        (eq, ":item_modifier", imod_masterwork),
        (val_add, ":difficulty", 4),
    (try_end),

    (item_get_type, ":type", ":item"),
    (try_begin),
        (eq, ":type", itp_type_horse),
        (store_skill_level, ":skill", "skl_riding", ":troop"),
    (else_try),
        (this_or_next|eq, ":type", itp_type_crossbow),
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (this_or_next|eq, ":type", itp_type_polearm),
        (this_or_next|eq, ":type", itp_type_head_armor),
        (this_or_next|eq, ":type", itp_type_body_armor),
        (this_or_next|eq, ":type", itp_type_foot_armor),
        (eq, ":type", itp_type_hand_armor),
        (store_attribute_level, ":skill", ":troop", ca_strength),
    (else_try),
        (eq, ":type", itp_type_shield),
        (store_skill_level, ":skill", "skl_shield", ":troop"),
    (else_try),
        (eq, ":type", itp_type_bow),
        (store_skill_level, ":skill", "skl_power_draw", ":troop"),
    (else_try),
        (eq, ":type", itp_type_thrown),
        (store_skill_level, ":skill", "skl_power_throw", ":troop"),
    (try_end),

    (try_begin),
        (lt, ":skill", ":difficulty"),
        (assign, reg0, 0),
    (else_try),
        (assign, reg0, 1),
    (try_end),
]),

#####################################################################
# gets an item's value
# Param1: item ID
# Param2: item modifier
#####################################################################
("dplmc_get_item_value_with_imod", [  # returns the sell price based on the item's money value and its imod
	(store_script_param, ":item", 1),
	(store_script_param, ":imod", 2),
	(store_item_value, ":score", ":item"),
	(try_begin),
		(eq, ":imod", imod_plain),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_cracked),
		(val_mul, ":score", 50),
	(else_try),
		(eq, ":imod", imod_rusty),
		(val_mul, ":score", 55),
	(else_try),
		(eq, ":imod", imod_bent),
		(val_mul, ":score", 65),
	(else_try),
		(eq, ":imod", imod_chipped),
		(val_mul, ":score", 72),
	(else_try),
		(eq, ":imod", imod_battered),
		(val_mul, ":score", 75),
	(else_try),
		(eq, ":imod", imod_poor),
		(val_mul, ":score", 80),
	(else_try),
		(eq, ":imod", imod_crude),
		(val_mul, ":score", 83),
	(else_try),
		(eq, ":imod", imod_old),
		(val_mul, ":score", 86),
	(else_try),
		(eq, ":imod", imod_cheap),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_fine),
		(val_mul, ":score", 190),
	(else_try),
		(eq, ":imod", imod_well_made),
		(val_mul, ":score", 250),
	(else_try),
		(eq, ":imod", imod_sharp),
		(val_mul, ":score", 160),
	(else_try),
		(eq, ":imod", imod_balanced),
		(val_mul, ":score", 350),
	(else_try),
		(eq, ":imod", imod_tempered),
		(val_mul, ":score", 670),
	(else_try),
		(eq, ":imod", imod_deadly),
		(val_mul, ":score", 850),
	(else_try),
		(eq, ":imod", imod_exquisite),
		(val_mul, ":score", 1450),
	(else_try),
		(eq, ":imod", imod_masterwork),
		(val_mul, ":score", 1750),
	(else_try),
		(eq, ":imod", imod_heavy),
		(val_mul, ":score", 190),
	(else_try),
		(eq, ":imod", imod_strong),
		(val_mul, ":score", 490),
	(else_try),
		(eq, ":imod", imod_powerful),
		(val_mul, ":score", 320),
	(else_try),
		(eq, ":imod", imod_tattered),
		(val_mul, ":score", 50),
	(else_try),
		(eq, ":imod", imod_ragged),
		(val_mul, ":score", 70),
	(else_try),
		(eq, ":imod", imod_rough),
		(val_mul, ":score", 60),
	(else_try),
		(eq, ":imod", imod_sturdy),
		(val_mul, ":score", 170),
	(else_try),
		(eq, ":imod", imod_thick),
		(val_mul, ":score", 260),
	(else_try),
		(eq, ":imod", imod_hardened),
		(val_mul, ":score", 390),
	(else_try),
		(eq, ":imod", imod_reinforced),
		(val_mul, ":score", 650),
	(else_try),
		(eq, ":imod", imod_superb),
		(val_mul, ":score", 250),
	(else_try),
		(eq, ":imod", imod_lordly),
		(val_mul, ":score", 1150),
	(else_try),
		(eq, ":imod", imod_lame),
		(val_mul, ":score", 40),
	(else_try),
		(eq, ":imod", imod_swaybacked),
		(val_mul, ":score", 60),
	(else_try),
		(eq, ":imod", imod_stubborn),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_timid),
		(val_mul, ":score", 180),
	(else_try),
		(eq, ":imod", imod_meek),
		(val_mul, ":score", 180),
	(else_try),
		(eq, ":imod", imod_spirited),
		(val_mul, ":score", 650),
	(else_try),
		(eq, ":imod", imod_champion),
		(val_mul, ":score", 1450),
	(else_try),
		(eq, ":imod", imod_fresh),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_day_old),
		(val_mul, ":score", 100),
	(else_try),
		(eq, ":imod", imod_two_day_old),
		(val_mul, ":score", 90),
	(else_try),
		(eq, ":imod", imod_smelling),
		(val_mul, ":score", 40),
	(else_try),
		(eq, ":imod", imod_rotten),
		(val_mul, ":score", 5),
	(else_try),
		(eq, ":imod", imod_large_bag),
		(val_mul, ":score", 190),
	(try_end),

	(assign, reg0, ":score"),
]),

("dplmc_get_item_score_with_imod",[
    # returns the score on the item's base score and its imod
      (store_script_param, ":item", 1),
      (store_script_param, ":imod", 2),

      (item_get_type, ":type", ":item"),
      (assign, ":imod_effect", 0), #default modifier
      (try_begin),
        # horse score = horse_speed*horse_armor*horse_sell_price
        (eq, ":type", itp_type_horse),
        # (item_get_slot, ":horse_speed", ":item", dplmc_slot_item_horse_speed),
        # (item_get_slot, ":horse_armor", ":item", dplmc_slot_item_horse_armor),
        (item_get_horse_speed, ":horse_speed", ":item"),
        (item_get_body_armor, ":horse_armor", ":item"),
        # (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
        (item_get_value, ":i_score", ":item"),
        # (assign, ":i_score", reg0),

        ## SB : price now secondary (additive) instead of multiplicative with actual attributes
        (item_get_horse_speed, ":horse_speed", ":item"),
        (item_get_horse_maneuver, ":horse_manu", ":item"),
        (item_get_body_armor, ":horse_armor", ":item"),
        (item_get_horse_charge_damage, ":horse_charge", ":item"),
        (item_get_hit_points, ":horse_health", ":item"),

        #imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
        #imodbits_horse_good = imodbit_spirited|imodbit_heavy
        (try_begin),
          (eq, ":imod", imod_swaybacked),
          (val_sub, ":horse_speed", 2),
          (val_sub, ":horse_manu", 2),
        (else_try), #do not pick lame horses at all other than last resort
          (eq, ":imod", imod_lame),
          (assign, ":horse_speed", 0),
        (else_try),
          (eq, ":imod", imod_heavy),
          (val_add, ":horse_armor", 3),
          (val_add, ":horse_charge", 4),
          (val_add, ":horse_health", 10),
        (else_try),
          (eq, ":imod", imod_stubborn),
          (val_add, ":horse_health", 5),
        (else_try),
          (eq, ":imod", imod_spirited),
          (val_add, ":horse_speed", 1),
          (val_add, ":horse_manu", 1),
          (val_add, ":horse_armor", 1),
          (val_add, ":horse_charge", 1),
        (else_try),
          (eq, ":imod", imod_champion),
          (val_add, ":horse_speed", 2),
          (val_add, ":horse_manu", 2),
          (val_add, ":horse_armor", 2),
          (val_add, ":horse_charge", 2),
        (try_end),

        (val_mul, ":horse_speed", ":horse_manu"),
        (val_add, ":i_score", ":horse_speed"),

        (val_mul, ":horse_charge", ":horse_armor"),
        (val_mul, ":horse_charge", ":horse_health"),
        (val_div, ":horse_charge", 100),#baseline hp
        (val_add, ":i_score", ":horse_charge"),
      (else_try),
        # shield score = shield_size*shield_armor
        (eq, ":type", itp_type_shield),
        # (item_get_slot, ":shield_size", ":item", dplmc_slot_item_shield_size),
        # (item_get_slot, ":shield_armor", ":item", dplmc_slot_item_shield_armor),

        ## SB : factor in speed and height
        (item_get_shield_height, ":shield_height", ":item"),
        (item_get_weapon_length, ":shield_width", ":item"),
        (item_get_body_armor, ":shield_armor", ":item"),
        (item_get_speed_rating, ":shield_speed", ":item"),
        (item_get_hit_points, ":shield_health", ":item"),

        (try_begin),
          (gt, ":shield_height", 0),
          (val_mul, ":shield_width", ":shield_height"),
          (set_fixed_point_multiplier, 100),
          (store_mul, ":i_score", ":shield_width", 100),
          (store_sqrt, ":i_score", ":i_score"),
          (val_div, ":i_score", 100),
        (else_try),
          # (val_mul, ":shield_width", ":shield_width"),
          (assign, ":i_score", ":shield_width"),
        (try_end),

        #imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
        (try_begin),
          # (eq, ":imod", imod_plain),
          # (assign, ":imod_effect", 0),
        # (else_try),
          (eq, ":imod", imod_cracked),
          (assign, ":imod_effect", -4),
          (val_sub, ":shield_health", 56),
        (else_try),
          (eq, ":imod", imod_battered),
          (assign, ":imod_effect", -2),
          (val_sub, ":shield_health", 26),
        (else_try),
          (eq, ":imod", imod_hardened),
          (assign, ":imod_effect", 3),
        (else_try),
          (eq, ":imod", imod_heavy),
          (assign, ":imod_effect", 3),
          (val_add, ":shield_health", 10),
        (else_try),
          (eq, ":imod", imod_thick),
          (assign, ":imod_effect", 2),
          (val_add, ":shield_health", 47),
        (else_try),
          (eq, ":imod", imod_reinforced),
          (assign, ":imod_effect", 4),
          (val_add, ":shield_health", 83),
        (else_try),
          (eq, ":imod", imod_lordly),
          (assign, ":imod_effect", 6),
          (val_add, ":shield_health", 155),
        (try_end),

        (val_add, ":shield_armor", ":imod_effect"),
        (val_add, ":shield_armor", 5), # add 5 to make sure shield_armor greater than 0
        (val_mul, ":i_score", ":shield_armor"),
        (val_mul, ":i_score", ":shield_speed"),
        (val_div, ":i_score", 92), #average speed of all Native's tableau
        (val_add, ":i_score", ":shield_health"), #tie-breaker
      (else_try),
        # armor score = head_armor + body_armor + foot_armor
        (this_or_next|eq, ":type", itp_type_head_armor),
        (this_or_next|eq, ":type", itp_type_body_armor),
        (this_or_next|eq, ":type", itp_type_foot_armor),
        (eq, ":type", itp_type_hand_armor),
        # (item_get_slot, ":head_armor", ":item", dplmc_slot_item_head_armor),
        # (item_get_slot, ":body_armor", ":item", dplmc_slot_item_body_armor),
        # (item_get_slot, ":leg_armor", ":item", dplmc_slot_item_leg_armor),
        (item_get_head_armor, ":head_armor", ":item"),
        (item_get_body_armor, ":body_armor", ":item"),
        (item_get_leg_armor, ":leg_armor", ":item"),
        (store_add, ":i_score", ":head_armor", ":body_armor"),
        (val_add, ":i_score", ":leg_armor"), # get total base score

        (try_begin),
          # (eq, ":imod", imod_plain),
          # (assign, ":imod_effect", 0),
        # (else_try),
          (eq, ":imod", imod_cracked),
          (assign, ":imod_effect", -4),
        (else_try),
          (eq, ":imod", imod_rusty),
          (assign, ":imod_effect", -3),
        (else_try),
          (eq, ":imod", imod_battered),
          (assign, ":imod_effect", -2),
        (else_try),
          (eq, ":imod", imod_crude),
          (assign, ":imod_effect", -1),
        (else_try),
          (eq, ":imod", imod_tattered),
          (assign, ":imod_effect", -3),
        (else_try),
          (eq, ":imod", imod_ragged),
          (assign, ":imod_effect", -2),
        (else_try),
          (eq, ":imod", imod_sturdy),
          (assign, ":imod_effect", 1),
        (else_try),
          (eq, ":imod", imod_thick),
          (assign, ":imod_effect", 2),
        (else_try),
          (eq, ":imod", imod_hardened),
          (assign, ":imod_effect", 3),
        (else_try),
          (eq, ":imod", imod_reinforced),
          (assign, ":imod_effect", 4),
        (else_try),
          (eq, ":imod", imod_lordly),
          (assign, ":imod_effect", 6),
        (try_end),

        (try_begin), # for armors have 2 or 3 defence of different part
          (neq, ":imod_effect", 0), # and item modifers that matter
          (assign, ":imod_effect_mul", 0),
          (try_begin), #do nothing if no armor part at all
            (gt, ":head_armor", 0),
            (store_add, ":temp_armor", ":head_armor", ":imod_effect"),
                (try_begin), #only calculate if imod degrades item's rating
                    (gt, ":temp_armor", 0),
                    (val_add, ":imod_effect_mul", 1),
                (else_try), #downgrade armor rating to 0 from bad armor instead of going negative
                    (val_sub, ":i_score", ":head_armor"),
                (try_end),
            (try_end),
            (try_begin),
                (gt, ":body_armor", 0),
                (store_add, ":temp_armor", ":body_armor", ":imod_effect"),
                (try_begin),
                    (gt, ":temp_armor", 0),
                    (val_add, ":imod_effect_mul", 1),
                (else_try),
                    (val_sub, ":i_score", ":body_armor"),
                (try_end),
            (try_end),
            (try_begin),
                (gt, ":leg_armor", 0),
                (store_add, ":temp_armor", ":leg_armor", ":imod_effect"),
                (try_begin),
                    (gt, ":temp_armor", 0),
                    (val_add, ":imod_effect_mul", 1),
                (else_try),
                    (val_sub, ":i_score", ":leg_armor"),
                (try_end),
            (try_end),

            (val_mul, ":imod_effect", ":imod_effect_mul"),
            (val_add, ":i_score", ":imod_effect"),
        (try_end),
    (else_try),
        # weapon score = max(swing_damage , thrust_damage)
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (this_or_next|eq, ":type", itp_type_bow),
        (this_or_next|eq, ":type", itp_type_crossbow),
        ##diplomacy start+ add extra types
        #(this_or_next|eq, ":type", itp_type_pistol),
        #(this_or_next|eq, ":type", itp_type_musket),
        ##diplomacy end+
        (eq, ":type", itp_type_polearm),
        (item_get_swing_damage, ":swing_damage", ":item"),
        (item_get_thrust_damage, ":thrust_damage", ":item"),
        (assign, reg1, ":swing_damage"), #sb : debug
        (assign, reg2, ":thrust_damage"), #sb : debug
        # (item_get_slot, ":swing_damage", ":item", dplmc_slot_item_swing_damage),
        # (item_get_slot, ":thrust_damage", ":item", dplmc_slot_item_thrust_damage),
        (val_mod, ":swing_damage", 256), # get actual damage value
        (val_mod, ":thrust_damage", 256),
        (assign, ":i_score", ":swing_damage"),
        (val_max, ":i_score", ":thrust_damage"),
        ##SB : get additional parameters
        (item_get_speed_rating, ":item_speed", ":item"),
        (item_get_weapon_length, ":item_length", ":item"),
        #shootspeed?
        (try_begin),
            # (eq, ":imod", imod_plain),
            # (assign, ":imod_effect", 0),
        # (else_try),
            (eq, ":imod", imod_cracked),
            (assign, ":imod_effect", -5),
        (else_try),
            (eq, ":imod", imod_rusty),
            (assign, ":imod_effect", -3),
        (else_try),
            (eq, ":imod", imod_bent),
            (assign, ":imod_effect", -3),
            (val_sub, ":item_speed", 3),
        (else_try),
            (eq, ":imod", imod_chipped),
            (assign, ":imod_effect", -1),
        (else_try), #SB : add fine
            (eq, ":imod", imod_fine),
            (assign, ":imod_effect", 1),
        (else_try),
            (eq, ":imod", imod_balanced),
            (assign, ":imod_effect", 3),
            (val_add, ":item_speed", 3),
        (else_try),
            (eq, ":imod", imod_tempered),
            (assign, ":imod_effect", 4),
        (else_try),
            (eq, ":imod", imod_masterwork),
            (assign, ":imod_effect", 5),
            (val_add, ":item_speed", 1),
        (else_try),
            (eq, ":imod", imod_heavy),
            (assign, ":imod_effect", 2),
            (val_sub, ":item_speed", 2),
        (else_try),
            (eq, ":imod", imod_strong),
            (assign, ":imod_effect", 3),
            (val_sub, ":item_speed", 3),
        (try_end),
        (val_add, ":i_score", ":imod_effect"),
        (try_begin), #try to pre-filter civilian weapons that are improvised from being looted (clubs, scythes, etc that should be passed over)
            (call_script, "script_cf_melee_weapon_is_civilian", ":item"),
            (val_div, ":i_score", 3),
        (try_end),
        (try_begin), #item_get_missile_speed is technically an important rating for ranged weapons, but we'll pretend NPCs can't math
            (this_or_next|is_between, ":type", itp_type_bow, itp_type_thrown),
            (is_between, ":type", itp_type_pistol, itp_type_bullets),
            (val_mul, ":i_score", ":item_speed"),
        (else_try), #assume base of 100 speed, 100 length
            (this_or_next|eq, ":type", itp_type_one_handed_wpn),
            (eq, ":type", itp_type_two_handed_wpn),
            (val_mul, ":item_length", ":item_speed"),
            (val_mul, ":i_score", ":item_length"),
        (else_try), #length priority over speed
            (eq, ":type", itp_type_polearm),
            (try_begin), #unless they're slashing
                (gt, ":thrust_damage", ":swing_damage"),
                (item_has_property, ":item", itp_couchable),
                # (item_has_property, ":item", itp_cant_use_on_horseback),
                (ge, ":item_length", dplmc_pike_length_cutoff),
                (val_sub, ":item_length", 50), #offset
                #no penalty for war spear range
                (val_max, ":item_length", 100),
                (val_mul, ":item_length", 4),
                #item speed rounded off when we couch
                (val_add, ":item_speed", 25),
                (val_div, ":item_speed", 10),
                # (val_mul, ":item_speed", 2),
            (try_end),
            (val_mul, ":item_length", ":item_speed"),
            (val_mul, ":i_score", ":item_length"),
        (try_end),
    (else_try),
        # ammo score = (thrust_damage + imod_effect)*2
        # a_large_bag will make score added by 1 to discriminate the same ammo with the plain modifier
        (this_or_next|eq, ":type", itp_type_arrows),
        (this_or_next|eq, ":type", itp_type_bolts),
        (eq, ":type", itp_type_thrown),
        (item_get_thrust_damage, ":thrust_damage", ":item"),
        (val_mod, ":thrust_damage", 256), # get actual damage value
        (store_add, ":i_score", ":thrust_damage", 3), # SB : make sure imods do not reduce damage to 0

        #imodbits_missile   = imodbit_bent | imodbit_large_bag
        #imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
        (try_begin),
            (eq, ":imod", imod_plain),
            (val_mul, ":i_score", 2),
        (else_try),
            (eq, ":imod", imod_large_bag),
            (val_mul, ":i_score", 2),
            (val_add, ":i_score", 1),
        (else_try),
            (eq, ":imod", imod_bent),
            (val_sub, ":i_score", 3),
            (val_mul, ":i_score", 2),
        (else_try),
            (eq, ":imod", imod_heavy),
            (val_add, ":i_score", 2),
            (val_mul, ":i_score", 2),
        (else_try),
            (eq, ":imod", imod_balanced),
            (val_add, ":i_score", 3),
            (val_mul, ":i_score", 2),
        (try_end),
    (try_end),

    (assign, reg0, ":i_score"),
]),
#### Autoloot improved by rubik end
####################################
# Let each hero loot from the pool
("dplmc_auto_loot_all", [
    (store_script_param_1, ":pool_troop32"),
    (store_script_param_2, ":sreg"),
    # for all the NPCs, in order of party listing
	(assign, ":sandler", ":sreg"),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
        (is_between, ":this_hero", companions_begin, companions_end),
        #SB : show strings for first iteration
        (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop32", ":sreg"),
        (val_add, ":sreg", 1),
    (try_end),

    #SB : get starting index once again
    (assign, ":sreg", ":sandler"),
    # pick up any discards and format string
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
        (is_between, ":this_hero", companions_begin, companions_end),
        (try_begin), #if first iteration picked up nothing
          (str_is_empty, ":sreg"),
          (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop32", ":sreg"),
        (else_try), #do not overwrite string from first iteration
          (call_script, "script_dplmc_auto_loot_troop", ":this_hero", ":pool_troop32", -1),
        (try_end),
        (try_begin), #skip the first one
          (gt, ":sreg", dplmc_loot_string),
          (neg|str_is_empty, ":sreg"), # in case second hasn't picked up changes either
          (str_store_string_reg, s1, ":sreg"),
          (str_store_string_reg, s0, dplmc_loot_string),
          (str_store_string, dplmc_loot_string, "str_dplmc_s0_newline_s1"),
        (try_end),
        (val_add, ":sreg", 1), #go to next string register
    (try_end),

    #Done. Now sort the remainder
    (troop_sort_inventory, ":pool_troop32"),

]),

####################################
# let this troop take its pick from the loot pool
("dplmc_auto_loot_troop", [
	# (try_begin),
		(store_script_param, ":troop", 1),
		(store_script_param, ":pool", 2),
		(store_script_param, ":sreg", 3), #SB : new param for storing changes

		(troop_get_slot,":upg_armor", ":troop",dplmc_slot_upgrade_armor),
		(troop_get_slot,":upg_horses",":troop",dplmc_slot_upgrade_horse),

		# dump whatever rubbish is in the main inventory
		(troop_get_inventory_capacity, ":inv_cap", ":troop"),
		(try_for_range, ":i_slot", dplmc_ek_alt_items_end, ":inv_cap"), #SB raise from 10, skip over civilian stuff
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
			(troop_add_item, ":pool", ":item", ":imod"), #put it back in the pool
			(troop_set_inventory_slot, ":troop", ":i_slot", -1), # delete it
		(try_end),

        #clear slot
        # (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, dplmc_slot_upgrade_wpn_3 + 1),
          # (troop_slot_eq, ":troop", ":slot_no", 0), #0 is keep
          # (troop_set_slot, "trp_heroes_end", ":slot_no", 999999),
        # (else_try), #otherwise we reset to default
          # (troop_set_slot, "trp_heroes_end", ":slot_no", -1),
        # (try_end),

        #SB : loop, calculate current item's score
        # (assign, ":slot_no", dplmc_slot_upgrade_wpn_0 - 1),
        (try_for_range, ":item_slot", ek_item_0, ek_head),
          #SB : clear the pool troop's ek_slots
          (troop_set_inventory_slot, ":pool", ":item_slot", -1), #delete it
          (store_add, ":slot_no", dplmc_slot_upgrade_wpn_0, ":item_slot"), #pre-increment
          (troop_get_slot, ":item_preference", ":troop", ":slot_no"),
          (gt, ":item_preference", 0), #0 is keep
          (troop_get_inventory_slot, ":item", ":troop", ":item_slot"),
          (ge, ":item", 0), #initial item check
          (troop_get_inventory_slot_modifier, ":imod", ":troop", ":item_slot"),

          (try_begin),
            (store_mod, ":item_type", ":item_preference", meta_itp_mask),
            (item_get_type, ":itp", ":item"),
            (neq, ":itp", ":item_type"),
            (troop_set_inventory_slot, ":troop", ":item_slot", -1), #delete it
            (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
            (assign, ":item", -1), #so we fail this loop
          (try_end),
          (ge, ":item", 0),
          #SB : cache the original equipment to see changes
          (troop_set_inventory_slot, ":pool", ":item_slot", ":item"),
          (troop_set_inventory_slot_modifier, ":pool", ":item_slot", ":imod"),

          (call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
          (assign, ":cur_value", reg0),
          #check to see whether damage is preferred
          (try_begin),
            (call_script, "script_cf_item_type_has_advanced_autoloot", ":item_type"),
            (store_div, ":dmg_type", ":item_preference", meta_dmg_mask),
            (neq, ":dmg_type", 0),
            (item_get_swing_damage, ":swing_damage", ":item"),
            (item_get_thrust_damage, ":thrust_damage", ":item"),
            (try_begin),
              (ge, ":swing_damage", ":thrust_damage"),
              (item_get_swing_damage_type, ":item_dmg_type", ":item"),
            (else_try),
              (lt, ":swing_damage", ":thrust_damage"),
              (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
            (try_end),
            #check if it matches preference
            (val_add, ":item_dmg_type", 1),
            (eq, ":dmg_type", ":item_dmg_type"),
            (val_mul, ":cur_value", 4),
          (try_end),
          (troop_set_slot, "trp_heroes_end", ":slot_no", ":cur_value"),
        (else_try),
          (eq, ":item_preference", 0), #0 is keep
          (troop_set_slot, "trp_heroes_end", ":slot_no", 999999),
        (else_try), #whether no item or discarded
          (lt, ":item", 0),
          (troop_set_slot, "trp_heroes_end", ":slot_no", 0),
        (try_end),

        # (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, dplmc_slot_upgrade_wpn_3 + 1),
          # (troop_get_slot, reg0, ":troop", ":slot_no"),
          # (troop_get_slot, reg1, "trp_heroes_end", ":slot_no"),
          # (store_sub, reg2, ":slot_no", dplmc_slot_upgrade_wpn_0),
          # (troop_get_inventory_slot, ":item", ":troop", reg2),
          # (try_begin),
            # (eq, ":item", -1),
            # (str_store_string, s1, "str_dplmc_none"),
          # (else_try),
            # (str_store_item_name, s1, ":item"),
          # (try_end),

          # (display_message, "@upgrading slot {reg2} with {reg0}, cur score for {s1}: {reg1}"),
        # (try_end),

		(try_for_range, ":i_slot", ek_head, ek_food),
			(troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
            (troop_set_inventory_slot, ":pool", ":i_slot", -1), #delete it
			(ge, ":item", 0),
            (troop_set_inventory_slot, ":pool", ":i_slot", ":item"), #store it
			(troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
            (troop_set_inventory_slot_modifier, ":pool", ":i_slot", ":imod"), #store it
			(try_begin),
				(neq, ":upg_armor", 0), # we're upgrading armors
				(is_between, ":i_slot", ek_head, ek_horse), # it's an armor slot
				(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
				(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(else_try),
				(neq, ":upg_horses", 0), # we're upgrading horses
				(eq, ":i_slot", ek_horse), # it's a horse slot
				(troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
				(troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
			(try_end),
		(try_end),

		# clear best matches
		(assign, ":best_helmet_slot", -1),
		(assign, ":best_helmet_val", 0),
		(assign, ":best_body_slot", -1),
		(assign, ":best_body_val", 0),
		(assign, ":best_boots_slot", -1),
		(assign, ":best_boots_val", 0),
		(assign, ":best_gloves_slot", -1),
		(assign, ":best_gloves_val", 0),
		(assign, ":best_horse_slot", -1),
		(assign, ":best_horse_val", 0),

		# Now search through the pool for the best items
		(troop_get_inventory_capacity, ":inv_cap", ":pool"),
		(try_for_range, ":i_slot", ek_food + 1, ":inv_cap"), #SB: skip cached items
			(troop_get_inventory_slot, ":item", ":pool", ":i_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":i_slot"),
			(call_script, "script_dplmc_troop_can_use_item", ":troop", ":item", ":imod"),
			(eq, reg0, 1), # can use
			#(call_script, "script_get_item_value_with_imod", ":item", ":imod"), # use the following instead

			#### Autoloot improved by rubik begin
			# get item_score instead of price
			(call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
			#### Autoloot improved by rubik end
			(assign, ":score", reg0),
			(item_get_type, ":item_type", ":item"),

			(try_begin),
				(eq, ":item_type", itp_type_horse), #it's a horse
				(eq, ":upg_horses", 1), # we're upgrading horses
				(gt, ":score", ":best_horse_val"),
				(assign, ":best_horse_slot", ":i_slot"),
				(assign, ":best_horse_val", ":score"),
			(else_try), #SB : move armor checks here
				(is_between, ":item_type", itp_type_head_armor, itp_type_hand_armor + 1), # we're checking armor
				(eq, ":upg_armor", 1), # we're upgrading armor
				(try_begin),
					(eq, ":item_type", itp_type_head_armor),
					(gt, ":score", ":best_helmet_val"),
					(assign, ":best_helmet_slot", ":i_slot"),
					(assign, ":best_helmet_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_body_armor),
					(gt, ":score", ":best_body_val"),
					(assign, ":best_body_slot", ":i_slot"),
					(assign, ":best_body_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_foot_armor),
					(gt, ":score", ":best_boots_val"),
					(assign, ":best_boots_slot", ":i_slot"),
					(assign, ":best_boots_val", ":score"),
				(else_try),
					(eq, ":item_type", itp_type_hand_armor),
					(gt, ":score", ":best_gloves_val"),
					(assign, ":best_gloves_slot", ":i_slot"),
					(assign, ":best_gloves_val", ":score"),
				(try_end),
            (else_try), #SB : move weapon checks back here
              (assign, ":limit", dplmc_slot_upgrade_wpn_3 + 1),
              (try_begin), #check for denying use on horseback
                  (this_or_next|gt, ":best_horse_val", 0),
                  (eq, ":upg_horses", 1), # we're upgrading horses
                  (this_or_next|item_has_property, ":item", itp_cant_use_on_horseback),
                  (this_or_next|item_has_property, ":item", itp_cant_reload_on_horseback),
                  (item_has_property, ":item", itp_cant_reload_while_moving_mounted),
                  (assign, ":limit", 0),
              (try_end),
              (try_for_range, ":slot_no", dplmc_slot_upgrade_wpn_0, ":limit"),
                (troop_get_slot, ":item_preference", ":troop", ":slot_no"),
                (neq, ":item_preference", 0), #not keep current
                (store_div, ":damage_type", ":item_preference", meta_dmg_mask),
                (val_mod, ":item_preference", meta_dmg_mask), #get the itp + meta
                (call_script, "script_item_get_type_aux", ":item"),
                (this_or_next|eq, ":item_preference", reg0), #either same meta-type
                (eq, ":item_preference", ":item_type"), #or matching base itp

                #check to see whether damage is preferred
                (try_begin),
                  (neq, ":damage_type", 0),
                  (item_get_swing_damage, ":swing_damage", ":item"),
                  (item_get_thrust_damage, ":thrust_damage", ":item"),
                  (try_begin),
                    (ge, ":swing_damage", ":thrust_damage"),
                    (item_get_swing_damage_type, ":item_dmg_type", ":item"),
                  (else_try),
                    (lt, ":swing_damage", ":thrust_damage"),
                    (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
                  (try_end),
                  #check if it matches preference
                  (val_add, ":item_dmg_type", 1),
                  (eq, ":damage_type", ":item_dmg_type"),
                  (val_mul, ":score", 4),
                (try_end),
                #if current score is not ge, replace item and score
                (neg|troop_slot_ge, "trp_heroes_end", ":slot_no", ":score"),
                (troop_set_slot, "trp_heroes_end", ":slot_no", ":score"),
                (assign, ":limit", -1), #loop break
                (store_sub, ":item_slot", ":slot_no", dplmc_slot_upgrade_wpn_0), #ek item slots
                (troop_get_inventory_slot, ":item_no", ":troop", ":item_slot"),
                (try_begin),
                  (eq, ":item_no", -1),
                  (troop_set_inventory_slot, ":pool", ":i_slot", -1),
                (else_try), #replace into pool
                  (troop_get_inventory_slot_modifier, ":imod_no", ":troop", ":item_slot"),
                  (troop_set_inventory_slot, ":pool", ":i_slot", ":item_no"),
                  (troop_set_inventory_slot_modifier, ":pool", ":i_slot", ":imod_no"),
                (try_end),
                (troop_set_inventory_slot, ":troop", ":item_slot", ":item"),
                (troop_set_inventory_slot_modifier, ":troop", ":item_slot", ":imod"),
                # (try_begin),
                  # (str_store_item_name, s1, ":item"),
                  # (try_begin),
                    # (eq, ":item_no", -1),
                    # (str_store_string, s2, "str_dplmc_none"),
                  # (else_try),
                    # (str_store_item_name, s2, ":item_no"),
                  # (try_end),
                  # (assign, reg1, ":score"),
                  # (display_message, "@{s1} better than {s2}, score of {reg1}"),
                # (try_end),
              (try_end),
            (try_end),
        (try_end),

		# Now we know which ones are the best. Give them to the troop.
		(try_begin),
			(assign, ":best_slot", ":best_helmet_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_head, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_head, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_body_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_body, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_body, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_boots_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_foot, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_foot, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_gloves_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_gloves, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_gloves, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		(try_begin),
			(assign, ":best_slot", ":best_horse_slot"),
			(ge, ":best_slot", 0),
			(troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
			(ge, ":item", 0),
			(troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			(troop_set_inventory_slot, ":troop", ek_horse, ":item"),
			(troop_set_inventory_slot_modifier, ":troop", ek_horse, ":imod"),
			(troop_set_inventory_slot, ":pool", ":best_slot", -1),
		(try_end),

		# (try_for_range, ":i_slot", ek_item_0, ek_head),
			# (store_add, ":trp_slot", ":i_slot", dplmc_slot_upgrade_wpn_0),
			# (troop_get_slot, ":type", ":troop", ":trp_slot"),
			# (gt, ":type", 0), #we're upgrading for this slot
			# (call_script, "script_dplmc_scan_for_best_item_of_type", ":pool", ":type", ":troop"), #search for the best
			# (assign, ":best_slot", reg0),
			# (neq, ":best_slot", -1), #got something
			# (troop_get_inventory_slot, ":item", ":pool", ":best_slot"), #get it
			# (ge, ":item", 0),
			# (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
			# (troop_set_inventory_slot, ":pool", ":best_slot", -1), #remove from pool
			# (troop_set_inventory_slot, ":troop", ":i_slot", ":item"), #add to slot
			# (troop_set_inventory_slot_modifier, ":troop", ":i_slot", ":imod"),
		# (try_end),

        #SB : string storage
        (try_begin),
          (neq, ":sreg", -1),
          (str_store_troop_name, ":sreg", ":troop"),
          (assign, ":num_changes", 0),
          (assign, ":last_change", 0),
          #three cases : discarded item -1, no change 0, change 1 (upgraded/swapped depending on item flags)
          (try_for_range, ":i_slot", ek_item_0, ek_food),
            (troop_get_inventory_slot, ":old_item", ":pool", ":i_slot"),
            (troop_get_inventory_slot, ":new_item", ":troop", ":i_slot"),
            (try_begin),
              (gt, ":old_item", -1),
              (troop_get_inventory_slot_modifier, ":old_imod", ":pool", ":i_slot"),
              (store_add, ":imod_no", ":old_imod", "str_imod_plain"),
              # (str_store_string, s10, ":imod_no"),
              # (str_store_item_name, s20, ":old_item"),
              # (display_message, "@old:{s10}{s20}"),
            (else_try),
              (assign, ":old_imod", imod_plain),
            (try_end),
            (try_begin),
              (gt, ":new_item", -1),
              (troop_get_inventory_slot_modifier, ":new_imod", ":troop", ":i_slot"),
              (store_add, ":imod_no", ":new_imod", "str_imod_plain"),
              # (str_store_string, s10, ":imod_no"),
              # (str_store_item_name, s20, ":new_item"),
              # (display_message, "@new:{s10}{s20}"),
            (else_try),
              (assign, ":new_imod", imod_plain),
            (try_end),

            # #placeholder swap strings
            # (str_clear, s0), #sreg
            # (str_clear, s1), #new string
            # (str_clear, s10), #imod
            # (str_clear, s20), #item

            (try_begin), #keep current
              (is_between, ":i_slot", ek_item_0, ek_head),
              (store_add, ":upgrade_slot", ":i_slot", dplmc_slot_upgrade_wpn_0),
              (troop_slot_eq, ":troop", ":upgrade_slot", 0),
              (assign, ":item_changed", 0),
            (else_try), #same
              (eq, ":new_item", ":old_item"),
              (eq, ":old_imod", ":new_imod"),
              (assign, ":item_changed", 0),
            (else_try), #discarded
              (eq, ":new_item", -1),
              (gt, ":old_item", -1),
              (assign, ":item_changed", 2),
              (assign, ":item_no", ":old_item"),
              (assign, ":imod_no", ":old_imod"),
            (else_try), #swapped/equipped
              (gt, ":new_item", -1),
              (assign, ":item_changed", 1),
              (assign, ":item_no", ":new_item"),
              (assign, ":imod_no", ":new_imod"),
            (try_end),

            #build string
            (try_begin),
              (gt, ":item_changed", 0),
              (val_add, ":imod_no", "str_imod_plain"),
              (str_store_string, s10, ":imod_no"), #this comes with a space
              (str_store_item_name, s20, ":item_no"),

              (try_begin),
                (neq, ":last_change", 1),
                (eq, ":item_changed", 1),
                (str_store_string, s1, "@equipped {s10}{s20}"),
              (else_try),
                (neq, ":last_change", 2),
                (eq, ":item_changed", 2),
                (str_store_string, s1, "@discarded {s10}{s20}"),
              (else_try), #same as before, no need to qualify
                (str_store_string, s1, "@{s10}{s20}"),
              (try_end),
              (str_store_string_reg, s0, ":sreg"),
              (try_begin), #no comma for first part
                (eq, ":num_changes", 0),
                (str_store_string, ":sreg", "str_s0_s1"),
              (else_try),
                (str_store_string, ":sreg", "str_dplmc_s0_comma_s1"),
              (try_end),
              # (assign, reg1, ":num_changes"),
              # (display_message, "@{reg1} : {s1}"),
              (val_add, ":num_changes", ":item_changed"),
              (assign, ":last_change", ":item_changed"),
            (try_end),
          (try_end),
          (try_begin), #discard if we didn't touch the inventory at all
            (le, ":num_changes", 0), #this is a flag, not a count
            (str_clear, ":sreg"),
          (try_end),
        (try_end),

    # (try_end),
]),

#######################
# Search for the most expensive item of a specified type
##diplomacy start+
#"script_dplmc_scan_for_best_item_of_type"
#
#INPUT:
#   arg1 :troop
#   arg2 :item_type
#   arg3 :troop_using
#
#OUTPUT:
#   reg0 index of best item (-1 if not found)
##diplomacy end+
("dplmc_scan_for_best_item_of_type", [
	(store_script_param, ":troop",1),
	(store_script_param, ":item_type",2),
	(store_script_param, ":troop_using", 3),

    #SB : parse damage type and meta type (if any)
    # (store_div, ":dmg_type", ":item_type", meta_dmg_mask),
    (store_mod, ":meta_type", ":item_type", meta_dmg_mask), #use this instead
    (store_mod, ":item_type", ":meta_type", meta_itp_mask), #base type

    (assign, ":best_slot", -1),
    (assign, ":best_value", -1),
    # iterate through the list of items
    (troop_get_inventory_capacity, ":inv_cap", ":troop"),
    (try_for_range, ":i_slot", 0, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
        (ge, ":item", 0),
        (troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
        #(item_get_type, ":this_item_type", ":item"), use the following instead

        # #### Autoloot improved by rubik begin
        # (try_begin),
            # # (item_slot_eq, ":item", dplmc_slot_two_handed_one_handed, 1),
            # (item_has_property, ":item", itp_type_two_handed_wpn),
            # (neg|item_has_property, ":item", itp_two_handed),
            # (assign, ":this_item_type", 11), # type 11 = two-handed/one-handed
        # (else_try),
            # (item_get_type, ":this_item_type", ":item"),
        # (try_end),
        # #### Autoloot improved by rubik end
        (call_script, "script_item_get_type_aux", ":item"), #SB : compare metatype
        (eq, ":meta_type", reg0), # it's one of the kind we're looking for (meta-type holds itp if none exists)
        (call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":item", ":imod"),
        (eq, reg0, 1), # can use
        #(call_script, "script_get_item_value_with_imod", ":item", ":imod"), # use the following instead

        #### Autoloot improved by rubik begin
        # get item_score instead of price
        (call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
        #### Autoloot improved by rubik end
        (assign, ":cur_value", reg0),
        #SB : adjust value here for damage preference
        # (try_begin),
          # (call_script, "script_cf_item_type_has_advanced_autoloot", ":item_type"),
          # (item_get_swing_damage, ":swing_damage", ":item"),
          # (item_get_thrust_damage, ":thrust_damage", ":item"),
          # (try_begin),
            # (ge, ":swing_damage", ":thrust_damage"),
            # (item_get_swing_damage_type, ":item_dmg_type", ":item"),
          # (else_try),
            # (lt, ":swing_damage", ":thrust_damage"),
            # (item_get_thrust_damage_type, ":item_dmg_type", ":item"),
          # (try_end),
          # #check if it matches preference
          # (eq, ":dmg_type", ":item_dmg_type"),
          # (val_mul, ":cur_value", 3),
        # (try_end),
        (gt, ":cur_value", ":best_value"), # best one we've seen yet
        (assign, ":best_slot", ":i_slot"),
        (assign, ":best_value", ":cur_value"),
    (try_end),

    # return the slot of the best one
    (assign, reg0, ":best_slot"),
]),

##diplomacy start+
#"script_dplmc_count_better_items_of_same_type"
#
#INPUT:
#   arg1 :inventory_troop
#   arg2 :item
#   arg2 :item_imod
#   arg3 :troop_using
#
#OUTPUT:
#   reg0 number of items of same type
("dplmc_count_better_items_of_same_type", [
	(store_script_param, ":inventory_troop",1),
	(store_script_param, ":base_item",2),
	(store_script_param, ":base_imod",3),
	(store_script_param, ":troop_using", 4),

	(assign, ":number_better_of_type", 0),
	#(assign, ":total_items_of_type", 0),

	# (item_get_type, ":main_item_type", ":base_item"),
	# (try_begin),
		# (item_has_property, ":item", itp_type_two_handed_wpn),
		# (neg|item_has_property, ":item", itp_two_handed),
		# (assign, ":main_item_type", 11), # type 11 = two-handed/one-handed
	# (try_end),
    #SB : metatype
    (call_script, "script_item_get_type_aux", ":base_item"),
    (assign, ":main_item_type", reg0),

	(call_script, "script_dplmc_get_item_score_with_imod", ":base_item", ":base_imod"),
	(assign, ":primary_score", reg0),

	(call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":base_item", ":base_imod"),
	(assign, ":can_use", 1),
	(try_begin),
		(neq, reg0, 1),
		(assign, ":primary_score", -1000),
		(assign, ":can_use", 0),
	(try_end),
	(assign, ":exact_matches_found", 0),

	(troop_get_inventory_capacity, ":inv_cap", ":inventory_troop"),
	(try_for_range, ":i_slot", 0, ":inv_cap"),
		(troop_get_inventory_slot, ":item", ":inventory_troop", ":i_slot"),
		(ge, ":item", 0),
        # SB : metatype
        (call_script, "script_item_get_type_aux", ":item"),
		(eq, ":main_item_type", reg0),
		#(val_add, ":total_items_of_type", 1),
		(troop_get_inventory_slot_modifier, ":imod", ":inventory_troop", ":i_slot"),
		(call_script, "script_dplmc_troop_can_use_item", ":troop_using", ":item", ":imod"),
		(this_or_next|eq, ":can_use", 0),
			(ge, reg0, 1),
		(try_begin),
			(eq, ":item", ":base_item"),
			(eq, ":imod", ":base_imod"),
			(val_add, ":exact_matches_found", 1),
		(try_end),
		(this_or_next|neq, ":item", ":base_item"),
		(this_or_next|neq, ":imod", ":base_imod"),
			(ge, ":exact_matches_found", 2),
		(call_script, "script_dplmc_get_item_score_with_imod", ":item", ":imod"),
		(ge, reg0, ":primary_score"),#deliberately ge instead of gt because of what I want this for
		(val_add, ":number_better_of_type", 1),
	(try_end),

	(assign, reg0, ":number_better_of_type"),
	#(assign, reg1, ":total_items_of_type"),
]),

("dplmc_copy_upgrade_to_all_heroes",[
    (store_script_param_1, ":troop"),
    (store_script_param_2, ":type"),
    (try_begin),
        (eq, ":type", dplmc_wpn_setting_1),
        (troop_get_slot,":upg_wpn0", ":troop",dplmc_slot_upgrade_wpn_0),
        (troop_get_slot,":upg_wpn1", ":troop",dplmc_slot_upgrade_wpn_1),
        (troop_get_slot,":upg_wpn2", ":troop",dplmc_slot_upgrade_wpn_2),
        (troop_get_slot,":upg_wpn3", ":troop",dplmc_slot_upgrade_wpn_3),
        (try_for_range, ":hero", companions_begin, companions_end),
            (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_0,":upg_wpn0"),
            (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_1,":upg_wpn1"),
            (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_2,":upg_wpn2"),
            (troop_set_slot,":hero",dplmc_slot_upgrade_wpn_3,":upg_wpn3"),
        (try_end),
    (else_try),
        (eq, ":type", dplmc_armor_setting),
        (troop_get_slot,":upg_armor", ":troop",dplmc_slot_upgrade_armor),
        (try_for_range, ":hero", companions_begin, companions_end),
            (troop_set_slot,":hero",dplmc_slot_upgrade_armor,":upg_armor"),
        (try_end),
    (else_try),
        (eq, ":type", dplmc_horse_setting),
        (troop_get_slot,":upg_horse", ":troop",dplmc_slot_upgrade_horse),
        (try_for_range, ":hero", companions_begin, companions_end),
            (troop_set_slot,":hero",dplmc_slot_upgrade_horse,":upg_horse"),
        (try_end),
    (try_end),
]),

("dplmc_get_current_item_for_autoloot",[
    (store_script_param_1, ":slot_no"),

    #(try_begin),
    (assign, ":dest_slot", ":slot_no"),
    (troop_get_inventory_slot, ":item", "$temp", ":dest_slot"),
    #(else_try),
    #  (store_sub, ":dest_slot", "$temp", companions_begin),
    #  (val_mul, ":dest_slot", 4),
    #  (val_add, ":dest_slot", 10),
    #  (val_add, ":dest_slot", ":slot_no"),
    #  (troop_get_inventory_slot, ":item", "trp_merchants_end", ":dest_slot"),
    #(try_end),
    (try_begin),
        (ge, ":item", 0),
        (str_store_item_name, s10, ":item"),
    (else_try),
        (str_store_string, s10, "str_dplmc_none"),
    (try_end),
]),

("dplmc_get_troop_max_hp",[
    (store_script_param_1, ":troop"),

    (store_skill_level, ":skill", "skl_ironflesh", ":troop"),
    (store_attribute_level, ":attrib", ":troop", ca_strength),
    (val_mul, ":skill", 2),
    (val_add, ":skill", ":attrib"),
    (val_add, ":skill", 35),
    (assign, reg0, ":skill"),
]),

("dplmc_describe_prosperity_to_s4",[
    (store_script_param_1, ":center_no"),

    (str_store_party_name, s60,":center_no"),
    (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    (str_store_string, s4, "str_empty_string"),
    (try_begin),
        (is_between, ":center_no", towns_begin, towns_end),
        (try_begin),
            (eq, ":prosperity", 0),
            (str_store_string, s4, "str_town_prosperity_0"),
        (else_try),
            (is_between, ":prosperity", 1, 11),
            (str_store_string, s4, "str_town_prosperity_10"),
        (else_try),
            (is_between, ":prosperity", 11, 21),
            (str_store_string, s4, "str_town_prosperity_20"),
        (else_try),
            (is_between, ":prosperity", 21, 31),
            (str_store_string, s4, "str_town_prosperity_30"),
        (else_try),
            (is_between, ":prosperity", 31, 41),
            (str_store_string, s4, "str_town_prosperity_40"),
        (else_try),
            (is_between, ":prosperity", 41, 51),
            (str_store_string, s4, "str_town_prosperity_50"),
        (else_try),
            (is_between, ":prosperity", 51, 61),
            (str_store_string, s4, "str_town_prosperity_60"),
        (else_try),
            (is_between, ":prosperity", 61, 71),
            (str_store_string, s4, "str_town_prosperity_70"),
        (else_try),
            (is_between, ":prosperity", 71, 81),
            (str_store_string, s4, "str_town_prosperity_80"),
        (else_try),
            (is_between, ":prosperity", 81, 91),
            (str_store_string, s4, "str_town_prosperity_90"),
        (else_try),
            (is_between, ":prosperity", 91, 101),
            (str_store_string, s4, "str_town_prosperity_100"),
        (try_end),
    (else_try),
        (is_between, ":center_no", villages_begin, villages_end),
        (try_begin),
            (eq, ":prosperity", 0),
            (str_store_string, s4, "str_village_prosperity_0"),
        (else_try),
            (is_between, ":prosperity", 1, 11),
            (str_store_string, s4, "str_village_prosperity_10"),
        (else_try),
            (is_between, ":prosperity", 11, 21),
            (str_store_string, s4, "str_village_prosperity_20"),
        (else_try),
            (is_between, ":prosperity", 21, 31),
            (str_store_string, s4, "str_village_prosperity_30"),
        (else_try),
            (is_between, ":prosperity", 31, 41),
            (str_store_string, s4, "str_village_prosperity_40"),
        (else_try),
            (is_between, ":prosperity", 41, 51),
            (str_store_string, s4, "str_village_prosperity_50"),
        (else_try),
            (is_between, ":prosperity", 51, 61),
            (str_store_string, s4, "str_village_prosperity_60"),
        (else_try),
            (is_between, ":prosperity", 61, 71),
            (str_store_string, s4, "str_village_prosperity_70"),
        (else_try),
            (is_between, ":prosperity", 71, 81),
            (str_store_string, s4, "str_village_prosperity_80"),
        (else_try),
            (is_between, ":prosperity", 81, 91),
            (str_store_string, s4, "str_village_prosperity_90"),
        (else_try),
            (is_between, ":prosperity", 91, 101),
            (str_store_string, s4, "str_village_prosperity_100"),
        (try_end),
    (try_end),
]),


("dplmc_pay_into_treasury",[
    (store_script_param_1, ":amount"),
    (troop_add_gold, "trp_household_possessions", ":amount"),
    (assign, reg0, ":amount"),
    (play_sound, "snd_money_received"),
    (display_message, "@{reg0} denarii added to treasury.", color_good_news),
]),

("dplmc_withdraw_from_treasury", [
    (store_script_param_1, ":amount"),
    (troop_remove_gold, "trp_household_possessions", ":amount"),
    (assign, reg0, ":amount"),
    (play_sound, "snd_money_paid"),
    (display_message, "@{reg0} denarii removed from treasury.", color_bad_news),
]),

("dplmc_describe_tax_rate_to_s50",[
    (store_script_param_1, ":tax_rate"),
    (val_div, ":tax_rate", 25),
    (store_add, ":str_id","str_dplmc_tax_normal", ":tax_rate"),
    (str_store_string, s50, ":str_id"),
]),

("dplmc_player_troops_leave",[
    (store_script_param_1, ":percent"),
    (try_begin),#debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":percent"),
        (display_message, "@{!}DEBUG : removing player troops: {reg0}%"),
    (try_end),
    (assign, ":deserters", 0),
    (try_for_parties, ":party_no"),
        (assign, ":remove_troops", 0),
        (try_begin),
            (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
            (party_slot_eq, ":party_no", slot_party_type, spt_castle),
            (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
            (assign, ":remove_troops", 1),
        (else_try),
            (eq, "p_main_party", ":party_no"),
            (assign, ":remove_troops", 1),
        (try_end),
        (eq, ":remove_troops", 1),
        (party_get_num_companion_stacks, ":num_stacks",":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
            (val_mul, ":stack_size", ":percent"),
            (val_div, ":stack_size", 100),
            (party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
            (party_remove_members, ":party_no", ":troop_id", ":stack_size"),
            (val_add, ":deserters", ":stack_size"),
        (try_end),
    (try_end),
    (assign, reg0, ":deserters"),
]),
("dplmc_get_item_buy_price_factor",[
	##nested diplomacy start+
    #(store_script_param_1, ":item_kind_id"),
    #(store_script_param_2, ":center_no"),
	#Add two parameters
	(store_script_param, ":item_kind_id", 1),
	(store_script_param, ":center_no", 2),
	(store_script_param, ":customer_no", 3),
	(store_script_param, ":merchant_no", 4),
	##nested diplomacy start+
    (assign, ":price_factor", 100),

	##nested diplomacy start+
    #(call_script, "script_get_trade_penalty", ":item_kind_id"),
	(call_script, "script_dplmc_get_trade_penalty", ":item_kind_id", ":center_no", ":customer_no", ":merchant_no"),
	##nested diplomacy end+
    (assign, ":trade_penalty", reg0),

    (try_begin),
	  ##nested diplomacy start+
	  (gt, ":center_no", 0),
  	  (this_or_next|is_between, ":center_no", centers_begin, centers_end),
		(party_is_active, ":center_no"),

	  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
	  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
	  ##nested diplomacy end+
      (is_between, ":center_no", centers_begin, centers_end),
      (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
      (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
      (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
      (party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),

      (try_begin),
		##nested diplomacy start+
		#OLD:
        #(is_between, ":center_no", villages_begin, villages_end),
        #(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
		##NEW:
		(gt, ":center_no", 0),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
			(is_between, ":center_no", villages_begin, villages_end),
		(party_get_slot, ":market_town", ":center_no", slot_village_market_town),

		(ge, ":market_town", centers_begin),
		(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_town),
		(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_village),
			(is_between, ":market_town", centers_begin, centers_end),
		##nested diplomacy end+
        (party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
        (val_max, ":price_factor", ":price_in_market_town"),
      (try_end),
	  ##nested diplomacy start+
	  #Enforce constraints
	  (val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor + 1),
	  ##nested diplomacy end+

      #For villages, the good will be sold no cheaper than in the market town
      #This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers

      (val_mul, ":price_factor", 100), #normalize price factor to range 0..100
      (val_div, ":price_factor", average_price_factor),
    (try_end),

    (store_add, ":penalty_factor", 100, ":trade_penalty"),

    (val_mul, ":price_factor", ":penalty_factor"),
    (val_div, ":price_factor", 100),

    (assign, reg0, ":price_factor"),
    (set_trigger_result, reg0),
]),
("dplmc_party_calculate_strength",[
    (store_script_param_1, ":party"), #Party_id
    (store_script_param_2, ":exclude_leader"), #Party_id
    (assign, reg0,0),
    (party_get_num_companion_stacks, ":num_stacks", ":party"),
    (assign, ":first_stack", 0),
    (try_begin),
        (neq, ":exclude_leader", 0),
        (assign, ":first_stack", 1),
    (try_end),
    (assign, ":sum", 0),
    (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
        (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size",":party",":i_stack"),
        (try_end),
        (val_add, ":sum", ":stack_size"),
    (try_end),
    (assign, reg0, ":sum"),
    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (display_message, "@{!}DEBUG : sum: {reg0}"),
    (try_end),
]),

#script_dplmc_start_tributary_between_kingdoms, 20 days alliance, 40 days truce after that
# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
# Output: none
#sets relations between two kingdoms
("dplmc_start_tributary_between_kingdoms", [
    (store_script_param, ":kingdom_a", 1),##a has been subjugated
    (store_script_param, ":kingdom_b", 2),
    (store_script_param, ":initializing_war_peace_cond", 3),

    (faction_set_slot, ":kingdom_a", slot_faction_tributary_of, ":kingdom_b"),

    (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
    (val_add, ":relation", 15),
    (val_max, ":relation", 40),
    (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
    (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

    (try_begin),
        (faction_get_slot, ":king_a", ":kingdom_a", slot_faction_leader),
        (faction_get_slot, ":king_b", ":kingdom_b", slot_faction_leader),
        (call_script, "script_add_to_troop_wealth", ":king_a", -20000),#pays tribute
        (call_script, "script_add_to_troop_wealth", ":king_b", 20000),#gains tribute
    (try_end),
    (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
        (faction_set_slot, ":kingdom_b", slot_faction_recognized_player, 1),##they will recognize player
    (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
        (faction_set_slot, ":kingdom_a", slot_faction_recognized_player, 1),##they will recognize player
    (try_end),

    (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        ##diplomacy start+ #Due to complaints about the wording
            #(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
        (display_log_message, "@The {s1} have been subjugated by {s2}."),
        ##diplomacy end+

        (call_script, "script_add_notification_menu", "mnu_dplmc_notification_tribute_declared", ":kingdom_a", ":kingdom_b"),

        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),
    (try_end),

    (try_begin), #add truce
        (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        ##nested diplomacy start+ replace 80 with a named constant
        #(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
        (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_tributary_days_initial),
        ##nested diplomacy end+

        (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        ##nested diplomacy start+ replace 80 with a named constant
        #(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
        (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_tributary_days_initial),
        ##nested diplomacy end+

        (store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
        (faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
        (try_begin),
            (lt, ":damage_inflicted_by_a", 100),
            #controversial policy
        (try_end),
        (faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

        (store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
        (faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
        (try_begin),
            (lt, ":damage_inflicted_by_b", 100),
            #controversial policy
        (try_end),
        (faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
    (try_end),
    # stop wars
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":kingdom_a", ":faction_no"),
        (neq, ":kingdom_b", ":faction_no"),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
        #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
        (eq, reg0, -2),
        # MOTO build explanation string chief
        (assign, "$g_last_acting_faction", ":kingdom_b"),
        (assign, "$g_last_target_faction", ":faction_no"),
        (str_store_faction_name, s15, ":kingdom_a"),
        (str_store_faction_name, s16, ":faction_no"),
        (str_store_string, s64, "@Since {s15} has been subjugated, a peace will be signed with {s16}."),
        # MOTO build explanation string end
        (call_script, "script_diplomacy_start_peace_between_kingdoms",":kingdom_a", ":faction_no", 1),
        # (ge, reg0, -1),

        # # MOTO build explanation string chief
        # (assign, "$g_last_acting_faction", ":kingdom_b"),
        # (assign, "$g_last_target_faction", ":faction_no"),
        # (str_store_faction_name, s15, ":kingdom_b"),
        # (str_store_faction_name, s16, ":faction_no"),
        # (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
        # # MOTO build explanation string end

        # (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", logent_faction_declares_war_to_fulfil_pact), 	#MOTO chief pass log entries
        # (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 2),
    (try_end),
    ## a is now at war with whom ever b is at war
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":kingdom_a", ":faction_no"),
        (neq, ":kingdom_b", ":faction_no"),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
        #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
        (eq, reg0, -2),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
        (ge, reg0, -1),

        # MOTO build explanation string chief
        (assign, "$g_last_acting_faction", ":kingdom_a"),
        (assign, "$g_last_target_faction", ":faction_no"),
        (str_store_faction_name, s15, ":kingdom_a"),
        (str_store_faction_name, s16, ":faction_no"),
        (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
        # MOTO build explanation string end

        (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", logent_faction_declares_war_to_fulfil_pact), 	#MOTO chief pass log entries
        #(call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 2),
    (try_end),
]),

#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
# Output: none
("dplmc_start_alliance_between_kingdoms",[
    (store_script_param, ":kingdom_a", 1),
    (store_script_param, ":kingdom_b", 2),
    (store_script_param, ":initializing_war_peace_cond", 3),

    (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
    (val_add, ":relation", 15),
    (val_max, ":relation", 40),
    (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
    (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

    (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
    (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
    (try_end),

    (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        ##diplomacy start+ #Due to complaints about the wording
        #(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
        (display_log_message, "@{s1} and {s2} have entered into an alliance with each other."),
        ##diplomacy end+
        (try_begin),
            (eq, "$show_truce_expired", 1),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
        (try_end),
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),

    (try_end),

    (try_begin), #add truce
        (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        ##nested diplomacy start+ replace 80 with a named constant
        #(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
        (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_alliance_days_initial),
        ##nested diplomacy end+

        (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        ##nested diplomacy start+ replace 80 with a named constant
        #(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
        (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_alliance_days_initial),
        ##nested diplomacy end+

        (store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
        (faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
        (try_begin),
            (lt, ":damage_inflicted_by_a", 100),
            #controversial policy
        (try_end),
        (faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

        (store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
        (faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
        (try_begin),
            (lt, ":damage_inflicted_by_b", 100),
            #controversial policy
        (try_end),
        (faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

    (try_end),

    # share wars
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":kingdom_a", ":faction_no"),
        (neq, ":kingdom_b", ":faction_no"),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
        #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
        (eq, reg0, -2),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
        (ge, reg0, -1),

        (store_add, ":slot", slot_faction_neighbors_begin, ":kingdom_b"),
        (val_sub, ":slot", kingdoms_begin),
        (faction_get_slot, ":neighbors", ":faction_no", ":slot"),
        (eq, ":neighbors", 1),#they will only attack neighbors

        # MOTO build explanation string chief
        (assign, "$g_last_acting_faction", ":kingdom_b"),
        (assign, "$g_last_target_faction", ":faction_no"),
        (str_store_faction_name, s15, ":kingdom_b"),
        (str_store_faction_name, s16, ":faction_no"),
        (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
        # MOTO build explanation string end
        (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", logent_faction_declares_war_to_fulfil_pact), 	#MOTO chief pass log entries
    #      (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 2),
    (try_end),
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":kingdom_a", ":faction_no"),
        (neq, ":kingdom_b", ":faction_no"),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
        #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
        (eq, reg0, -2),
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
        (ge, reg0, -1),
    # MOTO build explanation string chief

        (store_add, ":slot", slot_faction_neighbors_begin, ":kingdom_a"),
        (val_sub, ":slot", kingdoms_begin),
        (faction_get_slot, ":neighbors", ":faction_no", ":slot"),
        (eq, ":neighbors", 1),#they will only attack neighbors

        (assign, "$g_last_acting_faction", ":kingdom_a"),
        (assign, "$g_last_target_faction", ":faction_no"),
        (str_store_faction_name, s15, ":kingdom_a"),
        (str_store_faction_name, s16, ":faction_no"),
        (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
    # MOTO build explanation string end
        (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", logent_faction_declares_war_to_fulfil_pact), 	#MOTO chief pass log entries
    #      (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 2),
    (try_end),
]),

#script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
# Output: none
("dplmc_start_defensive_between_kingdoms",[
    (store_script_param, ":kingdom_a", 1),
    (store_script_param, ":kingdom_b", 2),
    (store_script_param, ":initializing_war_peace_cond", 3),
    ##diplomacy start+
    #Since "fac_player_supporters_faction" is used as a shorthand for the faction
    #run by the player, intercept that here instead of the various places this is
    #called from.
    (assign, ":save_reg1", reg1),
    (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
    (assign, ":kingdom_a", reg0),
    (assign, ":kingdom_b", reg1),
    (assign, reg1, ":save_reg1"),
    ##diplomacy end+

    (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
    (val_add, ":relation", 10),
    (val_max, ":relation", 30),
    (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
    (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

    (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 10),
        (val_max, ":relation", 30),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
    (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 10),
        (val_max, ":relation", 30),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
    (try_end),

    (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),
        (try_begin),
            (eq, "$show_truce_expired", 1),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
        (try_end),
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),

    (try_end),

    (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##diplomacy start+ replace 60 with named variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 60),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_defense_days_initial),
	    ##diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##diplomacy start+ replace 60 with named variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 60),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_defense_days_initial),
	    ##diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

    (try_end),
]),

#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
# Output: none
("dplmc_start_trade_between_kingdoms", [
    (store_script_param, ":kingdom_a", 1),
    (store_script_param, ":kingdom_b", 2),
    (store_script_param, ":initializing_war_peace_cond", 3),
    ##diplomacy start+
    #Since "fac_player_supporters_faction" is used as a shorthand for the faction
    #run by the player, intercept that here instead of the various places this is
    #called from.
    (assign, ":save_reg1", reg1),
    (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
    (assign, ":kingdom_a", reg0),
    (assign, ":kingdom_b", reg1),
    (assign, reg1, ":save_reg1"),
    ##diplomacy end+

    (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
    (val_add, ":relation", 5),
    (val_max, ":relation", 20),
    (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
    (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

    (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 5),
        (val_max, ":relation", 20),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
    (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 5),
        (val_max, ":relation", 20),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
    (try_end),
    (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),
        (try_begin),
            (eq, "$show_truce_expired", 1),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
        (try_end),
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),
    (try_end),

    (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number of days with a variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_trade_days_initial),
	    ##nested diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number of days with a variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_trade_days_initial),
	    ##nested diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
    (try_end),
]),

#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
# Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
# Output: none
("dplmc_start_nonaggression_between_kingdoms",[
    (store_script_param, ":kingdom_a", 1),
    (store_script_param, ":kingdom_b", 2),
    (store_script_param, ":initializing_war_peace_cond", 3),
    ##diplomacy start+
    #Since "fac_player_supporters_faction" is used as a shorthand for the faction
    #run by the player, intercept that here instead of the various places this is
    #called from.
    (assign, ":save_reg1", reg1),
    (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
    (assign, ":kingdom_a", reg0),
    (assign, ":kingdom_b", reg1),
    (assign, reg1, ":save_reg1"),
    ##diplomacy end+

    (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
    (val_add, ":relation", 3),
    (val_max, ":relation", 10),
    (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
    (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

    (try_begin),
        (eq, "$players_kingdom", ":kingdom_a"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
        (val_add, ":relation", 3),
        (val_max, ":relation", 10),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
    (else_try),
        (eq, "$players_kingdom", ":kingdom_b"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
        (val_add, ":relation", 3),
        (val_max, ":relation", 10),
        (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        #(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
    (try_end),

    (try_begin),
        (eq, ":initializing_war_peace_cond", 1),
        (str_store_faction_name_link, s1, ":kingdom_a"),
        (str_store_faction_name_link, s2, ":kingdom_b"),
        (display_log_message, "@{s1} and {s2} have concluded a non aggression pact with each other."),
        (try_begin),
            (eq, "$show_truce_expired", 1),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
        (try_end),
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
        (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
        (assign, "$g_recalculate_ais", 1),

    (try_end),

    (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number with a variable
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
	    (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_truce_days_initial),
	    ##nested diplomacy end+

		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##nested diplomacy start+ replace hardcoded number with a variable
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
	    (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_truce_days_initial),
	    ##nested diplomacy end+

		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(try_begin),
			(lt, ":damage_inflicted_by_a", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(try_begin),
			(lt, ":damage_inflicted_by_b", 100),
			#controversial policy
		(try_end),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

    (try_end),
]),

# Input: arg1 = faction_no_1, arg2 = faction_no_2
("dplmc_get_prisoners_value_between_factions",[
       (store_script_param, ":faction_no_1", 1),
       (store_script_param, ":faction_no_2", 2),

       (assign, ":faction_no_1_value", 0),
       (assign, ":faction_no_2_value", 0),

       (try_for_parties, ":party_no"),
         (store_faction_of_party, ":party_faction", ":party_no"),
         (try_begin),
           (eq, ":party_faction", ":faction_no_1"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
           (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
             (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
             (store_troop_faction, ":cur_faction", ":cur_troop_id"),

             (eq, ":cur_faction", ":faction_no_2"),
             (try_begin),
               (troop_is_hero, ":cur_troop_id"),
               (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
               (val_add, ":faction_no_1_value", reg0),

               (try_begin),#debug
                 (eq, "$cheat_mode", 1),
                 (assign, reg0, ":faction_no_1_value"),
                 (display_message, "@{!}DEBUG : faction_no_1_value: {reg0}"),
               (try_end),

             (try_end),
           (try_end),
         (else_try),
           (eq, ":party_faction", ":faction_no_2"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
           (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
             (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
             (store_troop_faction, ":cur_faction", ":cur_troop_id"),

             (eq, ":cur_faction", ":faction_no_1"),
             (try_begin),
               (troop_is_hero, ":cur_troop_id"),
               (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
               (val_add, ":faction_no_2_value", reg0),

               (try_begin), #debug
                 (eq, "$cheat_mode", 1),
                 (assign, reg0, ":faction_no_2_value"),
                 (display_message, "@{!}DEBUG : faction_no_2_value: {reg0}"),
               (try_end),

             (try_end),
           (try_end),
         (try_end),
       (try_end),
       (store_sub, reg0, ":faction_no_1_value", ":faction_no_2_value"),
]),

# Input: arg1 = faction_no_1, arg2 = faction_no_2
("dplmc_get_truce_pay_amount",[
    (store_script_param, ":faction_no_1", 1),
    (store_script_param, ":faction_no_2", 2),
    (store_script_param, ":check_peace_war_result", 3),
    ##diplomacy start+
    #Since "fac_player_supporters_faction" is used as a shorthand for the faction
    #run by the player, intercept that here instead of the various places this is
    #called from.
    (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":faction_no_1", ":faction_no_2"),
    (assign, ":faction_no_1", reg0),
    (assign, ":faction_no_2", reg1),
    ##diplomacy end+

    (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":check_peace_war_result"), #debug
        (display_message, "@{!}DEBUG : peace_war_result: {reg0}"),#debug
    (try_end),

    ##nested diplomacy start+
    #Improve this script; costs were too low befow.
    #faction_no_1 is player faction asking for peace
    #faction_no_2 is NPC faction that already considered peace and considers
    #      it a bad idea, so the price should not be nominal.

    #(Also, a sign error meant that the amount asked was almost always
    #zero.)

    #Because the PC wants peace and the NPC doesn't, we aren't going to
    #bother calculating relative strength or the like.  Instead, we are
    #going to assume the NPC can achieve his strategic objectives if he
    #does not make peace, and set the price accordingly.

    #Add a generic cost for check_peace_war_result
    #These are the same as in Wahiti's original script.
    (assign, ":base_cost", 4000),
    (try_begin),
        #It's dubious that this is ever currently called if the check-peace-war
        #result was >= 0, but include this for completeness.
        (ge, ":check_peace_war_result", 0),
        (assign, ":base_cost", 4000),
    (else_try),
        (ge, ":check_peace_war_result", -1),
        (assign, ":base_cost", 8000),
    (else_try),
        (ge, ":check_peace_war_result", -2),
        (assign, ":base_cost", 12000),
    (else_try),
        #It shouldn't be used with this parameter; this is for the
        #sake of completeness.
        (le, ":check_peace_war_result", -3),
        (store_mul, ":base_cost", -6000, ":check_peace_war_result"),
    (try_end),

    #Get reparations for held centers.  A truce lasts 20 days, so the
    #value "lost" in rents and tarriffs by declaring peace now cannot be
    #is not greater than 3 times the weekly average (that upper bound is
    #if the NPC is in a position to immediately recapture all of them).

    #If the NPC kingdom is currently attacking a specific village or walled
    #center, even if it isn't an ex-possession it effectively becomes one.
    #(Also, assign it or its center as a demanded fief if there wasn't one
    #already.)
    (assign, ":target_fief", -1),
    (try_begin),
        (lt, ":check_peace_war_result", 1),#This should always be true anyway, but still.
        (this_or_next|faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_attacking_center),
        (faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_raiding_village),
        (faction_get_slot, reg0, ":faction_no_2", slot_faction_ai_object),
        (is_between, reg0, centers_begin, centers_end),
        (assign, ":target_fief", reg0),
    (try_end),

    (assign, ":center_cost", 0),
    (assign, ":concession_value", 0),
    #This this old are newer are considered "recently conquered", meaning that
    #faction_no_2 thinks there's a good chance they could reclaim them if the
    #fighting continued.
    (store_current_hours, ":recently_conquered"),
    (try_begin),
        (ge, ":check_peace_war_result", 1),#ordinarily this should not be true
        (val_sub, ":recently_conquered", 24 * 2),#only the last two days
    (else_try),
        (eq, ":check_peace_war_result", 0),
        (val_sub, ":recently_conquered", 24 * 15),#last 15 days
    (else_try),
        (eq, ":check_peace_war_result", -1),
        (val_sub, ":recently_conquered", 24 * 20),#last 20 days
    (else_try),
        (eq, ":check_peace_war_result", -2),
        (val_sub, ":recently_conquered", 24 * 30),#last 30 days
    (else_try),
        (val_sub, ":recently_conquered", 24 * 60),#last 60 days
    (try_end),

    (try_for_range, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_current_faction", ":party_no"),
        (eq, ":party_current_faction", ":faction_no_1"),

        #party_value is the estimated weekly income of the fief,
        #applied three times and time discounted
        (call_script, "script_dplmc_estimate_center_weekly_income", ":party_no"),
        #(store_mul, ":party_value", reg0, 3),
        (assign, ":party_value", reg0),
        (try_begin),
            (ge, "$g_concession_demanded", spawn_points_begin),
            (this_or_next|eq, "$g_concession_demanded", ":party_no"),
            (party_slot_eq, ":party_no", slot_village_bound_center, "$g_concession_demanded"),
            (val_add, ":concession_value", ":party_value"),
        (try_end),
        (assign, ":continue", 0),
        (try_begin),
            #A former possession of faction 2 (must have recently changed hands, or
            #faction 2 must be enthusiastic about the war)
            (party_slot_eq, ":party_no", slot_center_original_faction, ":faction_no_2"),
            (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
            (assign, ":continue", 1),
        (else_try),
            #A former possession of faction 2 (must have recently changed hands, or
            #faction 2 must be enthusiastic about the war)
            (party_slot_eq, ":party_no", slot_center_ex_faction, ":faction_no_2"),
            (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
            (assign, ":continue", 1),
        (else_try),
            #The center is being attacked by faction 2, or is a village whose castle
            #or town is being attacked by faction 2.
            (ge, ":target_fief", centers_begin),
            (this_or_next|eq, ":party_no", ":target_fief"),
            (party_slot_eq, ":party_no", slot_village_bound_center, ":target_fief"),
            (assign, ":continue", 1),
        (else_try),
            #The center is under siege by faction 2.
            (party_get_slot, reg0, ":party_no", slot_center_is_besieged_by),
            (gt, reg0, 0),
            (party_is_active, reg0),
            (store_faction_of_party, reg0, reg0),
            (eq, reg0, ":faction_no_2"),
            (assign, ":continue", 1),
        (else_try),
            #The center is a village, and the castle or town it is bound to
            #is under siege by faction 2.
            (is_between, ":party_no", villages_begin, villages_end),
            (party_get_slot, reg0, ":party_no", slot_village_bound_center),
            (is_between, reg0, centers_begin, centers_end),
            (party_get_slot, reg0, reg0, slot_center_is_besieged_by),
            (gt, reg0, -1),
            (party_is_active, reg0),
            (store_faction_of_party, reg0, reg0),
            (eq, reg0, ":faction_no_2"),
            (assign, ":continue", 1),
        (try_end),
        (gt, ":continue", 0),
        (val_add, ":center_cost", ":party_value"),
    (try_end),

    #If no held centers were found, assume the campaign objective is to
    #conquer territory rather than recover lost territory, if the
    #NPC is sufficiently enthusiastic about the war.
    (try_begin),
        #Equivalent of a castle and a village
        (eq, ":check_peace_war_result", -1),
        (val_max, ":center_cost", (1500 + 750) * 3),
    (else_try),
        #Equivalent of two castles with two villages
        (le, ":check_peace_war_result", -2),
        (val_max, ":center_cost", (1500 + 750) * 3 * 2),
    (try_end),

    #If the war started very recently, or a center changed hands very recently,
    #increase the cost.  The reasoning behind this is to make the AI less prone
    #to whipsawing.
    #
    #The multiplier is 2x for the first 48 hours, then decreases linearly from
    #the two-day mark until it reaches zero at the 8-day mark.
    #
    #As an example, here is how a cost of 10,000 would scale over this time:
    # 1 day  - 20000
    # 2 days - 20000
    # 3 days - 18333
    # 4 days - 16667
    # 5 days - 15000
    # 6 days - 13333
    # 7 days - 11667
    # 8 days - 10000
    # 9 days - 10000
    (store_current_hours, ":cur_hours"),
    (faction_get_slot, ":faction_ai_last_decisive_event", ":faction_no_2", slot_faction_ai_last_decisive_event),
    (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
    (val_max, ":hours_since_last_decisive_event", 0),
    (try_begin),
        #First 48 hours, the base & center costs are doubled.
        (lt, ":hours_since_last_decisive_event", 48 + 1),
        (val_mul, ":base_cost", 2),
        (val_mul, ":center_cost", 2),
    (else_try),
        #From 2 days to 8 days, the cost multiplier goes from 2 to 1
        (lt, ":hours_since_last_decisive_event", 24 * 8),
        (store_sub, reg0, 24 * 2, ":hours_since_last_decisive_event"),#0 to 6 days
        (store_sub, ":multiplier", 24 * 12, reg0),# 6 to 12 days

        (val_mul, ":base_cost", ":multiplier"),
        (val_add, ":base_cost", (24 * 6) // 2),
        (val_div, ":base_cost", 24 * 6),

        (val_mul, ":center_cost", ":multiplier"),
        (val_add, ":center_cost", (24 * 6) // 2),
        (val_div, ":center_cost", 24 * 6),
    (try_end),

    #Get (value of ransoms held by faction #1) - (value of ransoms held by faction #2)
    (call_script, "script_dplmc_get_prisoners_value_between_factions", ":faction_no_1", ":faction_no_2"),

    (try_begin),
        (eq, "$cheat_mode", 1),
        (display_message, "@{!}DEBUG : prisoner_value: {reg0}"),#debug
    (try_end),
    (assign, ":prisoner_value", reg0),

    #Write result to reg0
    (store_add, reg0, ":base_cost", ":center_cost"),

    #Scale for the player's wealth, to partially mitigate the problem
    #of the cost becoming meaningless as the player's wealth increases.
    #(Scale less than 1-to-1, so it is possible to become richer in real
    #terms.)  This is also aimed at reducing the necessity of replacing
    #the values in mods that alter gold scarcity.
    # (store_troop_gold, ":player_gold", "trp_household_possessions"),
    # (store_troop_gold, reg1, "trp_player"),
    # (val_add, ":player_gold", reg1),
    # (try_begin),
        # #Arbitrarily pick 100,000 as the target wealth, since that's when
        # (gt, ":player_gold", 100000),
        # (store_div, reg1, ":player_gold", 1000),
        # (val_mul, reg1, reg0),
        # (val_div, reg1, 100),

        # (val_add, reg0, reg1),
        # (val_div, reg0, 2),

        # #Apply the same scaling to the concession value
        # (store_div, reg1, ":player_gold", 1000),
        # (val_mul, reg1, ":concession_value"),
        # (val_div, reg1, 100),

        # (val_add, ":concession_value", reg1),
        # (val_div, ":concession_value", 2),
    # (try_end),

    #Take into account campaign difficulty
    (assign, ":min_cost", reg0),

    (val_mul, reg0, 3),
    (val_div, reg0, 2),
    (val_mul, ":min_cost", 87),#set min_cost to 87% of the original base_cost + center_cost
    (val_div, ":min_cost", 100),


    (val_sub, reg0, ":prisoner_value"),

    #Because the NPC kingdom doesn't want peace, it will not agree to peace
    #for free, as that would be a contradiction.
    (val_max, reg0, ":min_cost"),

    (try_begin),
        (eq, "$cheat_mode", 1),
        (display_message, "@{!}DEBUG : peace_war_result after prisoners: {reg0}"),#debug
    (try_end),

       #The value of the concession (if any) was already calculated above
    (assign, reg1, -1),
    (try_begin),
        (gt, "$g_concession_demanded", 0),
        (gt, ":concession_value", 0),
        (store_sub, reg1, reg0, ":concession_value"),
        (val_max, reg1, 0),
        #Only accept cash alone in lieu of a fief if you don't partcularly want war
        (lt, ":check_peace_war_result", 0),
        (assign, reg0, -1),
    (try_end),

    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (display_message, "@{!}DEBUG : truce_pay_amount0: {reg0}"),
        (display_message, "@{!}DEBUG : truce_pay_amount1: {reg1}"),
    (try_end),
     ##nested diplomacy end+
]),
("dplmc_player_center_surrender",[
    (store_script_param, ":center_no", 1),

    #protect player for 24 hours
    (store_current_hours,":protected_until"),
    (val_add, ":protected_until", 48),
    (party_get_slot, ":besieger", ":center_no", slot_center_is_besieged_by),
    (store_faction_of_party, ":besieger_faction",":besieger"),
    ##nested diplomacy start+
    #In this version this variable currently isn't used for anything
    #(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
    ##nested diplomacy end+

    (party_set_slot,":besieger",slot_party_ignore_player_until,":protected_until"),
    (party_ignore_player, ":besieger", 48),
	##nested diplomacy start+
	#Add support for promoted kingdom ladies
    (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
        # (try_for_range, ":lord", heroes_begin, heroes_end),
        # (this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
        # (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
        ##nested diplomacy end+
        (store_faction_of_troop, ":lord_faction", ":lord"),
        (eq, ":lord_faction", ":besieger_faction"),
        (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
        (party_is_active, ":led_party"),

        (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
        (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

        (party_is_active, ":besieger"),
        (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
        (lt, ":distance_to_marshal", 20),

        (party_set_slot,":led_party",slot_party_ignore_player_until,":protected_until"),
        (party_ignore_player, ":led_party", 48),
    (try_end),

    (party_set_faction,"$current_town","fac_neutral"), #temporarily erase faction so that it is not the closest town
    (party_get_num_attached_parties, ":num_attached_parties_to_castle",":center_no"),
    (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
        (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":iap"),
        (party_detach, ":attached_party"),
        (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
        (eq, ":attached_party_type", spt_kingdom_hero_party),
        (neq, ":attached_party_type", "p_main_party"),
        (store_faction_of_party, ":attached_party_faction", ":attached_party"),
        (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
        (try_begin),
            (gt, reg0, 0),
            (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
        (else_try),
            (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, ":center_no"),
        (try_end),
    (try_end),
    (call_script, "script_party_remove_all_companions", ":center_no"),
    (change_screen_return),
    (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"), #recalculate so that
    (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured

	##nested diplomacy start+
	#Anyone who lost a fief due to your surrender will be irritated
	(try_for_range, ":village_no", centers_begin, centers_end),
        (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
        (party_get_slot, ":village_lord", ":village_no", slot_town_lord),
        (neq, ":village_lord", "trp_player"),
        (is_between, ":village_lord", heroes_begin, heroes_end),
        (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
    (try_end),
	##nested diplomacy end+
    ##diplomacy
    (call_script, "script_give_center_to_faction", "$current_town", ":besieger_faction"),
    (call_script, "script_order_best_besieger_party_to_guard_center", ":center_no", ":besieger_faction"),

    #relation and controversy
    ##nested diplomacy start+, There should be no relation bonus with the enemy lord
    #(call_script, "script_change_player_relation_with_troop", ":enemy_party_leader", 2),
    ##nested diplomacy end+
    (try_begin),
        (gt, "$players_kingdom", 0),
        (neq, "$players_kingdom", "fac_player_supporters_faction"),
        (neq, "$players_kingdom", "fac_player_faction"),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        ##diplomacy start+
        ##OLD:
        #(neq, ":faction_leader", "trp_player"),
        ##NEW:
        #Also guard against faction leader being some invalid negative number
        (gt, ":faction_leader", "trp_player"),
        ##diplomacy end+
        (call_script, "script_change_player_relation_with_troop", ":faction_leader", -2),
    (try_end),

  	(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
  	(val_add, ":controversy", 4),
  	(val_min, ":controversy", 100),
  	(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
    ##nested diplmacy start+ add garrison to fief
    #The average # of troops added by script_cf_reinforce_party is 11.5.
    (assign, ":garrison_strength", 4),#easy: 34.5 for a castle
    (try_begin),
        (party_slot_eq, ":center_no", slot_party_type, spt_town),
        (assign, ":garrison_strength", 6),#easy: 103.5 for a town
    (try_end),

    (val_mul, ":garrison_strength", 5),
    (val_div, ":garrison_strength", 3),

    (try_for_range, ":party_template_slot", slot_cohort_town_begin, slot_cohort_town_end),
        (party_get_slot, ":party_template", ":center_no", ":party_template_slot"),
        (ge, ":party_template", 1),
        (call_script, "script_cohort_refil_garrison", ":center_no", ":party_template", ":party_template_slot",0),
    (try_end),

    (try_for_range, ":unused", 0, 7),# ADD some XP initially
        (store_mul, ":xp_range_min", 150, ":garrison_strength"),
        (store_mul, ":xp_range_max", 200, ":garrison_strength"),
        (store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
        (party_upgrade_with_xp, ":center_no", ":xp", 0),
    (try_end),
]),
("dplmc_send_messenger_to_troop",[
    (store_script_param, ":target_troop", 1),
    (store_script_param, ":message", 2),
    (store_script_param, ":orders_object", 3),

    #SB : correcting destination for lords waiting to respawn
    (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
    (try_begin),
        (le, ":target_party", 0),
        (call_script, "script_lord_get_home_center", ":target_troop"),
        (assign, ":target_party", reg0),
    (try_end),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", "$current_town", "pt_messenger_party"),
    (assign,":spawned_party",reg0),
    #SB : factionalized messenger
    (store_faction_of_party, ":faction_no", ":target_party"),
    (try_begin),
        (is_between, ":faction_no", npc_kingdoms_begin, kingdoms_end),
        (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
    (else_try),
        (assign, ":messenger_troop", "trp_dplmc_messenger"),
    (try_end),
    (party_add_members, ":spawned_party", ":messenger_troop", 1),

    (try_begin),
        (eq, ":message", spai_accompanying_army),
        (assign, ":orders_object", "p_main_party"),
    (try_end),

    # (party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
    (store_faction_of_troop, ":player_faction", "trp_player"),
    (party_set_faction, ":spawned_party", ":player_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
    (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
    #SB : cache the actual troop while going towards known center
    (party_set_slot, ":spawned_party", dplmc_slot_party_origin, ":target_troop"),

    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s13, ":target_party"),
        (display_message, "@{!}DEBUG - Send message to {s13}"),
    (try_end),
]),
("dplmc_send_messenger_to_party",[
    (store_script_param, ":target_party", 1),
    (store_script_param, ":message", 2),
    (store_script_param, ":orders_object", 3),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", "$current_town", "pt_messenger_party"),
    (assign, ":spawned_party", reg0),
    #SB : factionalized messenger
    (store_faction_of_party, ":faction_no", ":target_party"),

    (try_begin),
        (is_between, ":faction_no", npc_kingdoms_begin, kingdoms_end),
        (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
    (else_try),
        (assign, ":messenger_troop", "trp_dplmc_messenger"),
    (try_end),
    (party_add_members, ":spawned_party", ":messenger_troop", 1),
    (party_set_faction, ":spawned_party", "fac_player_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
    (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),

    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s13, ":target_party"),
        (display_message, "@{!}DEBUG - Send message to {s13}"),
    (try_end),
]),
("dplmc_send_gift",[
    (store_script_param, ":target_troop", 1),
    (store_script_param, ":gift", 2),
    (store_script_param, ":amount", 3),
    (try_begin),
        (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
    (else_try),
        (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
        (troop_get_slot, ":target_party", ":target_troop", slot_troop_cur_center),
    (try_end),
    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (str_store_item_name, s12, ":gift"),
        (str_store_party_name, s13, ":target_party"),
        (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
    (try_end),
    (try_begin),
        #Guard against this being called without an explicit amount
        (lt, ":amount", 1),
        (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
        (assign, ":amount", 1),
        (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
        (assign, ":amount", 150),
    (try_end),
    (assign, ":original_amount", ":amount"),#Save this here because amount gets modified below!

    (call_script, "script_dplmc_withdraw_from_treasury", 50),
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),

    (try_for_range, ":inventory_slot", 0, ":capacity"),
        (gt, ":amount", 0),
        (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
        (eq, ":item", ":gift"),
        (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
        (try_begin),
            (le, ":tmp_amount", ":amount"),
            (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
            (val_sub, ":amount", ":tmp_amount"),
        (else_try),
            (val_sub, ":tmp_amount", ":amount"),
            (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
            (assign, ":amount", 0),
        (try_end),
    (try_end),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", "$current_town", "pt_dplmc_gift_caravan"),
    (assign,":spawned_party",reg0),
    (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":target_troop"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":original_amount"),
]),
("dplmc_send_gift_to_center",[
    (store_script_param, ":target_party", 1),
    (store_script_param, ":gift", 2),
    (store_script_param, ":amount", 3),

    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (str_store_item_name, s12, ":gift"),
        (str_store_party_name, s13, ":target_party"),
        (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
    (try_end),

    (try_begin),
        #Guard against this being called without an explicit amount
        (lt, ":amount", 1),
        (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
        (assign, ":amount", 300),
    (try_end),
    (assign, ":original_amount", ":amount"),#Save this here because amount gets modified below!

    (call_script, "script_dplmc_withdraw_from_treasury", 50),
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
    (try_for_range, ":inventory_slot", 0, ":capacity"),
        (gt, ":amount", 0),
        (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
        (eq, ":item", ":gift"),
        (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
        (try_begin),
            (le, ":tmp_amount", ":amount"),
            (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
            (val_sub, ":amount", ":tmp_amount"),
        (else_try),
            (val_sub, ":tmp_amount", ":amount"),
            (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
            (assign, ":amount", 0),
        (try_end),
    (try_end),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", "$current_town", "pt_dplmc_gift_caravan"),
    (assign,":spawned_party",reg0),
    (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, 0),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
    (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":original_amount"),
]),
# script_dplmc_troop_political_notes_to_s47
("dplmc_troop_political_notes_to_s47",[
    (store_script_param, ":troop_no", 1),
    ##diplomacy start+
    (assign, ":save_reg1", reg1),#save to revert
    (assign, ":save_reg4", reg4),#save to revert

    (try_begin),
        (eq, 0, 1),#Always disable this right now
        (is_between, "$g_talk_troop", heroes_begin, heroes_end),#i.e. not your chancellor
        (assign, ":troop_speaker", "$g_talk_troop"),
        (call_script, "script_troop_get_player_relation", ":troop_speaker"),
        (assign, ":speaker_player_relation", reg0),
    (else_try),
        (assign, ":troop_speaker", -1),
        (assign, ":speaker_player_relation", 100),
    (try_end),
    ##diplomacy end+

    (try_begin),
        (str_clear, s47),

        (store_faction_of_troop, ":troop_faction", ":troop_no"),

        (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),

        (str_clear, s40),
        (assign, ":logged_a_rivalry", 0),
        ##nested diplomacy start+
        (str_clear, s41),
        #lord can be married or related to player
        #(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (try_for_range, ":kingdom_hero", active_npcs_including_player_begin, active_npcs_end),
            #Also, don't include rivalries with retired (or dead) characters
            (neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement),
            ##nested diplomacy end+
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
            (lt, reg0, -10),

            (str_store_troop_name_link, s39, ":kingdom_hero"),
                ##nested diplomacy start+ use second person
            (try_begin),
                (eq, ":kingdom_hero", "trp_player"),
                (str_store_string, s39, "str_you"),
            (try_end),
                ##nested diplomacy end+
            (try_begin),
                (eq, ":logged_a_rivalry", 0),
                ##nested diplomacy start+
                (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
                ##nested diplomacy end+
                (str_store_string, s40, "str_dplmc_s39_rival"),
                (assign, ":logged_a_rivalry", 1),
            (else_try),
                (str_store_string, s41, "str_s40"),
                (str_store_string, s40, "str_dplmc_s41_s39_rival"),
            (try_end),
        (try_end),
        (str_clear, s46),
        ##nested diplomacy start+
        #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
        (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
        (str_store_troop_name, s46,":troop_no"),
        (assign, ":details_available", 0),
        (try_begin),
            #Enable details for lords you have met
            (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
            (assign, ":details_available", 1),
        (else_try),
            #Enable details when using an "omniscient" or non-specific speaker
            (neg|is_between, ":troop_speaker", heroes_begin, heroes_end),
            (assign, ":details_available", 1),
        (else_try),
            #Enable details for NPCs that aren't standard heroes, because the following checks don't apply
            (neg|is_between, ":troop_no", heroes_begin, heroes_end),
            (assign, ":details_available", 1),
        (else_try),
            #Enable details for lords the speaker has met
            (is_between, ":troop_speaker", heroes_begin, heroes_end),
            (is_between, ":troop_no", heroes_begin, heroes_end),
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":troop_speaker"),
            (neq, reg0, 0),#between NPCs, relation 0 means "have not met"
            (assign, ":details_available", 1),
        (else_try),
            #Enable details for v. notable lords (based on renown)
            (troop_slot_ge, ":troop_no", slot_troop_renown, 500),
            (assign, ":details_available", 1),
        (else_try),
            #Enable details for v. notable lords (based on fiefs)
            (assign, reg0, 0),
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                (this_or_next|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
                (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
                (troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
                (val_add, reg0, 2),
                (party_slot_eq, ":center_no", slot_party_type, spt_town),
                (val_add, reg0, 2),
            (try_end),
            (ge, reg0, 4),#one town, or 2+ castles
            (assign, ":details_available", 1),
        (try_end),
        #xxx TODO: Make a full implementation of the above that takes into account the time of the last spy report.
        (try_begin),
            (eq, ":details_available", 0),
            (troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
            (str_store_string, s46, "str_dplmc_reputation_unknown"),
        (else_try),
        ##nested diplomacy end+
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
            (str_store_string, s46, "str_dplmc_reputation_martial"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
            (str_store_string, s46, "str_dplmc_reputation_debauched"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
            (str_store_string, s46, "str_dplmc_reputation_pitiless"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
            (str_store_string, s46, "str_dplmc_reputation_calculating"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
            (str_store_string, s46, "str_dplmc_reputation_quarrelsome"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
            (str_store_string, s46, "str_dplmc_reputation_goodnatured"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
            (str_store_string, s46, "str_dplmc_reputation_upstanding"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
            (str_store_string, s46, "str_dplmc_reputation_conventional"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
            (str_store_string, s46, "str_dplmc_reputation_adventurous"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_hedonistic),
            (str_store_string, s46, "str_dplmc_reputation_hedonistic"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
            (str_store_string, s46, "str_dplmc_reputation_romantic"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
            (str_store_string, s46, "str_dplmc_reputation_moralist"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
            (str_store_string, s46, "str_dplmc_reputation_ambitious"),
        (else_try),
            (troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
            (str_store_string, s46, "str_dplmc_reputation_unknown"),
        (try_end),
        ##diplomacy start+
        (str_clear, s39),#remove annoying bug
        (str_clear, s45),#remove annoying bug

        #Special-case spouse into showing up if it doesn't get added below
        (try_begin),
            (troop_get_slot, ":spouse", ":troop_no", slot_troop_spouse),
            (ge, ":spouse", 0),

            #Because blank memory is initially zero, enforce this
            (this_or_next|is_between, ":troop_no", heroes_begin, heroes_end),
            (neq, ":spouse", "trp_player"),
            #Initialize s45
            (str_store_troop_name, s39, ":spouse"),
            (try_begin),
                (eq, ":spouse", "trp_player"),
                (str_store_string, s39, "str_you"),##<-- dplmc+ note, this was s59 before, probably an accidental bug
            (else_try), #SB : speaker
                (eq, ":spouse", ":troop_speaker"),
                (str_store_string, s39, "str_me"),
            (try_end),
            (str_store_string, s45, "str_dplmc_s40_married_s39"),
        (try_end),
        ##diplomacy end+

        (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
            (troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
            ##nested diplomacy start+ ; some lords could romance opposite-gender lords
            #(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
            (is_between, ":love_interest", active_npcs_begin, kingdom_ladies_end),
            #Also prevent a bug for companions / claimants who are lords
            (neq, ":love_interest", "trp_knight_1_1_wife"),#<- should not appear in the game
            #Also prevent bad messages for married/betrothed lords
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
            (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
            (troop_slot_eq, ":troop_no", slot_troop_betrothed, -1),
            ##nested diplomacy end+
            (str_store_troop_name, s39, ":love_interest"),
            ##nested diplomacy start+ Use second person properly
            (try_begin),
                (eq, ":love_interest", "trp_player"),
                (str_store_string, s39, "str_you"),
            (else_try), #SB : speaker
                (eq, ":love_interest", ":troop_speaker"),
                (str_store_string, s39, "str_me"),
            (try_end),
            ##nested diplomacy start+
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
            ##nested diplomacy start+
            (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
            ##nested diplomacy end+
            (str_store_string, s45, "str_dplmc_s40_love_interest_s39"),
            (try_begin),
                (troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
                (str_store_string, s45, "str_dplmc_s40_married_s39"),
            (else_try),
                (troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
                (str_store_string, s45, "str_dplmc_s40_betrothed_s39"),
            (try_end),
        (try_end),

        (str_clear, s44),
        (try_begin),
            (neq, ":troop_no", ":faction_leader"),
            ##nested diplomacy start+
            (gt, ":details_available", 0),
            #Ensure leader is valid
            (assign, reg0, 0),#continue if 0
            (try_begin),
                (neq, ":troop_no", "trp_player"),
                (neq, ":faction_leader", "trp_player"),
                (this_or_next|neg|is_between, ":troop_no", heroes_begin, heroes_end),
                (neg|is_between, ":faction_leader", heroes_begin, heroes_end),
                (assign, reg0, 1),
            (try_end),
            (eq, reg0, 0),

            (try_begin),
                (gt, ":troop_speaker", 0),
                (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":troop_speaker"),
                #(val_min, reg0, 20),
                #(neq, ":faction_leader", "trp_player"),
                #(val_div, reg0, 2),
            (try_end),
            (this_or_next|lt, reg0, 1),
            (ge, ":speaker_player_relation", 1),
            ##nested diplomacy end+
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),

            (assign, ":relation", reg0),
            ##diplomacy start+ Don't mention anything for kingdom ladies at the beginning; it doesn't add information.
            (this_or_next|lt, reg0, 0),
            (this_or_next|gt, reg0, 1),#Remember that relation 1 is neutral (it just means "met") between NPCs
            (this_or_next|neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
            (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
            ##diplomacy end+
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            ##nested diplomacy start+
            #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
            (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
            #TODO: Come back and add this (take into account spying)
            #(neq, ":details_available", 0),#don't show unless more details are available
            ##nested diplomacy end+
            (store_add, ":str_id", "str_dplmc_relation_mnus_100_ns", ":str_offset"),
            (try_begin),
                (eq, ":faction_leader", "trp_player"),
                ##nested diplomacy start+ "str_you" exists, so we might as well use it
                #(str_store_string, s59, "@you"),
                (str_store_string, s59, "str_you"),
                ##diplomacy end+
            (else_try),
                (str_store_troop_name, s59, ":faction_leader"),
            (try_end),
            (str_store_string, s59, ":str_id"),
            (str_store_string, s44, "@{!}^{s59}"),
        (try_end),

        (str_clear, s48),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (store_current_hours, ":hours"),
            (gt, ":hours", 0),
            (call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
            (str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
        (try_end),

        (str_store_string, s47, "str_s46s45s44s48"),
        # (troop_get_slot, reg40, ":troop_no", slot_troop_wealth),
        # (str_store_string, s47, "@{s47} ^He currently has a wealth of {reg40} denarii."),
    (try_end),
    ##diplomacy start+
    (assign, reg1, ":save_reg1"),#revert register
    (assign, reg4, ":save_reg4"),#revert register to avoid clobbering
    ##diplomacy end+
]),
("dplmc_send_patrol",[
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":size", 3), #0 small, 1 medium, 2, big, 3 elite
    (store_script_param, ":template_faction", 4),
    (store_script_param, ":order_troop", 5),

    (try_begin),
        (is_between, ":start_party", walled_centers_begin, walled_centers_end),
        (try_begin),
            (eq, ":size", 2),
            (faction_get_slot, ":party_template", ":template_faction", slot_faction_reinforcements_c),
        (else_try),
            (eq, ":size", 1),
            (faction_get_slot, ":party_template", ":template_faction", slot_faction_reinforcements_b),
        (else_try),
            (faction_get_slot, ":party_template", ":template_faction", slot_faction_reinforcements_a),
        (try_end),

        (try_begin),
            (faction_slot_eq, ":template_faction", slot_faction_government_type, gov_imperial),
            (is_between, ":order_troop", active_npcs_begin, active_npcs_end),
            (this_or_next|troop_slot_ge, ":order_troop", slot_troop_legion, 1),
            (troop_slot_ge, ":order_troop", slot_troop_aux, 1),
            (assign, ":gold", 1000000),
        (else_try),
            (eq, ":order_troop", "trp_player"),
            #Remove any remaining gold from the treasury
            (store_troop_gold, ":gold", "trp_household_possessions"),
            #Remove the gold from the player
            (store_troop_gold, reg1, "trp_player"),
            (val_add, ":gold", reg1),
        (else_try),
            (faction_slot_eq, ":template_faction", slot_faction_government_type, gov_feudal),
            (is_between, ":order_troop", active_npcs_begin, active_npcs_end),
            (troop_get_slot, ":gold", ":order_troop", slot_troop_wealth),
        (else_try),
            (assign, ":gold", 1000000),
        (try_end),

        (call_script, "script_get_cohort_info_to_s5", ":party_template", ":template_faction"),
        (try_begin),
            (ge, ":gold", reg6),

            (set_spawn_radius, 1),
            (call_script, "script_spawn_party", ":start_party", "pt_patrol_party"),
            (assign,":spawned_party",reg0),
            (party_set_faction, ":spawned_party", ":template_faction"),
            (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
            (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),

            (party_set_helpfulness, ":spawned_party", 500),#make them more helpful, as they are patrols
            (party_set_aggressiveness, ":spawned_party", 5),

            (party_set_slot, ":start_party", slot_town_patrol_party, ":spawned_party"),

            (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"),
            (str_store_party_name, s5, ":target_party"),
            (party_set_name, ":spawned_party", "str_s5_patrol"),

            (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":spawned_party", ":target_party"),
            (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
            (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),

            (party_set_slot, ":spawned_party", slot_cohort_1, ":party_template"),
            (call_script, "script_cohort_describe_strength_to_s5_and_refil", ":spawned_party", ":party_template", slot_cohort_1, -1, ":order_troop", 1),

            (call_script, "script_update_party_icon", ":spawned_party"),

            (try_begin), #debug
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s13, ":target_party"),
                (str_store_faction_name, s14, ":template_faction"),
                (str_store_party_name, s15, ":start_party"),
                (display_message, "@{!}DEBUG - Send {s14} patrol from {s15} to {s13}"),
            (try_end),
        (else_try),
            (ge, "$cheat_mode", 1),
            (str_store_party_name, s13, ":target_party"),
            (str_store_faction_name, s14, ":template_faction"),
            (str_store_party_name, s15, ":start_party"),
            (display_message, "@{!} {s14} could not send a patrol from {s15} to patrol around {s13}"),
        (try_end),
    (else_try),
        (assign, reg13, ":start_party"),
        (display_message, "@Invalid start_party: {reg13}"),
    (try_end),
]),
("dplmc_move_troops_party",[
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":party_no", 3),
    (store_script_param, ":template_faction", 4),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", ":start_party", "pt_patrol_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":template_faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (str_store_party_name, s5, ":target_party"),
    #SB : fixed string
    (party_set_name, ":spawned_party", "str_s5_transfer"),

    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":spawned_party", ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_ai_state, spai_retreating_to_center),
    (party_set_aggressiveness, ":spawned_party", 0),
    (party_set_courage, ":spawned_party", 3),
    (party_set_ai_initiative, ":spawned_party", 100),

    (call_script, "script_update_party_icon", ":spawned_party"),

    (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
]),
("dplmc_send_scout_party",[
    (store_script_param, ":start_party", 1),
    (store_script_param, ":target_party", 2),
    (store_script_param, ":faction", 3),

    (set_spawn_radius, 1),
    (call_script, "script_spawn_party", ":start_party", "pt_scout_party"),
    (assign,":spawned_party",reg0),
    (party_set_faction, ":spawned_party", ":faction"),
    (party_set_slot, ":spawned_party", slot_party_type, spt_scout),
    (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
    (str_store_party_name, s5, ":target_party"),
    (party_set_name, ":spawned_party", "str_s5_scout"),

    (party_add_members, ":spawned_party", "trp_dplmc_scout", 1),

    (party_get_position, pos1, ":target_party"),
    (map_get_random_position_around_position, pos2, pos1, 1),
    (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_point),
    (party_set_ai_target_position, ":spawned_party", pos2),
    (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
    (party_set_slot, ":spawned_party", slot_party_orders_object, ":target_party"),
    (party_set_aggressiveness, ":spawned_party", 0),
    (party_set_courage, ":spawned_party", 3),
    (party_set_ai_initiative, ":spawned_party", 100),
]),

("dplmc_init_domestic_policy",[
    (try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        (try_begin),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_roman"),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_greek"),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_bosporan"),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_judean"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, 3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 3),
        (else_try),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_judean"),# judean
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 0),
        (else_try),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_sarmatian"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, -3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, 3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, 3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, -3), ##stepp people are naturaly free
        (else_try),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_germanic"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, -3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, 3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, 2),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 0),
        (else_try),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_celtic"),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_caledonian"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, -3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, 3),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 1),
        (else_try),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_parthian"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, -2),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, -3), ##zorathoism do not like slaves
        (else_try),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_caucasian"),
            (this_or_next|faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_egyptian"),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_syrian"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, -1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, -2),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 1),
        (else_try),
            (faction_slot_eq, ":kingdom", slot_faction_culture, "fac_culture_dacian"),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, 1),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, 0),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, 0),
        (else_try),
            (store_random_in_range, ":random", -3, 4),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, ":random"),
            (store_random_in_range, ":random", -3, 4),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, ":random"),
            (store_random_in_range, ":random", -3, 4),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, ":random"),
            (store_random_in_range, ":random", -3, 4),
            (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, ":random"),
        (try_end),
    (try_end),
]),
# #SB : add this to allow randomization of a single faction (see prsnt_dplmc_policy_management)
("dplmc_randomize_faction_domestic_policy",[
    (store_script_param, ":kingdom", 1),
    (try_for_range, ":slot", dplmc_slot_faction_centralization, dplmc_slot_faction_mercantilism + 1),
        (store_random_in_range, ":random", -3, 4),
        (faction_set_slot, ":kingdom", ":slot", ":random"),
    (try_end),
]),

("dplmc_is_affiliated_family_member",[
    (store_script_param, ":troop_id", 1),
    (assign, ":is_affiliated_family_member", 0),
    ##nested diplomacy start+
    (assign, ":save_reg1", reg1),#<- Save reg1 which gets overwritten by script_dplmc_troop_get_family_relation_to_troop
    ##nested diplomacy end+
    (try_begin),
        (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
        (try_begin),
            ##nested diplomacy start+ add use of dplmc_slot_troop_affiliated
            (this_or_next|troop_slot_eq, ":troop_id", dplmc_slot_troop_affiliated, 3),
            ##diplomacy end+
            (eq, "$g_player_affiliated_troop", ":troop_id"),
            (assign, ":is_affiliated_family_member", 1),
        (else_try),
            (is_between, ":troop_id", lords_begin, kingdom_ladies_end),
            ##nested diplomacy start+
                #(call_script, "script_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
            (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
            ##nested diplomacy end+
            (gt, reg0, 0),
            (call_script, "script_troop_get_relation_with_troop", "$g_player_affiliated_troop", ":troop_id"),
            (ge, reg0, -10),
            (assign, ":is_affiliated_family_member", 1),
        (try_end),
    (try_end),
    ##nested diplomacy start+
    (assign, reg1, ":save_reg1"),#revert register
    ##nested diplomacy end+
    (assign, reg0, ":is_affiliated_family_member"),
]),
("dplmc_affiliate_end",[
    (store_script_param, ":cause", 1),
    (assign, "$g_player_affiliated_troop", 0),
    (try_begin),
        (eq, ":cause", 1),
        (assign, ":max_penalty", -16),
        (assign, ":term", 20),
        (assign, ":honor_val", 10),
    (else_try),
        (assign, ":max_penalty", -12),
        (assign, ":honor_val", 5),
        (assign, ":term", 15),
    (try_end),
    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
        (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
        (gt, reg0, 0),
        (store_skill_level, ":value", "skl_persuasion", "trp_player"),
        (store_random_in_range, ":value", 0, ":value"),
        ##nested diplomacy start+   Fix mistake.
        ##
        ##OLD:
        #(val_add, ":value", ":max_penalty", ":value"),
        #
        #NEW:
        #I'm pretty sure this is what was intended.
        (val_add, ":value", ":max_penalty"),
        ##nested diplomacy end+
        (val_min, ":value", 0),
        (call_script, "script_change_player_relation_with_troop", ":family_member", ":value"),
    (try_end),
    (try_begin),
        (gt, "$player_honor", ":honor_val"),
        (val_add, ":term", ":honor_val"),
    (else_try),
        (val_add, ":term", "$player_honor"),
    (try_end),
    (store_current_hours, ":cur_hours"),
    (store_sub, ":affiliated_hours", ":cur_hours", "$g_player_affiliated_time"),
    (store_div, ":affiliated_days", ":affiliated_hours", 24),
    (val_sub, ":term", ":affiliated_days"),
    (val_max, ":term", 0),
    (val_min, ":term", 40),
    (troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
    (val_add, ":controversy", ":term"),
    (val_min, ":controversy", 100),
    (troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
]),
("dplmc_appoint_chamberlain",[
    (troop_set_auto_equip, "trp_dplmc_chamberlain", 0),
    (faction_get_slot, ":culture", "$players_kingdom", slot_faction_culture),
    (try_begin),
        (neg|is_between, ":culture", cultures_begin, cultures_end),
        (troop_get_slot, ":culture", "trp_player", slot_troop_culture),
    (try_end),
    (try_begin),
        (eq, ":culture", "fac_culture_dacian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_dacian_light10"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007840d824225e2a6129d51630a00000000000ac99d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_celtic"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_celtic_light1"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_celtic_boots"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000078b052189229dae5052a23b1b00000000000cb29b0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caledonian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_celtic_light4"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007ba0d94cf48e46eb2d18aa6db000000000009d6ec0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_sarmatian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_kaftan_3"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_sarmatian_shoes"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000079810d251271ab34535b5ac9b00000000001ecd150000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_germanic"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_germanic_light11"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000078a059592490357da6496c62900000000001da75b0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caucasian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_armenian_tunic_4"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_eastern_shoe_b"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007a200d48146928e3a5a892b1d000000000009bd720000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_parthian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_parthian_tunic_3"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_eastern_shoe_r"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007b504b4c44295ceb52471c6dc00000000001e56a20000000000000000"),
    (else_try),
        (this_or_next|eq, ":culture", "fac_culture_greek"),
        (eq, ":culture", "fac_culture_roman"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
    (else_try),
        (eq, ":culture", "fac_culture_judean"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_sarranid_cloth_robe_fancy_3"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007930ce1443b5a39c92392559d00000000000fc6dc0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_bosporan"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_bosporan_light2"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000079f0852cd46d49512e59aa60c000000000010b51e0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_arabian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_arabian_tunic_2"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007b90d354126a36acd5b6ed2e300000000001d449c0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_berber"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000007950c735036d44ed861cdd4e400000000001d48dd0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_garmantian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_garmantian_armor_4"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000078211450a58dd30cd2156e645000000000005556b0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_nubian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000078c04f3c3372bb26a9e7534d50000000000064b0b0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_saka"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_kaftan_3"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_eastern_shoe_y"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@0x0000000a4d0083ca3cab4767252a4b1100000000001ec9750000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_syrian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_arab_noble_tunic_1"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_eastern_shoe_y"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@00000000001144cc172ad258e2714d2b000000000015b4db0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_egyptian"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_head, "itm_numidian_wig"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_judean_tunic_4"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chamberlain", "@000000001d09400138c945269b71ad3400000000001d9b2b0000000000000000"),
    (else_try),
        (display_message, "@dplmc_appoint_chamberlain: Issue with culture of player faction detected."),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_caligea"),
    (try_end),
    (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
    #SB : grab all gold from chest troops (seneschals)
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
        (store_sub, ":chest_troop", ":center_no", towns_begin),
        (val_add, ":chest_troop", "trp_town_1_seneschal"),
        (store_troop_gold, ":cur_gold", ":chest_troop"),
        (troop_remove_gold, ":chest_troop", ":cur_gold"),
        (troop_add_gold, "trp_household_possessions", ":cur_gold"), #no script call
    (try_end),
]),
("dplmc_appoint_chancellor",[
    (troop_set_auto_equip, "trp_dplmc_chancellor", 0),
    (faction_get_slot, ":culture", "$players_kingdom", slot_faction_culture),
    (try_begin),
        (neg|is_between, ":culture", cultures_begin, cultures_end),
        (troop_get_slot, ":culture", "trp_player", slot_troop_culture),
    (try_end),
    (try_begin),
        (eq, ":culture", "fac_culture_dacian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_dacian_light10"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000078d0061ce559b8dc315c4bace000000000014a4f60000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_celtic"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_celtic_light1"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_celtic_boots"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007bb0980cb6f1451d6d46cb4e1000000000018d6e20000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caledonian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_celtic_light4"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000079d0000c868db8ecc72c6269b00000000000a14cd0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_sarmatian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_kaftan_3"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_sarmatian_shoes"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000078e004351472d93389e49d6eb00000000001142ed0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_germanic"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_germanic_light11"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000078c1195083554a8c4d3d1270d0000000000129ca50000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caucasian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_armenian_tunic_4"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_eastern_shoe_b"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007a60825503914ce59248b54940000000000119b630000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_parthian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_parthian_tunic_3"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_eastern_shoe_r"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000079600b404396565c7ab2a426d00000000001dd7230000000000000000"),
    (else_try),
        (this_or_next|eq, ":culture", "fac_culture_greek"),
        (eq, ":culture", "fac_culture_roman"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
    (else_try),
        (eq, ":culture", "fac_culture_judean"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_sarranid_cloth_robe_fancy_3"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000079f0da5092a7c724cd2b3366d00000000001249240000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_bosporan"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_bosporan_light2"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007930c14ce49a94d56656aa9e30000000000121b2a0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_arabian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_arabian_tunic_2"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007ac0541cf68e54e17ab92b51a00000000000e591d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_berber"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007a409554a291b4db2b38e546300000000001cbce20000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_garmantian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_garmantian_armor_4"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007a411a1c036d245a76431b71a00000000001de4f00000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_nubian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@00000007b904718e6713863c9571ab11000000000012a39c0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_saka"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_kaftan_2"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_eastern_shoe_b"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@0x0000000a640c94c9395c16325bd9d51200000000001db76d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_syrian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_arab_noble_tunic_2"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_eastern_shoe_r"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000003b11a5095923d0b6536dd6ec000000000006d11c0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_egyptian"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_judean_tunic_1"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_chancellor", "@000000003d05401136d24f5d15b754d400000000001e592c0000000000000000"),
    (else_try),
        (display_message, "@dplmc_appoint_chancellor: Issue with culture of player faction detected."),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_caligea"),
    (try_end),
    (assign, "$g_player_chancellor", "trp_dplmc_chancellor"),
]),
("dplmc_appoint_constable",[
    (troop_set_auto_equip, "trp_dplmc_constable", 0),
    (faction_get_slot, ":culture", "$players_kingdom", slot_faction_culture),
    (try_begin),
        (neg|is_between, ":culture", cultures_begin, cultures_end),
        (troop_get_slot, ":culture", "trp_player", slot_troop_culture),
    (try_end),
    (try_begin),
        (eq, ":culture", "fac_culture_dacian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_dacian_light10"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007b00442044af4c8cb9bb6c653000000000011c2e50000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_celtic"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_celtic_light1"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_celtic_boots"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007be0c140432dd31c66b0924dc00000000001204e20000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caledonian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_celtic_light4"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@0000000078a0d148868ca6a38d5b5b514000000000005acd50000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_sarmatian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_kaftan_3"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_sarmatian_shoes"),
        (troop_set_face_keys, "trp_dplmc_constable", "@0000000078605858519558d94eb6e265b00000000001237310000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_germanic"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_germanic_light11"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007800c3592429b8957608e231300000000001e49310000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_caucasian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_armenian_tunic_4"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_eastern_shoe_b"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007a3004581446ac6c72c89949b000000000009a5430000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_parthian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_parthian_tunic_3"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_eastern_shoe_r"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007ba00648432e24d4d15aa16d300000000000647630000000000000000"),
    (else_try),
        (this_or_next|eq, ":culture", "fac_culture_greek"),
        (eq, ":culture", "fac_culture_roman"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
    (else_try),
        (eq, ":culture", "fac_culture_judean"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_sarranid_cloth_robe_fancy_3"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007bf04058436d4b1d74433432f00000000001cd5230000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_bosporan"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_bosporan_light2"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_leather_boots"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007bf0911415a91d723339229a100000000001dbd0d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_arabian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_arabian_tunic_2"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007b000b18f2924aad8d465b74900000000001eab5d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_berber"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@0000000078409404829ac2e48ed9254ee00000000001a398d0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_garmantian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_garmantian_armor_4"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007b20d53501475b944e429cc6500000000000db6a30000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_nubian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_numidian_armor_5"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000007b4107109199c43669b36267b00000000001e18d40000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_saka"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_kaftan_1"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_eastern_shoe_r"),
        (troop_set_face_keys, "trp_dplmc_constable", "@0x0000000a7f04510c54e5d24d13ac96ee00000000001f174b0000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_syrian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_sarranid_cloth_robe_fancy_2"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_eastern_shoe_b"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000003210b34e28b6adc45a72c6a400000000001e19710000000000000000"),
    (else_try),
        (eq, ":culture", "fac_culture_egyptian"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_judean_tunic_3"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
        (troop_set_face_keys, "trp_dplmc_constable", "@000000002908e5c1252ad46cd48ecd2c00000000001ec8540000000000000000"),
    (else_try),
        (display_message, "@dplmc_appoint_constable: Issue with culture of player faction detected."),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_roman_toga"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_caligea"),
    (try_end),
    (assign, "$g_player_constable", "trp_dplmc_constable"),
]),
#Importing a script used in Custom Commander.  The inventory copying is used
#as a clever way to make "unmodifiable" views of others' equipment (both the
#PC and NPC have their inventory copied before viewing, and after the window
#closes the copies are written back over the originals).
("dplmc_copy_inventory",[
    (store_script_param_1, ":source"),
    (store_script_param_2, ":target"),

    (troop_clear_inventory, ":target"),
    (troop_get_inventory_capacity, ":inv_cap", ":source"),
    (try_for_range, ":i_slot", 0, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
        (troop_set_inventory_slot, ":target", ":i_slot", ":item"),
        (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
        (troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
        (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
        (gt, ":amount", 0),
        (troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
    (try_end),
]),

#Decide whether an NPC wants to exchange a fief or not.
#
# param#1 is NPC being asked
# param#2 is that NPC's fief being asked for
# param#3 is the one asking (usually the player)
# param#4 is the fief being offered in exchange
#
# Result is returned in reg0.  Negative means "no", zero means "yes",
# positive means "yes but you have to pay me this amount".
# If the result is negative, the response string is stored in s14.
("dplmc_evaluate_fief_exchange",[
    (store_script_param, ":target_npc", 1),
    (store_script_param, ":target_fief", 2),
    (store_script_param, ":asker", 3),
    (store_script_param, ":offered_fief", 4),
    (assign, ":result", -1),
    (assign, reg0, ":result"),
    (str_store_string, s14, "str_ERROR_string"),
    (try_begin),
        #Both NPCs are valid, and are not same character.  One can be the player.
        (neq, ":target_npc", ":asker"),
        (is_between, ":target_npc", heroes_begin, heroes_end),
        (this_or_next|is_between, ":asker", heroes_begin, heroes_end),
            (eq,":asker","trp_player"),
        #Both fiefs are valid and owned by the lords in the arguments
        (is_between, ":target_fief", centers_begin, centers_end),
        (party_slot_eq, ":target_fief", slot_town_lord, ":target_npc"),
        (is_between, ":offered_fief", centers_begin, centers_end),
        (party_slot_eq, ":offered_fief", slot_town_lord, ":asker"),
        #The lords are in the same faction
        (store_troop_faction, ":target_faction", ":target_npc"),
        (store_troop_faction, ":asker_faction", ":asker"),
        (try_begin),
            #Special handling needed for player faction
            (eq, ":asker", "trp_player"),
            (neg|eq, ":target_faction", ":asker_faction"),
            (assign, ":asker_faction", "$players_kingdom"),
        (try_end),
        (this_or_next|eq, ":target_faction", ":asker_faction"),
        (this_or_next|faction_slot_eq,":target_faction",slot_faction_leader,":asker"),
        (faction_slot_eq,":asker_faction",slot_faction_leader,":target_npc"),
        #Get prosperity for use in later tests
        (party_get_slot, ":target_prosperity", ":target_fief", slot_town_prosperity),
        (party_get_slot, ":offered_prosperity", ":offered_fief", slot_town_prosperity),
        (store_div, ":min_prosperity", ":target_prosperity", 10),
        (val_mul, ":min_prosperity", 10),
        #...take into account relation
        (call_script, "script_troop_get_relation_with_troop", ":target_npc", ":asker"),
        (store_div, ":relation_div_10", reg0, 10),
        (val_sub, ":min_prosperity", ":relation_div_10"),
        #...take into account persuasion
        (store_skill_level, ":asker_persuasion", "skl_persuasion", ":asker"),
        (val_sub, ":min_prosperity", ":asker_persuasion"),
        #...take into account personal (not party) trade skill
        (store_skill_level, ":asker_trade", "skl_trade", ":asker"),
        (val_sub, ":min_prosperity", ":asker_trade"),
        #...don't let it rise above original's prosperity.
        (val_min, ":min_prosperity", ":target_prosperity"),
        #target_type 1 = village, 2 = castle, 3 = town
        (assign, ":target_type", 0),
        (try_begin),
            (party_slot_eq, ":target_fief", slot_party_type, spt_town),
            (assign, ":target_type", 3),
        (else_try),
            (party_slot_eq, ":target_fief", slot_party_type, spt_castle),
            (assign, ":target_type", 2),
        (else_try),
            (party_slot_eq, ":target_fief", slot_party_type, spt_village),
            (assign, ":target_type", 1),
        (try_end),
        (ge, ":target_type", 1),#break with error if the type was bad
        #offered_type: 1 = village, 2 = castle, 3 = town
        (assign, ":offered_type", 0),
        (try_begin),
            (party_slot_eq, ":offered_fief", slot_party_type, spt_town),
            (assign, ":offered_type", 3),
        (else_try),
            (party_slot_eq, ":offered_fief", slot_party_type, spt_castle),
            (assign, ":offered_type", 2),
        (else_try),
            (party_slot_eq, ":offered_fief", slot_party_type, spt_village),
            (assign, ":offered_type", 1),
        (try_end),
        (ge, ":offered_type", 1),#break with error if the type was bad
        #Now execute comparison logic:
        (try_begin),
            (party_slot_ge, ":offered_fief", slot_party_looted_left_days, 1),
            (str_store_party_name, s14, ":offered_fief"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_looted"),
        (else_try),
            (party_slot_ge, ":offered_fief", slot_center_ongoing_rebellion, 1),
            (str_store_party_name, s14, ":offered_fief"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_rebell_on"),
        (else_try),
            (party_slot_ge, ":offered_fief", slot_center_can_rebell, 1),
            (party_get_slot, ":culture", ":offered_fief", slot_center_culture),
            (store_faction_of_troop, ":faction", ":target_npc"),
            (neg|faction_slot_eq, ":faction", slot_faction_culture, ":culture"),
            (str_store_party_name, s14, ":offered_fief"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_rebell_can"),
        (else_try),
            #refuse to trade town for a castle or village
            (lt, ":offered_type", ":target_type"),
            (eq, ":target_type", 3),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_town"),
        (else_try),
            #refuse to trade any better type for a worse type
            (lt, ":offered_type", ":target_type"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_castle"),
        (else_try),
            #refuse to trade for something under siege or being raided
            (this_or_next|party_slot_eq, ":offered_fief", slot_village_state, svs_under_siege),
            (party_slot_eq, ":offered_fief", slot_village_state, svs_being_raided),
            (str_store_party_name, s14, ":offered_fief"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_s14_attack"),
        (else_try),
            #accept a trade if the offered type is better
            (lt, ":target_type", ":offered_type"),
            (str_store_string, s14, "str_dplmc_fief_exchange_accept"),
            (assign, ":result", 0),
        (else_try),
			#refuse to trade away home center (unless trading up for a better type)
			#Target fief is home of NPC...
            (this_or_next|party_slot_eq, ":target_fief", dplmc_slot_center_original_lord, ":target_npc"),
            (troop_slot_eq, ":target_npc", slot_troop_home, ":target_fief"),
            (neg|party_slot_eq, ":offered_fief", dplmc_slot_center_original_lord, ":target_npc"),
			#...and offered fief is not.
            (neg|troop_slot_eq, ":target_npc", slot_troop_home, ":offered_fief"),
            (this_or_next|neg|is_between, ":target_npc", companions_begin, companions_end),
            (neg|troop_slot_eq, ":target_npc", slot_troop_town_with_contacts, ":offered_fief"),
            (str_store_party_name, s14, ":target_fief"), #Line added by zerilius
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_home"),
        (else_try),
            #refuse trade if prosperity is too low
            (lt, ":offered_prosperity", ":min_prosperity"),
            (str_store_string, s14, "str_dplmc_fief_exchange_refuse_rich"),
        (else_try),
            #accept trade for 0 or more denarii
            (store_sub, ":result", ":target_prosperity", ":offered_prosperity"),
            (val_mul, ":result", ":target_type"),
            (val_mul, ":result", 36),#Should probably be 60 instead
            #(val_div, ":result", 100),
            (val_add, ":result", 2000),
            (val_max, ":result", 0),
            (try_begin),
                (ge, ":result", 1),
                (assign, reg3, ":result"),
                (str_store_string, s14, "str_dplmc_fief_exchange_accept_reg3_denars"),
            (else_try),
                (str_store_string, s14, "str_dplmc_fief_exchange_accept"),
            (try_end),
        (try_end),
    (try_end),
    (assign, reg0, ":result"),
]),
# script_dplmc_time_sorted_heroes_for_center_aux
# For internal use only
# param 1: center no
# param 2: party_no_to_collect_heroes
# param 3: minimum time since last met (inclusive), or negative for no restriction
# param 4: maximum time since last met (exclusive), or negative for no restriction
("dplmc_time_sorted_heroes_for_center_aux",[
    (store_script_param_1, ":center_no"),
    (store_script_param_2, ":party_no_to_collect_heroes"),
    (store_script_param, ":min_time", 3),
    (store_script_param, ":max_time", 4),

    (store_current_hours, ":current_hours"),

    (party_get_num_companion_stacks, ":num_stacks",":center_no"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (is_between, ":stack_troop", active_npcs_begin,kingdom_ladies_end),
        ##(neq, ":stack_troop", "trp_player"),#freelancer, since player party is now attached

        (assign, ":c", 0),
        (try_begin),
            (ge, "$enlisted_party", 1),#is freelancing
            (main_party_has_troop, ":stack_troop"),#to avoid companions spawning in castle
            (assign, ":c", 1),
        (try_end),
        (eq, ":c", 0),
        #get time since last talk
        (troop_get_slot, ":troop_last_talk_time", ":stack_troop", slot_troop_last_talk_time),
        (store_sub, ":time_since_last_talk", ":current_hours", ":troop_last_talk_time"),
        #add if time meets constraints
        (this_or_next|ge, ":time_since_last_talk", ":min_time"),
        (lt, ":min_time", 0),
        (this_or_next|lt, ":time_since_last_talk", ":max_time"),
        (lt, ":max_time", 0),
        (party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
    (try_end),
    (party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
    (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
        (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
        (call_script, "script_dplmc_time_sorted_heroes_for_center_aux", ":attached_party", ":party_no_to_collect_heroes",":min_time",":max_time"),
    (try_end),
]),

# script_dplmc_time_sorted_heroes_for_center
# Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
# Output: none, adds heroes to the party_no_to_collect_heroes party
# The catch is that it returns heroes who haven't been met in a day
# or more before others, for greater use in feasts.
("dplmc_time_sorted_heroes_for_center",[
    (store_script_param_1, ":center_no"),
    (store_script_param_2, ":party_no_to_collect_heroes"),
    (party_clear, ":party_no_to_collect_heroes"),
    (try_begin),
        (eq, "$g_player_court", ":center_no"),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
        ##diplomacy start+
        #It's not exactly clear if this would work for kingdom ladies.  If they
        #can go from slto_kingdom_lady to slto_inactive, this could take them
        #from there to slto_kingdom_hero unintentionally.
        #
        #Because of this, don't enable this for now.  Elsewhere (where defections
        #occur) add alternate behavior for promoted kingdom ladies.
        #
        #TODO: Later, make sure that kingdom ladies are never inactive normally,
        #so this loop can be expanded to work with them.
        ##diplomacy end+
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "fac_player_supporters_faction"),
            (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
            (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
            (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she does not have a party
            (neq, ":active_npc", "$g_player_minister"),
            (party_add_members, ":party_no_to_collect_heroes", ":active_npc"),
            # (set_visitor, ":cur_pos", ":active_npc"),
            # (val_add,":cur_pos", 1),
        (try_end),
    (try_end),
    #Heroes you haven't spoken to in 24+ hours
    (call_script, "script_dplmc_time_sorted_heroes_for_center_aux", ":center_no", ":party_no_to_collect_heroes", 24, -1),
    #Heroes you haven't spoken to in 12 to 24 hours
    (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",":center_no", ":party_no_to_collect_heroes", 12, 24),
    #Everyone else
    (call_script, "script_dplmc_time_sorted_heroes_for_center_aux", ":center_no", ":party_no_to_collect_heroes", -1, 12),
]),

# script_dplmc_faction_leader_splits_gold
# INPUT: arg1 = troop_id, arg2 = new faction_no
# OUTPUT: none
("dplmc_faction_leader_splits_gold",[
	(store_script_param_1, ":faction_no"),
    (store_script_param_2, ":king_gold"),
	(assign, ":push_reg0", reg0),#revert register value at end of script
	(assign, ":push_reg1", reg1),#revert register value at end of script

	(faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
	(faction_get_slot, reg0, ":faction_no", dplmc_slot_faction_centralization),
	(val_clamp, reg0, -3, 4),
	(val_mul, reg0, -5),
	(try_begin),
		(troop_slot_ge, ":faction_liege", slot_troop_wealth, 20000),
		(val_add, reg0, 20),#20% if the king is at or above his starting gold
	(else_try),
		(val_add, reg0, 50),#50% otherwise
	(try_end),
	(val_add, reg0, 50),
	(store_mul, ":lord_gold", ":king_gold", reg0),#king splits other half among lords
	(val_div, ":lord_gold", 100),
	(val_sub, ":king_gold", ":lord_gold"),
	(try_begin),
		#If there's enough gold to give a meaningful amount to everyone, do so.
		#(This accomplishes two things.  It makes the distribution more even, and
		#it prevents this script from taking an unreasonably long time for very
		#large amounts of gold.)
		#
		#"Meaningful" is at least 300, because that's the minimum amount of gold a
		#lord will to to a fief to collect (it is also the AI recruitment cost on
		#hard).
		(assign, ":num_lords", 0),#<-- number of lords in faction, not including faction leader
		(try_for_range, ":lord_no", heroes_begin, heroes_end),
			(store_troop_faction, ":lord_faction_no", ":lord_no"),
			(eq, ":faction_no", ":lord_faction_no"),
			(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
			(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
			(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
			(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
			(ge, ":lord_party", 0),
			(val_add, ":num_lords", 1),
		(try_end),
		(try_begin),
			#handle player
			(eq, "$players_kingdom", ":faction_no"),
			(neq, "trp_player", ":faction_liege"),
			(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
			(val_add, ":num_lords", 1),
		(try_end),
		(gt, ":num_lords", 0),#<-- can fail
		(store_div, ":gold_to_each", ":lord_gold", ":num_lords"),
		(ge, ":gold_to_each", 300),
		(val_div, ":gold_to_each", 150),#regularize (standard reinforcement costs for easy/medium/hard are 600/450/300, which are multiples of 150)
		(val_mul, ":gold_to_each", 150),

		#(try_begin),
		#	(ge, "$cheat_mode", 1),
		#	(assign, reg0, ":num_lords"),
		#	(assign, reg1, ":gold_to_each"),
		#	(str_store_faction_name, s5, ":faction_no"),
		#	(display_message, "@ {reg0} vassals of the {s5} receive {reg1} denarii each (dplmc_faction_leader_splits_gold)"),
		#(try_end),

		(try_for_range, ":lord_no", heroes_begin, heroes_end),
			(ge, ":lord_gold", ":gold_to_each"),
			#verify lord is vassal of kingdom
			(store_troop_faction, ":lord_faction_no", ":lord_no"),
			(eq, ":faction_no", ":lord_faction_no"),
			(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
			(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
			(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
			(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
			(ge, ":lord_party", 0),
			#give gold to lord
			(val_sub, ":lord_gold", ":gold_to_each"),
			#(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
			#(val_add, reg0, ":gold_to_each"),
			#(troop_set_slot, ":lord_no", slot_troop_temp_slot, reg0),
			##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
			(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_to_each", ":lord_no"),
		(try_end),
		(try_begin),
			(ge, ":lord_gold", ":gold_to_each"),
			#give gold to player if player is vassal of kingdom
			(eq, "$players_kingdom", ":faction_no"),
			(neq, "trp_player", ":faction_liege"),
			(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
			(val_sub, ":lord_gold", ":gold_to_each"),
			(troop_get_slot, reg0, "trp_player", slot_troop_temp_slot),
			(val_add, reg0, ":gold_to_each"),
			(troop_set_slot, "trp_player", slot_troop_temp_slot, reg0),
			##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
		(try_end),
	(try_end),
	#Now, distribute the remaining gold.  Assign gold in increments of 300,
	#because that's the minimum amount of gold a lord will go to a fief for
	#(also the AI recruitment cost on hard).
	(store_div, ":count", ":lord_gold", 300),
	(val_max, ":count", 1),
	(try_for_range, ":unused", 0, ":count"),
		(ge, ":lord_gold", 300),
		(call_script, "script_cf_get_random_lord_except_king_with_faction", ":faction_no"),
		(is_between, reg0, heroes_begin, heroes_end),
		(assign, ":troop_no", reg0),
		(val_sub, ":lord_gold", 300),
		(troop_get_slot, reg0, ":troop_no", slot_troop_temp_slot),
		(val_add, reg0, 300),
		(troop_set_slot, ":troop_no", slot_troop_temp_slot, reg0),
		#(call_script, "script_troop_add_gold", ":troop_no", 300),
	(try_end),

	#Now the distribution is set.  Give each one his allotment.
	(try_for_range, ":lord_no", heroes_begin, heroes_end),
		(ge, ":lord_gold", ":gold_to_each"),
		#verify lord is vassal of kingdom
		(store_troop_faction, ":lord_faction_no", ":lord_no"),
		(eq, ":faction_no", ":lord_faction_no"),
		(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
		(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
		(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
		(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
		(ge, ":lord_party", 0),
		#get promised gold
		(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
		(neq, reg0, 0),
		#(try_begin),
		#	(ge, "$cheat_mode", 1),
		#	(str_store_troop_name, s4, ":lord_no"),
		#	(str_store_faction_name, s5, ":faction_no"),
		#	(str_store_troop_name, s6, ":faction_liege"),
		#	(display_message, "@{!}{s4} of the {s5} receives {reg0} denarii (dplmc_faction_leader_splits_gold)"),
		#(try_end),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", reg0, ":lord_no"),
		(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
	(try_end),

	(val_add, ":king_gold", ":lord_gold"),#Give remaining gold to king
	(try_begin),
		(ge, "$cheat_mode", 1),
		(str_store_troop_name, s4, ":troop_no"),
		(str_store_faction_name, s5, ":faction_no"),
		(str_store_troop_name, s6, ":faction_liege"),
		(display_message, "@{!}{s6} of the {s5} retains the remaining {reg0} denarii (dplmc_faction_leader_splits_gold)"),
	(try_end),

	#(call_script, "script_troop_add_gold", ":faction_liege", ":king_gold"),
	(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":king_gold", ":faction_liege"),
	(assign, reg0, ":push_reg0"),#revert register value
	(assign, reg1, ":push_reg1"),#revert register value
]),

#script_dplmc_lord_return_from_exile
# INPUT: arg1 = troop_id, arg2 = new faction_no
# OUTPUT: none
("dplmc_lord_return_from_exile",[
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":faction_no"),
    #Check validity
    (try_begin),
        (is_between, ":troop_no", heroes_begin, heroes_end),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (neq, ":troop_no", "trp_player"),
        (faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
        #The lord definitely should not already belong to a kingdom
        (store_troop_faction, ":old_faction", ":troop_no"),
        (neg|is_between, ":old_faction", kingdoms_begin, kingdoms_end),
        (try_begin),
			#Handle separately for adding to the player's faction
			#The player may decide to accept or reject the return
			(this_or_next|eq, ":faction_liege", "trp_player"),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			#(eq, 1, 0),#<-- temporarily disable
			#Lord comes to petition the player instead of automatically returning
			(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
			(troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive),
			#Show event (no log without actual faction change)
			(str_store_troop_name_link, s4, ":troop_no"),
			(str_store_faction_name_link, s5, ":faction_no"),
			(faction_get_color, ":color", ":faction_no"), #SB : store colour for logs
			(str_store_troop_name_link, s6, ":faction_liege"),
			(display_message, "@{s4} has returned from exile, seeking refuge with {s6} of {s5}.", ":color"),
		    #Remove party
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
            (call_script, "script_destroy_party", ":led_party"),
            (troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
			#
        (else_try),
			 #NPC king auto-accepts
			 #Normalize relation between NPC and king
			 (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_liege"),
			 (store_sub, ":relation_change", 0, reg0),#enough to increase to 0 if negative
			 (val_max, ":relation_change", 5),
			 (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_liege", ":relation_change"),
			 #Perform reverse of relation change for exile
			 (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #all lords in own faction, and relatives regardless of faction
				(assign, ":relation_change", 0),#no change for non-relatives in other factions
				(try_begin),
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":faction_no", ":active_npc_faction"),
					#Auto-exiling someone at -75 relation to his liege gives a -1 base
					#relation penalty from other lords, so the gain is 1 by default.
					(assign, ":relation_change", 1),
				(try_end),
				##(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
				(assign, ":family_relation", reg0),
				(try_begin),
					(gt, ":family_relation", 1),
					(store_div, ":family_modifier", reg0, 3),
					(val_add, ":relation_change", ":family_modifier"),
				(try_end),

				(neq, ":relation_change", 0),

				(call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":active_npc", ":relation_change"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s17, ":active_npc"),
					(str_store_troop_name, s18, ":faction_liege"),
					(assign, reg3, ":relation_change"),
					(display_message, "str_trial_influences_s17s_relation_with_s18_by_reg3"),
				(try_end),
			 (try_end),#end try for range :active_npc

			#Now actually change the faction
			(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
			(try_begin), #new-begin
				(neq, ":faction_no", "fac_player_supporters_faction"),
				(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_retirement),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile), #SB : revoke exile
				(troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		    (try_end), #new-end

			#Log event
			(str_store_troop_name_link, s4, ":troop_no"),
			(str_store_faction_name_link, s5, ":faction_no"),
			(str_store_troop_name_link, s6, ":faction_liege"),
			(faction_get_color, ":color", ":faction_no"), #SB : store colour for logs
			(display_log_message, "@{s4} has been granted a pardon by {s6} of {s5} and has returned from exile.", ":color"),

            #SB : spawn full army
            (troop_set_slot, ":troop_no", slot_troop_spawned_before, 0),
			(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
            (call_script, "script_destroy_party", ":led_party"),
            (troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
        (try_end),#end NPC king auto-accepts
    (else_try),
	    #Failure.  Perform string register assignment first to avoid differences
		#between debug and non-debug behavior.
		(str_store_troop_name, s5, ":troop_no"),
		(str_store_faction_name, s7, ":faction_no"),
		#(ge, "$cheat_mode", 1),#<-- always show this
		(display_message, "@{!}DEBUG : failure in dplmc_lord_return_from_exile((s5}, {s7})"),
    (try_end),
]),

#script_dplmc_get_troop_morality_value
# INPUT: arg1 = troop_id, arg2 = morality type
# OUTPUT: reg0 has morality value, or 0 if inapplicable
("dplmc_get_troop_morality_value",[
    (store_script_param, ":troop_id", 1),
    (store_script_param, ":morality_type", 2),

    (assign, reg0, 0),
    (try_begin),
        (neg|is_between, ":troop_id", companions_begin, companions_end),#<-- result is 0 for non-companions
    (else_try),
        (troop_slot_eq, ":troop_id", slot_troop_morality_type, ":morality_type"),
        (troop_get_slot, reg0, ":troop_id", slot_troop_morality_value),
    (else_try),
        (troop_slot_eq, ":troop_id", slot_troop_2ary_morality_type, ":morality_type"),
        (troop_get_slot, reg0, ":troop_id", slot_troop_2ary_morality_value),
    (try_end),
]),

#script_dplmc_print_subordinate_says_sir_madame_to_s0
#
#In a number of circumstances a subordinate (a soldier in the player's employ) will refer
#to him as "sir" or "madame".  This is intended as a sign of respect, but becomes
#unintentionally disrespectful if the player would ordinarily merit a higher title.
#
#This function does not take into account the personal characteristics of the speaker in
#any way.  That logic should occur elsewhere.
#
#input: none
#output: reg0 gets a number corresponding to the title used
#1: str_dplmc_sirmadame
#2: str_dplmc_my_lordlady
#3: str_dplmc_your_highness
#sepcial cases:
#1: if players is talking to spouse then use "my love"
#2: if player is talking to some lord lady use playername
#3: for companions use the companion honorific
("dplmc_print_subordinate_says_sir_madame_to_s0",[
    (assign, ":highest_honor", 1),#{sir/madame}
    #initialize variables for following steps
    (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),

    (str_store_troop_name, s0, "trp_player"), # default

    (try_begin),
        #disable extra honors when the player is not recognized
        (gt, "$sneaked_into_town", disguise_none),
        (assign, ":highest_honor", 1),
    (else_try),
        #check if the player is the spouse of one of a widely recognized monarch,
        #or if the player is the ruler of one of the starting kingdoms (this can't happen but check anyway)
        (ge, ":player_spouse", 1),
        (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
            (this_or_next|faction_slot_eq, ":faction_no", slot_faction_leader, "trp_player"),
            (faction_slot_eq, ":faction_no", slot_faction_leader, ":player_spouse"),
            (val_max, ":highest_honor", 3),
        (try_end),
        (this_or_next|is_between, ":player_spouse", kings_begin, kings_end),
      #  (this_or_next|is_between, ":player_spouse", pretenders_begin, pretenders_end),
        (ge, ":highest_honor", 3),
        (val_max, ":highest_honor", 3),
        #Do not continue, since you've already used the highest available honor.
    (else_try),
        #the player is head of his own faction
        (ge, "$players_kingdom", 0),
        #faction leader is player, or faction leader is spouse and spouse is valid
        (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
        (faction_slot_eq, "$players_kingdom", slot_faction_leader, ":player_spouse"),
        (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
        (ge, ":player_spouse", 1),

        (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
        (try_begin),
            #If you have sufficient right-to-rule and renown, your subjects
            #will call you "highness".
            (ge, "$player_right_to_rule", 10),
            (store_sub, reg0, 75 + 75, "$player_right_to_rule"),
            (val_mul, reg0, 1200 // 75),#minimum required renown (as an aside, 1200 is evenly divisibly by 75)
            #examples: at right to rule 50, renown must be at least 1600
            #          at right to rule 99, renown must be at least 816
            #          at right to rule 10, renown must be at least 2240
            (ge, ":player_renown", reg0),
            (val_max, ":highest_honor", 3),
        (else_try),
            #"Highness" is also used if the player's kingdom holds meaningful territory.
            (try_begin),
                #Recalculate the cached value if it's suspicious
                (faction_slot_eq, "$players_kingdom", slot_faction_num_castles, 0),
                (faction_slot_eq, "$players_kingdom", slot_faction_num_towns, 0),
                (call_script, "script_faction_recalculate_strength", "$players_kingdom"),
            (else_try),
                #Recalculate the cached value if it's obviously wrong
                (this_or_next|neg|faction_slot_ge, "$players_kingdom", slot_faction_num_castles, 0),
                (neg|faction_slot_ge, "$players_kingdom", slot_faction_num_towns, 0),
                (call_script, "script_faction_recalculate_strength", "$players_kingdom"),
            (try_end),
            #Territory points: castles = 2, towns = 3 (ignore villages)
            (faction_get_slot, ":territory_points", "$players_kingdom", slot_faction_num_towns),
            (val_mul, ":territory_points", 3),
            (faction_get_slot, reg0, "$players_kingdom", slot_faction_num_castles),
            (val_add, ":territory_points", reg0),
            (val_add, ":territory_points", reg0),
            #If the player owns even a single center, that's worth at least "my lord" from his followers
            (ge, ":territory_points", 1),
            (val_max, ":highest_honor", 2),
            #By default there are around 48 castles and 22 towns on the map, for a total of 70
            #centers, and 162 "points" if weighting castles = 2 and towns = 3.
            (store_sub, ":global_points", towns_end, towns_begin),
            (val_mul, ":global_points", 3),
            (store_sub, reg0, castles_end, castles_begin),
            (val_add, ":global_points", reg0),
            (val_add, ":global_points", reg0),
            #By default there are 6 NPC kingdoms, averaging 8 castles and 3.66... towns or
            #27 points each (although the initial distribution of territory is not even).
            (store_sub, ":number_kingdoms", npc_kingdoms_end, npc_kingdoms_begin),
            (val_max, ":number_kingdoms", 1),
            #Territory must be at least 3/4 the total points divided by number of initial kingdoms.
            #Right to rule applied as a percentage bonus, scaled so that you gain recognition with
            #75% right to rule and a 50% size kingdom.

            #What I want is: ( (RtR * 2/3) + 100 ) * territory * kingdoms >= globe * 3/4
            #This is equivalent to: (RtR * 2 + 300) * territory * kingdoms * 4 >= globe * 9
            #The re-ordering is because of rounding.
            (store_mul, ":target_points", ":global_points", 9),
            (store_mul, reg0, "$player_right_to_rule", 2),
            (val_add, reg0, 300),
            (val_mul, reg0, ":territory_points"),
            (val_mul, reg0, ":number_kingdoms"),
            (val_mul, reg0, 4),
            (ge, reg0, ":target_points"),
            (val_max, ":highest_honor", 3),
        (try_end),
        #stop evaluation if you reached highest honor
        (ge, ":highest_honor", 3),
    (else_try),
        #the player is a vassal of one of the initial kingdoms
        (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        (val_max, ":highest_honor", 1),
        (eq, "$player_has_homage", 1),#<- can fail
        (val_max, ":highest_honor", 2),
    (try_end),

    (try_begin),
        (eq, "$g_is_emperor", 1),
        (ge, ":highest_honor", 3),
        (str_store_string, s0, "@Divine Caesar"),
    (else_try),
        (ge, ":highest_honor", 3),
        (str_store_string, s0, "str_dplmc_your_highness"),
    (else_try),
        (eq, ":highest_honor", 2),
        (str_store_string, s0, "str_dplmc_my_lordlady"),
    (else_try),
        (str_store_string, s0, "str_dplmc_sirmadam"),
    (try_end),

      ##Special cases
    (try_begin),
        (gt, ":player_spouse", 0),
        (eq, ":player_spouse", "$g_talk_troop"),
        (str_store_string, s0, "@my love"),
    (else_try),
        (is_between, "$g_talk_troop", lords_begin, kingdom_ladies_end),
        (str_store_troop_name, s0, "trp_player"),
    (else_try),
        (eq, "$sneaked_into_town", disguise_none),
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (ge, ":highest_honor", 1),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
        (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
        (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
        (ge, ":honorific", "str_npc1_honorific"),
        (str_store_string, s0, ":honorific"),
    (else_try),
        (eq, ":highest_honor", 1),
        (is_between, "$g_talk_troop", heroes_begin, heroes_end),
        (str_store_string, s0, "str_dplmc_sirmadame"),
    (try_end),
    (assign, reg0, ":highest_honor"),
]),

#"script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0"
#
#In a number of circumstances a commoner, who might or might not be a subject of
#the player, will refer to him as "sir" or "madame."  This script determines whether
#a different title would be warranted.
#
#input: party_no (usually a village or town)
#output: reg0 gets a number corresponding to the title used
("dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", [
    (store_script_param_1, ":party_no"),

    (assign, ":title_level", 1),
    (str_store_string, s0, "str_dplmc_sirmadam"),
    (store_faction_of_party, ":party_faction"),

    (try_begin),
        (eq, "$sneaked_into_town", disguise_none),#disable extra honors when the player is not recognized
        (ge, ":party_no", 0),

        #This is used in various conditions below, so I am calling it once
        #for simplicity.
        (assign, ":save_g_talk_troop", "$g_talk_troop"),
        (assign, ":save_g_encountered_party", "$g_encountered_party"),
        (try_begin),
            (neq, ":party_no", "$g_encountered_party"),
            (assign, "$g_encountered_party", -1),
            (assign, "$g_talk_troop", -1),
        (try_end),
        (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
        (assign, ":title_level", reg0),
        (assign, "$g_encountered_party", ":save_g_encountered_party"),
        (assign, "$g_talk_troop", ":save_g_talk_troop"),

        (try_begin),
            #The player is a full member of the faction: use full honors
            (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
            (ge, reg0, DPLMC_FACTION_STANDING_DEPENDENT),
            #(nothing more needs to be done)
        (else_try),
            #the faction has recognized him formally: use full honors
            (this_or_next|eq, ":party_no", "p_main_party"),
            (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
            (faction_slot_ge, ":party_faction", slot_faction_recognized_player, 1),
            #(nothing more needs to be done)
        (else_try),
            #The player is the lord of the town: keep result from script_dplmc_print_subordinate_says_sir_madame_to_s0
            (is_between, ":party_no", centers_begin, centers_end),
            (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
            #(nothing more needs to be done)
        (else_try),
            #Subjects of neutral kingdoms will use titles up to "my lord".
            (store_relation, ":relation", "fac_player_supporters_faction", ":party_faction"),
            (ge, ":relation", 0),
            (try_begin),
                (ge, ":title_level", 3),
                (assign, ":title_level", 2),
                (str_store_string, s0, "str_dplmc_my_lordlady"),
            (try_end),
        (else_try),
            #Subjects of kingdoms at war (that do not recognize the player) and all cases not
            #yet mentioned will reduce the "level" of the title awarded to the player by 1, to
            #a minimum of 1.
            (try_begin),
                (ge, ":title_level", 3),
                (assign, ":title_level", 2),
                (str_store_string, s0, "str_dplmc_my_lordlady"),
            (else_try),
                (eq, ":title_level", 2),
                (assign, ":title_level", 1),
                (str_store_string, s0, "str_dplmc_sirmadam"),
            (try_end),
        (try_end),
    (try_end),

    ##Special cases
    (try_begin),
        (neq, ":party_no", "$g_encountered_party"),
    (else_try),
        (eq, "$sneaked_into_town", disguise_none),
        (ge, ":title_level", 1),
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
        (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
        (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
        (ge, ":honorific", "str_npc1_honorific"),
        (str_store_string, s0, ":honorific"),
    (else_try),
        (eq, ":title_level", 1),
        (is_between, "$g_talk_troop", heroes_begin, heroes_end),
        (assign, ":title_level", "str_dplmc_sirmadame"),
    (try_end),

    (assign, reg0, ":title_level"),

    ##Switch to cultural equivalents
    #(try_begin),
    #   (eq, ":party_no", "$g_encountered_party"),
    #   (is_between, "$g_talk_troop", heroes_begin, heroes_end),
    #   (troop_get_slot, ":culture_faction", "$g_talk_troop", slot_troop_original_faction),
    #   (is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
    #(else_try),
    #   (eq, ":party_no", "$g_encountered_party"),
    #   (ge, "$g_talk_troop", soldiers_begin),
    #   (store_faction_of_troop, ":culture_faction", "$g_talk_troop"),
    #	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
    #(else_try),
    #   (is_between, ":party_no", centers_begin, centers_end),
    #   (party_get_slot, ":culture_faction", ":party_no", slot_center_original_faction),
    #	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
    #(else_try),
    #   (assign, ":culture_faction", ":party_faction"),
    #(try_end),
    #(try_begin),
    #   (is_between, "$g_talk_troop", companions_begin, companions_end),#do not switch
    #(else_try),
    #   (eq, ":title_level", 1),
    #	(eq, ":culture_faction", "fac_kingdom_6"),
    #	(str_store_string, s0, "@{!}{sahib/sahiba}"),
    #(try_end),
]),

# script_cf_is_female
("cf_is_female", [
    (store_script_param, ":type", 1),
	(this_or_next|eq, ":type", tf_female),
	(eq, ":type", tf_girl),
]),

##script_cf_dplmc_troop_is_female
#This exists to make it easy to modify this to work with mods that redefine the troop types.
#See script_dplmc_store_troop_is_female
#INPUT: arg1: troop_no
#OUTPUT: none
("cf_dplmc_troop_is_female",[
	(store_script_param_1, ":troop_no"),
	(assign, ":type", 0),
	(ge, ":troop_no", 0),#Undefined behavior when the arguments are invalid.
	(try_begin),
        (eq, ":troop_no", active_npcs_including_player_begin),
        (assign, ":troop_no", "trp_player"),
	(try_end),
    (troop_get_type, ":type", ":troop_no"),
    (call_script, "script_cf_is_female", ":type"),
]),

  ##script_dplmc_store_troop_is_female
  #
  #This exists to make it easy to modify this to work with mods that redefine the troop types.
  #
  #If you change this, remember to also change script_cf_dplmc_troop_is_female and
  #script_dplmc_store_is_female_troop_1_troop_2
  #
  #INPUT: arg1: troop_no
  #
  #OUTPUT:
  #       reg0: 1 is yes, 0 is no
("dplmc_store_troop_is_female",[
    (store_script_param_1, ":troop_no"),
    (try_begin),
        (eq, ":troop_no", active_npcs_including_player_begin),
        (assign, ":troop_no", "trp_player"),
    (try_end),
    (troop_get_type, reg0, ":troop_no"),
    (try_begin),
        (neq, reg0, tf_male),#man
        (neq, reg0, tf_boy),#boy
        (neq, reg0, tf_male_barbarian),#
        (neq, reg0, tf_male_black),#
        (neq, reg0, tf_male_eastern),#
        (neq, reg0, tf_male_north_african),#
        (assign, reg0, 1),
    (else_try),
        (assign, reg0, 0),
    (try_end),
]),

("dplmc_store_troop_is_female_reg",[
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":reg_no"),
    (troop_get_type, ":is_female", ":troop_no"),
    #The following will make it so, for example, tf_undead does not appear to be female.
    #Mods where this is relevant will likely want to tweak it, but this will work in at
    #least one that I know of that has non-human lords.
    (try_begin),
        (neq, ":is_female", tf_male),#man
        (neq, ":is_female", tf_boy),#boy
        (neq, ":is_female", tf_male_barbarian),#
        (neq, ":is_female", tf_male_black),#
        (neq, ":is_female", tf_male_eastern),#
        (neq, ":is_female", tf_male_north_african),#
        (assign, ":is_female", 1),
    (else_try),
        (assign, ":is_female", 0),
    (try_end),
        ##Can asign to registers 0,1,2,3, 65, or 4
    (try_begin),
        (eq, ":reg_no", 4),
        (assign, reg4, ":is_female"),
    (else_try),
        (eq, ":reg_no", 3),
        (assign, reg3, ":is_female"),
    (else_try),
        (eq, ":reg_no", 2),
        (assign, reg2, ":is_female"),
    (else_try),
        (eq, ":reg_no", 1),
        (assign, reg1, ":is_female"),
    (else_try),
        (eq, ":reg_no", 0),
        (assign, reg0, ":is_female"),
    (else_try),
        (eq, ":reg_no", 65),
        (assign, reg65, ":is_female"),
    (else_try),
        ##default to reg4
        (assign, reg4, ":reg_no"),
        (display_message, "@{!} ERROR: called script dplmc-store-troop-is-female-reg with bad argument {reg4}"),
        (assign, reg4, ":is_female"),
    (try_end),
]),

##script_dplmc_store_is_female_troop_1_troop_2
#
#This exists to make it easy to modify this to work with mods that redefine the troop types.
#See script_dplmc_store_troop_is_female
#
#INPUT:
#      arg1: troop_1
#      arg2: troop_2
#OUTPUT:
#       reg0: 0 for not female, 1 for female
#       reg1: 0 for not female, 1 for female
("dplmc_store_is_female_troop_1_troop_2",[
    (store_script_param_1, ":troop_1"),
    (store_script_param_2, ":troop_2"),
    (troop_get_type, ":is_female_1", ":troop_1"),
    (troop_get_type, ":is_female_2", ":troop_2"),
    #The following will make it so, for example, tf_undead does not appear to be female.
    #Mods where this is relevant will likely want to tweak it, but this will work in at
    #least one that I know of that has non-human lords.
    (try_begin),
        (neq, ":is_female_1", tf_male),
        (neq, ":is_female_1", tf_boy),
        (neq, ":is_female_1", tf_male_barbarian),#
        (neq, ":is_female_1", tf_male_black),#
        (neq, ":is_female_1", tf_male_eastern),#
        (neq, ":is_female_1", tf_male_north_african),#
        (assign, ":is_female_1", 1),
    (else_try),
        (assign, ":is_female_1", 0),
    (try_end),
    (try_begin),
        (neq, ":is_female_2", tf_male),
        (neq, ":is_female_2", tf_boy),
        (neq, ":is_female_2", tf_male_barbarian),#
        (neq, ":is_female_2", tf_male_black),#
        (neq, ":is_female_2", tf_male_eastern),#
        (neq, ":is_female_2", tf_male_north_african),#
        (assign, ":is_female_2", 1),
    (else_try),
        (assign, ":is_female_2", 0),
    (try_end),
    (assign, reg0, ":is_female_1"),
    (assign, reg1, ":is_female_2"),
]),

#script_dplmc_center_point_calc
# INPUT: arg1 = faction_id
#        arg2 = troop_1
#        arg2 = troop_2
#        arg3 = town_point_value (see explanation below)
#
# OUTPUT:
#        reg0 = total renown / total faction points (or 0 if no centers held)
#        reg1 = troop_1 total (not divided)
#        reg2 = troop_2 total (not divided)
#        reg3 = faction average lord renown (or 0 if no lords)
#
#In various places the game tallies center points differently.  The values of
#villages/castles/fiefs, respectively, in some places are 1/2/2, in other
#places are 1/2/3, and in others are 1/3/4.
#Specifying the town point value determines which scheme will be used to
#determine ceter points:
#        arg3 = 2 gives 1/2/2
#        arg3 = 3 gives 1/2/3
#        arg3 = 4 gives 1/2/4
#
#If the specified town_point_value is not 2,3, or 4, the script is allowed to
#clamp the value or substitute a default.
("dplmc_center_point_calc",[
    (store_script_param, ":faction_id", 1),
    (store_script_param, ":troop_1", 2),
    (store_script_param, ":troop_2", 3),
    (store_script_param, ":town_point_value", 4),

    (val_clamp, ":town_point_value", 2, 5),

    #The outputs
    (assign, ":faction_score", 0),
    (assign, ":troop_1_score", 0),
    (assign, ":troop_2_score", 0),
    #(assign, ":average_renown", 0),

    #Intermediate values we use for computing outputs
    (assign, ":total_renown", 0),
    (assign, ":num_lords", 0),

    #Handle the player first
    #(assign, ":player_in_faction", 0),
    (assign, ":faction_alias", ":faction_id"),
    (try_begin),
        (this_or_next|eq, ":faction_id", "$players_kingdom"),
            (eq, ":faction_id", "fac_player_supporters_faction"),
        (val_add, ":num_lords", 1),
        (troop_get_slot, ":total_renown", "trp_player", slot_troop_renown),
        #(assign, ":player_in_faction", 1),
        (assign, ":faction_alias", "fac_player_supporters_faction"),
        (eq, ":faction_id", "fac_player_supporters_faction"),
        (assign, ":faction_alias", "$players_kingdom"),
    (try_end),

    #Get lords in faction
    (try_for_range, ":troop_no", heroes_begin, heroes_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (this_or_next|eq, ":faction_no", ":faction_id"),
            (eq, ":faction_no", ":faction_alias"),

        (val_add, ":num_lords", 1),
        (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
        (val_max, ":renown", 0),
        (val_add, ":total_renown", ":renown"),
    (try_end),

    #Get stats for centers
    (try_for_parties, ":center_no"),
        (assign, ":points", 0),
        (try_begin),
            #Towns are 2, 3, or 4 points
            (this_or_next|is_between, ":center_no", towns_begin, towns_end),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":points", ":town_point_value"),
        (else_try),
            #Castles are always 2 points
            (this_or_next|is_between, ":center_no", castles_begin, castles_end),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (assign, ":points", 2),#castles are always 2
        (else_try),
            #Villages are always 1 point
            (this_or_next|is_between, ":center_no", villages_begin, villages_end),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (try_end),

        #Don't process parties that aren't centers.
        (ge, ":points", 1),

        #NB: We don't know for sure that troop_1 and troop_2 aren't the
        #same value, and we don't even necessarily know that they're part
        #of the specified faction.
        (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, ":troop_1"),
            (val_add, ":troop_1_score", ":points"),
        (try_end),

        (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, ":troop_2"),
            (val_add, ":troop_2_score", ":points"),
        (try_end),

        (store_faction_of_party, ":faction_no", ":center_no"),
        (this_or_next|eq, ":faction_no", ":faction_id"),
            (eq, ":faction_no", ":faction_alias"),
        (val_add, ":faction_score", ":points"),
    (try_end),

    # OUTPUT:
    #        reg0 = faction renown / faction points (or 0 if faction has no centers)
    #        reg1 = troop_1 total (not divided)
    #        reg2 = troop_2 total (not divided)
    #        reg3 = faction average lord renown (or 0 if no lords)
    (assign, reg0, 0),
    (try_begin),
        (neq, ":faction_score", 0),
        (store_div, reg0, ":total_renown", ":faction_score"),
    (try_end),
    (assign, reg1, ":troop_1_score"),
    (assign, reg2, ":troop_2_score"),
    (assign, reg3, 0),
    (try_begin),
        (neq, ":num_lords", 0),
        (store_div, reg0, ":total_renown", ":num_lords"),
    (try_end),
]),

#script_dplmc_good_produced_at_center_or_its_villages
# For towns, also includes the villages that attach to it
#
# INPUT: arg1 = good_no
#        arg2 = center_no
# OUTPUT:
#        reg0 = 0 if no, 1 if yes
("dplmc_good_produced_at_center_or_its_villages",[
	(store_script_param, ":good_no", 1),
	(store_script_param, ":center_no", 2),

	(assign, ":has_good", 0),
	(assign, ":save_reg1", reg1),
	(assign, ":save_reg2", reg2),
	# (store_current_hours, ":cur_hours"),
	# (store_sub, ":recent_time", ":cur_hours", 3 * 24),

	(try_begin),
		(is_between, ":good_no", trade_goods_begin, trade_goods_end),
		(ge, ":center_no", 1),
		(this_or_next|is_between, ":center_no", centers_begin, centers_end),
			(party_is_active, ":center_no"),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_castle),
		(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
			(is_between, ":center_no", centers_begin, centers_end),
		(call_script, "script_center_get_production", ":center_no", ":good_no"),
		(try_begin),
			#Positive production
			(ge, reg0, 1),
			(assign, ":has_good", 1),
		(else_try),
			#Is a town or a castle, and one of its villages has positive prodution
			(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(party_slot_eq, ":center_no", slot_party_type, spt_castle),
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(eq, ":has_good", 0),
				#is bound to center
				(this_or_next|party_slot_eq, ":cur_village", slot_village_market_town, ":center_no"),
                (party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),#for castles
               # (assign, reg0, 0),
               # (try_begin),
                  #If a trading party from the village reached the town recently, its goods are
				  #available.
                  # (party_slot_ge, ":cur_village", dplmc_slot_village_trade_last_arrived_to_market, ":recent_time"),
                  # (assign, reg0, 1),
               # (else_try),
                  #If the village is not looted and this center is not under siege, the
				  #goods from the village could be acquired if they were needed.
                (neg|party_slot_eq, ":cur_village", slot_village_state, svs_looted),
                (neg|party_slot_eq, ":cur_village", slot_village_state, svs_deserted),
                (neg|party_slot_eq, ":center_no", slot_village_state, svs_under_siege),
                    # (assign, reg0, 1),
                # (try_end),
                # (eq, reg0, 1),
				#If an eligible village has positive production, set "has_good" to true.
				(call_script, "script_center_get_production", ":cur_village", ":good_no"),
				(ge, reg0, 1),
				(assign, ":has_good", 1),
			(try_end),
		(try_end),
	(try_end),

	(assign, reg0, ":has_good"),
	(assign, reg1, ":save_reg1"),
	(assign, reg2, ":save_reg2"),
]),

#script_dplmc_assess_ability_to_purchase_good_from_center
# INPUT: arg1 = good_no
#        arg2 = center_no
# OUTPUT:
#        reg0 = actual price (may be theoretical if unavailable)
#        reg1 = 1 if available, 0 if unavailable
("dplmc_assess_ability_to_purchase_good_from_center",[
    (store_script_param, ":good_no", 1),
    (store_script_param, ":center_no", 2),

    #This is still quite experimental.  This is a work in progress
            #rather than a finished formula.
    (assign, ":price_factor", average_price_factor),
    (assign, ":has_good", 0),

    (try_begin),
        (is_between, ":center_no", centers_begin, centers_end),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
        (party_slot_eq, ":center_no", slot_party_type, spt_town),

        (is_between, ":good_no", trade_goods_begin, trade_goods_end),

        (store_sub, ":item_slot_no", ":good_no", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),

        (call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":center_no"),
        (assign, ":has_good", reg0),
        #abort if good is found
        (lt, ":has_good", 1),

        (store_faction_of_party, ":center_faction", ":center_no"),
        (faction_get_slot, ":mercantilism", ":center_faction", dplmc_slot_faction_mercantilism),
        (val_clamp, ":mercantilism", -3, 4),

        #For towns, check trade centers.
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
        (is_between, ":center_no", towns_begin, towns_end),

        # (store_current_hours, ":cur_hours"),
        (assign, ":best_foreign_price", maximum_price_factor),
        (assign, ":worst_price_seen", ":price_factor"),

        (try_for_range, ":trade_town_index", slot_town_trade_routes_begin, slot_town_trade_routes_end),
            (party_get_slot, ":trade_town", ":center_no", ":trade_town_index"),
            (is_between, ":trade_town", centers_begin, centers_end),

            (party_get_slot, ":price_factor_2", ":trade_town", ":item_slot_no"),
            (val_max, ":worst_price_seen", ":price_factor_2"),

            (party_slot_eq, ":trade_town", slot_party_type, spt_town),
            (call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":trade_town"),
            #The town has or produces the item
            (ge, reg0, 1),

            #Get the number of hours since the last caravan arrival, and set the penalty accordingly.
            # (assign, ":hours_since", 0),
            # #The slot storing the arrival time.  This may be uninitialized for old saved games used
            # #with this mod.
            # (store_sub, ":arrival_slot", ":trade_town_index", slot_town_trade_routes_begin),
            # (val_add, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin),
            # (try_begin),
                # #This condition can only occur if the number of trade route slots was increased
                # #but the number of trade arrival time slots was not.  Check just in case, to avoid
                # #strange errors.
                # (neg|is_between, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
                # #Set "hours-since" to one week.
                # (assign, ":hours_since", 7 * 24),
            # (else_try),
                # #If the slot is uninitialized, give it a random plausible value.
                # (party_slot_eq, ":center_no", ":arrival_slot", 0),#Uninitialzed memory!
                # (store_random_in_range, ":hours_since", 1, (24 * 7 * 5) + 1),#random time in last five weeks
                # (party_get_slot, ":prosperity_factor", ":center_no", slot_town_prosperity),
                # (val_clamp, ":prosperity_factor", 0, 101),
                # (val_add, ":prosperity_factor", 75),
                # (val_mul, ":hours_since", 125),
                # (val_div, ":hours_since", ":prosperity_factor"),#last arrival some time in the last five weeks, plus or minus up to 40% based on prosperity
                # (store_sub, ":last_arrival", ":cur_hours", ":hours_since"),
                # (party_set_slot, ":center_no", ":arrival_slot", ":last_arrival"),
            # (else_try),
                # (party_get_slot, ":last_arrival", ":center_no", ":arrival_slot"),
                # (store_sub, ":hours_since", ":cur_hours", ":last_arrival"),
                # (val_max, ":hours_since", 0),
            # (try_end),

            #Base penalty is 5%.  It stays at a flat 5% for the first week, then begins rising
            #at a rate of 5% per week afterwards (incremented continuously).
            #Clamp the maximum penalty at 50%.
            (assign, ":penalty", 5),
            (val_add, ":penalty", (24 * 7) // 2),
            (val_div, ":penalty", 24 * 7),
            (val_max, ":penalty", 5),#required for the first week
            (val_min, ":penalty", 50),#don't increase above 50%

            #Apply mercantilism
            (store_faction_of_party, ":other_faction", ":trade_town"),
            (try_begin),
                #Decrease penalty for mercantilism, increase for free trade
                (eq, ":other_faction", ":center_faction"),
                (val_sub, ":penalty", ":mercantilism"),
            (else_try),
                #Increase penalty for mercantilism, decrease for free trade
                (val_add, ":penalty", ":mercantilism"),
            (try_end),

            (try_begin),
                (ge, ":price_factor_2", average_price_factor),
                (val_mul, ":price_factor_2", ":penalty"),
                (val_add, ":price_factor_2", 50),
                (val_div, ":price_factor_2", 100),
            (else_try),
                (store_add, reg0, 100, ":penalty"),
                (val_mul, reg0, average_price_factor),
                (val_add, reg0, 50),
                (val_div, reg0, 100),
                (val_add, ":price_factor_2", reg0),
            (try_end),
            #Make use of the source
            (assign, ":has_good", 1),
            (val_min, ":best_foreign_price", ":price_factor_2"),
        (try_end),
        (try_begin),
            (ge, ":has_good", 1),
            (val_max, ":price_factor", ":best_foreign_price"),
        (else_try),
            #Make it so that lack of supply will not make the price lower
            (lt, ":has_good", 1),
            (val_max, ":price_factor", ":worst_price_seen"),
        (try_end),
    (try_end),

    (try_begin),
        (lt, ":has_good", 1),
        (val_max, ":price_factor", average_price_factor),#don't give bargains if there is no supply
        (val_mul, ":price_factor", 8),#sixty percent penalty
        (val_div, ":price_factor", 5),
    (try_end),

    #Apply constraints at the last step
    (val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor),

    (assign, reg0, ":price_factor"),
    (assign, reg1, ":has_good"),
]),

# script_dplmc_get_faction_truce_length_with_faction
# INPUT
#   arg1:  faction_1
#   arg2:  faction_2
# OUTPUT
#   reg0:  The length in days of faction_1's truce with faction_2, if any.
#          If no truce exists, the appropriate value to return is zero.
("dplmc_get_faction_truce_length_with_faction",[
    (store_script_param, ":faction_1", 1),
    (store_script_param, ":faction_2", 2),

    (assign, ":truce_length", 0),

    (try_begin),
        (is_between, ":faction_1", kingdoms_begin, kingdoms_end),
        (is_between, ":faction_2", kingdoms_begin, kingdoms_end),
        (neq, ":faction_1", ":faction_2"),
        (store_add, ":truce_slot", ":faction_2", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        (faction_get_slot, ":truce_length", ":faction_1", ":truce_slot"),
    (try_end),
    (assign, reg0, ":truce_length"),
]),

#script_dplmc_get_terrain_code_for_battle
#
# Gets the terrain code for a battle between two parties, which
# is usually a value like rt_desert, but can instead be two
# special values: -1 for
#
# INPUT: arg1 = attacker_party
#        arg2 = defender_party
# OUTPUT: reg0 = terrain code (-1 for invalid, -2 for siege)
("dplmc_get_terrain_code_for_battle",[
    (store_script_param, ":attacker_party", 1),
    (store_script_param, ":defender_party", 2),

    (assign, reg0, dplmc_terrain_code_unknown), #Terrain code, defined in header_terrain_types.py

    (try_begin),
        #Check for village missions
        (this_or_next|eq, ":attacker_party", "p_main_party"),
        (eq, ":defender_party", "p_main_party"),
        (ge, "$g_encounter_is_in_village", 1),
        (assign, reg0, dplmc_terrain_code_village),#defined in header_terrain_types.py
    (else_try),
        #If the attacker party is a town, a castle, a village, a bandit lair, or a ship,
        #set the terrain code to "none" since we don't have any specific ideas for modifying
        #the unit-type performance in scenarios of that type (whatever they are).
        (ge, ":attacker_party", 0),
        (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
        (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_castle),
        (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_village),
        (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_bandit_lair),
        (party_slot_eq, ":attacker_party", slot_party_type, spt_ship),#no modifier for being attacked by a ship
        (assign, reg0, dplmc_terrain_code_unknown),#no terrain options, defined in header_terrain_types.py
    (else_try),
        #If the attacker party is *attached* to a town/castle/village, a bandit lair, or a ship,
        #set the terrain code to "none" since we don't have any specific ideas for modifying
        #the unit-type performance in scenarios of that type (whatever they are).
        (ge, ":attacker_party", 0),
        (party_get_attached_to, ":attachment", ":attacker_party"),
        (ge, ":attachment", 0),
        (party_is_active, ":attachment"),
        (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
        (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_castle),
        (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_village),
        (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
        (party_slot_eq, ":attachment", slot_party_type, spt_ship),#no modifier for being attacked by a ship
        (assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
    (else_try),
        #If the attacker party isn't a weird type, the terrain is entirely based on the
        #defender (unless the defender is invalid).
        (ge, ":defender_party", 0),
        (try_begin),
        #If the defender is a walled center, use siege mode.
            (this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_town),
            (party_slot_eq, ":defender_party", slot_party_type, spt_castle),
            (assign, reg0, dplmc_terrain_code_siege),#siege mode, defined in header_terrain_types.py
        (else_try),
             #If the defender is a village
            (party_slot_eq, ":defender_party", slot_party_type, spt_village),
            (assign, reg0, dplmc_terrain_code_village),
        (else_try),
			#If the defender is a bandit lair or a ship, use no terrain modifier.
            (this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_bandit_lair),
            (party_slot_eq, ":defender_party", slot_party_type, spt_ship),
            (assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
        (else_try),
            #If the defender is attached, do the same checks but for the attachment.
            (party_get_attached_to, ":attachment", ":defender_party"),
            (ge, ":attachment", 0),
            (party_is_active, ":attachment"),
            (assign, ":attachment_value", -100),
            (try_begin),
                #Walled centers use siege modifiers
                (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),
                (party_slot_eq, ":attachment", slot_party_type, spt_castle),
                (assign, ":attachment_value", dplmc_terrain_code_siege),
            (else_try),
                #Villages
                (party_slot_eq, ":attachment", slot_party_type, spt_village),
                (assign, ":attachment_value", dplmc_terrain_code_village),
            (else_try),
                #bandit-lairs and ships have no modifiers currently
                (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
                (party_slot_eq, ":attachment", slot_party_type, spt_ship),
                (assign, ":attachment_value", dplmc_terrain_code_unknown),#no terrain modifiers
            (try_end),
            #If neither of the above apply, fall through to the next condition.
            (neq, ":attachment_value", -100),
            (assign, reg0, ":attachment_value"),
        (else_try),
                #Use the terrain under the defender.
                #In the future I might want to change this so there's a tactics contest
                #between the attacker and defender to choose the more favorable ground
                #from their immediate surroundings.  I would also have to change the actual
                #terrain-type code.
            (party_get_current_terrain, reg0, ":defender_party"),
        (try_end),
    (else_try),
    #If we get here, it means the defender was invalid, so use the terrain under
    #the attacker.
        (ge, ":attacker_party", 0),
        (party_get_current_terrain, reg0, ":attacker_party"),#terrain under attacker
    (try_end),
]),

#script_dplmc_party_calculate_strength_in_terrain
# INPUT: arg1 = party_id
#        arg2 = terrain (from header_terrain_types.py)
#        arg3 = exclude leader (0 for do-not-exclude, 1 for exclude)
#        arg4 = cache policy (1 is use terrain, 2 is use non-terrain, 0 is do not use)
# OUTPUT: reg0 = strength with terrain
#         reg1 = strength ignoring terrain
("dplmc_party_calculate_strength_in_terrain",[
    (store_script_param, ":party", 1), #Party_id
    (store_script_param, ":terrain_type", 2),#a value from header_terrain_types.py
    (store_script_param, ":exclude_leader", 3),#(0 for do-not-exclude, 1 for exclude)
    (store_script_param, ":cache_policy", 4),#1 is use terrain, 2 is use non-terrain, 0 is do not use)

    (assign, ":total_strength_terrain", 0),
    (assign, ":total_strength_no_terrain", 0),

    (party_get_num_companion_stacks, ":num_stacks", ":party"),
    (assign, ":first_stack", 0),
    (try_begin),
        (neq, ":exclude_leader", 0),
        (assign, ":first_stack", 1),
    (try_end),
	  #Bonus for heroes on top of the rest
	  (assign, ":hero_percent", 110),
	  ##Moved setting the multipliers out of the loop...
	  (assign, ":guaranteed_horse_percent", 100),
	  (assign, ":guaranteed_ranged_percent", 100),
	  (assign, ":guaranteed_neither_percent", 100),
	  #First, test for some special codes:
	  (try_begin),
	      (eq, ":terrain_type", dplmc_terrain_code_none),#Apply no modifiers
		    (assign, ":hero_percent", 100),
	  (else_try),
	  	  (eq, ":terrain_type", dplmc_terrain_code_village),#A dismounted fight at a village (apply hero modifier, nothing else)
    (else_try),
        (eq, ":terrain_type", dplmc_terrain_code_siege),#A siege battle, not including sorties.
        (assign, ":guaranteed_ranged_percent", 120),
	  (else_try),
        (eq, ":terrain_type", rt_steppe),
		    (assign, ":guaranteed_horse_percent", 125),
	  (else_try),
        (this_or_next|eq, ":terrain_type", rt_snow),
        (this_or_next|eq, ":terrain_type", rt_desert),
			  (eq, ":terrain_type", rt_plain),
		    (assign, ":guaranteed_horse_percent", 110),
    (else_try),
	      (eq, ":terrain_type", rt_steppe_forest),
        (assign, ":guaranteed_horse_percent", 115),
    (else_try),
        (this_or_next|eq, ":terrain_type", rt_forest),
        (this_or_next|eq, ":terrain_type", rt_mountain_forest),
        (eq, ":terrain_type", rt_snow_forest),
		    (assign, ":guaranteed_neither_percent", 110),
	  (try_end),

    (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
        (store_character_level, ":stack_strength", ":stack_troop"),
        (val_add, ":stack_strength", 4),
        (val_mul, ":stack_strength", ":stack_strength"),
        (val_mul, ":stack_strength", 2),
        (assign, ":terrain_free_strength", ":stack_strength"),
        (try_begin),
            (assign, ":hero_horse", 0),#added for heroes (any positive number = has a horse)
            (try_begin),
                (this_or_next|eq, "trp_player", ":stack_troop"),
                (troop_is_hero, ":stack_troop"),
                (gt, ":guaranteed_horse_percent", ":hero_percent"),#don't bother if we wouldn't use the result
                (neg|troop_is_guarantee_horse, ":stack_troop"),#don't bother if we already know the troop has a horse
                (store_skill_level, reg0, "skl_riding", ":stack_troop"),
                (ge, reg0, 2),#don't bother if the troop has no/minimal riding skill
                #Just checking ek_horse may not work for non-companions, so check the inventory
                (troop_get_inventory_capacity, ":inv_cap", ":stack_troop"),
                (ge, ":inv_cap", 1),
                (val_min, ":inv_cap", dplmc_ek_alt_items_begin + 8),#Don't check too much of the inventory
                (try_for_range, ":inv_slot", 0, ":inv_cap"),
                    (troop_inventory_slot_get_item_amount, reg1, ":stack_troop", ":inv_slot"),
                    (ge, reg1, 1),#quantity must be greater than zero
                    (troop_get_inventory_slot, reg0, ":stack_troop", ":inv_slot"),
                    (ge, reg0, 1),#must be a valid item
                    (item_get_type, reg1, reg0),#check if the item is a horse
                    (eq, reg1, itp_type_horse),
                    (assign, ":inv_cap", ":inv_slot"),#break loop
                (try_end),
            #If no horse found, set to zero
                (neg|is_between, ":hero_horse", horses_begin, horses_end),
                (assign, ":hero_horse", 0),
            (try_end),
            (assign, ":stack_strength_multiplier", 100),#<-- percent multiplier
            (try_begin),#Mounted troops
                (this_or_next|ge, ":hero_horse", 1),
                (troop_is_guarantee_horse, ":stack_troop"),
                (assign, ":stack_strength_multiplier", ":guaranteed_horse_percent"),
            (else_try),#horse archer
                (troop_is_guarantee_ranged, ":stack_troop"),
                (troop_is_guarantee_horse, ":stack_troop"),
                (store_add, ":stack_strength_multiplier", ":guaranteed_horse_percent", 10),
            (else_try),#Ranged troops
                (troop_is_guarantee_ranged, ":stack_troop"),
                (assign, ":stack_strength_multiplier", ":guaranteed_ranged_percent"),
            (else_try),#Infantry
                (assign, ":stack_strength_multiplier", ":guaranteed_neither_percent"),
            (try_end),

            #Use hero/player modifiers if a better one didn't apply
            (try_begin),
                (this_or_next|eq, ":stack_troop", "trp_player"),
                (troop_is_hero, ":stack_troop"),
                (val_max, ":stack_strength_multiplier", ":hero_percent"),#hero bonus
            (try_end),

            (val_mul, ":stack_strength", ":stack_strength_multiplier"),
            (val_add, ":stack_strength", 50),#add this before division for correct rounding
            (val_div, ":stack_strength", 100),
            ##AotE terrain advantages
        (try_end),
        #moved the next two lines here from above
        (val_div, ":stack_strength", 100),#<- moved here from above
        (val_max, ":stack_strength", 1), #new (patch 1.125) #<- moved here from above
        (val_div, ":terrain_free_strength", 100),
        (val_max, ":terrain_free_strength", 1),
        (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size",":party",":i_stack"),
            (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
            (val_sub, ":stack_size", ":num_wounded"),
            (val_mul, ":stack_strength", ":stack_size"),
            (val_mul, ":terrain_free_strength", ":stack_size"),
        (else_try),
            (troop_is_wounded, ":stack_troop"), #hero & wounded
            (assign, ":stack_strength", 0),
            (assign, ":terrain_free_strength", 0),
        (try_end),
        (val_add, ":total_strength_terrain", ":stack_strength"),
        (val_add, ":total_strength_no_terrain", ":terrain_free_strength"),
    (try_end),
	  #Load results into registers and cache if appropriate
	  (assign, reg0, ":total_strength_terrain"),
	  (assign, reg1, ":total_strength_no_terrain"),
    (try_begin),
        (eq, ":cache_policy", 1),
        (party_set_slot, ":party", slot_party_cached_strength, reg0),
    (else_try),
        (eq, ":cache_policy", 2),
        (party_set_slot, ":party", slot_party_cached_strength, reg1),
    (try_end),
]),

#script_dplmc_player_can_give_troops_to_troop  (Warning, clobbers {s11}!)
#
# INPUT: arg1 = troop_id
# OUTPUT: reg0 = 1 or more is yes, 0 or less is no
#
# This script does not take into account things like whether the troop
# is a prisoner of a party, so it can be used for checking whether troops
# can be added to a garrison.
#
# The general logic is that you can give troops to a member of your
# own faction if any of the following are true:
#   - You are the faction leader or marshall
#   - You are the spouse of the faction leader, and the faction
#     leader is not on bad terms with you
#   - The troop is an affiliated family member
#   - The troop is your spouse, and is either pliable or not on bad terms
#   - The troop is a former companion with whom you are on good terms
#   - The troop is related to you by marriage and you are on good terms
#
# For allied factions, the conditions are similar to the above.
# However, being the marshall or leader of your own faction does not
# guarantee cooperation from lords who dislike you.
#
# For non-allied other factions, the check for faction leader or
# marshall are not relevant, and the faction must not be at war
# with the player's faction.
("dplmc_player_can_give_troops_to_troop",[
	(store_script_param, ":troop_id", 1), #Party_id
	(assign, ":can_give_troops", 0),
	(assign, ":save_reg1", reg1),

	(try_begin),
		(this_or_next|eq, ":troop_id", "trp_kingdom_heroes_including_player_begin"),
		(eq, ":troop_id", "trp_player"),
		(assign, ":can_give_troops", 1),
	(else_try),
		(lt, ":troop_id", 1),
		(assign, ":can_give_troops", 0),
	(else_try),
		(store_faction_of_troop, ":troop_faction", ":troop_id"),

		(call_script, "script_troop_get_player_relation", ":troop_id"),
		(assign, ":troop_relation", reg0),
		(troop_get_slot, ":troop_reputation", ":troop_id", slot_lord_reputation_type),

		(try_begin),
			#Troop is member of player supporters faction
			(eq, ":troop_faction", "fac_player_supporters_faction"),
			##Always yes in Native, but if centralization is negative allow non-compliance
			(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
			(try_begin),
				(ge, reg0, 0),
				(assign, reg0, -200),
			(else_try),
				(val_mul, reg0, -10),
				(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
			(try_end),
			(gt, ":troop_relation", reg0),
			(assign, ":can_give_troops", 1),
		(else_try),
			#Troop is a member of the same faction as the player
			(eq, ":troop_faction", "$players_kingdom"),
			(faction_get_slot, ":troop_faction_leader", ":troop_faction", slot_faction_leader),
			(try_begin),
				#Leader or marshall
				(this_or_next|eq, ":troop_faction_leader", "trp_player"),
					(faction_slot_eq, ":troop_faction", slot_faction_marshall, "trp_player"),
				#If centralization is negative allow non-compliance
				(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
				(try_begin),
					(ge, reg0, 0),
					(assign, reg0, -200),
				(else_try),
					(val_mul, reg0, -10),
					(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
				(try_end),
				(gt, ":troop_relation", reg0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of leader
				(gt, ":troop_faction_leader", 1),
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_faction_leader", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_faction_leader"),
				(call_script, "script_troop_get_player_relation", ":troop_faction_leader"),
				(ge, reg0, 0),
				#If centralization is negative allow non-compliance
				(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
				(try_begin),
					(ge, reg0, 0),
					(assign, reg0, -200),
				(else_try),
					(val_mul, reg0, -10),
					(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
				(try_end),
				(gt, ":troop_relation", reg0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(is_between, ":troop_id", companions_begin, companions_end),
				#	(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(else_try),
			#Troop is member of a faction allied with the player's
			(call_script, "script_dplmc_get_faction_truce_length_with_faction", "$players_kingdom", ":troop_faction"),
			(gt, reg0, dplmc_treaty_defense_days_expire),
			(faction_get_slot, ":player_faction_leader", "$players_kingdom", slot_faction_leader),
			(try_begin),
				#Leader or marshall
				(this_or_next|eq, ":player_faction_leader", "trp_player"),
					(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
				(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of leader
				(gt, ":player_faction_leader", 1),
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":player_faction_leader", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":player_faction_leader"),
				(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
				(call_script, "script_troop_get_player_relation", ":player_faction_leader"),
				(ge, reg0, 0),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(is_between, ":troop_id", companions_begin, companions_end),
					#(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(else_try),
			#Troop is a member of a faction that isn't hostile to the player's
			(store_relation, reg0, ":troop_faction", "fac_player_faction"),
			(ge, reg0, 0),
			(store_relation, reg0, ":troop_faction", "$players_kingdom"),
			(ge, reg0, 0),
			(try_begin),
				#Spouse of troop
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
				(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|ge, ":troop_relation", 0),
				(this_or_next|eq, ":troop_reputation", lrep_conventional),
				(this_or_next|eq, ":troop_reputation", lrep_moralist),
					(eq, ":troop_reputation", lrep_otherworldly),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Affiliated family member
				(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
				(ge, reg0, 1),
				(assign, ":can_give_troops", 1),
			(else_try),
				#Close companion previously under arms
				(is_between, ":troop_id", companions_begin, companions_end),
					#(is_between, ":troop_id", pretenders_begin, pretenders_end),
				(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(else_try),
				#In-law (or hypothetically a blood relative) who is close with the player
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
				(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
				(ge, ":troop_relation", 14),
				(this_or_next|ge, reg0, 10),
					(ge, ":troop_relation", 20),
				(assign, ":can_give_troops", 1),
			(try_end),
		(try_end),
	(try_end),

	(assign, reg1, ":save_reg1"),
	(assign, reg0, ":can_give_troops"),
]),

#"script_dplmc_distribute_gold_to_lord_and_holdings"
#
#Related to script_dplmc_remove_gold_from_lord_and_holdings, divides the gold
#between the lord and his fortresses in a semi-intelligent way.
#
#INPUT:
#   arg1: the amount of gold
#   arg2: the lord's ID
("dplmc_distribute_gold_to_lord_and_holdings",[
	(store_script_param_1, ":gold_left"),
	(store_script_param_2, ":lord_no"),

	(try_begin),
		(lt, ":lord_no", 0),#Invalid ID
	(else_try),
		#If the number is negative, handle this using script_dplmc_remove_gold_from_lord_and_holdings
		(lt, ":gold_left", 0),
		(val_mul, ":gold_left", -1),
		(call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":gold_left", ":lord_no"),
		(assign, ":gold_left", 0),
	(else_try),
		(neq, ":lord_no", "trp_player"),
		(neg|troop_is_hero, ":lord_no"),#Not hero or player
        (troop_add_gold, ":lord_no", ":gold_left"),
        (assign, ":gold_left", 0),
	(else_try),
		#The player doesn't use center wealth to pay garrison wages, so just
		#give it directly.
		(eq, ":lord_no", "trp_player"),
		(troop_add_gold, "trp_player", ":gold_left"),
		(assign, ":gold_left", 0),
	(else_try),
		(neg|troop_is_hero, ":lord_no"),#If the lord isn't the player, and isn't a hero, do nothing
	(else_try),
		(troop_get_slot, ":lord_gold", ":lord_no", slot_troop_wealth),
		(val_max, ":lord_gold", 0),
		(val_add, ":lord_gold", ":gold_left"),
        (troop_set_slot, ":lord_no", slot_troop_money_to_center, 0),
        (try_begin),##if lord has enough gold he will gift it to towns
            (gt, ":lord_gold", 75000),
            (assign, ":total_difference", 0),
            # (display_message, "@Add gold to town"),
            (assign, ":limit_to_donate", 50000),
            # (try_begin),
                # (this_or_next|troop_slot_ge, ":lord_no", slot_troop_legion, 1),
                # (troop_slot_ge, ":lord_no", slot_troop_aux, 1),
                # (assign, ":limit_to_donate", 50000),
            # (try_end),
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                (gt, ":lord_gold", ":limit_to_donate"),
                (party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
                (party_get_slot, ":town_gold", ":center_no", slot_town_wealth),
                (try_begin),
                    (party_slot_eq, ":center_no", slot_party_type, spt_town),
                    (store_sub,":difference", 20000, ":town_gold"),
                (else_try),
                    (store_sub,":difference", 10000, ":town_gold"),
                (try_end),
                (gt, ":difference", 0),
                (val_clamp, ":difference", 1, 1001),
                (val_add, ":town_gold", ":difference"),
                (val_add, ":total_difference", ":difference"),
                (party_set_slot, ":center_no", slot_town_wealth, ":town_gold"),
                (val_sub, ":lord_gold", ":difference"),
                # (str_store_troop_name, s22, ":lord_no"),
                # (str_store_party_name, s23, ":center_no"),
                # (assign, reg19, ":difference"),
                # (display_message, "@{s22} added {reg19} denarii to {s23}"),
            (try_end),
            (troop_set_slot, ":lord_no", slot_troop_money_to_center, ":total_difference"),
        (try_end),
		(troop_set_slot, ":lord_no", slot_troop_wealth, ":lord_gold"),
	(try_end),
]),

#"script_dplmc_remove_gold_from_lord_and_holdings"
#INPUT:
#   arg1: the amount of money to remove (greater than zero)
#   arg2: the ID of the lord spending the money
#OUTPUT:
#   None
("dplmc_remove_gold_from_lord_and_holdings",[
    (store_script_param_1, ":gold_cost"),
	(store_script_param_2, ":lord_no"),

	(try_begin),
		(lt, ":lord_no", 0),#Invalid ID
	(else_try),
		(neq, ":lord_no", "trp_player"),
		(neg|troop_is_hero, ":lord_no"),#Not player or hero
	(else_try),
		#If the number is negative, give gold instead of taking it.
		#Handle this using script_dplmc_distribute_gold_to_lord_and_holdings
		(lt, ":gold_cost", 0),
		(val_mul, ":gold_cost", -1),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_cost", ":lord_no"),
		(assign, ":gold_cost", 0),
	(else_try),
		#For the player, first subtract the gold from his treasury (if any).
		(eq, ":lord_no", "trp_player"),
        (store_troop_gold, ":treasury", "trp_household_possessions"),
		(try_begin),
            (ge, ":treasury", 1),
            (val_min, ":treasury", ":gold_cost"),
            (call_script, "script_dplmc_withdraw_from_treasury", ":treasury"),
            (val_sub, ":gold_cost", ":treasury"),
		(try_end),
		(store_troop_gold, ":treasury", "trp_player"),
		(try_begin),
			(ge, ":treasury", 1),
			(val_min, ":treasury", ":gold_cost"),
			(troop_remove_gold, "trp_player", ":treasury"),
			(val_sub, ":gold_cost", ":treasury"),
		(try_end),
		#Fall through to the next section if the treasury didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove the gold directly from the lord's wealth slot
		(ge, ":gold_cost", 1),
		(ge, ":lord_no", 1),#not the player
		(troop_get_slot, ":treasure", ":lord_no", slot_troop_wealth),
		(ge, ":treasure", 1),
		(try_begin),
			(ge, ":treasure", ":gold_cost"),
			(val_sub, ":treasure", ":gold_cost"),
			(assign, ":gold_cost", 0),
		(else_try),
			(val_sub, ":gold_cost", ":treasure"),
			(assign, ":treasure", 0),
		(try_end),
		(troop_set_slot, ":lord_no", slot_troop_wealth, ":treasure"),
		#Fall through to the next section if his personal wealth didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove remaining gold from uncollected taxes.
		#We iterate backwards in order to remove from villages before castles and towns.
		(ge, ":gold_cost", 1),
		(try_for_range_backwards, ":center_no", centers_begin, centers_end),
			(ge, ":gold_cost", 1),
			(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
			(party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
			(try_begin),
                (gt, ":accumulated_rents", 0),
				(ge, ":accumulated_rents", ":gold_cost"),
				(val_sub, ":accumulated_rents", ":gold_cost"),
				(assign, ":gold_cost", 0),
			(else_try),
                (gt, ":accumulated_rents", 0),
				(val_sub, ":gold_cost", ":accumulated_rents"),
				(assign, ":accumulated_rents", 0),
			(try_end),
            (val_max, ":accumulated_rents", 0),#to be on the save side
            (party_set_slot, ":center_no", slot_center_accumulated_rents, ":accumulated_rents"),
            (ge, ":gold_cost", 1),
			(party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
			(try_begin),
                (gt, ":accumulated_tariffs", 0),
				(ge, ":accumulated_tariffs", ":gold_cost"),
				(val_sub, ":accumulated_tariffs", ":gold_cost"),
				(assign, ":gold_cost", 0),
			(else_try),
                (gt, ":accumulated_tariffs", 0),
				(val_sub, ":gold_cost", ":accumulated_tariffs"),
				(assign, ":accumulated_tariffs", 0),
			(try_end),
            (val_max, ":accumulated_tariffs", 0),#to be on the save side
            (party_set_slot, ":center_no", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
		(try_end),
		#Fall through to the next section if the uncollected taxes didn't cover it.
		(lt, ":gold_cost", 1),
	(else_try),
		#Remove remaining gold from center wealth.  We iterate backwards to remove from
		#castles before towns.
		(ge, ":gold_cost", 1),
		(try_for_range_backwards, ":center_no", centers_begin, centers_end),
			(ge, ":gold_cost", 1),
			(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
			(party_get_slot, ":treasure", ":center_no", slot_town_wealth),
            (ge, ":treasure", 1),
            (try_begin),
                (ge, ":treasure", ":gold_cost"),
                (val_sub, ":treasure", ":gold_cost"),
                (assign, ":gold_cost", 0),
            (else_try),
                (val_sub, ":gold_cost", ":treasure"),
                (assign, ":treasure", 0),
            (try_end),
			(party_set_slot, ":center_no", slot_town_wealth, ":treasure"),
		(try_end),
		(lt, ":gold_cost", 1),
	(else_try),
	    #Try to remove the gold from the hero himself
		(store_troop_gold, ":treasure", ":lord_no"),
		(gt, ":treasure", 0),
		(try_begin),
			(ge, ":treasure", ":gold_cost"),
			(troop_remove_gold, ":lord_no", ":gold_cost"),
			(assign, ":gold_cost", 0),
		(try_end),
	(try_end),
]),

# "script_dplmc_prepare_hero_center_points_ignoring_center"
#
# Input: arg1 = target_center
("dplmc_prepare_hero_center_points_ignoring_center",[
    (store_script_param, ":target_center", 1),

    (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
    (troop_set_slot, "trp_player", dplmc_slot_troop_temp_slot, 0),

    (try_for_range, ":troop_no", heroes_begin, heroes_end),
        (troop_set_slot, ":troop_no", slot_troop_temp_slot, 0),
        (troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, 0),
    (try_end),

    (try_for_range, ":center_no", centers_begin, centers_end),
        #Skip "target center"
      (neq, ":center_no", ":target_center"),

      #Lord is player or a hero
      (party_get_slot, ":troop_no", ":center_no", slot_town_lord),
      (this_or_next|eq, ":troop_no", "trp_player"),
        (is_between, ":troop_no", heroes_begin, heroes_end),

      #Update lord point total
      (assign, ":center_points", 1),
      (try_begin),
        (party_slot_eq, ":center_no", slot_party_type, spt_town),
        (assign, ":center_points", 3),
      (else_try),
        (party_slot_eq, ":center_no", slot_party_type, spt_castle),
        (assign, ":center_points", 2),
      (try_end),

      (troop_get_slot, ":slot_value", ":troop_no", slot_troop_temp_slot),
      (val_add, ":slot_value", ":center_points"),
      (troop_set_slot, ":troop_no", slot_troop_temp_slot, ":slot_value"),

      #Update distance from closest owned center to target
      (is_between, ":target_center", centers_begin, centers_end),
      (troop_get_slot, ":slot_value", ":troop_no", dplmc_slot_troop_temp_slot),
      (store_distance_to_party_from_party, ":cur_distance", ":target_center", ":center_no"),
      (val_max, ":cur_distance", 1),
      (try_begin),
        (eq, ":slot_value", 0),
        (assign, ":slot_value", ":cur_distance"),
      (try_end),
      (val_min, ":slot_value", ":cur_distance"),
      (troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, ":slot_value"),
    (try_end),
	  ##Update cached totals
	  (try_for_range, ":troop_no", heroes_begin, heroes_end),
      (troop_get_slot, reg0, ":troop_no", slot_troop_temp_slot),
      (val_add, reg0, 1),
      (troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
    (try_end),
    (troop_get_slot, reg0, "trp_player", slot_troop_temp_slot),
    (val_add, reg0, 1),
    (troop_set_slot, "trp_player", dplmc_slot_troop_center_points_plus_one, reg0),
    #Since the target center was omitted from the point totals, handle it here
	  (try_begin),
      (is_between, ":target_center", centers_begin, centers_end),
      (party_get_slot, ":troop_no", ":target_center", slot_town_lord),
      #Only perform this update for a troop whose center point value was updated above
      (this_or_next|is_between, ":troop_no", heroes_begin, heroes_end),
      (eq, ":troop_no", "trp_player"),
      (troop_get_slot, reg0, ":troop_no", dplmc_slot_troop_center_points_plus_one),
      (val_add, reg0, 1),#1 point for villages
      (try_begin),
         (is_between, ":target_center", walled_centers_begin, walled_centers_end),
         (val_add, reg0, 1),#2 points for castles
         (is_between, ":target_center", towns_begin, towns_end),
         (val_add, reg0, 1),#3 points for towns
      (try_end),
      (troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
	  (try_end),
   ]),

  # script_dplmc_calculate_troop_score_for_center_aux
  #  Similar to script_calculate_troop_score_for_center
  #
  # slot_troop_temp_slot must already be loaded with center points;
  # dplmc_slot_troop_temp_slot must already be loaded with distance.
  #
  # Input: arg1 = evaluator
  #        arg2 = troop_no
  #        arg3 = center_no
  # Output: reg0 = score
  #         reg1 = explanation string
  ("dplmc_calculate_troop_score_for_center_aux",
   [(store_script_param, ":troop_1", 1),
    (store_script_param, ":troop_2", 2),
	 (store_script_param, ":center_no", 3),

	 (assign, ":explanation", "str_political_explanation_most_deserving_in_faction"),
	 (assign, ":explanation_priority", -1),

   (try_begin),
      (lt, ":troop_1", 0),
      (assign, ":relation", 0),
      (assign, ":reputation", lrep_none),
   (else_try),
      (eq, ":troop_1", ":troop_2"),
      (assign, ":relation", 50),
	   (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
   (else_try),
      (call_script, "script_troop_get_relation_with_troop", ":troop_1", ":troop_2"),
      (assign, ":relation", reg0),
      (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
   (try_end),
   (val_clamp, ":relation", -100, 101),

   (troop_get_slot, reg0, ":troop_2", slot_troop_renown),
   (val_max, reg0, 0),
   (store_add, ":score", 500, reg0),
	(troop_get_slot, ":num_center_points", ":troop_2", slot_troop_temp_slot),
	(val_max, ":num_center_points", 0),
	(val_add, ":num_center_points", 1),

	#Subtract distance from closest other fief owned, except when
	#considering the lord's original holdings.
	(try_begin),
	  (troop_slot_ge, ":troop_2", slot_troop_temp_slot, 1),
	  (neg|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
	  (neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2"),

	  (troop_get_slot, reg0, ":troop_2", dplmc_slot_troop_temp_slot),
	  (gt, reg0, 1),
	  (val_min, reg0, 250),#upper cap on distance effect (bear in mind that this is subtracted from 500 + troop renown)
	  (val_sub, ":score", reg0),
	(try_end),

   #(store_random_in_range, ":random", 50, 100),
   #(val_mul, ":score", ":random"),
	(val_mul, ":score", 75),
   (val_div, ":score", ":num_center_points"),

	(assign, ":fiefless_bonus_used", 0),
	(try_begin),
	   #Bonus for lords with no other fiefs when a village is being considered.
      (lt, ":num_center_points", 2),
	  (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (neq, ":reputation", lrep_debauched),
      (neq, ":reputation", lrep_selfrighteous),
      (neq, ":reputation", lrep_quarrelsome),
		(val_mul, ":score", 2),
		(try_begin),
		  (lt, ":explanation_priority", 100),
		  (assign, ":explanation_priority", 100),
		  (assign, ":explanation", "str_political_explanation_lord_lacks_center"),
		(try_end),
	 (assign, ":fiefless_bonus_used", 1),#because it has already been applied
	(try_end),

	(assign, ":troop_2_slot_alias", ":troop_2"),
	(try_begin),
		(eq, ":troop_2", "trp_player"),
		(assign, ":troop_2_slot_alias", "trp_kingdom_heroes_including_player_begin"),
	(try_end),

   (try_begin),
	#Bonus for conquerer
		(neq, ":reputation", lrep_debauched),
		(this_or_next|neq, ":reputation", lrep_selfrighteous),
		   (eq, ":troop_1", ":troop_2"),
		(neq, ":reputation", lrep_cunning),
	  (neg|party_slot_eq, ":center_no", slot_party_type, spt_village),
      (party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":troop_2_slot_alias"),
	  (try_begin),
		 (lt, ":num_center_points", 2),
		 (eq, ":fiefless_bonus_used", 0),
		 (assign, reg1, 50),#50% increase
	  (else_try),
	     (this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
		 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
		 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
			(eq, ":reputation", lrep_martial),
		 (assign, reg1, 50),#50% increase
	  (else_try),
		 (assign, reg1, 25),#25% increase
	  (try_end),
	  (store_add, reg0, 100, reg1),
	  (val_mul, ":score", reg0),
	  (val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
		  (assign, ":explanation", "str_political_explanation_lord_took_center"),
 		(try_end),
	(else_try),
	#Bonus for original owner
		(gt, ":troop_2", 0),
		(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
		(try_begin),
			(lt, ":num_center_points", 2),
			(eq, ":fiefless_bonus_used", 0),
			(assign, reg1, 50),#50% increase
		(else_try),
			(this_or_next|eq, ":troop_2", ":troop_1"),
			(this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
				(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
			(assign, reg1, 50),#50% increase
		(else_try),
			(assign, reg1, 25),#25% increase
		(try_end),
		(store_add, reg0, 100, reg1),
		(val_mul, ":score", reg0),
		(val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Bonus for previous owner, lord
		(gt, ":troop_2", 0),
		(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
		(try_begin),
			(lt, ":num_center_points", 2),
			(eq, ":fiefless_bonus_used", 0),
			(assign, reg1, 50),#50% increase
		(else_try),
		(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
			(assign, reg1, 50),
		(else_try),
			(assign, reg1, 25),#25% increase
		(try_end),
		(store_add, reg0, 100, reg1),
		(val_mul, ":score", reg0),
		(val_div, ":score", 100),
		(try_begin),
		  (ge, reg1, ":explanation_priority"),
		  (assign, ":explanation_priority", reg1),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Bonus for lord claiming the center as home
		(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
		(val_mul, ":score", 5),
		(val_div, ":score", 4),
		(try_begin),
		  (ge, 25, ":explanation_priority"),
		  (assign, ":explanation_priority", 25),
        (assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
 		(try_end),
	(else_try),
	#Aesthetic penalty (doesn't apply when there was a bonus)
	#To try to make the late game less mixed, have a preference towards
	#assigning lords to their own faction types.
		(troop_get_slot, reg0, ":troop_2", slot_troop_original_faction),
		(party_get_slot, reg1, ":center_no", slot_center_original_faction),
		(neq, reg0, reg1),
	#These extra checks are to avoid penalizing the player or promoted companions
	#unintentionally.
		(is_between, reg0, npc_kingdoms_begin, npc_kingdoms_end),
		(is_between, reg1, npc_kingdoms_begin, npc_kingdoms_end),
		#Take 95% of score
		(val_mul, ":score", 19),
		(val_add, ":score", 10),
		(val_div, ":score", 20),
   (try_end),

	#add 2 x relation (minus controversy) to score
   (troop_get_slot, ":controversy", ":troop_2", slot_troop_controversy),
   (val_clamp, ":controversy", 0, 101),
	(store_mul, ":relation_mod", ":relation", 2),
	(val_sub, ":relation_mod", ":controversy"),
	#this modifier will not raise the score by more than 50%
	(store_add, reg0, ":score", 1),
	(val_div, reg0, 2),
	(val_max, reg0, 1),
	(val_min, ":relation_mod", reg0),

	(store_mul, reg0, ":score", 100),#rego has pre-relationship modified score
	(val_add, ":score", ":relation_mod"),
	(val_div, reg0, ":score"),
	(store_sub, reg1, ":score", 100),#reg1 has percentage change (i.e. 1.5 times becomes 50% change) from relation/controversy

	(try_begin),
		(ge, reg1, 0),
		(ge, reg1, ":explanation_priority"),
		  (ge, ":relation", 15),
		(assign, ":explanation_priority", reg1),
		  (assign, ":explanation", "str_political_explanation_most_deserving_friend"),
	(try_end),

   (assign, reg0, ":score"),
	(assign, reg1, ":explanation"),
   ]),

  #Adapted "auto-sell" from rubik's Custom Commander
  #auto sell credit rubik (CC) begin:
  #
  # script_dplmc_auto_sell
  # INPUTS:
  #    arg1 :customer (the one selling the stuff)
  #    arg2 :merchant (the one buying the stuff)
  #    arg3 :auto_sell_price_limit (only sell stuff less expensive than this)
  #    arg4 :valid_items_begin (use this to only sell a limited range of things)
  #    arg5 :valid_items_end   (use this to only sell a limited range of things)
  #    arg6 :actually_sell_items (set to 0 for a "dry run"; set to 2 to print a descriptive message)
  #
  # OUTPUTS:
  #    reg0 amount of gold gained by customer (not actually gained if this was a dry run)
  #    reg1 number of items sold by customer (not actually sold if this was a dry run)
  ("dplmc_auto_sell", [
	#This script has various changes from the CC version.
	#In particular, all parameters other than "customer" and "merchant",
	#and reporting the number of items & gold change.
	(store_script_param, ":customer", 1),
	(store_script_param, ":merchant", 2),
	#dplmc+ start added parameters
	(store_script_param, ":auto_sell_price_limit", 3),
	(store_script_param, ":valid_items_begin", 4),
	(store_script_param, ":valid_items_end", 5),
	(store_script_param, ":actually_sell_items", 6),
	#dplmc+ end added parameters

	#dplmc+ added section begin
	(assign, ":save_reg2", reg2),
	(assign, ":save_reg3", reg3),
	(assign, ":save_reg65", reg65),
	(assign, ":save_talk_troop", "$g_talk_troop"),
	#The talk troop is used for price information, but it's possible for this to be called
	#from other contexts (like a menu).
	(assign, "$g_talk_troop", ":merchant"),

	(assign, ":gold_gained", 0),
	(assign, ":items_sold", 0),
	#(assign, ":most_expensive_sold_item", -1),
	#(assign, ":most_expensive_sold_imod", -1),
	#(assign, ":most_expensive_sold_price", -1),
	#dplmc+ added section end

    (store_free_inventory_capacity, ":space", ":merchant"),
    (troop_get_inventory_capacity, ":inv_cap", ":customer"),
	(set_show_messages, 0),#<-dplmc+ added
	(store_troop_gold, ":m_gold", ":merchant"),#dplmc+: to support "dry runs", move this out of the loop
    (try_for_range_backwards, ":i_slot", dplmc_ek_alt_items_end, ":inv_cap"),#we're reserving several "safe" slots in the beginning of the inventory
        (troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
        (troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
        (gt, ":item", -1),
        (item_get_type, ":type", ":item"),
        (item_slot_eq, ":type", dplmc_slot_item_type_not_for_sell, 0),
        #dplmc+ begin added constraints
        (is_between, ":item", ":valid_items_begin", ":valid_items_end"),
        (neg|is_between, ":type", books_begin, books_end),
        (this_or_next|neg|is_between, ":type", food_begin, food_end),
            (eq, ":imod", imod_rotten),
        (neg|is_between, ":type", trade_goods_begin, trade_goods_end),
        (neq, ":imod", imod_lordly),#dplmc+: never sell "lordly" items
        #dplmc+ end added constraints

        (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
        (assign, ":score", reg0),
        (val_div, ":score", 100),
        (call_script, "script_game_get_item_sell_price_factor", ":item"),
        (assign, ":sell_price_factor", reg0),
        (val_mul, ":score", ":sell_price_factor"),
        (val_div, ":score", 100),
        (val_max, ":score",1),

        #dplmc+ start changed section
        (le, ":score", ":auto_sell_price_limit"),
        (le, ":score", ":m_gold"),
        (gt, ":space", 0),

        #For equipment, in general don't sell the item unless you have a better one,
        #or the item is useless to you.  (The idea is to stop from accidentally
        #selling the player's own equipment.)
        (item_get_type, ":this_item_type", ":item"),

        #Normally, we would do the following:

        #(try_begin),
        #   (item_slot_eq, ":item", dplmc_slot_two_handed_one_handed, 1),
        #	 (assign, ":this_item_type", 11), # type 11 = two-handed/one-handed
        #(try_end),

        #However, we are delaying that step until later, because type 11 is the
        #same as itp_type_goods.

        #Don't sell items if there's a reasonable chance that they might
        #be the player's alternate personal equipment.  It goes without saying
        #that items the player can't use aren't counted.
        #
        #(Items the player has equipped will not even be considered for sale,
        #but it is common for players to have a variety of items they use in
        #different circumstances, which might not all be equipped.)
        #
        #For melee weapons: don't sell the best weapon or the second-best of a type
        #   (it might be a backup, or there might be a variety of weapons of
        #   the same type in situational use)
        #For shields: don't sell the best or second-best shield
        #For thrown weapons: don't sell the best three thrown weapons
        #For ammunition: don't sell the best three of the ammunition kind (arrows,
        #   bolts) unless you lack a weapon that uses the ammunition.
        #For armor: don't sell the best armor of a kind.
        #For horses: don't sell the best or second-best horse
        #For bows and crossbows: don't sell the best item of a kind (all bows are
        #   very similar, so there's little chance someone would carry an alternate)
        #For muskets and pistols: don't sell the best or second-best weapon of
        #   a kind.

        (assign, ":can_sell", 1),

        (try_begin),
            #Ammunition type: arrows (if you have a bow you can use, don't sell the best 3 arrow packs you have)
            (eq, ":this_item_type", itp_type_arrows),
            (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_bow, ":customer"),
            (try_begin),
                (ge, reg0, 0),
                (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
                (lt, reg0, 3),#must not be best (0), second-best (1), or third-best (2)
                (assign, ":can_sell", 0),
            (try_end),
        (else_try),
            #Ammunition type: bolts (if you have a crossbow you can use, don't sell the best 3 bolt packs you have)
            (eq, ":this_item_type", itp_type_bolts),
            (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_crossbow, ":customer"),
            (try_begin),
                (ge, reg0, 0),
                (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
                (lt, reg0, 3),#must not be best (0), second-best (1), or third-best (2)
                (assign, ":can_sell", 0),
            (try_end),
        (else_try),
            #Ammunition type: bullets (if you have a pistol or musket you can use, don't sell the best 3 bullet packs you have)
            (eq, ":this_item_type", itp_type_bullets),
            #Do muskets and pistols both use bullets?  I'll assume so.
            (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_musket, ":customer"),
            (assign, reg1, reg0),
            (call_script, "script_dplmc_scan_for_best_item_of_type", ":customer", itp_type_pistol, ":customer"),
            (try_begin),
                (this_or_next|ge, reg0, 0),
                    (ge, reg1, 0),
                (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
                (lt, reg0, 3),
                (assign, ":can_sell", 0),
            (try_end),
        (else_try),
            #Catch: all non-usable equipment
            (is_between, ":this_item_type", itp_type_horse, itp_type_musket + 1),
            (neq, ":this_item_type", itp_type_goods),
            (call_script, "script_dplmc_troop_can_use_item", ":customer", ":item", ":imod"),
            (eq, reg0, 0),#Past here, we don't have to check for usability
        (else_try),
            #Thrown weapons: don't sell best 3 you can use
            (eq, ":this_item_type", itp_type_thrown),
            (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
            (store_sub, ":can_sell", reg0, 2),#must not be best (0) or second-best (1) or third-best (2)
        (else_try),
            #Types where both the best and the second-best aren't sold
            #Horses, shields, melee weapons, and firearms
            (this_or_next|is_between, ":this_item_type", itp_type_horse, itp_type_polearm + 1),
            (this_or_next|eq, ":this_item_type", itp_type_shield),
            (this_or_next|eq, ":this_item_type", itp_type_pistol),
                (eq, ":this_item_type", itp_type_musket),
            (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
            (store_sub, ":can_sell", reg0, 1),#must not be best (0) or second best (1)
        (else_try),
            #Types where the best isn't sold (armor, not including shields)
            (is_between, ":this_item_type", itp_type_head_armor, itp_type_hand_armor + 1),
            (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
            (assign, ":can_sell", reg0),#must not be best (0)
        (try_end),

        #(try_begin),
        #   (lt, ":can_sell", 1),
        #	 (gt, "$cheat_mode", 0),
        #	 (call_script, "script_dplmc_count_better_items_of_same_type", ":customer", ":item", ":imod", ":customer"),
        #	 (assign, reg1, ":i_slot"),
        #	 (str_store_item_name, s0, ":item"),
        #	 (display_message, "@{!} DEBUG - Will not sell item {s0} at slot {reg1}.  Better items of same kind: {reg0}"),
        #(try_end),

        (ge, ":can_sell", 1),

        #(try_begin),
        #	(ge, ":score", ":most_expensive_sold_price"),
        #	(assign, ":most_expensive_sold_item", ":item"),
        #	(assign, ":most_expensive_sold_imod", ":imod"),
        #	(assign, ":most_expensive_sold_price", ":score"),
        #(try_end),

        #Log the transaction even if in dry run mode
        (val_sub, ":m_gold", ":score"),
        (val_add, ":gold_gained", ":score"),
        (val_add, ":items_sold", 1),
        (val_sub, ":space", 1),

        #If not a dry run, apply the transaction
        (neq, ":actually_sell_items", 0),
        (troop_add_item, ":merchant", ":item", ":imod"),
        (troop_set_inventory_slot, ":customer", ":i_slot", -1),
        (troop_remove_gold, ":merchant", ":score"),
        (troop_add_gold, ":customer", ":score"),
        #dplmc+ end changed section
    (try_end),

	(set_show_messages, 1),#<- dplmc+ added

	#dplmc+ added section begin
	#Print a message if appropriate
	(try_begin),
		(is_between, ":actually_sell_items", 2, 4),#2 or 3
		(this_or_next|ge, ":items_sold", 1),
			(eq, ":actually_sell_items", 3),
		(assign, reg0, ":gold_gained"),
		(assign, reg1, ":items_sold"),
		(store_sub, reg3, reg1, 1),
		(str_store_troop_name, s0, ":merchant"),
		(try_begin),
			(this_or_next|is_between, ":merchant", quick_battle_troops_begin, quick_battle_troops_end),
			(this_or_next|is_between, ":merchant", heroes_begin, heroes_end),
			(this_or_next|is_between, ":merchant", dplmc_employees_begin, dplmc_employees_end),
			(is_between, ":merchant", walkers_end, tournament_champions_end),
			(display_message, "@You sold {reg1} {reg3?items:item} to {s0} and gained {reg0} {reg3?denarii:denarius}."),
		(else_try),
			(display_message, "@You sold {reg1} {reg3?items:item} to the {s0} and gained {reg0} {reg3?denarii:denarius}."),
		(try_end),
	(try_end),

	#Revert variables
	(assign, reg2, ":save_reg2"),
	(assign, reg3, ":save_reg3"),
	(assign, reg65, ":save_reg65"),
	(assign, "$g_talk_troop", ":save_talk_troop"),

	#Return diagnostics
	(assign, reg0, ":gold_gained"),
	(assign, reg1, ":items_sold"),
	#dplmc+ added section end
]),
#auto sell credit rubik (CC) end

##For use with autosell
#Input: center_no
#Output: none
("dplmc_player_auto_sell_at_center", [
    (store_script_param, ":center_no", 1),
    (assign, ":save_reg0", reg0),
    (assign, ":save_reg1", reg1),
    (try_begin),
	    ##For Towns:
		(is_between, ":center_no", towns_begin, towns_end),
		(try_begin),
			#1. Selling weapons, shields, and ranged weapons to the weaponsmith
		    (party_get_slot, ":merchant_troop", ":center_no", slot_town_weaponsmith),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", weapons_begin, ranged_weapons_end, 2),
		(try_end),
		(try_begin),
			#2. Selling armor to the armorer
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_armorer),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", armors_begin, armors_end, 2),
 		(try_end),
		(try_begin),
			#3. Selling horses to the horse merchant
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_horse_merchant),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", horses_begin, horses_end, 2),
		(try_end),
		(try_begin),
			#4. Selling whatever may remain to the general merchant
			(party_get_slot, ":merchant_troop", ":center_no", slot_town_merchant),
			(ge, ":merchant_troop", 1),
			(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", all_items_begin, all_items_end, 2),
		(try_end),
    (else_try),
		##For Villages:
		(is_between, ":center_no", villages_begin, villages_end),
		(party_get_slot, ":merchant_troop", ":center_no", slot_town_elder),
		(ge, ":merchant_troop", 1),
		(call_script, "script_dplmc_auto_sell", "trp_player", ":merchant_troop", "$g_dplmc_auto_sell_price_limit", all_items_begin, all_items_end, 2),
    (else_try),
	    ##Error
		(assign, reg0, ":center_no"),
		(display_message, "@{!} ERROR FOR AUTOSELL for town ID {reg0}: Bad town or merchant was missing"),
    (try_end),
    (assign, reg0, ":save_reg0"),
    (assign, reg1, ":save_reg1"),
]),

##Adapted Auto-Buy-Food from rubik's Custom Commander
#Changed to parameterize merchant and customer, but did not finish expanding
#the script to work with non-player arguments.  (There is currently no need,
#but I can imagine using it for NPCs sent on item-purchasing missions, or if
#NPC parties had to buy food.)
#
##OLD: Overwrites: reg1, reg2, reg3, reg4
##NEW: Overwrite reg0
#
#INPUT:
#      arg1 :customer
#      arg2 :merchant_troop
("dplmc_auto_buy_food", [
    (store_script_param, ":customer", 1),
    (store_script_param, ":merchant_troop", 2),
    (store_script_param, ":ignore_limits", 3),
    (store_script_param, ":troop_paying", 4),
    ##added section begin, preserve registers
    (assign, ":save_reg1", reg1),
    (assign, ":save_reg2", reg2),
    (assign, ":save_reg3", reg3),
    (assign, ":save_reg4", reg4),
    ##added section end

    (store_troop_gold, ":begin_gold", ":troop_paying"),
    (store_free_inventory_capacity, ":begin_space", ":customer"),
    (troop_get_inventory_capacity, ":inv_cap", ":merchant_troop"),
    (set_show_messages, 0),
    (try_for_range, ":i_slot", 10, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":merchant_troop", ":i_slot"),
        (gt, ":item", -1),
        (is_between, ":item", food_begin, food_end),
        (troop_inventory_slot_get_item_amount, ":amount", ":merchant_troop", ":i_slot"),
        ##dplmc+: The next line required making a change to header_operations.py
        (troop_inventory_slot_get_item_max_amount, ":max_amount", ":merchant_troop", ":i_slot"),
        (eq, ":amount", ":max_amount"),

        (item_get_slot, ":food_portion", ":item", dplmc_slot_item_food_portion),
        (val_max, ":food_portion", 0),#dplmc+ added
        (store_item_kind_count, ":food_count", ":item", ":customer"),

        (this_or_next|lt, ":food_count", ":food_portion"),
        (eq, ":ignore_limits", 1),

        (store_free_inventory_capacity, ":free_inv_cap", ":customer"),
        (gt, ":free_inv_cap", 0),

        (call_script, "script_game_get_item_buy_price_factor", ":item"),
        (assign, ":buy_price_factor", reg0),
        (store_item_value,":score",":item"),
        (val_mul, ":score", ":buy_price_factor"),
        (val_div, ":score", 100),
        (val_max, ":score",1),
        (store_troop_gold, ":customer_gold", ":troop_paying"),
        (ge, ":customer_gold", ":score"),

        (troop_add_item, ":customer", ":item"),
        (troop_set_inventory_slot, ":merchant_troop", ":i_slot", -1),
        (troop_remove_gold, ":troop_paying", ":score"),
        (troop_add_gold, ":merchant_troop", ":score"),
    (try_end),
    (set_show_messages, 1),
    (store_troop_gold, ":end_gold", ":troop_paying"),
    (store_free_inventory_capacity, ":end_space", ":customer"),
    (try_begin),
        (neq, ":end_gold", ":begin_gold"),
        (store_sub, reg1, ":begin_gold", ":end_gold"),
        (store_sub, reg2, ":begin_space", ":end_space"),
        (store_sub, reg3, reg1, 1),
        (store_sub, reg4, reg2, 1),
        (this_or_next|eq, ":customer", "trp_player"),
        (eq, ":customer", "trp_follower_party_mules"),
        (display_message, "@You have bought {reg2} {reg4?kinds:kind} of food and lost {reg1} {reg3?denarii:denarius}."),
    (try_end),

    # sell rotten food
    (store_troop_gold, ":begin_gold", ":troop_paying"),
    (store_free_inventory_capacity, ":begin_space", ":customer"),
    (troop_get_inventory_capacity, ":inv_cap", ":customer"),
    (set_show_messages, 0),
    (try_for_range, ":i_slot", 10, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
        (gt, ":item", -1),
        (is_between, ":item", food_begin, food_end),
        (troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
        (eq, ":imod", imod_rotten),
        (store_free_inventory_capacity, ":free_inv_cap", ":merchant_troop"),
        (gt, ":free_inv_cap", 0),

        (call_script, "script_dplmc_get_item_value_with_imod", ":item", ":imod"),
        (assign, ":score", reg0),
        (val_div, ":score", 100),
        (call_script, "script_game_get_item_sell_price_factor", ":item"),
        (assign, ":sell_price_factor", reg0),
        (val_mul, ":score", ":sell_price_factor"),
        (troop_inventory_slot_get_item_amount, ":amount", ":customer", ":i_slot"),
        (troop_inventory_slot_get_item_max_amount, ":max_amount", ":customer", ":i_slot"),
        (val_mul, ":score", ":amount"),
        (val_div, ":score", ":max_amount"),
        (val_div, ":score", 100),
        (val_max, ":score",1),
        (store_troop_gold, ":merchant_gold", ":merchant_troop"),
        (ge, ":merchant_gold", ":score"),

        #(troop_add_item, ":merchant_troop", ":item", ":imod"),
        (troop_set_inventory_slot, ":customer", ":i_slot", -1),
        (troop_remove_gold, ":merchant_troop", ":score"),
        (troop_add_gold, ":troop_paying", ":score"),
    (try_end),
    (set_show_messages, 1),
    (store_troop_gold, ":end_gold", ":troop_paying"),
    (store_free_inventory_capacity, ":end_space", ":customer"),
    (try_begin),
        (neq, ":end_gold", ":begin_gold"),
        (store_sub, reg1, ":end_gold", ":begin_gold"),
        (store_sub, reg2, ":end_space", ":begin_space"),
        (store_sub, reg3, reg1, 1),
        (store_sub, reg4, reg2, 1),
        (this_or_next|eq, ":customer", "trp_player"),
        (eq, ":customer", "trp_follower_party_mules"),
        (display_message, "@You sold {reg2} {reg4?kinds:kind} of rotten food and gained {reg1} {reg3?denarii:denarius}."),
    (try_end),
    ##added section begin, preserve registers
    (assign, reg1, ":save_reg1"),
    (assign, reg2, ":save_reg2"),
    (assign, reg3, ":save_reg3"),
    (assign, reg4, ":save_reg4"),
    ##added section end
]),

##Auto-Buy-Food from rubik's Custom Commander end

# script_dplmc_get_trade_penalty
#
#This is similar to the old script_get_trade_penalty,
#except it uses parameters instead of relying on global variables.
#
# Input:
# param1: item_kind_id
# param2: market center
# param3: customer troop (-1 for a non-troop-specific answer, -2 to notify the script that this is being used to evaluate a gift)
# param4: merchant troop (-1 for a non-troop-specific answer)
# Output: reg0
("dplmc_get_trade_penalty",[
    #Additions begin:
    (store_script_param, ":item_kind_id", 1),
    (store_script_param, ":market_center", 2),
    (store_script_param, ":customer_troop", 3),
    (store_script_param, ":merchant_troop", 4),
    #End Additions
    (assign, ":penalty",0),

    ##Change this to support alternative customers
    ##(party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
    (try_begin),
        #Player: use skill of player party
        (eq, ":customer_troop", "trp_player"),
        (party_get_skill_level, ":trade_skill", "p_main_party", "skl_trade"),
    (else_try),
        #Hero leading a party: use skill of led party
        (gt, ":customer_troop", -1),
        (troop_is_hero, ":customer_troop"),
        (troop_get_slot, ":customer_party", ":customer_troop", slot_troop_leaded_party),
        (gt, ":customer_party", 0),
        (party_is_active, ":customer_party"),
        (party_get_skill_level, ":trade_skill", ":customer_party", "skl_trade"),
    (else_try),
        #Troop: use troop skill
        (gt, ":customer_troop", -1),
        (store_skill_level, ":trade_skill", "skl_trade", ":customer_troop"),
    (else_try),
        (assign, ":trade_skill", 0),
    (try_end),
    ##End Change
    (try_begin),
        (this_or_next|is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (eq, ":item_kind_id", "itm_temple_gold"),
        (assign, ":penalty",15), #reduced slightly
        (store_mul, ":skill_bonus", ":trade_skill", 1),
        (val_sub, ":penalty", ":skill_bonus"),
    (else_try),
        (assign, ":penalty", 100),
        (store_mul, ":skill_bonus", ":trade_skill", 5),
        (val_sub, ":penalty", ":skill_bonus"),
    (try_end),

    (assign, ":penalty_multiplier", average_price_factor),#<-- replaced 1000 with average_price_factor
    ##       # Apply penalty if player is hostile to merchants faction
    ##      (store_relation, ":merchants_reln", "fac_merchants", "fac_player_supporters_faction"),
    ##      (try_begin),
    ##        (lt, ":merchants_reln", 0),
    ##        (store_sub, ":merchants_reln_dif", 10, ":merchants_reln"),
    ##        (store_mul, ":merchants_relation_penalty", ":merchants_reln_dif", 20),
    ##        (val_add, ":penalty_multiplier", ":merchants_relation_penalty"),
    ##      (try_end),

    # Apply penalty if player is on bad terms with the town
    (try_begin),
        (eq, ":customer_troop", "trp_player"),#added
        (is_between, ":market_center", centers_begin, centers_end),#changed $g_encountered_party to :market_center
        (party_get_slot, ":center_relation", ":market_center", slot_center_player_relation),#changed $g_encountered_party to :market_center
        (store_mul, ":center_relation_penalty", ":center_relation", -3),
        (val_add, ":penalty_multiplier", ":center_relation_penalty"),
        (try_begin),
            (lt, ":center_relation", 0),
            (store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
            (val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
            (val_div, ":penalty_multiplier", 100),
        (try_end),
    (try_end),

    # Apply penalty if player is on bad terms with the merchant (not currently used)
    ##Begin Change
    #(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    #(assign, ":troop_reln", reg0),
    (try_begin),
        (this_or_next|eq, ":merchant_troop", "trp_player"),
        (eq, ":customer_troop", "trp_player"),
        (gt, ":merchant_troop", -1),
        (gt, ":customer_troop", -1),
        (call_script, "script_troop_get_player_relation", ":merchant_troop"),
        (assign, ":troop_reln", reg0),
    (else_try),
        (is_between, ":merchant_troop", heroes_begin, heroes_end),
        (is_between, ":customer_troop", heroes_begin, heroes_end),
        (call_script, "script_troop_get_relation_with_troop", ":merchant_troop", ":customer_troop"),
        (assign, ":troop_reln", reg0),
    (else_try),
        (assign, ":troop_reln", 0),
    (try_end),
    ##End Change
    #(troop_get_slot, ":troop_reln", "$g_talk_troop", slot_troop_player_relation),
    (try_begin),
        (lt, ":troop_reln", 0),
        (store_sub, ":troop_reln_dif", 0, ":troop_reln"),
        (store_mul, ":troop_relation_penalty", ":troop_reln_dif", 20),
        (val_add, ":penalty_multiplier", ":troop_relation_penalty"),
    (try_end),
    (try_begin),
        ##Begin Change
        #(is_between, "$g_encountered_party", villages_begin, villages_end),
        (is_between, ":market_center", centers_begin, centers_end),
        (party_slot_eq, ":market_center", slot_party_type, spt_village),
        ##End Change
        (val_mul, ":penalty", 2),
    (try_end),
    (try_begin),
        (is_between, ":market_center", centers_begin, centers_end),

	    (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
	  	(this_or_next|eq, ":customer_troop", -2),
        (neg|is_between, ":item_kind_id", food_begin, food_end), # Do not apply this to food
        (assign, ":save_reg1", reg1),
        (assign, ":save_reg2", reg2),

	    (call_script, "script_center_get_production", ":market_center", ":item_kind_id"),
	    (eq, reg0, 0),
	    (call_script, "script_center_get_consumption", ":market_center", ":item_kind_id"),
	    (eq, reg0, 0),
        (val_mul, ":penalty", 2),

        (assign, reg1, ":save_reg1"),
        (assign, reg2, ":save_reg2"),
    (try_end),
    (val_mul, ":penalty", ":penalty_multiplier"),
    ##Begin Change
    (val_add, ":penalty", average_price_factor // 2),#round in the correct direction (we don't need to worry about penalty < 0)
    (val_div, ":penalty", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
    ##End Change
    (val_max, ":penalty", 1),
    (assign, reg0, ":penalty"),
]),

##"script_dplmc_print_cultural_word_to_sreg"
##INPUTS:
#  arg1  - speaker troop
#  arg2  - which word/phrase to retrieve (arbitrary code)
#  arg3  - string register
#OUTPUTS:
#  writes result to string register
("dplmc_print_cultural_word_to_sreg", [
    (store_script_param, ":speaker", 1),
    (store_script_param, ":context", 2),
    (store_script_param, ":string_register", 3),
    #Right now this is entirely faction-based, but you could give different
    #results for individual lords.
    #(Note: Now certain parts of it do vary for heroes, to mimic the behavior in Native
    #feast dialogs for the word for wine.)
    (assign, ":speaker_faction", -1),
    (assign, ":culture", -1),
    (try_begin),
        (troop_is_hero, ":speaker"),
        (troop_get_slot, ":troop_culture", ":speaker", slot_troop_culture),
        (is_between, ":troop_culture", cultures_begin, cultures_end),
        (assign, ":culture", ":troop_culture"),
    (else_try),
        (eq, ":culture", -1),
        (try_begin),
            #Player faction
            (this_or_next|eq, ":speaker", "trp_player"),
            (eq, ":speaker", "trp_kingdom_heroes_including_player_begin"),
            (assign, ":speaker_faction", "fac_player_supporters_faction"),#<- This will potentially get translated later
        (else_try),
            #Hero original faction
            (is_between, ":speaker", heroes_begin, heroes_end),
            (troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
        (else_try),
            #Hero original faction
            (gt, ":speaker", -1),
            (troop_is_hero, ":speaker"),
            (troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_begin),
            (neg|troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_end),
            (troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
        (else_try),
            #Troop current faction
            (gt, ":speaker", -1),
            (store_troop_faction, ":speaker_faction", ":speaker"),
        (try_end),

        (try_begin),
            (lt, ":speaker", 1),
        (else_try),
            ##Only continue if the current faction isn't associated with a distinctive culture
            (lt, ":speaker_faction", dplmc_non_generic_factions_begin),
            ##This will work unless the order of the first factions gets changed
        (else_try),
            #Translate raiders into the equivalent kingdoms
            (is_between, ":speaker", bandits_begin, bandits_end),
            (try_begin),
                (eq, ":speaker", "trp_judean_rebel"),#Mountain bandits
                (assign, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
            (else_try),
                (eq, ":speaker", "trp_hispanic_rebell"),#Forest bandits
                (assign, ":speaker_faction", "fac_kingdom_1"),#Swadian
            (else_try),
                (eq, ":speaker", "trp_sea_raider"),#Sea raiders
                (assign, ":speaker_faction", "fac_kingdom_4"),#Nords
            (else_try),
                (eq, ":speaker", "trp_alannic_raider"),#Steppe bandits
                (assign, ":speaker_faction", "fac_kingdom_3"),#Khergits
            (else_try),
                (eq, ":speaker", "trp_illyrian_rebell"),#Taiga bandits
                (assign, ":speaker_faction", "fac_kingdom_2"),#Vaegir
            (else_try),
                (eq, ":speaker", "trp_desert_bandit"),#Desert bandits
                (assign, ":speaker_faction", "fac_kingdom_6"),#Sarranid
            (try_end),
            (ge, ":speaker_faction", dplmc_non_generic_factions_begin),
        (else_try),
            #For companions without default initial cultures, infer one from their home.
            #(Actually, don't limit this to companions, since there's a chance that others
            #could have a valid home slot.)
            #(is_between, ":speaker", companions_begin, companions_end),
            #(is_between, ":speaker", heroes_begin, heroes_end),
            (troop_is_hero, ":speaker"),
            (troop_get_slot, ":home_center", ":speaker", slot_troop_home),
            (is_between, ":home_center", centers_begin, centers_end),
            (party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
        (else_try),
            #For villagers, merchants, etc.
            (eq, ":speaker", "$g_talk_troop"),
            (neg|is_between, ":speaker", heroes_begin, heroes_end),#Not a character that might have an explicitly-set faction
            (neg|is_between, ":speaker", training_ground_trainers_begin, tavern_minstrels_end),#Not a trainer, ransom broker, traveler, bookseller, or minstrel
            (ge, "$g_encountered_party", 0),
            (try_begin),
                #For towns / castles / villages, use the original faction
                (is_between, "$g_encountered_party", centers_begin, centers_end),
                (party_get_slot, ":speaker_faction", "$g_encountered_party", slot_center_original_faction),
            (else_try),
                #Use faction of encountered party
                (party_is_active, "$g_encountered_party"),
                (store_faction_of_party, ":speaker_faction", "$g_encountered_party"),
                #For generic factions, use the closest center
                (lt, ":speaker_faction", dplmc_non_generic_factions_begin),
                (assign, ":speaker_faction", reg0),#save register
                (call_script, "script_get_closest_center", "$g_encountered_party"),
                (assign, ":home_center", reg0),
                (assign, reg0, ":speaker_faction"),#revert register
                (party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
            (try_end),
        (try_end),
        (faction_get_slot, ":culture", ":speaker_faction", slot_faction_culture),
    (try_end),
    (try_begin),
        (neg|is_between, ":culture", cultures_begin, cultures_end),
        (assign, ":culture", "fac_culture_roman"),
        (display_message, "@INVALID CULTURE IN script_dplmc_print_cultural_word_to_sreg."),
    (try_end),
    (call_script, "script_print_culture_word", ":string_register", ":culture", ":context"),
]),

("print_culture_word",[
    (store_script_param, ":string_register", 1),
    (store_script_param, ":culture", 2),
    (store_script_param, ":context", 3),
    #Store variant
    (try_begin),
        #Iconic cultural weapon that can be used metonymously for force of arms.
        #Native equivalent is "sword".
        #Non-Warband example: "He who lives by the {sword}, dies by the {sword}."
        #Example usage: "My {sword} is at the disposal of my liege."
        (eq, ":context", DPLMC_CULTURAL_TERM_WEAPON),
        (try_begin),
            (this_or_next|eq, ":culture", "fac_culture_germanic"),#Nords
            (this_or_next|eq, ":culture", "fac_culture_celtic"),#Vaegirs
            (this_or_next|eq, ":culture", "fac_culture_caledonian"),#Vaegirs
            (eq, ":culture", "fac_culture_dacian"),#Vaegirs
            (str_store_string, ":string_register", "@axe"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),
            (this_or_next|eq, ":culture", "fac_culture_parthian"),
            (this_or_next|eq, ":culture", "fac_culture_greek"),
            (eq, ":culture", "fac_culture_judean"),
            (str_store_string, ":string_register", "@spear"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_egyptian"),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergits
            (str_store_string, ":string_register", "@bow"),
        (else_try),
            #Default: Swadia, Sarranid, others
            (str_store_string, ":string_register", "@gladius"),
        (try_end),
    (else_try),
        #Plural version of iconic cultural weapon that can be used metonymously for force of arms.
        #Native equivalent is "swords".
        (eq, ":context", DPLMC_CULTURAL_TERM_WEAPON_PLURAL),
        (try_begin),
            (this_or_next|eq, ":culture", "fac_culture_germanic"),#Nords
            (this_or_next|eq, ":culture", "fac_culture_dacian"),#Nords
            (this_or_next|eq, ":culture", "fac_culture_caledonian"),#Nords
            (eq, ":culture", "fac_culture_celtic"),#Vaegirs
            (str_store_string, ":string_register", "@axes"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Rhodoks
            (this_or_next|eq, ":culture", "fac_culture_judean"),#Rhodoks
            (this_or_next|eq, ":culture", "fac_culture_greek"),#Rhodoks
            (eq, ":culture", "fac_culture_parthian"),#Rhodoks
            (str_store_string, ":string_register", "@spears"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_egyptian"),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergits
            (str_store_string, ":string_register", "@bows"),
        (else_try),
            #Default: Swadia, Sarranid, others
            (str_store_string, ":string_register", "@gladii"),
        (try_end),
    (else_try),
        #Cultural phrase that means "fight" (first person singular)
        #Native equivalent is "swing my sword."
        #Example usage: "I want to be able to {swing my sword} with a good conscience."
        (eq, ":context", DPLMC_CULTURAL_TERM_USE_MY_WEAPON),
        (try_begin),
            (this_or_next|eq, ":culture", "fac_culture_germanic"),#Nords
            (this_or_next|eq, ":culture", "fac_culture_dacian"),#Nords
            (this_or_next|eq, ":culture", "fac_culture_caledonian"),#Nords
            (eq, ":culture", "fac_culture_celtic"),#Vaegirs
            (str_store_string, ":string_register", "@swing my axe"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Rhodoks
            (this_or_next|eq, ":culture", "fac_culture_judean"),#Rhodoks
            (this_or_next|eq, ":culture", "fac_culture_greek"),#Rhodoks
            (eq, ":culture", "fac_culture_parthian"),#Rhodoks
            (str_store_string, ":string_register", "@lift my spear"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_egyptian"),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergits
            (str_store_string, ":string_register", "@loose my arrows"),
        (else_try),
            #Default: Swadia, Sarranid, others
            (str_store_string, ":string_register", "@swing my gladius"),
        (try_end),
	(else_try),
        (eq, ":context", DPLMC_CULTURAL_TERM_KING_PRAISE),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@Caesar Augustus, Princeps of Rome"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "@Khan, scourge of the gods"),
        (else_try),
            (eq, ":culture", "fac_culture_syrian"),
            (str_store_string, ":string_register", "@Malka, great king"),
        (else_try),
            (eq, ":culture", "fac_culture_egyptian"),
            (str_store_string, ":string_register", "@Pharaoh"),
        (else_try),
            (eq, ":culture", "fac_culture_greek"),
            (str_store_string, ":string_register", "@Basileus"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@Shahanshah, king of all kings"),
        (else_try),
            (eq, ":culture", "fac_culture_judean"),
            (str_store_string, ":string_register", "@Melech, blessed by god"),
        (else_try),
            (str_store_string, ":string_register", "str_king"),
        (try_end),
	(else_try),
        (eq, ":context", DPLMC_CULTURAL_TERM_ARMY),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@legion"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "@hord"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_greek"),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@great host"),
        (else_try),
            (str_store_string, ":string_register", "@army"),
        (try_end),
	(else_try),
        (eq, ":context", DPLMC_CULTURAL_TERM_ARMY_PLURAL),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@legions"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "@hords"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_greek"),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@great hosts"),
        (else_try),
            (str_store_string, ":string_register", "@armies"),
        (try_end),
	(else_try),#Cohortes urbanae and the Praetorian Guard
        (eq, ":context", DPLMC_CULTURAL_TERM_GUARD),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@Cohortes urbanae and the Praetorian Guard"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "@guards of the khan"),
        (else_try),
            (eq, ":culture", "fac_culture_syrian"),
            (str_store_string, ":string_register", "@guards of the Shah"),
        (else_try),
            (eq, ":culture", "fac_culture_egyptian"),
            (str_store_string, ":string_register", "@guards of the Pharaoh"),
        (else_try),
            (eq, ":culture", "fac_culture_greek"),
            (str_store_string, ":string_register", "@guards of the Basileus"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@apitarpa, guards of the king"),
        (else_try),
            (str_store_string, ":string_register", "@Royal guards"),
        (try_end),
	(else_try),
        #equivalent to lowercase "king" or "queen"
        (this_or_next|eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
        (eq, ":context", DPLMC_CULTURAL_TERM_KING),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@Caesar"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "str_khan"),
        (else_try),
            (eq, ":culture", "fac_culture_syrian"),#Sarranid
            (str_store_string, ":string_register", "@Malka"),
        (else_try),
            (eq, ":culture", "fac_culture_egyptian"),#Sarranid
            (str_store_string, ":string_register", "@Pharaoh"),
        (else_try),
            (eq, ":culture", "fac_culture_greek"),#Sarranid
            (str_store_string, ":string_register", "@Basileus"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@Shah"),
        (else_try),
            (eq, ":culture", "fac_culture_judean"),
            (str_store_string, ":string_register", "@Melech"),
        (else_try),
            #Default: Swadia, Rhodok, Nord, Vaegir, others
            (str_store_string, ":string_register", "str_king"),
            (eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
            (str_store_string, ":string_register", "str_queen"),
        (try_end),
    (else_try),
        #equivalent to lowercase "kings"
        (eq, ":context", DPLMC_CULTURAL_TERM_KING_PLURAL),
        (try_begin),
            (eq, ":culture", "fac_culture_roman"),#romans
            (str_store_string, ":string_register", "@Caesars"),
        (else_try),
            (eq, ":culture", "fac_culture_sarmatian"),#Khergit
            (str_store_string, ":string_register", "@khans"),
        (else_try),
            (eq, ":culture", "fac_culture_syrian"),#Sarranid
            (str_store_string, ":string_register", "@Malka's"),
        (else_try),
            (eq, ":culture", "fac_culture_egyptian"),#Sarranid
            (str_store_string, ":string_register", "@Pharaoh's"),
        (else_try),
            (eq, ":culture", "fac_culture_greek"),#Sarranid
            (str_store_string, ":string_register", "@Basileus's"),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranid
            (eq, ":culture", "fac_culture_parthian"),#Sarranid
            (str_store_string, ":string_register", "@Shahs"),
        (else_try),
            (eq, ":culture", "fac_culture_judean"),#Sarranid
            (str_store_string, ":string_register", "@Melechs"),
        (else_try),
            #Default: Swadia, Rhodok, Nord, Vaegir, others
            (str_store_string, ":string_register", "@kings"),
        (try_end),
	(else_try),
		#equivalent to lowercase "lord"
		(eq, ":context", DPLMC_CULTURAL_TERM_LORD),
		(try_begin),
			(eq, ":culture", "fac_culture_roman"),#romans
			(str_store_string, ":string_register", "@legatus"),
		(else_try),
			(str_store_string, ":string_register", "@lord"),
		(try_end),
	(else_try),
		#equivalent to lowercase "lords"
		(eq, ":context", DPLMC_CULTURAL_TERM_LORD_PLURAL),
		(try_begin),
			(eq, ":culture", "fac_culture_roman"),#romans
			(str_store_string, ":string_register", "@legati"),
		(else_try),
			(str_store_string, ":string_register", "@lords"),
		(try_end),
	(else_try),
        #As in, "I shall tell my {swineherd} about your sweet promises" or "Any {swineherd} can claim to be king".
        (eq, ":context", DPLMC_CULTURAL_TERM_SWINEHERD),
        (store_random_in_range, ":mode", 0, 2),
        (try_begin),
            (eq, ":culture", "fac_culture_caledonian"),#Vaegirs
            (try_begin),
                (eq, ":mode", 0),
                (str_store_string, ":string_register", "@goatherd"),
            (else_try),
                (str_store_string, ":string_register", "@swineherd"),
            (try_end),
        (else_try),
            (eq, ":culture", "fac_culture_celtic"),#Vaegirs
            (try_begin),
                (eq, ":mode", 0),
                (str_store_string, ":string_register", "@goatherd"),
            (else_try),
                (str_store_string, ":string_register", "@swineherd"),
            (try_end),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_egyptian"),
            (this_or_next|eq, ":culture", "fac_culture_greek"),
            (eq, ":culture", "fac_culture_roman"),#Romans
            (try_begin),
                (eq, ":mode", 0),
                (str_store_string, ":string_register", "@dog"),
            (else_try),
                (str_store_string, ":string_register", "@rat"),
            (try_end),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_bosporan"),#Vaegirs
            (eq, ":culture", "fac_culture_sarmatian"),#Khergits
            (try_begin),
                (eq, ":mode", 0),
                (str_store_string, ":string_register", "@stable {boy/girl}"),
            (else_try),
                (str_store_string, ":string_register", "@shepherd {boy/girl}"),
            (try_end),
        (else_try),
            (this_or_next|eq, ":culture", "fac_culture_syrian"),
            (this_or_next|eq, ":culture", "fac_culture_caucasian"),#Sarranids
            (this_or_next|eq, ":culture", "fac_culture_judean"),#Sarranids
            (eq, ":culture", "fac_culture_parthian"),#Sarranids
            (try_begin),
                (eq, ":mode", 0),
                (str_store_string, ":string_register", "@goatherd"),
            (else_try),
                (str_store_string, ":string_register", "@shepherd {boy/girl}"),
            (try_end),
        (else_try),
            #Swadia, Rhodok, Nord, others
            (str_store_string, ":string_register", "@swineherd"),
        (try_end),
	(else_try),
		(eq, ":context", DPLMC_CULTURAL_TERM_TAVERNWINE),
		(try_begin),
			(this_or_next|eq, ":culture", "fac_culture_caledonian"),
            (this_or_next|eq, ":culture", "fac_culture_dacian"),
            (eq, ":culture", "fac_culture_celtic"),
			(str_store_string, ":string_register", "@bear"),
		(else_try),
			(eq, ":culture", "fac_culture_sarmatian"),
			(str_store_string, ":string_register", "@kumis"),
		(else_try),
			(eq, ":culture", "fac_culture_germanic"),
			(str_store_string, ":string_register", "@mead"),
		(else_try),
			(str_store_string, ":string_register", "@wine"),
		(try_end),
    (else_try),
	#Error string
        (assign, ":save_reg0", reg0),
		(assign, reg0, ":context"),
		(display_message, "@{!}ERROR - dplmc_print_cultural_word_to_sreg called for bad context {reg0}"),
		(str_store_string, ":string_register", "str_ERROR_string"),
		(assign, reg0, ":save_reg0"),
    (try_end),
]),

#script_dplmc_print_player_spouse_says_my_husband_wife_to_s0
#
#INPUT:
#  arg1: troop_no
#  arg2: whether the first letter must be capitalized
#
#OUTPUT:
#    s0: a string that can be substituted for "my {husband/wife}" or "my love"
("dplmc_print_player_spouse_says_my_husband_wife_to_s0",[
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":capitalized"),

    (assign, ":save_reg0", reg0),
    (assign, ":save_reg6", reg6),
    (assign, ":save_reg7", reg7),
    #(assign, reg6, ":capitalized"),
    (assign, reg7, 0),
    #Base switch is 50 (i.e. where the "brave champion" greeting starts)
    (try_begin),
        (lt, ":troop_no", 1),#bad value
        (assign, reg0, 0),
        (assign, reg6, lrep_none),
    (else_try),
	    (call_script, "script_troop_get_player_relation", ":troop_no"),#write relation to reg0
        (troop_get_slot, reg6, ":troop_no", slot_lord_reputation_type),#write relation to reg6
        (eq, reg6, lrep_conventional),#...jumps to next branch (keeping reg0 and reg6) if this isn't true
        (val_add, reg0, 25),#from 25+
    (else_try),
        (eq, reg6, lrep_otherworldly),
        (val_add, reg0, 30),#from 20+
    (else_try),
        (eq, reg6, lrep_moralist),
        (store_sub, reg7, "$player_honor", 10),
        (val_clamp, reg7, -40, 31),
        (val_add, reg0, reg7),
        (assign, reg7, 0),
    (else_try),
        (eq, reg6, lrep_ambitious),
        (assign, reg7, -10),
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
            (val_add, reg7, 10),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (val_add, reg7, 10),
        (try_end),
        (val_clamp, reg7, -10, 30),
        (val_add, reg0, reg7),
        (assign, reg7, 0),
    (else_try),
        (eq, reg6, lrep_hedonistic),
        (val_add, reg7, 10),#from 30+
    (else_try),
        (eq, reg6, lrep_adventurous),
        (val_add, reg7, 20),#from 30+
    (else_try),
        (eq, reg6, lrep_none),
        (is_between, reg6, heroes_begin, heroes_end),
        (val_sub, reg0, 20),#from 70+
    (else_try),
        (eq, reg6, lrep_cunning),
        (val_sub, reg0, 20),#from 70+
    (else_try),
        (this_or_next|eq, reg6, lrep_debauched),
        (this_or_next|eq, reg6, lrep_quarrelsome),
        (eq, reg6, lrep_selfrighteous),
        (val_sub, reg0, 30),#from 80+
    (try_end),
    (try_begin),
        (ge, reg0, 50),
        (assign, reg7, 1),
    (try_end),
    (try_begin),
        #Embellishment: diminuitive pet-names
        (eq, reg6, lrep_debauched),
        (gt, ":troop_no", 0),
        (store_character_level, ":player_level", "trp_player"),
        (store_character_level, ":troop_level", ":troop_no"),
        (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        (this_or_next|ge, ":troop_level", ":player_level"),
        (this_or_next|troop_slot_ge, ":troop_no", slot_troop_renown, ":player_renown"),
        (lt, reg0, 50),
        (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
        (str_store_string, s0, "@{reg6?M:m}y poppet"),
    (else_try),
        #The basic idea.  Further embellishments may come.
        (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
        (str_store_string, s0, "str_dplmc_reg6my_reg7spouse"),
    (try_end),
    #Revert registers
    (assign, reg0, ":save_reg0"),
    (assign, reg6, ":save_reg6"),
    (assign, reg7, ":save_reg7"),
]),

##"script_dplmc_initialize_autoloot"
##
##Only needs to be called once, but it's safe to call multiple times
##(it uses "$g_autoloot" to store the version)
##
##Inputs: arg1: 1 to force this to run
##Outputs: None
("dplmc_initialize_autoloot",[
	(store_script_param_1, ":force_to_run"),
    (try_begin),
        #Check if there is anything to do
        (this_or_next|eq, ":force_to_run", 1),
        (neq, "$g_autoloot", 2),
        (try_begin),
            #Print a message to make it obvious when this is happening more than it should.
            (ge, "$cheat_mode", 1),
            (store_current_hours, ":hours"),
            (gt, ":hours", 0),
            (display_message, "@{!}Initializing auto-loot.  This message should not appear more than once."),
        (try_end),
        #Initialize
        (try_for_range, ":cur_food", food_begin, food_end),
            (item_set_slot, ":cur_food", dplmc_slot_item_food_portion, 1),
        (try_end),
        # #deprecated due to 1.165 operations
        # (call_script, "script_dplmc_init_item_difficulties"),
        # (call_script, "script_dplmc_init_item_base_score"),
        (assign, "$g_dplmc_auto_sell_price_limit", 50),
        (assign, "$g_dplmc_sell_items_when_leaving", 0),
        (assign, "$g_dplmc_buy_food_when_leaving", 0),
        (item_set_slot, itp_type_book, dplmc_slot_item_type_not_for_sell, 1),
        (item_set_slot, itp_type_goods, dplmc_slot_item_type_not_for_sell, 1),
        (item_set_slot, itp_type_animal, dplmc_slot_item_type_not_for_sell, 1),
        (assign, "$g_autoloot", 2),
    (try_end),
]),

##"script_dplmc_get_troop_standing_in_faction"
#
#INPUT: arg1  :troop_no
#       arg2  :faction_no
#
#OUTPUT:
#       reg0  A constant with the value DPLMC_FACTION_STANDING_<something>
#
## Constants defined in module_constants.py
#DPLMC_FACTION_STANDING_LEADER = 60
#DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
#DPLMC_FACTION_STANDING_MARSHALL = 40
#DPLMC_FACTION_STANDING_LORD = 30
#DPLMC_FACTION_STANDING_DEPENDENT = 20
#DPLMC_FACTION_STANDING_MEMBER = 10#includes mercenaries
#DPLMC_FACTION_STANDING_PETITIONER = 5
#DPLMC_FACTION_STANDING_UNAFFILIATED = 0
("dplmc_get_troop_standing_in_faction",[
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":faction_no"),

    (assign, ":standing", DPLMC_FACTION_STANDING_UNAFFILIATED),
    (assign, ":original_faction_no", ":faction_no"),
    (try_begin),
        #Translate fac_player_faction
        (eq, ":faction_no", "fac_player_faction"),
        (assign, ":faction_no", "fac_player_supporters_faction"),
    (try_end),

    (try_begin),
        (this_or_next|lt, ":troop_no", 0),#Do nothing, bad troop ID
        (lt, ":faction_no", 0),#Do nothing, bad faction
    (else_try),
        #Because of how this script is used, if fac_player_supporters_faction is active,
        # this always reports that the player is its leader (even though that is sometimes
        # untrue, for example in a claimant quest)
        (eq, ":troop_no", "trp_player"),#Short-circuit the remainder if these are true
        (eq, ":faction_no", "fac_player_supporters_faction"),
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
        # (neg|is_between, "$supported_pretender", pretenders_begin, pretenders_end), #SB : claimant exception
        (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
    (else_try),
		(try_begin),
            #Translate fac_player_supporters_faction
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (gt, "$players_kingdom", 0),
            (assign, ":faction_no", "$players_kingdom"),
		(try_end),

        (store_faction_of_troop, ":troop_faction", ":troop_no"),
        (try_begin),
            #Translate fac_player_supporters_faction
            (this_or_next|eq, ":troop_no", "trp_player"),
            (this_or_next|eq, ":troop_faction", "fac_player_faction"),
            (eq, ":troop_faction", "fac_player_supporters_faction"),
            (assign, ":troop_faction", "fac_player_supporters_faction"),
            (gt, "$players_kingdom", 0),
            (assign, ":troop_faction", "$players_kingdom"),
        (try_end),
        (eq, ":troop_faction", ":faction_no"),#<- Short-circuit the remainder if this is false
        (assign, ":standing", DPLMC_FACTION_STANDING_MEMBER),

        (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
        (try_begin),
            #Faction leader
            (eq, ":faction_leader", ":troop_no"),
            (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
        (else_try),
            #Spouse of faction leader
            (gt, ":faction_leader", -1),
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
            (troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
            #Deal with possible uninitialized slot
            (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
            (this_or_next|neq, ":faction_leader", 0),
            (is_between, ":troop_no", heroes_begin, heroes_end),
            (assign, ":standing", DPLMC_FACTION_STANDING_LEADER_SPOUSE),
        (else_try),
            #Faction marshall
            (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
            (assign, ":standing", DPLMC_FACTION_STANDING_MARSHALL),
        (else_try),
           #If the troop is the player, if he has homage he is a lord.
           #Otherwise he is a mercenary.
           (eq, ":troop_no", "trp_player"),
           (try_begin),
                (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
                (ge, "$player_has_homage", 1),
                (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
           (else_try),
                #If the player is married to a lord/lady in the faction, the
                #homage variable should always be set to 1+, but add a separate
                #check just in case.
                (troop_get_slot, reg0, "trp_player", slot_troop_spouse),
                (is_between, reg0, heroes_begin, heroes_end),
                (store_faction_of_troop, reg0, reg0),
                (this_or_next|eq, reg0, "fac_player_supporters_faction"),
                (eq, reg0, ":faction_no"),
                (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
           (try_end),
        (else_try),
            #None of the following conditions apply for non-heroes
            (this_or_next|lt, ":troop_no", heroes_begin),
            (neg|troop_is_hero, ":troop_no"),
        (else_try),
            #For kingdom heroes, part 1 (check lordship based on occupation)
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
            (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
        (else_try),
            #For kingdom ladies
            (this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
            (assign, ":standing", DPLMC_FACTION_STANDING_DEPENDENT),
        (else_try),
            #For petitioners
            (eq, ":original_faction_no", "fac_player_supporters_faction"),
            (is_between, ":troop_no", lords_begin, lords_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
            (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (assign, ":standing", DPLMC_FACTION_STANDING_PETITIONER),
        (else_try),
            #For kingdom heroes, part 2 (all non-companion active NPCs)
            (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
            (neg|is_between, ":troop_no", companions_begin, companions_end),
            (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
        (try_end),
    (try_end),
    (assign, reg0, ":standing"),
]),

## "script_dplmc_store_troop_is_eligible_for_affiliate_messages"
("dplmc_store_troop_is_eligible_for_affiliate_messages",[
	(store_script_param_1, ":troop_no"),
	(assign, ":is_eligible", 0),
	(assign, ":save_reg1", reg1),
	(try_begin),
		(lt, ":troop_no", 1),
	(else_try),
		(neg|troop_is_hero, ":troop_no"),
	(else_try),
		#Initialize :faction_no and :faction_relation
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		(store_relation, ":faction_relation", ":faction_no", "fac_player_supporters_faction"),
		(try_begin),
			(eq, ":faction_no", "$players_kingdom"),
			(val_max, ":faction_relation", 1),
		(try_end),
		#Companion
		(gt, ":faction_relation", -1),
		(is_between, ":troop_no", companions_begin, companions_end),
		(neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
		(troop_slot_ge, ":troop_no", slot_troop_player_relation, 20),
		(assign, ":is_eligible", 1),
	(else_try),
		#Faction marshall (if the player is the faction leader)
		#Faction leader (if the player is the faction marshall)
		(eq, ":faction_no", "$players_kingdom"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
		(call_script, "script_dplmc_get_troop_standing_in_faction", ":troop_no", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
		(assign, ":is_eligible", 1),
	(else_try),
		#Spouse / relatives / in-laws
		(gt, ":faction_relation", -1),
		#(is_between, ":troop_no", heroes_begin, heroes_end),## should be safe even for non-heroes
		(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", "trp_player"),
		(ge, reg0, 2),
		(troop_get_slot, reg1, ":troop_no", slot_troop_player_relation),
		(val_add, reg0, reg1),
		(ge, reg0, 20),
		(assign, ":is_eligible", 1),
	(else_try),
		#Affiliates
		(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
		(ge, reg0, 1),
		(assign, ":is_eligible", 1),
	(else_try),
		#Cheat mode: add faction leaders to test this out
		(gt, "$cheat_mode", 0),
		(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
		(faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
		(assign, ":is_eligible", 1),
	(try_end),
	(assign, reg1, ":save_reg1"),
	(assign, reg0, ":is_eligible"),
]),

# "script_dplmc_sell_all_prisoners"
#INPUT:
#Arg 1: actually remove (positive for yes, zero or negative for no)
#Arg 2: if positive, use this as a fixed price instead of calculating dynamically
#OUTPUT:
#reg0: amount of gold gained (or would have been gained if the sale occurred)
#reg1: number of prisoners sold (or would have been sold if the sale occurred)
("dplmc_sell_all_prisoners",[
    (store_script_param_1, ":actually_remove"),
    (store_script_param_2, ":fixed_price"),
    (assign, ":total_removed", 0),
    (assign, ":total_income", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":troop_no", "p_main_party", ":i_stack"),
        #SB : correction to use game script
        (call_script, "script_game_check_prisoner_can_be_sold", ":troop_no"),
        (eq, reg0, 1),
        # (neg|troop_is_hero, ":troop_no"),
        (party_prisoner_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
        (try_begin),
            (gt, ":fixed_price", 0),
            (assign, ":sell_price", ":fixed_price"),
        (else_try),
            (call_script, "script_game_get_prisoner_price", ":troop_no"),
            (assign, ":sell_price", reg0),
        (try_end),
        (store_mul, ":stack_total_price", ":sell_price", ":stack_size"),
        (val_add, ":total_income", ":stack_total_price"),
        (val_add, ":total_removed", ":stack_size"),
        (gt, ":actually_remove", 0),#Stop short if this is a dry run
        (party_remove_prisoners, "p_main_party", ":troop_no", ":stack_size"),
    (try_end),
    (try_begin),
        (gt, ":actually_remove", 0),#Stop short if this is a dry run
        (troop_add_gold, "trp_player", ":total_income"),
    (try_end),
    (assign, reg0, ":total_income"),
    (assign, reg1, ":total_removed"),
]),

#"script_dplmc_translate_inactive_player_supporter_faction_2"
#
#Since "fac_player_supporters_faction" is often used as a parameter when what
#is really meant is "the faction led by the player" (which is never a different
#faction in Native), there are many calls we want to change.  Another solution
#is to approach the problem from the other side, and "correct" the arguments.
#
#If exactly one argument is equal to fac_player_supporters_faction, and fac_player_supporters_faction
#is not sfs_active, and $players_kingdom is an NPC kingdom of which the player is ruler or co-ruler,
#and the other argument is not equal to $players_kingdom, then the argument equal to fac_player_supporters_faction
#will be replaced with $players_kingdom.
#
#INPUT:
# arg1 - faction_1
# arg2 - faction_2
#OUTPUT:
# reg0 - faction_1, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
# reg1 - faction_2, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
("dplmc_translate_inactive_player_supporter_faction_2",[
    (store_script_param_1, ":faction_1"),
    (store_script_param_2, ":faction_2"),
	(try_begin),
		(this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
		(this_or_next|neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(this_or_next|eq, ":faction_1", "$players_kingdom"),
		(this_or_next|eq, ":faction_2", "$players_kingdom"),
        (eq, ":faction_1", ":faction_2"),
    #Do nothing
	(else_try),
		(eq, ":faction_1", "fac_player_supporters_faction"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":faction_1", "$players_kingdom"),
	(else_try),
		(eq, ":faction_2", "fac_player_supporters_faction"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":faction_2", "$players_kingdom"),
	(try_end),
	(assign, reg0, ":faction_1"),
	(assign, reg1, ":faction_2"),
]),

##"script_cf_dplmc_player_party_meets_autoloot_conditions"
##
#
#INPUT:
#   None
#OUTPUT:
#   reg0   -1 means there are no companions and skill is too low
#           0 means there are companions and skill is too low
#           1 means skill is high enough but there are no companions
#           2 means skill is high enough and there are companions
#
# Will fail if it does not set reg0 to 2.
##
("cf_dplmc_player_party_meets_autoloot_conditions",[
    (eq, "$g_autoloot_active", 1),
    (eq, "$enlisted_party", -1),#freelancer
    (store_skill_level, ":best_loot_skill", "skl_looting", "trp_player"),
    (store_skill_level, ":player_inv_skill", "skl_inventory_management", "trp_player"),
    (assign, ":best_inv_skill", ":player_inv_skill"),
    (assign, ":num_companions", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id,  ":stack_troop", "p_main_party", ":stack_no"),
        (ge, ":stack_troop", 0),
        #Check skill
        (is_between, ":stack_troop", heroes_begin, heroes_end),
        (store_skill_level, ":hero_skill", "skl_inventory_management", ":stack_troop"),
        (val_max, ":best_inv_skill", ":hero_skill"),

        (store_skill_level, ":hero_skill", "skl_looting", ":stack_troop"),
        (val_max, ":best_loot_skill", ":hero_skill"),
        #Check is companion
        (is_between, ":stack_troop", companions_begin, companions_end),
        (val_add, ":num_companions", 1),
    (try_end),
    (try_begin),
        (lt, ":player_inv_skill", 2),
        (lt, ":best_inv_skill", 3),
        (lt, ":best_loot_skill", 2),
        (assign, reg0, 0),
        (try_begin),
            (lt, ":num_companions", 1),#change 2011-06-07
            (assign, reg0, -1),
        (try_end),
        (else_try),
        (assign, reg0, 1),
        (gt, ":num_companions", 0),
        (assign, reg0, 2),
    (try_end),
    (eq, reg0, 2),
]),

##"script_dplmc_troop_get_family_relation_to_troop"
##
##Like troop_get_family_relation_to_troop, except instead of writing to s11,
##it writes the index of the relation string to reg1, and writes nothing at
##all to reg4.
("dplmc_troop_get_family_relation_to_troop",[
    (store_script_param_1, ":troop_1"),
    (store_script_param_2, ":troop_2"),

    ##dplmc start+
	(try_begin),
		(eq, ":troop_1", active_npcs_including_player_begin),
		(assign, ":troop_1", "trp_player"),
	(try_end),
	(try_begin),
		(eq, ":troop_2", active_npcs_including_player_begin),
		(assign, ":troop_2", "trp_player"),
	(try_end),

	#use gender script
    #(troop_get_type, ":gender_1", ":troop_1"),
	(call_script, "script_dplmc_store_troop_is_female", ":troop_1"),
	(assign, ":gender_1", reg0),
	(assign, ":relation_string", "str_no_relation"),
	##dplmc end+
	(assign, ":relation_strength", 0),

	##dplmc start+
	#Uninitialized memory is 0, which equals "trp_player", which is the cause
	#of some annoying bugs.  In Native the game doesn't set the various family
	#slots to -1 except for the player and in the heroes_begin to heroes_end
	#range.

	(troop_get_slot, ":spouse_of_1", ":troop_1", slot_troop_spouse),#just do this to get an error if the troop ID is bad
	(troop_get_slot, ":spouse_of_2", ":troop_2", slot_troop_spouse),#just do this to get an error if the troop ID is bad

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_spouse),
	(assign, ":spouse_of_1", reg0),
	(assign, ":spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_father),
	(assign, ":father_of_spouse_of_1", reg0),
	(assign, ":father_of_spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_mother),
	#(assign, ":mother_of_spouse_of_1", reg0),
	(assign, ":mother_of_spouse_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_father),
	(assign, ":father_of_1", reg0),
	(assign, ":father_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_mother),
	(assign, ":mother_of_1", reg0),
	(assign, ":mother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_father),
	(assign, ":paternal_grandfather_of_1", reg0),
	(assign, ":paternal_grandfather_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_mother),
	(assign, ":paternal_grandmother_of_1", reg0),
	(assign, ":paternal_grandmother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_father),
	(assign, ":maternal_grandfather_of_1", reg0),
	(assign, ":maternal_grandfather_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_mother),
	(assign, ":maternal_grandmother_of_1", reg0),
	(assign, ":maternal_grandmother_of_2", reg1),

	(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_guardian),
	(assign, ":guardian_of_1", reg0),
	(assign, ":guardian_of_2", reg1),
	##diplomacy end+
	#(str_store_string, s11, "str_no_relation"),
	(try_begin),
        (eq, ":troop_1", ":troop_2"),
        #self
	(else_try),
        ##diplomacy start+
        (this_or_next|eq, ":spouse_of_2", ":troop_1"),#polygamy helper
        ##diplomacy end+
        (eq, ":spouse_of_1", ":troop_2"),
        (assign, ":relation_strength", 20),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_wife"),
        (else_try),
            (assign, ":relation_string", "str_husband"),
        (try_end),
    (else_try),
        (eq, ":father_of_2", ":troop_1"),
        (assign, ":relation_strength", 15),
        (assign, ":relation_string", "str_father"),
    (else_try),
        (eq, ":mother_of_2", ":troop_1"),
        (assign, ":relation_strength", 15),
        (assign, ":relation_string", "str_mother"),
	(else_try),
        (this_or_next|eq, ":father_of_1", ":troop_2"),
        (eq, ":mother_of_1", ":troop_2"),
        (assign, ":relation_strength", 15),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_daughter"),
        (else_try),
            (assign, ":relation_string", "str_son"),
        (try_end),
	##diplomacy start+
	(else_try),
	   #Check for half-siblings: sharing a father
	   (neq, ":father_of_1", -1),
	   (eq, ":father_of_1", ":father_of_2"),
	   (neq, ":mother_of_1", ":mother_of_2"),
	   (assign, ":relation_strength", 10),
	   (try_begin),
	     (eq, ":gender_1", tf_female),
	     (assign, ":relation_string", "str_dplmc_half_sister"),
	   (else_try),
	     (assign, ":relation_string", "str_dplmc_half_brother"),
	   (try_end),
   (else_try),
	   #Check for half-siblings: sharing a mother
	   (neq, ":mother_of_1", -1),
	   (eq, ":mother_of_1", ":mother_of_2"),
	   (neq, ":father_of_1", ":father_of_2"),
	   (assign, ":relation_strength", 10),
	   (try_begin),
	     (eq, ":gender_1", tf_female),
	     (assign, ":relation_string", "str_dplmc_half_sister"),
	   (else_try),
	     (assign, ":relation_string", "str_dplmc_half_brother"),
	   (try_end),
	##diplomacy end+
	(else_try),
        #(gt, ":father_of_1", -1), #necessary, as some lords do not have the father registered #dplmc+ replaced
        (neq, ":father_of_1", -1), #dplmc+ added
        (eq, ":father_of_1", ":father_of_2"),
        (assign, ":relation_strength", 10),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sister"),
        (else_try),
            (assign, ":relation_string", "str_brother"),
        (try_end),
	(else_try),
        (eq, ":guardian_of_2", ":troop_1"),
        (assign, ":relation_strength", 10),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sister"),
        (else_try),
            (assign, ":relation_string", "str_brother"),
        (try_end),
	(else_try),
        (eq, ":guardian_of_1", ":troop_2"),
        (assign, ":relation_strength", 10),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sister"),
        (else_try),
            (assign, ":relation_string", "str_brother"),
        (try_end),
	##diplomacy start+
   (else_try),#polygamy, between two people married to the same person
        (neq, ":spouse_of_1", -1),
        (eq, ":spouse_of_2", ":spouse_of_1"),
        (assign, ":relation_strength", 10),
        (try_begin),
            (call_script, "script_dplmc_store_troop_is_female", ":troop_2"),
            (neq, ":gender_1", reg0),
            (assign, ":relation_string", "str_dplmc_co_spouse"),
        (else_try),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_dplmc_sister_wife"),
        (else_try),
            (assign, ":relation_string", "str_dplmc_co_husband"),
        (try_end),
	##diplomacy end+
	(else_try),
        #(gt, ":paternal_grandfather_of_1", -1),#dplmc+ replaced
        (neq, ":father_of_2", -1),#dplmc+ added
        (this_or_next|eq, ":maternal_grandfather_of_1", ":father_of_2"),#dplmc+ added
        (eq, ":paternal_grandfather_of_1", ":father_of_2"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_niece"),
        (else_try),
            (assign, ":relation_string", "str_nephew"),
        (try_end),
	##diplomacy start+: add niece/nephew through mother
	(else_try),
        (neq, ":mother_of_2", -1),
        (this_or_next|eq, ":maternal_grandmother_of_1", ":mother_of_2"),
        (eq, ":paternal_grandmother_of_1", ":mother_of_2"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_niece"),
        (else_try),
            (assign, ":relation_string", "str_nephew"),
        (try_end),
	##diplomacy end+
	(else_try), #specifically aunt and uncle by blood -- i assume that in a medieval society with lots of internal family conflicts, they would not include aunts and uncles by marriage
        #(gt, ":paternal_grandfather_of_2", -1),#dplmc+ replaced
        (neq, ":father_of_1", -1),#dplmc+ added
        (this_or_next|eq, ":maternal_grandfather_of_2", ":father_of_1"),#dplmc+ added
        (eq, ":paternal_grandfather_of_2", ":father_of_1"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_aunt"),
        (else_try),
            (assign, ":relation_string", "str_uncle"),
        (try_end),
        ##diplomacy start+
	#blood uncles & blood aunts, continued (via mother)
	(else_try),
        (neq, ":mother_of_1", -1),
        (this_or_next|eq, ":maternal_grandmother_of_2", ":mother_of_1"),
        (eq, ":paternal_grandmother_of_2", ":mother_of_1"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_aunt"),
        (else_try),
            (assign, ":relation_string", "str_uncle"),
        (try_end),
	##diplomacy end+
	(else_try),
        #(gt, ":paternal_grandfather_of_1", 0),#dplmc+ replaced (why was this one "gt 0" but the previous "gt -1"?)
        (neq, ":paternal_grandfather_of_1", -1),#dplmc+ added
        (this_or_next|eq, ":maternal_grandfather_of_2", ":paternal_grandfather_of_1"),#dplmc+ added
        (eq, ":paternal_grandfather_of_2", ":paternal_grandfather_of_1"),
        (assign, ":relation_strength", 2),
        (assign, ":relation_string", "str_cousin"),
    ##diplomacy start+
    #Add cousin via paternal grandmother or maternal grandparents
    (else_try),
        (neq, ":maternal_grandfather_of_1", -1),
        (this_or_next|eq, ":maternal_grandfather_of_2", ":maternal_grandfather_of_1"),
        (eq, ":paternal_grandfather_of_2", ":maternal_grandfather_of_1"),
        (assign, ":relation_strength", 2),
        (assign, ":relation_string", "str_cousin"),
    (else_try),
        (neq, ":paternal_grandmother_of_1", -1),
        (this_or_next|eq, ":maternal_grandmother_of_2", ":paternal_grandmother_of_1"),
        (eq, ":paternal_grandmother_of_2", ":paternal_grandmother_of_1"),
        (assign, ":relation_strength", 2),
        (assign, ":relation_string", "str_cousin"),
    (else_try),
        (neq, ":maternal_grandmother_of_1", -1),
        (this_or_next|eq, ":maternal_grandmother_of_2", ":maternal_grandmother_of_1"),
        (eq, ":paternal_grandmother_of_2", ":maternal_grandmother_of_1"),
        (assign, ":relation_strength", 2),
        (assign, ":relation_string", "str_cousin"),
    ##diplomacy end+
    (else_try),
        (eq, ":father_of_spouse_of_1", ":troop_2"),
        (assign, ":relation_strength", 5),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_daughterinlaw"),
        (else_try),
            (assign, ":relation_string", "str_soninlaw"),
        (try_end),
    (else_try),
        (eq, ":father_of_spouse_of_2", ":troop_1"),
        (assign, ":relation_strength", 5),
        (assign, ":relation_string", "str_fatherinlaw"),
    (else_try),
        (eq, ":mother_of_spouse_of_2", ":troop_1"),
        (neq, ":mother_of_spouse_of_2", "trp_player"), #May be necessary if mother for troops not set to -1
        (assign, ":relation_strength", 5),
        (assign, ":relation_string", "str_motherinlaw"),
    (else_try),
        #(gt, ":father_of_spouse_of_1", -1), #necessary #dplmc+ replaced
        (neq, ":father_of_spouse_of_1", -1), #dplmc+ added
        (eq, ":father_of_spouse_of_1", ":father_of_2"),
        (assign, ":relation_strength", 5),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sisterinlaw"),
        (else_try),
            (assign, ":relation_string", "str_brotherinlaw"),
        (try_end),
	(else_try),
        #(gt, ":father_of_spouse_of_2", -1), #necessary #dplmc+ replaced
        (neq, ":father_of_spouse_of_2", -1), #dplmc+ added
        (eq, ":father_of_spouse_of_2", ":father_of_1"),
        (assign, ":relation_strength", 5),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sisterinlaw"),
        (else_try),
            (assign, ":relation_string", "str_brotherinlaw"),
        (try_end),
	(else_try),
        #	  (gt, ":spouse_of_2", -1), #necessary to avoid bug #dplmc+ replaced
        (neq, ":spouse_of_2", -1), #dplmc+ added
        (troop_slot_eq, ":spouse_of_2", slot_troop_guardian, ":troop_1"),
        (assign, ":relation_strength", 5),
        (try_begin),
            (eq, ":gender_1", tf_female),#dplmc+ added
            (assign, ":relation_string", "str_sisterinlaw"),
        (else_try),
            (assign, ":relation_string", "str_brotherinlaw"),
        (try_end),
	(else_try),
        #(gt, ":spouse_of_1", -1), #necessary to avoid bug #dplmc+ replaced
        (neq, ":spouse_of_1", -1), #dplmc+ added
        (troop_slot_eq, ":spouse_of_1", slot_troop_guardian, ":troop_2"),
        (assign, ":relation_strength", 5),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_sisterinlaw"),
        (else_try),
            (assign, ":relation_string", "str_brotherinlaw"),
        (try_end),
	(else_try),
        #grandchild
        (neq, ":troop_2", -1),
        (this_or_next|eq, ":paternal_grandfather_of_1", ":troop_2"),
        (this_or_next|eq, ":maternal_grandfather_of_1", ":troop_2"),
        (this_or_next|eq, ":paternal_grandmother_of_1", ":troop_2"),
        (eq, ":maternal_grandmother_of_1", ":troop_2"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_dplmc_granddaughter"),
        (else_try),
            (assign, ":relation_string", "str_dplmc_grandson"),
        (try_end),
	(else_try),
        #grandparent
        (neq, ":troop_1", -1),
        (this_or_next|eq, ":paternal_grandfather_of_2", ":troop_1"),
        (this_or_next|eq, ":maternal_grandfather_of_2", ":troop_1"),
        (this_or_next|eq, ":paternal_grandmother_of_2", ":troop_1"),
        (eq, ":maternal_grandmother_of_2", ":troop_1"),
        (assign, ":relation_strength", 4),
        (try_begin),
            (eq, ":gender_1", tf_female),
            (assign, ":relation_string", "str_dplmc_grandmother"),
        (else_try),
            (assign, ":relation_string", "str_dplmc_grandfather"),
        (try_end),
	(try_end),
	##Add uncles and aunts by marriage.
	##In Native, the relation strength for blood uncles/aunts is 4, and for cousins is 2.
	##In light of this I've decided to set the relation strength for aunts/uncles by marriage to 2.
	(try_begin),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 1
		(ge, ":spouse_of_1", 0),
		(neg|troop_slot_eq, ":spouse_of_1", slot_troop_father, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_father, ":paternal_grandfather_of_2"),
		(troop_slot_eq, ":spouse_of_1", slot_troop_father, ":maternal_grandfather_of_2"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_aunt"),
		(else_try),
			(assign, ":relation_string", "str_uncle"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 2
		(ge, ":spouse_of_1", 0),
		(neg|troop_slot_eq, ":spouse_of_1", slot_troop_mother, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":paternal_grandmother_of_2"),
		(troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":maternal_grandmother_of_2"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_aunt"),
		(else_try),
			(assign, ":relation_string", "str_uncle"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 1
		(ge, ":spouse_of_2", 0),
		(neg|troop_slot_eq, ":spouse_of_2", slot_troop_father, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_father, ":paternal_grandfather_of_1"),
        (troop_slot_eq, ":spouse_of_2", slot_troop_father, ":maternal_grandfather_of_1"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_niece"),
		(else_try),
			(assign, ":relation_string", "str_nephew"),
		(try_end),
	(else_try),
		(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
		#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 2
		(ge, ":spouse_of_2", 0),
		(neg|troop_slot_eq, ":spouse_of_2", slot_troop_mother, -1),
		(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":paternal_grandmother_of_1"),
        (troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":maternal_grandmother_of_1"),
		(assign, ":relation_strength", 2),
		(try_begin),
			(eq, ":gender_1", tf_female),
			(assign, ":relation_string", "str_niece"),
		(else_try),
			(assign, ":relation_string", "str_nephew"),
		(try_end),
	(try_end),
	(try_begin),
		(this_or_next|neg|troop_is_hero, ":troop_1"),
		(neg|troop_is_hero, ":troop_2"),
		(assign, ":relation_string", "str_no_relation"),
		(assign, ":relation_strength", 0),
	(try_end),
	(assign, reg0, ":relation_strength"),
	(assign, reg1, ":relation_string"),
]),

##"script_cf_dplmc_faction_has_bias_against_gender"
("cf_dplmc_faction_has_bias_against_gender", [
	(store_script_param_1, ":faction_no"),
	(store_script_param_2, ":test_gender"),#Special: 1 is female

    (assign, reg0, 0),
	(lt, "$g_disable_condescending_comments", 2),#If bias is disabled, do not continue
	(is_between, ":test_gender", 0, 2),#valid genders are 0 and 1

	(try_begin),
		(eq, ":faction_no", "fac_player_supporters_faction"),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(assign, ":faction_no", "$players_kingdom"),
	(try_end),

	(try_begin),
		#For a-typical factions, nothing by default.
		(neg|is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
	(else_try),
		#If the leader has that gender, no prejudice.
		(faction_get_slot, ":active_npc", ":faction_no", slot_faction_leader),
		(gt, ":active_npc", -1),
		(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
		(eq, reg0, ":test_gender"),
		(assign, reg0, 0),
	(else_try),
		#Traditional gender prejudice if both are true:
		#1.  The faction has no original members of the specified gender.
		#2.  The faction has original members with non-accepting lord personalities.

		(assign, ":num_closeminded", 0),
		(assign, ":end_cond", active_npcs_end),

		(try_for_range, ":active_npc", active_npcs_begin, ":end_cond"),#Deliberately do not include kingdom ladies
			#Also deliberately exclude companions and pretenders
			#(Pretenders are marginalized at the start of the game, and
			#companions don't necessarily start in positions of power either)
			(this_or_next|is_between, ":active_npc", kings_begin, kings_end),
				(is_between, ":active_npc", lords_begin, lords_end),
			(troop_slot_eq, ":active_npc", slot_troop_original_faction, ":faction_no"),

			(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
			(try_begin),
				(eq, reg0, ":test_gender"),
				(assign, ":num_closeminded", -1000),
				(assign, ":end_cond", ":active_npc"),
			(else_try),
				(troop_get_slot, reg0, ":active_npc", slot_lord_reputation_type),
				(is_between, reg0, lrep_none + 1, lrep_roguish),#Lord (non-commoner, non-liege, non-lady) personality type
				(neq, reg0, lrep_cunning),
				(neq, reg0, lrep_goodnatured),
				(val_add, ":num_closeminded", 1),
			(try_end),
		(try_end),

		(store_sub, reg0, ":num_closeminded", 1),#Needs at least one
		(val_clamp, reg0, 0, 2),
	(try_end),

	(try_begin),
		(ge, "$cheat_mode", 1),
		(assign, ":end_cond", reg1),#just save reg1 and reg2 (ignore the normal meaning of the variable names)
		(assign, ":active_npc", reg2),
		(assign, reg1, ":faction_no"),
		(assign, reg2, ":test_gender"),
		(display_message, "@{!} Checked if faction {reg1} is prejudiced against {reg2?women:men}: {reg0?true:false}"),
		(assign, reg1, ":end_cond"),#revert reg1 and reg2 (ignore the normal meaning of the variable names)
		(assign, reg2, ":active_npc"),
	(try_end),
	(gt, reg0, 0),
]),

#"script_dplmc_store_troop_personality_caution_level"
#
# INPUT:
#   arg1 :troop_no
# OUTPUT:
#   reg0 -1 for aggressive
#         0 for neither
#         1 for cautious
("dplmc_store_troop_personality_caution_level", [
	#Used a number of places to determine whether a lord is cautious
	#or aggressive.  The standard is something like:
	#
	#For cautious:
	#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
    #    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
	#
	#For aggressive:
	#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
    #    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
    #    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
	#
	#I've expanded this for companion/lady personalities.
	#The result can be either:
	# -1  =  aggressive
	#  0  =  neutral
	#  1  =  cautious
	(store_script_param_1, ":troop_no"),

	(try_begin),
		(neg|is_between, ":troop_no", heroes_begin, heroes_end),#The player or troops that don't have slot_lord_reputation_type
		(assign, reg0, 0),#neither cautious nor aggressive
	(else_try),
		(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_aristocratic),
		(lt, reg0, 0),#compliments when the player retreats
		(assign, reg0, 1),#cautious
	(else_try),
		(gt, reg0, 0),#complains when the player retreats
		(assign, reg0, -1),#aggressive
	(else_try),
		(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
		(this_or_next|eq, ":reputation", lrep_adventurous),
		(this_or_next|eq, ":reputation", lrep_martial),
		(this_or_next|eq, ":reputation", lrep_quarrelsome),
        (eq, ":reputation", lrep_selfrighteous),
		(assign, reg0, -1),#aggressive
	(else_try),
        (this_or_next|ge, ":reputation", lrep_hedonistic),
		(this_or_next|ge, ":reputation", lrep_conventional),
		(this_or_next|eq, ":reputation", lrep_upstanding),
		(this_or_next|eq, ":reputation", lrep_debauched),
		(this_or_next|eq, ":reputation", lrep_goodnatured),
        (eq, ":reputation", lrep_cunning),
		(assign, reg0, 1),#cautious
	(else_try),
		(assign, reg0, 0),#neither cautious nor aggressive
	(try_end),
]),

##"script_dplmc_cap_troop_describes_troop_to_troop_s1"
#
# e.g.
#
#(call_script, "script_dplmc_cap_troop_describes_troop_to_troop_s1", 1, "trp_player", ":third_lord", "$g_talk_troop"),
#
#INPUT:
#        arg1  :capitalization (0 if middle of sentence, 1 if sentence start)
#        arg2  :speaker (the one doing the talking)
#        arg3  :described (the one being named)
#        arg4  :listener (the one being spoken to)
#
#OUTPUT:
#        Writes result to s0, clobbers s0
#
#Similar to "script_troop_describes_troop_to_s15", except
#it takes into account the perspective of the one being
#spoken to, and writes to s0
("dplmc_cap_troop_describes_troop_to_troop_s1",[
	(store_script_param, ":capitalization", 1),
	(store_script_param, ":speaker", 2),
	(store_script_param, ":described", 3),
	(store_script_param, ":listener", 4),

	(assign, ":save_reg0", reg0),
	(assign, ":save_reg1", reg1),

	(str_store_troop_name, s0, ":described"),

	(assign, reg0, ":capitalization"),
	(try_begin),
		(eq, ":described", ":listener"),
		(neq, ":speaker", ":listener"),
		(str_store_string, s0, "@{reg0?Y:y}ou"),
		(assign, reg0, 1),
	(else_try),
		(eq, ":described", ":speaker"),
		(str_store_string, s0, "@{reg0?M:m}yself"),
		(assign, reg0, 1),
	(else_try),
        (this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
        (is_between, ":described", heroes_begin, kingdom_ladies_end),
        (assign, ":speaker_relation", 0),
        (assign, ":speaker_relation_string", 0),
		(try_begin),
            (this_or_next|eq, ":speaker", "trp_player"),#only calculate family relationships for the player and heroes
            (is_between, ":speaker", heroes_begin, kingdom_ladies_end),
            (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":speaker"),
            (assign, ":speaker_relation", reg0),
            (assign, ":speaker_relation_string", reg1),
		(try_end),
		(assign, reg0, 0),
		(try_begin),
            (this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
            (is_between, ":described", heroes_begin, kingdom_ladies_end),
            (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":listener"),
		(try_end),
		(this_or_next|ge, ":speaker_relation", 1),
        (ge, reg0, 1),
		(try_begin),
			(eq, ":speaker_relation", reg0),
			(eq, reg1, ":speaker_relation_string"),
			(neq, ":speaker", ":listener"),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, ":speaker_relation_string"),
			(str_store_string, s1, "@{reg0?O:o}ur {s1} {s0}"),
		(else_try),
			(ge, ":speaker_relation", reg0),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, ":speaker_relation_string"),
			(str_store_string, s1, "@{reg0?M:m}y {s1} {s0}"),
		(else_try),
			(assign, reg0, ":capitalization"),
			(str_store_string, s1, reg1),
			(str_store_string, s1, "@{reg0?Y:y}our {s1} {s0}"),
		(try_end),
	(else_try),
		(str_store_string, s1, "str_s0"),
	(try_end),

	(assign, reg0, ":save_reg0"),
	(assign, reg1, ":save_reg1"),
	(str_store_string_reg, s0, s1),
]),

##"script_dplmc_helper_get_troop1_troop2_family_slot_aux"
##
## Helper function that does something specific that I want in
## script_dplmc_troop_get_family_relation_to_troop.
##
## Gets the slot value, but for troops that aren't trp_player
## and are not within (heroes_begin, heroes_end), values of "0"
## are transformed to -1.  Also gives a result of -1 (instead of
## an error) for negative troop IDs, which is what I want in
## this situation (otherwise I'd be explicitly checking this and
## setting the result to -1 if it was bad).
##
## Also, values equal to "active_npcs_including_player_begin" are
## transformed to "trp_player" (i.e. 0), to allow storing that
## value.
##
##INPUT:  arg1   :troop_1
##        arg2   :troop_2
##        arg3   :slot_no
##
##OUTPUT: reg0   value of slot for troop_1, or -1
##        reg1   value of slot for troop_2, or -1
("dplmc_helper_get_troop1_troop2_family_slot_aux",[
    (store_script_param, ":troop_1", 1),
    (store_script_param, ":troop_2", 2),
    (store_script_param, ":slot_no", 3),

    #(1) Get the value for the first troop into reg0
    (try_begin),
        #Negative numbers are placeholders for invalid family members
        (lt, ":troop_1", 0),
        (assign, reg0, -1),
    (else_try),
        #For active_npcs_including_player_begin, use the family slot from trp_player
        (eq, ":troop_1", active_npcs_including_player_begin),
        (troop_get_slot, reg0, "trp_player", ":slot_no"),
    (else_try),
        #Otherwise get the family member slot
        (troop_get_slot, reg0, ":troop_1", ":slot_no"),
        #However, for non-heroes, the memory might not be initialized,
        #so don't take a value of 0 at face-value.
        (eq, reg0, 0),
        (neg|is_between, ":troop_1", heroes_begin, kingdom_ladies_end),
        (neq, ":troop_1", "trp_player"),
        (assign, reg0, -1),
    (try_end),

    #Translate from active_npcs_including_player_begin to trp_player
    (try_begin),
        (eq, reg0, active_npcs_including_player_begin),
        (assign, reg0, "trp_player"),
    (try_end),

    #(2) Get the value for the second troop into reg1
    (try_begin),
        #Negative numbers are placeholders for invalid family members
        (lt, ":troop_2", 0),
        (assign, reg1, -1),
    (else_try),
        #For active_npcs_including_player_begin, use the family slot from trp_player
        (eq, ":troop_2", active_npcs_including_player_begin),
        (troop_get_slot, reg1, "trp_player", ":slot_no"),
    (else_try),
        #Otherwise get the family member slot
        (troop_get_slot, reg1, ":troop_2", ":slot_no"),
        #However, for non-heroes, the memory might not be initialized,
        #so don't take a value of 0 at face-value.
        (eq, reg1, 0),
        (neg|is_between, ":troop_2", heroes_begin, kingdom_ladies_end),
        (neq, ":troop_2", "trp_player"),
        (assign, reg1, -1),
    (try_end),

    #Translate from active_npcs_including_player_begin to trp_player
    (try_begin),
        (eq, reg1, active_npcs_including_player_begin),
        (assign, reg1, "trp_player"),
    (try_end),
]),

##"script_dplmc_estimate_center_weekly_income"
#
#  INPUT:  arg1   :center_no
# OUTPUT:  reg0   estimated value of weekly income
#
##now this estimate should work
("dplmc_estimate_center_weekly_income", [
    (store_script_param_1, ":center"),
    (call_script, "script_center_get_capital", ":center"),##moved it here
    (store_mul, reg0, reg49, 60),#normal tax rate
    (val_div, reg0, 100),
    (party_get_slot, ":center_tariffs", ":center", slot_center_accumulated_tariffs),
    (val_add, reg0, ":center_tariffs"),
]),

# "script_dplmc_get_closest_center_or_two"
# Input: arg1 = party_no
# Output: reg0 = center_no (closest)
#         reg1 = center_no2 (another close center or -1)
#
# If reg1 is non-negative, it should make some sense to say "<party_no> is
# between <reg0> and <reg1>".
#
# The way I do this is:
#   1.  Find the closest center to the party.
#   2.  Excluding the center from (1), find the closest center to the
#       party which is not closer to the center from (1) than it is to
#       the party.  (There might not be any centers matching this
#       description.)
#
# If the party is much closer to center_1 than center_2, I discard
# the second center.  (The rationale is that if I'm standing on my
# doorstep, it is be helpful to say "I am between my house and the
# grocery store".  It is less misleading to just say "I am near my
# house.")
("dplmc_get_closest_center_or_two",[
    (store_script_param_1, ":party_no"),
    (call_script, "script_get_closest_center", ":party_no"),#writes closest center to reg0
    (store_distance_to_party_from_party, ":distance_to_beat", ":party_no", reg0),
    (val_mul, ":distance_to_beat", 2),
    (val_add, ":distance_to_beat", 1),

    (assign, reg1, -1),
    (try_for_range, ":center_no", centers_begin, centers_end),
        (neq, ":center_no", reg0),
        (store_distance_to_party_from_party, ":party_to_center_distance", ":party_no", ":center_no"),
        (lt, ":party_to_center_distance", ":distance_to_beat"),
        (store_distance_to_party_from_party, ":center_to_center_distance", reg0, ":center_no"),
        (gt, ":center_to_center_distance", ":party_to_center_distance"),
        (assign, ":distance_to_beat", ":party_to_center_distance"),
        (assign, reg1, ":center_no"),
    (try_end),
]),
#script_cf_dplmc_battle_continuation
#new camera setup scripts, setting up other calls
("cf_dplmc_battle_continuation", [
    (eq, "$g_dplmc_battle_continuation", 0),
    (assign, ":num_allies", 0),
    (try_for_agents, ":agent"),
        (agent_is_ally, ":agent"),
        (agent_is_alive, ":agent"),
        (val_add, ":num_allies", 1),
    (try_end),
    (gt, ":num_allies", 0),
    (try_begin),
        (neq, "$enable_deahtcam", 0),
        (eq, "$g_dplmc_cam_activated", 0),
        #(store_mission_timer_a, "$g_dplmc_main_hero_fallen_seconds"),
        (assign, "$g_dplmc_cam_activated", "$g_dplmc_cam_default"),

        (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
        (store_add, ":string", "$g_dplmc_cam_activated", "str_camera_keyboard"),
        (val_sub, ":string", 1),
        (display_message, ":string"),
        # (display_message, "@To watch the fight you can use 'w, a, s, d, numpad_+/numpad_-' to move and 'numpad_1,2,3,4,6,8' to rotate the cam."),

        (try_begin),
            (eq, "$g_charge_on_player_death", 1),
            (get_player_agent_no, ":player_agent"),
            (agent_get_team, ":player_team", ":player_agent"),
            (set_show_messages, 0),
            (team_give_order, ":player_team", grc_everyone, mordr_charge),
            (team_give_order, ":player_team", grc_everyone, mordr_use_any_weapon),
            (team_give_order, ":player_team", grc_everyone, mordr_fire_at_will),
            (set_show_messages, 1),
        (try_end),

        (mission_cam_get_position, pos1), #Death pos
        (position_get_rotation_around_z, ":rot_z", pos1),

        (init_position, pos47),
        (position_copy_origin, pos47, pos1), #Copy X,Y,Z pos
        (position_rotate_z, pos47, ":rot_z"), #Copying X-Rotation is likely possible, but I haven't figured it out yet

        (mission_cam_set_mode, 1, 0, 0), #Manual?

        (try_begin), #auto-assign the closest agent
            (eq, "$g_dplmc_cam_activated", camera_follow),
            (call_script, "script_dmod_closest_agent"),
        (try_end),

        (mission_cam_set_position, pos47),
    (try_end),
]),

#script_dplmc_npc_morale
("dplmc_npc_morale",[
    (store_script_param_1, ":npc"),
    (store_script_param_2, ":mode"),
    (try_begin), #if we actually care
        (eq, ":mode", 1),
        (call_script, "script_npc_morale", ":npc"),
    (else_try), #we just want the numbers
        (troop_get_slot, ":morality_grievances", ":npc", slot_troop_morality_penalties),
        (troop_get_slot, ":personality_grievances", ":npc", slot_troop_personalityclash_penalties),
        (party_get_morale, ":party_morale", "p_main_party"),

        (store_sub, ":troop_morale", ":party_morale", ":morality_grievances"),
        (val_sub, ":troop_morale", ":personality_grievances"),
        (val_add, ":troop_morale", 50),

        # (assign, reg8, ":troop_morale"),

        (val_mul, ":troop_morale", 5),
        (val_div, ":troop_morale", 6),
        (val_clamp, ":troop_morale", 0, 101),
        (assign, reg0, ":troop_morale"),
    (try_end),
]),

#updates info_pages dynamically with DPLMC settings
("dplmc_update_info_settings",[
    # (try_begin),
    #     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
    #     (assign, ":setting", "str_dplmc_tax_low"),
    # (else_try),
    #     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
    #     (assign, ":setting", "str_dplmc_medium"),
    # (else_try),
    #     (eq, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
    #     (assign, ":setting", "str_dplmc_tax_high"),
    # (else_try),
    #     (assign, ":setting", "str_off"),
    # (try_end),
    # (str_store_string, s1, ":setting"),
    # (add_info_page_note_from_sreg, ip_dplmc_gold_changes, 1, "@{s1}", 0),

    # (try_begin),
    #     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
    #     (assign, ":setting", "str_dplmc_tax_low"),
    # (else_try),
    #     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
    #     (assign, ":setting", "str_dplmc_medium"),
    # (else_try),
    #     (eq, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
    #     (assign, ":setting", "str_dplmc_tax_high"),
    # (else_try),
    #     (assign, ":setting", "str_off"),
    # (try_end),
    # (str_store_string, s1, ":setting"),
    # (add_info_page_note_from_sreg, ip_dplmc_ai_changes, 1, "@{s1}", 0),

    (try_begin),
        (assign, "$g_autoloot_active", 1),
        (str_store_string, s1, "@Enabled"),
    (else_try),
        (str_store_string, s1, "@Disabled"),
    (try_end),
    (add_info_page_note_from_sreg, ip_dplmc_autoloot, 1, "@{s1}", 0),
]),

("dplmc_remove_disguise",[
    (try_begin),        #dckplmc: handle removing disguise here, bug with saving in-mission
        (gt, "$sneaked_into_town", disguise_none),
        (display_message, "@Removing disguise...", message_alert), #SB : colorize
        (try_begin),
            (eq, "$g_dplmc_player_disguise", 1),
            (set_show_messages, 0),
            #equipment is deposited back to inventory, it starts off blank
            (try_for_range, ":i_slot", ek_item_0, ek_food + 1),
                (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
                (neq, ":item", -1),
                (troop_get_inventory_slot_modifier, ":imod", "trp_player", ":i_slot"),
                (troop_add_item, "trp_random_town_sequence", ":item", ":imod"),
            (try_end),
            #less efficient, but merge and respect original player inventory's order
            (call_script, "script_move_inventory_and_gold", "trp_player", "trp_random_town_sequence", 0), #do not move gold
            (call_script, "script_dplmc_copy_inventory", "trp_random_town_sequence", "trp_player"),
            (call_script, "script_troop_transfer_gold", "trp_random_town_sequence", "trp_player", 0), #move remaining gold now
            (set_show_messages, 1),
        (try_end),
        (assign, "$sneaked_into_town", disguise_none),
    (try_end),
]),
]
