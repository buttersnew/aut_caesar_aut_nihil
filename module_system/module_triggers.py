from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_terrain_types import *
from module_constants import *

#from compiler import *
####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

triggers = [

#initialization of certain start options
(0,0,ti_once,[
],[
    (call_script, "script_set_settlement_names"), # province names
    ## init recruits for player recruitement
    # (display_message, "@type, province, center, peasants, nobles, mercs"),
    (try_for_range, ":center_no", centers_begin, centers_end),
        (try_begin),
            (is_between, ":center_no", villages_begin, villages_end),
            (call_script, "script_update_volunteer_troops_in_village", ":center_no"),
        (try_end),
        (call_script, "script_get_volunteer_limits", ":center_no"),
        (party_set_slot, ":center_no", slot_center_peasant_troop_amount, reg1),
        (party_set_slot, ":center_no", slot_center_volunteer_noble_troop_amount, reg2),
        (party_set_slot, ":center_no", slot_center_mercenary_troop_amount_2, reg3),
        # (str_store_party_name, s10, ":center_no"),
        # (try_begin),
        #     (is_between, ":center_no", villages_begin, villages_end),
        #     (str_store_string, s11, "@village"),
        # (else_try),
        #     (is_between, ":center_no", castles_begin, castles_end),
        #     (str_store_string, s11, "@castle"),
        # (else_try),
        #     (str_store_string, s11, "@town"),
        # (try_end),
        # (party_get_slot, ":province", ":center_no", slot_center_province),
        # (val_add, ":province", str_province_begin),
        # (str_store_string, s12, ":province"),
        # (display_message, "@{s11}, {s12}, {s10}, {reg1}, {reg2}, {reg3}"),
    (try_end),

    (try_for_range, ":center_no", minor_towns_begin, minor_towns_end),
        (call_script, "script_get_volunteer_limits", ":center_no"),
        (party_set_slot, ":center_no", slot_center_peasant_troop_amount, reg1),
        (party_set_slot, ":center_no", slot_center_volunteer_noble_troop_amount, reg2),
        (party_set_slot, ":center_no", slot_center_mercenary_troop_amount_2, reg3),
        # (str_store_party_name, s10, ":center_no"),
        # (try_begin),
        #     (is_between, ":center_no", villages_begin, villages_end),
        #     (str_store_string, s11, "@village"),
        # (else_try),
        #     (is_between, ":center_no", castles_begin, castles_end),
        #     (str_store_string, s11, "@castle"),
        # (else_try),
        #     (str_store_string, s11, "@town"),
        # (try_end),
        # (party_get_slot, ":province", ":center_no", slot_center_province),
        # (val_add, ":province", str_province_begin),
        # (str_store_string, s12, ":province"),
        # (display_message, "@{s11}, {s12}, {s10}, {reg1}, {reg2}, {reg3}"),
    (try_end),
]),

#death of poppaea through assassination
(24,0,ti_once,[
    (check_quest_active, "qst_blank_quest_19"),
    (quest_slot_eq, "qst_blank_quest_19", slot_quest_main_poppaea_fate, 3),
    (troop_slot_eq, "trp_kingdom_7_lady_1", slot_troop_occupation, slto_kingdom_lady),
    (troop_slot_eq, "trp_antonia", slot_troop_occupation, slto_kingdom_lady),
    (quest_get_slot, ":day", "qst_blank_quest_19", slot_quest_main_poppaea_timer),
    (gt, ":day", -1),
    (store_current_day, ":cur_day"),
    (val_sub, ":cur_day", ":day"),
    (ge, ":cur_day", 14),
],[
    (call_script, "script_add_notification_menu", "mnu_assassination_of_antonia",0,0),
    (quest_set_slot, "qst_blank_quest_19", slot_quest_main_poppaea_timer, -1),
]),

## goy event
(24,0,ti_once,[
    (eq, "$jewish_revolt", 1),
    (this_or_next|eq, "$g_campaign_type", g_campaign_lord),
    (this_or_next|eq, "$g_campaign_type", g_campaign_king),
    (eq, "$g_campaign_type", g_campaign_sandbox),
    (store_current_hours, ":hours"),
    (call_script, "script_game_get_date_text", 0, ":hours"),
    (ge, reg2, 68),
    (troop_slot_eq, trp_kingdom_7_lord, slot_troop_occupation, slto_kingdom_hero), # nero alive
    (store_faction_of_party, ":fac", "p_town_6"), # rome should be part of ROME
    (eq, ":fac", "fac_kingdom_7"),
    (faction_slot_eq, "fac_kingdom_7", slot_faction_state, sfs_active), # rome is active
],[
    (call_script, "script_add_notification_menu", "mnu_year_of_four_ceasars",0,0),
]),

#goy event 2
(24,0,ti_once,[
    (store_current_day, ":day"),
    (neg|troop_slot_ge, "trp_global_variables", g_civil_war_timer, ":day"),
    #(troop_slot_ge, "trp_global_variables", g_civil_war_timer, ":day"),
    (neg|troop_slot_eq, "trp_global_variables", g_civil_war_timer, 0),
    (neg|troop_slot_eq, "trp_global_variables", g_civil_war_timer, -1),
],[
    (call_script, "script_add_notification_menu", "mnu_civil_war_start",0,0),
]),

# raise to nobility
(24,0,ti_once,[
    (store_troop_gold, ":g", "trp_player"),
    (ge, ":g", 200000),
    (troop_slot_ge, "trp_global_variables", g_number_of_lat, 5),
    (troop_slot_ge, "trp_player", slot_troop_renown, 200),
    (troop_slot_eq, "trp_player", slot_troop_culture, "fac_culture_7"),
    (neg|is_between,"$players_kingdom", kingdoms_begin,kingdoms_end),
    (check_quest_active, "qst_blank_quest_19"),
    (check_quest_active, "qst_gain_renown"),
    (neg|faction_slot_eq, "fac_player_supporters_faction",slot_faction_state, sfs_active),

    ##block for main story
    (assign, ":block", 0),
    (try_begin),
        (eq, "$g_campaign_type", g_campaign_story_rome),
        (neg|check_quest_active, "qst_gain_renown"),
        (assign, ":block", 1),
    (try_end),
    (eq, ":block", 0),
],[
    (call_script, "script_add_notification_menu", "mnu_player_raises_to_nobility",0,0),
]),

(0, 24*7, 0,[],[
    (store_current_hours, "$g_next_pay_time"),
    (val_add, "$g_next_pay_time", 24 * 7),

    # (assign, "$g_apply_budget_report_to_gold", 1),
    # (start_presentation, "prsnt_imperial_budget_report"),

    (try_begin),
        (eq, "$g_infinite_camping", 0),
        (assign, "$g_apply_budget_report_to_gold", 1),
        (start_presentation, "prsnt_budget_report"),
        (try_begin),
            (gt, "$g_player_debt_to_party_members", 75000),
            (call_script, "script_add_notification_menu", "mnu_dplmc_deserters",20,0),
        (try_end),
        (try_begin),
            (troop_get_slot, ":taken_money", "trp_player", slot_player_takes_money_from_treasury),
            (ge, ":taken_money", 0),
            (val_sub, ":taken_money", 125000),
            (val_max, ":taken_money", 0),
            (troop_set_slot, "trp_player", slot_player_takes_money_from_treasury, ":taken_money"),
        (try_end),
    (try_end),
    (try_for_range, ":imperial_faction", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_slot_eq, ":imperial_faction", slot_faction_state, sfs_active),
        (neg|faction_slot_eq, ":imperial_faction", slot_faction_leader, "trp_player"),
        (faction_slot_eq, ":imperial_faction", slot_faction_government_type, gov_imperial),
        (call_script, "script_weekly_imperial_balance", ":imperial_faction"),
        (faction_get_slot, ":tax_rate", ":imperial_faction", slot_faction_tax_rate),
        (faction_get_slot, ":tax_rate_business", ":imperial_faction", slot_faction_tax_rate_buisness),
        (faction_get_slot, ":leader", ":imperial_faction", slot_faction_leader),

        (try_begin),
            (faction_slot_ge, ":imperial_faction", slot_faction_debts, 1500000),
            (assign, ":uper_limit", 50),
            (assign, ":uper_limit_business", 35),
        (else_try),
            (faction_slot_ge, ":imperial_faction", slot_faction_debts, 1250000),
            (assign, ":uper_limit", 45),
            (assign, ":uper_limit_business", 30),
        (else_try),
            (faction_slot_ge, ":imperial_faction", slot_faction_debts, 1000000),
            (assign, ":uper_limit", 40),
            (assign, ":uper_limit_business", 30),
        (else_try),
            (faction_slot_ge, ":imperial_faction", slot_faction_debts, 750000),
            (assign, ":uper_limit", 35),
            (assign, ":uper_limit_business", 25),
        (else_try),
            (assign, ":uper_limit", 30),
            (assign, ":uper_limit_business", 20),
        (try_end),
        (try_begin),
            (faction_slot_ge, ":imperial_faction", slot_faction_debts, 500000),
            (le, ":tax_rate", ":uper_limit"),
            (str_store_troop_name, s1, ":leader"),
            (tutorial_box, "@{s1} has increased taxes!"),
            (val_add, ":tax_rate", 5),
            (le, ":tax_rate_business", ":uper_limit_business"),
            (val_add, ":tax_rate_business", 5),
        (else_try),
            (faction_slot_ge, ":imperial_faction", slot_faction_treasury, 500000),
            (str_store_troop_name, s1, ":leader"),
            (tutorial_box, "@{s1} has cut taxes!"),
            (ge, ":tax_rate", 10),
            (val_sub, ":tax_rate", 5),
            (ge, ":tax_rate_business", 5),
            (val_sub, ":tax_rate_business", 5),
        (try_end),
        (faction_set_slot, ":imperial_faction", slot_faction_tax_rate, ":tax_rate"),
        (faction_set_slot, ":imperial_faction", slot_faction_tax_rate_buisness, ":tax_rate_business"),
    (try_end),
]),

(0, 0, 24*180,[
    (le, "$g_is_emperor", 0),
    (troop_slot_eq, "trp_global_variables", g_iazyges_event, 0),
    (this_or_next|eq, "$g_campaign_type", g_campaign_king),
    (this_or_next|eq, "$g_campaign_type", g_campaign_lord),
    (eq, "$g_campaign_type", g_campaign_sandbox),
    #(neg|troop_slot_eq, "trp_player", slot_troop_culture, "fac_culture_7"),
],[
    (store_current_hours, ":hours"),
    (call_script, "script_game_get_date_text", 0, ":hours"),
    (ge, reg2, 66),
    (try_begin),
        (assign, ":c", 0),
        (try_for_range, ":center", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":center", slot_center_province, p_cent_panno),
            (store_faction_of_party, ":faction", ":center"),
            (eq, ":faction", "fac_kingdom_7"),
            (assign, ":c", 1),
        (try_end),
        (eq, ":c", 1),
        (troop_set_slot, "trp_global_variables", g_iazyges_event, 2),
    (else_try),
        (troop_set_slot, "trp_global_variables", g_iazyges_event, -1),
    (try_end),
]),

(24*7, 0, ti_once,[
    (troop_slot_eq, "trp_global_variables", g_batava_event, 0),
    (gt, "$g_civil_war", 1),
],[
    (call_script, "script_add_notification_menu", "mnu_batava_revolt", 0, 0),
]),

(24 + 16, 6, ti_once,[
    (map_free,0),
],[
    (start_presentation, "prsnt_game_concepts_tutorial"),
]),

(24*3, 0, ti_once,[
    (neq, "$g_player_is_captive", 1),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_1"),
    (quest_slot_ge, "qst_wlodowiecus_adventure_1", slot_quest_current_state, 1),
    (quest_get_slot, ":timer", "qst_wlodowiecus_adventure_1", slot_quest_timer),
    (neq, ":timer", 0),
    (store_current_day, ":cur_day"),
    (val_sub, ":cur_day", ":timer"),
    (ge, ":cur_day", 14), ## 14 days

    (quest_slot_eq, "qst_wlodowiecus_adventure_2", slot_quest_current_state, 0),
    (store_character_level, ":level", "trp_player"),
    (ge, ":level", 16),
],[
    (call_script, "script_add_notification_menu", "mnu_wlodowiecus_adventure_1_2_intro", 0, 0),
]),

(24*3, 0, ti_once,[
    (neq, "$g_player_is_captive", 1),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_1"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_2"),
    (quest_slot_ge, "qst_wlodowiecus_adventure_2", slot_quest_current_state, 1),

    (quest_get_slot, ":timer", "qst_wlodowiecus_adventure_2", slot_quest_timer),
    (neq, ":timer", 0),
    (store_current_day, ":cur_day"),
    (val_sub, ":cur_day", ":timer"),
    (ge, ":cur_day", 14), ## 14 days

    (quest_slot_eq, "qst_wlodowiecus_adventure_3", slot_quest_current_state, 0),
    (store_character_level, ":level", "trp_player"),
    (ge, ":level", 21),
],[
    (call_script, "script_add_notification_menu", "mnu_wlodowiecus_adventure_1_3_intro", 0, 0),
]),

