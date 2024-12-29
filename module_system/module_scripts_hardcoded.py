# -*- coding: cp1254 -*-
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

scripts_hardcoded = [
# script_game_start
# This script is called when a new game is started
# INPUT: none
("game_start",[

    (troop_set_slot, "trp_global_variables", g_iazyges_event, 0),#not triggered yet

    #default starting year
    (troop_set_slot, "trp_global_variables", g_starting_year, 63),

    #for cheats
    (troop_set_slot, "trp_global_variables", g_is_dev, 1),
    (assign, "$g_campaign_type", g_campaign_story_rome),#campaign type

    (troop_set_slot, "trp_household_villa", slot_troop_spouse, "scn_domus_mare_interior"),#for domus mare scene upgrade

    (assign, reg62, 0),#used for script_view_party_members
    (quest_set_slot, "qst_olympic_games", slot_quest_dont_give_again_remaining_days, 240),

    (call_script, "script_update_party_creation_random_limits"),

    ##freelancer variables
    (assign, "$enlisted_party", -1),
    (assign, "$g_charge_on_player_death", 1),
    (assign, "$can_sacrific", 1),

    (assign, "$player_piety", 100),

    (assign, "$can_spawn_commoners", 0),
    ##for events
    (assign, "$senate_events", 0),

    (assign, "$g_horses_are_avaliable", 10), # horse culling

    #for slave treatment
    (assign, "$g_slave_manu", 1),
    (assign, "$g_slave_treatment", 0),
    #formation
    (assign, "$form_ai_autorotate", 1),

    (assign, "$g_corruption_check", ACAN_CORRUPT_SAVE_CHECK),#check if save is corrupted
    (troop_set_slot, "trp_global_variables", g_corruption_check, ACAN_CORRUPT_SAVE_CHECK),

    (assign, "$g_dancers", 0),
    #new special quests
    (assign, "$slave_revolt", 0),
    ##for primitive bank system
    # (assign, "$g_player_bank", 0),
    #(assign, "$g_eagle", 0),
    ##some settings
    (assign, "$g_governor_appointment_message", 0),
    (assign, "$g_show_senate_meeting", 0),
    (assign, "$g_autoloot_active", 1),
    (assign, "$show_truce_expired", 0),
    (assign, "$show_raid_messages", 0),
    (assign, "$use_player_auxiliary", 1), #set as default now
    (assign, "$vc_wounds_on", 1),
    (assign, "$g_gore_on", 1),
    (assign, "$g_charge_on", 1),
    (assign, "$moralep_on", 1),
    (assign, "$g_love_messages_on", 0),
    (assign, "$g_body_guard_on", 1),

    ##reinforcement numbers
    (assign, "$defender_threshold", 40),
    #for sieges:
    (assign, "$reduce_factor", 1),

    ##moral options
    (assign, "$moral_shock", 45),             #was 30 in vc
    (assign, "$battle_ratio_multiple", 6000), #was 7000
    (assign, "$agent_run_away_multiplier", 10), #was 7000
    (assign, "$dead_effect_on_killer", 1), #was 0
    (assign, "$dead_effect_on_ally", -4), #was -4
    (assign, "$more_lose_leader", 1), #was 1
    (assign, "$ranged_penality", 1),
    (assign, "$moral_recovery", 1),
    (assign, "$debug_moral", 0),

    (assign, "$event_oneuse", 0),
    (assign, "$foragers_a", 0), #foragers ok
    (assign, "$g_player_rent", 0),
    (assign, "$g_player_villa_costs", 0),

    # (assign, "$g_riddle", 0),
    (assign, "$nero_events", 0),
   # (assign, "$FormAI_AI_no_defense", 0),
    (assign, "$players_ship", -1),
    (assign, "$conducted_census", -1),
    (assign, "$g_timer", -1),
    (assign, "$g_peace_ask", 0),
    (assign, "$templelooted", 0),
    (assign, "$g_rank", 0),
    (assign, "$g_heir_of_rome", -1),
    (assign, "$jewish_revolt", 0),
    (assign, "$edict1", 0),##das ist die abschaffen von diesen petitionen
    (assign, "$edict2", 1),##das ist das sitten gesetz von kaiser augustus
    (assign, "$edict3", 0),##das ist das gesetz womit es verboten wird christen zu verfolgen
    (assign, "$edict4", 0),##das ist das gesetz womit christenverfolgung zur staatsangelegenheit wird
    (assign, "$edict5", 0),##das ist das gesetz womit allen freien reichsbewohnern das bugerrecht verliehen wird
    (assign, "$edict6", 0),##reichsverfassung + nachfolgegesetz
    ##jetzt kommen ein paar gesetze aus republikanischer Zeit
    (assign, "$edict7", 1),##Lex frumentaria et agraria: maximaler getreide preis: 100 denars per unit,
               ## this means 1000 denars for scenter price slot,
    (assign, "$edict8", 1),##Lex militaris minimal alter von Rekruten ist 17 Jahre
    (assign, "$edict9", 0),##Alimenta von trajan
    (assign, "$edict10",0),##rename month
    (assign, "$edict11", 1), # manumisson tax
    (assign, "$g_libelli", 0),
    (assign, "$g_civil_war", 0),
    (assign, "$wounded_today", 0),
    (assign, "$g_judicio", 0), ## for special emperor events

    (assign, "$g_random_eventnorepit", 0),
    # (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
    # (assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
    (assign, "$g_dplmc_lord_recycling", 1),
    (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),

    (call_script, "script_dplmc_update_info_settings"),##to display the option in game concepts

    (assign,"$player_ambushed",0),
    (assign, "$gwenny", -1),
    (assign, "$g_last_affiliate_attempt", 0),
    (assign, "$g_player_affiliated_troop", -1),

    (assign,"$g_nino_varon",0),##the children of the player
    (assign,"$g_nina_chica",0),
    (assign, "$g_spouse_embarazada", 0), #spouse prego
    (options_set_battle_size, 0),

    (assign, "$first_time", 0),	#squelch compiler warnings

    (assign, "$praefectus_urbani", "trp_tigellinus"),

    (assign, "$g_is_emperor", 0), # wenn man kaiser wird

    (assign, "$g_custom_banner_new_game", 1), #new game
    (assign, "$g_realistic_wounding", 1), #new game

    (assign, "$g_unrest", 5), # how stable the roman empire is
    # (assign, "$g_support", 0), #1 menas player get support form a lord, 2 means lord gets support from player. in g_who is stored who was supported
    (assign, "$form_ai_off", 0),

    (assign, "$season", 1),#add game start it is summer
    (assign, "$g_fire", 0),#create fire of roma

    #SB : default parameters for post-battle continuation
    (call_script, "script_setup_camera_keys"),
    (assign, "$g_dplmc_cam_default", camera_keyboard),
    (assign, "$g_dplmc_player_disguise", disguise_pilgrim),
    # (assign, "$g_dplmc_charge_when_dead", 0),

    (try_for_range, ":edible", "itm_raw_date_fruit", food_end),
        (neq, ":edible", "itm_furs"),
        (item_set_slot, ":edible", slot_item_edible, 1),
    (try_end),

    (assign, "$g_player_luck", 200),
    (assign, "$g_player_party_icon", -1),

    (try_for_range, ":item", legendary_items_begin, legendary_items_end),
        (item_set_slot, ":item", slot_item_discovered, -1),
    (try_end),

    (call_script, "script_initialize_banner_info"),
    (call_script, "script_initialize_item_info"),
    (call_script, "script_initialize_factions"),

    #set slots
    (troop_set_slot, "trp_player", slot_troop_influence, 0),#influence test
    (troop_set_slot, "trp_player", slot_troop_occupation, slto_kingdom_hero),

    (try_for_range, ":npc", active_npcs_including_player_begin, kingdom_ladies_end),
        (try_begin),
            (eq, ":npc", "trp_kingdom_heroes_including_player_begin"),
            (assign, ":npc", "trp_player"),
        (try_end),
        (troop_set_slot, ":npc",slot_troop_aux, -1),
        (troop_set_slot, ":npc",slot_troop_legion, -1),
        (troop_set_slot, ":npc",slot_troop_govern, -1),
        (troop_set_slot, ":npc", slot_troop_tortured_by, -1),
        (troop_set_slot, ":npc", slot_troop_spouse, -1),

        (troop_set_slot, ":npc", slot_troop_father, -1),
        (troop_set_slot, ":npc", slot_troop_mother, -1),
        (troop_set_slot, ":npc", slot_troop_guardian, -1),
        (troop_set_slot, ":npc", slot_troop_betrothed, -1),
        (troop_set_slot, ":npc", slot_troop_prisoner_of_party, -1),
        (troop_set_slot, ":npc", slot_lady_last_suitor, -1),
        (troop_set_slot, ":npc", slot_troop_stance_on_faction_issue, -1),
        (troop_set_slot, ":npc", slot_troop_temp, 0),
        (troop_set_slot, ":npc", slot_troop_lover, -1),

        (troop_set_slot, ":npc", slot_troop_lover_found, -1),
        (troop_set_slot, ":npc", slot_troop_flirted_with, 0),

        (troop_set_slot, ":npc", slot_troop_assassin_attempt, 0),
        (troop_set_slot, ":npc", slot_troop_banner_scene_prop, 0),
        (store_random_in_range, ":decision_seed", 0, 10000),
        (troop_set_slot, ":npc", slot_troop_set_decision_seed, ":decision_seed"),	#currently not used
        (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":decision_seed"),	#currently not used, holds for at least 24 hours

        (neq, ":npc", "trp_player"),
        (troop_set_slot, ":npc", slot_troop_leaded_party, -1),
        (try_begin),
            (store_faction_of_troop, ":npc_faction", ":npc"),
            (is_between, ":npc_faction", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_get_slot, ":culture", ":npc_faction", slot_faction_culture),
            (troop_set_slot, ":npc", slot_troop_culture, ":culture"),
        (try_end),
        ##construct normal distribution
        (store_random_in_range, ":trade_skill", -6, 6),# -5 to 5
        (store_random_in_range, reg0, -6, 6),# -5 to 5
        (val_add, ":trade_skill", reg0),
        (val_abs, ":trade_skill"),
        (troop_raise_skill, ":npc", "skl_trade", ":trade_skill"),

        (store_random_in_range, ":engineer_skill", -6, 6),# -5 to 5
        (store_random_in_range, reg0, -6, 6),# -5 to 5
        (val_add, ":engineer_skill", reg0),
        (val_abs, ":engineer_skill"),
        (troop_raise_skill, ":npc", "skl_engineer", ":engineer_skill"),
    (try_end),
    #saqueo para centers. Siege warfare
    (try_for_range, ":center_no", centers_begin, centers_end),
        (party_set_slot,":center_no",slot_center_blockaded,0),#siege stuff
        (party_set_slot,":center_no",slot_center_blockaded_time,0),
        (party_set_slot, ":center_no", slot_center_mantlets_placed, 0),
        (party_set_slot,":center_no",slot_center_ladder_time,0),
        (party_set_slot,":center_no",slot_center_latrines,0),
        (party_set_slot,":center_no",slot_center_infiltration_type,0),
        (party_set_slot,":center_no",slot_center_pursue,0),##for christian
        (party_set_slot,":center_no",slot_crucified_slave_icon,-1),#for christian
        (try_for_range, ":buildings", village_improvements_begin, walled_center_improvements_end),
            (party_set_slot, ":center_no",":buildings", 0),
        (try_end),
    (try_end),

    (call_script, "script_initialize_aristocracy"),
    (call_script, "script_initialize_npcs"),
    (assign, "$disable_npc_complaints", 0),
    (assign, "$disable_companions_leaving", 0),
    #NPC companion changes end

    # Setting random feast time
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (store_random_in_range, ":last_feast_time", 0, 312), #240 + 72
        (val_mul, ":last_feast_time", -1),
        (faction_set_slot, ":faction_no", slot_faction_last_feast_start_time, ":last_feast_time"),
    (try_end),

    # Setting the random town sequence:
    (store_sub, ":num_towns", towns_end, towns_begin),
    (assign, ":num_iterations", ":num_towns"),
    (try_for_range, ":cur_town_no", 0, ":num_towns"),
        (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", -1),
    (try_end),
    (assign, ":cur_town_no", 0),
    (try_for_range, ":unused", 0, ":num_iterations"),
        (store_random_in_range, ":random_no", 0, ":num_towns"),
        (assign, ":is_unique", 1),
        (try_for_range, ":cur_town_no_2", 0, ":num_towns"),
            (troop_slot_eq, "trp_random_town_sequence", ":cur_town_no_2", ":random_no"),
            (assign, ":is_unique", 0),
        (try_end),
        (try_begin),
            (eq, ":is_unique", 1),
            (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", ":random_no"),
            (val_add, ":cur_town_no", 1),
        (else_try),
            (val_add, ":num_iterations", 1),
        (try_end),
    (try_end),
    (call_script, "script_initialize_faction_troop_types"),
    ##diplomacy begin
    (call_script, "script_dplmc_init_domestic_policy"),
    ##diplomacy end

    (try_for_range, ":fac", kingdoms_begin, kingdoms_end),
        (faction_set_slot, ":fac", slot_faction_player_tributary, -1),
    (try_end),
    (try_for_range, ":fac", minor_kingdoms_begin, minor_kingdoms_end),
        (faction_set_slot, ":fac", slot_faction_player_tributary, -1),
    (try_end),
# Towns:
    (try_for_range, ":item_no", trade_goods_begin, trade_goods_end),
        (store_sub, ":offset", ":item_no", trade_goods_begin),
        (val_add, ":offset", slot_town_trade_good_prices_begin),
        (try_for_range, ":center_no", centers_begin, centers_end),
            (party_set_slot, ":center_no", ":offset", average_price_factor), #1000
        (try_end),
    (try_end),

    (call_script, "script_initialize_trade_routes"),
	  (call_script, "script_initialize_sea_trade_routes"), ###Seatrade Marker
    (call_script, "script_initialize_town_arena_info"),
    #start some tournaments
    (try_for_range, ":town_no", towns_begin, towns_end),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 20),
        (store_random_in_range, ":random_days", 12, 15),
        (party_set_slot, ":town_no", slot_town_has_tournament, ":random_days"),
    (try_end),

    ##reatia et noricum
    (call_script, "script_give_village_to_center", "p_village_241", "p_castle_73"),
    (call_script, "script_give_village_to_center", "p_village_240", "p_castle_72"),

    (call_script, "script_give_village_to_center", "p_village_75", "p_castle_9"),
    (call_script, "script_give_village_to_center", "p_village_78", "p_castle_9"),
    (call_script, "script_give_village_to_center", "p_village_195", "p_castle_4"),
    (call_script, "script_give_village_to_center", "p_village_17", "p_castle_12"),
    (call_script, "script_give_village_to_center", "p_village_8", "p_castle_39"),
    ##illyricum
    (call_script, "script_give_village_to_center", "p_village_248", "p_castle_78"),
    (call_script, "script_give_village_to_center", "p_village_74", "p_castle_35"),
    (call_script, "script_give_village_to_center", "p_village_160", "p_castle_35"),
    (call_script, "script_give_village_to_center", "p_village_62", "p_castle_20"),
    #thracia
    (call_script, "script_give_village_to_center", "p_village_86", "p_castle_29"),
    (call_script, "script_give_village_to_center", "p_village_158", "p_castle_13"),
    (call_script, "script_give_village_to_center", "p_village_107", "p_castle_15"),

    (call_script, "script_give_village_to_center", "p_village_42", "p_town_16"),

    ##greece
    (call_script, "script_give_village_to_center", "p_village_50", "p_town_35"),
    (call_script, "script_give_village_to_center", "p_village_156", "p_town_35"),
    (call_script, "script_give_village_to_center", "p_village_33", "p_town_35"),

    (call_script, "script_give_village_to_center", "p_village_159", "p_town_36"),
    (call_script, "script_give_village_to_center", "p_village_69", "p_town_36"),
    (call_script, "script_give_village_to_center", "p_village_155", "p_town_36"),

    (call_script, "script_give_village_to_center", "p_village_161", "p_town_37"),
    (call_script, "script_give_village_to_center", "p_village_162", "p_town_37"),
    (call_script, "script_give_village_to_center", "p_village_71", "p_town_37"),
    (call_script, "script_give_village_to_center", "p_village_73", "p_town_37"),
    ##byzantium
    (call_script, "script_give_village_to_center", "p_village_41", "p_town_13"),
    ##anatolia
    (call_script, "script_give_village_to_center", "p_village_65", "p_town_38"),
    (call_script, "script_give_village_to_center", "p_village_165", "p_town_38"),
    (call_script, "script_give_village_to_center", "p_village_45", "p_town_38"),
    (call_script, "script_give_village_to_center", "p_village_52", "p_town_38"),

    (call_script, "script_give_village_to_center", "p_village_81", "p_town_8"),
    (call_script, "script_give_village_to_center", "p_village_63", "p_town_8"),
    (call_script, "script_give_village_to_center", "p_village_94", "p_town_8"),

    (call_script, "script_give_village_to_center", "p_village_90", "p_town_10"),
    (call_script, "script_give_village_to_center", "p_village_88", "p_town_10"),
    (call_script, "script_give_village_to_center", "p_village_85", "p_town_10"),

    (call_script, "script_give_village_to_center", "p_village_166", "p_castle_31"),
    (call_script, "script_give_village_to_center", "p_village_43", "p_castle_27"),
    (call_script, "script_give_village_to_center", "p_village_157", "p_castle_28"),
    (call_script, "script_give_village_to_center", "p_village_157", "p_castle_28"),
    ##syria
    (call_script, "script_give_village_to_center", "p_village_201", "p_town_22"),
    (call_script, "script_give_village_to_center", "p_village_163", "p_town_22"),
    (call_script, "script_give_village_to_center", "p_village_199", "p_town_22"),
    (call_script, "script_give_village_to_center", "p_village_110", "p_town_22"),
    ##judea
    (call_script, "script_give_village_to_center", "p_village_51", "p_castle_45"),
    (call_script, "script_give_village_to_center", "p_village_100", "p_castle_46"),

    (call_script, "script_give_village_to_center", "p_village_98", "p_town_19"),
    (call_script, "script_give_village_to_center", "p_village_97", "p_town_19"),
    (call_script, "script_give_village_to_center", "p_village_96", "p_town_19"),

    (call_script, "script_give_village_to_center", "p_village_109", "p_castle_44"),
    (call_script, "script_give_village_to_center", "p_village_164", "p_castle_47"),
    #persia
    (call_script, "script_give_village_to_center", "p_village_243", "p_castle_74"),
    (call_script, "script_give_village_to_center", "p_village_244", "p_castle_75"),
    (call_script, "script_give_village_to_center", "p_village_245", "p_castle_76"),
    (call_script, "script_give_village_to_center", "p_village_247", "p_castle_77"),

    ###egypt
    (call_script, "script_give_village_to_center", "p_village_95", "p_town_20"),
    (call_script, "script_give_village_to_center", "p_village_202", "p_town_20"),
    (call_script, "script_give_village_to_center", "p_village_203", "p_town_20"),
    (call_script, "script_give_village_to_center", "p_village_205", "p_town_20"),

    (call_script, "script_give_village_to_center", "p_village_204", "p_town_48"),
    (call_script, "script_give_village_to_center", "p_village_207", "p_town_48"),
    (call_script, "script_give_village_to_center", "p_village_206", "p_town_48"),
    (call_script, "script_give_village_to_center", "p_village_242", "p_town_48"),
    ##cyrene
    (call_script, "script_give_village_to_center", "p_village_102", "p_castle_41"),
    (call_script, "script_give_village_to_center", "p_village_108", "p_castle_41"),
    ##africa
    (call_script, "script_give_village_to_center", "p_village_137", "p_town_29"),
    (call_script, "script_give_village_to_center", "p_village_135", "p_town_29"),
    (call_script, "script_give_village_to_center", "p_village_134", "p_town_29"),

    (call_script, "script_give_village_to_center", "p_village_133", "p_town_28"),
    (call_script, "script_give_village_to_center", "p_village_103", "p_town_28"),
    (call_script, "script_give_village_to_center", "p_village_132", "p_town_28"),
    (call_script, "script_give_village_to_center", "p_village_91", "p_town_28"),

    (call_script, "script_give_village_to_center", "p_village_131", "p_castle_43"),

    (call_script, "script_give_village_to_center", "p_village_105", "p_town_21"),
    (call_script, "script_give_village_to_center", "p_village_106", "p_town_21"),
    (call_script, "script_give_village_to_center", "p_village_48", "p_town_21"),
    (call_script, "script_give_village_to_center", "p_village_104", "p_town_21"),
    #gaul
    (call_script, "script_give_village_to_center", "p_village_39", "p_town_4"),
    (call_script, "script_give_village_to_center", "p_village_36", "p_town_4"),
    (call_script, "script_give_village_to_center", "p_village_197", "p_town_4"),
    (call_script, "script_give_village_to_center", "p_village_30", "p_town_4"),

    (call_script, "script_give_village_to_center", "p_village_31", "p_town_46"),
    (call_script, "script_give_village_to_center", "p_village_32", "p_town_46"),
    (call_script, "script_give_village_to_center", "p_village_35", "p_town_46"),
    (call_script, "script_give_village_to_center", "p_village_196", "p_town_46"),

    (call_script, "script_give_village_to_center", "p_village_34", "p_town_2"),
    (call_script, "script_give_village_to_center", "p_village_72", "p_town_2"),
    (call_script, "script_give_village_to_center", "p_village_15", "p_town_2"),
    (call_script, "script_give_village_to_center", "p_village_38", "p_town_2"),

    (call_script, "script_give_village_to_center", "p_village_77", "p_town_12"),
    (call_script, "script_give_village_to_center", "p_village_82", "p_town_12"),
    (call_script, "script_give_village_to_center", "p_village_54", "p_town_12"),
    (call_script, "script_give_village_to_center", "p_village_70", "p_town_12"),
    (call_script, "script_give_village_to_center", "p_village_47", "p_town_12"),

    (call_script, "script_give_village_to_center", "p_village_27", "p_castle_16"),
    (call_script, "script_give_village_to_center", "p_village_61", "p_castle_24"),
    (call_script, "script_give_village_to_center", "p_village_38", "p_castle_10"),
    (call_script, "script_give_village_to_center", "p_village_68", "p_castle_10"),
    (call_script, "script_give_village_to_center", "p_village_84", "p_castle_34"),

    ##spain
    (call_script, "script_give_village_to_center", "p_village_24", "p_town_3"),
    (call_script, "script_give_village_to_center", "p_village_23", "p_town_3"),
    (call_script, "script_give_village_to_center", "p_village_145", "p_town_3"),
    (call_script, "script_give_village_to_center", "p_village_144", "p_town_3"),

    (call_script, "script_give_village_to_center", "p_village_143", "p_town_31"),
    (call_script, "script_give_village_to_center", "p_village_142", "p_town_31"),
    (call_script, "script_give_village_to_center", "p_village_4", "p_town_31"),
    (call_script, "script_give_village_to_center", "p_village_2", "p_town_31"),

    (call_script, "script_give_village_to_center", "p_village_141", "p_town_30"),
    (call_script, "script_give_village_to_center", "p_village_6", "p_town_30"),
    (call_script, "script_give_village_to_center", "p_village_140", "p_town_30"),
    (call_script, "script_give_village_to_center", "p_village_139", "p_town_30"),

    (call_script, "script_give_village_to_center", "p_village_146", "p_castle_3"),
    (call_script, "script_give_village_to_center", "p_village_138", "p_castle_2"),
    (call_script, "script_give_village_to_center", "p_village_7", "p_castle_1"),
    (call_script, "script_give_village_to_center", "p_village_229", "p_castle_1"),

    (call_script, "script_give_village_to_center", "p_village_14", "p_town_32"),
    (call_script, "script_give_village_to_center", "p_village_147", "p_town_32"),
    (call_script, "script_give_village_to_center", "p_village_148", "p_town_32"),
    (call_script, "script_give_village_to_center", "p_village_13", "p_town_32"),
    (call_script, "script_give_village_to_center", "p_village_29", "p_town_32"),

    ###italy
    (call_script, "script_give_village_to_center", "p_village_209", "p_town_5"),
    (call_script, "script_give_village_to_center", "p_village_210", "p_town_5"),
    (call_script, "script_give_village_to_center", "p_village_60", "p_town_5"),

    (call_script, "script_give_village_to_center", "p_village_211", "p_castle_11"),

    (call_script, "script_give_village_to_center", "p_village_152", "p_town_6"),
    (call_script, "script_give_village_to_center", "p_village_153", "p_town_6"),
    (call_script, "script_give_village_to_center", "p_village_58", "p_town_6"),

    (call_script, "script_give_village_to_center", "p_village_154", "p_town_34"),
    (call_script, "script_give_village_to_center", "p_village_57", "p_town_34"),
    (call_script, "script_give_village_to_center", "p_village_150", "p_town_34"),

    (call_script, "script_give_village_to_center", "p_village_56", "p_town_33"),
    (call_script, "script_give_village_to_center", "p_village_149", "p_town_33"),
    (call_script, "script_give_village_to_center", "p_village_151", "p_town_33"),

    ##sicily
    (call_script, "script_give_village_to_center", "p_village_53", "p_castle_6"),
    ##britannia
    (call_script, "script_give_village_to_center", "p_village_10", "p_castle_23"),

    (call_script, "script_give_village_to_center", "p_village_181", "p_town_43"),
    (call_script, "script_give_village_to_center", "p_village_180", "p_town_43"),
    (call_script, "script_give_village_to_center", "p_village_5", "p_town_43"),

    (call_script, "script_give_village_to_center", "p_village_182", "p_town_1"),

    (call_script, "script_give_village_to_center", "p_village_183", "p_castle_57"),

    (call_script, "script_give_village_to_center", "p_village_55", "p_town_1"),
    # (call_script, "script_give_village_to_center", "p_village_9", "p_town_1"),

    (call_script, "script_give_village_to_center", "p_village_184", "p_town_44"),
    (call_script, "script_give_village_to_center", "p_village_185", "p_town_44"),
    (call_script, "script_give_village_to_center", "p_village_186", "p_town_44"),

    (call_script, "script_give_village_to_center", "p_village_115", "p_castle_58"),
    # (call_script, "script_give_village_to_center", "p_village_116", "p_town_24"),
    (call_script, "script_give_village_to_center", "p_village_117", "p_town_24"),
    (call_script, "script_give_village_to_center", "p_village_118", "p_town_24"),

    (call_script, "script_give_village_to_center", "p_village_1", "p_castle_14"),
    (call_script, "script_give_village_to_center", "p_village_3", "p_castle_5"),
    ##Germania
    (call_script, "script_give_village_to_center", "p_village_26", "p_castle_36"),
    (call_script, "script_give_village_to_center", "p_village_46", "p_castle_8"),
    (call_script, "script_give_village_to_center", "p_village_66", "p_castle_49"),
    (call_script, "script_give_village_to_center", "p_village_190", "p_town_15"),
    (call_script, "script_give_village_to_center", "p_village_59", "p_castle_22"),

    (call_script, "script_give_village_to_center", "p_village_222", "p_castle_52"),
    (call_script, "script_give_village_to_center", "p_village_191", "p_castle_51"),
    (call_script, "script_give_village_to_center", "p_village_16", "p_castle_50"),

    (call_script, "script_give_village_to_center", "p_village_193", "p_castle_22"),
    (call_script, "script_give_village_to_center", "p_village_192", "p_castle_33"),
    (call_script, "script_give_village_to_center", "p_village_194", "p_castle_53"),
    (call_script, "script_give_village_to_center", "p_village_220", "p_castle_54"),

    (call_script, "script_give_village_to_center", "p_village_101", "p_castle_32"),

    (call_script, "script_give_village_to_center", "p_village_208", "p_town_15"),
    (call_script, "script_give_village_to_center", "p_village_189", "p_town_15"),
    (call_script, "script_give_village_to_center", "p_village_64", "p_town_15"),

    (call_script, "script_give_village_to_center", "p_village_188", "p_town_45"),
    (call_script, "script_give_village_to_center", "p_village_187", "p_town_45"),
    (call_script, "script_give_village_to_center", "p_village_80", "p_town_45"),
    (call_script, "script_give_village_to_center", "p_village_79", "p_town_45"),

    (call_script, "script_give_village_to_center", "p_village_113", "p_town_23"),
    (call_script, "script_give_village_to_center", "p_village_112", "p_town_23"),
    (call_script, "script_give_village_to_center", "p_village_225", "p_town_23"),

    #east germania
    (call_script, "script_give_village_to_center", "p_village_111", "p_town_49"),
    (call_script, "script_give_village_to_center", "p_village_223", "p_town_49"),
    (call_script, "script_give_village_to_center", "p_village_224", "p_town_49"),
    (call_script, "script_give_village_to_center", "p_village_114", "p_castle_60"),

    ##Dacia
    (call_script, "script_give_village_to_center", "p_village_67", "p_town_9"),
    (call_script, "script_give_village_to_center", "p_village_49", "p_town_9"),
    (call_script, "script_give_village_to_center", "p_village_92", "p_town_9"),

    (call_script, "script_give_village_to_center", "p_village_20", "p_town_42"),
    (call_script, "script_give_village_to_center", "p_village_176", "p_town_42"),
    (call_script, "script_give_village_to_center", "p_village_40", "p_town_42"),

    (call_script, "script_give_village_to_center", "p_village_89", "p_town_11"),
    (call_script, "script_give_village_to_center", "p_village_178", "p_town_11"),
    (call_script, "script_give_village_to_center", "p_village_177", "p_town_11"),
    (call_script, "script_give_village_to_center", "p_village_21", "p_town_11"),

    (call_script, "script_give_village_to_center", "p_village_19", "p_castle_19"),
    (call_script, "script_give_village_to_center", "p_village_179", "p_castle_18"),
    (call_script, "script_give_village_to_center", "p_village_11", "p_castle_17"),
    (call_script, "script_give_village_to_center", "p_village_18", "p_castle_7"),
    (call_script, "script_give_village_to_center", "p_village_22", "p_castle_37"),
    #steppe
    (call_script, "script_give_village_to_center", "p_village_238", "p_town_50"),
    (call_script, "script_give_village_to_center", "p_village_237", "p_town_50"),
    (call_script, "script_give_village_to_center", "p_village_236", "p_town_50"),
    (call_script, "script_give_village_to_center", "p_village_234", "p_castle_70"),
    (call_script, "script_give_village_to_center", "p_village_233", "p_castle_69"),
    (call_script, "script_give_village_to_center", "p_village_232", "p_castle_68"),

    (call_script, "script_give_village_to_center", "p_village_37", "p_castle_21"),

    (call_script, "script_give_village_to_center", "p_village_12", "p_town_7"),
    (call_script, "script_give_village_to_center", "p_village_25", "p_town_7"),
    (call_script, "script_give_village_to_center", "p_village_28", "p_town_7"),

    (call_script, "script_give_village_to_center", "p_village_122", "p_town_25"),
    (call_script, "script_give_village_to_center", "p_village_121", "p_town_25"),
    (call_script, "script_give_village_to_center", "p_village_120", "p_castle_59"),
    (call_script, "script_give_village_to_center", "p_village_230", "p_castle_66"),
    (call_script, "script_give_village_to_center", "p_village_9", "p_town_25"),
    #  (call_script, "script_give_village_to_center", "p_village_119", "p_town_25"),

    (call_script, "script_give_village_to_center", "p_village_175", "p_town_41"),
    (call_script, "script_give_village_to_center", "p_village_174", "p_town_41"),

    (call_script, "script_give_village_to_center", "p_village_125", "p_town_26"),
    (call_script, "script_give_village_to_center", "p_village_123", "p_town_26"),
    (call_script, "script_give_village_to_center", "p_village_173", "p_town_26"),

    (call_script, "script_give_village_to_center", "p_village_221", "p_castle_56"),

    (call_script, "script_give_village_to_center", "p_village_239", "p_castle_71"),

    ##armenia
    (call_script, "script_give_village_to_center", "p_village_214", "p_town_14"),
    (call_script, "script_give_village_to_center", "p_village_126", "p_town_14"),

    (call_script, "script_give_village_to_center", "p_village_213", "p_town_18"),
    (call_script, "script_give_village_to_center", "p_village_87", "p_town_18"),
    (call_script, "script_give_village_to_center", "p_village_215", "p_town_18"),

    (call_script, "script_give_village_to_center", "p_village_124", "p_castle_25"),
    (call_script, "script_give_village_to_center", "p_village_212", "p_castle_38"),
    (call_script, "script_give_village_to_center", "p_village_44", "p_castle_26"),
    ##parthia
    (call_script, "script_give_village_to_center", "p_village_76", "p_town_17"),
    (call_script, "script_give_village_to_center", "p_village_83", "p_town_17"),
    (call_script, "script_give_village_to_center", "p_village_235", "p_town_17"),

    (call_script, "script_give_village_to_center", "p_village_167", "p_town_40"),
    (call_script, "script_give_village_to_center", "p_village_168", "p_town_40"),
    (call_script, "script_give_village_to_center", "p_village_99", "p_town_40"),
    (call_script, "script_give_village_to_center", "p_village_171", "p_town_40"),

    (call_script, "script_give_village_to_center", "p_village_130", "p_town_27"),
    (call_script, "script_give_village_to_center", "p_village_172", "p_castle_65"),
    (call_script, "script_give_village_to_center", "p_village_127", "p_town_27"),
    (call_script, "script_give_village_to_center", "p_village_128", "p_castle_55"),
    (call_script, "script_give_village_to_center", "p_village_129", "p_town_27"),
    (call_script, "script_give_village_to_center", "p_village_246", "p_town_27"),

    (call_script, "script_give_village_to_center", "p_village_93", "p_town_39"),
    (call_script, "script_give_village_to_center", "p_village_169", "p_town_39"),
    (call_script, "script_give_village_to_center", "p_village_136", "p_town_39"),

    (call_script, "script_give_village_to_center", "p_village_216", "p_castle_48"),
    (call_script, "script_give_village_to_center", "p_village_170", "p_castle_30"),

    (call_script, "script_give_village_to_center", "p_village_198", "p_castle_42"),
    (call_script, "script_give_village_to_center", "p_village_200", "p_castle_40"),

    (call_script, "script_give_village_to_center", "p_village_217", "p_town_47"),
    (call_script, "script_give_village_to_center", "p_village_218", "p_town_47"),
    (call_script, "script_give_village_to_center", "p_village_219", "p_town_47"),

    (call_script, "script_give_village_to_center", "p_village_226", "p_castle_61"),
    (call_script, "script_give_village_to_center", "p_village_227", "p_castle_62"),
    (call_script, "script_give_village_to_center", "p_village_73", "p_castle_63"),
    (call_script, "script_give_village_to_center", "p_village_228", "p_castle_64"),
    (call_script, "script_give_village_to_center", "p_village_231", "p_castle_67"),

    (call_script, "script_give_village_to_center", "p_village_250", "p_town_51"),
    (call_script, "script_give_village_to_center", "p_village_249", "p_town_51"),
    (call_script, "script_give_village_to_center", "p_village_254", "p_town_51"),
    (call_script, "script_give_village_to_center", "p_village_253", "p_town_52"),
    (call_script, "script_give_village_to_center", "p_village_252", "p_town_52"),
    (call_script, "script_give_village_to_center", "p_village_251", "p_town_52"),

    (call_script, "script_give_village_to_center", "p_village_255", "p_castle_79"),
    (call_script, "script_give_village_to_center", "p_village_256", "p_castle_80"),

	  ##Holy Sides
    (call_script, "script_init_barbarian_holy_sides"),
   # Towns (loop)
    (try_for_range, ":town_no", towns_begin, towns_end),#ich verwend die selben scenen, sonst werd ich wahnsinnig
        (store_sub, ":offset", ":town_no", towns_begin),
        (party_set_slot,":town_no", slot_party_type, spt_town),
        (store_add, ":cur_object_no", "trp_town_1_mayor", ":offset"),
        (try_begin),
            (neg|is_between, ":cur_object_no", mayors_begin, mayors_end),
            (display_message, "@ERROR: NOT enough mayors!!"),
        (try_end),
        (party_set_slot,":town_no", slot_town_elder, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_tavernkeeper", ":offset"),
        (party_set_slot,":town_no", slot_town_tavernkeeper, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_weaponsmith", ":offset"),
        (party_set_slot,":town_no", slot_town_weaponsmith, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_armorer", ":offset"),
        (party_set_slot,":town_no", slot_town_armorer, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_horse_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_horse_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_master_craftsman", ":offset"),
        (party_set_slot,":town_no", slot_town_mastercraftman, ":cur_object_no"),
        # (party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
    (try_end),
    # Castles
    (try_for_range, ":castle_no", castles_begin, castles_end),
        # (party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
        (party_set_slot,":castle_no", slot_party_type, spt_castle),
        (party_set_slot,":castle_no", slot_center_is_besieged_by, -1),
    (try_end),
    #seneschals - dckplmc
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (store_sub, ":offset", ":center_no", walled_centers_begin),
        (store_add, ":cur_object_no", "trp_town_1_seneschal", ":offset"),
        (party_set_slot,":center_no", slot_town_seneschal, ":cur_object_no"),
        #(party_set_flags, ":center_no", pf_limit_members, 1),
    (try_end),
	  # Villages characters
    (try_for_range, ":village_no", villages_begin, villages_end),
        (store_sub, ":offset", ":village_no", villages_begin),
        (store_add, ":store_troop_no", "trp_village_1_elder", ":offset"),
        (try_begin),
            (neg|is_between, ":store_troop_no", village_elders_begin, village_elders_end),
            (display_message, "@ERROR: NOT enough village elders!!"),
        (try_end),
        (party_set_slot,":village_no", slot_town_elder, ":store_troop_no"),
        (party_set_slot,":village_no", slot_party_type, spt_village),
        (party_set_slot,":village_no", slot_village_raided_by, -1),
    (try_end),
    (try_for_range, ":center_no", centers_begin, centers_end),
        (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
        (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
        (party_set_slot, ":center_no", slot_center_last_taken_by_troop, -1),
    (try_end),

    # Assign banners and renown.
    (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":cur_faction_king", ":cur_faction", slot_faction_leader),
        (ge, ":cur_faction_king", 0),
        (faction_get_slot, ":cur_faction_banner", ":cur_faction", slot_faction_banner),
        (val_sub, ":cur_faction_banner", banner_meshes_begin),
        (val_add, ":cur_faction_banner", banner_scene_props_begin),
        (troop_set_slot, ":cur_faction_king", slot_troop_banner_scene_prop, ":cur_faction_banner"),
    (try_end),

    (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),

        (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
        (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),

        (faction_get_slot, ":cur_faction_banner", ":kingdom_hero_faction", slot_faction_banner),
        (val_sub, ":cur_faction_banner", banner_meshes_begin),
        (val_add, ":cur_faction_banner", banner_scene_props_begin),
        (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":cur_faction_banner"),

        (store_character_level, ":level", ":kingdom_hero"),
        (store_mul, ":renown", ":level", ":level"),
        (val_div, ":renown", 4), #for top lord, is about 400

        (troop_get_slot, ":age", ":kingdom_hero", slot_troop_age),
        (store_mul, ":age_addition", ":age", ":age"),
        (val_div, ":age_addition", 8), #for top lord, is about 400
        (val_add, ":renown", ":age_addition"),

        (store_random_in_range, ":random_renown", 0, 100),

        (val_add, ":renown", ":random_renown"),
        (troop_set_slot, ":kingdom_hero", slot_troop_renown, ":renown"),
    (try_end),

    (try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_slot_eq, ":kingdom_lady", slot_troop_occupation, slto_kingdom_lady),

        (troop_get_slot, ":spouse", ":kingdom_lady", slot_troop_spouse),
        (try_begin),
            (gt, ":spouse", -1),
            (troop_get_slot, ":renown", ":spouse", slot_troop_renown),
            (val_div, ":renown", 2),
        (else_try),
            (store_character_level, ":renown", ":kingdom_lady"),
            (val_mul, ":renown", 5),
        (try_end),

        (troop_get_slot, ":age", ":kingdom_lady", slot_troop_age),
        (store_mul, ":age_addition", ":age", ":age"),
        (val_div, ":age_addition", 10), #for top lord, is about 400
        (val_add, ":renown", ":age_addition"),

        (try_begin),
            (store_troop_faction, ":kingdom_lady_faction", ":kingdom_lady"),
            (faction_slot_eq, ":kingdom_lady_faction", slot_faction_leader, ":kingdom_lady"),
            (store_random_in_range, ":random_renown", 150, 200),
        (else_try),
            (store_random_in_range, ":random_renown", 0, 50),
        (try_end),
        (val_add, ":renown", ":random_renown"),
        (troop_set_slot, ":kingdom_lady", slot_troop_renown, ":renown"),
    (try_end),

    (try_for_range, ":troop_no", "trp_player", "trp_merchants_end"),
        (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
    (try_end),

    (try_for_range, ":center_no", centers_begin, centers_end),
        (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
    (try_end),

    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh"),
    (else_try),
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh_banner"),
    (try_end),

    (call_script, "script_initialize_government_types"),

    #Give centers to factions
    (call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_9"),
    (call_script, "script_give_center_to_faction_aux", "p_town_2", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_3", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_4", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_5", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_6", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_town_7", "fac_kingdom_3"),
    (call_script, "script_give_center_to_faction_aux", "p_town_8", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_9", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_town_10", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_11", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_town_12", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_13", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_14", "fac_kingdom_22"),
    (call_script, "script_give_center_to_faction_aux", "p_town_15", "fac_kingdom_14"),
    (call_script, "script_give_center_to_faction_aux", "p_town_16", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_17", "fac_kingdom_5"),
    (call_script, "script_give_center_to_faction_aux", "p_town_18", "fac_kingdom_5"),

    (call_script, "script_give_center_to_faction_aux", "p_town_19", "fac_kingdom_7"),
    (party_set_slot, "p_town_19", slot_center_has_barracks, "trp_kingdom_7_lord"),

    (call_script, "script_give_center_to_faction_aux", "p_town_20", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_21", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_22", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_23", "fac_kingdom_15"),
    (call_script, "script_give_center_to_faction_aux", "p_town_24", "fac_kingdom_2"),
    (call_script, "script_give_center_to_faction_aux", "p_town_25", "fac_kingdom_11"),
    (call_script, "script_give_center_to_faction_aux", "p_town_26", "fac_kingdom_12"),

    (call_script, "script_give_center_to_faction_aux", "p_town_27", "fac_kingdom_6"),
    (party_set_slot, "p_town_27", slot_center_has_barracks, "trp_kingdom_6_lord"),

    (call_script, "script_give_center_to_faction_aux", "p_town_28", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_29", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_30", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_31", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_32", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_33", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_34", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_35", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_36", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_37", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_38", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_39", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_town_40", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_town_41", "fac_kingdom_12"),
    (call_script, "script_give_center_to_faction_aux", "p_town_42", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_town_43", "fac_kingdom_8"),
    (call_script, "script_give_center_to_faction_aux", "p_town_44", "fac_kingdom_10"),
    (call_script, "script_give_center_to_faction_aux", "p_town_45", "fac_kingdom_14"),
    (call_script, "script_give_center_to_faction_aux", "p_town_46", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_47", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_48", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_town_49", "fac_kingdom_13"),

    (call_script, "script_give_center_to_faction_aux", "p_town_50", "fac_kingdom_20"),

    (call_script, "script_give_center_to_faction_aux", "p_town_51", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_town_52", "fac_kingdom_6"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_1", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_2", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_3", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_4", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_5", "fac_kingdom_10"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_6", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_7", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_8", "fac_kingdom_4"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_9", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_10", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_11", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_12", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_13", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_14", "fac_kingdom_8"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_15", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_16", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_17", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_18", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_19", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_20", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_21", "fac_kingdom_3"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_22", "fac_kingdom_4"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_23", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_24", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_25", "fac_kingdom_20"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_26", "fac_kingdom_22"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_27", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_28", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_29", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_30", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_31", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_32", "fac_kingdom_16"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_33", "fac_kingdom_16"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_34", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_35", "fac_kingdom_7"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_36", "fac_kingdom_4"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_37", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_38", "fac_kingdom_5"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_39", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_40", "fac_kingdom_23"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_41", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_42", "fac_kingdom_23"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_43", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_44", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_45", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_46", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_47", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_48", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_49", "fac_kingdom_4"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_50", "fac_kingdom_16"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_51", "fac_kingdom_15"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_52", "fac_kingdom_13"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_53", "fac_kingdom_16"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_54", "fac_kingdom_5"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_55", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_56", "fac_kingdom_12"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_57", "fac_kingdom_9"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_58", "fac_kingdom_2"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_59", "fac_kingdom_11"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_60", "fac_kingdom_15"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_61", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_62", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_63", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_64", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_65", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_66", "fac_kingdom_11"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_67", "fac_kingdom_1"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_68", "fac_kingdom_21"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_69", "fac_kingdom_21"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_70", "fac_kingdom_5"),

    (call_script, "script_give_center_to_faction_aux", "p_castle_71", "fac_kingdom_3"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_72", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_73", "fac_kingdom_7"),

    #persia
    (call_script, "script_give_center_to_faction_aux", "p_castle_74", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_75", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_76", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_77", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_78", "fac_kingdom_7"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_79", "fac_kingdom_6"),
    (call_script, "script_give_center_to_faction_aux", "p_castle_80", "fac_kingdom_6"),

    # give centers to governors
    (try_for_range, ":province", p_hisp_tarraco, p_provinces_end),
        (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
            (store_faction_of_party, ":fac", ":walled_center"),
            (faction_slot_eq, ":fac", slot_faction_government_type, gov_imperial),#is imperial government
            (party_slot_eq, ":walled_center", slot_center_province, ":province"),
            (troop_get_slot, ":governor", "trp_province_array", ":province"),
            (troop_set_slot, ":governor", slot_troop_govern, ":province"),#set slot properly
            (call_script, "script_give_center_to_lord2", ":walled_center", ":governor", 0),
        (try_end),
    (try_end),

    (call_script, "script_give_center_to_lord2", "p_castle_69", "trp_kingdom_21_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_castle_42", "trp_kingdom_23_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_14", "trp_kingdom_22_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_50", "trp_kingdom_20_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_18", "trp_kingdom_5_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_27", "trp_kingdom_6_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_11", "trp_kingdom_1_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_castle_32", "trp_kingdom_16_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_23", "trp_kingdom_15_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_15", "trp_kingdom_14_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_49", "trp_kingdom_13_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_castle_36", "trp_kingdom_4_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_26", "trp_kingdom_12_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_25", "trp_kingdom_11_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_44", "trp_kingdom_10_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_1", "trp_kingdom_9_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_43", "trp_kingdom_8_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_24", "trp_kingdom_2_lord", 0),
    (call_script, "script_give_center_to_lord2", "p_town_7", "trp_kingdom_3_lord", 0),

    (party_set_slot, "p_town_6", slot_center_has_slave_market, 1),
    (party_set_slot, "p_town_13", slot_center_has_slave_market, 1),
    (party_set_slot, "p_town_20", slot_center_has_slave_market, 1),

    (troop_set_slot, "trp_kingdom_7_lord", slot_troop_home, "p_town_6"),
    (troop_set_slot, "trp_kingdom_5_lord", slot_troop_home, "p_town_18"),
    (troop_set_slot, "trp_kingdom_6_lord", slot_troop_home, "p_town_27"),
    (troop_set_slot, "trp_kingdom_1_lord", slot_troop_home, "p_town_11"),
    (troop_set_slot, "trp_kingdom_16_lord", slot_troop_home, "p_castle_32"),
    (troop_set_slot, "trp_kingdom_15_lord", slot_troop_home, "p_town_23"),
    (troop_set_slot, "trp_kingdom_14_lord", slot_troop_home, "p_town_15"),
    (troop_set_slot, "trp_kingdom_13_lord", slot_troop_home, "p_castle_22"),
    (troop_set_slot, "trp_kingdom_4_lord", slot_troop_home, "p_castle_36"),
    (troop_set_slot, "trp_kingdom_12_lord", slot_troop_home, "p_town_26"),
    (troop_set_slot, "trp_kingdom_11_lord", slot_troop_home, "p_town_25"),
    (troop_set_slot, "trp_kingdom_10_lord", slot_troop_home, "p_town_44"),
    (troop_set_slot, "trp_kingdom_9_lord", slot_troop_home, "p_town_1"),
    (troop_set_slot, "trp_kingdom_8_lord", slot_troop_home, "p_town_43"),
    (troop_set_slot, "trp_kingdom_2_lord", slot_troop_home, "p_town_24"),
    (troop_set_slot, "trp_kingdom_3_lord", slot_troop_home, "p_town_7"),

    (call_script, "script_assign_lords_to_empty_centers"),
    ##pyramids is culutre_6
    (party_set_slot, "p_pyramids", slot_center_culture,  "fac_culture_6"),
    (party_set_slot, "p_forest", slot_center_culture,  "fac_culture_4"),
    #icons
    ###center rebellions (only for barbarians)
    #centers that can rebell:
    #germania: p_town_15, p_town_45, p_castle_50, p_castle_32, p_castle_33, p_castle_51, p_castle_52, p_town_23, p_castle_22, p_castle_49, p_castle_8, p_castle_36
    #britannia: p_town_43, p_town_1, p_town_24, p_town_44, p_castle_14, p_castle_5
    #steppelands: p_town_7, p_town_28, p_town_41, p_town_25, p_castle_21
    #dacia: p_town_9, p_town_11, p_town_42, p_castle_19, p_castle_7, p_castle_18, p_castle_17
    (try_for_range, ":party", towns_begin, towns_end),
        (store_faction_of_party, ":faction2", ":party"),
        (faction_get_slot, ":faction", ":faction2", slot_faction_culture),
        (try_begin),
            (eq, ":party", "p_town_37"),
            (party_set_icon, ":party", "icon_town_athen"),
        (else_try),
            (eq, ":party", "p_town_19"),
            (party_set_icon, ":party", "icon_town_jerusalem_temple"),
        (else_try),
            (eq, ":party", "p_town_6"),
            (party_set_icon, ":party", "icon_town_rome_before_fire"),
        (else_try),
            (eq, ":party", "p_town_20"),
            (party_set_icon, ":party", "icon_town_alexandria"),
        (else_try),
            (eq, ":faction", "fac_culture_1"),
            (party_set_icon, ":party", "icon_opidumn_rock_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (this_or_next|eq, ":faction", "fac_culture_2"),
            (eq, ":faction", "fac_culture_2_1"),
            (party_set_icon, ":party", "icon_opidumn_wood_br1_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_3"),
            (party_set_icon, ":party", "icon_opidumn_wood_dc1_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_4"),
            (party_set_icon, ":party", "icon_opidumn_wood_gl1_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_5"),
            (party_set_icon, ":party", "icon_town_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_6"),
            (party_set_icon, ":party", "icon_town_persian"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_7"),
            (party_set_icon, ":party", "icon_town_roman"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_8"),
            (party_set_icon, ":party", "icon_town_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_9"),
            (party_set_icon, ":party", "icon_town_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (try_end),
    (try_end),

    (try_for_range, ":party", castles_begin, castles_end),
        (store_faction_of_party, ":faction2", ":party"),
        (faction_get_slot, ":faction", ":faction2", slot_faction_culture),
        (try_begin),
            (eq, ":faction", "fac_culture_1"),
            (party_set_icon, ":party", "icon_opidumn_rock1_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (this_or_next|eq, ":faction", "fac_culture_2"),
            (eq, ":faction", "fac_culture_2_1"),
            (party_set_icon, ":party", "icon_opidumn_wood_br_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_3"),
            (party_set_icon, ":party", "icon_opidumn_wood_dc_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_4"),
            (party_set_icon, ":party", "icon_opidumn_wood_gl_Reduced"),
            (party_set_slot, ":party", slot_center_can_rebell, 1),
        (else_try),
            (eq, ":faction", "fac_culture_5"),
            (party_set_icon, ":party", "icon_fort_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_6"),
            (party_set_icon, ":party", "icon_fort_persian"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_7"),
            (party_set_icon, ":party", "icon_fort_roman"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_8"),
            (party_set_icon, ":party", "icon_fort_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (else_try),
            (eq, ":faction", "fac_culture_9"),
            (party_set_icon, ":party", "icon_fort_greek"),
            (party_set_slot, ":party", slot_center_can_rebell, 0),
        (try_end),
    (try_end),
    (try_for_range, ":party", villages_begin, villages_end),
        (call_script, "script_refresh_village_defenders", ":party"),
        (call_script, "script_refresh_village_defenders", ":party"),
        (call_script, "script_refresh_village_defenders", ":party"),
        (call_script, "script_refresh_village_defenders", ":party"),
        (store_faction_of_party, ":faction2", ":party"),
        (faction_get_slot, ":faction", ":faction2", slot_faction_culture),
        (try_begin),
            (eq, ":faction", "fac_culture_1"),
            (party_set_icon, ":party", "icon_village_barbarian"),
        (else_try),
            (this_or_next|eq, ":faction", "fac_culture_2"),
            (eq, ":faction", "fac_culture_2_1"),
            (party_set_icon, ":party", "icon_village_barbarian"),
        (else_try),
            (eq, ":faction", "fac_culture_3"),
            (party_set_icon, ":party", "icon_village_barbarian"),
        (else_try),
            (eq, ":faction", "fac_culture_4"),
            (party_set_icon, ":party", "icon_village_barbarian"),
        (else_try),
            (eq, ":faction", "fac_culture_5"),
            (party_set_icon, ":party", "icon_village_greek"),
        (else_try),
            (eq, ":faction", "fac_culture_6"),
            (party_set_icon, ":party", "icon_village_greek"),
        (else_try),
            (eq, ":faction", "fac_culture_7"),
            (party_set_icon, ":party", "icon_village_roman"),
        (else_try),
            (eq, ":faction", "fac_culture_8"),
            (party_set_icon, ":party", "icon_village_greek"),
        (else_try),
            (eq, ":faction", "fac_culture_9"),
            (party_set_icon, ":party", "icon_village_greek"),
        (try_end),
    (try_end),

    ## OLD DEBUGGING CODE
    # (try_for_range, ":troop", "trp_player", "trp_troops_end"),
        # (store_attribute_level, reg1,":troop", ca_agility),
        # (store_attribute_level, reg2,":troop", ca_charisma),
        # (store_attribute_level, reg3,":troop", ca_intelligence),
        # (store_attribute_level, reg4,":troop", ca_strength),

        # (str_store_troop_name, s1, ":troop"),
        # (try_for_range, ":skill", "skl_trade", "skl_reserved_14"),
            # (store_skill_level, reg5, ":skill", ":troop"),
            # (gt, reg5, 10),
            # (display_message, "@{s1} has skill larger than 10! ({reg2})"),
        # (try_end),
        # (store_character_level, reg6, ":troop"),

        # (assign, reg10, 0),
        # (troop_get_inventory_capacity, ":capacity", ":troop"),
        # (try_for_range, ":slot", 0, ":capacity"),
            # (troop_get_inventory_slot, ":item_id", "trp_player", ":slot"),
            # (ge, ":item_id", 0),
            # (val_add, reg10, 1),
        # (try_end),
        # (try_begin),
            # (gt, reg10, 40),
            # (display_message, "@{s1} has items larger than 40! ({reg10})"),
        # (try_end),
        # (try_begin),
            # (gt, reg1, 30),
            # (display_message, "@{s1} has agility larger than 30! ({reg1})"),
        # (try_end),
        # (try_begin),
            # (gt, reg2, 30),
            # (display_message, "@{s1} has charisma larger than 30! ({reg2})"),
        # (try_end),
        # (try_begin),
            # (gt, reg3, 30),
            # (display_message, "@{s1} has intelligence larger than 30! ({reg3})"),
        # (try_end),
        # (try_begin),
            # (gt, reg4, 30),
            # (display_message, "@{s1} has strength larger than 30! ({reg4})"),
        # (try_end),
       # (try_begin),
            # (gt, reg6, 40),
            # (display_message, "@{s1} has level larger than 40! ({reg6})"),
        # (try_end),
    # (try_end),
    # (try_for_range, ":party_no", centers_begin, centers_end),
        # (party_get_current_terrain, ":cur_terrain", ":party_no"),
        # # (display_message, "@HEHE"),
        # (try_begin),
            # (this_or_next|eq, ":cur_terrain", 4), #snow
            # (eq, ":cur_terrain", 12), #snow forest
            # (party_set_extra_icon, ":party_no", "icon_ground_snow", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 2), #steppe
            # (eq, ":cur_terrain", 10), #steppe forest
            # (party_set_extra_icon, ":party_no", "icon_ground_steppe", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 13), #desert forest
            # (eq, ":cur_terrain", 5), #rt_desert
            # (party_set_extra_icon, ":party_no", "icon_ground_desert", 0, 0, 0, 0),
        # (else_try),
            # (party_set_extra_icon, ":party_no", "icon_ground_plain", 0, 0, 0, 0),
        # (try_end),
    # (try_end),

    # (try_for_range, ":party_no", "p_caves_of_bacchus", "p_island"),
        # (neq, "p_sacred_grove_2"),
        # (party_get_current_terrain, ":cur_terrain", ":party_no"),
        # # (display_message, "@HEHE"),
        # (try_begin),
            # (this_or_next|eq, ":cur_terrain", 4), #snow
            # (eq, ":cur_terrain", 12), #snow forest
            # (party_set_extra_icon, ":party_no", "icon_ground_snow", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 2), #steppe
            # (eq, ":cur_terrain", 10), #steppe forest
            # (party_set_extra_icon, ":party_no", "icon_ground_steppe", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 13), #desert forest
            # (eq, ":cur_terrain", 5), #rt_desert
            # (party_set_extra_icon, ":party_no", "icon_ground_desert", 0, 0, 0, 0),
        # (else_try),
            # (party_set_extra_icon, ":party_no", "icon_ground_plain", 0, 0, 0, 0),
        # (try_end),
    # (try_end),

    # (try_for_range, ":party_no", "p_underworld", "p_ferry_1a"),
        # (party_get_current_terrain, ":cur_terrain", ":party_no"),
        # # (display_message, "@HEHE"),
        # (try_begin),
            # (this_or_next|eq, ":cur_terrain", 4), #snow
            # (eq, ":cur_terrain", 12), #snow forest
            # (party_set_extra_icon, ":party_no", "icon_ground_snow", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 2), #steppe
            # (eq, ":cur_terrain", 10), #steppe forest
            # (party_set_extra_icon, ":party_no", "icon_ground_steppe", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 13), #desert forest
            # (eq, ":cur_terrain", 5), #rt_desert
            # (party_set_extra_icon, ":party_no", "icon_ground_desert", 0, 0, 0, 0),
        # (else_try),
            # (party_set_extra_icon, ":party_no", "icon_ground_plain", 0, 0, 0, 0),
        # (try_end),
    # (try_end),
    # (try_for_range, ":party_no", "p_training_ground_1", "p_bridge_1"),
        # (party_get_current_terrain, ":cur_terrain", ":party_no"),
        # # (display_message, "@HEHE"),
        # (try_begin),
            # (this_or_next|eq, ":cur_terrain", 4), #snow
            # (eq, ":cur_terrain", 12), #snow forest
            # (party_set_extra_icon, ":party_no", "icon_ground_snow", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 2), #steppe
            # (eq, ":cur_terrain", 10), #steppe forest
            # (party_set_extra_icon, ":party_no", "icon_ground_steppe", 0, 0, 0, 0),
        # (else_try),
            # (this_or_next|eq, ":cur_terrain", 13), #desert forest
            # (eq, ":cur_terrain", 5), #rt_desert
            # (party_set_extra_icon, ":party_no", "icon_ground_desert", 0, 0, 0, 0),
        # (else_try),
            # (party_set_extra_icon, ":party_no", "icon_ground_plain", 0, 0, 0, 0),
        # (try_end),
    # (try_end),
    # (party_set_extra_icon, "p_vally_of_kings", "icon_ground_desert", 0, 0, 0, 0),

    #set original factions
    (try_for_range, ":center_no", centers_begin, centers_end),
        (store_faction_of_party, ":original_faction", ":center_no"),
        (faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
        (party_set_slot, ":center_no", slot_center_culture,  ":culture"),
        (party_set_slot, ":center_no", slot_center_original_faction,  ":original_faction"),
        (party_set_slot, ":center_no", slot_center_ex_faction,  ":original_faction"),
        ##diplomacy start+ set additional slots
        (party_get_slot, ":town_lord", ":center_no", slot_town_lord),

        (try_begin),
            (eq, ":town_lord", "trp_player"),
            #Use trp_kingdom_heroes_including_player_begin instead of trp_player as a workaround for
            #old saved games (since uninitialized memory is 0).
            (party_set_slot, ":center_no", dplmc_slot_center_ex_lord, "trp_kingdom_heroes_including_player_begin"),
            (troop_slot_eq, "trp_player", slot_troop_home, ":center_no"),
            (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
            (party_set_slot, ":center_no", dplmc_slot_center_original_lord, "trp_kingdom_heroes_including_player_begin"),
        (else_try),
            (party_set_slot, ":center_no", dplmc_slot_center_ex_lord, ":town_lord"),
            (ge, ":town_lord", 0),
            (troop_slot_eq, ":town_lord", slot_troop_home, ":center_no"),
            (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
            (party_set_slot, ":center_no", dplmc_slot_center_original_lord, ":town_lord"),
        (try_end),
        ##diplomacy end+
    (try_end),

    ## correct culture:
    (party_set_slot, "p_town_19", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_castle_44", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_castle_45", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_castle_46", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_98", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_97", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_96", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_109", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_51", slot_center_culture, "fac_culture_8"),
    (party_set_slot, "p_village_100", slot_center_culture, "fac_culture_8"),

    (call_script, "script_initialize_npc_items"),
    ##also add lady items, to it here because it require troop culture slot to be set properly
    (try_for_range, ":cur_lady", "trp_kingdom_1_lady_1", "trp_gwenhwyfar"),
        (call_script, "script_add_lady_items", ":cur_lady"),
    (try_end),

    ##add some border conflicts at game start
    (party_set_slot, "p_castle_21", slot_center_original_faction, "fac_kingdom_11"),#give it to the Sarmatians so they can conquer it
    (party_set_slot, "p_castle_23", slot_center_original_faction,  "fac_kingdom_8"),#londinium
    (party_set_slot, "p_castle_23", slot_center_ex_faction,  "fac_kingdom_8"),#londinium
	# (party_set_slot, "p_town_47", slot_center_ex_faction, "fac_kingdom_7"), #parthia has attacked the Imperium
	# (party_set_slot, "p_town_17", slot_center_ex_faction, "fac_kingdom_5"), #parthia has attacked armenia

    #Initialize troop classes here
    #set name of class
    (class_set_name, sdt_polearm, "@Spearmen"),
    (class_set_name, sdt_skirmisher, "@Skirmishers"),
    (class_set_name, sdt_harcher, "@Horse Archers"),
    (class_set_name, sdt_support, "@Support"),
    (class_set_name, sdt_bodyguard, "@Companions"),
    #Reassign divisions
    (try_for_range, ":troop_no", soldiers_begin, soldiers_end),
        (call_script, "script_troop_default_division", ":troop_no", 0),
        (troop_get_class, ":division", ":troop_no"),
        (neq, ":division", reg0),
        (troop_set_class, ":troop_no", reg0),
    (try_end),

    #vulcano smoke
    (party_add_particle_system, "p_reserved_1", "psys_map_village_fire_smoke"),
    (party_add_particle_system, "p_reserved_2", "psys_map_village_fire_smoke"),

    #initialise special quests
    (quest_set_slot, "qst_nero_special_quest", slot_quest_target_dna, -1),

    (call_script, "script_update_village_market_towns"),
    (call_script, "script_find_neighbors"),
	  ##diplomacy start+
	  #(1) Assign plausible ancestral homes to some of the lords (not all of them) who didn't have
    #one set before.  Among other things, this is used for a sense of possessiveness.
    #(2) Assign last-transfer-times to the contested centers.
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (try_begin),
            #Assign last-transfer-times to the contested centers.
            (party_get_slot, ":original_faction", ":center_no", slot_center_original_faction),
            (neg|party_slot_eq, ":center_no", slot_center_ex_faction, ":original_faction"),
            (store_random_in_range, ":transfer_time", 1, 181),#some time in the last 180 days (the length of a short game)
            (val_mul, ":transfer_time", -24),
            (party_set_slot, ":center_no", dplmc_slot_center_last_transfer_time, ":transfer_time"),
        (else_try),
            #For non-contested centers, possibly set the lord's home slot.  Note that because
            #we're iterating in order, lords will get set to towns they own before they get
            #set to cities.
            (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
            (ge, ":town_lord", 1),#only NPCs
            (neg|troop_slot_ge, ":town_lord", slot_troop_govern, 1),
            (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),#If there is an original owner who is dispossessed, such as a claimant
            (neg|troop_slot_ge, ":town_lord", slot_troop_home, 1),
            (troop_set_slot, ":town_lord", slot_troop_home, ":center_no"),
        (try_end),
    (try_end),

    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        #If the original owner of the lord is set, don't apply this
        (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
        #Don't apply this to contested centers.
        (party_get_slot, ":original_faction", ":center_no", slot_center_original_faction),
        (party_slot_eq, ":center_no", slot_center_ex_faction, ":original_faction"),
        #If the owner already has his "home" slot set, don't overwrite it
        (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
        (neg|troop_slot_ge, ":town_lord", slot_troop_home, 1),
        #No objections, so go ahead
        (troop_set_slot, ":town_lord", slot_troop_home, ":center_no"),
    (try_end),
    ##diplomacy end+

    ##set up initial diplomatic relations
    # (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_2", "fac_kingdom_10", 0),#to make britannia more active

    (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_3", "fac_kingdom_7", 0),
    # (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_8", "fac_kingdom_7", 0),
    # (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_9", "fac_kingdom_7", 0),
    (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_10", "fac_kingdom_7", 0),

    (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_22", "fac_kingdom_7", 0),
    (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_kingdom_20", "fac_kingdom_7", 0),
    (call_script, "script_dplmc_start_tributary_between_kingdoms", "fac_kingdom_23", "fac_kingdom_7", 0),
    (call_script, "script_dplmc_start_tributary_between_kingdoms", "fac_kingdom_5", "fac_kingdom_6", 0),

    (store_add, ":slot_provocation_days", "fac_kingdom_7", slot_faction_provocation_days_with_factions_begin),
    (val_sub, ":slot_provocation_days", kingdoms_begin),
    (faction_get_slot, ":provocation_days", "fac_kingdom_7", ":slot_provocation_days"),
    (val_add, ":provocation_days", 84), ##one year
    (faction_set_slot, "fac_kingdom_7", ":slot_provocation_days", ":provocation_days"),

    (try_for_range, ":kingdoms",kingdoms_begin, kingdoms_end),
        (store_random_in_range, ":fac", kingdoms_begin, kingdoms_end),
        (faction_set_slot, ":kingdoms",slot_faction_ai_diplomatic_object,":fac"),
    (try_end),
    # (try_for_range, ":unused", 0, 6), #was 47 # was 70, chill boys, we have all time
        # (try_begin),
            # (eq, "$cheat_mode", 1),
            # (display_message, "@{!}DEBUG -- initial war/peace check begins"),
        # (try_end),
        # (call_script, "script_randomly_start_war_peace_new", 0),
    # (try_end),

    #castle walkers
    #Initialize walkers
    (try_for_range, ":center_no", centers_begin, centers_end),
        (try_for_range, ":walker_no", 0, num_town_walkers),
            (call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
        (try_end),
    (try_end),

    #This needs to be after market towns
    (call_script, "script_initialize_economic_information"),

    (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
    (try_end),

    (try_for_range, ":troop_id", original_kingdom_heroes_begin, active_npcs_end),
        (try_begin),
            (store_troop_faction, ":faction_id", ":troop_id"),
            (is_between, ":faction_id", kingdoms_begin, kingdoms_end),
            (troop_set_slot, ":troop_id", slot_troop_original_faction, ":faction_id"),
            # (try_begin),
            # (is_between, ":troop_id", pretenders_begin, pretenders_end),
            # (faction_set_slot, ":faction_id", slot_faction_has_rebellion_chance, 1),
            # (try_end),
        (try_end),
        (assign, ":initial_wealth", 100000),
        (try_begin),
            (store_troop_faction, ":faction", ":troop_id"),
            (faction_slot_eq, ":faction", slot_faction_leader, ":troop_id"),
            (val_add, ":initial_wealth", 50000),
        (try_end),
        (try_begin),
            (eq, ":troop_id", "trp_kingdom_7_lord"),
            (val_add, ":initial_wealth", 150000),
        (else_try),
            (eq, ":troop_id", "trp_kingdom_6_lord"),
            (val_add, ":initial_wealth", 100000),
        (try_end),
        (troop_set_slot, ":troop_id", slot_troop_wealth, ":initial_wealth"),
    (try_end),

    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),#add town garrisons
        #Add initial center wealth
        (assign, ":initial_wealth", 2500),
        (try_begin),
            (is_between, ":center_no", towns_begin, towns_end),
            (val_add, ":initial_wealth", 5000),
        (try_end),
        (party_set_slot, ":center_no", slot_town_wealth, ":initial_wealth"),

        (assign, ":garrison_strength", 30),
        (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":garrison_strength", 60),
        (try_end),
        (try_begin),
            (party_get_slot, ":legati", ":center_no", slot_town_lord),
            (is_between, ":legati", "trp_legatus_1", "trp_aux_commander_1"),
            (assign, ":garrison_strength", 5),
        (try_end),

        (try_begin),
            (store_faction_of_party, ":faction", ":center_no"),
            (this_or_next|faction_slot_eq, ":faction", slot_faction_culture, "fac_culture_3"),###to help nomads to survive
            (faction_slot_eq, ":faction", slot_faction_culture, "fac_culture_4"),##to help germans
            (val_add, ":garrison_strength", 15),
        (try_end),
            ####

        (call_script, "script_update_center_garrision", ":center_no", ":faction"),

        (try_for_range, ":party_template_slot", slot_cohort_town_begin, slot_cohort_town_end),
            (party_get_slot, ":party_template", ":center_no", ":party_template_slot"),
            (ge, ":party_template", 1),
            (call_script, "script_cohort_refil_garrison", ":center_no", ":party_template", ":party_template_slot",0),
        (try_end),
        ## ADD some XP initially
        (store_div, ":xp_rounds", ":garrison_strength", 5),
        (val_add, ":xp_rounds", 5),

        (options_get_campaign_ai, ":reduce_campaign_ai"),

        (try_begin), #hard
            (eq, ":reduce_campaign_ai", 0),
            (assign, ":xp_addition_for_centers", 10000),
        (else_try), #moderate
            (eq, ":reduce_campaign_ai", 1),
            (assign, ":xp_addition_for_centers", 7500),
        (else_try), #easy
            (eq, ":reduce_campaign_ai", 2),
            (assign, ":xp_addition_for_centers", 5000),
        (try_end),

        (try_for_range, ":unused", 0, ":xp_rounds"),
            (party_upgrade_with_xp, ":center_no", ":xp_addition_for_centers", 0),
        (try_end),

        #Fill town food stores upto half the limit
        (call_script, "script_center_get_food_store_limit", ":center_no"),
        (assign, ":food_store_limit", reg0),
        (val_div, ":food_store_limit", 2),
        (party_set_slot, ":center_no", slot_party_food_store, ":food_store_limit"),

        #create lord parties
        # (try_begin),
            # (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
            # (ge, ":center_lord", 1),
            # (troop_slot_eq, ":center_lord", slot_troop_leaded_party, 0),
            # (assign, "$g_there_is_no_avaliable_centers", 0),
            # (call_script, "script_create_kingdom_hero_party", ":center_lord", ":center_no"),
            # (assign, ":lords_party", "$pout_party"),
            # (party_attach_to_party, ":lords_party", ":center_no"),
        # (try_end),
        (party_set_slot, ":center_no", slot_town_player_odds, 1000),
    (try_end),

    #spawn all lord parties
    (try_for_range, ":troop_no", heroes_begin, heroes_end),
        ##diplomacy end+
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
        (store_troop_faction, ":cur_faction", ":troop_no"),
        (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
        (try_begin),
            (eq, "$cheat_mode", 2),
            (str_store_troop_name, s4, ":troop_no"),
            (display_message, "str_debug__attempting_to_spawn_s4"),
        (try_end),
        (assign, "$g_there_is_no_avaliable_centers", 0),
        (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
        (is_between, reg0, walled_centers_begin, walled_centers_end),##avoid script errors
        (assign, ":center_no", reg0),

        (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),

        (try_begin),
            (eq, "$g_there_is_no_avaliable_centers", 0),
            (gt, "$pout_party", 0),#just to be save
            (party_attach_to_party, "$pout_party", ":center_no"),
        (try_end),
        #new
        #(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        #(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
        #(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
        #new end
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),
    (try_end),
	#More pre-Warband family structures removed here
    #Warband changes begin - set companions relations
    (try_for_range, ":companion", companions_begin, companions_end),
        (try_for_range, ":other_companion", companions_begin, companions_end),
            (neq, ":other_companion", ":companion"),
            (neg|troop_slot_eq, ":companion", slot_troop_personalityclash_object, ":other_companion"),
            (neg|troop_slot_eq, ":companion", slot_troop_personalityclash2_object, ":other_companion"),
            (call_script, "script_troop_change_relation_with_troop", ":companion", ":other_companion", 7), #companions have a starting relation of 14, unless they are rivals
        (try_end),
    (try_end),

	  #Warband changes continue -  sets relations in the same faction
    (try_for_range, ":lord", original_kingdom_heroes_begin, active_npcs_end),
        (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":lord_faction", ":lord", slot_troop_original_faction),

        (try_for_range, ":other_hero", original_kingdom_heroes_begin, active_npcs_end),
            (troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
            (troop_get_slot, ":other_hero_faction", ":other_hero", slot_troop_original_faction),
            (eq, ":other_hero_faction", ":lord_faction"),
            (call_script, "script_troop_get_family_relation_to_troop", ":lord", ":other_hero"),
            (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", reg0),

            (store_random_in_range, ":random", 0, 11), #this will be scored twice between two kingdom heroes, so starting relation will average 10. Between lords and pretenders it will average 7.5
            (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", ":random"),
        (try_end),
    (try_end),

    ##diplomacy start+
    ##Initialize town "last caravan arrived" times randomly
    # (try_for_range, ":cur_town", towns_begin, towns_end),
        # (try_for_range, ":cur_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
            # (party_slot_eq, ":cur_town", ":cur_slot", 0),
            # (store_random_in_range, ":last_arrived", 1, (24 * 7 * 5) + 1),#some time in the last five weeks
            # (val_mul, ":last_arrived", -1),
            # (party_get_slot, ":prosperity_factor", ":cur_town", slot_town_prosperity),#modify plus or minus 40% based on prosperity
            # (val_clamp, ":prosperity_factor", 0, 101),
            # (val_add, ":prosperity_factor", 75),
            # (val_mul, ":last_arrived", 125),
            # (val_div, ":last_arrived", ":prosperity_factor"),#last arrival some time in the last five weeks, plus or minus 40%
            # (party_set_slot, ":cur_town", ":cur_slot", ":last_arrived"),
        # (try_end),
    # (try_end),
    # (try_for_range, ":cur_village", villages_begin, villages_end),
        # (party_get_slot, ":prosperity_factor", ":cur_village", slot_town_prosperity),#modify plus or minus 40% based on prosperity
        # (val_clamp, ":prosperity_factor", 0, 101),
        # (val_add, ":prosperity_factor", 75),#average 125, min 75, max 175
        # (store_random_in_range, ":last_arrived", 1, (24 * 7) + 1),
        # (val_mul, ":last_arrived", -1),#some time in the last 7 days, plus or minus 40%
        # (val_mul, ":last_arrived", 125),
        # (val_div, ":last_arrived", ":prosperity_factor"),
        # (party_set_slot, ":cur_village", dplmc_slot_village_trade_last_returned_from_market, ":last_arrived"),
        # (store_random_in_range, ":last_arrived", 1, (24 * 7) + 1),
        # (val_mul, ":last_arrived", -1),#some time in the last 7 days
        # (val_mul, ":last_arrived", 125),
        # (val_div, ":last_arrived", ":prosperity_factor"),
        # (party_set_slot, ":cur_village", dplmc_slot_village_trade_last_arrived_to_market, ":last_arrived"),
    # (try_end),
    ##diplomacy end+

    #do about 5 years' worth of political history (assuming 3 random checks a day)
    (try_for_range, ":unused", 0, 5000),
        (call_script, "script_cf_random_political_event"),
    (try_end),
    (assign, "$total_random_quarrel_changes", 0),
    (assign, "$total_relation_adds", 0),
    (assign, "$total_relation_subs", 0),

    (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
        (call_script, "script_evaluate_realm_stability", ":kingdom"),
    (try_end),
    #Warband changes end

    #assign love interests to unmarried male lords
    (try_for_range, ":cur_troop", lords_begin, lords_end),
        (troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),
        ##diplomacy start+ Also bypass this for characters that start with manually-assigned fiancees
        (troop_slot_eq, ":cur_troop", slot_troop_betrothed, -1),
        ##diplomacy end+
        (neg|is_between, ":cur_troop", kings_begin, kings_end),
        # (neg|is_between, ":cur_troop", pretenders_begin, pretenders_end),

        (call_script, "script_assign_troop_love_interests", ":cur_troop"),
    (try_end),

    (store_random_in_range, "$romantic_attraction_seed", 0, 5),

    ##set slots, do it only once at game start
    (party_template_set_slot, "pt_sakas", slot_party_template_lair_type, "pt_saka_camp"),
    (party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_type, "pt_steppe_bandit_lair"),
    (party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_type, "pt_taiga_bandit_lair"),
    (party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_type, "pt_mountain_bandit_lair"),
    (party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_type, "pt_forest_bandit_lair"),
    (party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_type, "pt_sea_raider_lair"),
    (party_template_set_slot, "pt_black_sea_pirates", slot_party_template_lair_type, "pt_black_sea_pirates_lair"),

    (party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_type, "pt_desert_bandit_lair"),
    (party_template_set_slot, "pt_egyptian_rebels", slot_party_template_lair_type, "pt_egyptian_bandit_lair"),
    (party_template_set_slot, "pt_nubian", slot_party_template_lair_type, "pt_nubian_lair"),
    (party_template_set_slot, "pt_nabatean", slot_party_template_lair_type, "pt_nabatean_lair"),
    (party_template_set_slot, "pt_garamantes", slot_party_template_lair_type, "pt_numidian_bandit_lair"),
    (party_template_set_slot, "pt_gaetuli", slot_party_template_lair_type, "pt_gaetuli_bandit_lair"),

    (party_template_set_slot, "pt_sakas", slot_party_template_lair_spawnpoint, "p_saka_spawn"),
    (party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_spawnpoint, "p_steppe_bandit_spawn_point"), #the stepp
    (party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_spawnpoint, "p_taiga_bandit_spawn_point1"), #illyricum
    (party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point1"), # judea
    (party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_spawnpoint, "p_forest_bandit_spawn_point"), #hispania
    (party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_1"), # the coast
    (party_template_set_slot, "pt_black_sea_pirates", slot_party_template_lair_spawnpoint, "p_black_sea_pirates_spawn_1"), # the coast
    (party_template_set_slot, "pt_garamantes", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_23"), # africa
    (party_template_set_slot, "pt_nubian", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point3"), # africa
    (party_template_set_slot, "pt_gaetuli", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_2"), # mauretania
    (party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point2"), #arabia
    (party_template_set_slot, "pt_nabatean", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point"), #nabatea
    (party_template_set_slot, "pt_egyptian_rebels", slot_party_template_lair_spawnpoint, "p_egyptian_spawn"), #egypt

    (party_set_slot, "p_black_sea_pirates_spawn_1", slot_party_on_water, 1),

    (try_for_range, ":unused", 0, 40),#was 25
        (call_script, "script_spawn_bandits"),
    (try_end),

    #we are adding looter parties around each village with 1/5 probability.
    (set_spawn_radius, 5),
    (try_for_range, ":cur_village", villages_begin, villages_end),
        (store_random_in_range, ":random_value", 0, 6),
        (eq, ":random_value", 0),
        (call_script, "script_spawn_party", ":cur_village", "pt_looters"),
    (try_end),

    (call_script, "script_init_desert_cities"),
    (call_script, "script_add_ports_jetty_and_ferry_system"),

    (call_script, "script_update_mercenary_units_of_towns"),
    # (call_script, "script_update_companion_candidates_in_taverns"),
    (call_script, "script_update_ransom_brokers"),
    (call_script, "script_update_tavern_travellers"),
    (call_script, "script_update_tavern_minstrels"),
    (call_script, "script_update_booksellers"),

    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom"),
        (store_random_in_range, ":random_no", -24, 0),
        #Change to a time within the last week.
        (val_mul, ":random_no", 7),
        (faction_set_slot, ":cur_kingdom", slot_faction_last_offensive_concluded, ":random_no"),
    (try_end),

    (try_for_range, ":cur_troop", original_kingdom_heroes_begin, active_npcs_end),
        (troop_set_slot, ":cur_troop", slot_lord_granted_courtship_permission, 0), #initialize
        (call_script, "script_update_troop_notes", ":cur_troop"),
    (try_end),

    (try_for_range, ":cur_center", centers_begin, centers_end),
        ##diplomacy start+
        (party_get_slot, ":original_faction", ":cur_center", slot_center_original_faction),
        (try_begin),
            #Assign plausible last-transfer-times to the contested centers based
            #on the "last offensive concluded" slot of the controlling faction.
            (is_between, ":original_faction", kingdoms_begin, kingdoms_end),
            (neg|party_slot_eq, ":cur_center", slot_center_ex_faction, ":original_faction"),
            (faction_get_slot, reg0, ":original_faction", slot_faction_last_offensive_concluded),
            (party_set_slot, ":cur_center", dplmc_slot_center_last_transfer_time, reg0),
        (try_end),
        ##diplomacy end+
        (call_script, "script_update_center_notes", ":cur_center"),
    (try_end),

    (call_script, "script_update_troop_notes", "trp_player"),

    ##diplomacy start+
    ##Set initial relations between kingdom ladies and their relatives.
    ##Do *not* initialize their relations with anyone they aren't related to:
    ##that is used for courtship.
    ##  The purpose of this initialization is so if a kingdom lady gets promoted,
    ##her relations aren't a featureless slate.  Also, it would be interesting to
    ##further develop the idea of ladies as pursuing agendas even if they aren't
    ##leading warbands, which would benefit from giving them relations with other
    ##people.
    (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
        (troop_get_slot, ":lady_faction", ":lady", slot_troop_original_faction),

        (try_for_range, ":other_hero", heroes_begin, heroes_end),
            (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
            (troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":other_hero", slot_troop_original_faction, ":lady_faction"),

            (neq, ":other_hero", ":lady"),
            (try_begin),
                (this_or_next|troop_slot_eq, ":lady", slot_troop_spouse, ":other_hero"),
                (troop_slot_eq, ":other_hero", slot_troop_spouse, ":lady"),
                (store_random_in_range, reg0, 0, 11),
            (else_try),
                (call_script, "script_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
            (try_end),
            (call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", reg0),

            #This relation change only applies between kingdom ladies.
            (troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
            (is_between, ":other_hero", kingdom_ladies_begin, kingdom_ladies_end),

            (store_random_in_range, ":random", 0, 11),
            (call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", ":random"),
        (try_end),
    (try_end),

    #Perform initialization for autoloot / autosell.
    (call_script, "script_dplmc_initialize_autoloot", 1),#argument "1" forces this to make changes
    #Set the version number (this slot on this troop should never be used for anything else)
    #The lowest 7 bits of the slot are a verification code.  They should always be equal to 68,
    #  unless there is no version number set.  The rest of the slot is the version number.

    (faction_set_slot, "fac_kingdom_1", slot_faction_adjective, "str_kingdom_1_adjective"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_adjective, "str_kingdom_2_adjective"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_adjective, "str_kingdom_3_adjective"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_adjective, "str_kingdom_4_adjective"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_adjective, "str_kingdom_5_adjective"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_adjective, "str_kingdom_6_adjective"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_adjective, "str_kingdom_7_adjective"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_adjective, "str_kingdom_8_adjective"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_adjective, "str_kingdom_9_adjective"),
    (faction_set_slot, "fac_kingdom_10", slot_faction_adjective, "str_kingdom_10_adjective"),
    (faction_set_slot, "fac_kingdom_11", slot_faction_adjective, "str_kingdom_11_adjective"),
    (faction_set_slot, "fac_kingdom_12", slot_faction_adjective, "str_kingdom_12_adjective"),
    (faction_set_slot, "fac_kingdom_13", slot_faction_adjective, "str_kingdom_13_adjective"),
    (faction_set_slot, "fac_kingdom_14", slot_faction_adjective, "str_kingdom_14_adjective"),
    (faction_set_slot, "fac_kingdom_15", slot_faction_adjective, "str_kingdom_15_adjective"),
    (faction_set_slot, "fac_kingdom_16", slot_faction_adjective, "str_kingdom_16_adjective"),
    (faction_set_slot, "fac_kingdom_17", slot_faction_adjective, "str_kingdom_17_adjective"),
    (faction_set_slot, "fac_kingdom_18", slot_faction_adjective, "str_kingdom_18_adjective"),
    (faction_set_slot, "fac_kingdom_19", slot_faction_adjective, "str_kingdom_19_adjective"),
    (faction_set_slot, "fac_kingdom_20", slot_faction_adjective, "str_kingdom_20_adjective"),
    (faction_set_slot, "fac_kingdom_21", slot_faction_adjective, "str_kingdom_21_adjective"),
    (faction_set_slot, "fac_kingdom_22", slot_faction_adjective, "str_kingdom_22_adjective"),
    (faction_set_slot, "fac_kingdom_23", slot_faction_adjective, "str_kingdom_23_adjective"),
    (faction_set_slot, "fac_kingdom_24", slot_faction_adjective, "str_kingdom_24_adjective"),
    (faction_set_slot, "fac_kingdom_25", slot_faction_adjective, "str_kingdom_25_adjective"),
    (faction_set_slot, "fac_kingdom_26", slot_faction_adjective, "str_kingdom_26_adjective"),
    (faction_set_slot, "fac_kingdom_27", slot_faction_adjective, "str_kingdom_27_adjective"),

    (call_script, "script_get_player_party_morale_values"),
    (party_set_morale, "p_main_party", reg0),

    #Lady and companion notes become available as you meet/recruit them

    (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_set_note_available, ":faction_no", 1),
    (try_end),
    (faction_set_note_available, "fac_neutral", 0),

    (try_for_range, ":party_no", centers_begin, centers_end),
        (party_set_note_available, ":party_no", 1),
    (try_end),

    ##moved from gamestart script to speed things up
    #SB : training ground slots
    (try_for_range, ":npc", training_ground_trainers_begin, training_ground_trainers_end),
        #init trainer vars
        (troop_set_slot, ":npc", slot_troop_trainer_met, 0),
        (troop_set_slot, ":npc", slot_troop_trainer_waiting_for_result, 0),
        (troop_set_slot, ":npc", slot_troop_trainer_training_fight_won, 0),
        (troop_set_slot, ":npc", slot_troop_trainer_num_opponents_to_beat, 3),
        (troop_set_slot, ":npc", slot_troop_trainer_training_system_explained, 0),
        (troop_set_slot, ":npc", slot_troop_trainer_opponent_troop, fighters_begin),
        (troop_set_slot, ":npc", slot_troop_trainer_training_difficulty, 0),

        (store_sub, ":offset", ":npc", training_ground_trainers_begin),
        #init grounds vars
        (store_add, ":grounds", ":offset", training_grounds_begin),
        (store_add, ":scene", ":offset", "scn_training_ground_ranged_melee_1"),
        (party_set_slot, ":grounds", slot_grounds_melee, ":scene"),
        (store_add, ":scene", ":offset", "scn_training_ground_horse_track_1"),
        (party_set_slot, ":grounds", slot_grounds_track, ":scene"),
        (party_set_slot, ":grounds", slot_grounds_trainer, ":npc"),
        (party_set_slot, ":grounds", slot_grounds_count, 0),
        (troop_set_slot, ":npc", slot_troop_cur_center, ":grounds"),
    (try_end),

    ##moved from gamestart script to speed things up
    ###titles
    (try_for_range, ":sandler", "trp_kingdom_1_lord", kingdom_ladies_end),
        (store_faction_of_troop, ":snalder_faction", ":sandler"),
        (call_script, "script_troop_set_title_according_to_faction", ":sandler", ":snalder_faction"),
    (try_end),

    (try_for_range, ":center", centers_begin, centers_end),
        (call_script, "script_center_get_capital", ":center"),
        (party_set_slot, ":center", slot_center_capital, reg49),
    (try_end),

    (try_for_range, ":guest", 0, 100),
        (troop_set_slot, "trp_array_villa_feast", ":guest", -1),
    (try_end),

    (call_script, "script_troop_change_relation_with_troop", "trp_kingdom_7_lord", "trp_kingdom_7_lady_2", 55),##he loves her

    (troop_set_slot, "trp_kingdom_7_lady_2", slot_troop_lover, "trp_kingdom_7_lord"),
    (call_script, "script_troop_change_relation_with_troop", "trp_kingdom_7_lord", "trp_kingdom_7_lady_1", 30),##and her

    (call_script, "script_init_special_npcs"),

    #Batava Revolt
    (faction_set_slot, "fac_kingdom_19", slot_faction_state, sfs_inactive),
    (faction_set_note_available, "fac_kingdom_19",0),
    (troop_set_slot, "trp_kingdom_19_lord", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_19_1", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_19_2", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_19_3", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_19_lady_1", slot_troop_occupation, slto_inactive),
    (troop_set_note_available,"trp_kingdom_19_lord",0),
    (troop_set_note_available,"trp_knight_19_1",0),
    (troop_set_note_available,"trp_knight_19_2",0),
    (troop_set_note_available,"trp_knight_19_3",0),
    (troop_set_note_available,"trp_kingdom_19_lady_1",0),

    #Roman civil war factions
    (faction_set_slot, "fac_kingdom_24", slot_faction_state, sfs_inactive),
    (faction_set_note_available, "fac_kingdom_24",0),
    (faction_set_slot, "fac_kingdom_25", slot_faction_state, sfs_inactive),
    (faction_set_note_available, "fac_kingdom_25",0),
    (faction_set_slot, "fac_kingdom_26", slot_faction_state, sfs_inactive),
    (faction_set_note_available, "fac_kingdom_26",0),
    (faction_set_slot, "fac_kingdom_27", slot_faction_state, sfs_inactive),
    (faction_set_note_available, "fac_kingdom_27",0),

    (faction_set_slot, "fac_kingdom_24", slot_faction_government_type, gov_imperial),
    (faction_set_slot, "fac_kingdom_25", slot_faction_government_type, gov_imperial),
    (faction_set_slot, "fac_kingdom_26", slot_faction_government_type, gov_imperial),
    (faction_set_slot, "fac_kingdom_27", slot_faction_government_type, gov_imperial),

    (faction_set_slot, "fac_kingdom_24", slot_faction_tax_rate, 35),
    (faction_set_slot, "fac_kingdom_25", slot_faction_tax_rate, 35),
    (faction_set_slot, "fac_kingdom_26", slot_faction_tax_rate, 35),
    (faction_set_slot, "fac_kingdom_27", slot_faction_tax_rate, 35),

    (faction_set_slot, "fac_kingdom_24", slot_faction_tax_rate_buisness, 30),
    (faction_set_slot, "fac_kingdom_25", slot_faction_tax_rate_buisness, 30),
    (faction_set_slot, "fac_kingdom_26", slot_faction_tax_rate_buisness, 30),
    (faction_set_slot, "fac_kingdom_27", slot_faction_tax_rate_buisness, 30),

    #iazyges Invasion
    (faction_set_slot, "fac_kingdom_18", slot_faction_state, sfs_inactive),
    (troop_set_slot, "trp_kingdom_18_lord", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_3_lady_14", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_3_lady_11", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_3_lady_17", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_3_lady_20", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_3_11", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_3_14", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_3_17", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_3_20", slot_troop_occupation, slto_inactive),
    (faction_set_note_available, "fac_kingdom_18",0),
    (troop_set_note_available,"trp_kingdom_18_lord",0),
    (troop_set_note_available,"trp_knight_3_11",0),
    (troop_set_note_available,"trp_knight_3_14",0),
    (troop_set_note_available,"trp_knight_3_17",0),
    (troop_set_note_available,"trp_knight_3_20",0),
    (troop_set_note_available,"trp_kingdom_3_lady_14",0),
    (troop_set_note_available,"trp_kingdom_3_lady_11",0),
    (troop_set_note_available,"trp_kingdom_3_lady_17",0),
    (troop_set_note_available,"trp_kingdom_3_lady_20",0),

    #Jewish Revolt
    (faction_set_slot, "fac_kingdom_17", slot_faction_state, sfs_inactive),
    (troop_set_slot, "trp_knight_17_1", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_17_2", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_knight_17_3", slot_troop_occupation, slto_inactive),
    (troop_set_slot, "trp_kingdom_17_lord", slot_troop_occupation, slto_inactive),
    (faction_set_note_available, "fac_kingdom_17",0),
    (troop_set_note_available,"trp_knight_17_1",0),
    (troop_set_note_available,"trp_knight_17_2",0),
    (troop_set_note_available,"trp_knight_17_3",0),
    (troop_set_note_available,"trp_kingdom_17_lord",0),

    #Place kingdom ladies
    (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
        (troop_set_slot, ":troop_id", slot_troop_cur_center, reg1),
        ##diplomacy start+
        #Set their original faction.
        (ge, reg0, 0),
        (troop_get_slot, ":original_faction", reg0, slot_troop_original_faction),
        (troop_set_slot, ":troop_id", slot_troop_original_faction, ":original_faction"),
        ##diplomacy end+
    (try_end),

    (faction_set_slot, "fac_kingdom_7", slot_faction_has_nor_titles, 1),

    #icons
    (try_for_parties, ":party"),
        (gt, ":party", last_static_party),
        (party_is_active, ":party"),
        (call_script, "script_update_party_icon", ":party"),
    (try_end),

    #shader
    (call_script, "script_game_get_date_text", 0,0),
    (set_fixed_point_multiplier, 1),
    (try_begin),
        (is_between, "$g_cur_month", 3, 6), # spring
        (assign, "$shader_season", 0),#we start in summer
        (set_shader_param_float, "@vSeason", "$shader_season"),
    (else_try),
        (is_between, "$g_cur_month", 6, 9), # summer
        (assign, "$shader_season", 0),#we start in summer
        (set_shader_param_float, "@vSeason", "$shader_season"),
    (else_try),
        (is_between, "$g_cur_month", 9, 12), # autumn
        (assign, "$shader_season", 0),#we start in summer
        (set_shader_param_float, "@vSeason", "$shader_season"),
    (else_try),
        #(is_between, "$g_cur_month", 12, 3), # winter
        (assign, "$shader_season", 3),#we start in summer
        (set_shader_param_float, "@vSeason", "$shader_season"),
    (try_end),
    #shader
    (set_fixed_point_multiplier,1),
    (assign, "$wind_power", 1), #value in range of 0 (no wind) to 3 (extreme wind)
    (set_shader_param_float, "@vWindStrength", "$wind_power"),
    (set_shader_param_float, "@vWindDirection", 30),#30 degrees

    ##finally scenes
    (call_script, "script_game_set_scenes_for_towns"),

    (try_for_range, ":town", walled_centers_begin,walled_centers_end),
        (party_get_slot, ":lord", ":town", slot_town_lord),
        # (str_store_troop_name, s1, ":lord"),
        # (str_store_party_name, s2, ":town"),
        # (display_message, "@{s1} in {s2}"),
        (store_faction_of_troop, ":lord_faction", ":lord"),
        (this_or_next|troop_slot_ge, ":lord", slot_troop_legion, 1),
        (faction_slot_eq, ":lord_faction", slot_faction_leader, ":lord"),
        (party_set_slot, ":town", slot_center_has_barracks, ":lord"),
        # (display_message, "@Barracks build"),
    (try_end),

    (try_for_range, ":center", towns_begin, towns_end),
        (store_faction_of_party, ":fac", ":center"),
        (store_random_in_range, ":random_size", 0, 3),
        (call_script, "script_dplmc_send_patrol", ":center", ":center", ":random_size",":fac", -1),
    (try_end),

    #give titles to AI Rome
    (try_begin),
        (faction_slot_eq, "fac_kingdom_7", slot_faction_state, sfs_active),
        (call_script, "script_give_honorary_titles", "fac_kingdom_7"),
    (try_end),

    # initialize imperial bugdet
    (faction_set_slot, "fac_kingdom_7", slot_faction_hire, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_wages, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_garrison, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_garrison_wages, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_salary, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_spending_diplomacy, 0),

    (faction_set_slot, "fac_kingdom_7", slot_faction_taxes_govern, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_taxes_business, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_debts, 0),
    (faction_set_slot, "fac_kingdom_7", slot_faction_treasury, 500000),
    (faction_set_slot, "fac_kingdom_7", slot_faction_emperors_bocket, -100000),

    (faction_set_slot, "fac_kingdom_7", slot_faction_tax_rate, 25),
    (faction_set_slot, "fac_kingdom_7", slot_faction_tax_rate_buisness, 20),

    # initialize disguise system
    (troop_set_slot, "trp_player", slot_troop_player_disguise_sets, disguise_pilgrim),

    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (call_script, "script_faction_recalculate_strength", ":faction_no"),
    (try_end),

    ## init custom legion
    (troop_set_slot, "trp_players_legion", slot_troop_banner_scene_prop, "spr_banner_legion_vexilium_deitoriana_xxi"),
    (troop_set_name, "trp_players_legion", "@Legio XXII Deiotariana"),
    (troop_set_plural_name, "trp_players_legion", "@Legio XXII Deiotariana"),
]),
#script_game_get_use_string
# This script is called from the game engine for getting using information text
# INPUT: used_scene_prop_id
# OUTPUT: s0
("game_get_use_string",[
    (store_script_param, ":instance_id", 1),
    (try_begin),
        (prop_instance_is_valid, ":instance_id"),
        (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
        (try_begin),
            (this_or_next|eq, ":scene_prop_id", "spr_winch_b"),
            (eq, ":scene_prop_id", "spr_winch"),
            (assign, ":effected_object", "spr_portcullis"),
        (else_try),
            (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
            (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
            (assign, ":effected_object", ":scene_prop_id"),
        (try_end),

        (scene_prop_get_slot, ":item_situation", ":instance_id", scene_prop_open_or_close_slot),

        (try_begin), #opening/closing portcullis
            (eq, ":effected_object", "spr_portcullis"),
            (try_begin),
                (eq, ":item_situation", 0),
                (str_store_string, s0, "str_open_gate"),
            (else_try),
                (str_store_string, s0, "str_close_gate"),
            (try_end),
        (else_try), #arminius tomb
            (eq, ":scene_prop_id", "spr_arminius_tomb"),
            (str_store_string, s0, "str_arminius_tomb_use"),
        (else_try), #arminius tomb
            (eq, ":scene_prop_id", "spr_rescue_door"),
            (try_begin),
                (check_quest_active, "qst_wlodowiecus_adventure_3"),
                (quest_slot_eq, "qst_wlodowiecus_adventure_3", slot_quest_current_state, 9),
                (str_store_string, s0, "@Rescue Mathildiz."),
            (else_try),
                (str_store_string, s0, "@Locked door."),
            (try_end),
        (else_try), #arminius tomb
            (eq, ":scene_prop_id", "spr_roman_toilet_use"),
            (str_store_string, s0, "@Clean the toilet."),
        (else_try), #arminius tomb
            (eq, ":scene_prop_id", "spr_roman_undress"),
            (assign, ":item_to_remove", 0),
            (get_player_agent_no, ":player"),
            (agent_is_active, ":player"),
            (agent_is_alive, ":player"),
            (try_for_range, ":slot", ek_item_0, ek_horse),
                (agent_get_item_slot, ":cur_item", ":player", ":slot"),
                (gt, ":cur_item", -1),
                (val_add, ":item_to_remove", 1),
            (try_end),
            (try_begin),
                (ge, ":item_to_remove", 1),
                (str_store_string, s0, "@Undress yourself."),
            (else_try),
                (str_store_string, s0, "@Dress yourself."),
            (try_end),
        (else_try), #egypt texts
            (this_or_next|eq, ":scene_prop_id", "spr_wall_painting_heroglyphs2"),
            (eq, ":scene_prop_id", "spr_wall_painting_heroglyphs"),
            (str_store_string, s0, "str_hieroglyphs_use"),
        (else_try), #opening/closing door
            (this_or_next|eq, ":effected_object", "spr_door_destructible"),
            (this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
            (this_or_next|eq, ":effected_object", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":effected_object", "spr_castle_f_sally_door_a"),
            (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_left"),
            (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_right"),
            (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_left"),
            (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_right"),
            (eq, ":effected_object", "spr_castle_f_door_a"),

            (try_begin),
                (eq, ":item_situation", 0),
                (str_store_string, s0, "str_open_door"),
            (else_try),
                (str_store_string, s0, "str_close_door"),
            (try_end),
        (else_try), #raising/dropping ladder
            (try_begin),
                (eq, ":item_situation", 0),
                (str_store_string, s0, "str_raise_ladder"),
            (else_try),
                (str_store_string, s0, "str_drop_ladder"),
            (try_end),
        (try_end),
    (try_end),
]),

# script_game_quick_start
# This script is called from the game engine for initializing the global variables for tutorial, multiplayer and custom battle modes.
# INPUT:
# none
# OUTPUT:
# none
("game_quick_start",[
    (set_shader_param_float, "@vSeason", 0),
    (set_fixed_point_multiplier,1),
    (assign, "$wind_power", 1), #value in range of 0 (no wind) to 3 (extreme wind)
    (set_shader_param_float, "@vWindStrength", "$wind_power"),
    (set_shader_param_float, "@vWindDirection", 30),#30 degrees

    #for quick battle mode
    (assign, "$g_is_quick_battle", 0),
    (assign, "$g_quick_battle_game_type", 0),
    (assign, "$g_quick_battle_troop", quick_battle_troops_begin),
    (assign, "$g_quick_battle_map", quick_battle_scenes_begin),
    (assign, "$g_quick_battle_team_1_faction", "fac_kingdom_1"),
    (assign, "$g_quick_battle_team_2_faction", "fac_kingdom_2"),
    (assign, "$g_quick_battle_army_1_size", 25),
    (assign, "$g_quick_battle_army_2_size", 25),
    #(assign, "$form_ai_off", 0),

    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_infantry, "trp_mountain_bandit"),
    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_infantry, "trp_sea_raider"),
    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_archer, "trp_forest_bandit"),
    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_archer, "trp_taiga_bandit"),
    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_cavalry, "trp_steppe_bandit"),
    (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_cavalry, "trp_desert_bandit"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_infantry, "trp_dacian_flaxman_heavy"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_infantry, "trp_dacian_light_spearman"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_archer, "trp_dacian_skirmishers"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_archer, "trp_dacian_archers"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_cavalry, "trp_dacian_noble_cav"),
    (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_cavalry, "trp_dacian_noble_inf"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_infantry, "trp_celtic_light_clubman"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_infantry, "trp_celtic_naked_swordman"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_archer, "trp_celtic_skirmisher"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_archer, "trp_celtic_archer"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_cavalry, "trp_celtic_horseman"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_cavalry, "trp_celtic_noble_swords"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_infantry, "trp_sarmatian_light_spearman"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_infantry, "trp_sarmatian_archers"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_archer, "trp_sarmatian_light_horsearcher"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_archer, "trp_sarmatian_heavy_horsearcher"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_cavalry, "trp_sarmatian_heavy_horseman"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_cavalry, "trp_sarmatian_noble_horseman"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_infantry, "trp_germanic_light_clubman"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_infantry, "trp_germanic_noble_spearman"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_archer, "trp_germanic_skirmisher"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_archer, "trp_germanic_slinger"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_cavalry, "trp_germanic_cavalry"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_cavalry, "trp_germanic_berserker"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_infantry, "trp_eastern_light_axeman"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_infantry, "trp_eastern_heavy_inf"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_archer, "trp_eastern_slinger"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_archer, "trp_eastern_light_archer"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_cavalry, "trp_eastern_horsearcher"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_cavalry, "trp_eastern_medium_horseman"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_infantry, "trp_eastern_heavy_inf"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_infantry, "trp_eastern_heavy_spearman"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_archer, "trp_eastern_skrimisher"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_archer, "trp_eastern_light_archer"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_cavalry, "trp_eastern_medium_horseman"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_cavalry, "trp_eastern_cataphract"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_1_infantry, "trp_aux_inf_tungrorum"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_2_infantry, "trp_aux_inf_batavorum"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_1_archer, "trp_aux_archer"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_2_archer, "trp_aux_archer_praetoriana"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_1_cavalry, "trp_aux_cav"),
    (faction_set_slot, "fac_kingdom_7", slot_faction_quick_battle_tier_2_cavalry, "trp_aux_cav_praetoriani"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_1_infantry, "trp_legio_i_adjutrix"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_2_infantry, "trp_legio_i_adjutrix"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_1_archer, "trp_centurio_west"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_2_archer, "trp_signifer"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_1_cavalry, "trp_vexilarius_i"),
    (faction_set_slot, "fac_kingdom_8", slot_faction_quick_battle_tier_2_cavalry, "trp_aquilifer_i"),
    #for multiplayer mode
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_1_infantry, "trp_praetoriani_milites"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_2_infantry, "trp_praetoriani_milites"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_1_archer, "trp_centurio_preatoriani"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_2_archer, "trp_signifer"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_1_cavalry, "trp_vexilarius_praetoriani"),
    (faction_set_slot, "fac_kingdom_9", slot_faction_quick_battle_tier_2_cavalry, "trp_aquilifer_praetoriani"),

    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_1_infantry, "trp_gladiator_murmillo"),
    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_2_infantry, "trp_gladiator_thraex"),
    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_2_archer, "trp_gladiator_gladiatrix"),
    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_1_archer, "trp_gladiator_sagittarius"),
    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_1_cavalry, "trp_gladiator_euqes"),
    (faction_set_slot, "fac_gladiators", slot_faction_quick_battle_tier_2_cavalry, "trp_gladiator_retiarius"),

    #faction banners
    (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_1"),
    (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_2"),
    (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_3"),
    (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_4"),
    (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_5"),
    (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_6"),

    (faction_set_slot, "fac_kingdom_7", slot_faction_banner, "mesh_banner_kingdom_7"),

    (faction_set_slot, "fac_gladiators", slot_faction_banner, "mesh_banner_42"),

    (call_script, "script_initialize_banner_info"),
    (call_script, "script_set_faction_icons"),
]),

#script_game_missile_dives_into_water
# Called each time a missile dives into water
# INPUT
# script param 1 = missile item no
# script param 2 = missile item modifier
# script param 3 = launcher item no
# script param 4 = launcher item modifier
# script param 5 = shooter agent no
# script param 6 = missile no
# pos1 = water impact position and rotation
# script_game_missile_dives_into_water
# Input: arg1 = missile_item_id, arg2 = launcher_item_id, arg3 =
# shooter_agent_id, pos1 = missile_position_on_water
# Output: none
("game_missile_dives_into_water",[
    (copy_position, pos33, pos1),
    (particle_system_burst_no_sync, "psys_water_hit_a", pos33, 8),
    (position_move_z, pos33, 5, 1),
    (particle_system_burst_no_sync, "psys_water_hit_b", pos33, 4),
    (play_sound_at_position,"snd_missile_dive",pos33),
]),

("game_set_scenes_for_towns",[
    #scenen
    # Towns (loop)
    (try_for_range, ":town_no", towns_begin, towns_end),#ich verwend die selben scenen, sonst werd ich wahnsinnig
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_7"),#romer
        (party_set_slot,":town_no", slot_town_center, "scn_town_1_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_1_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_1_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_1_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_1_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_1_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_1_arena"),
    (else_try),
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_1"),#dacer
        (party_set_slot,":town_no", slot_town_center, "scn_town_15_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_15_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_15_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_15_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_15_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_15_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_15_arena"),
    (else_try),
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_3"),#nomaden
        (party_set_slot,":town_no", slot_town_center, "scn_town_22_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_22_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_22_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_22_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_22_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_22_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_22_arena"),
    (else_try),
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_9"),#bosporian
        (party_set_slot,":town_no", slot_town_center, "scn_town_bosporan_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_bosporan_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_bosporan_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_bosporan_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_bosporan_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_bosporan_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_bosporan_arena"),
    (else_try),
        (this_or_next|party_slot_eq, ":town_no", slot_center_culture, "fac_culture_2"),#britten
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_2_1"),#britten
        (party_set_slot,":town_no", slot_town_center, "scn_town_3_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_3_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_3_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_3_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_3_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_3_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_3_arena"),
    (else_try),
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_4"),#germanen
        (party_set_slot,":town_no", slot_town_center, "scn_town_4_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_4_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_4_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_4_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_4_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_4_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_4_arena"),
    (else_try),
        (this_or_next|party_slot_eq, ":town_no", slot_center_culture, "fac_culture_5"),#eastern
        (this_or_next|party_slot_eq, ":town_no", slot_center_culture, "fac_culture_8"),#eastern
        (party_slot_eq, ":town_no", slot_center_culture, "fac_culture_6"),
        (party_set_slot,":town_no", slot_town_center, "scn_town_2_center"),
        (party_set_slot,":town_no", slot_town_castle, "scn_town_2_castle"),
        (party_set_slot,":town_no", slot_town_prison, "scn_town_2_prison"),
        (party_set_slot,":town_no", slot_town_walls, "scn_town_2_walls"),
        (party_set_slot,":town_no", slot_town_tavern, "scn_town_2_tavern"),
        (party_set_slot,":town_no", slot_town_store, "scn_town_2_store"),
        (party_set_slot,":town_no", slot_town_arena, "scn_town_2_arena"),
    (try_end),
    #special towns
    (party_set_slot,"p_town_43", slot_town_center, "scn_town_26_center"),
    (party_set_slot,"p_town_43", slot_town_castle, "scn_town_26_castle"),
    (party_set_slot,"p_town_43", slot_town_prison, "scn_town_26_prison"),
    (party_set_slot,"p_town_43", slot_town_walls, "scn_town_26_walls"),
    (party_set_slot,"p_town_43", slot_town_tavern, "scn_town_26_tavern"),
    (party_set_slot,"p_town_43", slot_town_store, "scn_town_26_store"),
    (party_set_slot,"p_town_43", slot_town_arena, "scn_town_26_arena"),

    (party_set_slot,"p_town_40", slot_town_center, "scn_town_48_center"),
    (party_set_slot,"p_town_40", slot_town_castle, "scn_town_48_castle"),
    (party_set_slot,"p_town_40", slot_town_prison, "scn_town_48_prison"),
    (party_set_slot,"p_town_40", slot_town_walls, "scn_town_48_walls"),
    (party_set_slot,"p_town_40", slot_town_tavern, "scn_town_48_tavern"),
    (party_set_slot,"p_town_40", slot_town_store, "scn_town_48_store"),
    (party_set_slot,"p_town_40", slot_town_arena, "scn_town_48_arena"),

    (party_set_slot,"p_town_14", slot_town_center, "scn_colchis_center"),
    (party_set_slot,"p_town_14", slot_town_castle, "scn_colchis_castle"),
    (party_set_slot,"p_town_14", slot_town_prison, "scn_colchis_prison"),
    (party_set_slot,"p_town_14", slot_town_walls, "scn_colchis_walls"),
    (party_set_slot,"p_town_14", slot_town_tavern, "scn_colchis_tavern"),
    (party_set_slot,"p_town_14", slot_town_store, "scn_colchis_store"),
    (party_set_slot,"p_town_14", slot_town_arena, "scn_colchis_arena"),

    (party_set_slot,"p_town_37", slot_town_center, "scn_athen_center"),
    (party_set_slot,"p_town_37", slot_town_castle, "scn_athen_castle"),
    (party_set_slot,"p_town_37", slot_town_prison, "scn_athen_prison"),
    (party_set_slot,"p_town_37", slot_town_walls, "scn_athen_walls"),
    (party_set_slot,"p_town_37", slot_town_tavern, "scn_athen_tavern"),
    (party_set_slot,"p_town_37", slot_town_store, "scn_athen_store"),
    (party_set_slot,"p_town_37", slot_town_arena, "scn_athen_arena"),

    (party_set_slot,"p_town_49", slot_town_center, "scn_town_germanic_east_center"),
    (party_set_slot,"p_town_49", slot_town_castle, "scn_town_germanic_east_castle"),
    (party_set_slot,"p_town_49", slot_town_prison, "scn_town_germanic_east_prison"),
    (party_set_slot,"p_town_49", slot_town_walls, "scn_town_germanic_east_walls"),
    (party_set_slot,"p_town_49", slot_town_tavern, "scn_town_germanic_east_tavern"),
    (party_set_slot,"p_town_49", slot_town_store, "scn_town_germanic_east_store"),
    (party_set_slot,"p_town_49", slot_town_arena, "scn_town_germanic_east_arena"),

    (party_set_slot,"p_town_50", slot_town_center, "scn_town_caucasus_center"),
    (party_set_slot,"p_town_50", slot_town_castle, "scn_town_caucasus_castle"),
    (party_set_slot,"p_town_50", slot_town_prison, "scn_town_caucasus_prison"),
    (party_set_slot,"p_town_50", slot_town_walls, "scn_town_caucasus_walls"),
    (party_set_slot,"p_town_50", slot_town_tavern, "scn_town_caucasus_tavern"),
    (party_set_slot,"p_town_50", slot_town_store, "scn_town_caucasus_store"),
    (party_set_slot,"p_town_50", slot_town_arena, "scn_town_caucasus_arena"),

    (party_set_slot,"p_town_24", slot_town_center, "scn_town_34_center"),
    (party_set_slot,"p_town_24", slot_town_castle, "scn_town_34_castle"),
    (party_set_slot,"p_town_24", slot_town_prison, "scn_town_34_prison"),
    (party_set_slot,"p_town_24", slot_town_walls, "scn_town_34_walls"),
    (party_set_slot,"p_town_24", slot_town_tavern, "scn_town_34_tavern"),
    (party_set_slot,"p_town_24", slot_town_store, "scn_town_34_store"),
    (party_set_slot,"p_town_24", slot_town_arena, "scn_town_34_arena"),

    (party_set_slot,"p_town_19", slot_town_center, "scn_town_20_center"),
    (party_set_slot,"p_town_19", slot_town_castle, "scn_town_20_castle"),
    (party_set_slot,"p_town_19", slot_town_prison, "scn_town_20_prison"),
    (party_set_slot,"p_town_19", slot_town_walls, "scn_town_20_walls"),
    (party_set_slot,"p_town_19", slot_town_tavern, "scn_town_20_tavern"),
    (party_set_slot,"p_town_19", slot_town_store, "scn_town_20_store"),
    (party_set_slot,"p_town_19", slot_town_arena, "scn_town_20_arena"),

    (party_set_slot,"p_town_27", slot_town_center, "scn_ctesiphon"),##cetesiphon
    (party_set_slot,"p_town_27", slot_town_castle, "scn_town_19_castle"),
    (party_set_slot,"p_town_27", slot_town_prison, "scn_town_19_prison"),
    (party_set_slot,"p_town_27", slot_town_walls, "scn_ctesiphon_walls"),
    (party_set_slot,"p_town_27", slot_town_tavern, "scn_town_19_tavern"),
    (party_set_slot,"p_town_27", slot_town_store, "scn_town_19_store"),
    (party_set_slot,"p_town_27", slot_town_arena, "scn_ctesiphon_arena"),

    (party_set_slot,"p_town_51", slot_town_center, "scn_nisha"),##cetesiphon
    (party_set_slot,"p_town_51", slot_town_castle, "scn_nisha_castle"),
    (party_set_slot,"p_town_51", slot_town_prison, "scn_nisha_prison"),
    (party_set_slot,"p_town_51", slot_town_walls, "scn_nisha_walls"),
    (party_set_slot,"p_town_51", slot_town_tavern, "scn_nisha_tavern"),
    (party_set_slot,"p_town_51", slot_town_store, "scn_nisha_store"),
    (party_set_slot,"p_town_51", slot_town_arena, "scn_nisha_arena"),

    (party_set_slot,"p_town_20", slot_town_center, "scn_town_7_center"),
    (party_set_slot,"p_town_20", slot_town_castle, "scn_town_7_castle"),
    (party_set_slot,"p_town_20", slot_town_prison, "scn_town_7_prison"),
    (party_set_slot,"p_town_20", slot_town_walls, "scn_town_7_walls"),
    (party_set_slot,"p_town_20", slot_town_tavern, "scn_town_7_tavern"),
    (party_set_slot,"p_town_20", slot_town_store, "scn_town_7_store"),
    (party_set_slot,"p_town_20", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_10", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_10", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_10", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_10", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_10", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_10", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_10", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_45", slot_town_center, "scn_germanic_town_center"),
    (party_set_slot,"p_town_45", slot_town_castle, "scn_germanic_town_castle"),
    (party_set_slot,"p_town_45", slot_town_prison, "scn_germanic_town_prison"),
    (party_set_slot,"p_town_45", slot_town_walls, "scn_germanic_town_walls"),
    (party_set_slot,"p_town_45", slot_town_tavern,"scn_germanic_town_tavern"),
    (party_set_slot,"p_town_45", slot_town_store, "scn_germanic_town_store"),
    (party_set_slot,"p_town_45", slot_town_arena, "scn_germanic_town_arena"),

    (party_set_slot,"p_town_13", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_13", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_13", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_13", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_13", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_13", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_13", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_22", slot_town_center, "scn_antiochia"),
    (party_set_slot,"p_town_22", slot_town_walls, "scn_antiochia_wall"),
    (party_set_slot,"p_town_22", slot_town_arena, "scn_antiochia_arena"),
    (party_set_slot,"p_town_22", slot_town_castle, "scn_antiochia_castle"),
    (party_set_slot,"p_town_22", slot_town_tavern, "scn_antiochia_tavern"),

    (party_set_slot,"p_town_47", slot_town_center, "scn_palmyra"),
    (party_set_slot,"p_town_47", slot_town_walls, "scn_palmyra_wall"),
    (party_set_slot,"p_town_47", slot_town_arena, "scn_palmyra_arena"),
    (party_set_slot,"p_town_47", slot_town_castle, "scn_palmyra_castle"),
    (party_set_slot,"p_town_47", slot_town_tavern, "scn_palmyra_tavern"),
    (party_set_slot,"p_town_47", slot_town_prison, "scn_palmyra_prison"),
    (party_set_slot,"p_town_47", slot_town_store, "scn_palmyra_store"),

    (party_set_slot,"p_town_22", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_22", slot_town_prison, "scn_town_9_prison"),

    (party_set_slot,"p_town_28", slot_town_center, "scn_carthago_center"),
    (party_set_slot,"p_town_28", slot_town_castle, "scn_carthago_castle"),
    (party_set_slot,"p_town_28", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_28", slot_town_walls, "scn_carthago_walls"),
    (party_set_slot,"p_town_28", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_28", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_28", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_11", slot_town_center, "scn_dacian_capital_center"),
    (party_set_slot,"p_town_11", slot_town_castle, "scn_dacian_capital_castle"),
    (party_set_slot,"p_town_11", slot_town_prison, "scn_dacian_capital_prison"),
    (party_set_slot,"p_town_11", slot_town_walls, "scn_dacian_capital_walls"),
    (party_set_slot,"p_town_11", slot_town_tavern, "scn_dacian_capital_tavern"),
    (party_set_slot,"p_town_11", slot_town_store, "scn_dacian_capital_store"),
    (party_set_slot,"p_town_11", slot_town_arena, "scn_dacian_capital_arena"),

    (party_set_slot,"p_town_33", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_33", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_33", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_33", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_33", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_33", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_33", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_36", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_36", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_36", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_36", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_36", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_36", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_36", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_35", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_35", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_35", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_35", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_35", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_35", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_35", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_4", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_4", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_4", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_4", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_4", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_4", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_4", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_32", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_32", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_32", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_32", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_32", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_32", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_32", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_34", slot_town_center, "scn_town_9_center"),
    (party_set_slot,"p_town_34", slot_town_castle, "scn_town_9_castle"),
    (party_set_slot,"p_town_34", slot_town_prison, "scn_town_9_prison"),
    (party_set_slot,"p_town_34", slot_town_walls, "scn_town_9_walls"),
    (party_set_slot,"p_town_34", slot_town_tavern, "scn_town_9_tavern"),
    (party_set_slot,"p_town_34", slot_town_store, "scn_town_9_store"),
    (party_set_slot,"p_town_34", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_38", slot_town_center, "scn_town_41_center"),
    (party_set_slot,"p_town_38", slot_town_castle, "scn_town_41_castle"),
    (party_set_slot,"p_town_38", slot_town_prison, "scn_town_41_prison"),
    (party_set_slot,"p_town_38", slot_town_walls, "scn_town_41_walls"),
    (party_set_slot,"p_town_38", slot_town_tavern, "scn_town_41_tavern"),
    (party_set_slot,"p_town_38", slot_town_store, "scn_town_41_store"),
    (party_set_slot,"p_town_38", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_8", slot_town_center, "scn_town_32_center"),
    (party_set_slot,"p_town_8", slot_town_castle, "scn_town_32_castle"),
    (party_set_slot,"p_town_8", slot_town_prison, "scn_town_32_prison"),
    (party_set_slot,"p_town_8", slot_town_walls, "scn_town_32_walls"),
    (party_set_slot,"p_town_8", slot_town_tavern, "scn_town_32_tavern"),
    (party_set_slot,"p_town_8", slot_town_store, "scn_town_32_store"),
    (party_set_slot,"p_town_8", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_16", slot_town_center, "scn_town_32_center"),
    (party_set_slot,"p_town_16", slot_town_castle, "scn_town_32_castle"),
    (party_set_slot,"p_town_16", slot_town_prison, "scn_town_32_prison"),
    (party_set_slot,"p_town_16", slot_town_walls, "scn_town_32_walls"),
    (party_set_slot,"p_town_16", slot_town_tavern, "scn_town_32_tavern"),
    (party_set_slot,"p_town_16", slot_town_store, "scn_town_32_store"),
    (party_set_slot,"p_town_16", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_30", slot_town_center, "scn_town_32_center"),
    (party_set_slot,"p_town_30", slot_town_castle, "scn_town_32_castle"),
    (party_set_slot,"p_town_30", slot_town_prison, "scn_town_32_prison"),
    (party_set_slot,"p_town_30", slot_town_walls, "scn_town_32_walls"),
    (party_set_slot,"p_town_30", slot_town_tavern, "scn_town_32_tavern"),
    (party_set_slot,"p_town_30", slot_town_store, "scn_town_32_store"),
    (party_set_slot,"p_town_30", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_3", slot_town_center, "scn_town_13_center"),
    (party_set_slot,"p_town_3", slot_town_castle, "scn_town_13_castle"),
    (party_set_slot,"p_town_3", slot_town_prison, "scn_town_13_prison"),
    (party_set_slot,"p_town_3", slot_town_walls, "scn_town_13_walls"),
    (party_set_slot,"p_town_3", slot_town_tavern, "scn_town_13_tavern"),
    (party_set_slot,"p_town_3", slot_town_store, "scn_town_13_store"),
    (party_set_slot,"p_town_3", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_21", slot_town_center, "scn_town_13_center"),
    (party_set_slot,"p_town_21", slot_town_castle, "scn_town_13_castle"),
    (party_set_slot,"p_town_21", slot_town_prison, "scn_town_13_prison"),
    (party_set_slot,"p_town_21", slot_town_walls, "scn_town_13_walls"),
    (party_set_slot,"p_town_21", slot_town_tavern, "scn_town_13_tavern"),
    (party_set_slot,"p_town_21", slot_town_store, "scn_town_13_store"),
    (party_set_slot,"p_town_21", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_2", slot_town_center, "scn_town_13_center"),
    (party_set_slot,"p_town_2", slot_town_castle, "scn_town_13_castle"),
    (party_set_slot,"p_town_2", slot_town_prison, "scn_town_13_prison"),
    (party_set_slot,"p_town_2", slot_town_walls, "scn_town_13_walls"),
    (party_set_slot,"p_town_2", slot_town_tavern, "scn_town_13_tavern"),
    (party_set_slot,"p_town_2", slot_town_store, "scn_town_13_store"),
    (party_set_slot,"p_town_2", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_5", slot_town_center, "scn_town_13_center"),
    (party_set_slot,"p_town_5", slot_town_castle, "scn_town_13_castle"),
    (party_set_slot,"p_town_5", slot_town_prison, "scn_town_13_prison"),
    (party_set_slot,"p_town_5", slot_town_walls, "scn_town_13_walls"),
    (party_set_slot,"p_town_5", slot_town_tavern, "scn_town_13_tavern"),
    (party_set_slot,"p_town_5", slot_town_store, "scn_town_13_store"),
    (party_set_slot,"p_town_5", slot_town_arena, "scn_town_7_arena"),

    (party_set_slot,"p_town_6", slot_town_walls, "scn_rome_walls"),
    (party_set_slot,"p_town_6", slot_town_center, "scn_temple_of_concordia"),
    (party_set_slot,"p_town_6", slot_town_castle, "scn_roman_town_hall"),
    (party_set_slot,"p_town_6", slot_town_prison, "scn_rome_prison"),

    (party_set_slot,"p_town_18", slot_town_center, "scn_town_10_center"),
    (party_set_slot,"p_town_18", slot_town_castle, "scn_town_10_castle"),
    (party_set_slot,"p_town_18", slot_town_walls, "scn_town_10_walls"),
    (party_set_slot,"p_town_18", slot_town_tavern, "scn_town_10_tavern"),
    (party_set_slot,"p_town_18", slot_town_arena, "scn_town_10_arena"),

    (party_set_slot,"p_town_48", slot_town_center, "scn_theben_center"),
    (party_set_slot,"p_town_48", slot_town_castle, "scn_theben_castle"),
    (party_set_slot,"p_town_48", slot_town_walls, "scn_theben_walls"),
    (party_set_slot,"p_town_48", slot_town_tavern, "scn_theben_tavern"),

    (party_set_slot,"p_town_42", slot_town_center, "scn_dacidava_center"),
    (party_set_slot,"p_town_42", slot_town_castle, "scn_dacidava_castle"),
    (party_set_slot,"p_town_42", slot_town_walls, "scn_dacidava_walls"),
    (party_set_slot,"p_town_42", slot_town_tavern, "scn_dacidava_tavern"),

    (party_set_slot,"p_town_12", slot_town_tavern, "scn_lugdunum_tavern"),
    (party_set_slot,"p_town_12", slot_town_castle, "scn_lugdunum_castle"),
    (party_set_slot,"p_town_12", slot_town_walls, "scn_lugdunum_walls"),
    (party_set_slot,"p_town_12", slot_town_center, "scn_lugdunum_center"),
    (party_set_slot,"p_town_12", slot_town_prison, "scn_lugdunum_prison"),
    (party_set_slot,"p_town_12", slot_town_store, "scn_lugdunum_store"),
    (party_set_slot,"p_town_12", slot_town_arena, "scn_lugdunum_arena"),
#carthago: p_town_28,
# athen p_town_37
# alexandria p_town_20
#habours roman: p_town_10, p_town_22, p_town_13, p_town_33, p_town_36, p_town_35 (thessalonika), p_town_4, p_town_32, p_town_34
#mountain scene: town_8, town_38, town_30
#new generic scene: town_3, town_21, town_5, town_2
#castle scenen
    (try_for_range, ":castle_no", castles_begin, castles_end),#ich verwend die selben scenen, sonst werd ich wahnsinnig
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_7"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_1_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_1_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_1_prison"),
    (else_try),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_1"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_2_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_2_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_2_prison"),
    (else_try),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_3"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_3_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_3_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_3_prison"),
    (else_try),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_9"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_bosporan_ex"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_bosporan_in"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_bosporan_prison"),
    (else_try),
        (this_or_next|party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_2"),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_2_1"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_4_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_4_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_4_prison"),
    (else_try),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_4"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_5_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_5_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_5_prison"),
    (else_try),
        (this_or_next|party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_5"),
        (this_or_next|party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_8"),
        (party_slot_eq, ":castle_no", slot_center_culture, "fac_culture_6"),
        (party_set_slot,":castle_no", slot_castle_exterior, "scn_castle_6_exterior"),
        (party_set_slot,":castle_no", slot_town_castle, "scn_castle_6_interior"),
        (party_set_slot,":castle_no", slot_town_prison, "scn_castle_6_prison"),
 	  (try_end),

    (party_set_slot,"p_castle_41", slot_castle_exterior, "scn_roman_african_castle_ex"),
    (party_set_slot,"p_castle_41", slot_town_castle, "scn_castle_bosporan_in"),
    (party_set_slot,"p_castle_41", slot_town_prison, "scn_roman_african_castle_prison"),

    (party_set_slot,"p_castle_35", slot_castle_exterior, "scn_salona_ex"),
    (party_set_slot,"p_castle_35", slot_town_castle, "scn_salona_in"),
    (party_set_slot,"p_castle_35", slot_town_prison, "scn_salona_prison"),

    (party_set_slot,"p_castle_14", slot_castle_exterior, "scn_castle_56_exterior"),
    (party_set_slot,"p_castle_14", slot_town_castle, "scn_castle_56_interior"),
    (party_set_slot,"p_castle_14", slot_town_prison, "scn_castle_56_prison"),

    (party_set_slot,"p_castle_57", slot_castle_exterior, "scn_commu_exterrior"),
    (party_set_slot,"p_castle_57", slot_town_castle, "scn_commu_interior"),
    (party_set_slot,"p_castle_57", slot_town_prison, "scn_commu_prison"),

    (party_set_slot,"p_castle_30", slot_castle_exterior, "scn_arbela_exterior"),
    (party_set_slot,"p_castle_30", slot_town_castle, "scn_arbela_interior"),

    (party_set_slot,"p_castle_79", slot_castle_exterior, "scn_samosata_exterior"),
    (party_set_slot,"p_castle_79", slot_town_castle, "scn_samosata_interior"),
    (party_set_slot,"p_castle_79", slot_town_prison, "scn_samosata_prison"),

    (party_set_slot,"p_castle_65", slot_castle_exterior, "scn_susa_exterior"),
    (party_set_slot,"p_castle_65", slot_town_castle, "scn_samosata_interior"),
    (party_set_slot,"p_castle_65", slot_town_prison, "scn_samosata_prison"),

    (party_set_slot,"p_castle_42", slot_castle_exterior, "scn_parthian_castle_ex"),
    (party_set_slot,"p_castle_42", slot_town_castle, "scn_parthian_castle_in"),
    (party_set_slot,"p_castle_42", slot_town_prison, "scn_parthian_castle_pr"),
    ##germanic castles:
    #p_castle_60#
    #p_castle_50#
    #p_castle_52#
    #p_castle_51#
    #p_castle_32#
    #p_castle_33#
    #p_castle_53#
    #p_castle_49#
    #p_castle_8#
    #p_castle_36#
    #p_castle_22, only 22 uses generic castle
    (party_set_slot,"p_castle_50", slot_castle_exterior, "scn_castle_500_exterior"),#
    (party_set_slot,"p_castle_50", slot_town_castle, "scn_castle_500_interior"),
    (party_set_slot,"p_castle_50", slot_town_prison, "scn_castle_500_prison"),

    (party_set_slot,"p_castle_51", slot_castle_exterior, "scn_castle_10_exterior"),#
    (party_set_slot,"p_castle_51", slot_town_castle, "scn_castle_10_interior"),
    (party_set_slot,"p_castle_51", slot_town_prison, "scn_castle_10_prison"),

    (party_set_slot,"p_castle_52", slot_castle_exterior, "scn_castle_germanic_east_ex"),#
    (party_set_slot,"p_castle_52", slot_town_castle, "scn_castle_germanic_east_in"),
    (party_set_slot,"p_castle_52", slot_town_prison, "scn_castle_germanic_east_prison"),

    (party_set_slot,"p_castle_60", slot_castle_exterior, "scn_castle_germanic_sea_1_ex"),#
    (party_set_slot,"p_castle_60", slot_town_castle, "scn_castle_germanic_sea_1_in"),
    (party_set_slot,"p_castle_60", slot_town_prison, "scn_castle_germanic_sea_1_prison"),

    (party_set_slot,"p_castle_32", slot_castle_exterior, "scn_castle_11_exterior"),#
    (party_set_slot,"p_castle_32", slot_town_castle, "scn_castle_11_interior"),
    (party_set_slot,"p_castle_32", slot_town_prison, "scn_castle_11_prison"),

    (party_set_slot,"p_castle_53", slot_castle_exterior, "scn_castle_12_exterior"),#
    (party_set_slot,"p_castle_53", slot_town_castle, "scn_castle_12_interior"),
    (party_set_slot,"p_castle_53", slot_town_prison, "scn_castle_12_prison"),

    (party_set_slot,"p_castle_49", slot_castle_exterior, "scn_castle_32_exterior"),#
    (party_set_slot,"p_castle_49", slot_town_castle, "scn_castle_32_interior"),
    (party_set_slot,"p_castle_49", slot_town_prison, "scn_castle_32_prison"),

    (party_set_slot,"p_castle_33", slot_castle_exterior, "scn_castle_34_exterior"),#
    (party_set_slot,"p_castle_33", slot_town_castle, "scn_castle_34_interior"),
    (party_set_slot,"p_castle_33", slot_town_prison, "scn_castle_34_prison"),

    (party_set_slot,"p_castle_8", slot_castle_exterior, "scn_germanic_castle_1_exterior"),#
    (party_set_slot,"p_castle_8", slot_town_castle, "scn_germanic_castle_1_interior"),
    (party_set_slot,"p_castle_8", slot_town_prison, "scn_germanic_castle_1_prison"),

    (party_set_slot,"p_castle_36", slot_castle_exterior, "scn_germanic_castle_1_exterior"),#
    (party_set_slot,"p_castle_36", slot_town_castle, "scn_germanic_castle_1_interior"),
    (party_set_slot,"p_castle_36", slot_town_prison, "scn_germanic_castle_1_prison"),

    ##parthian castles:
    #p_castle_42
    #p_castle_40
    #p_castle_48
    #p_castle_30
    ##forts in israel
    #p_castle_45
    #p_castle_46
    #p_castle_44
    (party_set_slot,"p_castle_40", slot_castle_exterior, "scn_castle_47_exterior"),

    (party_set_slot,"p_castle_38", slot_castle_exterior, "scn_castle_30_exterior"),
    (party_set_slot,"p_castle_38", slot_town_castle, "scn_castle_30_interior"),
    (party_set_slot,"p_castle_38", slot_town_prison, "scn_castle_30_prison"),

    (party_set_slot,"p_castle_26", slot_castle_exterior, "scn_castle_17_exterior"),
    (party_set_slot,"p_castle_26", slot_town_castle, "scn_castle_17_interior"),
    (party_set_slot,"p_castle_26", slot_town_prison, "scn_castle_17_prison"),

    (party_set_slot,"p_castle_68", slot_castle_exterior,"scn_castle_caucasus_exterior"),
    (party_set_slot,"p_castle_68", slot_town_castle,    "scn_castle_caucasus_interior"),
    (party_set_slot,"p_castle_68", slot_town_prison,    "scn_castle_caucasus_prison"),

    (party_set_slot,"p_castle_69", slot_castle_exterior,"scn_castle_caucasus_exterior"),
    (party_set_slot,"p_castle_69", slot_town_castle,    "scn_castle_caucasus_interior"),
    (party_set_slot,"p_castle_69", slot_town_prison,    "scn_castle_caucasus_prison"),

    (party_set_slot,"p_castle_70", slot_castle_exterior,"scn_castle_caucasus_exterior"),
    (party_set_slot,"p_castle_70", slot_town_castle,    "scn_castle_caucasus_interior"),
    (party_set_slot,"p_castle_70", slot_town_prison,    "scn_castle_caucasus_prison"),

    (party_set_slot,"p_castle_44", slot_castle_exterior, "scn_castle_masada_ex"),
    (party_set_slot,"p_castle_44", slot_town_castle, "scn_castle_masada_in"),
    (party_set_slot,"p_castle_44", slot_town_prison, "scn_castle_masada_prison"),

    (party_set_slot,"p_castle_45", slot_castle_exterior, "scn_jotopata_ex"),
    (party_set_slot,"p_castle_45", slot_town_castle, "scn_jotopata_in"),
    (party_set_slot,"p_castle_45", slot_town_prison, "scn_jotopata_prison"),

    (party_set_slot,"p_castle_46", slot_castle_exterior, "scn_ceasarea_ex"),
    (party_set_slot,"p_castle_46", slot_town_castle, "scn_ceasarea_in"),
    (party_set_slot,"p_castle_46", slot_town_prison, "scn_ceasarea_prison"),

    (party_set_icon, "p_castle_46", "icon_fort_greek"),
    (party_set_icon, "p_castle_45", "icon_fort_greek"),
    (party_set_icon, "p_castle_44", "icon_fort_greek"),

    (party_set_slot,"p_castle_23", slot_castle_exterior, "scn_londinium"),#londinium
    (party_set_slot,"p_castle_23", slot_town_castle, "scn_londinium_castle"),#londinium
    (party_set_slot,"p_castle_23", slot_town_prison, "scn_londinium_prison"),#londinium

    (party_set_slot,"p_castle_16", slot_castle_exterior, "scn_roman_castle_2_exterior"),#colonia aggrippina
    (party_set_slot,"p_castle_16", slot_town_castle, "scn_roman_castle_2_interior"),#colonia aggrippina
    (party_set_slot,"p_castle_16", slot_town_prison, "scn_londinium_prison"),#colonia aggrippina

    (party_set_slot,"p_castle_24", slot_castle_exterior, "scn_roman_castle_1_exterior"),#Mogontiacum
    (party_set_slot,"p_castle_24", slot_town_castle, "scn_roman_castle_1_interior"),#Mogontiacum
    (party_set_slot,"p_castle_24", slot_town_prison, "scn_londinium_prison"),#Mogontiacum
    (party_set_slot,"p_castle_34", slot_castle_exterior, "scn_castellum"),#?

    (party_set_slot,"p_castle_9", slot_castle_exterior, "scn_castellum"),#?
    (party_set_slot,"p_castle_4", slot_castle_exterior, "scn_castellum"),#?

    (party_set_slot,"p_castle_20", slot_castle_exterior, "scn_castellum"),#?
    (party_set_slot,"p_castle_13", slot_castle_exterior, "scn_castellum"),#?
    (party_set_slot,"p_castle_27", slot_castle_exterior, "scn_castellum"),#?

    (party_set_slot,"p_castle_12", slot_castle_exterior, "scn_carnuntum_ex"),#?
    (party_set_slot,"p_castle_12", slot_town_castle, "scn_carnuntum_in"),#?
    (party_set_slot,"p_castle_12", slot_town_prison, "scn_carnuntum_prison"),#?

    #brytenwalda castle 63
    (party_set_slot,"p_castle_58", slot_castle_exterior, "scn_castle_caledonian_ex"),#?
    (party_set_slot,"p_castle_58", slot_town_castle, "scn_castle_caledonian_in"),#?
    (party_set_slot,"p_castle_58", slot_town_prison, "scn_castle_caledonian_prison"),#?

    (party_set_slot,"p_castle_7", slot_castle_exterior, "scn_dacian_castle_ex"),
    (party_set_slot,"p_castle_7", slot_town_castle, "scn_dacian_castle_in"),
    (party_set_slot,"p_castle_7", slot_town_prison, "scn_dacian_castle_prison"),

    (party_set_slot,"p_castle_18", slot_castle_exterior, "scn_dacian_castle_ex"),
    (party_set_slot,"p_castle_18", slot_town_castle, "scn_dacian_castle_in"),
    (party_set_slot,"p_castle_18", slot_town_prison, "scn_dacian_castle_prison"),

    (party_set_slot,"p_castle_6", slot_castle_exterior, "scn_castle_island_ex"),
    (party_set_slot,"p_castle_6", slot_town_castle, "scn_castle_island_in"),
    (party_set_slot,"p_castle_6", slot_town_prison, "scn_castle_island_prison"),

    (party_set_slot,"p_castle_63", slot_castle_exterior, "scn_castle_island_2_ex"),
    (party_set_slot,"p_castle_63", slot_town_castle, "scn_castle_island_2_in"),
    (party_set_slot,"p_castle_63", slot_town_prison, "scn_castle_island_prison"),

    (party_set_slot,"p_castle_62", slot_castle_exterior, "scn_castle_island_ex"),
    (party_set_slot,"p_castle_62", slot_town_castle, "scn_castle_island_in"),
    (party_set_slot,"p_castle_62", slot_town_prison, "scn_castle_island_prison"),

    (party_set_slot,"p_castle_61", slot_castle_exterior, "scn_castle_island_ex"),
    (party_set_slot,"p_castle_61", slot_town_castle, "scn_castle_island_in"),
    (party_set_slot,"p_castle_61", slot_town_prison, "scn_castle_island_prison"),

    (party_set_slot,"p_castle_47", slot_castle_exterior, "scn_petra_ex"),
    (party_set_slot,"p_castle_47", slot_town_castle, "scn_petra_in"),
    (party_set_slot,"p_castle_47", slot_town_prison, "scn_petra_prison"),

    (party_set_slot,"p_castle_64", slot_castle_exterior, "scn_africa_roman_castle"),
    (party_set_slot,"p_castle_64", slot_town_castle, "scn_africa_in"),
    (party_set_slot,"p_castle_64", slot_town_prison, "scn_africa_prison"),

    (party_set_slot,"p_castle_43", slot_castle_exterior, "scn_africa_roman_castle"),
    (party_set_slot,"p_castle_43", slot_town_castle, "scn_africa_in"),
    (party_set_slot,"p_castle_43", slot_town_prison, "scn_africa_prison"),

    (try_for_range, ":village_no", villages_begin, villages_end),
        (try_begin),
            (party_get_slot, ":province_cap", ":village_no", slot_village_bound_center),
            (party_get_slot, ":province", ":province_cap", slot_center_province),
            (party_set_slot, ":village_no", slot_center_province, ":province"),
        (try_end),
        #special scenes for this towns
        #p_town_20, p_town_48, p_town_47, p_town_40, p_town_27
        (try_begin),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_47"),#palmyra
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_palmyra"),
        (else_try),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_40"),#nisbis
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_euphrat"),
        (else_try),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_27"),#ctesiphon
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_94"),
        (else_try),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_19"),#Hierosolyma
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_judea"),
        (else_try),
            (party_slot_eq, ":village_no", slot_village_bound_center, "p_town_20"),
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_egypt_delta"),
        (else_try),
            (party_slot_eq, ":village_no", slot_village_bound_center, "p_town_48"),
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_egypt"),
        (else_try),
         ##special for deserts###
            (party_get_current_terrain, ":terrain", ":village_no"),
            (this_or_next|eq, ":terrain", rt_desert),
            (eq, ":terrain", rt_desert_forest),
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_102"),
        # (else_try),
        # ###else check if water is near and assign a water scene
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_7"),
        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_41"),
        #     (try_begin),
        #       (le, ":distance", 2),
        #       (party_set_slot,":village_no", slot_castle_exterior, "scn_village_1"),#passt
        #     (try_end),
        # (else_try),
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_1"),

        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_19"),
        #     (try_begin),
        #         (le, ":distance", 2),
        #         (party_set_slot,":village_no", slot_castle_exterior, "scn_village_95"),#passt
        #     (try_end),
        # (else_try),
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_3"),
        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_100"),
        #     (try_begin),
        #         (le, ":distance", 2),
        #         (party_set_slot,":village_no", slot_castle_exterior, "scn_village_42"),#passt
        #     (try_end),
        # (else_try),
        #     (this_or_next|party_slot_eq, ":village_no", slot_center_culture, "fac_culture_2"),
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_2"),
        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_19"),
        #     (try_begin),
        #         (le, ":distance", 2),
        #         (party_set_slot,":village_no", slot_castle_exterior, "scn_village_7"),#passt
        #     (try_end),
        # (else_try),
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_4"),
        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_74"),
        #     (try_begin),
        #         (le, ":distance", 2),
        #         (party_set_slot,":village_no", slot_castle_exterior, "scn_village_98"),#passt
        #     (try_end),
        # (else_try),
        #     (this_or_next|party_slot_eq, ":village_no", slot_center_culture, "fac_culture_8"),
        #     (this_or_next|party_slot_eq, ":village_no", slot_center_culture, "fac_culture_7"),
        #     (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_6"),
        #     (party_get_position,pos1,":village_no"),
        #     (map_get_water_position_around_position, pos2, pos1, 2),
        #     (party_set_position, "p_salt_mine", pos2),
        #     (store_distance_to_party_from_party, ":distance", "p_salt_mine", ":village_no"),
        #     #(party_set_slot,":village_no", slot_castle_exterior, "scn_village_2"),
        #     (try_begin),
        #         (le, ":distance", 2),
        #         (party_set_slot,":village_no", slot_castle_exterior, "scn_village_43"),
        #     (try_end),
          (try_end),
    (try_end),
    #otherwise set other special scenes
    (party_set_slot,"p_village_189", slot_castle_exterior, "scn_village_germanic_1"),
    (party_set_slot,"p_village_79", slot_castle_exterior, "scn_village_germanic_1"),
    (party_set_slot,"p_village_16", slot_castle_exterior, "scn_village_germanic_1"),

    #alps
    (party_set_slot,"p_village_17", slot_castle_exterior, "scn_roman_village_mountain"),
    (party_set_slot,"p_village_195", slot_castle_exterior, "scn_roman_village_mountain"),
    (party_set_slot,"p_village_240", slot_castle_exterior, "scn_roman_village_mountain"),
    (party_set_slot,"p_village_241", slot_castle_exterior, "scn_roman_village_mountain"),
    (party_set_slot,"p_village_70", slot_castle_exterior, "scn_roman_village_mountain"),
    (party_set_slot,"p_village_78", slot_castle_exterior, "scn_roman_village_mountain"),

    #african coastal villages
    (party_set_slot,"p_village_106", slot_castle_exterior, "scn_village_africa_coastal"),
    (party_set_slot,"p_village_104", slot_castle_exterior, "scn_village_africa_coastal"),
    (party_set_slot,"p_village_103", slot_castle_exterior, "scn_village_africa_coastal"),
    (party_set_slot,"p_village_137", slot_castle_exterior, "scn_village_africa_coastal"),
    (party_set_slot,"p_village_108", slot_castle_exterior, "scn_village_africa_coastal"),
    (party_set_slot,"p_village_51", slot_castle_exterior,  "scn_village_africa_coastal"),

    (party_set_slot,"p_village_12", slot_castle_exterior, "scn_village_bosporan"),
    (party_set_slot,"p_village_28", slot_castle_exterior, "scn_village_bosporan"),
    (party_set_slot,"p_village_25", slot_castle_exterior, "scn_village_bosporan"),

    (party_set_slot,"p_village_48", slot_castle_exterior, "scn_roman_village_african"),
    (party_set_slot,"p_village_133", slot_castle_exterior, "scn_roman_village_african"),
    (party_set_slot,"p_village_131", slot_castle_exterior, "scn_roman_village_african"),
    (party_set_slot,"p_village_132", slot_castle_exterior, "scn_roman_village_african"),
    (party_set_slot,"p_village_91", slot_castle_exterior, "scn_roman_village_african"),

    (party_set_slot,"p_village_135", slot_castle_exterior, "scn_roman_village_african"),
    (party_set_slot,"p_village_102", slot_castle_exterior, "scn_roman_village_african"),

    (party_set_slot,"p_village_134", slot_castle_exterior, "scn_village_garamantian"),

    (party_set_slot,"p_village_129", slot_castle_exterior, "scn_village_babylon"),#special scene for babylon

    (party_set_slot,"p_village_229", slot_castle_exterior, "scn_village_palma"),

    (party_set_slot,"p_village_6", slot_castle_exterior, "scn_village_spain_1"),
    (party_set_slot,"p_village_145", slot_castle_exterior, "scn_village_spain_2"),
    (party_set_slot,"p_village_23", slot_castle_exterior, "scn_village_spain_3"),

    (party_set_slot,"p_village_146", slot_castle_exterior, "scn_village_spain_1"),
    (party_set_slot,"p_village_13", slot_castle_exterior, "scn_village_spain_2"),
    (party_set_slot,"p_village_139", slot_castle_exterior, "scn_village_spain_3"),

    (party_set_slot,"p_village_144", slot_castle_exterior, "scn_village_spain_4"),
    (party_set_slot,"p_village_141", slot_castle_exterior, "scn_village_spain"),
    (party_set_slot,"p_village_148", slot_castle_exterior, "scn_village_spain_4"),
    (party_set_slot,"p_village_138", slot_castle_exterior, "scn_village_spain_5"),

    (party_set_slot,"p_village_228", slot_castle_exterior, "scn_village_spain_5"),

    (party_set_slot,"p_village_152", slot_castle_exterior, "scn_village_152"),
    (party_set_slot,"p_village_153", slot_castle_exterior, "scn_village_153"),
    (party_set_slot,"p_village_154", slot_castle_exterior, "scn_village_154"),
    (party_set_slot,"p_village_58", slot_castle_exterior, "scn_village_58"),

    (party_set_slot,"p_village_93", slot_castle_exterior, "scn_village_persia_1"),
    (party_set_slot,"p_village_169", slot_castle_exterior, "scn_village_persia_2"),
    (party_set_slot,"p_village_216", slot_castle_exterior, "scn_village_persia_3"),

    (party_set_slot,"p_village_34", slot_castle_exterior, "scn_village_103"),
    (party_set_slot,"p_village_30", slot_castle_exterior, "scn_village_104"),
    (party_set_slot,"p_village_38", slot_castle_exterior, "scn_village_103"),
    (party_set_slot,"p_village_54", slot_castle_exterior, "scn_village_104"),
    (party_set_slot,"p_village_72", slot_castle_exterior, "scn_village_103"),
    (party_set_slot,"p_village_196", slot_castle_exterior, "scn_village_104"),
    (party_set_slot,"p_village_195", slot_castle_exterior, "scn_village_103"),
    (party_set_slot,"p_village_61", slot_castle_exterior, "scn_village_104"),

    (party_set_slot,"p_village_115", slot_castle_exterior, "scn_village_caledonian"),
    (party_set_slot,"p_village_117", slot_castle_exterior, "scn_village_caledonian"),
    (party_set_slot,"p_village_118", slot_castle_exterior, "scn_village_caledonian"),

    (party_set_slot,"p_village_40", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_89", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_178", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_177", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_179", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_92", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_176", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_19", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_21", slot_castle_exterior, "scn_village_dacian"),
    (party_set_slot,"p_village_67", slot_castle_exterior, "scn_village_dacian"),

    (party_set_slot,"p_village_112", slot_castle_exterior, "scn_village_east_germanic_coastal"),
    (party_set_slot,"p_village_113", slot_castle_exterior, "scn_village_east_germanic_coastal"),
    (party_set_slot,"p_village_26", slot_castle_exterior, "scn_village_east_germanic_coastal"),

    (party_set_slot,"p_village_224", slot_castle_exterior, "scn_village_east_germanic"),
    (party_set_slot,"p_village_223", slot_castle_exterior, "scn_village_east_germanic"),
    (party_set_slot,"p_village_111", slot_castle_exterior, "scn_village_east_germanic"),
    (party_set_slot,"p_village_114", slot_castle_exterior, "scn_village_east_germanic"),
    (party_set_slot,"p_village_222", slot_castle_exterior, "scn_village_east_germanic"),
    (party_set_slot,"p_village_101", slot_castle_exterior, "scn_village_east_germanic"),

    (party_set_slot,"p_village_227", slot_castle_exterior, "scn_village_island"),
    (party_set_slot,"p_village_73", slot_castle_exterior, "scn_village_island"),
    (party_set_slot,"p_village_53", slot_castle_exterior, "scn_village_island"),
    (party_set_slot,"p_village_226", slot_castle_exterior, "scn_village_island"),

    (party_set_slot,"p_village_162", slot_castle_exterior, "scn_village_patrae"),
    (party_set_slot,"p_village_166", slot_castle_exterior, "scn_village_ephesus"),

    (party_set_extra_icon, "p_village_166","icon_wonder_artemis",0,0,0,0),

    (try_for_range, ":village_no", villages_begin, villages_end),#finally set all unassigned scenes yet
        (party_get_slot, ":scene", ":village_no", slot_castle_exterior),
        (lt, ":scene", "scn_training_ground_ranged_melee_5"),#not assigned yet
        (try_begin),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_7"),
            (store_random_in_range, ":scene", "scn_village_41", "scn_village_42"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_1"),
            (store_random_in_range, ":scene", "scn_village_7", "scn_village_41"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (this_or_next|party_slot_eq, ":village_no", slot_center_culture, "fac_culture_9"),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_3"),
            (store_random_in_range, ":scene", "scn_village_42", "scn_village_44"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (this_or_next|party_slot_eq, ":village_no", slot_center_culture, "fac_culture_2"),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_2_1"),
            (store_random_in_range, ":scene", "scn_village_7", "scn_village_95"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_4"),
            (store_random_in_range, ":scene", "scn_village_98", "scn_village_94"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_6"),
            (store_random_in_range, ":scene", "scn_village_parthian_1", "scn_village_7"),
            (party_set_slot,":village_no", slot_castle_exterior, ":scene"),
        (else_try),
            (party_slot_eq, ":village_no", slot_center_culture, "fac_culture_5"),
            (party_set_slot,":village_no", slot_castle_exterior, "scn_village_44"),
        (try_end),
    (try_end),
]),

#script_game_set_multiplayer_mission_end
# This script is called from the game engine when a multiplayer map is ended in clients (not in server).
# INPUT:
# none
# OUTPUT:
# none
("game_set_multiplayer_mission_end",[]),

##to avoid warning
("game_character_screen_requested",[]),

("game_troop_upgrades_button_clicked",[
    (store_script_param, ":troop", 1),
    (call_script, "script_start_customizing", ":troop"),
    # (try_begin),
    # (store_party_size_wo_prisoners, ":size", "p_follower_party"),
    # (ge, ":size", 1),
    # (try_begin),
        # (is_between, ":troop", "trp_follower_woman", "trp_caravan_master"),
        # (party_remove_members, "p_main_party", ":troop", 1),
        # (party_add_members, "p_follower_party", ":troop", 1),
        # (jump_to_menu, "mnu_auto_return"),
    # (else_try),
        # (display_message, "@Can't add this troop to follower party"),
    # (try_end),
    # (else_try),
    # (display_message, "@You haven't created a follower party yet."),
    # (try_end),
]),

("game_missile_launch",[]),

#script_game_enable_cheat_menu
# This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
# INPUT:
# none
# OUTPUT:
# none
("game_enable_cheat_menu",[
      (store_script_param, ":input", 1),
      (try_begin),
        (eq, ":input", 0),
        (assign, "$cheat_mode", 0),
      (else_try),
        (eq, ":input", 1),
        (assign, "$cheat_mode", 1),
        #SB : flavour text
        (call_script, "script_objectionable_action", tmt_honest, "str_stop_cheating"),
      (try_end),
      (try_begin),
        (troop_slot_eq, "trp_global_variables", g_is_dev, 1),
        (neg|is_presentation_active, "prsnt_modify_slots"),
        # (assign, "$g_talk_troop", ":input"),
        (assign, "$g_presentation_state", 0),
        (assign, "$g_presentation_input", rename_companion),
        (start_presentation, "prsnt_modify_slots"),
      (else_try),
        (troop_get_slot, ":cheats", "trp_global_variables", g_used_cheats),
        (val_add, ":cheats", 1),
        (troop_set_slot, "trp_global_variables", g_used_cheats, ":cheats"),
        (display_message, "@GAME HAS NOTICED: You are using CHEATS!", color_terrible_news),
        (display_message, "@GAME HAS NOTICED: You are using CHEATS!", color_terrible_news),
        (display_message, "@GAME HAS NOTICED: You are using CHEATS!", color_terrible_news),
      (try_end),
      ]),

#script_game_get_console_command
# This script is called from the game engine when a console command is entered from the dedicated server.
# INPUT: anything
# OUTPUT: s0 = result text
("game_get_console_command",[]),

# script_game_event_party_encounter:
# This script is called from the game engine whenever player party encounters another party or a battle on the world map
# INPUT:
# param1: encountered_party
# param2: second encountered_party (if this was a battle
("game_event_party_encounter",[
    (store_script_param_1, "$g_encountered_party"),
    (store_script_param_2, "$g_encountered_party_2"),# encountered_party2 is set when we come across a battle or siege, otherwise it's a negative value
    #       (store_encountered_party, "$g_encountered_party"),
    #       (store_encountered_party2,"$g_encountered_party_2"), # encountered_party2 is set when we come across a battle or siege, otherwise it's a minus value
    (store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
    (store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
    (party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
    (party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
    #       (try_begin),
    #         (gt, "$g_encountered_party_2", 0),
    #         (store_faction_of_party, "$g_encountered_party_2_faction","$g_encountered_party_2"),
    #         (store_relation, "$g_encountered_party_2_relation", "$g_encountered_party_2_faction", "fac_player_faction"),
    #         (party_get_template_id,"$g_encountered_party_2_template","$g_encountered_party_2"),
    #       (else_try),
    #         (assign, "$g_encountered_party_2_faction",-1),
    #         (assign, "$g_encountered_party_2_relation", 0),
    #         (assign,"$g_encountered_party_2_template", -1),
    #       (try_end),
    #NPC companion changes begin
    (call_script, "script_party_count_fit_regulars", "p_main_party"),
    (assign, "$playerparty_prebattle_regulars", reg0),
    #        (try_begin),
    #            (assign, "$player_party__regulars", 0),
    #            (call_script, "script_party_count_fit_regulars", "p_main_party"),
    #            (gt, reg0, 0),
    #            (assign, "$player_party_contains_regulars", 1),
    #        (try_end),
    #NPC companion changes end
    (assign, "$g_last_rest_center", -1),
    (assign, "$talk_context", 0),
    (assign, "$g_player_surrenders",0),
    (assign, "$g_enemy_surrenders",0),
    (assign, "$g_leave_encounter",0),
    (assign, "$g_engaged_enemy", 0),
    #       (assign,"$waiting_for_arena_fight_result", 0),
    #       (assign,"$arena_bet_amount",0),
    #       (assign,"$g_player_raiding_village",0),
    (try_begin),
        (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
        (rest_for_hours, 0), #stop waiting
        (assign, "$g_infinite_camping", 0),
    (try_end),
        #       (assign, "$g_permitted_to_center",0),
        #SB : do cheat here before other menus are accessed
    (try_begin),
        (eq, "$new_encounter", 2),
        (jump_to_menu, "mnu_party_cheat"),
    (else_try),
        (assign, "$new_encounter", 1), #check this in the menu.
        (try_begin),
            (lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
            (try_begin),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                (jump_to_menu, "mnu_castle_outside"),
            (else_try),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                (jump_to_menu, "mnu_castle_outside"),
            (else_try),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                (jump_to_menu, "mnu_village"),
            (else_try),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
                (jump_to_menu, "mnu_cattle_herd"),
            (else_try),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_player_camp),
                (jump_to_menu, "mnu_player_camp"),
            (else_try),
                (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
                (jump_to_menu, "mnu_training_ground"),
            (else_try),
                (party_get_template_id, ":template", "$g_encountered_party"), #SB : is_between range
                (is_between, ":template", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"),
                (assign, "$loot_screen_shown", 0),
                (jump_to_menu, "mnu_bandit_lair"),
            (else_try),
                (party_get_icon, ":icon", "$g_encountered_party"),
                (eq, ":icon", "icon_castle_a"),
                (jump_to_menu, "mnu_horde"),
            (else_try),
                (eq, "$g_encountered_party", "p_pillars"),
                (jump_to_menu, "mnu_pillars"),
            (else_try),
                (eq, "$g_encountered_party", "p_grave_anatolia"),
                (jump_to_menu, "mnu_grave_anatolia"),
            (else_try),
                (eq, "$g_encountered_party", "p_tarquinii"),
                (jump_to_menu, "mnu_tarquinii"),
            (else_try),
                (eq, "$g_encountered_party", "p_underworld"),
                (jump_to_menu, "mnu_underworld"),
            #  (else_try),
            #    (is_between, "$g_encountered_party", "p_african_holy_side_1", "p_forest"),
            #    (jump_to_menu, "mnu_test_holyside"),
            (else_try),
                (eq, "$g_encountered_party", "p_forest"),
                (jump_to_menu, "mnu_forest"),
            (else_try),
                (check_quest_active, "qst_langobard_arrive"),
                (eq, "$g_encountered_party", "p_langobard_landing"),
                (jump_to_menu, "mnu_langobard_landing"),
            (else_try),
                (eq, "$g_encountered_party", "p_langobard_landing"),
                (jump_to_menu, "mnu_langobard_village"),
            (else_try),
                (eq, "$g_encountered_party", "p_caves_of_bacchus"),
                (jump_to_menu, "mnu_bacchus_entrance"),
            (else_try),
                (eq, "$g_encountered_party", "p_kurgan"),
                (jump_to_menu, "mnu_kurgan_enter"),
            (else_try),
                (eq, "$g_encountered_party", "p_royal_tombs"),
                (jump_to_menu, "mnu_royal_tombs"),
            (else_try),
                (eq, "$g_encountered_party", "p_old_mine"),
                (jump_to_menu, "mnu_old_mine"),
            (else_try),
                (eq, "$g_encountered_party", "p_sacred_grove"),
                (jump_to_menu, "mnu_sacred_grove"),
            (else_try),
                (eq, "$g_encountered_party", "p_sacred_grove_2"),
                (jump_to_menu, "mnu_grove_2"),
            (else_try),
                (eq, "$g_encountered_party_template", "pt_grove"),
                (jump_to_menu, "mnu_grove"),
            (else_try),
                (eq, "$g_encountered_party_template", "pt_latifundium"),
                (jump_to_menu, "mnu_latifundium"),
            (else_try),
                (is_between, "$g_encountered_party", minor_towns_begin, minor_towns_end),
                (jump_to_menu, "mnu_desert_town"),
            (else_try),
                (eq, "$g_encountered_party", "p_olympia"),
                (jump_to_menu, "mnu_olympia"),
            (else_try),
                (eq, "$g_encountered_party", "p_mount_olymp"),
                (jump_to_menu, "mnu_mount_olymp"),
            (else_try),
                (eq, "$g_encountered_party", "p_delphi"),
                (jump_to_menu, "mnu_delphi"),
            (else_try),
                (eq, "$g_encountered_party", "p_pyramids"),
                (jump_to_menu, "mnu_pyramids"),
            (else_try),
                (eq, "$g_encountered_party", "p_vally_of_kings"),
                (jump_to_menu, "mnu_vally_of_kings"),
            (else_try),
                (eq, "$g_encountered_party", "p_sartemis"),
                (jump_to_menu, "mnu_sartemis"),
            (else_try),
                (eq, "$g_encountered_party", "p_holy_lance_cave"),
                (jump_to_menu, "mnu_holy_lance_caves"),
            (else_try),
                (eq, "$g_encountered_party", "p_island"),
                (jump_to_menu, "mnu_cythnus"),
            (else_try),
                (is_between, "$g_encountered_party", "p_german_temple_1", "p_end_temple"),
                (jump_to_menu, "mnu_paganholysites_visit"),
            (else_try),
                (is_between, "$g_encountered_party", "p_ferry_1a", "p_transporter"),
                (jump_to_menu, "mnu_ferry_encounter"),
            (else_try),
                (is_between, "$g_encountered_party", "p_jetty_1a", "p_jetty_end"),
                (jump_to_menu, "mnu_jetty_encounter"),
            (else_try),
                (eq, "$g_encountered_party", "p_landing_point"),
                (jump_to_menu, "mnu_landing_point_encounter"),
            (else_try),
                (eq, "$g_encountered_party_template", "pt_landet_ships"),
                (jump_to_menu, "mnu_landet_ships_encounter"),
            (else_try),
                (eq, "$g_encountered_party_template", "pt_port"),
                (jump_to_menu, "mnu_port_encounter"),
            (else_try),
                (eq, "$g_encountered_party", "p_test_scene"),
                (jump_to_menu, "mnu_test_scene"),
            (else_try),
                (eq, "$g_encountered_party", "p_battlefields"),
                (jump_to_menu, "mnu_battlefields"),
            (else_try),
                (eq, "$g_encountered_party", "p_training_ground"),
                (jump_to_menu, "mnu_tutorial"),
            (else_try),
                (eq, "$g_encountered_party", "p_camp_bandits"),
                (jump_to_menu, "mnu_camp"),
            (else_try),
                (eq, "$g_encountered_party_template", "pt_slave_hideout"),
                (jump_to_menu, "mnu_slave_hideout"),
            (else_try),
                (jump_to_menu, "mnu_simple_encounter"),
            (try_end),
        (else_try), #Battle or siege
		    #  (neg|is_between, "$g_encountered_party", "p_german_temple_1", "p_end_temple"),
            (try_begin),
                (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                (try_begin),
                    (eq, "$auto_enter_town", "$g_encountered_party"),
                    (jump_to_menu, "mnu_town"),
                (else_try),
                    (eq, "$auto_besiege_town", "$g_encountered_party"),
                    (jump_to_menu, "mnu_besiegers_camp_with_allies"),
                (else_try),
                    (jump_to_menu, "mnu_join_siege_outside"),
                (try_end),
            (else_try),
                (jump_to_menu, "mnu_pre_join"),
            (try_end),
        (try_end),
    (try_end),
    (assign,"$auto_enter_town",0),
    (assign,"$auto_besiege_town",0),
]),

#script_game_event_simulate_battle:
# This script is called whenever the game simulates the battle between two parties on the map.
# INPUT:
# param1: Defender Party
# param2: Attacker Party
("game_event_simulate_battle",[
    (store_script_param_1, ":root_defender_party"),
    (store_script_param_2, ":root_attacker_party"),

    (assign, "$marshall_defeated_in_battle", -1),

    (store_current_hours, ":hours"),
    (try_for_parties, ":party"),
        (party_is_active, ":party"),
        (party_get_battle_opponent, ":opponent", ":party"),
        (party_is_active, ":opponent"),
        (party_set_slot, ":party", slot_party_last_in_combat, ":hours"),
        (try_begin),
            (eq, ":party", "$enlisted_party"),
            (neg|troop_is_wounded, "trp_player"),
            (store_faction_of_party, ":fac_1", ":party"),
            (store_faction_of_party, ":fac_2", ":opponent"),
            (store_relation, ":relation", ":fac_1", ":fac_2"),
            (lt, ":relation", 0),
            (start_encounter, "$enlisted_party"),
        (try_end),
    (try_end),

    (assign, ":trigger_result", 1),

    (try_begin),
        (ge, ":root_defender_party", 1),
        (party_is_active, ":root_defender_party"),
        (party_slot_eq, ":root_defender_party", slot_party_type, spt_player_camp),
        (ge, "$g_camp_mode", 1),
        (eq, "$auto_enter_town", ":root_defender_party"),

        (assign, ":trigger_result", 0),

        (assign, "$g_camp_mode", 0),
        (assign, "$g_player_icon_state", pis_normal),
        (rest_for_hours, 0, 0, 0), #stop camping
        (start_encounter, ":root_defender_party"),
    (else_try),
        (ge, ":root_defender_party", 0),
        (ge, ":root_attacker_party", 0),
        (party_is_active, ":root_defender_party"),
        (party_is_active, ":root_attacker_party"),
        (store_faction_of_party, ":defender_faction", ":root_defender_party"),
        (store_faction_of_party, ":attacker_faction", ":root_attacker_party"),
        #(neq, ":defender_faction", "fac_player_faction"),
        #(neq, ":attacker_faction", "fac_player_faction"),
        (store_relation, ":reln", ":defender_faction", ":attacker_faction"),
        (lt, ":reln", 0),
        (assign, ":trigger_result", 0),

        (try_begin),
            (this_or_next|eq, "$g_battle_simulation_cancel_for_party", ":root_defender_party"),
            (eq, "$g_battle_simulation_cancel_for_party", ":root_attacker_party"),
            (assign, "$g_battle_simulation_cancel_for_party", -1),
            (assign, "$auto_enter_town", "$g_battle_simulation_auto_enter_town_after_battle"),
            (assign, ":trigger_result", 1),
        (else_try),
        (try_begin),
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_retreat_flag, 1),
            (party_slot_eq, ":root_attacker_party", slot_party_retreat_flag, 1),
            (assign, ":trigger_result", 1), #End battle!
        (try_end),
        (party_set_slot, ":root_attacker_party", slot_party_retreat_flag, 0),

        (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
        (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),

        ##diplomacy start+
        (assign, ":terrain_code", dplmc_terrain_code_none),#defined in header_terrain.py
        (try_begin),
            (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
            (call_script, "script_dplmc_get_terrain_code_for_battle", ":root_attacker_party", ":root_defender_party"),
            (assign, ":terrain_code", reg0),
            #
            (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_ally", ":terrain_code", 0, 1),
            (assign, ":defender_strength", reg0),
            (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", ":terrain_code", 0, 1),
            (assign, ":attacker_strength", reg0),
        (else_try),
            (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
            (assign, ":defender_strength", reg0),
            #(call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
            (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
            (assign, ":attacker_strength", reg0),
        (try_end),
        ##diplomacy end+

        (store_div, ":defender_strength", ":defender_strength", 20),
        (val_min, ":defender_strength", 50),
        (val_max, ":defender_strength", 1),
        (store_div, ":attacker_strength", ":attacker_strength", 20),
        (val_min, ":attacker_strength", 50),
        (val_add, ":attacker_strength", 1),
        (try_begin),
            #For sieges increase attacker casualties and reduce defender casualties.
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle),
            (party_slot_eq, ":root_defender_party", slot_party_type, spt_town),
            (val_mul, ":defender_strength", 125), #it was 1.5 in old version, now it is only 1.25
            (val_div, ":defender_strength", 100),

            (val_mul, ":attacker_strength", 100), #it was 0.5 in old version, now it is only 1 / 1.25
            (val_div, ":attacker_strength", 125),
        (try_end),

        ##defender
        (assign, ":defender_percent", 100),
        (try_begin),##I make judeans more powerful to withstand Roman attacks better#
            (neg|is_between, ":root_defender_party", walled_centers_begin, walled_centers_end),
            (faction_slot_eq, ":defender_faction", slot_faction_culture, "fac_culture_8"),
            (val_add, ":defender_percent", 8),
        (try_end),
        # (try_begin),
        #     (faction_get_slot, ":serfdom", ":defender_faction", dplmc_slot_faction_serfdom),
        #     (neq, ":serfdom", 0),
        #     (val_mul, ":serfdom", -2),
        #     (val_add, ":defender_percent", ":serfdom"),
        # (try_end),
        (try_begin),
            (faction_get_slot, ":quality", ":defender_faction", dplmc_slot_faction_quality),
            (neq, ":quality", 0),
            (val_mul, ":quality", 4),
            (val_add, ":defender_percent", ":quality"),
        (try_end),
        (val_mul, ":defender_strength", ":defender_percent"),
        (val_div, ":defender_strength", 100),
        ##attacker
        (assign, ":attacker_percent", 100),
        (try_begin),##I make judeans more powerful to withstand Roman attacks better
            (neg|is_between, ":root_attacker_party", walled_centers_begin, walled_centers_end),
            (faction_slot_eq, ":attacker_faction", slot_faction_culture, "fac_culture_8"),
            (val_add, ":attacker_percent", 8),
        (try_end),
        # (try_begin),
        #     (faction_get_slot, ":serfdom", ":attacker_faction", dplmc_slot_faction_serfdom),
        #     (neq, ":serfdom", 0),
        #     (val_mul, ":serfdom", -2),
        #     (val_add, ":attacker_percent", ":serfdom"),
        # (try_end),
        (try_begin),
            (faction_get_slot, ":quality", ":attacker_faction", dplmc_slot_faction_quality),
            (neq, ":quality", 0),
            (val_mul, ":quality", 4),
            (val_add, ":attacker_percent", ":quality"),
        (try_end),
        (val_mul, ":attacker_strength", ":attacker_percent"),
        (val_div, ":attacker_strength", 100),

        (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
        (assign, ":old_defender_strength", reg0),

        (try_begin),
            # (neg|is_currently_night), #Don't fight at night
            (try_begin),
                (eq, ":root_attacker_party", "p_main_party"),
                (display_message, "@ERROR in script_game_event_simulate_battle: player party was damaged as attacker!", color_bad_news),
            (try_end),
            (inflict_casualties_to_party_group, ":root_attacker_party", ":defender_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),
        (try_end),
        (call_script, "script_party_count_fit_for_battle", "p_collective_enemy", 0),
        (assign, ":new_attacker_strength", reg0),

        (try_begin),
            (gt, ":new_attacker_strength", 0),
            # (neg|is_currently_night), #Don't fight at night
            (try_begin),
                (eq, ":root_defender_party", "p_main_party"),
                (display_message, "@ERROR in script_game_event_simulate_battle: player party was damaged as defender!", color_bad_news),
            (try_end),
            (inflict_casualties_to_party_group, ":root_defender_party", ":attacker_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
        (try_end),
        (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
        (assign, ":new_defender_strength", reg0),

        (try_begin),
            (this_or_next|eq, ":new_attacker_strength", 0),
            (eq, ":new_defender_strength", 0),
            # Battle concluded! determine winner

            (assign, ":do_not_end_battle", 0),
            (try_begin),
                (neg|troop_is_wounded, "trp_player"),
                (eq, ":new_defender_strength", 0),
                (eq, "$auto_enter_town", "$g_encountered_party"),
                (eq, ":old_defender_strength", ":new_defender_strength"),
                (assign, ":do_not_end_battle", 1),
            (try_end),
            (eq, ":do_not_end_battle", 0),

            (try_begin),
                (eq, ":new_attacker_strength", 0),
                (eq, ":new_defender_strength", 0),
                (assign, ":root_winner_party", -1),
                (assign, ":root_defeated_party", -1),
                (assign, ":collective_casualties", -1),
            (else_try),
                (eq, ":new_attacker_strength", 0),
                (assign, ":root_winner_party", ":root_defender_party"),
                (assign, ":root_defeated_party", ":root_attacker_party"),
                (assign, ":collective_casualties", "p_collective_enemy"),
            (else_try),
                (assign, ":root_winner_party", ":root_attacker_party"),
                (assign, ":root_defeated_party", ":root_defender_party"),
                (assign, ":collective_casualties", "p_collective_ally"),
            (try_end),

            (try_begin),
                (gt, ":root_defeated_party", -1),
                (assign, ":minimum_distance", 1000000),
                (try_for_range, ":center", centers_begin, centers_end),
                    (store_distance_to_party_from_party, ":dist", ":root_defeated_party", ":center"),
                    (try_begin),
                        (lt, ":dist", ":minimum_distance"),
                        (assign, ":minimum_distance", ":dist"),
                        (assign, ":nearest_center", ":center"),
                    (try_end),
                (try_end),

                (str_clear, s10),
                (try_begin),
                    (gt, ":nearest_center", 0),
                    (str_store_party_name, s10, ":nearest_center"),
                    (str_store_string, s10, "@ near {s10}"),
                (try_end),

                #SB : reformat loop
                (party_get_slot, ":type", ":root_defeated_party", slot_party_type),
                (try_begin),
                    # (eq, ":type", dplmc_spt_recruiter),
                    # (party_get_slot, reg10, ":root_defeated_party", dplmc_slot_party_recruiter_needed_recruits),
                    # (party_get_slot, ":party_origin", ":root_defeated_party", dplmc_slot_party_recruiter_origin),
                    # (str_store_party_name_link, s13, ":party_origin"),
                    # (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated{s10}!", message_defeated),
                # (else_try),
                    (eq,":type", dplmc_spt_gift_caravan),
                    (party_get_slot, ":target_troop", ":root_defeated_party", slot_party_orders_object),
                    (party_get_slot, ":target_party", ":root_defeated_party", slot_party_ai_object),
                    (try_begin),
                        (gt, ":target_troop", 0),
                        (str_store_troop_name, s13, ":target_troop"),
                    (else_try),
                        (str_store_party_name, s13, ":target_party"),
                    (try_end),
                    (party_get_slot, ":gift", ":root_defeated_party", dplmc_slot_party_mission_diplomacy),
                    (str_store_item_name, s12, ":gift"),
                    #SB : defeated -> looted
                    (display_log_message, "@Your caravan sending {s12} to {s13} has been looted{s10}!", message_defeated),
                (else_try),
                    (eq, ":type", spt_messenger),
                    (party_get_slot, ":target_party", ":root_defeated_party", slot_party_orders_object),
                    (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
                    (str_store_troop_name, s13, ":party_leader"),
                    #SB : defeated -> intercepted
                    (display_log_message, "@Your messenger on the way to {s13} has been ambushed{s10}!", message_defeated),
                (else_try),
                    (eq, ":type", spt_patrol),
                    (party_get_slot, ":home_town", ":root_defeated_party", slot_party_home_center),
                    (party_set_slot, ":home_town", slot_town_patrol_party, 0),#clear slot
                    (party_slot_eq, ":root_defeated_party", dplmc_slot_party_mission_diplomacy, "trp_player"),
                    (party_get_slot, ":target_party", ":root_defeated_party", slot_party_ai_object),
                    (str_store_party_name, s13, ":target_party"),
                    (display_log_message, "@Your soldiers patrolling {s13} have been defeated{s10}!", message_defeated),
                (else_try),
                    (eq, ":type", spt_scout),
                    (store_faction_of_party, ":party_faction", ":root_defeated_party"),
                    (eq, ":party_faction", "$players_kingdom"),
                    (party_get_slot, ":target_party", ":root_defeated_party", slot_party_orders_object),
                    (str_store_party_name, s13, ":target_party"),
                    (display_log_message, "@A scout trying to gather information about {s13} has been slain{s10}!", message_defeated),
                # (else_try), #SB : reinforcements
                    # (eq, ":type", spt_reinforcement),
                    # (store_faction_of_party, ":party_faction", ":root_defeated_party"),
                    # (eq, ":party_faction", "$players_kingdom"), #show only if relevant
                    # (party_get_slot, ":home_village", ":root_defeated_party", slot_party_home_center),
                    # (party_get_slot, ":target_party", ":home_village", slot_village_bound_center),
                    # (str_store_party_name_link, s12, ":home_village"),
                    # (str_store_party_name_link, s13, ":target_party"),
                    # (display_log_message, "@Reinforcements from {s12} intended for {s13} have been intercepted{s10}!", message_defeated),
                (else_try), #nero rebellion changes
                    (eq, ":type", spt_rebellion),
                    (str_store_party_name, s44, ":root_defeated_party"),
                    (display_log_message, "@The {s44} was defeated!", message_defeated),
                    (party_get_slot, ":target", ":root_defeated_party", slot_rebellion_target),
                    (party_set_slot, ":target", slot_center_ongoing_rebellion, 0),
                    (store_faction_of_party, ":party_faction", ":root_defeated_party"),
                    (faction_set_slot, ":party_faction", slot_faction_rebelling_against, 0), # rebellion has end
                (else_try), #nero companion parties changes
                    (eq, ":type", spt_companion_raider),
                    (party_get_slot, ":leader", ":root_defeated_party", slot_pcamp_camp_commander),
                    (troop_set_slot, ":leader", slot_troop_leaded_party, -1),
                    (troop_set_slot, ":leader", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                    (str_store_troop_name, s44, ":leader"),
                    (display_log_message, "@Your companion {s44} was defeated.", message_defeated),
                (else_try), #nero quest grain supply changes
                    (check_quest_active, "qst_grain_supply"),
                    (quest_slot_eq, "qst_grain_supply", slot_quest_target_party, ":root_defeated_party"),
                    (quest_set_slot, "qst_grain_supply", slot_quest_target_party, -1),
                    (quest_set_slot, "qst_grain_supply", slot_quest_current_state, 0),
                    (display_log_message, "@Your grain transport has been defeated! You must organize a new one.", message_defeated),
                (else_try), #nero rebellion changes
                    (party_get_template_id, ":template", ":root_defeated_party"),
                    (eq, ":template", "pt_rebels"),
                    (val_sub, "$g_unrest", 3),
                    (val_max, "$g_unrest", 0),
                    (display_message, "@Rebels were defeated. Stability of the Empire increases", color_good_news),
                (try_end),
            (try_end),

            (try_begin),
                (ge, ":root_winner_party", 0),
                (call_script, "script_get_nonempty_party_in_group", ":root_winner_party"),
                (assign, ":nonempty_winner_party", reg0),
                (store_faction_of_party, ":faction_receiving_prisoners", ":nonempty_winner_party"),
                (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),
            (else_try),
                (assign, ":nonempty_winner_party", -1),
            (try_end),

            (try_begin),
                (ge, ":collective_casualties", 0),
                (party_get_num_companion_stacks, ":num_stacks", ":collective_casualties"),
            (else_try),
                (assign, ":num_stacks", 0),
            (try_end),

            #depending on war status we can enforce either message_positive or message_negative
            (try_for_range, ":troop_iterator", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
                ##for freelancer to avoid player to be taken prisoner
                (gt, ":cur_troop_id", 0),##not the player
                (troop_is_hero, ":cur_troop_id"),

                #for freelancer, avoid companions taken prison
                (assign, ":c", 0),
                (try_begin),
                    (gt, "$enlisted_party", 0),#is freelancing
                    (main_party_has_troop, ":cur_troop_id"),#main party has troop
                    (str_store_troop_name, s1, ":cur_troop_id"),
                    (display_message, "@{s1} escapes together with you."),
                    (party_add_members,"p_underworld", ":cur_troop_id", 1),
                    (assign, ":c", 1),
                (try_end),
                (eq, ":c", 0),

                (try_begin),
                    #abort quest if troop loses a battle during rest time
                    (check_quest_active, "qst_lend_surgeon"),
                    (quest_slot_eq, "qst_lend_surgeon", slot_quest_giver_troop, ":cur_troop_id"),
                    (call_script, "script_abort_quest", "qst_lend_surgeon", 0),
                (try_end),

                (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
                (troop_set_slot, ":cur_troop_id", slot_troop_leaded_party, -1),

                (store_random_in_range, ":rand", 0, 100),
                (str_store_troop_name_link, s1, ":cur_troop_id"),
                (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
                (store_troop_faction, ":defeated_troop_faction", ":cur_troop_id"),
                (str_store_faction_name_link, s3, ":defeated_troop_faction"),
                #SB : colorize
                (faction_get_color, ":color", ":defeated_troop_faction"),
                (try_begin),
                    (neg|party_slot_eq, ":root_defeated_party", slot_party_type, spt_companion_raider),#not for companion parties
                    (neg|party_slot_eq, ":root_defeated_party", slot_party_type, spt_player_camp),
                    (ge, ":rand", hero_escape_after_defeat_chance),
                    #dckplmc
                    (party_get_template_id, ":party_template", ":root_defeated_party"),
                    (try_begin),
                        (eq, ":party_template", "pt_hero_party"),
                        (is_between, ":cur_troop_id", companions_begin, companions_end),
                        (troop_set_slot, ":cur_troop_id", slot_troop_playerparty_history, pp_history_scattered),
                        (troop_set_slot, ":cur_troop_id", slot_troop_turned_down_twice, 0),
                        (troop_set_slot, ":cur_troop_id", slot_troop_occupation, 0),
                        # (assign, ":continue", 1),
                        # (assign, ":minimum_distance", 99999),
                        # (assign, ":prison_center", -1),
                          # (try_for_range, ":center", walled_centers_begin, walled_centers_end),
                            # (store_distance_to_party_from_party, ":dist", ":center", ":root_defeated_party"),
                            # (lt, ":dist", ":minimum_distance"),
                            # (assign, ":minimum_distance", ":dist"),
                            # (assign, ":prison_center", ":center"),
                          # (try_end),
                          # (assign, reg1, ":prison_center"),
                          # #(display_message, "@{!}DEBUG : prison center is {reg1}"),
                          # (try_begin),
                            # (ge, ":prison_center", 0),
                            # (party_add_prisoners, ":prison_center", ":cur_troop_id", 1),
                            # (troop_set_slot, ":cur_troop_id", slot_troop_prisoner_of_party, ":prison_center"),
                          # (else_try),
                            # (store_random_in_range, ":town_no", towns_begin, towns_end),
                            # (troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":town_no"),
                          # (try_end),
                    (try_end),
                    #(neq, ":party_template", "pt_hero_party"), #end

                    (party_stack_get_troop_id, ":leader_troop_id", ":nonempty_winner_party", 0),
                    ##diplomacy start+ kingdom ladies might lead kingdom parties
                    (this_or_next|is_between,":leader_troop_id", kingdom_ladies_begin, kingdom_ladies_end),
                    (is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end),

                    (this_or_next|troop_slot_eq, ":leader_troop_id", slot_troop_occupation, slto_kingdom_hero),
                    ##diplomacy end+
                    (is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end), #disable non-kingdom parties capturing enemy lords

                    (party_add_prisoners, ":nonempty_winner_party", ":cur_troop_id", 1),
                    (gt, reg0, 0),
                    #(troop_set_slot, ":cur_troop_id", slot_troop_is_prisoner, 1),
                    (troop_set_slot, ":cur_troop_id", slot_troop_prisoner_of_party, ":nonempty_winner_party"),

                    (display_log_message, "str_hero_taken_prisoner", ":color"),

                    (try_begin),
                        (call_script, "script_cf_prisoner_offered_parole", ":cur_troop_id"),

                        (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "@{!}DEBUG : Prisoner granted parole"),
                        (try_end),

                        (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", 3),
                        (val_add, "$total_battle_enemy_changes", 3),
                    (else_try),
                        (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "@{!}DEBUG : Prisoner not offered parole"),
                        (try_end),

                        (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", -5),
                        (val_add, "$total_battle_enemy_changes", -5),
                    (try_end),
                    (store_faction_of_party, ":capturer_faction", ":nonempty_winner_party"),
                    (call_script, "script_update_troop_location_notes_prisoned", ":cur_troop_id", ":capturer_faction"),
                (else_try),
                    #dckplmc
                    (try_begin),
                        (party_get_template_id, ":party_template", ":root_defeated_party"),
                        (eq, ":party_template", "pt_hero_party"),
                        (is_between, ":cur_troop_id", companions_begin, companions_end),
                        (store_random_in_range, ":town_no", towns_begin, towns_end),
                        (troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":town_no"),
                        (troop_set_slot, ":cur_troop_id", slot_troop_playerparty_history, pp_history_scattered),
                        (troop_set_slot, ":cur_troop_id", slot_troop_turned_down_twice, 0),
                        (troop_set_slot, ":cur_troop_id", slot_troop_occupation, 0),
                    (try_end),
                    (display_message,"@{s1} of {s3} was defeated in battle but managed to escape.", ":color"),
                (try_end),

                (try_begin),
                    (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
                    (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                    (faction_slot_eq, ":cur_troop_faction", slot_faction_marshall, ":cur_troop_id"),
                    (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                    (assign, "$marshall_defeated_in_battle", ":cur_troop_id"),
                    #Marshall is defeated, refresh ai.
                    (assign, "$g_recalculate_ais", 1),
                (try_end),

                ##diplomacy begin
                (try_begin),
                    (call_script, "script_dplmc_is_affiliated_family_member", ":cur_troop_id"),
                    (eq, reg0, 1),
                    ##diplomacy start+ skip relationship decay for defeat when the player himself is imprisoned or wounded
                    (eq, "$g_player_is_captive", 0),
                    (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
                    (neg|troop_is_wounded, "trp_player"),
                    ##diplomacy end+
                    (assign, ":mitigating_factors", 0),
                    (try_begin),
                        #Being at war with the troop's faction is a mitigating factor, unless the player leads his faction.
                        (store_relation, reg0, "$players_kingdom", ":cur_troop_faction"),
                        (lt, reg0, 0),
                        (neq, "$players_kingdom", "fac_player_supporters_faction"),
                        (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                        (assign, ":mitigating_factors", 1),
                    (try_end),
                    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
                        ##diplomacy start+
                        #The dead, exiled, and retired don't participate in this
                        (neg|troop_slot_ge, ":family_member", slot_troop_occupation, slto_retirement),
                        #Members of factions at war with the defeated affiliate's faction don't have
                        #any relation loss either: it would be nonsensical for them to be willing to
                        #battle him themselves, but become enraged at his defeat.
                        (store_troop_faction, ":family_member_faction", ":family_member"),
                        (store_relation, reg0, ":family_member_faction", ":cur_troop_faction"),
                        (this_or_next|eq, ":family_member_faction", ":cur_troop_faction"),
                        (ge, reg0, 0),
                        ##(call_script, "script_troop_get_family_relation_to_troop", ":family_member", "$g_player_affiliated_troop"),
                        (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
                        (gt, reg0, 0),
                        (assign, ":relation_los", -2),
                        (options_get_campaign_ai, ":reduce_campaign_ai"),
                        (try_begin),
                            (eq, ":reduce_campaign_ai", 0),#hard: -1
                            (assign, ":relation_los", -1),
                        (else_try),
                            (eq, ":reduce_campaign_ai", 1),#medium: -1 or 0
                            (store_random_in_range, ":relation_los", -1, 1),
                        (else_try),
                            (eq, ":reduce_campaign_ai", 2),#easy: 0
                            (assign, ":relation_los", 0),
                        (try_end),
                        (val_add, ":relation_los", ":mitigating_factors"),
                        (lt, ":relation_los", 0),
                        (call_script, "script_change_player_relation_with_troop", ":family_member", ":relation_los"),
                        ##diplomacy end+
                    (try_end),
                (try_end),
                ##diplomacy end
            (try_end),

            (try_begin),
                (ge, ":collective_casualties", 0),
                (party_get_num_prisoner_stacks, ":num_stacks", ":collective_casualties"),
            (else_try),
                (assign, ":num_stacks", 0),
            (try_end),

            (try_for_range, ":troop_iterator", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
                (troop_is_hero, ":cur_troop_id"),
                (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
                (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
                (str_store_troop_name_link, s1, ":cur_troop_id"),
                (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
                (str_store_faction_name_link, s3, ":cur_troop_faction"),

                (faction_get_color, ":faction_color", ":faction_receiving_prisoners"),   ##color
                (display_log_message, "str_hero_freed", ":faction_color"),

                (try_begin), #dckplmc
                    (is_between, ":cur_troop_id", companions_begin, companions_end),
                    (neg|troop_slot_eq, ":cur_troop_id", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
                    (neg|troop_slot_eq, ":cur_troop_id", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
                    (neg|troop_slot_eq, ":cur_troop_id", slot_troop_occupation, slto_kingdom_hero),
                    (store_random_in_range, ":town_no", towns_begin, towns_end),
                    (troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":town_no"),
                    (troop_set_slot, ":cur_troop_id", slot_troop_playerparty_history, pp_history_scattered),
                    (troop_set_slot, ":cur_troop_id", slot_troop_turned_down_twice, 0),
                    (troop_set_slot, ":cur_troop_id", slot_troop_occupation, 0),
                (try_end),
            (try_end),

            (try_begin),
                (ge, ":collective_casualties", 0),
                (party_clear, "p_temp_party"),
                (assign, "$g_move_heroes", 0), #heroes are already processed above. Skip them here.
                (call_script, "script_party_prisoners_add_party_prisoners", "p_temp_party", ":collective_casualties"),
                (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", ":collective_casualties"),
                (distribute_party_among_party_group, "p_temp_party", ":root_winner_party"),

                (call_script, "script_battle_political_consequences", ":root_defeated_party", ":root_winner_party"),

                (call_script, "script_clear_party_group", ":root_defeated_party"),
            (try_end),
            (assign, ":trigger_result", 1), #End battle!

            ##prevent errors with texts were bandit parties are called "governor" or other shit
            #it seems that the error is caused when a party is spawned:
            #e.g. party number 500 was the emperors party, and had extra text
            ## then it is destroyed
            ## then a new party is spawned, which reuses the old party number 500
            ## and it still has an extra text
            # (try_begin),
            # (ge, ":root_winner_party", "p_vally_of_kings"),
            # (neg|party_slot_eq, ":root_winner_party", slot_party_type, spt_kingdom_hero_party),
            # (party_set_extra_text, ":root_winner_party", "str_empty_string"),
            # (try_end),
            ################
            ################
            ################
            #Center captured
            (try_begin),#check if the faction surrenders as puppet state
                (ge, ":collective_casualties", 0),
                (this_or_next|party_slot_eq,  ":root_defeated_party", slot_party_type, spt_town),
                (party_slot_eq,  ":root_defeated_party", slot_party_type, spt_castle),

                (store_faction_of_party, ":winner_faction", ":root_winner_party"),
                (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),

                (neq, ":defeated_faction", "fac_kingdom_19"),# not a rebel faction
                (neq, ":defeated_faction", "fac_kingdom_17"),# not a rebel faction

                (faction_get_slot, ":centers_defeated", ":defeated_faction", slot_faction_num_towns),
                (faction_get_slot, ":castles", ":defeated_faction", slot_faction_num_castles),
                (val_add, ":centers_defeated", ":castles"),
                (le, ":centers_defeated", 2),

                (store_add, ":slot_war_damage_inflicted_on_winner_faction", ":defeated_faction", slot_faction_war_damage_inflicted_on_factions_begin),
                (val_sub, ":slot_war_damage_inflicted_on_winner_faction", kingdoms_begin),
                (faction_get_slot, ":war_damage_inflicted_by_winner", ":winner_faction", ":slot_war_damage_inflicted_on_winner_faction"),
                (try_begin),
                    (is_between, ":root_defeated_party", towns_begin, towns_end),
                    (val_add, ":war_damage_inflicted_by_winner", 40),
                (else_try),
                    (val_add, ":war_damage_inflicted_by_winner", 20),
                (try_end),
                (ge, ":war_damage_inflicted_by_winner", 150),

                (store_add, ":slot_war_damage_inflicted_on_defeated_faction", ":winner_faction", slot_faction_war_damage_inflicted_on_factions_begin),
                (val_sub, ":slot_war_damage_inflicted_on_defeated_faction", kingdoms_begin),
                (faction_get_slot, ":war_damage_inflicted_by_defeated", ":defeated_faction", ":slot_war_damage_inflicted_on_defeated_faction"),

                (val_mul, ":war_damage_inflicted_by_defeated", 2),

                (gt, ":war_damage_inflicted_by_winner", ":war_damage_inflicted_by_defeated"),

                (faction_get_slot, ":centers_winner", ":winner_faction", slot_faction_num_towns),
                (faction_get_slot, ":castles", ":winner_faction", slot_faction_num_castles),
                (val_add, ":centers_winner", ":castles"),
                (ge, ":centers_winner", 2),
                (assign, ":c", 0),
                (try_begin),
                    (ge, ":centers_winner", 5),
                    (assign, ":c", 1),
                (else_try),
                    (gt, ":war_damage_inflicted_by_winner", 400),
                    (assign, ":c", 1),
                (else_try),
                    (ge, ":centers_winner", 5),
                    (eq, ":centers_defeated", 1),
                    (assign, ":c", 1),
                    (val_add, ":war_damage_inflicted_by_winner", 100),
                (try_end),
                (eq, ":c", 1),

                (val_div, ":war_damage_inflicted_by_winner", 20),
                (store_add, ":probability", ":war_damage_inflicted_by_winner", 1),
                # (try_begin),
                #     (this_or_next|faction_slot_eq, ":defeated_faction", slot_faction_culture, "fac_culture_1"),
                #     (this_or_next|faction_slot_eq, ":defeated_faction", slot_faction_culture, "fac_culture_2"),
                #     (this_or_next|faction_slot_eq, ":defeated_faction", slot_faction_culture, "fac_culture_3"),
                #     (faction_slot_eq, ":defeated_faction", slot_faction_culture, "fac_culture_4"),
                #     (val_add, ":probability", 20),
                # (try_end),
                (store_random_in_range, ":rand", 0, 40),
                (le, ":rand", ":probability"),

                (call_script, "script_dplmc_start_tributary_between_kingdoms", ":defeated_faction", ":winner_faction", 1),

                (try_for_range, ":party_template_slot", slot_cohort_town_begin, slot_cohort_town_3),
                    (party_get_slot, ":party_template", ":root_defeated_party", ":party_template_slot"),
                    (ge, ":party_template", 1),
                    (call_script, "script_cohort_refil_garrison", ":root_defeated_party", ":party_template", ":party_template_slot",0),
                (try_end),
            (else_try),#looting
                (ge, ":collective_casualties", 0),
                (party_get_slot, ":cur_party_type", ":root_defeated_party", slot_party_type),
                (this_or_next|eq, ":cur_party_type", spt_town),
                (eq, ":cur_party_type", spt_castle),

                (store_faction_of_party, ":winner_faction", ":root_winner_party"),
                (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),

                # (party_get_slot, ":original_faction", ":root_defeated_party", slot_center_original_faction),
                # this code checks if a party will be sacked or captured
                (try_begin),
                    (faction_get_slot, ":culture33", ":winner_faction", slot_faction_culture),
                    (party_get_slot, ":original_faction", ":root_defeated_party", slot_center_original_faction),
                    (is_between, ":culture33", "fac_culture_1", "fac_culture_5"),
                    (try_begin),
                        (is_between, ":original_faction", npc_kingdoms_begin, npc_kingdoms_end),
                        (faction_slot_eq, ":original_faction", slot_faction_culture, ":culture33"),
                        (neq, ":original_faction", ":winner_faction"),
                        (faction_slot_eq, ":original_faction", slot_faction_state, sfs_defeated),
                        (assign, ":erobern", 2),
                    (else_try),
                        (eq, ":original_faction", ":winner_faction"),
                        # (party_slot_eq, ":root_defeated_party", slot_center_culture, ":culture33"),
                        #(eq, ":winner_faction", ":original_faction"),
                        (assign, ":erobern", 1),
                    (else_try),
                        (assign, ":erobern", 0),
                    (try_end),
                (else_try),
                    (eq, ":winner_faction", "fac_kingdom_18"),
                    (try_begin),
                        (this_or_next|party_slot_eq, ":root_defeated_party", slot_center_original_faction, ":winner_faction"),
                        (party_slot_eq, ":root_defeated_party", slot_center_culture, ":culture33"),
                        #(eq, ":winner_faction", ":original_faction"),
                        (assign, ":erobern", 1),
                    (else_try),
                        (neg|faction_slot_ge, ":winner_faction", slot_faction_num_castles, 6),
                        (neg|faction_slot_ge, ":winner_faction", slot_faction_num_towns, 4),
                        (assign, ":erobern", 1),
                    (else_try),
                        (assign, ":erobern", 0),
                    (try_end),
                (else_try),
                    (party_slot_eq, ":root_defeated_party", slot_center_original_faction, ":winner_faction"),
                    (assign, ":erobern", 1),
                (else_try),
                    (store_random_in_range, ":r", 0, 11),
                    (le, ":r", 1),
                    (assign, ":erobern", 0),
                (else_try),
                    (assign, ":erobern", 1),
                (try_end),
                ###end check
                (ge, ":erobern", 1),
                # (str_store_party_name, s44, ":winner_party"),
                # (str_store_party_name, s45, ":defeated_party"),
                # (display_message, "@{s44} wants to conquere {s45}"),
                #free all captive ladies
                (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
                    (troop_get_slot, ":center", ":lady", slot_troop_prisoner_of_party),
                    (neg|troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_hero),
                    (eq, ":root_defeated_party", ":center"),
                    (call_script, "script_remove_troop_from_prison", ":lady"),
                    (store_faction_of_troop, ":lady_faction", ":lady"),
                    (store_faction_of_party, ":rescue_faction", ":root_winner_party"),
                    (faction_get_color, ":lady_faction_color", ":lady_faction"),
                    (str_store_troop_name_link, s1, ":lady"),
                    (str_store_faction_name_link, s2, ":rescue_faction"),
                    (str_store_faction_name_link, s3, ":lady_faction"),
                    (display_log_message, "str_hero_freed", ":lady_faction_color"),
                (try_end),
                (assign, "$g_recalculate_ais", 1),
                (str_store_party_name, s1, ":root_defeated_party"),
                (str_store_faction_name, s2, ":winner_faction"),
                (str_store_faction_name, s3, ":defeated_faction"),
                ## CC
                (faction_get_color, ":faction_color", ":winner_faction"),
                (display_log_message, "str_center_captured", ":faction_color"),
                ## CC

                (store_current_hours, ":hours"),
                (faction_set_slot, ":winner_faction", slot_faction_ai_last_decisive_event, ":hours"),

                (try_begin),
                    (eq, "$g_encountered_party", ":root_defeated_party"),
                    (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
                (try_end),

                (try_begin),
                    (party_get_num_companion_stacks, ":num_stacks", ":root_winner_party"),
                    (gt, ":num_stacks", 0),
                    (party_stack_get_troop_id, ":leader_troop_no", ":root_winner_party", 0),
                    ##diplomacy start+ support for promoted kingdom ladies
                    # (is_between, ":leader_troop_no", heroes_begin, heroes_end),#<- dplmc+ added
                    # (this_or_next|troop_slot_eq, ":leader_troop_no", slot_troop_occupation, slto_kingdom_hero),#<- dplmc+ addded
                    (is_between, ":leader_troop_no", active_npcs_begin, active_npcs_end),
                    ##diplomacy end+
                    (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, ":leader_troop_no"),
                (else_try),
                    (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, -1),
                (try_end),

                (call_script, "script_lift_siege", ":root_defeated_party", 0),
                (call_script, "script_spawn_looters", ":root_defeated_party", 5), #SB : spawn some looters
                (store_faction_of_party, ":fortress_faction", ":root_defeated_party"),

                (try_begin),
                    (is_between, ":root_defeated_party", towns_begin, towns_end),
                    (assign, ":damage", 40),
                (else_try),
                    (assign, ":damage", 20),
                (try_end),
                (call_script, "script_faction_inflict_war_damage_on_faction", ":winner_faction", ":fortress_faction", ":damage"),

                #we do this in a simple_trigger "PROVINCE SYSTEM"
                #if there is a governor of a province, check if he lost the last center of his province and remove him from office
                # (party_get_slot, ":center_lord", ":root_defeated_party", slot_town_lord),
                # (try_begin),
                    # (gt, ":center_lord", -1),
                    # (troop_slot_ge, ":center_lord", slot_troop_govern, 1),
                    # (assign, ":end", walled_centers_end),
                    # (party_get_slot, ":province", ":root_defeated_party", slot_center_province),
                    # (try_for_range, ":center", walled_centers_begin, ":end"),
                        # (neq, ":center", ":root_defeated_party"),
                        # (party_slot_eq, ":center", slot_center_province, ":province"),
                        # (party_slot_eq, ":center", slot_town_lord), ":center_lord"),
                        # (assign, ":end", -1),
                    # (try_end),
                    # (neq, ":end", -1),
                    # (str_store_string, s5, ":center_lord"),
                    # (store_add, s6, ":province", "str_province_begin"),
                    # (display_log_message, "@The province {s6} was lost. {s5} is no longer a governor."),
                    # (call_script, "script_troop_set_rank", ":center_lord", slot_troop_govern, -1),
                    # (try_begin),
                        # (gt, ":center_lord", 0),#not player
                        # (troop_get_slot, ":party", ":center_lord", slot_troop_leaded_party),
                        # (try_begin),
                            # (party_is_active, ":party"),
                            # (try_for_range, ":unused", 0, 9999),
                                # (store_party_size_wo_prisoners, ":size", ":party"),
                                # (gt, ":size", 1),
                                # (party_get_num_companion_stacks,":l", ":party"),
                                # (try_for_range, ":r", 0, ":l"),
                                    # (party_stack_get_troop_id, ":t", ":party", ":r"),
                                    # (neg|troop_is_hero, ":t"),
                                    # (party_stack_get_size, ":s", ":party", ":r"),
                                    # (party_remove_members, ":party", ":t", ":s"),
                                # (try_end),
                            # (try_end),
                            # (party_set_extra_text, ":party", "str_empty_string"),
                            # (call_script, "script_hire_men_to_kingdom_hero_party", ":center_lord"),
                        # (try_end),
                    # (try_end),
                # (try_end),
                #end province system
                (try_begin),
                    (eq, ":erobern", 2),
                    (is_between, ":original_faction", npc_kingdoms_begin, npc_kingdoms_end),
                    (call_script, "script_give_center_to_faction", ":root_defeated_party", ":original_faction"),
                    (call_script, "script_reactivate_kingdom", ":original_faction", ":winner_faction", ":root_defeated_party"),
                (else_try),
                    (call_script, "script_give_center_to_faction", ":root_defeated_party", ":winner_faction"),
                (try_end),

                (try_begin),#perform genocid on conquest
                    (is_between, ":original_faction", npc_kingdoms_begin, npc_kingdoms_end),
                    (is_between, ":culture33", "fac_culture_1", "fac_culture_5"),
                    (faction_get_slot, ":original_faction_culture", ":original_faction", slot_center_original_faction),
                    (is_between, ":original_faction_culture", "fac_culture_1", "fac_culture_5"),
                    (neg|party_slot_eq, ":root_defeated_party", slot_center_culture, ":original_faction_culture"),
                    (call_script, "script_change_culture_of_center", ":root_defeated_party", ":original_faction_culture"),
                    (call_script, "script_add_notification_menu", "mnu_notification_center_genocid", ":root_defeated_party", ":winner_faction"),
                (try_end),

                (try_begin),
                    ##diplomacy start+ Handle player is co-ruler of faction
                    (assign, ":is_defeated_faction_coruler", 0),
                    (try_begin),
                        ##zerilius changes begin
                        (eq, ":defeated_faction", "$players_kingdom"),
                        # (eq, ":is_defeated_faction_coruler", "$players_kingdom"),
                        ##zerilius changes end
                        (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                        (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
                        (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
                        (assign, ":is_defeated_faction_coruler", 1),
                    (try_end),
                    (this_or_next|eq, ":is_defeated_faction_coruler", 1),
                    ##diplomacy end+
                    (eq, ":defeated_faction", "fac_player_supporters_faction"),
                    (try_begin),
                        (eq, ":erobern", 2),
                        (is_between, ":original_faction", npc_kingdoms_begin, npc_kingdoms_end),
                        (call_script, "script_add_notification_menu", "mnu_notification_center_lost", ":root_defeated_party", ":original_faction"),
                    (else_try),
                        (call_script, "script_add_notification_menu", "mnu_notification_center_lost", ":root_defeated_party", ":winner_faction"),
                    (try_end),
                (try_end),

                (try_begin),
                    (neg|party_slot_eq, ":root_winner_party", slot_party_type, spt_rebellion),
                    #
                    (call_script, "script_calculate_loot_for_troop", ":root_winner_party", ":root_defeated_party", 0),

                    (party_get_num_attached_parties, ":num_attached_parties",  ":root_attacker_party"),
                    (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                        (party_get_attached_party_with_rank, ":attached_party", ":root_attacker_party", ":attached_party_rank"),
                        #add troops to garrison
                        (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
                        (assign, ":total_size", 0),
                        (try_for_range, ":i_stack", 0, ":num_stacks"),
                            (party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
                            (val_add, ":total_size", ":stack_size"),
                        (try_end),
                        (try_begin),
                            (ge, ":total_size", 50),
                            (assign, ":stacks_added", 0),
                            (assign, ":last_random_stack", -1),
                            (assign, ":end_condition", 10),
                            (try_for_range, ":unused", 0, ":end_condition"),
                                (store_random_in_range, ":random_stack", 1, ":num_stacks"),
                                (party_stack_get_troop_id, ":random_stack_troop", ":attached_party", ":random_stack"),
                                (party_stack_get_size, ":stack_size", ":attached_party", ":random_stack"),
                                (ge, ":stack_size", 4),
                                (neq, ":random_stack", ":last_random_stack"),

                                (store_mul, ":total_size_mul_2", ":total_size", 2),
                                (assign, ":percentage", ":total_size_mul_2"),
                                (val_min, ":percentage", 100),

                                (val_mul, ":stack_size", ":percentage"),
                                (val_div, ":stack_size", 100),

                                (party_stack_get_troop_id, ":party_leader", ":attached_party", 0),
                                (try_begin),
                                    ##diplomacy start+ add lady personality
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_conventional),
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_otherworldly),
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_adventurous),
                                    ##diplomacy end+
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_goodnatured),
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_upstanding),
                                    (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_martial),
                                    (assign, reg2, 0),
                                    (store_random_in_range, ":random_percentage", 40, 51), #average 45%
                                (else_try),
                                    ##diplomacy start+ add lady personality
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_ambitious),
                                    ##diplmoacy end+
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_quarrelsome),
                                    (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_cunning),
                                    (assign, reg2, 1),
                                    (store_random_in_range, ":random_percentage", 30, 41), #average 35%
                                (else_try),
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_selfrighteous),
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_roguish),
                                    (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_debauched),
                                    (assign, reg2, 2),
                                    (store_random_in_range, ":random_percentage", 20, 31), #average 25%
                                (else_try),
                                    ##diplomacy start+ add lady personality
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_moralist),
                                    ##diplomacy end+
                                    (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_benefactor),
                                    (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_custodian),
                                    (assign, reg2, 3),
                                    (store_random_in_range, ":random_percentage", 50, 61), #average 55%
                                (try_end),

                                (val_min, ":random_percentage", 100),
                                (val_mul, ":stack_size", ":random_percentage"),
                                (val_div, ":stack_size", 100),

                                (party_add_members, ":root_defender_party", ":random_stack_troop", ":stack_size"),
                                (party_remove_members, ":attached_party", ":random_stack_troop", ":stack_size"),

                                (val_add, ":stacks_added", 1),
                                (assign, ":last_random_stack", ":random_stack"),

                                (try_begin),
                                    #if troops from three different stack is already added then break
                                    (eq, ":stacks_added", 3),
                                    (assign, ":end_condition", 0),
                                (try_end),
                            (try_end),
                        (try_end),
                    (try_end),
                (try_end),

                #now done in script_calculate_loot_for_troop
                # #Reduce prosperity of the center by 5
                # (try_begin),
                    # #(neg|is_between, ":root_defeated_party", castles_begin, castles_end),
                    # (call_script, "script_change_center_prosperity", ":root_defeated_party", -5),
                    # (val_add, "$newglob_total_prosperity_from_townloot", -5),
                # (try_end),

                (call_script, "script_order_best_besieger_party_to_guard_center", ":root_defeated_party", ":winner_faction"),

                (try_for_range, ":party_template_slot", slot_cohort_town_begin, slot_cohort_town_3),
                    (party_get_slot, ":party_template", ":root_defeated_party", ":party_template_slot"),
                    (ge, ":party_template", 1),
                    (call_script, "script_cohort_refil_garrison", ":root_defeated_party", ":party_template", ":party_template_slot",0),
                (try_end),
                ##nero rebellion##hier her
                (try_begin),
                    (party_slot_eq, ":root_winner_party", slot_party_type, spt_rebellion),
                    (party_set_ai_behavior, ":root_winner_party", ai_bhvr_hold),
                    (call_script, "script_party_add_party", ":root_defeated_party", ":root_winner_party"),

                    (try_for_range, ":party_template_slot", slot_cohort_town_3, slot_cohort_town_5),
                        (party_get_slot, ":party_template", ":root_defeated_party", ":party_template_slot"),
                        (ge, ":party_template", 1),
                        (call_script, "script_cohort_refil_garrison", ":root_defeated_party", ":party_template", ":party_template_slot",0),
                    (try_end),

                    (str_store_party_name, s67, ":root_defeated_party"),
                    (party_set_slot, ":root_defeated_party", slot_center_ongoing_rebellion, 0),
                    #(party_set_slot, ":root_defeated_party", slot_center_has_recently_rebelled, 60),#move to simple trigger
                    (display_message, "@The rebellion in {s67}  was successful!", message_alert),

                    (store_faction_of_party, ":party_faction", ":root_winner_party"),
                    (faction_set_slot, ":party_faction", slot_faction_rebelling_against, 0), # rebellion has end
                (try_end),
                ##end
        ############
        (else_try), #stop barbarian empires
            (ge, ":collective_casualties", 0),
            (party_get_slot, ":cur_party_type", ":root_defeated_party", slot_party_type),
            (this_or_next|eq, ":cur_party_type", spt_town),
            (eq, ":cur_party_type", spt_castle),

            #free all captive ladies
            (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
                (troop_get_slot, ":center", ":lady", slot_troop_prisoner_of_party),
                (neg|troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_hero),
                (eq, ":root_defeated_party", ":center"),
                (call_script, "script_remove_troop_from_prison", ":lady"),
                (store_faction_of_troop, ":lady_faction", ":lady"),
                (store_faction_of_party, ":rescue_faction", ":root_winner_party"),
                (faction_get_color, ":lady_faction_color", ":lady_faction"),
                (str_store_troop_name_link, s1, ":lady"),
                (str_store_faction_name_link, s2, ":rescue_faction"),
                (str_store_faction_name_link, s3, ":lady_faction"),
                (display_log_message, "str_hero_freed", ":lady_faction_color"),
            (try_end),

            (assign, "$g_recalculate_ais", 1),

            (store_faction_of_party, ":winner_faction", ":root_winner_party"),
            (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),

            (str_store_party_name, s1, ":root_defeated_party"),
            (str_store_faction_name, s2, ":winner_faction"),
            (str_store_faction_name, s3, ":defeated_faction"),
            ## CC
            (faction_get_color, ":faction_color", ":winner_faction"),
            (display_log_message, "str_center_looted", ":faction_color"),
            ## CC

            (store_current_hours, ":hours"),
            (faction_set_slot, ":winner_faction", slot_faction_ai_last_decisive_event, ":hours"),

            (try_begin),
                (eq, "$g_encountered_party", ":root_defeated_party"),
                (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
            (try_end),

            # (try_begin),
            # (party_get_num_companion_stacks, ":num_stacks", ":root_winner_party"),
            # (gt, ":num_stacks", 0),
            # (party_stack_get_troop_id, ":leader_troop_no", ":root_winner_party", 0),
            # ##diplomacy start+ support for promoted kingdom ladies
            # (is_between, ":leader_troop_no", heroes_begin, heroes_end),#<- dplmc+ added
            # (this_or_next|troop_slot_eq, ":leader_troop_no", slot_troop_occupation, slto_kingdom_hero),#<- dplmc+ addded
                # (is_between, ":leader_troop_no", active_npcs_begin, active_npcs_end),
            # ##diplomacy end+
            # (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, ":leader_troop_no"),
            # (else_try),
            # (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, -1),
            # (try_end),

            (call_script, "script_lift_siege", ":root_defeated_party", 0),
            (call_script, "script_spawn_looters", ":root_defeated_party", 8), #SB : spawn some looters
            (store_faction_of_party, ":fortress_faction", ":root_defeated_party"),
            (try_begin),
                (is_between, ":root_defeated_party", towns_begin, towns_end),
                (assign, ":damage", 40),
            (else_try),
                (assign, ":damage", 20),
            (try_end),
            (call_script, "script_faction_inflict_war_damage_on_faction", ":winner_faction", ":fortress_faction", ":damage"),

            (call_script, "script_calculate_loot_for_troop", ":root_winner_party", ":root_defeated_party", 1),
            ###loot it !!! burn it !!! enslave them all!
            (call_script, "script_destroy_center", ":root_defeated_party"),
            (try_begin),
                ##diplomacy start+ Handle player is co-ruler of faction
                (assign, ":is_defeated_faction_coruler", 0),
                (try_begin),
                    ##zerilius changes begin
                    (eq, ":defeated_faction", "$players_kingdom"),
                    # (eq, ":is_defeated_faction_coruler", "$players_kingdom"),
                    ##zerilius changes end
                    (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                    (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
                    (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
                    (assign, ":is_defeated_faction_coruler", 1),
                (try_end),
                (this_or_next|eq, ":is_defeated_faction_coruler", 1),
                ##diplomacy end+
                (eq, ":defeated_faction", "fac_player_supporters_faction"),
                (call_script, "script_add_notification_menu", "mnu_notification_center_sacked", ":root_defeated_party", ":winner_faction"),
            (try_end),

            #lass es brennen
            (party_add_particle_system, ":root_defeated_party", "psys_map_village_fire"),
            (party_add_particle_system, ":root_defeated_party", "psys_map_village_fire_smoke"),
            #there is already prosperity change in #calculate loot for troop, this here
            #Reduce prosperity of the center by 15
            # (try_begin),
                # #(neg|is_between, ":root_defeated_party", castles_begin, castles_end),
                # (call_script, "script_change_center_prosperity", ":root_defeated_party", -15),
                # (val_add, "$newglob_total_prosperity_from_townloot", -15),
            # (try_end),
        (try_end),
    (try_end),

            #ADD XP
            (try_begin),
                (party_slot_eq, ":root_attacker_party", slot_party_type, spt_kingdom_hero_party),

                (assign, ":xp_gained_attacker", 200),
                (options_get_campaign_ai, ":reduce_campaign_ai"),
                (store_faction_of_party, ":root_attacker_party_faction", ":root_attacker_party"),
                (try_begin),
                    (this_or_next|eq, ":root_attacker_party", "p_main_party"),
                    (this_or_next|eq, ":root_attacker_party_faction", "fac_player_supporters_faction"),
                    (eq, ":root_attacker_party_faction", "$players_kingdom"),
                    #same
                (else_try),
                    (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
                    (val_mul, ":xp_gained_attacker", 3),
                    (val_div, ":xp_gained_attacker", 2),
                (else_try),
                    (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
                    #same
                (else_try),
                    (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
                    (val_div, ":xp_gained_attacker", 2),
                (try_end),

                (gt, ":new_attacker_strength", 0),
                (call_script, "script_upgrade_hero_party", ":root_attacker_party", ":xp_gained_attacker"),
            (try_end),
            (try_begin),
                (party_slot_eq, ":root_defender_party", slot_party_type, spt_kingdom_hero_party),

                (assign, ":xp_gained_defender", 200),
                (store_faction_of_party, ":root_defender_party_faction", ":root_defender_party"),
                (options_get_campaign_ai, ":reduce_campaign_ai"),
                (try_begin),
                    (this_or_next|eq, ":root_defender_party", "p_main_party"),
                    (this_or_next|eq, ":root_defender_party_faction", "fac_player_supporters_faction"),
                    (eq, ":root_defender_party_faction", "$players_kingdom"),
                  #same
                (else_try),
                    (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
                    (val_mul, ":xp_gained_defender", 3),
                    (val_div, ":xp_gained_defender", 2),
                (else_try),
                    (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
                    #same
                (else_try),
                    (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
                    (val_div, ":xp_gained_defender", 2),
                (try_end),

                (gt, ":new_defender_strength", 0),
                (call_script, "script_upgrade_hero_party", ":root_defender_party", ":xp_gained_defender"),
            (try_end),

            (try_begin),
                #ozan - do not randomly end battles aganist towns or castles.
                (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle), #added by ozan
                (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_town),   #added by ozan
                #end ozan

                (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
                (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
                (party_get_slot, ":strength_of_attacker_followers", ":root_attacker_party", slot_party_follower_strength),
                (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
                (val_add, ":total_attacker_strength", ":strength_of_attacker_followers"),

                (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
                (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
                (party_get_slot, ":strength_of_defender_followers", ":root_defender_party", slot_party_follower_strength),
                (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),
                (val_add, ":total_attacker_strength", ":strength_of_defender_followers"),

                #Players can make save loads and change history because these random values are not determined from random_slots of troops
                (store_random_in_range, ":random_num", 0, 100),

                (try_begin),
                    (lt, ":random_num", 10),
                    (assign, ":trigger_result", 1), #End battle!
                (try_end),
            (else_try),
                (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
                (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
                (party_get_slot, ":strength_of_followers", ":root_attacker_party", slot_party_follower_strength),
                (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
                (val_add, ":total_attacker_strength", ":strength_of_followers"),

                (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
                (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
                (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),

                (val_mul, ":total_defender_strength", 13), #multiply defender strength with 1.3
                (val_div, ":total_defender_strength", 10),

                (gt, ":total_defender_strength", ":total_attacker_strength"),
                (gt, ":total_defender_strength", 3),

                #Players can make save loads and change history because these random values are not determined from random_slots of troops
                (store_random_in_range, ":random_num", 0, 100),

                (try_begin),
                    (lt, ":random_num", 15), #15% is a bit higher than 10% (which is open area escape probability)
                    (assign, ":trigger_result", 1), #End battle!

                    (assign, "$g_recalculate_ais", 1), #added new

                    (try_begin),
                      (eq, "$cheat_mode", 1),
                      (display_message, "@{!}DEBUG : Siege attackers are running away"),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
    (try_end),
    (set_trigger_result, ":trigger_result"),
]),

#script_game_event_battle_end:
# This script is called whenever the game ends the battle between two parties on the map.
# INPUT:
# param1: Defender Party
# param2: Attacker Party
("game_event_battle_end",[
    # (store_script_param_1, ":root_defender_party"),
    #(store_script_param_2, ":root_attacker_party"),

      #Fixing deleted heroes
      ##diplomacy start+ kingdom ladies may also potentially lead parties
      (try_for_range, ":cur_troop", heroes_begin, heroes_end),#<- changed active_npcs to heroes
      #diplomacy end+
        (this_or_next|troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (is_between, ":cur_troop", companions_begin, companions_end),
        (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
        (troop_get_slot, ":cur_prisoner_of_party", ":cur_troop", slot_troop_prisoner_of_party),
        (try_begin),
          (ge, ":cur_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_companions_of_type, ":amount", ":cur_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} no longer leads a party."),
          (try_end),

          (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
          #(str_store_troop_name, s5, ":cur_troop"),
          #(display_message, "@{!}DEBUG : {s5}'s troop_leaded_party set to -1"),
        (try_end),
        (try_begin),
          (ge, ":cur_prisoner_of_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_prisoner_of_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} is no longer a prisoner."),
          (try_end),
          (call_script, "script_remove_troop_from_prison", ":cur_troop"),
          #searching player
          (try_begin),
            (party_count_prisoners_of_type, ":amount", "p_main_party", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, "p_main_party"),
            (assign, ":continue", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of player."),
            (try_end),
          (try_end),
          (eq, ":continue", 1),
		  ##diplomacy start+
		  #Add increased information for affiliates.
		  (call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":cur_troop"),
		  (assign, ":is_affiliated", reg0),
		  ##diplomacy end+
          #searching kingdom heroes
	  ##diplomacy start+ support for promoted kingdom ladies
          (try_for_range, ":cur_troop_2", heroes_begin, heroes_end),#<-- changed active_npcs to heroes
          ##diplomacy end+
			(this_or_next|troop_slot_eq, ":cur_troop_2", slot_troop_occupation, slto_kingdom_hero),
            (is_between, ":cur_troop_2", companions_begin, companions_end),
			(eq, ":continue", 1),
            (troop_get_slot, ":cur_prisoner_of_party_2", ":cur_troop_2", slot_troop_leaded_party),
            (party_is_active, ":cur_prisoner_of_party_2"),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
			##diplomacy start+ Show for affiliates
			  (ge, ":is_affiliated", 1),
			  (str_store_troop_name, s1, ":cur_troop"),
			  (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
			  (display_message, "@{s1} is now a prisoner of {s2}."),
			(else_try),
			##diplomacy end+
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
          #searching walled centers
          (try_for_range, ":cur_prisoner_of_party_2", walled_centers_begin, walled_centers_end),
            (eq, ":continue", 1),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
			##diplomacy start+ Show for affiliates
			  (ge, ":is_affiliated", 1),
			  (str_store_troop_name, s1, ":cur_troop"),
			  (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
			  (display_message, "@{s1} is now a prisoner of {s2}."),
			(else_try),
			##diplomacy end+
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
	(try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
		(troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
		(gt, ":party", 0),
		(neg|party_is_active, ":party"),

		(str_store_troop_name, s0, ":chest"),
		(display_message, "str_pcamp_s0_destroyed", 0xFFFF2222),

		(try_begin),
			(eq, "$auto_enter_town", ":party"),
			(assign, "$auto_enter_town", 0),
		(try_end),

		(troop_get_slot, ":commander", ":chest", slot_pcamp_chest_commander),
		(call_script, "script_cleanup_player_camp_slot", ":chest"),
		(call_script, "script_cleanup_player_camp_commander", ":party", ":commander"),
	(try_end),
	# #####new icon script
      # (store_script_param_1, ":root_defender_party"),
      # (try_begin),
        # (ge, ":root_defender_party", 0),
        # (party_is_active, ":root_defender_party"),
        # (call_script, "script_update_party_icon", ":root_defender_party"),
      # (try_end),
      # (store_script_param_2, ":root_attacker_party"),
      # (try_begin),
        # (ge, ":root_attacker_party", 0),
        # (party_is_active, ":root_attacker_party"),
        # (call_script, "script_update_party_icon", ":root_attacker_party"),
      # (try_end),
]),

#script_game_get_item_buy_price_factor:
# This script is called from the game engine for calculating the buying price of any item.
# INPUT:
# param1: item_kind_id
# OUTPUT:
# trigger_result and reg0 = price_factor
("game_get_item_buy_price_factor",[
    (store_script_param_1, ":item_kind_id"),
    (assign, ":price_factor", 100),

    (call_script, "script_get_trade_penalty", ":item_kind_id"),
    (assign, ":trade_penalty", reg0),

    (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),

        #new
        #(try_begin),
        #	(is_between, "$g_encountered_party", villages_begin, villages_end),
        #	(party_get_slot, ":market_town", "$g_encountered_party", slot_village_market_town),
        #	(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
        #	(val_max, ":price_factor", ":price_in_market_town"),
        #(try_end),

        #For villages, the good will be sold no cheaper than in the market town
        #This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers

        (val_mul, ":price_factor", 100), #normalize price factor to range 0..100
        (val_div, ":price_factor", average_price_factor),
    (try_end),

    (store_add, ":penalty_factor", 100, ":trade_penalty"),

    (val_mul, ":price_factor", ":penalty_factor"),
    (val_div, ":price_factor", 100),

    ##nero claudius chances begin
    (try_begin),
        (eq, "$edict7", 1),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (store_faction_of_party, ":fac", "$g_encountered_party"),
        (faction_slot_eq, ":fac", slot_faction_culture, "fac_culture_7"),
        (eq, ":item_kind_id", "itm_grain"),
        (val_clamp, ":price_factor", 50, 101),##grain price limits
    (try_end),
    ##nero claudius chances end

    (assign, reg0, ":price_factor"),
    (set_trigger_result, reg0),
]),

#script_game_get_item_sell_price_factor:
# This script is called from the game engine for calculating the selling price of any item.
# INPUT:
# param1: item_kind_id
# OUTPUT:
# trigger_result and reg0 = price_factor
("game_get_item_sell_price_factor",[
    (store_script_param_1, ":item_kind_id"),
    (assign, ":price_factor", 100),

    (call_script, "script_get_trade_penalty", ":item_kind_id"),
    (assign, ":trade_penalty", reg0),

    (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
        (val_mul, ":price_factor", 100),#normalize price factor to range 0..100
        (val_div, ":price_factor", average_price_factor),
    (else_try),
        #increase trade penalty while selling weapons, armor, and horses
        (val_mul, ":trade_penalty", 4),
    (try_end),

    # use a lesser trade penalty when selling to the correct merchant in town.
    (try_begin),
        (is_between, "$g_encountered_party", towns_begin, towns_end),
        (gt, "$g_talk_troop", "trp_player"),
        (try_begin), #Selling weapons to the weaponsmith
            (party_slot_eq, "$g_encountered_party", slot_town_weaponsmith, "$g_talk_troop"),
            (this_or_next|is_between, ":item_kind_id", weapons_begin, weapons_end),
            (this_or_next|is_between, ":item_kind_id", shields_begin, shields_end),
            (is_between, ":item_kind_id", ranged_weapons_begin, ranged_weapons_end),
            (val_mul, ":trade_penalty", 9),
            (val_div, ":trade_penalty", 10),
        (else_try), #Selling armor to the armorer
            (party_slot_eq, "$g_encountered_party", slot_town_armorer, "$g_talk_troop"),
            (is_between, ":item_kind_id", armors_begin, armors_end),
            (val_mul, ":trade_penalty", 9),
            (val_div, ":trade_penalty", 10),
        (else_try), #Selling horses to the horse merchant
            (party_slot_eq, "$g_encountered_party", slot_town_horse_merchant, "$g_talk_troop"),
            (is_between, ":item_kind_id", horses_begin, horses_end),
            (val_mul, ":trade_penalty", 9),
            (val_div, ":trade_penalty", 10),
        (try_end),
    (try_end),

    (try_begin), #If economic changes are enabled, increase food prices in a town under siege.
		(is_between, "$g_encountered_party", centers_begin, centers_end),
		#Check selling food
		(is_between, ":item_kind_id", food_begin, food_end),
		#Check at a town or castle under siege for at least 48 hours
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
		(party_slot_eq, "$g_encountered_party", slot_village_state, svs_under_siege),

		(party_slot_ge, "$g_encountered_party", slot_center_is_besieged_by, 1),
		(party_get_slot, ":siege_start", "$g_encountered_party", slot_center_siege_begin_hours),
		(store_current_hours, ":cur_hours"),
		(store_sub, reg0, ":cur_hours", ":siege_start"),
		(ge, reg0, 48),
		#Check last caravan or village trading party arrival (default to eight weeks ago)
		# (store_sub, ":last_arrival", ":cur_hours", 8 * 7 * 24),
		# (val_min, ":last_arrival", ":siege_start"),
		# (try_for_range, ":village_no", villages_begin, villages_end),
			# (party_slot_eq, ":village_no", slot_village_market_town, "$g_encountered_party"),
			# (party_get_slot, reg0, ":village_no", dplmc_slot_village_trade_last_arrived_to_market),
			# (val_min, reg0, ":cur_hours"),
			# (val_max, ":last_arrival", reg0),
		# (try_end),
		# (try_for_range, ":slot_no", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
			# #Not all of these slots correspond to towns, but that doesn't
			# #matter since their arrival times won't update after the start
			# #of the game.
			# (party_get_slot, reg0, "$g_encountered_party", ":slot_no"),
			# (val_min, reg0, ":cur_hours"),
			# (val_max, ":last_arrival", reg0),
		# (try_end),
		##Increase food prices by 10% for every 3 days the siege has been going on,
		#or a minimum of 5%.
		#TODO: Make use of the last caravan arrival time.
		(store_sub, ":hours_since", ":cur_hours", ":siege_start"),
		(store_mul, ":siege_percent", ":hours_since", 10),
		(val_add, ":siege_percent", (3 * 24) // 2),
		(val_div, ":siege_percent", 3 * 24),
		(val_max, ":siege_percent", 5),
		(val_add, ":siege_percent", 100),
		(val_mul, ":price_factor", ":siege_percent"),
		(val_add, ":price_factor", 50),
		(val_div, ":price_factor", 100),
    (try_end),
    ##diplomacy end+

    (store_add, ":penalty_divisor", 100, ":trade_penalty"),

    (val_mul, ":price_factor", 100),

    (try_begin),
        (gt, ":penalty_divisor", 0),
        (store_div, reg0, ":penalty_divisor", 2),
        (val_add, ":price_factor", reg0),#round correctly
    (try_end),

    (val_div, ":price_factor", ":penalty_divisor"),

    ##nero claudius chances begin
    (try_begin),
        (eq, "$edict7", 1),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (store_faction_of_party, ":fac", "$g_encountered_party"),
        (faction_slot_eq, ":fac", slot_faction_culture, "fac_culture_7"),
        (eq, ":item_kind_id", "itm_grain"),
        (val_clamp, ":price_factor", 50, 101),##grain price limits
    (try_end),
    ##nero claudius chances end

    (assign, reg0, ":price_factor"),
    (set_trigger_result, reg0),
]),
#script_game_event_buy_item:
# This script is called from the game engine when player buys an item.
# INPUT:
# param1: item_kind_id
("game_event_buy_item",[
    (store_script_param_1, ":item_kind_id"),
    (store_script_param_2, ":reclaim_mode"),
    (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
            (eq, ":reclaim_mode", 0),
            (val_add, ":multiplier", 20),
        (else_try),
            (val_add, ":multiplier", 30),
        (try_end),
        (store_item_value, ":item_value", ":item_kind_id"),
        (try_begin),
            (ge, ":item_value", 100),
            (store_sub, ":item_value_sub_100", ":item_value", 100),
            (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
            (val_add, ":multiplier", ":item_value_sub_100_div_8"),
        (try_end),
        (val_min, ":multiplier", maximum_price_factor),
        (party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
    (try_end),
]),

  #script_game_event_sell_item:
  # This script is called from the game engine when player sells an item.
  # INPUT:
  # param1: item_kind_id
  ("game_event_sell_item",
    [
      (store_script_param_1, ":item_kind_id"),
      (store_script_param_2, ":return_mode"),
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
          (eq, ":return_mode", 0),
          (val_sub, ":multiplier", 30),
        (else_try),
          (val_sub, ":multiplier", 20),
        (try_end),

        (store_item_value, ":item_value", ":item_kind_id"),
        (try_begin),
          (ge, ":item_value", 100),
          (store_sub, ":item_value_sub_100", ":item_value", 100),
          (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
          (val_sub, ":multiplier", ":item_value_sub_100_div_8"),
        (try_end),
        (val_max, ":multiplier", minimum_price_factor),

        (party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
      (try_end),
  ]),
# script_game_get_troop_wage
# This script is called from the game engine for calculating troop wages.
# Input:
# param1: troop_id, param2: party-id
# Output: reg0: weekly wage
("game_get_troop_wage",[
    (store_script_param_1, ":troop_id"),
    (store_script_param_2, ":party_no"), #party id
    (assign,":wage", 0),

    (try_begin),
        (party_stack_get_troop_id, ":leader", ":party_no", 0),
        (this_or_next|is_between, ":leader", active_npcs_begin,active_npcs_end),
        (eq, ":leader", "trp_player"),
        (store_skill_level, ":leadership_level", "skl_leadership", ":leader"), #good leadership mean pay a lot less
        (store_skill_level, ":persuasion", "skl_persuasion", ":leader"),
        (val_sub, ":persuasion", 6),
        (troop_get_slot, ":culture", ":leader", slot_troop_culture),
    (else_try),
        (assign, ":leadership_level", 5),
        (assign, ":persuasion", 1),
        (store_faction_of_party, ":leader_faction", ":party_no"),
        (faction_get_slot, ":culture", ":leader_faction", slot_faction_culture),
    (try_end),

    (try_begin),
        (this_or_next|eq, ":troop_id", "trp_player"),
        (this_or_next|is_between, ":troop_id", kings_begin, kingdom_ladies_end),
        (this_or_next|troop_slot_eq, ":troop_id", slot_troop_playerparty_history,dplmc_pp_history_lord_rejoined),
        (this_or_next|troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
        (this_or_next|troop_slot_eq, ":troop_id",slot_troop_occupation, slto_kingdom_lady),
        (eq, ":troop_id", "trp_kidnapped_girl"),
    (else_try),
        ##OLD:
        # (store_character_level, ":troop_level", ":troop_id"),
        # (assign, ":wage", ":troop_level"),
        # (val_add, ":wage", 3),
        # (val_mul, ":wage", ":wage"),
        # (val_div, ":wage", 25),
        #NEW:
        (store_character_level, ":troop_level", ":troop_id"), #produces wage chief =  (troop_level * 20)  + (troop_level * 20) / 25
        (assign, ":wage", ":troop_level"),
        (try_begin),
            (le, ":troop_level", 23), #26 are good troops and cheap -- too cheap
            (val_add, ":wage", 6), #chief cambia
            (val_sub, ":wage", ":leadership_level"), #chief cambia
        (else_try),
            (le, ":troop_level", 26),
            (val_add, ":wage", 12), #chief cambia
            (val_sub, ":wage", ":leadership_level"), #chief cambia
            (val_sub, ":wage", ":persuasion"),
            (val_mul, ":wage", 6),
            (val_div, ":wage", 5),
        (else_try),
            #       (gt, ":troop_level", 23), #27 or higher level expensive
            (val_add, ":wage", 22), #chief cambia
            (val_sub, ":wage", ":leadership_level"), #chief cambia
            (val_sub, ":wage", ":persuasion"),
            (val_mul, ":wage", 4), #chief cambia
            (val_div, ":wage", 3),
        (try_end),
        (val_max, ":wage", 1),
    (try_end),

    (try_begin),
        (ge, ":party_no", -1),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (try_begin),
            (eq, ":party_no", "p_main_party"),
            (assign, ":party_faction", "$players_kingdom"),
        (else_try),
            (store_faction_of_party, ":party_faction", ":party_no"),
        (try_end),
        (try_begin),
            (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
            (faction_get_slot, ":quality_muliplier", ":party_faction", dplmc_slot_faction_quality),
            (val_add, ":quality_muliplier", 100),
            (val_mul, ":wage", ":quality_muliplier"),
            (val_div, ":wage", 100),
        (try_end),
    (try_end),

    (try_begin), #mounted troops cost more than the normal cost
        (neg|is_between, ":troop_id", companions_begin, companions_end),
        (troop_is_mounted, ":troop_id"),
        (try_begin),#parthia
            (store_faction_of_troop, ":troop_culture", ":troop_id"),
            (eq, ":troop_culture", "fac_culture_6"),
            (eq, ":culture", "fac_culture_6"),
            (val_mul, ":wage", 2),
        (else_try),#nomads do not pay additional wages
            (eq, ":troop_culture", "fac_culture_3"),
            (eq, ":culture", "fac_culture_3"),
            (val_mul, ":wage", 3),
            (val_div, ":wage", 2),
        (else_try),#armenians
            (eq, ":culture", "fac_culture_5"),
            (eq, ":troop_culture", "fac_culture_5"),
            (val_mul, ":wage", 3),
        (else_try),
            (val_mul, ":wage", 5),
        (try_end),
    (try_end),

    (try_begin), #mercenaries cost more than the normal cost
        (is_between, ":troop_id", mercenary_troops_begin, mercenary_troops_end),
        (val_mul, ":wage", 6),
        (val_div, ":wage", 5),
    (try_end),

    (try_begin),
        (is_between, ":troop_id", companions_begin, companions_end),
        (val_mul, ":wage", 5),
        (eq, "$disable_companions_leaving", 1),
        (val_mul, ":wage", 5),
    (try_end),

    (try_begin),#-25% wage for judeans
        (eq, ":culture", "fac_culture_8"),#judeans
        (val_mul, ":wage", 3),
        (val_div, ":wage", 4),
    (try_end),
    # (store_skill_level, ":leadership_level", "skl_leadership", "trp_player"),
    # (store_mul, ":leadership_bonus", 4, ":leadership_level"),
    # (store_sub, ":leadership_factor", 100, ":leadership_bonus"),
    # (val_mul, ":wage", ":leadership_factor"),  #wage = wage * (100 - 4*leadership)/100
    # (val_div, ":wage", 100),

    (try_begin),
        (neq, ":troop_id", "trp_player"),
        (neq, ":troop_id", "trp_kidnapped_girl"),
        #(neg|is_between, ":troop_id", pretenders_begin, pretenders_end),
        ##diplomacy start+ For temporarily rejoined lords, and temporarily joined ladies
        (neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history,dplmc_pp_history_lord_rejoined),
        (neg|troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
        (neg|is_between, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        ##diplomacy end+
        (val_max, ":wage", 1),
    (try_end),
    (assign, reg0, ":wage"),

    # (str_store_party_name, s1, ":party_no"),
    # (str_store_troop_name, s2, ":troop_id"),
    # (display_message, "@party: {s1}, troop {s2}, wage: {reg0}"),
    (set_trigger_result, reg0),
]),

# script_game_get_total_wage
# This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
# Input: none
# Output: reg0: weekly wage
("game_get_total_wage",[
    (assign, ":total_wage", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
        (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
        (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
        (val_mul, reg0, ":stack_size"),
        (val_add, ":total_wage", reg0),
    (try_end),
    ##diplomacy start+
    #If the player leads a kingdom, take into account centralization.
    (faction_get_slot, ":centralization", "$players_kingdom", dplmc_slot_faction_centralization),
    (try_begin),
        (neq, ":centralization", 0),

        (assign, reg0, 0),
        (try_begin),
            (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
            (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
            (ge, ":faction_leader", 0),
            (this_or_next|eq, ":faction_leader", "trp_player"),
            (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
            (troop_slot_eq, "trp_player", slot_troop_spouse, reg0),
            (assign, reg0, 1),
        (try_end),

        (this_or_next|eq, reg0, 1),
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),

		  #Apply centralization, but limit it for nascent kingdoms
        (val_clamp, ":centralization", -3, 4),
        (faction_get_slot, ":policy_limit", "$players_kingdom", slot_faction_num_towns),
        (faction_get_slot, reg0, "$players_kingdom", slot_faction_num_castles),
        (val_add, ":policy_limit", reg0),

        (val_max, ":policy_limit", 0),
        (val_min, ":centralization", ":policy_limit"),
        (val_mul, ":policy_limit", -1),
        (val_max, ":centralization", ":policy_limit"),

        #Now reg0 is going to be the result again
        (store_mul, reg0, ":centralization", -5),
        (val_add, reg0, 100),
        (val_mul, reg0, ":total_wage"),
        (val_add, reg0, 50),#rounding
        (val_div, reg0, 100),
    (try_end),
    ##diplomacy end+
    (assign, reg0, ":total_wage"),
    (set_trigger_result, reg0),
]),
# script_game_get_join_cost
# This script is called from the game engine for calculating troop join cost.
# Input:
# param1: troop_id,
# Output: reg0: weekly wage
("game_get_join_cost",[
    (store_script_param_1, ":troop_id"),
    (assign,":join_cost", 0),
    (try_begin),
        (troop_is_hero, ":troop_id"),
    (else_try),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":join_cost", ":troop_level"),
        (val_add, ":join_cost", 8),
        (val_mul, ":join_cost", ":join_cost"),
        (val_add, ":join_cost", 250), #was 40
        (val_div, ":join_cost", 5),
        # (try_begin),##renown influence
        # (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
        # (ge, ":player_renown", 400),
        # (val_min, ":player_renown" ,1000),
        # (val_sub, ":player_renown", 100),
        # (val_div, ":player_renown", 10),
        # (val_sub, ":join_cost", ":player_renown"),
        # (try_end),
        (try_begin), #mounted troops cost %100 more than the normal cost chief cambia
            (troop_is_mounted, ":troop_id"),
            (val_mul, ":join_cost", 2),
        (try_end),
    (try_end),
    (assign, reg0, ":join_cost"),
    (set_trigger_result, reg0),
]),
# script_game_get_upgrade_xp
# This script is called from game engine for calculating needed troop upgrade exp
# Input:
# param1: troop_id,
# Output: reg0 = needed exp for upgrade
("game_get_upgrade_xp",[
    (store_script_param_1, ":troop_id"),
    (assign, ":x", 0),
    #formula : int needed_upgrade_xp = 2 * (30 + 0.006f * level_boundaries[troops[troop_id].level + 3]);
    (store_character_level, ":troop_level", ":troop_id"),
    (try_begin),
        (le, ":troop_level", 10),
        (store_mul, ":x", ":troop_level", 20),
        (val_add, ":x", 100),
    (else_try),
        (le, ":troop_level", 20),
        (store_mul, ":x", ":troop_level", 15),
        (val_add, ":x", 200),
    (else_try),
        (le, ":troop_level", 30),
        (store_mul, ":x", ":troop_level", 10),
        (val_add, ":x", 300),
    (else_try),
        (le, ":troop_level", 40),
        (store_mul, ":x", ":troop_level", 5),
        (val_add, ":x", 400),
    (else_try),
        (store_mul, ":x", ":troop_level", 2),
        (val_add, ":x", 520),
    (try_end),
    (try_begin),
        # (gt, ":troop_level", 23),
        # (val_mul, ":x", 4),
        # (val_div, ":x", 3),
        # (else_try),
        (val_mul, ":x", 4),
        (val_div, ":x", 3),
    (try_end),
    (assign, reg0, ":x"),
    (set_trigger_result, reg0),
]),
# script_game_get_upgrade_cost
# This script is called from game engine for calculating needed troop upgrade exp
# Input:
# param1: troop_id,
# Output: reg0 = needed cost for upgrade
("game_get_upgrade_cost",[
    (store_script_param_1, ":troop_id"),
    (store_character_level, ":troop_level", ":troop_id"),
    (try_begin),
        (le, ":troop_level", 23),
        (assign, ":cost", ":troop_level"),
        (val_mul, ":cost", 12),# was 4 - simplified calculations + expensive. Upgrading is expensive.
    (else_try),
        (assign, ":cost", ":troop_level"),
        (val_mul, ":cost", 36),
    (try_end),
    (try_begin), #mounted troops cost 33% more than the normal cost
        (troop_is_mounted, ":troop_id"),
        (val_mul, ":cost", 4),
        (val_div, ":cost", 3),
    (try_end),
    (assign, reg0, ":cost"),
    (set_trigger_result, reg0),
]),

# script_game_get_prisoner_price
# This script is called from the game engine for calculating prisoner price
# Input:
# param1: troop_id,
# Output: reg0
("game_get_prisoner_price",[
    (store_script_param_1, ":troop_id"),

    (try_begin), #SB : regular prices for constable selling
        (this_or_next|eq, "$g_talk_troop", "$g_player_constable"),
        (is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
        (store_character_level, ":troop_level", ":troop_id"),
        (store_add, ":ransom_amount", ":troop_level", 10),##e.g. level is 40 => 50
        # (val_add, ":ransom_amount", 10),
        (val_mul, ":ransom_amount", ":ransom_amount"),##e.g. 50^2 = 2500
        (val_div, ":ransom_amount", 5), ##e.g. 2500/5 = 500
    (else_try),
        (eq, "$g_talk_troop", "trp_slave_trader"),
        (assign, ":ransom_amount", 300),
    (else_try),
        (this_or_next|eq, "$g_talk_troop", "trp_ramun_the_slave_trader"),
        (eq, "$g_talk_troop", "trp_galeas"),
        (assign, ":ransom_amount", 301),
    (else_try),
        (assign, ":ransom_amount", 150),
    (try_end),
    (assign, reg0, ":ransom_amount"),
    (set_trigger_result, reg0),
]),

# script_game_check_prisoner_can_be_sold
# This script is called from the game engine for checking if a given troop can be sold.
# Input:
# param1: troop_id,
# Output: reg0: 1= can be sold; 0= cannot be sold.
("game_check_prisoner_can_be_sold",[
    (store_script_param_1, ":troop_id"),
    (assign, reg0, 0),
    (try_begin),
        (neg|troop_is_hero, ":troop_id"),
        (try_begin),
            (check_quest_active, "qst_hunt_down_fugitive"),
            (eq, ":troop_id", "trp_fugitive"), #SB : can't sell quest troops
            (assign, reg0, 0),
        (else_try),
            (check_quest_active, "qst_hunt_down_fugitive"),
            (this_or_next|eq, ":troop_id", "trp_spy"),
            (eq, ":troop_id", "trp_spy_partner"),
            (assign, reg0, 0),
        (else_try),
            (assign, reg0, 1),
        (try_end),
    (try_end),
    (set_trigger_result, reg0),
]),

# script_game_get_morale_of_troops_from_faction
# This script is called from the game engine
# Input:
# param1: faction_no,
# Output: reg0: extra morale x 100
("game_get_morale_of_troops_from_faction",[
    (store_script_param_1, ":troop_no"),
    (store_troop_faction, ":faction_no", ":troop_no"),
    (try_begin),
        (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, reg0, ":faction_no",  slot_faction_morale_of_player_troops),
        #(assign, reg1, ":faction_no"),
        #(assign, reg2, ":troop_no"),
        #(assign, reg3, reg0),
        #(display_message, "@extra morale for troop {reg2} of faction {reg1} is {reg3}"),
    (else_try),
        (assign, reg0, 0),
    (try_end),

    (val_div, reg0, 100),
    (party_get_morale, reg1, "p_main_party"),
    (val_add, reg0, reg1),
    (set_trigger_result, reg0),
]),

#script_game_event_detect_party:
# This script is called from the game engine when player party inspects another party.
# INPUT:
# param1: Party-id
("game_event_detect_party",[
    (store_script_param_1, ":party_id"),
    (try_begin),
        (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
        (party_stack_get_troop_id, ":leader", ":party_id", 0),
        ##diplomacy start+ support for promoted kingdom ladies
        #(is_between, ":leader", heroes_begin, heroes_end),
        #(this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
        ##diplomacy end+
        (is_between, ":leader", active_npcs_begin, active_npcs_end),
        (call_script, "script_update_troop_location_notes", ":leader", 0),
    (else_try),
        (is_between, ":party_id", walled_centers_begin, walled_centers_end),
        (party_get_num_attached_parties, ":num_attached_parties",  ":party_id"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            (party_get_attached_party_with_rank, ":attached_party", ":party_id", ":attached_party_rank"),
            (party_stack_get_troop_id, ":leader", ":attached_party", 0),
            ##diplomacy start+ support for promoted kingdom ladies
            #(is_between, ":leader", heroes_begin, heroes_end),
            #(this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
            ##diplomacy end+
            (is_between, ":leader", active_npcs_begin, active_npcs_end),
            (call_script, "script_update_troop_location_notes", ":leader", 0),
        (try_end),
    (try_end),
]),

  #script_game_event_undetect_party:
  # This script is called from the game engine when player party inspects another party.
  # INPUT:
  # param1: Party-id
  ("game_event_undetect_party",
    [
    (store_script_param_1, ":party_id"),
    (try_begin),
      (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
      (party_stack_get_troop_id, ":leader", ":party_id", 0),
      ##diplomacy start+ support for promoted kingdom ladies
      #(is_between, ":leader", heroes_begin, heroes_end),
      #(this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
      ##diplomacy end+
      (is_between, ":leader", active_npcs_begin, active_npcs_end),
      (call_script, "script_update_troop_location_notes", ":leader", 0),
    (try_end),
  ]),

#script_game_get_statistics_line:
# This script is called from the game engine when statistics page is opened.
# INPUT:
# param1: line_no
("game_get_statistics_line",[
    (store_script_param_1, ":line_no"),
    (try_begin),
        (eq, ":line_no", 0),
        (get_player_agent_kill_count, reg1),
        (str_store_string, s1, "str_number_of_troops_killed_reg1"),
        (set_result_string, s1),
    (else_try),
        (eq, ":line_no", 1),
        (get_player_agent_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_troops_wounded_reg1"),
        (set_result_string, s1),
    (else_try),
        (eq, ":line_no", 2),
        (get_player_agent_own_troop_kill_count, reg1),
        (str_store_string, s1, "str_number_of_own_troops_killed_reg1"),
        (set_result_string, s1),
    (else_try),
        (eq, ":line_no", 3),
        (get_player_agent_own_troop_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_own_troops_wounded_reg1"),
        (set_result_string, s1),
    (try_end),
]),

#script_game_get_date_text:
# This script is called from the game engine when the date needs to be displayed.
# INPUT: arg1 = number of days passed since the beginning of the game
# OUTPUT: result string = date
#7 tage pro monate wie bei bannerlord
("game_get_date_text", [
    (store_script_param_2, ":num_hours"),
    (store_div, ":num_days", ":num_hours", 24),
    (store_add, ":cur_day", ":num_days", 1),
    (assign, ":cur_month", 6),
    (troop_get_slot, ":starting_year", "trp_global_variables", g_starting_year),
    (assign, ":cur_year", ":starting_year"),
    (assign, ":try_range", 99999),
    (try_for_range, ":unused", 0, ":try_range"),
        (assign, ":month_day_limit", 7),
        (try_begin),
            (gt, ":cur_day", ":month_day_limit"),
            (val_sub, ":cur_day", ":month_day_limit"),
            (val_add, ":cur_month", 1),
            (try_begin),
            (gt, ":cur_month", 12),
            (val_sub, ":cur_month", 12),
            (val_add, ":cur_year", 1),
            (try_end),
        (else_try),
            (assign, ":try_range", 0),
        (try_end),
    (try_end),
    (assign, reg1, ":cur_day"),
    (assign, reg2, ":cur_year"),
    (assign, "$g_cur_month", ":cur_month"),
    (try_begin),
        (eq, "$edict10", ":cur_month"),
        (str_store_troop_name, s1, "trp_bard_end"),
        (str_store_string, s1, "str_month_begin"),
    (else_try),
        (eq, ":cur_month", 1),
        (str_store_string, s1, "str_january_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 2),
        (str_store_string, s1, "str_february_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 3),
        (str_store_string, s1, "str_march_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 4),
        (str_store_string, s1, "str_april_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 5),
        (str_store_string, s1, "str_may_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 6),
        (str_store_string, s1, "str_june_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 7),
        (str_store_string, s1, "str_july_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 8),
        (str_store_string, s1, "str_august_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 9),
        (str_store_string, s1, "str_september_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 10),
        (str_store_string, s1, "str_october_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 11),
        (str_store_string, s1, "str_november_reg1_reg2"),
    (else_try),
        (eq, ":cur_month", 12),
        (str_store_string, s1, "str_december_reg1_reg2"),
    (try_end),
    (set_result_string, s1),
]),

#script_game_get_money_text:
# This script is called from the game engine when an amount of money needs to be displayed.
# INPUT: arg1 = amount in units
# OUTPUT: result string = money in text
("game_get_money_text",[
    (store_script_param_1, ":amount"),
    (try_begin),
        (eq, ":amount", 1),
        (str_store_string, s1, "str_1_denar"),
    (else_try),
        (assign, reg1, ":amount"),
        (str_store_string, s1, "str_reg1_denars"),
    (try_end),
    (set_result_string, s1),
]),

#script_game_get_party_companion_limit:
# This script is called from the game engine when the companion limit is needed for a party.
# INPUT: arg1 = none
# OUTPUT: reg0 = companion_limit
("game_get_party_companion_limit",[
    (store_script_param_1, ":party"),
    (assign, ":limit", 0),
    (try_begin),
        (eq, ":party", "p_main_party"),
        (call_script, "script_party_get_ideal_size", ":party"),
        (assign, ":limit", reg0),
    (else_try),
        (party_is_active, ":party"),#to be on the save side
        (neq, ":party", "p_main_party"),
        (try_begin),
            (eq, reg62, 1),
            (assign, ":limit", 0),
        #patrols and players camp
        (else_try),
            (this_or_next|eq, "$g_encountered_party_template", "pt_patrols_end"),
            (eq, "$g_encountered_party_template", "pt_player_camp"),

            (this_or_next|party_slot_eq, ":party", slot_party_type, spt_player_camp),
            (party_slot_eq, ":party", slot_party_type, spt_companion_raider),
            (assign, ":limit", 200),
            # add bonus from commander skills
            (party_get_slot, ":troop_no", ":party", slot_pcamp_camp_commander),
            (store_skill_level, ":skill", "skl_leadership", ":troop_no"),
            (store_attribute_level, ":charisma", ":troop_no", ca_charisma),
            (val_mul, ":skill", pcamp_commander_leadership_size_bonus),
            (val_mul, ":charisma", pcamp_commander_charisma_size_bonus),
            (val_add, ":limit", ":skill"),
            (val_add, ":limit", ":charisma"),
        #player latifundia
        (else_try),
            (eq, "$g_encountered_party_template", "pt_latifundium"),
            (party_slot_eq, ":party", slot_party_type, spt_latifundium),
            (assign, ":limit", 0),
            (try_begin),
                (party_slot_ge, ":party", slot_lat_guards, 1),
                (val_add, ":limit", 10),
            (try_end),
        #castles (if enabled flag to limit garrision)
        (else_try),
            (party_slot_eq, ":party", slot_party_type, spt_castle),
            (assign, ":limit", 1000),
            (try_begin),
                (party_slot_ge, ":party", slot_center_has_barracks, 1),
                (val_add, ":limit", 500),
            (try_end),
        #towns, if enabled flag to limit garrision
        (else_try),
            (party_slot_eq, ":party", slot_party_type, spt_town),
            (assign, ":limit", 2500),
            (try_begin),
                (party_slot_ge, ":party", slot_center_has_barracks, 1),
                (val_add, ":limit", 500),
            (try_end),
        (try_end),
    (try_end),
    (assign, reg0, ":limit"),
    (set_trigger_result, reg0),
]),

#script_game_reset_player_party_name:
# This script is called from the game engine when the player name is changed.
# INPUT: none
# OUTPUT: none
("game_reset_player_party_name",[
    (str_store_troop_name, s5, "trp_player"),
    (party_set_name, "p_main_party", s5),
     (troop_set_plural_name, "trp_player", s5),
]),

#script_game_get_troop_note
# This script is called from the game engine when the notes of a troop is needed.
# INPUT: arg1 = troop_no, arg2 = note_index
# OUTPUT: s0 = note
("game_get_troop_note",[
    (store_script_param_1, ":troop_no"),
    (store_script_param_2, ":note_index"),
    (set_trigger_result, 0),

    (str_store_troop_name, s54, ":troop_no"),
    (try_begin),
        (eq, ":troop_no", "trp_player"),
        (this_or_next|eq, "$player_has_homage", 1),
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        (assign, ":troop_faction", "$players_kingdom"),
    (else_try),
        (store_troop_faction, ":troop_faction", ":troop_no"),
    (try_end),
    (str_clear, s49),

    #Family notes
    (try_begin),
        ##diplomacy start+ add support for displaying relations with kings and claimants
        #(this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),
        #(eq, ":troop_no", "trp_player"),
        #(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

        (this_or_next|eq, ":troop_no", "trp_player"),
        (this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),#includes pretenders
        (is_between, ":troop_no", kings_begin, kings_end),

        ##The following would only show relations for kings and claimants if they are married.
        #(this_or_next|troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
        #	(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        #(this_or_next|troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
        #	(neg|is_between, ":troop_no", kings_begin, kings_end),

        ##diplomacy end+
        (assign, ":num_relations", 0),

        (try_begin),
            (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
            (gt, reg0, 0),
            (val_add, ":num_relations", 1),
        (try_end),
        ##diplomacy start+
        (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),
            (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
            (is_between, ":aristocrat", kings_begin, kings_end),
            (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            (gt, reg0, 0),
            (val_add, ":num_relations", 1),
        (try_end),
        (str_clear, s49),
        (try_begin),
            (call_script, "script_cf_troop_has_trait", ":troop_no", trait_triumphator),
            (str_store_string, s49, "@Traits: Vir triumphalis.^"),
        (try_end),
        (troop_get_slot, reg1, ":troop_no", slot_troop_age),
        (str_store_string, s49, "str__age_reg1"),
        (try_begin),
            (gt, ":num_relations", 0),
            (str_store_string, s49, "@{s49}^Family:"),

            (try_begin),
                (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
                (gt, reg0, 0),
                (str_store_troop_name_link, s12, "trp_player"),
                (val_sub, ":num_relations", 1),
                (try_begin),
                    (eq, ":num_relations", 0),
                    (str_store_string, s49, "str_s49_s12_s11_end"),
                (else_try),
                    (str_store_string, s49, "str_s49_s12_s11"),
                (try_end),
            (try_end),
            # #diplomacy start+
            (try_for_range, ":aristocrat", active_npcs_begin, kingdom_ladies_end),
                (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
                (is_between, ":aristocrat", kings_begin, kings_end),
                (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
                (gt, reg0, 0),
                (try_begin),
                    (neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name_link, s12, ":aristocrat"),
                    (call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
                    (str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
                (else_try),
                    (str_store_troop_name_link, s12, ":aristocrat"),
                    (val_sub, ":num_relations", 1),
                    (try_begin),
                        (eq, ":num_relations", 0),
                        (str_store_string, s49, "str_s49_s12_s11_end"),
                    (else_try),
                        (str_store_string, s49, "str_s49_s12_s11"),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),

        # love affairs:
        (try_begin),
            (this_or_next|troop_slot_ge, ":troop_no", slot_troop_lover_found, 0),
            (ge, "$cheat_mode", 1),

            (troop_get_slot, ":lover", ":troop_no", slot_troop_lover),
            (ge, ":lover", 0),
            (str_store_troop_name_link, s12, ":lover"),
            (str_store_string, s49, "@{s49}^^Lover: {s12}."),
        (try_end),

        (try_begin),
            (this_or_next|eq, ":troop_no", "trp_player"),
            (ge, "$cheat_mode", 1),
            (str_store_string, s49, "@{s49}^^Affairs:^"),
            (str_clear, s11),
            (assign, ":count", 0),
            (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
                (troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
                (troop_slot_eq, ":lady", slot_troop_lover, ":troop_no"),
                (str_store_troop_name_link, s12, ":lady"),
                (try_begin),
                    (eq, ":count", 0),
                    (str_store_string, s11, "@{s12}"),
                (else_try),
                    (eq, ":count", 1),
                    (str_store_string, s11, "@{s12} and {s11}"),
                (else_try),
                    (str_store_string, s11, "@{s12}, {s11}"),
                (try_end),
                (val_add, ":count", 1),
            (try_end),
            (try_begin),
                (str_is_empty, s11),
                (str_store_string, s11, "str_none"),
            (try_end),
            (str_store_string, s49, "@{s49} {s11}."),
        (try_end),
    (try_end),
    (try_begin),#minor factions
        (is_between, ":troop_faction", minor_kingdoms_begin, minor_kingdoms_end),
        (neq, ":troop_no", "trp_player"),
        (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name_link, s56, ":troop_faction"),
            (str_store_string, s0, "@{s54} is the ruler of {s56}."),
            (set_trigger_result, 1),
        (else_try),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
        (try_end),
    (else_try),#other guys, non lords
        (neq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (neg|is_between, ":troop_no", companions_begin, companions_end),
        # (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        (try_begin),
            (eq, ":note_index", 0),
            (str_store_string, s0, "str_s54_has_left_the_realm"),
            ##diplomacy start+
            #Check for "deceased" instead
            (try_begin),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
                (str_store_string, s0, "str_s54_is_deceased"),
            (else_try),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_heir),
                (str_store_string, s0, "str_s54_is_heir"),
            (else_try),
                (eq, ":troop_no", "trp_fortuna"),
                (str_store_string, s0, "@From Olymp, she looks at the world."),
            (else_try),
                (eq, ":troop_no", "trp_martial"),
                (str_store_string, s0, "@Currently, he lives in Rome."),
            (else_try),
                (eq, ":troop_no", "trp_iuvenal"),
                (str_store_string, s0, "@Currently, he lives in Alexandria."),
            (else_try),
                (is_between, ":troop_no", tournament_champions_begin, tournament_champions_end),
                (str_store_string, s0, "@He travelles around the world to fight in the arena."),
            (try_end),
            ##diplomacy end+
            (set_trigger_result, 1),
        (else_try),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
        (try_end),
    (else_try),#dead people
        (neq, ":troop_no", "trp_player"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
        (try_begin),
            (eq, ":note_index", 0),
            (str_store_string, s0, "str_s54_is_deceased"),
            (set_trigger_result, 1),
        (else_try),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
        (try_end),
    (else_try),#companions
        (is_between, ":troop_no", companions_begin, companions_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (eq, ":note_index", 0),
        (set_trigger_result, 1),
        (str_clear, s0),
        (assign, ":companion", ":troop_no"),
        (str_store_troop_name, s4, ":companion"),
        (try_begin),
            (this_or_next|main_party_has_troop, ":companion"),
            (this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
            (this_or_next|eq, "$praefectus_urbani", ":companion"),
            (eq, "$g_player_minister", ":companion"),
            #SB : replace the call
            (call_script, "script_companion_get_mission_string", ":companion"),
        ##diplomacy start+
        #Check for explicit "exiled" and "dead" settings
        (else_try),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_heir),
            (str_store_string, s0, "str_s54_is_heir"),
        (else_try),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
            (str_store_string, s0, "str_s54_has_left_the_realm"),
        ##diplomacy end+
        (else_try),
            (str_store_string, s0, "str_whereabouts_unknown"),
        (try_end),
        (troop_get_slot, reg20, ":troop_no", slot_troop_age),
        (troop_get_slot, reg21, ":troop_no", slot_troop_renown),

        (str_store_string, s0, "@{s0}^^Age: {reg20}. Renown: {reg21}."),

        (try_begin),#overwrite if deceased
            (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
            (str_store_string, s0, "str_s54_is_deceased"),
        (try_end),

    (else_try),#lords and stuff
        (try_begin),
            (eq, ":note_index", 0),
            (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
            (ge, ":faction_leader", 0),
            (str_store_troop_name_link, s55, ":faction_leader"),
            (str_store_faction_name_link, s56, ":troop_faction"),
            (assign, ":troop_is_player_faction", 0),
            (assign, ":troop_is_faction_leader", 0),
            (try_begin),
                (eq, ":troop_faction", "fac_player_faction"),
                (assign, ":troop_is_player_faction", 1),
            (else_try),
                (eq, ":faction_leader", ":troop_no"),
                (assign, ":troop_is_faction_leader", 1),
            (try_end),
            #SB: add marshal check
            (try_begin),
                (faction_slot_eq, ":troop_faction", slot_faction_marshall, ":troop_no"),
                (assign, ":troop_is_marshal", 1),
            (else_try),
                (assign, ":troop_is_marshal", 0),
            (try_end),
            (assign, ":num_centers", 0),
            (str_store_string, s58, "@nowhere"),
            (str_clear, s11),
            (try_begin),
                (faction_slot_eq, ":troop_faction", slot_faction_government_type, gov_imperial),
                (assign, ":end", p_provinces_end),
                (try_for_range, ":province", p_hisp_tarraco, ":end"),
                    (troop_slot_eq, "trp_province_array", ":province", ":troop_no"),
                    (store_add, ":string", "str_province_begin", ":province"),
                    (str_store_string, s69, ":string"),
                    (assign, ":end", -1),
                (try_end),
                (eq, ":end", -1),
                (store_add, ":slot", slot_province_senatorial_begin, ":province"),
                (troop_get_slot, ":timer", "trp_province_array", ":slot"),
                (try_begin),
                    (ge, ":timer", 1),
                    (store_current_day, ":day"),
                    (val_sub, ":timer", ":day"),
                    (val_max, ":timer", 1),
                    (assign, reg0, ":timer"),
                    (str_store_string, s71, "@It is a senatorial province, governorship expires in approximatly {reg0} days"),
                (else_try),
                    (str_store_string, s71, "@It is an imperial province."),
                (try_end),
            (try_end),
            (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
                (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
                (try_begin),
                    (eq, ":num_centers", 0),
                    (str_store_party_name_link, s58, ":cur_center"),
                (else_try),
                    (eq, ":num_centers", 1),
                    (str_store_party_name_link, s57, ":cur_center"),
                    (str_store_string, s58, "@{s57} and {s58}"),
                (else_try),
                    (str_store_party_name_link, s57, ":cur_center"),
                    (str_store_string, s58, "@{!}{s57}, {s58}"),
                (try_end),
                (val_add, ":num_centers", 1),
            (try_end),
            (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),

            (str_clear, s59),
            (try_begin),
                (call_script, "script_troop_get_player_relation", ":troop_no"),
                (assign, ":relation", reg0),
                (store_add, ":normalized_relation", ":relation", 100),
                (val_add, ":normalized_relation", 5),
                (store_div, ":str_offset", ":normalized_relation", 10),
                (val_clamp, ":str_offset", 0, 20),
                (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
                (neq, ":str_id", "str_relation_plus_0_ns"),
                (str_store_string, s60, "@{reg3?She:He}"),
                (str_store_string, s59, ":str_id"),
                (str_store_string, s59, "@{!}^{s59}"),
            (try_end),
            #lord recruitment changes begin
            #This sends a bunch of political information to s47.
            (str_clear, s35),
            ##personality
            (try_begin),
                (troop_slot_ge, ":troop_no", slot_troop_met, 1),
                (troop_get_slot, ":personality", ":troop_no", slot_lord_reputation_type),
                (store_add, ":string", "str_personality_archetypes", ":personality"),
                (str_store_string, s34, ":string"),
                (str_store_string, s35, "@Personality: {reg3?She:He} seems to be a {s34} person."),
            (try_end),
            (str_clear, s26),
            (try_begin),
                (troop_get_slot,reg49, ":troop_no", slot_troop_loses),
                (troop_get_slot,reg50, ":troop_no", slot_troop_loses_wife),
                (troop_get_slot,reg51, ":troop_no", slot_troop_loses_lover),
                (troop_get_slot,reg52, ":troop_no", slot_troop_paid_taxes),
                (troop_get_slot,reg53, ":troop_no", slot_troop_money_to_center),
                (troop_get_slot,":title", ":troop_no", slot_troop_honorary_title),
                (try_begin),
                    (gt, ":title", 0),
                    (val_add, ":title", "str_title_begin"),
                    (str_store_string, s44, ":title"),
                    (str_store_string, s26, "@He has the honorary title of {s44}"),
                (try_end),
                (try_begin),
                    (gt, reg49, 0),
                    (str_store_string, s26, "@{s26}^Last week he spend for court, servants, cloths, etc {reg49} denars"),
                (try_end),
                (try_begin),
                    (gt, reg50, 0),
                    (str_store_string, s26, "@{s26}^Last week he spend for his family {reg50} denars"),
                (try_end),
                (try_begin),
                    (gt, reg51, 0),
                    (str_store_string, s26, "@{s26}^Last week he spend for his love affairs {reg51} denars"),
                (try_end),
                (try_begin),
                    (gt, reg52, 0),
                    (str_store_string, s26, "@{s26}^Last week he paid {reg52} denars imperial tax."),
                (try_end),
                (try_begin),
                    (gt, reg53, 0),
                    (str_store_string, s26, "@{s26}^Last week he donated {reg53} denars to his settlements."),
                (try_end),
            (try_end),
            (str_clear, s53),
            #refresh registers
            (assign, reg9, ":num_centers"),
            ##diplomacy start+ use script for gender
            #(troop_get_type, reg3, ":troop_no"),
            (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),
            ##diplomacy end+

            #SB : rearrange registers a bit
            (assign, reg4, ":troop_is_faction_leader"),
            (assign, reg5, ":troop_is_marshal"),
            (assign, reg6, ":troop_is_player_faction"),

            #SB : TODO, add rounding based on personal relation/time last met?
            (troop_get_slot, reg15, ":troop_no", slot_troop_renown),
            (troop_get_slot, reg16, ":troop_no", slot_troop_controversy),
            #SB : actually use this wealth in string
            (try_begin),
                (eq, ":troop_no", "trp_player"),
                (store_troop_gold, reg17, "trp_player"),
            (else_try),
                (troop_get_slot, reg17, ":troop_no", slot_troop_wealth), #DEBUGS
            (try_end),
            ##diplomacy start+ xxx remove third argument (was it doing anything?)
            #(str_store_string, s0, "str_lord_info_string", 0),
            (try_begin),
                (eq, reg3, 0),
                (try_begin),
                    (troop_slot_ge, ":troop_no", slot_troop_govern, 1),
                    (str_store_string, s27, "@governor"),
                (else_try),
                    (troop_slot_eq, ":troop_no", slot_troop_legion, 12),
                    (str_store_string, s27, "@praefectus praetorio"),
                (else_try),
                    (troop_slot_ge, ":troop_no", slot_troop_legion, 1),
                    (str_store_string, s27, "@legatus legionis"),
                (else_try),
                    (troop_slot_ge, ":troop_no", slot_troop_aux, 1),
                    (str_store_string, s27, "@auxiliary commander"),
                (else_try),
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_4"),
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_3"),
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_1"),
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_2_1"),
                    (troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_2"),
                    (str_store_string, s27, "@chieftain"),
                (else_try),
                    (this_or_next|troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_5"),
                    (troop_slot_eq, ":troop_no", slot_troop_culture, "fac_culture_6"),
                    (str_store_string, s27, "@vassal"),
                (else_try),
                    (str_store_string, s27, "@noble"),
                (try_end),
            (else_try),
                (str_store_string, s27, "@noblewoman"),
            (try_end),
            (try_begin),
                (troop_get_slot, ":legion", ":troop_no",slot_troop_legion),
                (ge, ":legion", 1),
                (try_begin),
                    (eq, ":legion", 13),
                    (str_store_troop_name, s28, "trp_players_legion"),
                (else_try),
                    (store_add, ":string", "str_lover_talk", ":legion"),
                    (str_store_string, s28, ":string"),
                (try_end),
                (str_store_string, s53, "@He commands the {s28}."),

                (try_begin),
                    (call_script, "script_get_troop_headquarter", ":troop_no"),
                    (is_between, reg0, walled_centers_begin, walled_centers_end),
                    (str_store_party_name_link, s0, reg0),
                    (str_store_string, s53, "@{s53} The headquarters are in {s0}."),
                (try_end),
                (str_store_string, s53, "@{s53}^^It has the following auxiliar units attached:"),
                (str_store_string, s29, "@None."),
                (try_for_range, ":aux_commander_slot", slot_aux_commander_begin, slot_aux_commander_end),
                    (store_sub, ":aux_legion_slot", ":aux_commander_slot", slot_aux_commander_begin),
                    (val_add, ":aux_legion_slot", slot_aux_legion_begin),
                    (troop_slot_eq, "trp_province_array", ":aux_legion_slot", ":legion"),
                    (troop_get_slot, ":aux_comander", "trp_province_array", ":aux_commander_slot"),
                    (is_between, ":aux_comander", active_npcs_begin, active_npcs_end),

                    (troop_get_slot, ":aux", ":aux_comander",slot_troop_aux),
                    (ge, ":aux", 1),
                    (try_begin),
                        (eq, ":aux", "pt_player_aux_inf"),
                        (str_store_troop_name, s28, "trp_players_aux_inf"),
                    (else_try),
                        (eq, ":aux", "pt_player_aux_cav"),
                        (str_store_troop_name, s28, "trp_players_aux_cav"),
                    (else_try),
                        (val_sub, ":aux", "pt_cohors_aux"),
                        (val_add, ":aux", "str_cohors_aux"),
                        (str_store_string, s28, ":aux"),
                    (try_end),
                    (str_store_troop_name_link, s0, ":aux_comander"),
                    (str_store_string, s29, "@^{s28}, commanded by {s0}."),
                (try_end),
                (str_store_string, s53, "@{s53}^{s29}"),
                (troop_get_slot, reg18, ":troop_no", slot_troop_triumph_points),
                (str_store_string, s0, "str_lord_info_string_legion"),
            (else_try),
                (troop_get_slot, ":aux", ":troop_no",slot_troop_aux),
                (ge, ":aux", 1),
                (val_sub, ":aux", "pt_cohors_aux"),
                (store_add, ":slot", slot_aux_legion_begin, ":aux"),
                (troop_get_slot, ":legion", "trp_province_array", ":slot"),
                (try_begin),
                    (eq, ":legion", 13),
                    (str_store_troop_name, s0, "trp_players_legion"),
                (else_try),
                    (store_add, ":string", "str_lover_talk", ":legion"),
                    (str_store_string, s0, ":string"),
                (try_end),

                (store_add, ":slot", ":legion", slot_legion_commanders_begin),
                (troop_get_slot, ":legate", "trp_province_array", ":slot"),
                (str_store_string, s29, "str_noone"),
                (try_begin),
                    (ge, ":legate", 0),
                    (str_store_troop_name_link, s29, ":legate"),
                (try_end),
                (try_begin),
                    (eq, ":aux", pt_player_aux_inf - pt_cohors_aux),
                    (str_store_troop_name, s28, "trp_players_aux_inf"),
                (else_try),
                    (eq, ":aux", pt_player_aux_cav - pt_cohors_aux),
                    (str_store_troop_name, s28, "trp_players_aux_cav"),
                (else_try),
                    (val_add, ":aux", "str_cohors_aux"),
                    (str_store_string, s28, ":aux"),
                (try_end),
                (str_store_string, s53, "@He commands the {s28}, which is part of {s0} (commanded by {s29})."),
                (troop_get_slot, reg18, ":troop_no", slot_troop_triumph_points),
                (str_store_string, s0, "str_lord_info_string_legion"),
            (else_try),
                (faction_slot_eq, ":troop_faction", slot_faction_government_type, gov_imperial),
                (troop_get_slot, reg18, ":troop_no", slot_troop_triumph_points),
                (str_store_string, s0, "str_lord_info_string_imperial"),
            (else_try),
                (str_store_string, s0, "str_lord_info_string_feudal"),
            (try_end),

            ##if player finishes the quest he get a cognomen
            (try_begin),
                (eq, ":troop_no", "trp_player"),
                (this_or_next|quest_slot_ge, "qst_blank_quest_22", slot_quest_target_dna, 1),
                (this_or_next|quest_slot_ge, "qst_blank_quest_25", slot_quest_target_dna, 1),
                (this_or_next|quest_slot_ge, "qst_blank_quest_24", slot_quest_target_dna, 1),
                (quest_slot_ge, "qst_blank_quest_23", slot_quest_target_dna, 1),

                (str_store_string_reg, s2, s0),
                (call_script, "script_print_cognomen_to_s1"),
                (str_store_string_reg, s0, s2),
                (str_store_string, s0, "@Cognomina: {s1}^^{s0}"),
            (try_end),

            ##diplomacy end+
            #lord recruitment changes end
            (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
            (set_trigger_result, 1),
        (try_end),
    (try_end),
]),

#script_game_get_center_note
# This script is called from the game engine when the notes of a center is needed.
# INPUT: arg1 = center_no, arg2 = note_index
# OUTPUT: s0 = note
("game_get_center_note",[
    (store_script_param_1, ":center_no"),
    (store_script_param_2, ":note_index"),

    (set_trigger_result, 0),
    (try_begin),
        (eq, ":note_index", 0),
        (party_get_slot, ":lord_troop", ":center_no", slot_town_lord),
        (try_begin),
            (ge, ":lord_troop", 0),
            (store_troop_faction, ":lord_faction", ":lord_troop"),
            (str_store_troop_name_link, s1, ":lord_troop"),
            (try_begin),
                (eq, ":lord_troop", "trp_player"),
                (gt, "$players_kingdom", 0),
                (str_store_faction_name_link, s2, "$players_kingdom"),
            (else_try),
                (str_store_faction_name_link, s2, ":lord_faction"),
            (try_end),
            (str_store_party_name, s50, ":center_no"),
            (try_begin),
                (party_slot_eq, ":center_no", slot_party_type, spt_town),
                (str_store_string, s51, "@The town of {s50}"),
            (else_try),
                (party_slot_eq, ":center_no", slot_party_type, spt_village),
                (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
                (str_store_party_name_link, s52, ":bound_center"),
                (str_store_string, s51, "@The village of {s50} near {s52}"),
            (else_try),
                (str_store_string, s51, "@{!}{s50}"),
            (try_end),
                ##diplomacy start+ Show when the city is the home of a lord or is a court
            (assign, ":bound_center", reg0),#Save reg0 to avoid having it randomly change
            (try_begin),
                (eq, "$g_player_court", ":center_no"),
                (store_and, reg1, "$players_kingdom_name_set", rename_center), #SB : specify capitals
                (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is {reg1?your capital:where you make your court}.^"),
            (else_try),
                (neq, ":lord_troop", "trp_player"),
                (neg|is_between, ":center_no", villages_begin, villages_end),
                (call_script, "script_lord_get_home_center", ":lord_troop"),
                (eq, reg0, ":center_no"),
                (call_script, "script_dplmc_get_troop_standing_in_faction", ":lord_troop", ":lord_faction"),
                (try_begin),
                    (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
                    (call_script, "script_dplmc_store_troop_is_female", ":lord_troop"),
                    (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is where {reg0?she:he} makes {reg0?her:his} court.^"),
                (else_try),
                    (call_script, "script_dplmc_store_troop_is_female", ":lord_troop"),
                    (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is where {reg0?she:he} makes {reg0?her:his} home.^"),
                (try_end),
            (else_try),#Fall through to normal behavior
                ##diplomacy end+
                (str_store_string, s2, "@{s51} belongs to {s1} of {s2}.^"),
                ##diplomacy start+
            (try_end),
            (assign, reg0, ":bound_center"),#Revert reg0 to avoid having it randomly change
            ##diplomacy end+
        (else_try),
            (str_clear, s2),
            ##diplomacy start+ Don't hide notes for centers with no lords.
            (store_faction_of_party, ":lord_faction", ":center_no"),
            (str_store_string, s1, "str_noone"),
            (try_begin),
                (ge, ":lord_faction", 1),
                (str_store_faction_name_link, s2, ":lord_faction"),
            (else_try),
                (str_store_string, s2, "str_noone"),
            (try_end),
            (str_store_party_name, s50, ":center_no"),
            (try_begin),
                (party_slot_eq, ":center_no", slot_party_type, spt_town),
                (str_store_string, s51, "@The town of {s50}"),
            (else_try),
                (party_slot_eq, ":center_no", slot_party_type, spt_village),
                (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
                (str_store_party_name_link, s52, ":bound_center"),
                (str_store_string, s51, "@The village of {s50} near {s52}"),
            (else_try),
                (str_store_string, s51, "@{!}{s50}"),
            (try_end),
            (try_begin),
                (is_between, ":lord_faction", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":lord_faction", slot_faction_state, sfs_active),
                (str_store_string, s2, "@{s51} belongs to {s2} but has not yet been granted to a lord.^"),
            (else_try),
                (str_store_string, s2, "@{s51} belongs to {s2}.^"),
            (try_end),
            ##diplomacy end+
        (try_end),
        (try_begin),
            (is_between, ":center_no", villages_begin, villages_end),
            ##diplomacy start+ Show market town if it differs from the bound center
            (party_get_slot, ":market_center", ":center_no", slot_village_market_town),
            (try_begin),
                (is_between, ":market_center", centers_begin, centers_end),
                (neq, ":market_center", ":center_no"),
                (neg|party_slot_eq, ":center_no", slot_village_bound_center, ":market_center"),
                (str_store_party_name_link, s8, ":market_center"),
                (str_store_string, s2, "@{s2}Its market town is {s8}.^"),
            (try_end),
            ##diplomacy end+
        (else_try),
            (assign, ":num_villages", 0),
            (try_for_range_backwards, ":village_no", villages_begin, villages_end),
                (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
                (try_begin),
                    (eq, ":num_villages", 0),
                    (str_store_party_name_link, s8, ":village_no"),
                (else_try),
                    (eq, ":num_villages", 1),
                    (str_store_party_name_link, s7, ":village_no"),
                    (str_store_string, s8, "@{s7} and {s8}"),
                (else_try),
                    (str_store_party_name_link, s7, ":village_no"),
                    (str_store_string, s8, "@{!}{s7}, {s8}"),
                (try_end),
                (val_add, ":num_villages", 1),
            (try_end),
            (try_begin),
                (eq, ":num_villages", 0),
                (str_store_string, s2, "@{s2}It has no villages.^"),
            (else_try),
                (store_sub, reg0, ":num_villages", 1),
                (str_store_string, s2, "@{s2}{reg0?Its villages are:Its village is} {s8}.^"),
            (try_end),
        (try_end),
        (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
        #(party_get_slot, reg7, ":center_no", slot_town_prosperity),
        (str_store_string, s2, "@{s2}Its prosperity is: {s50}", 0),

        (try_begin),
            (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (party_get_slot, reg1, ":center_no", slot_town_wealth),
            (str_store_string, s2, "@{s2}^Treasury of the town watch: {reg1} denars", 0),
        (try_end),

        (party_get_slot, reg1, ":center_no", slot_center_capital),
        (str_store_string, s2, "@{s2}^Its wealth is: {reg1}", 0),

        (try_begin),
            (is_between, ":center_no", centers_begin, centers_end),#not for minor towns
            (str_store_string, s2, "@{s2}^^The following buildings have been constructed:"),
            (try_for_range, ":buildings", village_improvements_begin, slot_center_has_forum),
                (party_slot_ge, ":center_no",":buildings", 1),
                (call_script, "script_get_improvement_details", ":buildings", ":center_no"),
                (str_store_string, s2, "@{s2} {s0},"),
            (try_end),
        (try_end),

        (try_begin),
            (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (str_store_string, s2, "@{s2}^^The following decrees have been issued:"),
            (try_for_range, ":decree", slot_center_decree_curfew, slot_center_capital),
                (party_slot_eq, ":center_no", ":decree", 1),
                (store_sub, ":string", ":decree", slot_center_decree_curfew),
                (val_add, ":string", "str_decree_curfew_name"),
                (str_store_string, s48, ":string"),
                (str_store_string, s2, "@{s2} {s48},"),
            (try_end),
        (try_end),

        (try_begin),#not for minor towns
            (is_between, ":center_no", centers_begin, centers_end),
            (party_get_slot, ":province", ":center_no", slot_center_province),
            (val_add, ":province", "str_province_begin"),
            (str_store_string, s49, ":province"),
            (str_store_string, s2, "@{s2}^^Province: {s49}"),
        (try_end),

        (str_store_string, s0, "@{s2}", 0),
        (set_trigger_result, 1),
    (try_end),
]),

  #script_game_get_faction_note
  # This script is called from the game engine when the notes of a faction is needed.
  # INPUT: arg1 = faction_no, arg2 = note_index
  # OUTPUT: s0 = note
("game_get_faction_note",[
    (store_script_param_1, ":faction_no"),
    (store_script_param_2, ":note_index"),
    (set_trigger_result, 0),

    (try_begin),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        #conditions end
        (try_begin),
            (eq, ":note_index", 0),
            (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
            (ge, ":faction_leader", 0),
            (str_store_faction_name, s5, ":faction_no"),
            (try_begin),
                (lt, ":faction_leader", 0),
                (str_store_string, s6, "str_noone"),
            (else_try),
                (eq, ":faction_leader", "trp_kingdom_heroes_including_player_begin"),
                (assign, ":faction_leader", "trp_player"),
                (str_store_troop_name_link, s6, ":faction_leader"),
            (else_try),
                (str_store_troop_name_link, s6, ":faction_leader"),
            (try_end),
            (assign, ":num_centers", 0),

            #faction centers
            (str_store_string, s8, "@nowhere"),
            (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
                (store_faction_of_party, ":center_faction", ":cur_center"),
                (eq, ":center_faction", ":faction_no"),
                (try_begin),
                    (eq, ":num_centers", 0),
                    (str_store_party_name_link, s8, ":cur_center"),
                (else_try),
                    (eq, ":num_centers", 1),
                    (str_store_party_name_link, s7, ":cur_center"),
                    (str_store_string, s8, "@{s7} and {s8}"),
                (else_try),
                    (str_store_party_name_link, s7, ":cur_center"),
                    (str_store_string, s8, "@{!}{s7}, {s8}"),
                (try_end),
                (val_add, ":num_centers", 1),
            (try_end),
            (assign, ":num_members", 0),
            (assign, ":num_members_1", 0),
            (assign, ":num_members_2", 0),
            (str_store_string, s10, "@noone"),
            (str_store_string, s31, "@noone"),
            (str_store_string, s32, "@noone"),

            #faction members
            (try_for_range_backwards, ":loop_var", "trp_kingdom_heroes_including_player_begin", heroes_end),#<- changed active_npcs_end to heroes_end
                (assign, ":cur_troop", ":loop_var"),
                (try_begin),
                    (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
                    (assign, ":cur_troop", "trp_player"),
                    (assign, ":troop_faction", "$players_kingdom"),
                (else_try),
                    (store_troop_faction, ":troop_faction", ":cur_troop"),
                (try_end),
                (eq, ":troop_faction", ":faction_no"),
                (neq, ":cur_troop", ":faction_leader"),
                (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
                (try_begin),
                    (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),
                    (this_or_next|troop_slot_ge, ":cur_troop", slot_troop_legion, 1),
                    (troop_slot_ge, ":cur_troop", slot_troop_aux, 1),
                    (try_begin),
                        (eq, ":num_members_1", 0),
                        (str_store_troop_name_link, s31, ":cur_troop"),
                    (else_try),
                        (eq, ":num_members_1", 1),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s31, "@{s9} and {s31}"),
                    (else_try),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s31, "@{!}{s9}, {s31}"),
                    (try_end),
                    (val_add, ":num_members_1", 1),
                (else_try),
                    (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),
                    (troop_slot_ge, ":cur_troop", slot_troop_govern, 1),
                    (try_begin),
                        (eq, ":num_members_2", 0),
                        (str_store_troop_name_link, s32, ":cur_troop"),
                    (else_try),
                        (eq, ":num_members_2", 1),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s32, "@{s9} and {s32}"),
                    (else_try),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s32, "@{!}{s9}, {s32}"),
                    (try_end),
                    (val_add, ":num_members_2", 1),
                (else_try),
                    (try_begin),
                        (eq, ":num_members", 0),
                        (str_store_troop_name_link, s10, ":cur_troop"),
                    (else_try),
                        (eq, ":num_members", 1),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s10, "@{s9} and {s10}"),
                    (else_try),
                        (str_store_troop_name_link, s9, ":cur_troop"),
                        (str_store_string, s10, "@{!}{s9}, {s10}"),
                    (try_end),
                    (val_add, ":num_members", 1),
                (try_end),
            (try_end),

            (str_store_string, s12, "@noone"),

            ##SB : add domestic policy as overview
            (str_clear, s21),
            (str_clear, s20),

            (str_store_string, s20, "@Domestic policy: ^^"),
            (call_script, "script_display_policy_string_to_reg", ":faction_no", 0, 1),

            #other foreign relations
            (str_store_string, s21, "str_foreign_relations__"),

            (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
                (neq, ":faction_no", ":cur_faction"),
                (str_store_faction_name_link, s14, ":cur_faction"),
                (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction_no", ":cur_faction"),
                (assign, ":diplomatic_status", reg0),
                (assign, ":duration_of_status", reg1),

                (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_faction", ":faction_no"),
                (assign, ":reverse_diplomatic_status", reg0),
                (try_begin),
                    (eq, ":diplomatic_status", -2),
                    (str_store_string, s21, "str_s21__the_s5_is_at_war_with_the_s14"),
                    (store_add, ":slot_war_damage_inflicted", ":cur_faction", slot_faction_war_damage_inflicted_on_factions_begin),
                    (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
                    (faction_get_slot, ":war_damage_inflicted", ":faction_no", ":slot_war_damage_inflicted"),
                    (store_mul, ":war_damage_inflicted_x_2", ":war_damage_inflicted", 2),

                    (store_add, ":slot_war_damage_suffered", ":faction_no", slot_faction_war_damage_inflicted_on_factions_begin),
                    (val_sub, ":slot_war_damage_suffered", kingdoms_begin),
                    (faction_get_slot, ":war_damage_suffered", ":cur_faction", ":slot_war_damage_suffered"),
                    (store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),

                    (assign, ":war_cause", 0),
                    (assign, ":attacker", 0),
                    (try_for_range, ":log_entry", 0, "$num_log_entries"),
                        (troop_get_slot, ":type", "trp_log_array_entry_type", ":log_entry"),
                        (is_between, ":type", logent_faction_declares_war_out_of_personal_enmity, logent_war_declaration_types_end),
                        (troop_get_slot, ":actor", "trp_log_array_actor", ":log_entry"),
                        (troop_get_slot, ":object", "trp_log_array_faction_object", ":log_entry"),

                        (try_begin),
                            (eq, ":actor", ":cur_faction"),
                            (eq, ":object", ":faction_no"),
                            (assign, ":war_cause", ":type"),
                            (assign, ":attacker", ":actor"),
                        (else_try),
                            (eq, ":actor", ":faction_no"),
                            (eq, ":object", ":cur_faction"),
                            (assign, ":war_cause", ":type"),
                            (assign, ":attacker", ":actor"),
                        (try_end),
                    (try_end),

                    #bug fix! backing up s8 to somewhere else
                    (str_store_string, s25, s8),
                    (try_begin),
                        (gt, ":war_cause", 0),
                        (str_store_faction_name, s8, ":attacker"),
                        (try_begin),
                            (eq, ":war_cause", logent_faction_declares_war_out_of_personal_enmity),
                            (str_store_string, s21, "str_s21_the_s8_declared_war_out_of_personal_enmity"),
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_respond_to_provocation),
                            (str_store_string, s21, "str_s21_the_s8_declared_war_in_response_to_border_provocations"),
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_curb_power),
                            (str_store_string, s21, "str_s21_the_s8_declared_war_to_curb_the_other_realms_power"),
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_regain_territory),
                            (str_store_string, s21, "str_s21_the_s8_declared_war_to_regain_lost_territory"),
                        ##diplomacy begin
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_fulfil_pact),
                            (str_store_string, s21, "str_dplmc_s21_the_s8_declared_war_to_fulfil_pact"),
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_end_civil_war),
                            (str_store_string, s21, "str_dplmc_s21_the_s8_declared_war_to_end_civil_war"),
                        (else_try),
                            (eq, ":war_cause", logent_faction_declares_war_to_declare_independence),
                            (str_store_string, s21, "str_dplmc_s21_the_s8_declared_war_to_declare_independence"),
                        ##diplomacy end
                        (else_try),
                            (eq, ":war_cause", logent_player_faction_declares_war),
                            (neq, ":attacker", "fac_player_supporters_faction"),
                            (str_store_string, s21, "str_s21_the_s8_declared_war_as_part_of_a_bid_to_conquer_all_calradia"),
                        (try_end),
                    (try_end),
                    #bug fix! restoring the back up to s8
                    (str_store_string, s8, s25),

                    (try_begin),
                        (gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
                        (str_store_string, s21, "str_s21_the_s5_has_had_the_upper_hand_in_the_fighting"),
                    (else_try),
                        (gt, ":war_damage_suffered", ":war_damage_inflicted_x_2"),
                        (str_store_string, s21, "str_s21_the_s5_has_gotten_the_worst_of_the_fighting"),
                    (else_try),
                        (gt, ":war_damage_inflicted", 100),
                        (gt, ":war_damage_inflicted", 100),
                        (str_store_string, s21, "str_s21_the_fighting_has_gone_on_for_some_time_and_the_war_may_end_soon_with_a_truce"),
                    (else_try),
                        (str_store_string, s21, "str_s21_the_fighting_has_begun_relatively_recently_and_the_war_may_continue_for_some_time"),
                    (try_end),
                    (try_begin),
                        (eq, "$cheat_mode", 1),
                        (assign, reg4, ":war_damage_inflicted"),
                        (assign, reg5, ":war_damage_suffered"),
                        (str_store_string, s21, "str_s21_reg4reg5"),
                    (try_end),
                (else_try),
                    (eq, ":diplomatic_status", 1),
                    (str_clear, s18),
                    (try_begin),
                        (neq, ":reverse_diplomatic_status", 1),
                        (str_store_string, s18, "str__however_the_truce_is_no_longer_binding_on_the_s14"),
                    (try_end),
                    (assign, reg1, ":duration_of_status"),
                    (try_begin),
                        (is_between, ":duration_of_status", dplmc_treaty_truce_days_expire + 1, dplmc_treaty_truce_days_initial + 1),
                        (str_store_string, s21, "str_s21__the_s5_is_bound_by_truce_not_to_attack_the_s14s18_the_truce_will_expire_in_reg1_days"),
                    (else_try),
                        (is_between, ":duration_of_status", dplmc_treaty_trade_days_expire + 1, dplmc_treaty_trade_days_initial + 1),
                        (val_sub, reg1, dplmc_treaty_trade_days_expire),
                        (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_trade_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
                    (else_try),
                        (is_between, ":duration_of_status", dplmc_treaty_defense_days_expire + 1, dplmc_treaty_defense_days_initial + 1),
                        (val_sub, reg1, dplmc_treaty_defense_days_expire),
                        (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_defensive_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
                    (else_try),
                        (is_between, ":duration_of_status", dplmc_treaty_alliance_days_expire + 1, dplmc_treaty_alliance_days_initial + 1),
                        (val_sub, reg1, dplmc_treaty_alliance_days_expire),
                        (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_alliance_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
                    (else_try),
                        (is_between, ":duration_of_status", dplmc_treaty_tributary_days_expire + 1, dplmc_treaty_tributary_days_initial + 1),
                        (val_sub, reg1, dplmc_treaty_tributary_days_expire),
                        (faction_get_slot, ":tributary_cur", ":cur_faction", slot_faction_tributary_of),
                        (faction_get_slot, ":tributary_no", ":faction_no", slot_faction_tributary_of),
                        (try_begin),
                            (eq, ":tributary_cur", ":faction_no"),
                            (str_store_string, s21, "str_s5_over_s14"),
                        (else_try),
                            (eq, ":tributary_no", ":cur_faction"),
                            (str_store_string, s21, "str_s14_over_s5"),
                        (try_end),
                    (try_end),
                (else_try),
                    (ge, "$cheat_mode", 1),
                    (eq, ":diplomatic_status", 0),
                    (str_store_string, s21, "str_s21__the_s5_has_no_outstanding_issues_with_the_s14"),
                (try_end),
                (try_begin),
                    # (eq, ":diplomatic_status", -1),
                    (store_add, ":slot_provocation_days", ":cur_faction", slot_faction_provocation_days_with_factions_begin),
                    (val_sub, ":slot_provocation_days", kingdoms_begin),
                    (faction_get_slot, reg41, ":faction_no", ":slot_provocation_days"),
                    (gt, reg41, 0),
                    (val_max, reg41, 1),
                    (str_store_string, s21, "str_s21__the_s5_has_recently_suffered_provocation_by_subjects_of_the_s14_and_there_is_a_risk_of_war_reg41"),
                (try_end),
                (try_begin),
                    # (eq, ":reverse_diplomatic_status", -1),
                    (store_add, ":slot_provocation_days", ":faction_no", slot_faction_provocation_days_with_factions_begin),
                    (val_sub, ":slot_provocation_days", kingdoms_begin),
                    (faction_get_slot, reg41, ":cur_faction", ":slot_provocation_days"),
                    (gt, reg41, 0),
                    (val_max, reg41, 1),
                    (str_store_string, s21, "str_s21_the_s14_was_recently_provoked_by_subjects_of_the_s5_and_there_is_a_risk_of_war_reg41"),
                (try_end),
                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (call_script, "script_npc_decision_checklist_peace_or_war", ":faction_no", ":cur_faction", -1),
                    (str_store_string, s21, "@{!}DEBUG : {s21}.^CHEAT MODE ASSESSMENT: {s14}^"),
                (try_end),
            (try_end),
            (try_begin),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),
                (str_store_string, s0, "str_the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21_rome", 0),
            (else_try),
                (str_store_string, s0, "str_the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", 0),
            (try_end),
            (try_begin),
                (ge, "$cheat_mode", 1),
                (faction_slot_eq, ":faction_no", slot_faction_government_type, gov_imperial),
                (faction_get_slot, reg1, ":faction_no", slot_faction_treasury),
                (faction_get_slot, reg2, ":faction_no", slot_faction_debts),
                (str_store_string, s0, "@{s0}^^Treasury: {reg1}. Debts: {reg2}"),
                (try_for_range, ":budget_item", slot_faction_hire, slot_faction_spending_diplomacy+1),
                    (store_sub, ":string", ":budget_item", slot_faction_hire),
                    (val_add, ":string", "str_faction_hire"),
                    (str_store_string, s1, ":string"),
                    (faction_get_slot, reg1, ":faction_no", ":budget_item"),
                    (str_store_string, s0, "@{s0}^{s1}: {reg1}."),
                (try_end),
                (try_for_range, ":budget_item", slot_faction_taxes_govern, slot_faction_taxes_diplomacy+1),
                    (store_sub, ":string", ":budget_item", slot_faction_taxes_govern),
                    (val_add, ":string", "str_faction_taxes_govern"),
                    (str_store_string, s1, ":string"),
                    (faction_get_slot, reg1, ":faction_no", ":budget_item"),
                    (str_store_string, s0, "@{s0}^{s1}: {reg1}."),
                (try_end),
            (try_end),
            (set_trigger_result, 1),
        (try_end),
    (else_try),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_defeated),
        (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name, s5, ":faction_no"),
            (str_store_string, s0, "@{s5} has been defeated!", 0),
            (set_trigger_result, 1),
        (else_try),
            (eq, ":note_index", 1),
            (str_clear, s0),
            (set_trigger_result, 1),
        (try_end),
    (else_try),
        (is_between, ":faction_no", minor_kingdoms_begin, minor_kingdoms_end),
        (eq, ":note_index", 0),

        (faction_get_slot, ":lord", ":faction_no", slot_faction_leader),
        (str_store_string, s49, "str_noone"),
        (try_begin),
            (ge, ":lord", 0),
            (str_store_troop_name_link, s49, ":lord"),
        (try_end),
        (str_store_faction_name, s48, ":faction_no"),
        (store_relation, reg33, ":faction_no", "$players_kingdom"),
        (str_store_string, s0, "@The {s48} are ruled by {s49}^^Your relation with them: {reg33}^", 0),

        (store_sub, ":string", ":faction_no", minor_kingdoms_begin),
        (val_add, ":string", "str_minor_faction_description_garamantes"),
        (str_store_string, s48, ":string"),
        (str_store_string, s0, "@{s0}^{s48}"),
        (set_trigger_result, 1),
    (else_try),
        (this_or_next|eq, ":note_index", 0),
        (eq, ":note_index", 1),
        (str_clear, s0),
        (set_trigger_result, 1),
    (try_end),
]),

#script_game_get_quest_note
# This script is called from the game engine when the notes of a quest is needed.
# INPUT: arg1 = quest_no, arg2 = note_index
# OUTPUT: s0 = note
("game_get_quest_note",[
    (store_script_param, ":quest", 1),
    (store_script_param, ":note_index", 2),
    (try_begin),
        (eq, ":note_index", 5),
        (try_begin),
            (eq, ":quest", "qst_blank_quest_23"),
            (str_store_string, s0, "@Your realm (not allies or tributaries) must hold the following settlements:^"),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (this_or_next|eq, ":walled_center", "p_town_27"),
                (this_or_next|eq, ":walled_center", "p_town_40"),
                (this_or_next|eq, ":walled_center", "p_town_47"),
                (this_or_next|eq, ":walled_center", "p_castle_55"),
                (this_or_next|eq, ":walled_center", "p_castle_40"),
                (this_or_next|eq, ":walled_center", "p_castle_42"),
                (eq, ":walled_center", "p_castle_30"),
                (str_store_party_name_link, s1, ":walled_center"),
                (store_faction_of_party, ":faction", ":walled_center"),
                (str_store_faction_name_link, s2, ":faction"),
                (str_store_string, s0, "@{s0}^{s1} currently owned by {s2}."),
            (try_end),
            (set_trigger_result, 1),
        (else_try),
            (eq, ":quest", "qst_blank_quest_22"),
            (str_store_string, s0, "@Your realm (not allies or tributaries) must hold the following settlements:^"),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (this_or_next|eq, ":walled_center", "p_town_45"),
                (this_or_next|eq, ":walled_center", "p_town_15"),
                (this_or_next|eq, ":walled_center", "p_castle_8"),
                (this_or_next|eq, ":walled_center", "p_castle_49"),
                (this_or_next|eq, ":walled_center", "p_castle_50"),
                (this_or_next|eq, ":walled_center", "p_castle_53"),
                (eq, ":walled_center", "p_castle_33"),
                (str_store_party_name_link, s1, ":walled_center"),
                (store_faction_of_party, ":faction", ":walled_center"),
                (str_store_faction_name_link, s2, ":faction"),
                (str_store_string, s0, "@{s0}^{s1} currently owned by {s2}."),
            (try_end),
            (set_trigger_result, 1),
        (else_try),
            (eq, ":quest", "qst_blank_quest_24"),
            (str_store_string, s0, "@Your realm (not allies or tributaries) must hold the following settlements:^"),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (this_or_next|eq, ":walled_center", "p_town_11"),
                (this_or_next|eq, ":walled_center", "p_town_42"),
                (this_or_next|eq, ":walled_center", "p_town_9"),
                (this_or_next|eq, ":walled_center", "p_castle_19"),
                (eq, ":walled_center", "p_castle_37"),
                (str_store_party_name_link, s1, ":walled_center"),
                (store_faction_of_party, ":faction", ":walled_center"),
                (str_store_faction_name_link, s2, ":faction"),
                (str_store_string, s0, "@{s0}^{s1} currently owned by {s2}."),
            (try_end),
            (set_trigger_result, 1),
        (else_try),
            (eq, ":quest", "qst_blank_quest_25"),
            (str_store_string, s0, "@Your realm (not allies or tributaries) must hold the following settlements:^"),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (this_or_next|eq, ":walled_center", "p_town_43"),
                (this_or_next|eq, ":walled_center", "p_town_1"),
                (this_or_next|eq, ":walled_center", "p_town_44"),
                (this_or_next|eq, ":walled_center", "p_castle_14"),
                (this_or_next|eq, ":walled_center", "p_castle_23"),
                (eq, ":walled_center", "p_castle_5"),
                (str_store_party_name_link, s1, ":walled_center"),
                (store_faction_of_party, ":faction", ":walled_center"),
                (str_store_faction_name_link, s2, ":faction"),
                (str_store_string, s0, "@{s0}^{s1} currently owned by {s2}."),
            (try_end),
            (set_trigger_result, 1),
        (try_end),
    (else_try),
        (set_trigger_result, 0),
    (try_end),
]),

#script_game_get_info_page_note
# This script is called from the game engine when the notes of a info_page is needed.
# INPUT: arg1 = info_page_no, arg2 = note_index
# OUTPUT: s0 = note
("game_get_info_page_note",[
    (store_script_param_1, ":info_page_no"),
    (store_script_param_2, ":note_index"),

    #(display_message, "@game_get_info_page_note triggered"),
    #list of companions and their locations
    (try_begin),
        (eq, ":note_index", 0),
        (eq, ":info_page_no", "ip_overview"),
        (str_clear, s9),
        (try_for_range, ":info_page", ip_dplmc_autoloot, ip_dplmc_disguise + 1),
            (str_store_info_page_name_link, s10, ":info_page"),
            (str_store_string, s9, "@     *) {s10}^{s9}"),
        (try_end),

        (str_store_string, s0,
            "@Aut Caesar Aut Nihil is a total overhaul, changing nearly every aspect of basic warband game play."
            +"^^The mod uses also a modified version of Diplomacy "+DPLMC_DIPLOMACY_VERSION_STRING+"."
            +"^^Additional information about the diplomacy features can be found at:"
            +"^^{s9}"
        ),

        (str_store_info_page_name_link, s10, "ip_hoty_keys"),
        (str_store_string, s0, "@{s0}^^A list of all usefull hot-keys (for battles and menus) can be found at {s10}."),

        (str_store_info_page_name_link, s10, "ip_companions"),
        (str_store_string, s0, "@{s0}^^A list of all companions and their locations can be found at {s10}."),

        (str_store_info_page_name_link, s10, "ip_provinces"),
        (str_store_string, s0, "@{s0}^^A list of all provinces, their settlements and their abbreviations can be found at {s10}."),

        (str_store_info_page_name_link, s10, "ip_provinces_abbreviations"),
        (str_store_string, s0, "@{s0}^^At game start you can select an option to include province names or abbreviations in the name of a settlement. You can find a list of all abbreviations at {s10}."),

        (str_clear, s9),
        (try_for_range, ":info_page", ip_q_and_q, ip_crafting_orders + 1),
            (str_store_info_page_name_link, s10, ":info_page"),
            (str_store_string, s9, "@     *) {s10}^{s9}"),
        (try_end),
        (str_store_string, s0,
            "@{s0}"
            +"^^^Other mod features of interest:"
            +"^^{s9}"
        ),

        (set_trigger_result, 1),
    (else_try),
        (eq, ":note_index", 0),
        (eq, ":info_page_no", "ip_provinces"),
        (str_store_string, s0,
            "@Every town, fortress and village is part of a province. The respective province can be seen under the center notes."
            +" A full list of all provinces and their respective settlements is provided here."
            +" ^^List of provinces:"
        ),
        (try_for_range, ":province", p_hisp_tarraco, p_provinces_end),
            (assign, ":count", 0),
            (str_store_string, s9, "str_none"),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (party_slot_eq, ":walled_center", slot_center_province, ":province"),
                (str_store_party_name_link, s10, ":walled_center"),
                (str_store_string, s9, "@{s10}, {s9}"),
                (try_begin),
                    (ge, ":count", 2),
                    (str_store_string, s9, "@{s10}, {s9}"),
                (else_try),
                    (eq, ":count", 1),
                    (str_store_string, s9, "@{s10} and {s9}"),
                (else_try),
                    (str_store_string, s9, "@{s10}"),
                (try_end),
                (val_add, ":count", 1),
            (try_end),
            (store_add, ":province_string", ":province", "str_province_begin"),
            (str_store_string, s10, ":province_string"),
            (str_store_string, s0, "@{s0}^*)  {s10}^     Consists of: {s9}."),
        (try_end),

        (set_trigger_result, 1),
    (else_try),
        (eq, ":note_index", 0),
        (eq, ":info_page_no", "ip_aor"),
        (str_store_string, s0, "@Military units you can currently hire and their recruitment locations:^"),

        (try_for_range, ":cohort", "pt_mercenary_guard", "pt_germans"),
            (assign, ":num_recruitable_cohorts", 0),
            (str_clear, s2),
            (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                (call_script, "script_cf_can_hire_cohort", ":cohort", ":walled_center"),
                (str_store_party_name_link, s1, ":walled_center"),
                (try_begin),
                    (ge, ":num_recruitable_cohorts", 1),
                    (str_store_string, s2, "@{s2}, {s1}"),
                (else_try),
                    (str_store_string, s2, "@{s1}"),
                (try_end),
                (val_add, ":num_recruitable_cohorts", 1),
            (try_end),
            (try_for_range, ":walled_center", minor_towns_begin, minor_towns_end),
                (call_script, "script_cf_can_hire_cohort", ":cohort", ":walled_center"),
                (str_store_party_name_link, s1, ":walled_center"),
                (try_begin),
                    (ge, ":num_recruitable_cohorts", 1),
                    (str_store_string, s2, "@{s2}, {s1}"),
                (else_try),
                    (str_store_string, s2, "@{s1}"),
                (try_end),
                (val_add, ":num_recruitable_cohorts", 1),
            (try_end),
            (ge, ":num_recruitable_cohorts", 1),
            (call_script, "script_get_cohort_name_to_s5", ":cohort"),
            (str_store_string, s0, "@{s0}^{s5}: {s2}"),
        (try_end),
        (set_trigger_result, 1),
    (else_try),
        (eq, ":note_index", 0),
        (eq, ":info_page_no", "ip_companions"),
        (str_store_string, s0, "@List of companions and their locations:^"),
        (try_for_range, ":companions", companions_begin, companions_end),
            (str_store_troop_name_link, s1, ":companions"),
            (try_begin),
                (main_party_has_troop, ":companions"),
                (str_store_string, s4, "@In your party."),
            (else_try),
                (troop_slot_eq, ":companions", slot_troop_occupation, slto_kingdom_hero),
                (str_store_string, s4, "@Currenlty roaming around the world."),
            (else_try),
                (troop_slot_eq, ":companions", slot_troop_occupation, dplmc_slto_dead),
                (str_store_string, s4, "@Is most likely dead."),
            (else_try),
                (assign, ":break_1", castles_end),
                (assign, ":break_2", location_barracks),
                (try_for_range, ":center_no", towns_begin, ":break_1"),
                    (try_for_range, ":location", location_tavern, ":break_2"),
                        (call_script, "script_spawn_companion", ":center_no", ":location"),
                        (eq, reg0, ":companions"),
                        (assign, ":break_1", -1),
                        (assign, ":break_2", -1),
                    (try_end),
                (try_end),
                (eq, ":break_1", -1),
                (eq, ":break_2", -1),
                (val_add, ":location", "str_location_tavern"),
                (str_store_string, s3, ":location"),
                (str_store_party_name_link, s2, ":center_no"),
                (str_store_string, s4, "@Likely in {s2} ({s3})."),
            (else_try),
                (eq, ":companions", "trp_npc35"),
                (str_store_string, s4, "@Joins together with Ligia."),
            (else_try),
                (str_store_string, s4, "@Joins during quest."),
            (try_end),
            (str_store_string, s0, "@{s0}^{s1}: {s4}"),
        (try_end),
        (set_trigger_result, 1),
    (try_end),
]),

#script_game_get_scene_name
# This script is called from the game engine when a name for the scene is needed.
# INPUT: arg1 = scene_no
# OUTPUT: s0 = name
("game_get_scene_name",[]),

#script_game_get_mission_template_name
# This script is called from the game engine when a name for the mission template is needed.
# INPUT: arg1 = mission_template_no
# OUTPUT: s0 = name
("game_get_mission_template_name",[]),

#script_game_receive_url_response
#response format should be like this:
#  [a number or a string]|[another number or a string]|[yet another number or a string] ...
# here is an example response:
# 12|Player|100|another string|142|323542|34454|yet another string
# INPUT: arg1 = num_integers, arg2 = num_strings
# reg0, reg1, reg2, ... up to 128 registers contain the integer values
# s0, s1, s2, ... up to 128 strings contain the string values
("game_receive_url_response",[]),

("game_get_cheat_mode",[
    (assign, reg0, "$cheat_mode"),
]),

#script_game_receive_network_message
# This script is called from the game engine when a new network message is received.
# INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
("game_receive_network_message",[]),

("game_get_multiplayer_server_option_for_mission_template",[]),

# script_game_multiplayer_server_option_for_mission_template_to_string
# Input: arg1 = mission_template_id, arg2 = option_index, arg3 = option_value
# Output: s0 = option_text
("game_multiplayer_server_option_for_mission_template_to_string",[]),
# script_game_multiplayer_event_duel_offered
# Input: arg1 = agent_no
# Output: none
("game_multiplayer_event_duel_offered",[]),
# script_game_get_multiplayer_game_type_enum
# Input: none
# Output: reg0:first type, reg1:type count
("game_get_multiplayer_game_type_enum",[]),

# script_game_multiplayer_get_game_type_mission_template
# Input: arg1 = game_type
# Output: mission_template
("game_multiplayer_get_game_type_mission_template",[]),

#script_game_get_party_prisoner_limit:
# This script is called from the game engine when the prisoner limit is needed for a party.
# INPUT: arg1 = party_no
# OUTPUT: reg0 = prisoner_limit
("game_get_party_prisoner_limit",[
    (store_script_param_1, ":party_id"),
    (assign, ":troop_no", "trp_player"),
    (try_begin),
        (eq, ":party_id", "p_main_party"),
        (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),
        (store_div, ":limit", ":player_party_size", 4),
        (assign, ":limit", 0),
        (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
        (val_mul, ":skill", 9),
        (val_add, ":limit", ":skill"),
        (val_max, ":limit", 5),
        ###ich weis nciht was das soll?
        (try_begin), #SB : override with diplomacy_var2
            (eq, "$diplomacy_var", DPLMC_CURRENT_VERSION_CODE),
            (assign, ":limit", "$diplomacy_var2"),
        (try_end),
      ####################
        (try_begin),
            (ge, "$cheat_mode", 1),
            (val_add, ":limit", 2000),
        (try_end),
        (try_begin),
            (lt, "$player_honor", -90),
            (val_mul, ":limit", 21),
            (val_div, ":limit", 10),
        (else_try),
            (lt, "$player_honor", -70),
            (val_mul, ":limit", 19),
            (val_div, ":limit", 10),
        (else_try),
            (lt, "$player_honor", -40),
            (val_mul, ":limit", 17),
            (val_div, ":limit", 10),
        (else_try),
            (lt, "$player_honor", -20),
            (val_mul, ":limit", 14),
            (val_div, ":limit", 10),
        (try_end),
    (else_try),
        (party_is_active, ":party_id"),
        (neq, ":party_id", "p_main_party"),
        (try_begin),
            (this_or_next|party_slot_eq, ":party_id", slot_party_type, spt_player_camp),
            (party_slot_eq, ":party_id", slot_party_type, spt_companion_raider),

            # keep a percentage of player stats
            (val_mul, ":limit", pcamp_player_prisoner_count_percentage),
            (val_div, ":limit", 100),

            # recompute prisoner limit from commander skills and troop count
            (party_get_slot, ":troop_no", ":party_id", slot_pcamp_camp_commander),
            (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
            (val_mul, ":skill", pcamp_commander_prisoner_skill_bonus),
            (val_add, ":limit", ":skill"),
            (store_party_size_wo_prisoners, ":troops", ":party_id"),
            (val_div, ":troops", pcamp_troop_count_prisoner_divisor),
            (val_add, ":limit", ":troops"),
        (else_try),
            (party_slot_eq, ":party_id", slot_party_type, spt_latifundium),
            (assign, ":limit", 110),
            (try_begin),
                (party_slot_ge, ":party_id", slot_lat_barracks, 1),
                (val_add, ":limit", 100),
            (try_end),
        (try_end),
    (try_end),

    (assign, reg0, ":limit"),
    (set_trigger_result, reg0),
]),

#script_game_get_item_extra_text:
# This script is called from the game engine when an item's properties are displayed.
# INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
# OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
("game_get_item_extra_text",[
    (store_script_param, ":item_no", 1),
    (store_script_param, ":extra_text_id", 2),
    (store_script_param, ":item_modifier", 3),

    (try_begin),
        (is_between, ":item_no", "itm_raw_date_fruit", food_end),
        (neq, ":item_no", "itm_furs"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (assign, ":continue", 1),
            (try_begin),
                (this_or_next|eq, ":item_no", "itm_cattle_meat"),
                (this_or_next|eq, ":item_no", "itm_pork"),
                (eq, ":item_no", "itm_chicken"),

                (eq, ":item_modifier", imod_rotten),
                (assign, ":continue", 0),
            (try_end),
            (eq, ":continue", 1),
            (item_get_slot, ":food_bonus", ":item_no", slot_item_food_bonus),
            (assign, reg1, ":food_bonus"),
            (set_result_string, "@+{reg1} to party morale"),
            (set_trigger_result, 0x4444FF),
        (else_try),
            (eq, ":extra_text_id", 1),
            (assign, ":quest_no", -1), #no quest selected
            (try_begin),
                (check_quest_active, "qst_deliver_wine"),
                (quest_slot_eq, "qst_deliver_wine", slot_quest_target_item, ":item_no"),
                (assign, ":quest_no", "qst_deliver_wine"),
                (quest_get_slot, ":quest_target_center", ":quest_no", slot_quest_target_center),
            (try_end),

            (try_begin), #prioritize town missions
                (eq, ":quest_no", -1),
                (check_quest_active, "qst_deliver_grain"),
                (quest_slot_eq, "qst_deliver_grain", slot_quest_target_item, ":item_no"),
                (assign, ":quest_no", "qst_deliver_grain"),
                (quest_get_slot, ":quest_target_center", ":quest_no", slot_quest_giver_center),
            (try_end),
            (neq, ":item_modifier", imod_rotten),
            (neq, ":quest_no", -1),
            (quest_get_slot, reg5, ":quest_no", slot_quest_target_amount),
            #probably do a x/n items counter here or something
            (str_store_party_name, s5, ":quest_target_center"),
            (set_result_string, "@Deliver {reg5} units to {s5}"),
            (set_trigger_result, message_alert),
        (try_end),
    (else_try),
        #anadido chief para estandartes
        (eq, ":item_no", "itm_poisoned_arrows"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@This arrows are poisoned and will do additional damage."),
            (set_trigger_result, 0x4444FF),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_crown_shah"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The crown of the king of Persia. A sign of authority and leadership.^Improves leadership and persuasion skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (this_or_next|eq, ":item_no", "itm_laurel_gold"),
        (eq, ":item_no", "itm_laurel_silver"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Improves leadership and persuasion skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_perfume_special"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Famous and exquisite perfume. A perfect present for a lady."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (this_or_next|eq, ":item_no", "itm_horn"),
        (this_or_next|eq, ":item_no", "itm_trumpet_eastern"),
        (eq, ":item_no", "itm_trumpet_celtic"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Increases morale during battle."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_hercules_club"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@'They sing of him first of all heroes' - Club of Donar, the great thunderer.^Decorated with ornaments and made out of gold. Thus it is very heavy.^Having it in inventory Improves power strike skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_pharaoh_crown"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The double crown of Egypt.^^Improves leadership and persuasion skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_celtic_carnyx"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A Carnyx made purely of gold.^Improves tactics skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_dacian_treasure"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Over the centuries the Getae kings collected this treasure. It is a sign of wealth.^Improves trade skill."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_holy_grail"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A fish and the name Chrestos are engraved on the cup."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_allat"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Statue of Al-Lat, goddess of fertility.^It is said that a woman who touches the statue will become more fertile, but also more gluttonous.^Increases party morale if you are not worshipping Christus or YHWH."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_mithras"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Statue of Mithras.^Increases party morale if you are not worshipping Christus or YHWH."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_book_poop"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string,
            "@Art of poop, by Poopienus, is a humorous collection of jokes and witty observations,^"
            +" all centered around the universal yet comical theme of toilet humor. Playfully irreverent,^"
            +" this lighthearted book turns everyday toilet experiences into laugh-out-loud moments."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_mirror_poppaea"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A Mirror richly decorated with gold and gemstones with a picture of Poppaea Sabina on the back side."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_menorah"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Great golden menorah from the temple in Hierosolyma.^Increases party morale if you worship YHWH."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_scythian_bong"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A golden bong.^Increases party morale."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_arminius_spatha"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Spatha of Arminius. The handle is made out of wood and ivory. It is decorated with bronze and gold."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_african_longbow"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Bow of African gods."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_danish_longsword"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Germanic sword from the Heruli tribe, decorated with bronze and silver."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_danish_longsword_2"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@This sword is decorated with bronze, ivory and silver. It has been gifted to you by Freya."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_ancient_spatha"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Lavishly decorated spatha. It once belonged to Augustus, the first Princeps."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_augustus_armor"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Lorica musculata of Augustus, first Princeps."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_arminius_mask"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Galea with golden mask. The mask is made from the gold of the murdered Roman soldiers in Teuteburg.^The gold makes the helm very heavy."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_anti_fooling_paint"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Increases party speed on water."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_didos_underwear"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Whisper-thin silk said to have belonged to the fabled Queen of Carthage, radiating an air of timeless allure.^Troops love to sniff at it, thus increases party moral."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_xylospongium"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A sea sponge fixed on a stick. Can be used for anything. Be creative."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_aegis"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Forged by Hephaestus, legendary shield of Zeus."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_lyre_rich"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Nero's golden Lyre! Equip it and press 'O' to play on it."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_caesars_sword"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Legendary gladius of Julius Caesar."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_felt_steppe_cap"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@A souvenir from Mamertinus' party."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_pilos_ultimate"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The legendary pilos helmet. It is said that the owner of the helm is the leader of the PILOS religion."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no", "itm_laurel_wreath"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The prize for winning the Olympic games."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (is_between, ":item_no", "itm_ancient_helm_light", "itm_anti_fooling_paint"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Forged by Vulcanus, thousands of years ago."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_holy_lance"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Longinus pierced Christ's side with this lance."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_aslans_fur"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Fur of the mighty lion Aslan."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_cupid_arrow"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@Someone stung will fall in love with the first person they see."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_alexanders_helm"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The helm of Megas Alexandros. (+1 to leadership)"),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_linothorax_alexander"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The armor of Megas Alexandros. (+1 to leadership)"),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (eq, ":item_no",  "itm_gallic_spear_4"),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (set_result_string, "@The magical silver spear of Olyndicus, sent by the gods from the sky."),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (is_between, ":item_no", readable_books_begin, readable_books_end),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (item_get_slot, reg1, ":item_no", slot_item_intelligence_requirement),
            (set_result_string, "@Requires {reg1} intelligence to read"),
            (set_trigger_result, 0xFFEEDD),
        (else_try),
            (eq, ":extra_text_id", 1),
            (item_get_slot, ":progress", ":item_no", slot_item_book_reading_progress),
            (val_div, ":progress", 10),
            (assign, reg1, ":progress"),
            (set_result_string, "@Reading Progress: {reg1}%"),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
        (is_between, ":item_no", reference_books_begin, reference_books_end),
        (try_begin),
            (eq, ":extra_text_id", 0),
            (try_begin),
                (eq, ":item_no", "itm_book_wound_treatment_reference"),
                (str_store_string, s1, "@wound treament"),
            (else_try),
                (eq, ":item_no", "itm_book_training_reference"),
                (str_store_string, s1, "@trainer"),
            (else_try),
                (eq, ":item_no", "itm_book_surgery_reference"),
                (str_store_string, s1, "@surgery"),
            (else_try),
                (eq, ":item_no", "itm_book_first_aid"),
                (str_store_string, s1, "@first aid"),
            (else_try),
                (eq, ":item_no", "itm_book_pathfinding"),
                (str_store_string, s1, "@pathfinding"),
            (try_end),
            (set_result_string, "@+1 to {s1} while in inventory"),
            (set_trigger_result, 0xFFEEDD),
        (try_end),
    (else_try),
      # sb : debug
        (try_begin),
            (ge, "$cheat_mode", 1),
            (eq, ":extra_text_id", 4),
            (call_script, "script_dplmc_get_item_value_with_imod", ":item_no", ":item_modifier"),
            (assign, ":value", reg0),
            (call_script, "script_dplmc_get_item_score_with_imod", ":item_no", ":item_modifier"),
            (store_div, reg1, ":value", 100),
            (set_result_string, "@item score:{reg0}, value:{reg1}"),
            (set_trigger_result, 0x0DDEEE),
        (try_end),
        (try_begin), #SB : display this block when in item pool mode
            (eq, ":extra_text_id", 2),
            (eq, "$pool_troop", "trp_temp_troop"), #new exit code resets condition
            (this_or_next|eq, "$lord_selected", "trp_player"),
            (is_between, "$lord_selected", companions_begin, companions_end),
            (call_script, "script_item_get_type_aux", ":item_no"),
            (assign, ":meta_type", reg0),
            (gt, ":meta_type", meta_itp_mask), #has a valid meta-type
            (assign, ":string", "str_empty_string"),
            (try_begin), #doesn't need it, Native item type already shows
                # (eq, ":meta_type", dplmc_itp_morningstar),
                # (assign, ":string", "str_dplmc_hero_wpn_slot_two_handed_one_handed"),
            # (else_try),
                (eq, ":meta_type", dplmc_itp_lance),
                (assign, ":string", "str_dplmc_hero_wpn_slot_lance"),
            (else_try),
                (eq, ":meta_type", dplmc_itp_pike),
                (assign, ":string", "str_dplmc_hero_wpn_slot_pikes"),
            (else_try),
                (eq, ":meta_type", dplmc_itp_halberd),
                (assign, ":string", "str_dplmc_hero_wpn_slot_halberd"),
            (try_end),
            (gt, ":string", "str_empty_string"), #could use directly
            (set_result_string, ":string"),
            (set_trigger_result, 0xDDEEFF),
        (try_end),
    (try_end),
]),

#script_game_on_disembark:
# This script is called from the game engine when the player reaches the shore with a ship.
# INPUT: pos0 = disembark position
# OUTPUT: none
("game_on_disembark",[
   #(jump_to_menu, "mnu_disembark"),
]),

#script_game_context_menu_get_buttons:
# This script is called from the game engine when the player clicks the right mouse button over a party on the map.
# INPUT: arg1 = party_no
# OUTPUT: none, fills the menu buttons
("game_context_menu_get_buttons",[
    (store_script_param, ":party_no", 1),
    (try_begin),
        (eq, ":party_no", "p_main_party"),
        (store_add, ":string", "str_party_stance_default", "$g_stance"),
        (str_store_string, s0, ":string"),
        (context_menu_add_item, "@Change party stance (currently {s0})", cmenu_party_stance),
    (try_end),
    (try_begin),
        (eq, ":party_no", "p_main_party"),
        (store_party_size_wo_prisoners, ":size", "p_follower_party"),
        (gt, ":size", 0),
        (context_menu_add_item, "@Manage follower party", cmenu_follower_party),
    (try_end),
    (try_begin),
        (neq, ":party_no", "p_main_party"),
        (context_menu_add_item, "@Move here", cmenu_move),
    (try_end),
    (try_begin),
        (is_between, ":party_no", centers_begin, centers_end),
        (context_menu_add_item, "@View notes", cmenu_notes),
    (else_try),
        (is_between, ":party_no", minor_towns_begin, minor_towns_end),
        (context_menu_add_item, "@View notes", cmenu_notes),
    (else_try),
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (gt, ":num_stacks", 0),
        (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
        ##diplomacy start+ support for promoted kingdom ladies
        # (is_between, ":troop_no", heroes_begin, heroes_end),
        # (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        ##diplomacy end+
        (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
        (context_menu_add_item, "@View notes", cmenu_notes), #move this to same slot
    (try_end),
    (try_begin),
        (neq, ":party_no", "p_main_party"),
        (store_faction_of_party, ":party_faction", ":party_no"),

        (this_or_next|eq, ":party_faction", "$players_kingdom"),
        (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
        (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),

        (neg|is_between, ":party_no", centers_begin, centers_end),

        (context_menu_add_item, "@Accompany", cmenu_follow),
    (try_end),
    #phaiak begin
    (try_begin),
        (eq, ":party_no", "p_main_party"),
        (party_slot_eq, "p_main_party", slot_party_on_water, 1),
        # (set_fixed_point_multiplier, 1000),
        (map_get_land_position_around_position, pos2, pos1, 1),
        (party_set_position, "p_temp_party", pos2),
        (party_get_current_terrain, ":terrain_type", "p_temp_party"),
        (neq, ":terrain_type", 0),
        (neq, ":terrain_type", 1), #cliffs
        (neq, ":terrain_type", 7),
        (neq, ":terrain_type", 8),
        (context_menu_add_item, "@Find landing point", cmenu_landing_point),
    (try_end),
    #SB : debug cheats
    (try_begin),
        (troop_slot_eq, "trp_global_variables", g_is_dev, 1),
        (ge, "$cheat_mode", 1),
        (try_begin),
            (neq, ":party_no", "p_main_party"),
            (context_menu_add_item, "@Attach", cmenu_attach),
            # (context_menu_add_item, "@Reinforce", cmenu_reinforce),
            (context_menu_add_item, "@Inspect", cmenu_encounter),
            # (context_menu_add_item, "@Exchange", cmenu_exchange),
        (try_end),
        (try_begin),
            (party_get_num_attached_parties, ":num_attached", ":party_no"),
            (gt, ":num_attached", 0),
            (try_begin),
                (eq, ":party_no", "p_main_party"),
                (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
                (str_store_party_name, s1, ":attached_party"),
                (set_fixed_point_multiplier, 1000),
                (party_get_position, pos1, ":party_no"),
                (position_get_x, reg1, pos1),
                (position_get_y, reg2, pos1),
                (context_menu_add_item, "@Detach {s1} at {reg1},{reg2}", cmenu_attach),
            (try_end),
            (context_menu_add_item, "@Detach All", cmenu_detach),
        (try_end),
        (try_begin),
            (party_get_battle_opponent, ":other_party", ":party_no"),
            (party_is_active, ":other_party"),
            (context_menu_add_item, "@Win Battle", cmenu_winbattle),
            (context_menu_add_item, "@Lose Battle", cmenu_losebattle),
        # (else_try),
            # (context_menu_add_item, "@Wound All", cmenu_wound),
            # (context_menu_add_item, "@Heal All", cmenu_heal),
        (try_end),
        # (try_begin),
          # (is_between, ":party_no", centers_begin, centers_end),
          # (context_menu_add_item, "@Spawn Bandits", cmenu_spawnbandit),
        # (try_end),
    (try_end),
]),

#script_game_event_context_menu_button_clicked:
# This script is called from the game engine when the player clicks on a button at the right mouse menu.
# INPUT: arg1 = party_no, arg2 = button_value
# OUTPUT: none
("game_event_context_menu_button_clicked",[
    (store_script_param, ":party_no", 1),
    (store_script_param, ":button_value", 2),
    (try_begin),
        (eq, ":button_value", cmenu_follower_party),
        (assign, "$temp", 1),
        (jump_to_menu, "mnu_follower_party"),
    (else_try),
        (eq, ":button_value", cmenu_notes),
        #SB : unify this under a single constant
        (try_begin),
            (is_between, ":party_no", centers_begin, centers_end),
            (change_screen_notes, 3, ":party_no"),
        (else_try),
            (is_between, ":party_no", minor_towns_begin, minor_towns_end),
            (change_screen_notes, 3, ":party_no"),
        (else_try),
            (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
            (change_screen_notes, 1, ":troop_no"),
        (try_end),
    (else_try), #SB : lots of cheats
        (eq, ":button_value", cmenu_attach),
        (try_begin),
            (neq, ":party_no", "p_main_party"),
            (party_set_next_battle_simulation_time, ":party_no", -1),
            (party_leave_cur_battle, ":party_no"),
            (party_set_flags, ":party_no", pf_is_static, 0),
            (party_attach_to_party, ":party_no", "p_main_party"),
        (else_try),
            (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
            (party_get_position, pos1, "p_main_party"),
            (party_detach, ":attached_party"),
            (party_set_position, ":attached_party", pos1),
            (try_begin),
                (is_between, ":attached_party", centers_begin, centers_end),
                (party_set_flags, ":attached_party", pf_is_static, 1),
            (try_end),
        (try_end),
    (else_try),
        (eq, ":button_value", cmenu_detach),
        (party_get_num_attached_parties, ":num_stacks", ":party_no"),
        (try_for_range_backwards, ":stacks", 0, ":num_stacks"),
            (party_get_attached_party_with_rank, ":attached_party", ":party_no", ":stacks"),
            (party_detach, ":attached_party"),
            (party_set_ai_behavior, ":attached_party", ai_bhvr_hold),
            (party_set_flags, ":attached_party", pf_default_behavior, 1),
            (party_relocate_near_party, ":attached_party", ":party_no", 2),
            (try_begin),
                (is_between, ":attached_party", centers_begin, centers_end),
                (party_set_flags, ":attached_party", pf_is_static, 1),
            (try_end),
        (try_end),
    (else_try),
        (eq, ":button_value", cmenu_encounter),
        (assign, "$new_encounter", 2), #this lets us branch to a different menu
        (start_encounter, ":party_no"),
    (else_try), #too lazy to invoke magical commands, screw around with composition
        (eq, ":button_value", cmenu_losebattle),
        (call_script, "script_party_wound_all_members", ":party_no"),
        (party_set_next_battle_simulation_time, ":party_no", -1),
    (else_try), #winning is half the battle
        (eq, ":button_value", cmenu_winbattle),
        (party_get_battle_opponent, ":other_party", ":party_no"),
        (call_script, "script_party_wound_all_members", ":other_party"),
        (party_set_next_battle_simulation_time, ":party_no", 0),
    (else_try),
        (eq, ":button_value", cmenu_landing_point),
        (try_begin),
            (party_get_position, pos1, "p_temp_party"),
            (call_script, "script_get_next_water_position", 0, "p_temp_party"),
            (party_set_position, "p_landing_point", pos2),
        (try_end),
    (else_try),
        (eq, ":button_value", cmenu_party_stance),
        (val_add, "$g_stance", 1),
        (try_begin),
          (ge, "$g_stance", 3),
          (assign, "$g_stance", 0),
        (try_end),
        (call_script, "script_game_get_party_speed_multiplier", "p_main_party"),
        (store_add, ":string", "str_party_stance_default", "$g_stance"),
        (str_store_string, s0, ":string"),
        (display_message, "@Party stance changed to {s0}"),
    (try_end),
]),

#script_game_get_skill_modifier_for_troop
# This script is called from the game engine when a skill's modifiers are needed
# INPUT: arg1 = troop_no, arg2 = skill_no
# OUTPUT: trigger_result = modifier_value
("game_get_skill_modifier_for_troop",[
    (store_script_param, ":troop_no", 1),
    (store_script_param, ":skill_no", 2),
    (assign, ":modifier_value", 0),
    (troop_get_inventory_slot,":cur_armor",":troop_no",ek_body),
    (troop_get_inventory_slot,":cur_helmet",":troop_no",ek_head),

    #VC-2404 (Use second outfit in second outfit situations)
    (try_begin),
        (eq, ":troop_no", "trp_player"),
        (is_between, "$g_encountered_party",  centers_begin, centers_end),
        (party_get_battle_opponent,":opponent","p_main_party"),
        (lt, ":opponent", 0), #party is not itself involved in a battle
        (call_script, "script_cf_player_use_second_outfit"),
        (troop_get_inventory_slot, ":cur_armor", "trp_pseudo_troop_end", ek_body),
        (troop_get_inventory_slot, ":cur_helmet", "trp_pseudo_troop_end", ek_head),
    (try_end),

    (try_begin),
       (this_or_next|eq, ":cur_helmet", "itm_crown_shah"),
       (this_or_next|eq, ":cur_helmet", "itm_laurel_gold"),
       (this_or_next|eq, ":cur_helmet", "itm_pharaoh_crown"),
       (eq, ":cur_helmet", "itm_laurel_silver"),
       (this_or_next|eq, ":skill_no", "skl_leadership"),
       (eq, ":skill_no", "skl_persuasion"),
       (val_add, ":modifier_value", 1),
    (try_end),

    (try_begin),
        (eq, ":skill_no", "skl_power_strike"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_hercules_club"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (try_end),
    (try_begin),
        (eq, ":skill_no", "skl_tactics"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_celtic_carnyx"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (try_end),
    (try_begin),
        (eq, ":skill_no", "skl_trade"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_dacian_treasure"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (try_end),
    (try_begin),
        (eq, ":skill_no", "skl_leadership"),
        (eq, ":cur_helmet", "itm_alexanders_helm"),
        (val_add, ":modifier_value", 1),
    (try_end),
    (try_begin),
        (eq, ":skill_no", "skl_leadership"),
        (eq, ":cur_helmet", "itm_aslans_fur"),
        (val_add, ":modifier_value", 1),
    (try_end),
    (try_begin),
        (eq, ":skill_no", "skl_leadership"),
        (eq, ":cur_armor", "itm_linothorax_alexander"),
        (val_add, ":modifier_value", 1),
    (try_end),

    (try_begin),
        (eq, ":skill_no", "skl_wound_treatment"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_wound_treatment_reference"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (else_try),
        (eq, ":skill_no", "skl_first_aid"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_first_aid"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (else_try),
        (eq, ":skill_no", "skl_trainer"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_training_reference"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (else_try),
        (eq, ":skill_no", "skl_surgery"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_surgery_reference"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (else_try),
        (eq, ":skill_no", "skl_pathfinding"),
        (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_pathfinding"),
        (gt, reg0, 0),
        (val_add, ":modifier_value", 1),
    (try_end),

    (try_begin),
        (troop_is_hero, ":troop_no"),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
        (assign, ":party", -1),
        (try_begin),
            (main_party_has_troop, ":troop_no"),
            (assign, ":party", "p_main_party"),
        (else_try),
            (troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
            (ge, ":leaded_party", 1), #1 = troop leader yes
            (assign, ":party", ":leaded_party"),
        (try_end),

        (ge, ":party", 0),
        (party_is_active, ":party"),

        (try_begin),
            (eq, ":skill_no", "skl_tactics"),
            (eq, ":party", "p_main_party"),

            (store_party_size_wo_prisoners, ":size", "p_main_party"),
            (try_begin),
                (ge, ":size", 500),
                (assign, ":size_threshold", 10),
            (else_try),
                (ge, ":size", 400),
                (assign, ":size_threshold", 8),
            (else_try),
                (ge, ":size", 300),
                (assign, ":size_threshold", 6),
            (else_try),
                (ge, ":size", 200),
                (assign, ":size_threshold", 4),
            (else_try),
                (ge, ":size", 100),
                (assign, ":size_threshold", 2),
            (else_try),
                (assign, ":size_threshold", 0),
            (try_end),
            (assign, ":total_valor", 0),
            (party_get_num_companion_stacks, ":num_of_stacks", ":party"),##now p_follower_party

            (try_for_range, ":i", 0, ":num_of_stacks"),
                (party_stack_get_troop_id, ":stack_troop", ":party", ":i"),
                (call_script, "script_cf_is_low_officer", ":stack_troop"),

                (party_stack_get_size, ":stack_size", ":party", ":i"),
                (party_stack_get_num_wounded, ":stack_wounded", ":party", ":i"),
                (val_sub, ":stack_size", ":stack_wounded"),
                (val_add, ":total_valor", ":stack_size"),
            (try_end),
            (val_sub, ":total_valor", ":size_threshold"),
            (try_begin),
                (lt, ":total_valor", 0),
                (val_max, ":total_valor", -2),
                (val_add, ":modifier_value", ":total_valor"),
            (try_end),
          # (assign, reg1, ":modifier_value"),
          # (assign, reg2, ":total_valor"),
          # (assign, reg3, ":size_threshold"),
          # (display_message, "@modifier: {reg1}, total_valor: {reg2} threshold: {reg3}"),
        (else_try),
            (eq, ":skill_no", "skl_leadership"),
            (assign, ":total_valor", 0),
            (party_get_num_companion_stacks, ":num_of_stacks", ":party"),
            (try_for_range, ":i", 0, ":num_of_stacks"),
                (party_stack_get_troop_id, ":stack_troop", ":party", ":i"),
                (call_script, "script_cf_is_high_officer", ":stack_troop"),
                (party_stack_get_size, ":stack_size", ":party", ":i"),
                (party_stack_get_num_wounded, ":stack_wounded", ":party", ":i"),
                (val_sub, ":stack_size", ":stack_wounded"),
                (val_add, ":total_valor", ":stack_size"),
            (try_end),
            (try_begin),
                (ge, ":total_valor", 4),
                (val_add, ":modifier_value", 3),
            (else_try),
                (ge, ":total_valor", 3),
                (val_add, ":modifier_value", 2),
            (else_try),
                (ge, ":total_valor", 2),
                (val_add, ":modifier_value", 1),
            (try_end),
        (else_try),
            (eq, ":skill_no", "skl_surgery"),
            (eq, ":party", "p_main_party"),

            (assign, ":total_valor", 0),
            (party_get_num_companion_stacks, ":num_of_stacks", "p_follower_party"),##now p_follower_party

            (try_for_range, ":i", 0, ":num_of_stacks"),
                (party_stack_get_troop_id, ":stack_troop", "p_follower_party", ":i"),
                (eq, ":stack_troop", "trp_sword_sister"),

                (party_stack_get_size, ":stack_size", "p_follower_party", ":i"),
                (party_stack_get_num_wounded, ":stack_wounded", "p_follower_party", ":i"),
                (val_sub, ":stack_size", ":stack_wounded"),
                (val_add, ":total_valor", ":stack_size"),
            (try_end),
            (try_begin),
                (gt, ":total_valor", 29),
                (val_add, ":modifier_value", 3),
            (else_try),
                (gt, ":total_valor", 9),
                (val_add, ":modifier_value", 2),
            (else_try),
                (gt, ":total_valor", 0),
                (val_add, ":modifier_value", 1),
            (try_end),

        (else_try),
            (eq, ":skill_no", "skl_wound_treatment"),
            (eq, ":party", "p_main_party"),

            (assign, ":total_valor", 0),
            (party_get_num_companion_stacks, ":num_of_stacks", "p_follower_party"),##now p_follower_party

            (try_for_range, ":i", 0, ":num_of_stacks"),
                (party_stack_get_troop_id, ":stack_troop", "p_follower_party", ":i"),
                (is_between, ":stack_troop", "trp_follower_woman", "trp_caravan_master"),

                (party_stack_get_size, ":stack_size", "p_follower_party", ":i"),
                (party_stack_get_num_wounded, ":stack_wounded", "p_follower_party", ":i"),
                (val_sub, ":stack_size", ":stack_wounded"),
                (val_add, ":total_valor", ":stack_size"),
            (try_end),

            (try_begin),
                (gt, ":total_valor", 69),
                (val_add, ":modifier_value", 3),
            (else_try),
                (gt, ":total_valor", 39),
                (val_add, ":modifier_value", 2),
            (else_try),
                (gt, ":total_valor", 19),
                (val_add, ":modifier_value", 1),
            (try_end),
        (try_end),
    (try_end),
    (set_trigger_result, ":modifier_value"),
]),

#Enable script_game_check_party_sees_party to prevent compassionate lords from
#attacking villagers and merchant caravans.
#script_game_check_party_sees_party
# This script is called from the game engine when a party is inside the range of another party
# INPUT: arg1 = party_no_seer, arg2 = party_no_seen
# OUTPUT: trigger_result = true or false (1 = true, 0 = false)
("game_check_party_sees_party",[
	(store_script_param_1, ":party_no_seer"),
	(store_script_param_2, ":party_no_seen"),

	(assign, ":trigger_result", 1),
	(assign, ":save_reg0", reg0),

    #bandits wont attack a raiding player from now on
    (try_begin),
        (is_between, "$g_player_raiding_village", villages_begin, villages_end),
        (eq, ":party_no_seen", "p_main_party"),
        (neg|party_slot_eq, ":party_no_seer", slot_party_type, spt_kingdom_hero_party),
        (neg|party_slot_eq, ":party_no_seer", slot_party_type, spt_patrol),
        (assign, ":trigger_result",0),
    (try_end),

    (try_begin),
		#Only apply this when the "seer" is a kingdom hero party
		(party_slot_eq, ":party_no_seer", slot_party_type, spt_kingdom_hero_party),

		#Only needed if the seen party is of a hostile faction
		(call_script, "script_get_relation_between_parties", ":party_no_seer", ":party_no_seen"),
		(lt, reg0, 0),

		#Only apply this when the seen party is a merchant caravan or villagers
        (party_get_num_companion_stacks, ":num_stacks", ":party_no_seer"),
        (ge, ":num_stacks", 1),
        (party_stack_get_troop_id, ":leader", ":party_no_seer", 0),
        (ge, ":leader", 1),
        (troop_is_hero, ":leader"),
		(party_get_template_id, ":template", ":party_no_seen"),
        (try_begin),
            (this_or_next|party_slot_eq, ":party_no_seen", slot_party_type, spt_kingdom_caravan),
            (this_or_next|party_slot_eq,":party_no_seen", slot_party_type, dplmc_spt_gift_caravan),#custom diplomacy caravan
            (this_or_next|eq,":template", "pt_refugees"),
            (party_slot_eq, ":party_no_seen", slot_party_type, spt_village_farmer),
            #Never apply this when the seen party is engaging in hostile actions
            (party_get_battle_opponent, reg0, ":party_no_seen"),
            (lt, reg0, 0),
            #Only apply this when the leader is tmt_humanitarian, lrep_benefactor, or lrep_moralist
            #or if there is a campaign in progress

            (call_script, "script_dplmc_get_troop_morality_value", ":leader", tmt_humanitarian),
            (this_or_next|ge, reg0, 1),
            (this_or_next|troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_goodnatured),
            (this_or_next|troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_benefactor),
            (troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_moralist),

            (assign, ":trigger_result", 0),
        (else_try),
        # do not attack
            (this_or_next|party_slot_eq, ":party_no_seer", slot_party_ai_state, spai_besieging_center),
            (this_or_next|party_slot_eq, ":party_no_seer", slot_party_ai_state, spai_engaging_army),
            (this_or_next|party_slot_eq, ":party_no_seer", slot_party_ai_state, spai_accompanying_army),
            (party_slot_eq, ":party_no_seer", slot_party_ai_state, spai_screening_army),

            (neg|party_slot_eq, ":party_no_seen", slot_party_type, spt_kingdom_hero_party),
            # (neg|party_slot_eq, ":party_no_seen", slot_party_type, spt_patrol),
            (neg|party_slot_eq, ":party_no_seen", slot_party_type, spt_rebellion),
            (neg|party_slot_eq, ":party_no_seen", slot_party_type, spt_minor_faction_raiders),

            (assign, ":trigger_result", 0),
        (try_end),
	(try_end),
	(assign, reg0, ":save_reg0"),
	(set_trigger_result, ":trigger_result"),
]),
##diplomacy end+

#script_game_get_party_speed_multiplier
# This script is called from the game engine when a skill's modifiers are needed
# INPUT: arg1 = party_no
# OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
("game_get_party_speed_multiplier",[
    (store_script_param_1, ":party_no"),

    (party_get_current_terrain, ":cur_terrain", ":party_no"), ##set variables
    (assign,":speed_multiplier",speed_modifier_campaign),     ##set variables
    (try_begin),##start with player
        (eq, ":party_no", "p_main_party"),# player
        (try_begin), #on water
            (this_or_next|eq,":cur_terrain",rt_bridge),
            (this_or_next|eq,":cur_terrain",rt_water),
            (eq,":cur_terrain",rt_river),
            (try_begin), #but no ship
                (party_slot_eq, ":party_no", slot_party_on_water, 0),
                (display_message, "@Player on water without ship", message_alert),
                (set_trigger_result, 1),
                (party_get_position, pos1, ":party_no"),
                (rest_for_hours, 1, 1, 0),
                (rest_for_hours, 0, 0, 0),
                (set_fixed_point_multiplier, 100),
                (call_script, "script_get_next_land_position", 1),
                (party_set_position, "p_main_party", pos2),
            (try_end),
            ##if party is on water speed is determnied by wind
            (try_begin),
                (party_slot_eq, ":party_no", slot_party_on_water, 1),
                (assign, ":speed_multiplier", 80),
                (try_begin),
                    (eq, "$wind_power", 0),
                    (val_sub, ":speed_multiplier", 25),
                (else_try),
                    (eq, "$wind_power", 1),
                    (val_add, ":speed_multiplier", 20),
                (else_try),
                    (eq, "$wind_power", 2),
                    (val_add, ":speed_multiplier", 10),
                (else_try),
                    (val_add, ":speed_multiplier", 15),
                (try_end),
                ####special items: #itm_anti_fooling_paint
                (try_begin),
                    (store_item_kind_count, ":item_count", "itm_anti_fooling_paint"),
                    (gt, ":item_count", 0),
                    (val_add, ":speed_multiplier", 5),
                (try_end),
                ####speed bonus from sailors
                (try_begin),
                    (store_party_size_wo_prisoners, ":party_size", "p_main_party"),
                    (gt, ":party_size", 0),
                    (party_count_companions_of_type, ":num_sailors_follower", "p_follower_party", "trp_sailor"),
                    (party_count_companions_of_type, ":num_sailors", "p_main_party", "trp_sailor"),
                    (party_count_companions_of_type, ":num_sailors1", "p_main_party", "trp_sea_raider"),
                    (party_count_companions_of_type, ":num_sailors1", "p_main_party", "trp_black_sea_priate"),
                    (val_add, ":num_sailors", ":num_sailors1"),

                    (val_add, ":num_sailors", ":num_sailors_follower"),

                    (val_mul, ":num_sailors", 80),
                    (store_div, ":troop_speed_percent", ":num_sailors", ":party_size"),
                    (val_min, ":troop_speed_percent", 40),	# troop speed bonus limit cap of 40% VC-2124
                    (assign, reg6, ":troop_speed_percent"),					#for presentation
                    (store_mul, ":troop_speed_bonus", ":troop_speed_percent", ":speed_multiplier"),
                    (val_div, ":troop_speed_bonus", 100),
                (try_end),
                (val_add, ":speed_multiplier", ":troop_speed_bonus"),
            (try_end),
        (else_try), #on land
            (try_begin),##normal
                (party_slot_eq, ":party_no", slot_party_on_water, 0),
                (party_get_skill_level, ":speed_multiplier_additio", ":party_no", skl_pathfinding), #skills is important now
                (val_mul,":speed_multiplier_additio",2),
                (val_add,":speed_multiplier",":speed_multiplier_additio"),
            (else_try),
                #with ship
                (party_slot_eq, ":party_no", slot_party_on_water, 1),
                (set_trigger_result, 1),
                (party_get_position, pos1, ":party_no"),
                (call_script, "script_get_next_water_position", 1, ":party_no"),
                (party_set_position, "p_main_party", pos2),
                (rest_for_hours, 0, 0, 0),
            #  (display_message, "@Relocated player: reason: on land but with ship"),
            (try_end),
            #stance
            (try_begin),
                (eq, "$g_stance", 1),
                (val_add, ":speed_multiplier", 40),
            (else_try),
                (eq, "$g_stance", 2),
                (val_sub, ":speed_multiplier", 30),
            (try_end),
            #camp follower party
            (try_begin),
                (store_party_size_wo_prisoners, ":size", "p_follower_party"),
                (gt, ":size", 0),
                (val_mul, ":speed_multiplier", 4),
                (val_div, ":speed_multiplier", 5),
            (try_end),
        (try_end),
    (else_try), ##now AI
        (try_begin),    #AI on water
            # (eq,":cur_terrain",rt_river),
            # (call_script, "script_get_next_land_position", 2),
            # (party_set_position, ":party_no", pos2),
            # (str_store_party_name, s22, ":party_no"),
            # (call_script, "script_get_closest_center", ":party_no"),
            # (str_store_party_name, s23, reg0),
            # (display_message, "@Relocated {s22} near {s23}, it was on a river!"),
        # (else_try),
            (this_or_next|eq,":cur_terrain",rt_bridge),
            (this_or_next|eq,":cur_terrain",rt_river),
            (eq,":cur_terrain",rt_water),		# maybe remove line later...

            # (try_begin),
            #     (party_slot_eq, ":party_no", slot_party_on_water, 0),	#PARTY IS SWITCHING FROM LAND TO WATER
            #     (party_set_slot, ":party_no", slot_party_on_water, 1),
            #     (party_set_flags, ":party_no", pf_is_ship, 1),
            #     (try_begin),	#free player if he is captive
            #         (eq, "$g_player_is_captive", 1),
            #         (eq, "$travel_town", 0),	#VC-2283
            #         (eq, ":party_no", "$capturer_party"),
            #         (jump_to_menu,"mnu_captivity_end_wilderness_escape"),
            #     (try_end),
            #     (call_script, "script_update_party_icon", ":party_no"),#update icon
            # (try_end),
            ##if party is on water speed is determnied by wind
            (try_begin),
                (party_slot_eq, ":party_no", slot_party_on_water, 1),
                (assign, ":speed_multiplier", 80),
                (try_begin),
                    (eq, "$wind_power", 0),
                    (val_sub, ":speed_multiplier", 25),
                (else_try),
                    (eq, "$wind_power", 1),
                    (val_add, ":speed_multiplier", 20),
                (else_try),
                    (eq, "$wind_power", 2),
                    (val_add, ":speed_multiplier", 10),
                (else_try),
                    (val_add, ":speed_multiplier", 15),
                (try_end),
            (try_end),
        (else_try), #on land

            # (try_begin),
            #     (party_slot_eq, ":party_no", slot_party_on_water, 1),	#PARTY IS SWITCHING FROM WATER TO LAND
            #     (party_set_slot, ":party_no", slot_party_on_water, 0),
            #     (party_set_flags, ":party_no", pf_is_ship, 0),#I think this should still be necessary
            #     (call_script, "script_update_party_icon", ":party_no"),#update icon
            # (try_end),
            # AI
            (try_begin), #lords
                (neg|party_slot_eq, ":party_no", slot_party_on_water, 1),##not on water
                (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
                (party_get_skill_level, ":speed_multiplier_additio", ":party_no", skl_pathfinding), #skills is important now
                (val_mul,":speed_multiplier_additio",2),
                (val_add,":speed_multiplier",":speed_multiplier_additio"),
            (else_try),
                (party_get_template_id,":party_template",":party_no"),#get variables
                (eq,":party_template","pt_kingdom_caravan_party"),
                (val_sub,":speed_multiplier", 5),
            (else_try),
                (eq,":party_template","pt_messenger_party"),
                (val_add,":speed_multiplier", 40),
            (else_try),#to make this quest easier
                (eq,":party_template","pt_spy"),
                (val_mul,":speed_multiplier", 2),
                (val_div,":speed_multiplier", 5),
            (else_try),
                (this_or_next|eq, ":party_template", "pt_hord_siraken"),
                (eq, ":party_template", "pt_hord_roxolanen"),
                (party_get_icon, ":icon", ":party_no"),
                (try_begin),
                    (eq, ":icon", "icon_castle_a"),
                    (assign, ":speed_multiplier", 0),
                (else_try),
                    (assign, ":speed_multiplier", 50),
                (try_end),
            (else_try),
                (eq, ":party_template", "pt_routed_warriors"),#smal bonus for
                (val_add,":speed_multiplier",7),
            (try_end),
            ##if a slow lords follow a fast marshall he may get lost, this helps
            (try_begin),
                (get_party_ai_behavior, ":behavior", ":party_no"),
                (eq, ":behavior", ai_bhvr_driven_by_party),
                (val_add,":speed_multiplier",20),
            (try_end),
            (try_begin),
                (get_party_ai_behavior, ":behavior", ":party_no"),
                (eq, ":behavior", ai_bhvr_escort_party),##if party follows party it will get a speed bonus,needs testing
                (val_add,":speed_multiplier",20),
            (try_end),
            (try_begin),
                (party_stack_get_troop_id, ":commander", ":party_no", 0),
                (this_or_next|troop_slot_ge, ":commander", slot_troop_legion, 1),
                (troop_slot_ge, ":commander", slot_troop_aux, 1),
                (val_add,":speed_multiplier",10),
            (try_end),
        (try_end),
    (try_end),
    ##special cases:
    (try_begin), # TRAVEL SYSTEM (Ferry)
        (eq, ":party_no", "p_transporter"),
        (try_begin),
            (gt, "$travel_town", towns_end),	#ferry is in use
            (assign,":speed_multiplier", 20),
        (else_try),
            (assign,":speed_multiplier", 75),
        (try_end),
    (try_end),
    (try_begin), ##permanent player camps
        (party_slot_eq, ":party_no", slot_party_type, spt_player_camp),
        (assign, ":speed_multiplier", 0),
    (try_end),
    (val_max, ":speed_multiplier", 0),
    (set_trigger_result, ":speed_multiplier"),
]),
]#end of file