(24*3, 0, ti_once,[
    (neq, "$g_player_is_captive", 1),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_1"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_2"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_3"),
    (quest_slot_ge, "qst_wlodowiecus_adventure_3", slot_quest_current_state, 1),

    (quest_get_slot, ":timer", "qst_wlodowiecus_adventure_3", slot_quest_timer),
    (neq, ":timer", 0),
    (store_current_day, ":cur_day"),
    (val_sub, ":cur_day", ":timer"),
    (ge, ":cur_day", 14), ## 14 days

    (quest_slot_eq, "qst_wlodowiecus_adventure_4", slot_quest_current_state, 0),
    (store_character_level, ":level", "trp_player"),
    (ge, ":level", 26),
],[
    (call_script, "script_add_notification_menu", "mnu_wlodowiecus_adventure_1_4_intro", 0, 0),
]),

(24, 0, ti_once,[
    (neq, "$g_player_is_captive", 1),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_1"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_2"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_3"),
    (neg|check_quest_active, "qst_wlodowiecus_adventure_4"),
    (quest_slot_ge, "qst_wlodowiecus_adventure_4", slot_quest_current_state, 1),
    (quest_slot_eq, "qst_wlodowiecus_adventure_4", slot_quest_object_faction, 1),
    (quest_get_slot, ":timer", "qst_wlodowiecus_adventure_4", slot_quest_timer),
    (neq, ":timer", 0),
    (store_current_day, ":cur_day"),
    (val_sub, ":cur_day", ":timer"),
    (ge, ":cur_day", 6), ## 7 days
],[
    (call_script, "script_add_notification_menu", "mnu_wlodowiecus_adventure_1_phamanus", 0, 0),
]),

(48, 0, ti_once, [
    (neq, "$g_player_is_captive", 1),
    (eq, "$enlisted_party", -1),#not freelancing
    (troop_slot_eq, "trp_player", slot_troop_culture, "fac_culture_7"),
    (troop_slot_ge, "trp_player", slot_troop_renown, 400),
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 40000),
    (troop_slot_eq, "trp_global_variables", g_player_villa, 0),
],[
    (troop_set_slot, "trp_global_variables", g_player_villa, 1),
	  (dialog_box,"@You receive a message from the magister civium of Neapolis. He wants to inform you about a villa he has for sale. A famous person like you should own such an estate. Talk with the magister civium of Neapolis."),
]),

# (1, 0, ti_once, [
#     (neq, "$g_is_emperor", 1),
#     (neg|check_quest_active, "qst_blank_quest_5"),
#     (neg|check_quest_active, "qst_blank_quest_19"),
#     (store_distance_to_party_from_party, ":distance", "p_main_party", "p_town_6"),
#     (lt, ":distance", 10),
#     (neq, "$g_player_is_captive", 1),
#     (eq, "$g_campaign_type", g_campaign_story_rome),
# ],[
#     (jump_to_menu, "mnu_ad_mortem"),
# ]),

(1, 0, ti_once, [
    (neg|troop_slot_ge, "trp_petrus", slot_troop_met, 1),#havent talked with petrus yet
    (neq, "$g_is_emperor", 1),
    (troop_slot_ge, "trp_paulus", slot_troop_met, 1),#talked with paulus
    (neg|check_quest_active, "qst_blank_quest_8"),#rome burned down
    (store_distance_to_party_from_party, ":distance", "p_main_party", "p_town_6"),
    (lt, ":distance", 6),
    (neq, "$g_player_is_captive", 1),
],[
    (jump_to_menu, "mnu_event_petrus"),
]),


(24, 0, 24*7, [
    (check_quest_active, "qst_freelancing"),
    (party_is_active, "$enlisted_party"),
    (party_get_battle_opponent, ":commander_opponent", "$enlisted_party"),
    (lt, ":commander_opponent", 0),
    (party_get_attached_to, ":town", "$enlisted_party"),
    (neg|is_between, ":town", centers_begin, centers_end),
    (neg|party_slot_eq, "$enlisted_party", slot_party_on_water, 1),#not on water
],[
    (jump_to_menu, "mnu_freelancer_weekly_duty")
]),

(0, 0, 0, [
  (key_clicked, key_k),
  (check_quest_active, "qst_freelancing"),
  (party_is_active, "$enlisted_party"),
], [
  (try_begin),
    (party_get_battle_opponent, ":commander_opponent", "$enlisted_party"),
    (lt, ":commander_opponent", 0),
    (party_get_attached_to, ":town", "$enlisted_party"),
    (neg|is_between, ":town", centers_begin, centers_end),
    (neg|party_slot_eq, "$enlisted_party", slot_party_on_water, 1),#not on water
    (jump_to_menu, "mnu_freelancer_weekly_duty"),
  (else_try),
    (display_message, "@Not possible now."),
  (try_end),
]),

# Refresh slave merchants
(0, 0, 168.0, [],[
    # Refill town-based slave traders
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (call_script, "script_get_slave_merchant_troop", ":center_no"),
      (assign, ":slave_trader", reg0),
      (is_between, ":slave_trader", slave_traders_centers_begin, slave_traders_centers_end),
      (call_script, "script_refill_slave_merchant", ":slave_trader", ":center_no"),
    (try_end),
    # Refill bandit-lair slave traders
    (try_for_range, ":slave_trader", slave_traders_begin, slave_traders_end),
      (call_script, "script_refill_slave_merchant", ":slave_trader", -1), # -1 indicates not a town
    (try_end),
    # refill ransom brokers
    (try_for_range, ":ransom_broker", ransom_brokers_begin, ransom_brokers_end),
      (call_script, "script_refill_slave_merchant", ":ransom_broker", -1), # -1 indicates not a town
    (try_end),
    # Refill special traders
    (call_script, "script_refill_slave_merchant", "trp_galeas", -1),
    (call_script, "script_refill_slave_merchant", "trp_ramun_the_slave_trader", -1),
]),

# Refresh Merchants
(0.0, 0, 168.0, [],[
  (call_script, "script_refresh_center_inventories"),
]),

# Refresh Armor sellers
(0.0, 0, 168.0, [],[
  (call_script, "script_refresh_center_armories"),
]),

# Refresh Weapon sellers
(0.0, 0, 168.0, [],[
  (call_script, "script_refresh_center_weaponsmiths"),
]),

# Refresh Horse sellers
(0.0, 0, 168.0, [],[
  (call_script, "script_refresh_center_stables"),
]),

# Refresh special merchants
(0.0, 0, 168.0, [],[
  (call_script, "script_refresh_special_merchants"),
]),

(1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
],[
  (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit


		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),

		(try_for_parties, ":party"),
			# (gt, ":party", "p_spawn_points_end"),
			 (gt, ":party", "p_arabian_town_1"),

			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),


			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),

			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
    (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
]),

#freelancer menu
(0.0, 0, 0, [
  (ge, "$enlisted_party", 1),
],[
  (try_begin),# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU
    (party_is_active, "$enlisted_party"),
    (key_clicked, key_left_mouse_button),
    (set_fixed_point_multiplier, 1000),
    (mouse_get_position, pos0),
    (position_get_y, ":y", pos0),
    (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    (jump_to_menu, "mnu_world_map_soldier"),
    (rest_for_hours_interactive, 9999, 4, 0),
  (else_try),#commander defeated
    (neg|party_is_active, "$enlisted_party"),
    (jump_to_menu, "mnu_freelancer_defeated"),
  (try_end),
]),

(4.0, 0, 0.0,[
  (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
  (assign, ":continue", 0),
  (try_begin),
    (neg|party_is_active, "$caravan_escort_party_id"),
    (assign, ":continue", 1),
  (else_try),
    (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
    (neq, ":ai_object", "$caravan_escort_destination_town"),
    (assign, ":continue", 1),
  (try_end),
  (eq, ":continue", 1),
],[
  (assign, "$caravan_escort_state", 0),
]),

#Kingdom Parties: caravans
(1.0, 0, 0.0, [],[
  (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
    (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
    (try_begin),
      (store_random_in_range, ":random_no", 0, 100),
      (lt, ":random_no", 10),
      (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
    (try_end),
    (try_begin),                        #SEATRADE
      (store_random_in_range, ":random_no", 0, 100),       #Disable these for faster testing
      (lt, ":random_no", 30),                              #Disable these for faster testing
      (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_merchant_caravan),
    (try_end),
  (try_end),
]),
##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
(0.2, 0.0, 0.0,[
  (check_quest_active, "qst_incriminate_loyal_commander"),
  (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
  (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
  (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
  (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
  (try_begin),
    (neg|party_is_active, ":quest_target_party"),
    (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
    (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
  (else_try),
    (party_is_in_town, ":quest_target_party", ":quest_target_center"),
    (remove_party, ":quest_target_party"),
    (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
    (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
    # (assign, ":num_available_factions", 0),
    # (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
    #   (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
    #   (neq, ":faction_no", "fac_player_supporters_faction"),
    #   (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
    #   (val_add, ":num_available_factions", 1),
    # (try_end),
    # (try_begin),
    #   (gt, ":num_available_factions", 0),
    #   (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
    #   (assign, ":target_faction", -1),
    #   (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
    #     (eq, ":target_faction", -1),
    #     (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
    #     (neq, ":faction_no", "fac_player_supporters_faction"),
    #     (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
    #     (val_sub, ":random_faction", 1),
    #     (lt, ":random_faction", 0),
    #     (assign, ":target_faction", ":faction_no"),
    #   (try_end),
    # (try_end),
    # (try_begin),
    #   (gt, ":target_faction", 0),
    #   (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
    # (else_try),
    (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
    # (try_end),
    (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
  (try_end),
],[]),

# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),

         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),

         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),

 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),

  (0.3, 0, 1.1, [
    (check_quest_active, "qst_escort_merchant_caravan"),
    (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
    (neg|party_is_active,":quest_target_party"),
  ],[
    (call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
  ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),

# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),
#NPC system changes begin
#Move unemployed NPCs around taverns
   # (24 * 15 , 0, 0,
   # [
    # (call_script, "script_update_companion_candidates_in_taverns"),
    # ],
   # []
   # ),

#Process morale and determine personality clashes
(0, 0, 24,[],[
    #Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
    #Set their relation to the player
    (assign, ":npcs_in_party", 0),
    (assign, ":grievance_divisor", 100),
    (try_for_range, ":npc1", companions_begin, companions_end),
        (main_party_has_troop, ":npc1"),
        (val_add, ":npcs_in_party", 1),
    (try_end),
    (val_div, ":npcs_in_party", 2),
    (val_sub, ":grievance_divisor", ":npcs_in_party"),
    (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
    (val_add, ":grievance_divisor", ":persuasion_level"),
    #(assign, reg7, ":grievance_divisor"),
    #(display_message, "@{!}Process NPC changes. GD: {reg7}"),

    ##Activate personality clash from 24 hours ago
    (try_begin), #scheduled personality clashes require at least 24hrs together
        (gt, "$personality_clash_after_24_hrs", 0),
        (eq, "$disable_npc_complaints", 0),
        (try_begin),
            (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
            (main_party_has_troop, "$personality_clash_after_24_hrs"),
            (is_between, ":other_npc", companions_begin, companions_end),#check that he exists
            (main_party_has_troop, ":other_npc"),
            (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
        (try_end),
        (assign, "$personality_clash_after_24_hrs", 0),
    (try_end),
    #
    (try_for_range, ":npc", companions_begin, companions_end),
        ###Reset meeting variables
        (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
        (try_begin),
            (troop_slot_eq, ":npc", slot_troop_met, 1),
            (troop_set_slot, ":npc", slot_troop_met_previously, 1),
        (try_end),

        ###Check for coming out of retirement
        (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
        (try_begin),
            (eq, ":occupation", slto_retirement),
            (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

            (str_store_troop_name, s31, ":npc"),
            (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
            (assign, reg4, ":player_renown"),
            (assign, reg5, ":renown_min"),
            #                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

            (gt, ":player_renown", ":renown_min"),
            (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
            (troop_set_slot, ":npc", slot_troop_occupation, 0),
        (try_end),


        #Check for political issues
        (try_begin), #does npc's opponent pipe up?
            (troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
            (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

            (troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
            (is_between, ":other_npc", companions_begin, companions_end),#check that he exists
            (troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),

            (troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),

            (str_store_troop_name, s3, ":npc"),
            (str_store_troop_name, s4, ":other_npc"),

            (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
            (try_end),
        (try_end),

        #Check for quitting
        (try_begin),
            (main_party_has_troop, ":npc"),

            (call_script, "script_dplmc_npc_morale", ":npc", 0), #SB : just the number
            (assign, ":npc_morale", reg0),
            # (str_store_troop_name, s10, ":npc"),
            # (display_message, "@{s10}: morale {reg0}"),
            (try_begin),
                (eq, "$disable_companions_leaving", 0),
                (lt, ":npc_morale", 20),
                (store_random_in_range, ":random", 0, 100),
                (val_add, ":npc_morale", ":random"),
                (lt, ":npc_morale", 20),
                (neq, ":npc", "trp_npc35"), # not ursus
                (neq, ":npc", "trp_mathildiz"), # not mathildize
                (neq, ":npc", "trp_turakina"), # not eamane
                (assign, "$npc_is_quitting", ":npc"),
            (try_end),

            #Reduce grievance over time (or augment, if party is overcrowded
            (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
            # (try_begin),
            #     (ge, "$cheat_mode", 1),
            #     (str_store_troop_name, s0, ":npc"),
            #     (assign, reg1, ":grievance"),
            #     (display_message, "@{s0}: {reg1} grievance"),
            # (try_end),
            (val_mul, ":grievance", 90),
            (val_div, ":grievance", ":grievance_divisor"),
            (val_clamp, ":grievance", -10000, 10000),
            (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

            (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
            (val_mul, ":grievance", 90),
            (val_div, ":grievance", ":grievance_divisor"),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
            #Change personality grievance levels
            (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                (main_party_has_troop, ":object"),
                (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
            (try_end),
            (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                (main_party_has_troop, ":object"),
                (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
            (try_end),
            (try_begin),
                (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                (eq, "$disable_npc_complaints", 1),
                (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                (main_party_has_troop, ":object"),
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 9),
                (val_div, ":grievance", 10),
                (val_clamp, ":grievance", -10000, 10000),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
            (try_end),
            #Check for new personality clashes
            #Active personality clash 1 if at least 24 hours have passed
            (try_begin),
                (eq, "$disable_npc_complaints", 0),
                (eq, "$npc_with_personality_clash", 0),
                (eq, "$npc_with_personality_clash_2", 0),
                (eq, "$personality_clash_after_24_hrs", 0),
                (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                (is_between, ":other_npc", companions_begin, companions_end),#check that he exists
                (main_party_has_troop, ":other_npc"),
                (assign, "$personality_clash_after_24_hrs", ":npc"),
            (try_end),

            #Personality clash 2 and personality match is triggered by battles
            (try_begin),
                (eq, "$npc_with_political_grievance", 0),

                (troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
                (assign, "$npc_with_political_grievance", ":npc"),
            (try_end),

        #main party does not have troop, and the troop is a companion
        (else_try),
            (neg|main_party_has_troop, ":npc"),
            (eq, ":occupation", slto_player_companion),

            (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),

            (troop_get_slot, ":leaded_party", ":npc", slot_troop_leaded_party),
            (assign, ":continue", 1),
            (try_begin),
                (party_is_active, ":leaded_party"),
                (this_or_next|party_slot_eq, ":leaded_party", slot_party_type, spt_companion_raider),
                (party_slot_eq, ":leaded_party", slot_party_type, spt_player_camp),
                (assign, ":continue", 0),
            (try_end),
            (eq, ":continue", 1),

            (try_begin), #debug
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, s10, ":npc"),
                (assign, reg0, ":days_on_mission"),
                (display_message, "@Checking rejoin of {s10} days on mission: {reg0}"),
            (try_end),

            (try_begin),
                (gt, ":days_on_mission", 0),
                (val_sub, ":days_on_mission", 1),
                (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
                ##diplomacy begin
            (else_try),
                (this_or_next|troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request), #spy mission
                (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner), #SB : escue mission
                (troop_slot_ge, ":npc", dplmc_slot_troop_mission_diplomacy, 1), #caught

                (try_begin), #use hired blade for spy
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request),
                    (troop_set_slot, "trp_hired_blade", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", "trp_hired_blade"),
                (else_try), #use town walker
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner),
                    (troop_get_slot, ":town_no", ":npc", slot_troop_town_with_contacts),
                    (store_random_in_range, ":slot_no", slot_center_walker_0_troop, slot_center_walker_0_troop + num_town_walkers),
                    (party_get_slot, ":walker_no", ":town_no", ":slot_no"),
                    (troop_set_slot, ":walker_no", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", ":walker_no"),
                (try_end),
                ##diplomacy end
            (else_try),
                (troop_slot_ge, ":npc", slot_troop_current_mission, 1),

                #If the hero can join
                (this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                (hero_can_join),

                (assign, "$npc_to_rejoin_party", ":npc"),
            (try_end),
        (try_end),
    (try_end),
]),
# Appoint chamberlain
(24*14, 0, ti_once,[],[
    (neq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
        (eq, ":has_fief", 0),
        (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            (assign, ":has_fief", 1),
        (else_try),
            (party_get_slot, ":latifundium", ":center_no",slot_center_has_latifundium),
            (gt, ":latifundium", 0),
            (party_is_active, ":latifundium"),
            (assign, ":has_fief", 1),
        (try_end),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, "$g_player_chamberlain"),
        (display_message, "@{!}DEBUG : chamberlain: {reg0}"),
    (try_end),
    (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chamberlain", 0, 0),
]),
# Appoint constable
(24*14, 0, ti_once,[],[
    (neq, "$g_player_constable", "trp_dplmc_constable"),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (eq, ":has_fief", 0),
        (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
        (eq, ":lord_troop_id", "trp_player"),
        (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, "$g_player_constable"),
        (display_message, "@{!}DEBUG : constable: {reg0}"),
    (try_end),
    (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_constable", 0, 0),
]),

# Appoint chancellor
(24*14, 0, ti_once,[],[
    (neq, "$g_player_chancellor", "trp_dplmc_chancellor"),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
        (eq, ":has_fief", 0),
        (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
        (eq, ":lord_troop_id", "trp_player"),
        (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, "$g_player_chancellor"),
        (display_message, "@{!}DEBUG : chancellor: {reg0}"),
    (try_end),
    (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chancellor", 0, 0),
]),

(0.1, 0.5, 0, [
    (map_free,0),
    (eq,"$g_move_fast", 1)
],[
    (assign,"$g_move_fast", 0)
]),
##diplomacy end
# #in exchange for the old "find landing points" trigger here is a new solution
(0, 0, 0,[
    (key_clicked, key_left_mouse_button),
    (party_slot_eq, "p_main_party", slot_party_on_water, 1),

    (set_fixed_point_multiplier, 100),
    (party_get_position, pos1, "p_main_party"),
    (party_get_position, pos2, "p_landing_point"),
    (get_distance_between_positions, ":distance", pos1, pos2),
    (gt, ":distance", 200),
    #
    (map_get_land_position_around_position, pos2, pos1, 1),
    (party_set_position, "p_temp_party", pos2),
    (party_get_current_terrain, ":terrain_type", "p_temp_party"),
    (neq, ":terrain_type", 0),
    (neq, ":terrain_type", 1), #cliffs
    (neq, ":terrain_type", 7),
    (neq, ":terrain_type", 8),

    (assign, ":block", 0),
    (try_for_range, ":curr_town", towns_begin, towns_end),	#avoid landing points next to ports
        (party_slot_eq, ":curr_town", slot_town_port, 1),
        (store_distance_to_party_from_party, ":dist", "p_temp_party", ":curr_town"),
        (lt, ":dist", 5),
        (assign, ":block", 1),
    (try_end),
    # (try_for_range, ":curr_bridge", "p_Bridge_1", "p_ferry_1a"),	#avoid landing points next to bridges
      # (store_distance_to_party_from_party, ":dist", "p_temp_party", ":curr_bridge"),
      # (lt, ":dist", 5),
      # (assign, ":block", 1),
    # (try_end),
    (eq, ":block", 0),
],[
    (try_begin),
        (party_get_position, pos1, "p_temp_party"),
        (call_script, "script_get_next_water_position", 0, "p_temp_party"),
        (party_set_position, "p_landing_point", pos2),
    (try_end),
]),

####siege warfare, player lose money each day while siege. Sieges are expensive.
(24, 0, 0, [(eq, "$g_empieza_asedio", 1),], [
  (store_troop_gold,":money","trp_player"),
  (try_begin),
      (ge,":money",100),
      (troop_remove_gold, "trp_player", 100),
      (display_message,"@Each day of the siege, you need to cover a number of expenses. You pay for rewards, digging latrines, cleaning stables, buying and bringing water and food, cooking, entertaining the troops...", 0xFF0000),
      (store_random_in_range,":chance",1,10),
      (try_begin),
          (le,":chance",4),
          (call_script, "script_change_player_party_morale", -1),
      (try_end),
  (else_try),
      (display_message,"@You do not have money to cover the basic expenses of a siege. This greatly undermines morale.", 0xFF0000),
      (call_script, "script_change_player_party_morale", -5),
  (try_end),
]),

(2, 0, 0, [
    (neq, "$moralep_on", 0),
    (neq, "$g_empieza_asedio", 1),
    (eq, "$enlisted_party",-1),
], [
#morale impact chief of resting/not resting by motomataru.
#A little sleep is a lot different than NO sleep. After 90 hours of NO sleep, I think we can agree that most troops would be useless.
#The original system checked if the player got at least TWO hours rest in a town/castle. If so, it reduced the penalty HALF. So you not only reduced penalty but reduced chances of recovery. Intervals longer than eight hours, of course, may miss the night altogether and effectively make this trigger a complete waste of resources.
#On the penalty side, it only increased at night WHLE TRAVELING, so -4 per day MAX, and it doesn't even effect morale immediately (unlike recovery, which does). After 96 hours of doing NOTHING but marching and fighting, it is possible to have a penalty of -16. If a player is NEVER going to stop anywhere at night, he/she should just turn the option off.
#I don't think this is excessive, so am returning it to the original, but give up to +4 per night for resting in the field, but personally I never camp when I play, because of lack of the security of a town
    (store_party_size_wo_prisoners, reg0, "p_main_party"),
    (try_begin),
        (lt, reg0, 2),
        (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, 0),
    (else_try),
        (is_currently_night),
        (try_begin),
            # (this_or_next|eq, "$g_camp_mode", 1),#Camp rest?
            (eq, "$g_last_rest_center", "$current_town"),
            (assign, "$rest_up", 1),
        (else_try),
            (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),
            (neq, "$g_player_icon_state", pis_camping), #camp rest should add morale?
            (neq, "$g_player_icon_state", pis_ship), # in this game, generally not passengers
            (neq, "$g_player_besiege_town", "$g_encountered_party"),
            (neq, "$g_player_is_captive", 1),
            #(neg|key_is_down, key_space),
            (store_random_in_range, ":r",0,2),
            (eq, ":r", 0),
            (val_add, reg0, 1),
            (val_clamp, reg0, 0, 31),
            (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
            #minor recovery from not marching or fighting
        (else_try),
            (val_sub, reg0, 2),
            (val_max, reg0, 0),
            (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
        (try_end),
    (else_try),
        (neq, "$rest_up", 0),
        (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),
        (try_begin),
            #(lt, reg0, 3),
            (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, 0),
          # (else_try),
            # (val_div, reg0, 2),
            # (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, reg0),
        (try_end),
        (store_div, ":add_morale", reg0, 2),

        #add small bonus to current morale for "diversions" available in towns
        (try_begin),
            (ge, "$g_last_rest_center", 0),
            (this_or_next|party_slot_eq, "$g_last_rest_center", slot_party_type, spt_town),
            (this_or_next|party_slot_eq, "$g_last_rest_center", slot_party_type, spt_castle),
            (this_or_next|party_slot_eq, "$g_last_rest_center", slot_party_type, spt_latifundium),
            (party_slot_eq, "$g_last_rest_center", slot_party_type, spt_village),
            (val_add, ":add_morale", 1),
        (try_end),
        (display_message, "@Your troops feel refreshed from the night's rest."),
        (call_script, "script_change_player_party_morale", ":add_morale"),
        (assign, "$rest_up", 0),
    (else_try),
        (store_time_of_day, reg0),
        (is_between, reg0, 6, 8),
        (party_get_slot, reg0, "p_main_party", slot_party_unrested_morale_penalty),

        (try_begin),
            (gt, reg0, 4),  #more than 1 night without rest?
            (lt, reg0, 6),  #more than 1 night without rest?
            (display_message, "@Your men need rest or their morale will suffer.", color_bad_news),
        (try_end),
        (try_begin),
            (ge, reg0, 10),  #more than 1 night without rest?
            (display_message, "@Your men need rest or their morale will suffer.", color_bad_news),
        (try_end),
    (try_end),
]),

###forager camp system
(0, 0, 24,  #give food each 24 hours
  [
    (map_free), #en mapa
    (party_get_current_terrain, ":cur_terrain", "p_main_party"),
    (neq,":cur_terrain",rt_water),
    (neq,":cur_terrain",rt_bridge),
    (neq,":cur_terrain",rt_river),
    (eq, "$g_player_is_captive", 0),
    (eq, "$foragers_a", 1), #foragers ok
  ],
  [
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    (try_begin),
      (lt, ":num_men", 40), # if men = or less than 40, no forager
      (assign, "$foragers_a", 0),
    (else_try),
      #(ge, ":num_men", 40), # if men = or less than 40, no forager
      (store_free_inventory_capacity, ":inv_cap_a", "trp_player"),
      (gt, ":inv_cap_a", 3), #player need space free in inventory

      (assign, ":num_food", 0),
      (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
      (try_for_range, ":cur_inv_slot", 0, ":max_inv_slot"),
        (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
        (ge, ":cur_item", 0),
        (is_between, ":cur_item", food_begin, food_end),
        (val_add, ":num_food", 1), #player has food
      (try_end),
      (try_begin),
        (lt, ":num_food", 8), #system works when player have 8 or less food to advoid problems with villages to player if he has enough food
        #consequences = + food each 24 hours, possible problems with nearby villages -2 relation (30%)

        (store_random_in_range, ":random_chance", 0, 100), #differents options
        (try_begin),
          (ge, ":random_chance", 70), #success, food, no problems with villages
          (tutorial_box, "str_good_news_our_foragers_found_much_meat", "@Foragers"),
          (display_message, "str_good_news_our_foragers_found_much_meat", 0x00FF00),
          (troop_add_item, "trp_player","itm_cattle_meat",0),
          (try_begin),
            (ge, ":num_men", 200), # huge army = more food
            (troop_add_item, "trp_player","itm_cattle_meat",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 400), # total army = more food
            (troop_add_item, "trp_player","itm_cattle_meat",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 500), # total army = more food
            (troop_add_item, "trp_player","itm_cattle_meat",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 600), # total army = more food
            (troop_add_item, "trp_player","itm_cattle_meat",0),
          (try_end),
          (call_script, "script_change_player_party_morale", 2),
        (else_try),
          (ge, ":random_chance", 40), #success, food from villages
          (tutorial_box, "str_our_foragers_have_returned_after_getting_some_food", "@Foragers"),
          (display_message, "str_our_foragers_have_returned_after_getting_some_food", 0xFFFF00),
          (troop_add_item, "trp_player","itm_grain",0),
          (try_begin),
            (ge, ":num_men", 200), # huge army = more food
            (troop_add_item, "trp_player","itm_grain",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 400), # total army = more food
            (troop_add_item, "trp_player","itm_grain",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 500), # total army = more food
            (troop_add_item, "trp_player","itm_grain",0),
            (troop_add_item, "trp_player","itm_grain",0),
          (try_end),
          (try_begin),
            (ge, ":num_men", 600), # total army = more food
            (troop_add_item, "trp_player","itm_grain",0),
            (troop_add_item, "trp_player","itm_grain",0),
          (try_end),
          #reduce relacion con cada centro cercano chief
          (try_for_range, ":center", villages_begin, villages_end),
            (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center"),
            (lt,":cur_distance",15),
            (call_script, "script_change_player_relation_with_center", ":center", -2),
          (try_end),

        (else_try),
          (ge, ":random_chance", 3), #fail,  no food
          (tutorial_box, "str_bad_news_our_foragers_didnt_find_food_today", "@Foragers"),
          # (dialog_box,"@Bad news, our foragers don't found food today.")
          (display_message, "str_bad_news_our_foragers_didnt_find_food_today", 0xFF0000),
        (else_try),
          #disaster
          (tutorial_box, "str_very_bad_news_our_foragers_were_attacked", "@Foragers"),
          (display_message, "str_very_bad_news_our_foragers_were_attacked", 0xFF0000),
          (assign, "$foragers_a", 0), #no foragers until new orders
          (store_random_in_range, ":p_leave", 1, 3), #few number
          (assign, ":num_troops", ":p_leave"),
          (try_for_range, ":unused", 0, ":num_troops"),
            (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
]),

]#end of file
