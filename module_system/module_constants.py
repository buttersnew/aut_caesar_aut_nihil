from IDs.ID_items import *
from IDs.ID_quests import *
from IDs.ID_factions import *
from IDs.ID_parties import *
from IDs.ID_troops import *
from IDs.ID_strings import *

#from compiler import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4

slot_item_discovered               = 5

slot_item_amount_available         = 5

slot_item_urban_demand             = 6 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 7 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 8 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 9
slot_item_production_string        = 10

slot_item_tied_to_good_price       = 11 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 21
slot_item_positions_begin          = 23 #reserve around 5 slots after this



slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site			    = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost


slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values

slot_item_edible = 70

slot_item_has_commented            = 100

########################################################
##  AGENT SLOTS            #############################
########################################################

#general slots
slot_agent_target_entry_point     = 0
slot_agent_is_in_scripted_mode    = 1

#slots for moral code
slot_agent_is_running_away        = 2
slot_agent_courage_score          = 3
slot_agent_recently_decided       = 4

#battle feature slot
slot_agent_shieldbash_cooldown    = 5

shielbash_miss_cooldown = 2 #x2 = 2 seconds #12 seconds #before 2, now 30 = more time penalty. VC-2854
shielbash_hit_cooldown = 15 #x2 = 20 seconds # 30 seconds

#skirmish slots
slot_agent_make_dist_with_enemy    = 6
slot_agent_skirmish_direction      = 7
slot_agent_last_damage             = 8

#formation slots
slot_agent_formation_rank           = 9
slot_agent_inside_formation         = 10
slot_agent_nearest_enemy_agent      = 11
slot_agent_new_division             = 12
slot_agent_positioned               = 13
slot_agent_rank_closeness		    = 14

#tournament slots
slot_agent_tournament_point       = 15

slot_agent_arena_team_set         = 16
slot_agent_cur_animation          = 17
slot_agent_walker_occupation      = 18

#other slots
slot_agent_bought_horse           = 19
slot_agent_already_begg           = 20
slot_agent_fatiga                 = 21
slot_possessed                    = 22
slot_real_troop                   = 23
slot_horse_sprinting              = 24#only during horse race in olympics
slot_agent_race_state             = 25

#slots for retreat calculation
slot_agent_is_alive_before_retreat  = 26
slot_agent_is_not_reinforcement     = 27
slot_agent_map_overlay_id           = 28


slot_agent_has_commented            = 29# used for lords commenting on player

slot_agent_is_poisoned              = 30

slot_agent_is_blocked               = 31

########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_icon                       = 3
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5
slot_faction_ai_diplomatic_object       = 6 #Currently unused, can be linked to strings generated from decision checklists

slot_faction_marshall                   = 7
slot_faction_marshal = slot_faction_marshall
slot_faction_ai_offensive_max_followers = 8

slot_faction_culture                    = 9
slot_faction_leader                     = 10

slot_faction_temp_slot                  = 11

slot_faction_banner                     = 12

##diplomacy start+
slot_faction_number_of_parties    = 13#Deprecated, use slot_faction_num_parties instead
slot_faction_num_parties          = slot_faction_number_of_parties
##diplomacy end+
slot_faction_state                = 14

slot_faction_adjective            = 15


slot_faction_player_alarm         		= 16
slot_faction_last_mercenary_offer_time 	= 17
slot_faction_recognized_player    		= 18

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 19
slot_faction_quick_battle_tier_2_infantry      = 20
slot_faction_quick_battle_tier_1_archer        = 21
slot_faction_quick_battle_tier_2_archer        = 22
slot_faction_quick_battle_tier_1_cavalry       = 23
slot_faction_quick_battle_tier_2_cavalry       = 24

slot_faction_tier_1_troop         = 25
slot_faction_tier_2_troop         = 26
slot_faction_tier_3_troop         = 27
slot_faction_tier_4_troop         = 28
slot_faction_tier_5_troop         = 29

slot_faction_deserter_troop       = 30
slot_faction_guard_troop          = 31
slot_faction_messenger_troop      = 32
slot_faction_prison_guard_troop   = 33
slot_faction_castle_guard_troop   = 34

slot_faction_town_walker_male_troop      = 35
slot_faction_town_walker_female_troop    = 36
slot_faction_village_walker_male_troop   = 37
slot_faction_village_walker_female_troop = 38
slot_faction_town_spy_male_troop         = 39
slot_faction_town_spy_female_troop       = 40

slot_faction_has_rebellion_chance   = 41

slot_faction_instability            = 42 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
# slot_faction_war_damage_inflicted_when_marshal_appointed = 43 #Probably deprecate
# slot_faction_war_damage_suffered_when_marshal_appointed  = 44 #Probably deprecate

slot_faction_debts      = 43
slot_faction_treasury   = 44

slot_faction_political_issue            = 45 #Center or marshal appointment
slot_faction_political_issue_time       = 46 #Now is used

slot_faction_reinforcements_a        = 47
slot_faction_reinforcements_b        = 48
slot_faction_reinforcements_c        = 49

slot_faction_num_armies              = 50
slot_faction_num_castles             = 51
slot_faction_num_towns               = 52

slot_faction_last_attacked_center    = 53
slot_faction_last_attacked_hours     = 54
slot_faction_last_safe_hours         = 55

slot_faction_num_routed_agents       = 56

slot_faction_rebelling_against       = 57 # stores if a faction has active rebellion against other faction
#useful for competitive consumption
# slot_faction_biggest_feast_score      = 57
# slot_faction_biggest_feast_time       = 58
# slot_faction_biggest_feast_host       = 59

#Faction AI states
slot_faction_last_feast_concluded       = 60 #Set when a feast starts -- this needs to be deprecated
slot_faction_last_feast_start_time      = 61 #this is a bit confusing

slot_faction_ai_last_offensive_time 	= 62 #Set when an offensive concludes
slot_faction_last_offensive_concluded 	= 63 #Set when an offensive concludes

slot_faction_ai_last_rest_time      	= 64 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = 65 #

slot_faction_ai_last_decisive_event     = 66 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops      = 67
slot_faction_tributary_of	              = 68

slot_faction_parthian_expedition            = 69

#diplomacy
slot_faction_truce_days_with_factions_begin 			= 70 #we have 23 factions + player so at least 18
slot_faction_provocation_days_with_factions_begin 		= 100
slot_faction_war_damage_inflicted_on_factions_begin 	= 130
slot_faction_sum_advice_about_factions_begin 			= 160
slot_faction_neighbors_begin	                        = 190
##diplomacy start+ end-points for the ranges for iteration and range checks
slot_faction_truce_days_with_factions_end 			= slot_faction_provocation_days_with_factions_begin
slot_faction_provocation_days_with_factions_end 		= slot_faction_war_damage_inflicted_on_factions_begin
slot_faction_war_damage_inflicted_on_factions_end 	= slot_faction_sum_advice_about_factions_begin
slot_faction_sum_advice_about_factions_end			= slot_faction_neighbors_begin
##diplomacy end+



slot_faction_has_nor_titles                 = 221
slot_faction_player_tributary               = 222
slot_faction_government_type                = 223

gov_feudal   = 0
gov_imperial = 1
gov_republic = 2


dplmc_slot_faction_policy_time                = 224
dplmc_slot_faction_centralization             = 225
dplmc_slot_faction_aristocracy                = 226
dplmc_slot_faction_serfdom                    = 227
dplmc_slot_faction_quality                    = 228
dplmc_slot_faction_patrol_time                = 229
dplmc_slot_faction_mercantilism               = 230 # + mercantilism / - free trade

dplmc_slot_faction_policies_begin = dplmc_slot_faction_centralization #Define these for convenient iteration.  Requires them to be continuous.
dplmc_slot_faction_policies_end   = dplmc_slot_faction_mercantilism + 1


#Other slots
# #use faction slots to remember information between battles
slot_faction_d0_mem_formation           = 231
slot_faction_d0_mem_formation_space     = 241
slot_faction_d0_mem_relative_x_flag     = 251
slot_faction_d0_mem_relative_y          = 261

slot_faction_hire               = 262
slot_faction_wages              = 263
slot_faction_garrison           = 264
slot_faction_garrison_wages     = 265
slot_faction_spending_edicts    = 266
slot_faction_spending_admin     = 267
slot_faction_salary             = 268
slot_faction_spending_diplomacy = 269
slot_faction_taxes_govern       = 270
slot_faction_taxes_business     = 271
slot_faction_taxes_war          = 272
slot_faction_taxes_edicts       = 273
slot_faction_taxes_diplomacy    = 274
slot_faction_emperors_bocket    = 275
slot_faction_tax_rate           = 276
slot_faction_tax_rate_buisness  = 277
#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)

##diplomacy start+
#Treaty lengths.  Use these constants instead of "magic numbers" to make it
#obvious what code is supposed to do, and also make it easy to change the
#lengths without having to go through the entire mod.

# Truces (as exist in Native)
dplmc_treaty_truce_days_initial    = 25
dplmc_treaty_truce_days_expire     =  0

#Trade treaties convert to truces after 25 days.
dplmc_treaty_trade_days_initial    = 45
dplmc_treaty_trade_days_expire     = dplmc_treaty_truce_days_initial

#Defensive alliances convert to trade treaties after 20 days.
dplmc_treaty_defense_days_initial  = 65
dplmc_treaty_defense_days_expire   = dplmc_treaty_trade_days_initial

#Alliances convert to defensive alliances after 20 days.
dplmc_treaty_alliance_days_initial = 85
dplmc_treaty_alliance_days_expire  = dplmc_treaty_defense_days_initial

dplmc_treaty_tributary_days_initial = 165
dplmc_treaty_tributary_days_expire  = dplmc_treaty_alliance_days_initial

#Define these by name to make them more clear in the source code.
#They should not be altered from their definitions.
dplmc_treaty_truce_days_half_done = (dplmc_treaty_truce_days_initial + dplmc_treaty_truce_days_expire) // 2
dplmc_treaty_trade_days_half_done = (dplmc_treaty_trade_days_initial + dplmc_treaty_trade_days_expire) // 2
dplmc_treaty_defense_days_half_done = (dplmc_treaty_defense_days_initial + dplmc_treaty_defense_days_expire) // 2
dplmc_treaty_alliance_days_half_done = (dplmc_treaty_alliance_days_initial + dplmc_treaty_alliance_days_expire) // 2

##diplomacy end+

########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

slot_town_lord                 = 7
slot_party_ai_substate         = 8
# slot_town_claimed_by_player    = 9 # this slot number is free

slot_cattle_driven_by_player = slot_town_lord #hack

# slots used by parties which are not centers:
slot_cohort_1   =10
slot_cohort_2   =11
slot_cohort_3   =12
slot_cohort_4   =13
slot_cohort_5   =14
slot_cohort_6   =15
slot_cohort_7   =16
slot_cohort_8   =17
slot_cohort_9   =18
slot_cohort_10  =19
slot_cohort_11  =20
slot_cohort_12  =21
slot_cohort_13  =22
slot_cohort_14  =23
slot_cohort_15  =24

slot_cohort_begin   = slot_cohort_1
slot_cohort_end     = slot_cohort_15 +1

#this slots here are all only used by towns:
slot_town_center            = 10
slot_town_castle            = 11
slot_town_prison            = 12
slot_town_tavern            = 13
slot_town_store             = 14
slot_town_arena             = 15
slot_town_mastercraftman    = 16
slot_town_walls             = 17
slot_center_culture         = 18

slot_paganside_god          = slot_town_castle
slot_priest_troop           = slot_town_prison
slot_merchant_poor          = slot_town_tavern
slot_merchant_rich          = slot_town_store
slot_holy_side_event        = slot_town_arena

slot_town_tavernkeeper  = 19
slot_town_weaponsmith   = 20
slot_town_armorer       = 21
slot_town_merchant      = 22
slot_town_horse_merchant= 23
slot_town_elder         = 24
slot_center_player_relation = 25


##diplomacy start+ This range doesn't need to be exhaustive (e.g. the seneschal isn't included), but it should be continuous
# dplmc_slot_town_merchants_begin = slot_town_tavernkeeper
# dplmc_slot_town_merchants_end = slot_town_elder + 1
##diplomacy end+
slot_center_last_taken_by_troop              = 26

# party will follow this party if set:
slot_party_commander_party                   = 27 #default -1   #Deprecate
# slot_party_following_player                  = 28
slot_party_follow_player_until_time          = 29
# slot_party_dont_follow_player_until_time     = 30

slot_village_raided_by                      = 31
slot_village_state                          = 32 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress                  = 33
slot_village_recover_progress               = 34
slot_village_smoke_added                    = 35

slot_village_infested_by_bandits        = 36

slot_center_last_visited_by_lord        = 37

slot_center_last_player_alarm_hour      = 38

## Seatrade
slot_party_on_water                  	= 39
slot_party_port_party                   = 40
slot_town_port 					        = 41

slot_village_player_can_not_steal_cattle = 42

slot_center_accumulated_rents       = 43 #collected automatically by NPC lords
slot_center_accumulated_tariffs     = 44 #collected automatically by NPC lords
slot_town_wealth                    = 45 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity                = 46 #affects the amount of wealth generated
slot_town_player_odds               = 47

slot_party_last_toll_paid_hours         = 48
slot_party_food_store                   = 49 #used for sieges
slot_center_is_besieged_by              = 50 #used for sieges
slot_center_last_spotted_enemy          = 51

castle_food_days        = 8
town_food_days          = 12

slot_party_cached_strength        = 52
slot_party_nearby_friend_strength = 53
slot_party_nearby_enemy_strength  = 54
slot_party_follower_strength      = 55

# slot_town_reinforcement_party_template = 56
# #SB : alias for slot
# slot_village_reinforcement_party = slot_town_reinforcement_party_template

slot_center_original_faction           = 57
slot_center_ex_faction                 = 58

slot_party_follow_me                   = 59
slot_center_siege_begin_hours          = 60 #used for sieges
slot_center_siege_hardness             = 61

slot_center_sortie_strength            = 62
slot_center_sortie_enemy_strength      = 63

slot_party_last_in_combat              = 64 #used for AI
slot_party_last_in_home_center         = 65 #used for AI
slot_party_leader_last_courted         = 66 #used for AI
slot_party_last_in_any_center          = 67 #used for AI

slot_castle_exterior    = slot_town_center

#SB : training ground scene slots
slot_grounds_melee = slot_town_center
slot_grounds_track = slot_town_castle
slot_grounds_count = slot_town_prison
slot_grounds_trainer = slot_town_lord

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added

#slot_town_village_product = 76

#slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

###maybe I will add something like this for traveling, lets see
#(or a more detailed province system)
slot_center_province		      = 68
slot_center_statues 		      = 69

slot_center_statues_days 		  = 70
slot_party_time_service 		  = 71
slot_party_looted_left_days		  = 72

slot_town_arena_melee_mission_tpl = 73
slot_town_arena_torny_mission_tpl = 74
slot_town_arena_melee_1_num_teams = 75
slot_town_arena_melee_1_team_size = 76
slot_town_arena_melee_2_num_teams = 77
slot_town_arena_melee_2_team_size = 78
slot_town_arena_melee_3_num_teams = 79
slot_town_arena_melee_3_team_size = 80
slot_town_arena_melee_cur_tier    = 81
##slot_town_arena_template        = 87
# slot_num_hours_battle_icon_on_map	   = 82

# slot_center_npc_volunteer_troop_type   = 83
slot_center_peasant_troop_amount = 83
slot_center_mercenary_troop_amount_2 = 84

slot_center_mercenary_troop_type  = 85
slot_center_mercenary_troop_amount= 86
slot_center_volunteer_troop_type  = 87
slot_center_volunteer_troop_amount= 88

slot_center_ransom_broker         = 89
slot_center_tavern_traveler       = 90
slot_center_traveler_info_faction = 91
slot_center_tavern_bookseller     = 92
slot_center_tavern_minstrel       = 93

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 94
slot_party_looted_item_1          = 95
slot_party_looted_item_2          = 96
slot_party_looted_item_3          = 97
slot_party_looted_item_4          = 98
slot_party_looted_item_5          = 99
slot_party_looted_item_1_modifier = 100
slot_party_looted_item_2_modifier = 101
slot_party_looted_item_3_modifier = 102
slot_party_looted_item_4_modifier = 103
slot_party_looted_item_5_modifier = 104

slot_village_bound_center         = 105
slot_village_market_town          = 106
slot_village_farmer_party         = 107
slot_party_home_center            = 108 #Only use with caravans and villagers
slot_town_patrol_party            = slot_party_home_center #only used for towns

slot_party_last_traded_center     = 111
##center decrees: 0 means it is not issued, 1 means it is issued


slot_center_player_enterprise                     = 112 #noted with the item produced
slot_center_player_enterprise_production_order    = 113
slot_center_player_enterprise_days_until_complete = 114 #Used instead

slot_center_has_bandits                        = 115
slot_town_has_tournament                       = 116
slot_town_tournament_max_teams                 = 117
slot_town_tournament_max_team_size             = 118

slot_center_faction_when_oath_renounced        = 119

slot_center_walker_0_troop                   = 120
slot_center_walker_1_troop                   = 121
slot_center_walker_2_troop                   = 122
slot_center_walker_3_troop                   = 123
slot_center_walker_4_troop                   = 124
slot_center_walker_5_troop                   = 125
slot_center_walker_6_troop                   = 126
slot_center_walker_7_troop                   = 127
slot_center_walker_8_troop                   = 128
slot_center_walker_9_troop                   = 129

slot_center_walker_0_dna                     = 130
slot_center_walker_1_dna                     = 131
slot_center_walker_2_dna                     = 132
slot_center_walker_3_dna                     = 133
slot_center_walker_4_dna                     = 134
slot_center_walker_5_dna                     = 135
slot_center_walker_6_dna                     = 136
slot_center_walker_7_dna                     = 137
slot_center_walker_8_dna                     = 138
slot_center_walker_9_dna                     = 139

slot_center_walker_0_type                    = 140
slot_center_walker_1_type                    = 141
slot_center_walker_2_type                    = 142
slot_center_walker_3_type                    = 143
slot_center_walker_4_type                    = 144
slot_center_walker_5_type                    = 145
slot_center_walker_6_type                    = 146
slot_center_walker_7_type                    = 147
slot_center_walker_8_type                    = 148
slot_center_walker_9_type                    = 149

slot_village_give_goldcoin			          = 150
slot_center_inventory						  = 151


#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate
#slot 152 is free
slot_center_volunteer_noble_troop_amount = 152

slot_center_head_cattle             = 153 #dried meat, cheese, hides, butter
slot_village_number_of_cattle       = slot_center_head_cattle
slot_center_head_sheep		    	= 154 #sausages, wool
slot_center_head_horses		    	= 155 #horses can be a trade item used in tracking but which are never offered for sale

slot_center_acres_pasture           = 156 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster
slot_center_acres_grain		    	= 157 #grain
slot_center_acres_olives            = 158 #olives
slot_center_acres_vineyard		    = 159 #fruit
slot_center_acres_flax              = 160 #flax
slot_center_acres_dates			    = 161 #dates

slot_center_fishing_fleet		    = 162 #smoked fish
slot_center_salt_pans		        = 163 #salt

slot_center_apiaries       		    = 164 #honey
slot_center_silk_farms			    = 165 #silk
slot_center_kirmiz_farms		    = 166 #dyes

slot_center_iron_deposits           = 167 #iron
slot_center_fur_traps			    = 168 #furs

##new stuff
slot_center_soapstone_depositis	        = 169 #soapstone
slot_center_frankincense                = 170
slot_center_amber_deposits		        = 171 #amber
slot_center_walrus_fleet		        = 172 #ivory
slot_center_silver_deposits             = 173 #silver
slot_center_forest     			        = 174 #silver

slot_center_mills				    = 175 #bread
slot_center_breweries		  	    = 176 #ale
slot_center_wine_presses		    = 177 #wine
slot_center_olive_presses		    = 178 #oil

slot_center_linen_looms			    = 179 #linen
slot_center_silk_looms              = 180 #velvet
slot_center_wool_looms              = 181 #wool cloth

slot_center_pottery_kilns		    = 182 #pottery
slot_center_smithies			    = 183 #tools
slot_center_tanneries			    = 184 #leatherwork
slot_center_shipyards			    = 185 #naval stores - uses timber, pitch, and linen

slot_center_household_gardens       = 186 #cabbages

slot_production_sources_end         = 187
#187 is free


#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

slot_town_last_nearby_fire_time         = 188

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
slot_party_following_orders_of_troop        = 189
slot_party_orders_type				        = 190
slot_party_orders_object				    = 191
slot_party_orders_time				    	= 192

slot_party_temp_slot_1			            = 193 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion		    = 194 #move this up a bit

slot_party_unrested_morale_penalty          = 195    #motomataru chief morale addition

slot_town_trade_good_prices_begin 			= 196#we have 50 goods so 196 - 246 are slots for prices
##196 - 246 are slots for prices
##trade good prices go to 302 !!!!

dplmc_slot_party_mission_diplomacy            = 247

dplmc_slot_center_taxation                    = 248
##diplomacy start+ additional center slots
dplmc_slot_center_ex_lord                     = 249 #The last lord (not counting those who willingly transferred it)
dplmc_slot_center_original_lord               = 250 #The original lord
dplmc_slot_center_last_transfer_time          = 251 #The last time it was captured
dplmc_slot_center_last_attacked_time          = 252 #Last attempted raid or siege
dplmc_slot_center_last_attacker               = 253 #Last lord who attempted to raid or siege

slot_center_ongoing_rebellion               = 254
slot_center_auxilia 	                    = 255
slot_center_has_recently_rebelled 	        = 256

# 257 is free

slot_center_can_rebell                  = 258
slot_rebellion_target                   = 259

slot_crucified_slave_icon               = 260
slot_center_pursue		                = 261

# slot_center_old_lord_rebell		        = 262

slot_center_has_latifundium             = 263 ##player latifundium

##decrees for towns and castles
slot_center_decree_curfew	     		    = 264
slot_center_decree_control	     		    = 265
slot_center_decree_garbage_collection	    = 266
slot_center_decree_housing	     		    = 267
slot_center_decree_law_enforcement		    = 268
slot_center_decree_beggingban	   		    = 269

decree_cost	= 2000
####price slots go to 302

##extort options:
extort_tax          = 1
extort_toll         = 2
extort_concile      = 3
extort_end          = 4

slot_center_capital                 = 270
##Buildings:
slot_center_has_silver_mine         = 271 #village

slot_center_has_manor                = 272 #village
slot_center_has_fish_pond            = 273 #village
slot_center_has_watch_tower          = 274 #village
slot_center_has_school               = 275 #village
slot_center_has_iron_mine            = 276 #village
slot_center_change_culture_village   = 277  #village
slot_center_has_farms                = 278  #village
slot_center_has_cattle               = 279  #village
slot_center_has_trader               = 280  #village
slot_center_has_quarry               = 281  #village
slot_center_has_irigation            = 282  #village

slot_center_has_messenger_post       = 283 #town, castle, village
slot_center_has_guard                = 284 #town, castle, village
slot_center_has_fishport             = 285 #town, castle, village
slot_center_has_roads                = 286 #town, castle, village
slot_center_has_hosptial             = 287 #town, castle, village

slot_center_change_culture_town      = 288 #town, castle
slot_center_has_prisoner_tower       = 289 #town, castle
slot_center_has_fire_fighter         = 290 #town, castle
slot_center_has_training_grounds     = 291 #town, castle
slot_center_has_slave_market 	     = 292 #town, castle
slot_center_has_barracks             = 293 #town, castle
slot_center_has_sewers               = 294 #town, castle
slot_center_has_industry             = 295 #town, castle
slot_center_has_loom                 = 296 #town, castle
slot_center_has_smith                = 297 #town, castle
slot_center_has_port                 = 298 #town, castle
##this are player only buildinga
slot_center_has_forum   		     = 299 #town, castle
slot_center_has_theatre   		     = 300 #town, castle
slot_center_has_triumph   		     = 301 #town, castle
slot_center_has_water   		     = 302 #town, castle
slot_center_has_temple               = 303 #town, castle
slot_center_rome_rebuild             = 304 #rome only
slot_center_has_temple_god           = 305 #town, castle

 ## player only ends

slot_center_current_improvement     = 109
slot_center_improvement_end_hour    = 110
slot_center_current_improvement_2   = 306
slot_center_improvement_2_end_hour  = 307
#slot_center_has_blacksmith     = 351 #town, castle

village_improvements_begin 					 = slot_center_has_silver_mine
village_improvements_end         			 = slot_center_change_culture_town

walled_center_improvements_begin 			 = slot_center_has_messenger_post
walled_center_improvements_end               = slot_center_has_temple_god

number_of_buildings_town =    walled_center_improvements_end - walled_center_improvements_begin
number_of_buildings_village = village_improvements_end - village_improvements_begin

# slot_center_criminalraiting                                  = 367

slot_town_seneschal                                          = 308

slot_center_blockaded             = 310 #used for but a single value; global should be used
slot_center_blockaded_time        = 311 #used for but a single value; global should be used
slot_center_mantlets_placed       = 312 #used for but a single value; global should be used
slot_center_latrines              = 313 #used for but a single value; global should be used
slot_center_ladder_time           = 314 #used for but a single value; global should be used
slot_center_infiltration_type     = 315 #used for but a single value; global should be used
slot_center_starvation_time       = 316 #used for but a single value; global should be used

slot_party_messenger_time         = 317 #used for but a single value; global should be used
slot_donate_party                 = 318

# reused slots for fixing VC-1537 without breaking save games
slot_party_ai_state_backup 		= 319
slot_party_ai_object_backup 	= 320
slot_party_ai_behavior_backup   = 321
slot_party_ai_embarking_port 	= 322
slot_party_spawn_point          = 323


slot_center_disease               = 324

#use only prime numbers
disease_consumption_timer     = 2
disease_consumption           = 5

disease_slow_fever_timer      = 7
disease_slow_fever            = 10

disease_camp_fever_timer      = 12
disease_camp_fever            = 15

disease_plague_timer          = 16
disease_plague                = 20

disease_measles_timer         = 22
disease_measles               = 25

disease_smallpox_timer        = 27
disease_smallpox              = 30

disease_greatpoxpox_timer     = 32
disease_greatpoxpox           = 35

slot_center_event                 = 325
# event constants
#effects of catastrophic events will stay for two weeks, decrease tax revenue
event_earthquake_timer    =   97
event_earthquake          =   100

event_fire_timer          =   109
event_fire                =   110

event_drought_timer       =   116
event_drought             =   120

event_insects_timer       =   128
event_insects             =   130

event_conquered_timer     =   138
event_conquered           =   140

event_fire_of_rome_timer  =   165#
event_fire_of_rome        =   191#182 days, more than 2 years, 26 weeks in-game

event_good_harvest_timer  =   206#
event_good_harvest        =   209#

event_poor_harvest_timer  =   211#
event_poor_harvest        =   214#

event_mild_winter_timer  =   216#
event_mild_winter        =   219#

event_harsh_winter_timer  =   211#
event_harsh_winter        =   214#

# slots continue
slot_center_current_improvement_builder = 326
slot_center_current_improvement_2_builder = 327

slot_center_caravan_visits      = 328
slot_center_trader_visits       = 329

slot_town_trade_route_1           = 330
slot_town_trade_route_2           = 331
slot_town_trade_route_3           = 332
slot_town_trade_route_4           = 333
slot_town_trade_route_5           = 334
slot_town_trade_route_6           = 335
slot_town_trade_route_7           = 336
slot_town_trade_route_8           = 337
slot_town_trade_route_9           = 338
slot_town_trade_route_10          = 339
slot_town_trade_route_11          = 340
slot_town_trade_route_12          = 341
slot_town_trade_route_13          = 342
slot_town_trade_route_14          = 343
slot_town_trade_route_15          = 344
slot_town_trade_route_16          = 345
slot_town_trade_route_17          = 346
slot_town_trade_route_18          = 347
slot_town_trade_route_19          = 348
slot_town_trade_route_20          = 349
slot_town_trade_route_21          = 350
slot_town_trade_route_22          = 351
slot_town_trade_route_23          = 352
slot_town_trade_route_24          = 353
slot_town_trade_route_25          = 354
slot_town_trade_route_26          = 355
slot_town_trade_route_27          = 356
slot_town_trade_route_28          = 357
slot_town_trade_route_29          = 358
slot_town_trade_route_30          = 359
slot_town_trade_route_31          = 360

slot_town_sea_trade_route_1           = 362
slot_town_sea_trade_route_2           = 363
slot_town_sea_trade_route_3           = 364
slot_town_sea_trade_route_4           = 365
slot_town_sea_trade_route_5           = 366
slot_town_sea_trade_route_6           = 367
slot_town_sea_trade_route_7           = 368
slot_town_sea_trade_route_8           = 369
slot_town_sea_trade_route_9           = 370
slot_town_sea_trade_route_10          = 371
slot_town_sea_trade_route_11          = 372
slot_town_sea_trade_route_12          = 373
slot_town_sea_trade_route_13          = 374
slot_town_sea_trade_route_14          = 375
slot_town_sea_trade_route_15          = 376


dplmc_slot_party_origin              = 377
dplmc_slot_party_mission_parameter_1 = 378
dplmc_slot_party_mission_parameter_2 = 379

# recruiter kit begin
# dplmc_slot_party_recruiter_needed_recruits         = 377           # Amount of recruits the employer ordered.
# dplmc_slot_party_recruiter_origin                  = 378                    # Walled center from where the recruiter was hired.
# dplmc_slot_village_reserved_by_recruiter           = 379             # This prevents recruiters from going to villages targeted by other recruiters.
# dplmc_slot_party_recruiter_needed_recruits_faction = 380   # Alkhadias Master, you forgot this one from the PM you sent me :D

slot_cohort_town_1   =381
slot_cohort_town_2   =382
slot_cohort_town_3   =383
slot_cohort_town_4   =384
slot_cohort_town_5   =385
slot_cohort_town_6   =386
slot_cohort_town_7   =387
slot_cohort_town_8   =388
slot_cohort_town_9   =389
slot_cohort_town_10  =390
slot_cohort_town_11  =391
slot_cohort_town_12  =392
slot_cohort_town_13  =393
slot_cohort_town_14  =394
slot_cohort_town_15  =395
slot_cohort_town_16  =396
slot_cohort_town_17  =397
slot_cohort_town_18  =398
slot_cohort_town_19  =399
slot_cohort_town_20  =400
slot_cohort_town_21  =401
slot_cohort_town_22  =402
slot_cohort_town_23  =403
slot_cohort_town_24  =404
slot_cohort_town_25  =405

slot_cohort_town_begin   = slot_cohort_town_1
slot_cohort_town_end     = slot_cohort_town_25 +1

##diplomacy start+ Re-use those slots for other party types

##diplomacy end+

# dplmc_slot_town_trade_route_last_arrival_1        = 381
# dplmc_slot_town_trade_route_last_arrival_2        = 382
# dplmc_slot_town_trade_route_last_arrival_3        = 383
# dplmc_slot_town_trade_route_last_arrival_4        = 384
# dplmc_slot_town_trade_route_last_arrival_5        = 385
# dplmc_slot_town_trade_route_last_arrival_6        = 386
# dplmc_slot_town_trade_route_last_arrival_7        = 387
# dplmc_slot_town_trade_route_last_arrival_8        = 388
# dplmc_slot_town_trade_route_last_arrival_9        = 389
# dplmc_slot_town_trade_route_last_arrival_10        = 390
# dplmc_slot_town_trade_route_last_arrival_11        = 391
# dplmc_slot_town_trade_route_last_arrival_12        = 392
# dplmc_slot_town_trade_route_last_arrival_13        = 393
# dplmc_slot_town_trade_route_last_arrival_14        = 394
# dplmc_slot_town_trade_route_last_arrival_15        = 395
# dplmc_slot_town_trade_route_last_arrival_16        = 396
# dplmc_slot_town_trade_route_last_arrival_17        = 397
# dplmc_slot_town_trade_route_last_arrival_18        = 398
# dplmc_slot_town_trade_route_last_arrival_19        = 399
# dplmc_slot_town_trade_route_last_arrival_20        = 400
# dplmc_slot_town_trade_route_last_arrival_21        = 401
# dplmc_slot_town_trade_route_last_arrival_22        = 402
# dplmc_slot_town_trade_route_last_arrival_23        = 403
# dplmc_slot_town_trade_route_last_arrival_24        = 404
# dplmc_slot_town_trade_route_last_arrival_25        = 405
# dplmc_slot_town_trade_route_last_arrival_26        = 406
# dplmc_slot_town_trade_route_last_arrival_27        = 407
# dplmc_slot_town_trade_route_last_arrival_28        = 408
# dplmc_slot_town_trade_route_last_arrival_29        = 409
# dplmc_slot_town_trade_route_last_arrival_30        = 410
# dplmc_slot_town_trade_route_last_arrival_31        = 411
# dplmc_slot_town_trade_route_last_arrivals_begin    = dplmc_slot_town_trade_route_last_arrival_1
# dplmc_slot_town_trade_route_last_arrivals_end      = dplmc_slot_town_trade_route_last_arrival_31 + 1

# dplmc_slot_village_trade_last_returned_from_market = dplmc_slot_town_trade_route_last_arrival_1#overlaps with dplmc_slot_town_trade_route_last_arrival_1
# dplmc_slot_village_trade_last_arrived_to_market    = dplmc_slot_town_trade_route_last_arrival_2#overlaps with dplmc_slot_town_trade_route_last_arrival_2

slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_31 + 1
slot_town_sea_trade_routes_begin = slot_town_sea_trade_route_1
slot_town_sea_trade_routes_end = slot_town_sea_trade_route_15 + 1

num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin          = 415 #a harmless number, until it can be deprecated


# slot_center_last_reconnoitered_by_faction_time  = 515 #this generates a list

#slot_party_type values
##spt_caravan            = 1
spt_castle                  = 2
spt_town                    = 3
spt_village                 = 4

spt_patrol                  = 5
spt_messenger               = 6
spt_scout                   = 7

spt_kingdom_caravan         = 8
dplmc_spt_recruiter         = 9
spt_kingdom_hero_party      = 10

spt_merchant_caravan        = 11     #Seatrader
spt_village_farmer          = 12
spt_ship                    = 13
spt_cattle_herd             = 14
spt_bandit_lair             = 15

dplmc_spt_gift_caravan      = 16
spt_player_camp             = 17 #
spt_latifundium             = 18
spt_companion_raider	    = 19
spt_prisoner_train          = 20
spt_rebellion               = 21
spt_paganholyside           = 22
spt_minor_faction_raiders   = 23

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4

#slot_faction_ai_state values
sfai_default                   		 = 0 #also defending
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present

#Rebellion system changes begin
sfai_nascent_rebellion          = 7
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages
spai_starting_raid              = 17

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2

#################################
#### LATIFUNIDUM
##other slots
slot_lat_doctor               = 214
slot_lat_mercenary_amount     = 215
slot_lat_mercenary_type       = 216
slot_lat_deity     = 217
slot_lat_teacher   = 218
##buildings begin
slot_lat_silk      = 219
slot_lat_vineyard  = 220
slot_lat_winepress = 221
slot_lat_oilpress  = 222
slot_lat_oilgrove  = 223
slot_lat_smith     = 224
slot_lat_cattle    = 225
slot_lat_butcher   = 226
slot_lat_fishery   = 227
slot_lat_fruits    = 228
slot_lat_bakery    = 229
slot_lat_temple    = 230
slot_lat_deco      = 231
slot_lat_barracks  = 232
slot_lat_guards    = 233
slot_lat_wall      = 234
slot_lat_pottery   = 235
slot_lat_sheep     = 236
slot_lat_horse     = 237
slot_lat_tanner    = 238
slot_lat_cheeser   = 239
slot_lat_weaver    = 240
slot_lat_camp      = 241
slot_lat_inn       = 242
slot_lat_merchant  = 243
#sheep
#wool looms
#leather
slot_lat_building_end      = 244
####END latifundium
###############################

########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0

########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free
#slot_troop_homage_type         = 45
#homage_mercenary =             = 1 #Player is on a temporary contract
#homage_official =              = 2 #Player has a royal appointment
#homage_feudal   =              = 3 #


slot_troop_state               = 3
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

slot_troop_influence = 6

slot_troop_party_template      = 6#Nero: seems to be unused
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

##slot_troop_is_prisoner         = 8  # important for heroes only
slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_present_at_event    = 9

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14 # for pretenders

#slot 15-17 are free
#16-17 are only used by the banner troop for the custom banner
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures
slot_troop_player_order_state   = 16 #Deprecated
slot_troop_player_order_object  = 17 #Deprecated

#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that

#Post 0907 changes begin
slot_troop_age                 =  18
slot_troop_age_appearance      =  19 # Nero: seems to be unused

slot_troop_unhealth              =  20

#used for player crafting items
slot_crafting_order_time            = slot_troop_age
slot_crafting_order_time_modifier   = slot_troop_age_appearance
slot_crafting_order_item            = slot_troop_player_order_object

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22

slot_troop_religion            = 23
##germanic gods
# worships_baduhenna 		= 1	#goddess of war (strength, agility, power_strike, power_throw, power_draw)
# worships_dunraz 		= 2 #god of smithing, prodection on the battlefield (agility, intelligent, engineering, ironflesh)
# worships_frijo 			= 3 #goddes of life, prodection
# ##roman and greek gods
# worships_vest 			= 4 #goddes of life, prodection
# worships_saturn	 		= 5 #god of agriculture
# worships_castor_pollux 	= 6 #navigation (pathfinding etc)
# worships_aphrodite 		= 7 #beauty sexuality
# worships_mars 			= 8 #god of war
# worships_jupiter 		= 9 #helps you to lead and govern

# slot_troop_conv 							 = 185 # conversion attempted 0-initial state, 1-tried&failed 2-converted
#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that
#Gods of war:
worships_baduhenna = 1
worships_mars 	= 2
#Gods of crafting:
worships_dunraz	= 3
#Gods of prodection:
worships_frijo	= 4
worships_vest	= 5
#Gods of agriculture:
worships_saturn	= 6
#Gods of Beauty
worships_aphrodite	    = 7
#King of the gods
worships_jupiter	    = 8
#god of navigation:
worships_castor_pollux	= 9
##christus:
worships_christus 		= 10
##judea
worships_yhwhe 		    = 11
##alcis
worships_alcis          = 12
#mithras
worships_mithras        = 13

#celtic
worships_andraste   = 14
worships_maponos    = 15

#dacian
worships_gebeleizis = 16
worships_zalmoxis   = 17

#sarmatian
worships_goitosuros = 18
worships_artimpasa  = 19

#caucasian
worships_mihr       = 20
worships_armazi     = 21

#persian
worships_mazda      = 22

#arabian
worships_allat      = 23

#african
worships_ifri       = 24

#lybian
worships_ammon      = 25

#nubian
worships_apedemak   = 26

small_sacrifice_percentage = 2
medium_sacrifice_percentage = 5
large_sacrifice_percentage = 10
huge_sacrifice_percentage = 15

small_sacrifice_cost = 1000
medium_sacrifice_cost = 5000
large_sacrifice_cost = 10000
huge_sacrifice_cost = 25000
#####################################
#
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

#olympia slots for organiser
won_horse = 30
won_mule  = 31
won_throwing  = 32
won_fighting  = 33
won_running_tunic  = 34
won_running_hoplit  = 35
won_throwing_2       = 36
current_opponent_1  = 37
rest_olympia        = 38
olympia_progress    = 39
olympia_auto_menu    = 40
olympia_easter_egg    = 41

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
	##diplomacy start+
	#NOTE TO MODDERS: There is code that depends on these slots appearing in the correct order and being continuous.
dplmc_slot_troop_relatives_begin = slot_troop_spouse
dplmc_slot_troop_relatives_end   = slot_troop_betrothed
dplmc_slot_troop_relatives_including_betrothed_end = slot_troop_betrothed + 1
	##diplomacy end+
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38#has to be the same as slot_lord_granted_courtship_permission
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding


##trainer slots
slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36

slot_lady_used_tournament				     = 40
slot_troop_lover							 = 41
slot_troop_lover_attempt			         = 42
slot_troop_lover_found				         = 43
slot_troop_temp							     = 44
slot_troop_current_rumor         = 45
slot_troop_temp_slot             = 46
slot_troop_promised_fief         = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
slot_player_battle_event              = 52 #reputation type is not used for player
slot_lord_reputation_type             = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55

##diplomacy start+ Use this slot to track owned center points (village = 1, castle = 2, town = 3)
#The value should be one more than the actual number of center points, because it makes
#it obvious when the slot has not been initialized.  (It also so happens that we often
#add 1 to the value anyway to avoid division by 0, so this can be convenient.)
dplmc_slot_troop_center_points_plus_one = 56
##diplomacy end+

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate
slot_troop_kill_count  = 57
slot_troop_wound_count = 58
# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5
tmt_casualties = 6#new: only triggered for high casualities

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions

#courtship slots
slot_lady_courtship_heroic_recited      = 74
slot_lady_courtship_allegoric_recited   = 75
slot_lady_courtship_comic_recited       = 76
slot_lady_courtship_mystic_recited      = 77
slot_lady_courtship_tragic_recited      = 78
slot_troop_refused  					= 79

#NPC history slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4
##diplomacy start+
dplmc_pp_history_appointed_office    = 5 #assigned an office (like Minister)
dplmc_pp_history_granted_fief        = 6 #was granted a fief, or (for pretenders) completed Pretender quest
dplmc_pp_history_lord_rejoined       = 7 #enfeoffed lord temporarily rejoined the party
dplmc_pp_history_nonplayer_entry     = 8 #became a lord without first being a companion of the player (normally this is assumed to be impossible)
##diplomacy end+

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro 						= 101
slot_troop_intro_response_1 			= 102

slot_player_embezzeled_founds           = 102 #use this instead of a global
slot_player_takes_money_from_treasury   = 103

slot_troop_intro_response_2 			= 103
slot_troop_backstory_a 					= 104
slot_troop_backstory_b 				  	= 105
slot_troop_backstory_c 				  	= 106
slot_troop_backstory_delayed 		    = 107
slot_troop_backstory_response_1 		= 108
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b    = 119
slot_troop_personalityclash2_speech     = 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 		    = 124
slot_troop_rehire_speech 			    = 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	      = 137
slot_troop_fief_acceptance_string	      = 138
slot_troop_woman_to_woman_string	      = 139
slot_troop_turn_against_string	          = 140

slot_troop_strings_end 					  = 141

slot_troop_payment_request 				  = 141

#141, support base removed, slot now available

slot_troop_kingsupport_state			  = 142
slot_troop_kingsupport_argument			= 143
slot_troop_kingsupport_opponent			= 144
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 146
slot_troop_ally_routed_agents                   = 147
slot_troop_enemy_routed_agents                  = 148

#Special quest slots
slot_troop_mission_participation        = 149
mp_unaware                              = 0
mp_stay_out                             = 1
mp_prison_break_fight                   = 2
mp_prison_break_stand_back              = 3
mp_prison_break_escaped                 = 4
mp_prison_break_caught                  = 5

slot_troop_days_on_mission		            = 150
slot_troop_current_mission			        = 151
slot_troop_mission_object                   = 152

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# These are troops slots
##diplomacy start+ Altered because 154 is slot_troop_stance_on_faction_issue.
#(Companions can become lords, so parts of the auto-loot system had undesired consequences for promoted companions.)
dplmc_slot_upgrade_armor = 153 #was 153 before Diplomacy 4.0
dplmc_slot_upgrade_horse = 154 #was 154 before Diplomacy 4.0
##diplomacy end+
dplmc_slot_upgrade_wpn_0 = 155
dplmc_slot_upgrade_wpn_1 = 156
dplmc_slot_upgrade_wpn_2 = 157
dplmc_slot_upgrade_wpn_3 = 158
# This is an item slot
dplmc_slot_item_difficulty = 5
#### Autoloot improved by rubik begin
dplmc_slot_item_head_armor      = 6
dplmc_slot_item_body_armor      = 7
dplmc_slot_item_leg_armor       = 8

# slots redefine, no need to create more new slots, 3 is enough
dplmc_slot_item_thrust_damage      = dplmc_slot_item_head_armor
dplmc_slot_item_swing_damage       = dplmc_slot_item_body_armor
dplmc_slot_two_handed_one_handed   = dplmc_slot_item_leg_armor

dplmc_slot_item_horse_speed        = dplmc_slot_item_head_armor
dplmc_slot_item_horse_armor        = dplmc_slot_item_body_armor

dplmc_slot_item_shield_size        = dplmc_slot_item_head_armor
dplmc_slot_item_shield_armor       = dplmc_slot_item_body_armor

##diplomacy start+ slots redefined, re-use for rubik "auto buy food"
dplmc_slot_item_food_portion       = dplmc_slot_item_leg_armor

##New slot needed for rubik's Auto-Sell
dplmc_slot_item_type_not_for_sell  = 71
##diplomacy end+
dplmc_wpn_setting_1                 = 1
dplmc_wpn_setting_2                 = 2
dplmc_armor_setting                 = 3
dplmc_horse_setting                 = 4
dplmc_loot_string = 30  #SB : string register to start recording loot changes
###################################################################################
# End Autoloot
###################################################################################


slot_troop_will_join_prison_break      = 159

dplmc_slot_troop_mission_diplomacy            = 160
dplmc_slot_troop_mission_diplomacy2           = 161
dplmc_slot_troop_political_stance             = 162 #dplmc+ deprecated, see note below
##diplomacy start+
#Though you may assume otherwise from the name,  dplmc_slot_troop_political_stance is
#actually used as a temporary slot (it's overwritten every time you start a conversation
#with your chancellor about who supports whom, and in Diplomacy 3.3.2 it isn't used
#elsewhere).
#   I'm giving it a new name to reflect its use, to avoid confusion.
dplmc_slot_troop_temp_slot                    = 163 #replaces dplmc_slot_troop_political_stance
##diplomacy end+
dplmc_slot_troop_affiliated                   = 164 ##notes: 0 is default, 1 is asked; on newer games 3 is affiliated and 4 is betrayed

# slot_troop_marriage_time 				      = 165
slot_troop_triumph_points                = 165

triumph_threshold = 800

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.
#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek
slot_troop_controversy                     = 166 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type 	           = 167 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 168 #to whom it happened
slot_troop_recent_offense_time             = 169
slot_troop_stance_on_faction_issue         = 170 #when it happened

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

##npc missions
slot_troop_mission_target				        = 171
slot_troop_mission_amount				        = 172
##all mission types
npc_mission_kingsupport					        = 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8
dplmc_npc_mission_war_request                 = 9
dplmc_npc_mission_alliance_request            = 10
dplmc_npc_mission_spy_request                 = 11
dplmc_npc_mission_gift_fief_request           = 12
dplmc_npc_mission_gift_horses_request         = 13
dplmc_npc_mission_threaten_request            = 14
dplmc_npc_mission_prisoner_exchange           = 15
dplmc_npc_mission_defensive_request           = 16
dplmc_npc_mission_trade_request               = 17
dplmc_npc_mission_nonaggression_request       = 18
dplmc_npc_mission_persuasion                  = 19
dplmc_npc_mission_rescue_prisoner             = 20 #SB : added for quest, using slot_troop_town_with_contacts
npc_mission_deliver_message_secede				        = 21
npc_mission_deliver_message_leave_faction		        = 22
npc_mission_deliver_message_send_troops			        = 23
npc_mission_deliver_message_improve_relation	        = 24
npc_mission_improve_relations         			        = 25
npc_mission_beat_someone_up          		            = 26
npc_mission_foederati_request					        = 27
npc_mission_spy_on_spouse					        	= 28
npc_mission_on_patrol						            = 29
npc_mission_bring_money							        = 30
npc_mission_stage_border							    = 31
npc_mission_stage_revolt							    = 32
npc_mission_resupply 							        = 33
npc_mission_followers 							        = 34
npc_mission_mercs 							            = 35
npc_mission_tributary 							        = 36
npc_mission_improve_influence                           = 37

slot_troop_flirted_with           	        = 173
slot_troop_tortured 					    = 174

slot_troop_assassin_attempt				    = 175
# slot_troop_player_knows					    = 176

##these slots are used for romans only
slot_troop_govern                 = 177
slot_troop_legion                 = 178
slot_troop_aux                    = 179

# slot_troop_courtesan              = 180
slot_troop_traits                   = 180

trait_triumphator = 1

slot_troop_tortured_by 					= 181

slot_troop_recently_blamed				= 182
slot_troop_culture						= 183
slot_troop_bachus						= 184

slot_troop_loses						= 185
slot_troop_loses_wife					= 186
slot_troop_loses_lover				    = 187
slot_troop_paid_taxes             = 188
slot_troop_honorary_title         = 189
slot_troop_money_to_center        = 190

slot_troop_service_time        = 191
slot_troop_last_busines        = 192

ht_censor     = 4
ht_consul     = 3
ht_aedil      = 2
ht_quaestor   = 1

#troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change
slot_troop_relations_begin				= -150

#this creates an array for relations between troops
#it starts with the id of trp_npc1, which is currently and run to where lords end
##lords start at 437 and run to 807

########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39


########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0

#Rebellion changes end
# character backgrounds
cb_ceres = 1
cb_diana = 2
cb_minerva = 3
cb_mars = 4
cb_mercurius = 5
cb_jupiter = 6

#NPC system changes end
#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game

slto_kingdom_hero       = 2

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
# slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
# slto_inactive_pretender = 9 disabled pretenders


stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement      = 11

#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end
##diplomacy start+

#These constants are not (yet) used, but they are defined so that other mods can
#extend diplomacy in a consistent way, and have confidence that base diplomacy
#will correctly respect the flags they set.

#Note that the existing code assumes that dplmc_slto_exile and dplmc_slto_dead are
#greater than slto_retirement.  If you had to change this, look around for every instance
#where diplomacy checks "troop_slot_ge" slto_retirement, and expand it to also check
#dead, exiled, etc.

dplmc_slto_exile           = 14 #Set for newly exiled lords.  In saved games, this is retroactively applied (once only).
dplmc_slto_dead            = 15 #not normally set
dplmc_slto_heir            = 16 #heir of player
##diplomacy end+

########################################################
##  QUEST SLOTS            #############################
########################################################
slot_quest_thunder_dont_give_again  = 1
slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14

slot_quest_object_faction           = 15

slot_quest_freelancer_payment        = 8
slot_quest_freelancer_agent_spawned  = 9
slot_quest_freelancer_agent_limit    = 10
slot_quest_freelancer_pretorian      = 11
slot_quest_freelancer_service_length = 12
slot_quest_freelancer_progress_limit = 13
slot_quest_freelancer_progress       = 14
slot_quest_freelancer_rank           = 15
slot_quest_freelancer_state          = 16
slot_quest_freelancer_event          = 17
slot_quest_freelancer_event_2        = 18
slot_quest_freelancer_kill           = 19
slot_quest_freelancer_treatment      = 20
slot_quest_freelancer_mission_1      = 21
slot_quest_freelancer_mission_2      = 22


slot_freelancer_equip_start        = 28

slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot      			= 27

slot_quest_timer                    = 28

slot_quest_main_poppaea_knows       = slot_quest_gold_reward

main_story_poppaea_knows_nothing = 0
main_story_poppaea_knows_all = 1
main_story_poppaea_knows_little = 2

slot_quest_main_poppaea_fate        = slot_quest_target_item
slot_quest_main_poppaea_timer       = slot_quest_object_faction
slot_quest_main_antonia_or_poppaea  = slot_quest_giver_center

# Phaiak begin
slot_quest_menu_1					= 31
slot_quest_menu_2					= 32
slot_quest_menu_3					= 33
slot_quest_menu_4					= 34
slot_quest_menu_5					= 35
slot_quest_menu_6					= 36
slot_quest_menu_7					= 37
slot_quest_menu_8					= 38
slot_quest_menu_9					= 39
slot_quest_menu_10					= 40
slot_quest_menu_11					= 41
slot_quest_menu_12					= 42
slot_quest_menu_13					= 43
slot_quest_menu_14					= 44
slot_quest_menu_15					= 45
slot_quest_menu_16					= 46
slot_quest_menu_17					= 47
slot_quest_menu_18					= 48
slot_quest_menu_19					= 49
slot_quest_menu_20					= 50
slot_quest_menu_21					= 51
slot_quest_menu_22					= 52
slot_quest_menu_23					= 53
slot_quest_menu_24					= 54
slot_quest_menu_25					= 55

# wound system
slot_quest_int_penalty_left_days = slot_quest_menu_1
slot_quest_cha_penalty_left_days = slot_quest_menu_2
slot_quest_str_penalty_left_days = slot_quest_menu_3
slot_quest_agi_penalty_left_days = slot_quest_menu_4
slot_quest_end_penalty_left_days = slot_quest_menu_5

slot_quest_int_penalty_fluid_points = slot_quest_menu_11
slot_quest_cha_penalty_fluid_points = slot_quest_menu_12
slot_quest_str_penalty_fluid_points = slot_quest_menu_13
slot_quest_agi_penalty_fluid_points = slot_quest_menu_14
slot_quest_end_penalty_fluid_points = slot_quest_menu_15

slot_quest_int_penalty_perma_points = slot_quest_menu_21
slot_quest_cha_penalty_perma_points = slot_quest_menu_22
slot_quest_str_penalty_perma_points = slot_quest_menu_23
slot_quest_agi_penalty_perma_points = slot_quest_menu_24
slot_quest_end_penalty_perma_points = slot_quest_menu_25



########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1

slot_party_template_lair_type    	 	= 3
slot_party_template_lair_party    		= 4
slot_party_template_lair_spawnpoint     = 5

slot_party_template_lair_next_spawn = 6


# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6
scene_prop_timer					          = 7

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk                 = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden                     = 16
tc_courtship                  = 16
tc_after_duel                 = 17
tc_prison_break               = 18
tc_escape                     = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21

tc_camp_talk          		  = 22#camp scene
tc_player_defeated            = 23
tc_permanent_camp_talk        = 24#camp scene
tc_feast					  = 25##for feasts in your villa in neapolis
tc_campaign_talk			  = 26##if player has other lords attached to his party

##used for freelancer special event dialogues
tc_marshing_camp			        = 27
tc_last_promotion			        = 28
tc_promotion_optio			        = 29
tc_camp_training			        = 30
tc_camp_training_2            = 31
tc_freelancer_event_1         = 32
tc_freelancer_event_2         = 33
tc_freelancer_event_3         = 34
tc_freelancer_event_4         = 35
tc_octavia_event_1            = 36
tc_octavia_event_2            = 37
tc_pret_event_1               = 38
tc_pret_event_2               = 39
tc_pret_event_3               = 40
tc_pret_event_14              = 41
tc_girl_talk                  = 42

#new parthian thundergod quest
tc_thunder_god_talk            = 41

tc_avaritia_talk               = 42
tc_mission_1_talk              = 43

tc_poppaea_event_1          = 44
tc_poppaea_event_2          = 45

tc_main_story_fleet         = 46

#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants           = 4

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance                     = 21
logent_liege_grants_fief_to_vassal            = 22


logent_renounced_allegiance      = 23

logent_player_claims_throne_1    		               = 24
logent_player_claims_throne_2    		               = 25


logent_troop_feels_cheated_by_troop_over_land		   = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                  	   = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshall_appointment			   = 32
logent_lord_blames_defeat						   	   = 33

logent_player_suggestion_succeeded					   = 35
logent_player_suggestion_failed					       = 36

logent_liege_promises_fief_to_vassal				   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43

logent_game_start                           = 45
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip

logent_lady_and_suitor_break_engagement		  = 60
logent_lady_marries_suitor				          = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation             = 80
logent_policy_ruler_ignores_provocation                     = 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon                    = 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war                          = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity          = 91
logent_faction_declares_war_to_regain_territory             = 92
logent_faction_declares_war_to_curb_power                   = 93
logent_faction_declares_war_to_respond_to_provocation       = 94
##diplomacy begin
logent_faction_declares_war_to_fulfil_pact                  = 95
logent_faction_declares_war_to_declare_independence         = 96
logent_faction_declares_war_to_end_civil_war                = 97
logent_war_declaration_types_end                            = 98
##diplomacy end
logent_player_renamed_capital = 97 #SB : unused logged event

logent_player_attacked_buisness = 98
logent_player_helped_buisness   = 99
logent_battle_of_bedriacum      = 100

logent_raided_delphi            = 101

logent_triumph                  = 102

# logent_executed_prisoners = 97
# logent_rejected_bodyguards = 98

#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0

#lords/kings
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

#companions
lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#ladies
lrep_conventional    = 11 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 12 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 13 #Prone to mysticism, romantic.
lrep_ambitious       = 14 #Lady Macbeth
lrep_moralist        = 15 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa
lrep_end             = 16 #end of reputation slots


#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
	#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times

##diplomacy start+
#Define these for clarity and convenience elsewhere
dplmc_lrep_ladies_begin = lrep_conventional
dplmc_lrep_ladies_end = lrep_moralist + 1

dplmc_lrep_commoners_begin = lrep_roguish
dplmc_lrep_commoners_end = dplmc_lrep_ladies_begin

dplmc_lrep_nobles_including_liege_begin = lrep_none
dplmc_lrep_nobles_begin = lrep_martial
dplmc_lrep_nobles_end = dplmc_lrep_commoners_begin
##diplomacy end+

courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire)
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated

#Troop Commentaries end

# tutorial_fighters_begin = "trp_tutorial_fighter_1"
# tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types:
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers 		   = 8
town_walker_entries_start  = 32

##now only used for recruitment of centers with center wealth, see simple triggers
# reinforcement_cost_easy = 1200
# reinforcement_cost_moderate = 1100
# reinforcement_cost_hard = 1000

reinforcement_cost_celts    = 2000
reinforcement_cost_romans   = 3500
reinforcement_cost_eastern  = 3000
reinforcement_cost_germans  = 2000
reinforcement_cost_stepp    = 2000
reinforcement_cost_dacian   = 2500

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 37


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

##diplomacy start+
cultures_begin = "fac_culture_1"
cultures_end   = "fac_player_faction"
##diplomacy end+

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

minor_kingdoms_begin = "fac_garamantes"
minor_kingdoms_end = "fac_minor_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

quick_battle_kingdoms_begin = "fac_kingdom_1"
quick_battle_kingdoms_end = "fac_kingdom_8"

bandits_begin = "trp_looter"
bandits_end = "trp_follower_woman"

follower_troops_begin = "trp_follower_woman"
follower_troops_end = "trp_town_walker_1"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

# pretenders_begin = "trp_kingdom_1_pretender"
# pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = "trp_knight_1_1_wife"

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

minor_kings_begin = "trp_slavic_king"
minor_kings_end = "trp_gaetulian_queen"

minor_queens_begin = minor_kings_end
minor_queens_end   = "trp_arab_richmerchant"

companions_begin = "trp_npc1"
companions_end = kings_begin

seneschal_begin = "trp_town_1_seneschal"
seneschal_end = "trp_town_1_arena_master"

special_roman_merchants_begin = "trp_merchant1"
special_roman_merchants_end = "trp_merchant5"

special_eastern_merchants_begin = "trp_merchant5"
special_eastern_merchants_end = "trp_prisoner"

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

kingdom_heroes_begin = active_npcs_begin
kingdom_heroes_end = active_npcs_end

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = active_npcs_end ##NERO CLAUDIUS: was  kingdom_ladies_end

soldiers_begin = "trp_sarmatian_peasant"
soldiers_end = "trp_town_walker_1"

soldiers_2_begin = "trp_town_walker_1"
soldiers_2_end = "trp_new_troops_end"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

# pretenders_begin = "trp_kingdom_1_pretender"
# pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenaries_end"

greek_mercenary_troops_begin = "trp_watchman"
greek_mercenary_troops_end = "trp_hispanic_infantry"

celtic_mercenary_troops_begin = "trp_celtic_freeman"
celtic_mercenary_troops_end = "trp_germanic_hunter"

stepp_mercenary_troops_begin = "trp_scythian_horse_archer"
stepp_mercenary_troops_end = "trp_celtic_freeman"

eastern_mercenary_troops_begin = "trp_persian_picaxe_man"
eastern_mercenary_troops_end = "trp_indian_archer"

germanic_mercenary_troops_begin = "trp_germanic_hunter"
germanic_mercenary_troops_end = "trp_baltic_hunter"

baltic_mercenary_troops_begin = "trp_baltic_hunter"
baltic_mercenary_troops_end = "trp_danish_skirmisher"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_global_variables"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "trp_global_variables"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_8"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_10"
mayor_quests_end_2   = "qst_blank_quest_12"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_19"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

# horses_begin    = "itm_sumpter_horse"
# horses_end      = "itm_arrows"

legendary_items_begin = "itm_hercules_club"
legendary_items_end = "itm_dedal_kufel"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

number_of_castles        = p_village_1 - p_castle_1
number_of_villages       = p_salt_mine - p_village_1
number_of_towns          = p_castle_1 - p_town_1
number_of_walled_centers = number_of_towns+number_of_castles
number_of_centers        = number_of_walled_centers + number_of_villages
number_of_factions       = fac_kingdoms_end - fac_player_supporters_faction
number_of_active_npcs    = trp_knight_1_1_wife - trp_npc1
number_of_companions     = trp_kingdom_1_lord - trp_npc1

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

#SB : replaced spelling of "gound"
training_ground_trainers_begin    = "trp_trainer_1"
training_ground_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_sarmatian_village_walker"

village_walkers_begin = "trp_sarmatian_village_walker"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

# startup_merchants_begin = "trp_roman_start_merchant"
# startup_merchants_end = "trp_superbus"

##diplomacy start+
tournament_champions_begin = "trp_Xerina"
tournament_champions_end   = "trp_tutorial_trainer"

merchants_begin = armor_merchants_begin
merchants_end = village_elders_end

dplmc_employees_begin = "trp_dplmc_chamberlain"#Individual employees (chancellor, constable, chamberlain)
dplmc_employees_end   = "trp_dplmc_messenger"#The messenger is not included, since it's a generic figure rather than a specific person.
##diplomacy end+


num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_javelin"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = weapons_begin
shields_begin = weapons_end
shields_end = ranged_weapons_begin

# horses
parthian_horses_begin   = "itm_cataphract_horse_parthian_1"
parthian_horses_end     = "itm_leopard_horse_1"

roman_noble_horses_begin   = "itm_leopard_horse_1"
roman_noble_horses_end     = "itm_camel"

camels_begin = "itm_camel"
camels_end   = "itm_donkey_mount"

donkeys_begin = "itm_donkey_mount"
donkeys_end   = "itm_arrows"

arabian_horses_begin = "itm_arabian_horse_a"
arabian_horses_end   = "itm_parthian_horse_a"

steppe_horses_begin = "itm_steppe_horse_1"
steppe_horses_end   = "itm_arabian_horse_a"

numidian_horses_begin = "itm_numidian_horse_1"
numidian_horses_end   = "itm_steppe_horse_1"

roman_horses_begin = "itm_horse_1"
roman_horses_end   = "itm_numidian_horse_1"

generic_horses_begin = "itm_normal_horse_1"
generic_horses_end   = "itm_horse_1"

pack_horses_begin = "itm_sumpter_horse"
pack_horses_end   = "itm_normal_horse_1"
# horses end

# ammunition
sling_rocks_begin   = "itm_sling_rock1"
sling_rocks_end     = "itm_ballista_bolts"

ballista_bolts_begin   = "itm_ballista_bolts"
ballista_bolts_end     = "itm_leather_gloves"

generic_arrows_begin   = "itm_arrows"
generic_arrows_end     = "itm_syrian_barbed_arrows"

arabian_arrows_begin   = "itm_syrian_barbed_arrows"
arabian_arrows_end     = "itm_sarmatian_arrows_1"

sarmatian_arrows_begin   = "itm_sarmatian_arrows_1"
sarmatian_arrows_end     = "itm_sling_rock1"
# ammunition end

# hand armour
gloves_begin = "itm_leather_gloves"
gloves_end = "itm_aquilifer_legion_squamata_1"

# body armour
roman_armour_begin = "itm_aquilifer_legion_squamata_1"
roman_armour_end   = "itm_garmantian_armor_1"

north_african_armoury_begin = "itm_garmantian_armor_1"
north_african_armoury_end   = "itm_indian_pants"

indian_armoury_begin = "itm_indian_pants"
indian_armoury_end   = "itm_celtic_naked1"

celtic_armoury_begin = "itm_celtic_naked1"
celtic_armoury_end   = "itm_dacian_naked1"

dacian_armoury_begin    = "itm_dacian_naked1"
dacian_armoury_end      = "itm_germanic_completenaked1"

germanic_armoury_begin = "itm_germanic_completenaked1"
germanic_armoury_end   = "itm_alan_light_1"

alan_armoury_begin = "itm_alan_light_1"
alan_armoury_end = "itm_sarmatian_light1"

sarmatian_armoury_begin = "itm_sarmatian_light1"
sarmatian_armoury_end = "itm_saka_armour_1"

saka_armoury_begin = "itm_saka_armour_1"
saka_armoury_end = "itm_scythian_light1"

scythian_armoury_begin = "itm_scythian_light1"
scythian_armoury_end = "itm_bosporan_light1"

bosporan_armoury_begin = "itm_bosporan_light1"
bosporan_armoury_end = "itm_caucasian_scale_heavy_1"

caucasian_armoury_begin = "itm_caucasian_scale_heavy_1"
caucasian_armoury_end   = "itm_persian_tunic_1"

persian_armoury_begin = "itm_persian_sheepskin_1"
persian_armoury_end   = "itm_parthian_tunic_1"

parthian_armoury_begin = "itm_parthian_tunic_1"
parthian_armoury_end   = "itm_illyrian_medium1"

illyrian_armoury_begin = "itm_illyrian_medium1"
illyrian_armoury_end   = "itm_iberian_light1"

ibarian_armoury_begin = "itm_iberian_light1"
ibarian_armoury_end   = "itm_arabian_tunic_1"

arabian_armoury_begin = "itm_arabian_tunic_1"
arabian_armoury_end   = "itm_judean_tunic_1"

judean_armoury_begin  = "itm_judean_tunic_1"
judean_armoury_end    = "itm_linen_tunic"

eastern_armoury_begin = "itm_sarranid_cloth_robe"
eastern_armoury_end   = "itm_linothorax_greek1"

greek_armoury_shit_begin    = "itm_linothorax_greek1"
greek_armoury_shit_end      = "itm_rawhide_coat"

bandit_armoury_shit_begin    = "itm_rawhide_coat"
bandit_armoury_shit_end      = "itm_phrygian_cap"

roman_tunics_begin = "itm_linen_tunic"
roman_tunics_end   = "itm_roman_toga"

roman_toga_begin = "itm_roman_toga"
roman_toga_end   = "itm_roman_noble_dress_1"

roman_dresses_noble_begin = "itm_roman_noble_dress_1"
roman_dresses_noble_end   = "itm_german_femal_rich_1"

germanic_dresses_noble_begin = "itm_german_femal_rich_1"
germanic_dresses_noble_end   = "itm_barb_femal_rich1"

briton_dresses_begin = "itm_female_1_barb"
briton_dresses_end   = "itm_green_dress"

barbarian_dresses_noble_begin = "itm_barb_femal_rich1"
barbarian_dresses_noble_end   = "itm_roman_lupa_dress"

prostitute_dresses_begin = "itm_roman_lupa_dress"
prostitute_dresses_end   = "itm_female_1"

barbarian_dresses_begin = "itm_female_1"
barbarian_dresses_end   = "itm_female_1_barb"

eastern_dresses_begin = "itm_sarranid_common_dress"
eastern_dresses_end   = "itm_sarranid_cloth_robe"

eastern_dresses_noble_begin = "itm_green_dress"
eastern_dresses_noble_end   = "itm_sarranid_common_dress"
# body armour end

# head cloths
phrygian_caps_begin = "itm_phrygian_cap"
phrygian_caps_end   = "itm_alan_light_helm"

alan_helmets_begin = "itm_alan_light_helm"
alan_helmets_end   = "itm_saka_cap_1"

saka_helmets_begin = "itm_saka_cap_1"
saka_helmets_end   = "itm_sarmatian_cap_1"

sarmatian_helmets_begin = "itm_sarmatian_cap_1"
sarmatian_helmets_end   = "itm_bosporan_spangenhelm_1"

bosporan_helmets_begin = "itm_bosporan_spangenhelm_1"
bosporan_helmets_end   = "itm_kopfband"

african_hats_begin  = "itm_kopfband"
african_hats_end    = "itm_dacian_pileus_a_1"

dacian_helmets_begin = "itm_dacian_pileus_a_1"
dacian_helmets_end   = "itm_germanic_cap_1"

germanic_helmets_begin = "itm_germanic_cap_1"
germanic_helmets_end   = "itm_mak_helm_1"

greek_helmets_begin = "itm_mak_helm_1"
greek_helmets_end   = "itm_illyrian_hevy_helmet_plume2"

illyrian_helmets_begin = "itm_illyrian_hevy_helmet_plume2"
illyrian_helmets_end   = "itm_indian_turban_1"

indian_helmets_begin    = "itm_indian_turban_1"
indian_helmets_end      = "itm_britton_helm1"

celtic_helmets_begin = "itm_britton_helm1"
celtic_helmets_end   = "itm_cataphract_helm1"

parthian_helmets_begin = "itm_cataphract_helm1"
parthian_helmets_end   = "itm_armenian_helm_legion_1"

caucasian_helmets_begin = "itm_armenian_helm_legion_1"
caucasian_helmets_end   = "itm_pilos_chad"

arabian_helmets_begin = "itm_pilos_chad"
arabian_helmets_end   = "itm_sarranid_felt_hat"

eastern_hats_begin = "itm_sarranid_felt_hat"
eastern_hats_end   = "itm_roman_townguard_helm"

roman_helmets_begin = "itm_roman_townguard_helm"
roman_helmets_end   = "itm_straw_hat"

straw_hats_begin = "itm_straw_hat"
straw_hats_end   = "itm_headcloth"

eastern_head_cloth_begin = "itm_headcloth"
eastern_head_cloth_end   = "itm_common_hood"

eastern_helmets_begin = "itm_desert_padded_hat_a"
eastern_helmets_end   = "itm_flower_crown"

generic_hoods_begin = "itm_common_hood"
generic_hoods_end   = "itm_fur_hat"

bandit_helmets_begin    = "itm_fur_hat"
bandit_helmets_end      = "itm_turban"

turbans_begin   = "itm_turban"
turbans_end     = "itm_desert_padded_hat_a"

female_head_cloth_begin   = "itm_flower_crown"
female_head_cloth_end     = "desert_celtic_boots"
# head cloths end

# boots
barbarian_boots_begin = "itm_celtic_boots"
barbarian_boots_end   = "itm_sarmatian_shoes"

sarmatian_boots_begin   = "itm_sarmatian_shoes"
sarmatian_boots_end     = "itm_female_caligea_gold"

roman_civilian_boots_begin   = "itm_female_caligea_gold"
roman_civilian_boots_end     = "itm_legio_armored_caligea_2"

roman_military_boots_begin   = "itm_legio_armored_caligea_2"
roman_military_boots_end     = "itm_eastern_shoe"

eastern_boots_begin   = "itm_eastern_shoe"
eastern_boots_end     = "itm_cataphract_boots"

cataphract_boots_begin  = "itm_cataphract_boots"
cataphract_boots_end    = "itm_wooden_stick"
# boots end

# weapons
tools_begin = "itm_wooden_stick"
tools_end   = "itm_fighting_axe"

generic_axes_begin  = "itm_fighting_axe"
generic_axes_end    = "itm_club"

clubs_begin  = "itm_club"
clubs_end    = "itm_spiked_mace"

maces_begin  = "itm_spiked_mace"
maces_end    = "itm_celtic_sword1"

celtic_weapons_begin  = "itm_celtic_sword1"
celtic_weapons_end    = "itm_sword_akinakes"

greek_weapons_begin  = "itm_sword_akinakes"
greek_weapons_end    = "itm_kopis"

special_begin  = "itm_kopis"
special_end    = "itm_dagger_parthian_1"

parthian_weapons_begin  = "itm_dagger_parthian_1"
parthian_weapons_end    = "itm_eastern_sword1"

eastern_weapons_begin  = "itm_eastern_sword1"
eastern_weapons_end    = "itm_dacian_noble_sword"

dacian_weapons_begin  = "itm_dacian_noble_sword"
dacian_weapons_end    = "itm_cheruski_sword"

germanic_weapons_begin  = "itm_cheruski_sword"
germanic_weapons_end    = "itm_nubian_axe"

nubian_weapons_begin  = "itm_nubian_axe"
nubian_weapons_end    = "itm_kartil_axe_1"

caucasian_weapons_begin  = "itm_kartil_axe_1"
caucasian_weapons_end    = "itm_dagger"

roman_weapons_begin  = "itm_dagger"
roman_weapons_end    = "itm_palmyran_gladius"

arabian_weapons_begin  = "itm_palmyran_gladius"
arabian_weapons_end    = "itm_alan_long_sword"

alan_weapons_begin  = "itm_alan_long_sword"
alan_weapons_end    = "itm_sarmatian_sword_2"

sarmatian_weapons_begin  = "itm_sarmatian_sword_2"
sarmatian_weapons_end    = "itm_scythe"

generic_polearms_begin  = "itm_scythe"
generic_polearms_end    = "itm_light_lance"

kontos_begin  = "itm_light_lance"
kontos_end    = "itm_wooden_shield"
# weapons end

# shields
bosporan_shields_begin  = "itm_bosphoran_shield_new_1"
bosporan_shields_end    = "itm_caucasian_shield_1"

generic_round_shields_begin  = "itm_wooden_shield"
generic_round_shields_end    = "itm_bosphoran_shield_new_1"

caucasian_shields_begin  = "itm_caucasian_shield_1"
caucasian_shields_end    = "itm_hoplon_1"

greek_shields_begin  = "itm_hoplon_1"
greek_shields_end    = "itm_african_shield_1"

african_shields_begin  = "itm_african_shield_1"
african_shields_end    = "itm_nubian_kite_shield_1"

nubian_shields_begin  = "itm_nubian_kite_shield_1"
nubian_shields_end    = "itm_eastern_shield_inf_light1"

eastern_shields_begin  = "itm_eastern_shield_inf_light1"
eastern_shields_end    = "itm_scythian_shield_cav1"

eastern_cav_shields_begin  = "itm_scythian_shield_cav1"
eastern_cav_shields_end    = "itm_indian_shield_1"

indian_shields_begin  = "itm_indian_shield_1"
indian_shields_end    = "itm_pict_square_shield_1"

celtic_shields_begin  = "itm_pict_square_shield_1"
celtic_shields_end    = "itm_dacian_oval_shield_1"

dacian_shields_begin  = "itm_dacian_oval_shield_1"
dacian_shields_end    = "itm_scythisn_shield_inf5"

armenian_shields_begin  = "itm_scythisn_shield_inf1"
armenian_shields_end    = "itm_eastern_germanic_shield_1"

germanic_shields_begin  = "itm_eastern_germanic_shield_1"
germanic_shields_end    = "itm_arabian_oval_shield_1"

arabian_shields_begin  = "itm_arabian_oval_shield_1"
arabian_shields_end    = "itm_illyrian_shield_large1"

illyrian_shields_begin  = "itm_illyrian_shield_large1"
illyrian_shields_end    = "itm_battle_standard"

barbarian_battle_standards_begin  = "itm_battle_standard"
barbarian_battle_standards_end    = "itm_old_scutum"

old_roman_shields_begin  = "itm_old_scutum"
old_roman_shields_end    = "itm_roman_shield_1"

roman_round_shields_begin  = "itm_roman_shield_1"
roman_round_shields_end    = "itm_signum_bireme"

roman_signum_begin  = "itm_signum_bireme"
roman_signum_end    = "itm_vexilum_legio_xiii"

roman_vexilium_begin  = "itm_vexilum_legio_xiii"
roman_vexilium_end    = "itm_scutum_legio_i"

roman_shields_begin  = "itm_scutum_legio_i"
roman_shields_end    = "itm_judean_shield_large_1"

judean_shields_begin  = "itm_judean_shield_large_1"
judean_shields_end    = "itm_egyptian_shield_large_1"

egyptian_shields_begin  = "itm_egyptian_shield_large_1"
egyptian_shields_end    = "itm_cetratus_christian"

special_shields_begin  = "itm_cetratus_christian"
special_shields_end    = "itm_simple_thraex_shield"

generic_shields_begin  = "itm_simple_thraex_shield"
generic_shields_end    = "itm_javelin"
# shields end

# missile weapons
generic_javelins_begin = "itm_javelin"
generic_javelins_end   = "itm_javelin_berber"

african_javelins_begin = "itm_javelin_berber"
african_javelins_end   = "itm_throwing_spears_east"

eastern_javelins_begin = "itm_throwing_spears_east"
eastern_javelins_end   = "itm_throwing_spears_dacian"

dacian_javelins_begin = "itm_throwing_spears_dacian"
dacian_javelins_end   = "itm_throwing_spears_germanic"

germanic_javelins_begin = "itm_throwing_spears_germanic"
germanic_javelins_end   = "itm_jarid_celt"

celtic_javelins_begin = "itm_jarid_celt"
celtic_javelins_end   = "itm_throwing_spears_roman"

roman_javelins_begin = "itm_throwing_spears_roman"
roman_javelins_end   = "itm_stones"

generic_bows_javelins_begin = "itm_stones"
generic_bows_javelins_end   = "itm_german_shortbow"

germanic_bows_begin = "itm_german_shortbow"
germanic_bows_end   = "itm_arabian_bow_1"

arabian_bows_begin = "itm_arabian_bow_1"
arabian_bows_end   = "itm_nomad_bow"

composite_bows_begin = "itm_nomad_bow"
composite_bows_end   = "itm_strong_bow"

caucasian_bows_begin = "itm_strong_bow"
caucasian_bows_end   = "itm_nubian_war_bow"

nubian_bows_begin = "itm_nubian_war_bow"
nubian_bows_end   = "itm_sling"

slings_begin = "itm_sling"
slings_end   = "itm_ballista_mounted"

ballista_begin = "itm_ballista_mounted"
ballista_end   = "itm_torch"
# end missle weapons

# music instruments
roman_music_begin   = "itm_f_cornu"
roman_music_end     = "itm_lyre"

barbarian_music_begin   = "itm_horn"
barbarian_music_end     = "itm_f_cornu"
# end music instruments


# Banner constants

banner_meshes_begin = "mesh_banner_kingdom_1"
banner_meshes_end_minus_one = "mesh_banner_f21"

banner_meshes_legion_begin = "mesh_banner_legion_vexilium_italica_ii"
banner_meshes_legion_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_kingdom_1"
arms_meshes_end_minus_one = "mesh_arms_f21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_map_flag_kingdom_1"
banner_map_icons_end_minus_one = "icon_banners_end"

banner_scene_props_begin = "spr_banner_kingdom_1"
banner_scene_props_end_minus_one = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125

banners_end_offset = 136

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

##bandit spawn points, used for spawnung bandits randomly
num_forest_bandit_spawn_points = 3

num_steppe_bandit_spawn_points = 3
num_taiga_bandit_spawn_points = 3
num_desert_bandit_spawn_points = 3
num_numidian_bandit_spawn_points = 3
num_sea_raider_spawn_points = 3

# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

#default ones
cmenu_notes = 1
cmenu_landing_point = 2
#SB : context menu cheats, some we roll into a menu instead
cmenu_attach = 9
cmenu_detach = 10
# cmenu_exchange = 11
cmenu_encounter = 12
# cmenu_spawnbandit = 13
cmenu_losebattle = 14
cmenu_winbattle = 15
# cmenu_reinforce = 16
# cmenu_heal = 17
# cmenu_wound = 18

# Town center modes - resets in game menus during the options
tcm_default 		= 0
tcm_disguised 		= 1
tcm_prison_break 	= 2
tcm_escape      	= 3


# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4 #unused

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 5000

#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours


# #NORMAL ACHIEVEMENTS
# ACHIEVEMENT_NONE_SHALL_PASS = 1,
# ACHIEVEMENT_MAN_EATER = 2,
# ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
# ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
# ACHIEVEMENT_KHAAAN = 5,
# ACHIEVEMENT_GET_UP_STAND_UP = 6,
# ACHIEVEMENT_BARON_GOT_BACK = 7,
# ACHIEVEMENT_BEST_SERVED_COLD = 8,
# ACHIEVEMENT_TRICK_SHOT = 9,
# ACHIEVEMENT_GAMBIT = 10,
# ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
# ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
# ACHIEVEMENT_MOUNTAIN_BLADE = 13,
# ACHIEVEMENT_HOLY_DIVER = 14,
# ACHIEVEMENT_FORCE_OF_NATURE = 15,

# #SKILL RELATED ACHIEVEMENTS:
# ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
# ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
# ACHIEVEMENT_COMMUNITY_SERVICE = 18,
# ACHIEVEMENT_AGILE_WARRIOR = 19,
# ACHIEVEMENT_MELEE_MASTER = 20,
# ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
# ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
# ACHIEVEMENT_ART_OF_WAR = 23,
# ACHIEVEMENT_THE_RANGER = 24,
# ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

# #MAP RELATED ACHIEVEMENTS:
# ACHIEVEMENT_MIGRATING_COCONUTS = 26,
# ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
# ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
# ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
# ACHIEVEMENT_THE_BANDIT = 30,
# ACHIEVEMENT_GOT_MILK = 31,
# ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
# ACHIEVEMENT_MEDIEVAL_TIMES = 33,
# ACHIEVEMENT_GOOD_SAMARITAN = 34,
# ACHIEVEMENT_MORALE_LEADER = 35,
# ACHIEVEMENT_ABUNDANT_FEAST = 36,
# ACHIEVEMENT_BOOK_WORM = 37,
# ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

# #POLITICALLY ORIENTED ACHIEVEMENTS:
# ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
# ACHIEVEMENT_HEART_BREAKER = 40,
# ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
# ACHIEVEMENT_I_DUB_THEE = 42,
# ACHIEVEMENT_SASSY = 43,
# ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
# ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
# ACHIEVEMENT_TALKING_HELPS = 46,
# ACHIEVEMENT_KINGMAKER = 47,
# ACHIEVEMENT_PUGNACIOUS_D = 48,
# ACHIEVEMENT_GOLD_FARMER = 49,
# ACHIEVEMENT_ROYALITY_PAYMENT = 50,
# ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
# ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
# ACHIEVEMENT_MANIFEST_DESTINY = 53,
# ACHIEVEMENT_CONCILIO_CALRADI = 54,
# ACHIEVEMENT_VICTUM_SEQUENS = 55,

# #MULTIPLAYER ACHIEVEMENTS:
# ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
# ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
# ACHIEVEMENT_HARASSING_HORSEMAN = 58,
# ACHIEVEMENT_THROWING_STAR = 59,
# ACHIEVEMENT_SHISH_KEBAB = 60,
# ACHIEVEMENT_RUIN_THE_RAID = 61,
# ACHIEVEMENT_LAST_MAN_STANDING = 62,
# ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
# ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
# ACHIEVEMENT_MACE_IN_YER_FACE = 65,
# ACHIEVEMENT_THE_HUSCARL = 66,
# ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
# ACHIEVEMENT_ELITE_WARRIOR = 68,

# #COMBINED ACHIEVEMENTS
# ACHIEVEMENT_SON_OF_ODIN = 69,
# ACHIEVEMENT_KING_ARTHUR = 70,
# ACHIEVEMENT_KASSAI_MASTER = 71,
# ACHIEVEMENT_IRON_BEAR = 72,
# ACHIEVEMENT_LEGENDARY_RASTAM = 73,
# ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

# ACHIEVEMENT_MAN_HANDLER = 75,
# ACHIEVEMENT_GIRL_POWER = 76,
# ACHIEVEMENT_QUEEN = 77,
# ACHIEVEMENT_EMPRESS = 78,
# ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
# ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

#battle_ratio_multiple = 7000
max_morale = 40000 #was 35000
#max_ratio = max_morale/2


#slot_agent_courage_score_bonus	  = 27
# slot_agent_rank_depth			  = 28
# slot_agent_rank_closeness		  = 29

# recruiter kit end


#For $g_dplmc_terrain_advantage
DPLMC_TERRAIN_ADVANTAGE_DISABLE     =  -1
DPLMC_TERRAIN_ADVANTAGE_ENABLE      =  0   #So I don't have to keep track of whether it is enabled or disabled by default

#For $g_dplmc_lord_recycling
# 1 enabled
# 0 disabled
# DPLMC_LORD_RECYCLING_DISABLE           = -1
# DPLMC_LORD_RECYCLING_ENABLE            =  0
# DPLMC_LORD_RECYCLING_FREQUENT          =  1

#For $g_dplmc_ai_changes
# DPLMC_AI_CHANGES_DISABLE        =  -1
# DPLMC_AI_CHANGES_LOW            =   0
# DPLMC_AI_CHANGES_MEDIUM         =   1
# DPLMC_AI_CHANGES_HIGH           =   2

#Mercantilism
# - Your caravans generate more revenue for your towns, but your benefit
#   from the caravans of other kingdoms is diminished.
# - Trade within the kingdom is made more efficient, while imports are
#   discouraged.
#
#Low:
# - Caravan trade benefits both the source and the destination
# - When the player surrenders, there is a chance his personal equipment
#   will not be looted, based on who accepted the surrender and the difficulty
#   setting.  (This is meant to address a gameplay issue.  In the first 700
#   days or so, there is no possible benefit to surrendering rather than
#   fighting to the last man.)  Also, a bug that made it possible for
#   books etc. to be looted was corrected.
# - AI caravans take into consideration distance when choosing their next
#   destination and will be slightly more like to visit their own faction.
#   This strategy is mixed with the Native one, so the trade pattern will
#   differ but not wildly.
# - Scale town merchant gold by prosperity (up to a maximum 40% change).
# - Food prices increase in towns that have been under siege for at least
#   48 hours.
# - In towns the trade penalty script has been tweaked to make it more
#   efficient to sell goods to merchants specializing in them.
# - Food has a chance of not spoiling depending on inventory management.
# - Villages being raided now delays construction projects.
#
#Medium:
# - Food consumption increases in towns as prosperity increases.
#   Consumption also increases with garrison sizes.
# - Lords' looting skill affects how much gold they take from the player
#   when they defeat him.
# - Lords' leadership skill modifies their troop wage costs the same way
#   it does for the player.
# - The player can lose gold when his fiefs are looted, like lords.
# - The same way that lord party sizes increase as the player progresses,
#   mercenary party sizes also increase to maintain their relevance.
#   (The rate is the same as for lords: a 1.25% increase per level.)
# - If the player has a kingdom of his own, his spouse will receive
#   part of the bonus that ordinarily would be due a liege.  The extent
#   of this bonus depends on the number of fiefs the players holds.
#   This bonus is non-cumulative with the marshall bonus.
# - Attrition is inflicted on NPC-owned centers if they can't pay wages,
#   but only above a certain threshold.
# - Strangers cannot acquire enterprises (enforced at 1 instead of at 0,
#   so you have to do something).
# - Village prosperity has an impact on bandit infestation (chance of death spiral).
# - Village elder now receives the gold when you buy cattle
#
#High:
# - The total amount of weekly bonus gold awarded to kings in Calradia
#   remains constant: as kings go into exile, their bonuses are divided
#   among the remaining kings.
# - If lord's run a personal gold surplus after party wages, the extra is
#   divided among the lord and his garrisons budgets (each castle and town
#   has its own pool of funds to pay for soldiers) on the basis of whether
#   the lord is low on gold or any of his fortresses are.  (If none are low
#   on gold, the lord takes everything, like before.)
# - The honor loss from an offense depends in part on the player's honor
#   at the time.  The purer the reputation, the greater the effect of a single
#   disagrace.
# - Raiding change: village gold lost is removed from uncollected taxes before
#   the balance (if any) is removed from the lord.
# - Trading parties will drop off prisoners at walled centers.
# - Cash for prisoners
# - allows cancelling improvements (cash goes back to local economy)

#For relatives: a standard way of generating IDs for "relatives" that are not
#implemented in the game as troops, but nevertheless should be taken into
#account for the purpose of script_troop_get_family_relation_to_troop
DPLMC_VIRTUAL_RELATIVE_MULTIPLIER = -4
DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET = -1#e.g. father for x = (DPLMC_VIRTUAL_RELATIVE_MULTIPLIER * x) + DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET
DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET = -2
DPLMC_VIRTUAL_RELATIVE_SPOUSE_OFFSET = -3

#For cultural terms, with "script_dplmc_store_cultural_word_reg0" :
DPLMC_CULTURAL_TERM_WEAPON = 1#sword
DPLMC_CULTURAL_TERM_WEAPON_PLURAL = 2#"swords"
DPLMC_CULTURAL_TERM_USE_MY_WEAPON = 3#"swing my sword", etc.
DPLMC_CULTURAL_TERM_KING = 4#"king"
DPLMC_CULTURAL_TERM_KING_FEMALE = 5#"queen"
DPLMC_CULTURAL_TERM_KING_PLURAL = 6#"kings"
DPLMC_CULTURAL_TERM_LORD = 7#"lord"
DPLMC_CULTURAL_TERM_LORD_PLURAL = 8#"lords"
DPLMC_CULTURAL_TERM_SWINEHERD = 9
DPLMC_CULTURAL_TERM_TAVERNWINE = 10#"wine" (used in tavern talk)
DPLMC_CULTURAL_TERM_KING_PRAISE = 11
DPLMC_CULTURAL_TERM_ARMY = 12
DPLMC_CULTURAL_TERM_GUARD = 13
DPLMC_CULTURAL_TERM_ARMY_PLURAL = 14

## Possible return values from "script_dplmc_get_troop_standing_in_faction"
DPLMC_FACTION_STANDING_LEADER = 60
DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
DPLMC_FACTION_STANDING_MARSHALL = 40
DPLMC_FACTION_STANDING_LORD = 30
DPLMC_FACTION_STANDING_DEPENDENT = 20
DPLMC_FACTION_STANDING_MEMBER = 10#includes mercenaries
DPLMC_FACTION_STANDING_PETITIONER = 5
DPLMC_FACTION_STANDING_UNAFFILIATED = 0


#SB : bunch of constants
slot_prisoner_agreed = 181	#Hablar prisioneros chief

#ranges
bandit_party_templates_begin = "pt_steppe_bandits"
bandit_party_templates_end   = "pt_deserters"

fighters_begin = "trp_novice_fighter"
fighters_end = "trp_cattle"

#threshold for lord upgrades
#slot_troop_wealth must exceed the calculated amount for action in script_troop_does_business_in_center
dplmc_improvement_limit = 75000#
dplmc_equipment_limit = 60000
dplmc_command_renown_limit = 300

dplmc_ransom_commission = 500
dplmc_ransom_debt_mask = 100000

dplmc_companion_skill_renown = 3
dplmc_companion_emissary_renown = 2
dplmc_companion_battle_renown = 1

#the following used in mnu_party_size_report, script_game_get_party_companion_limit, script_party_get_ideal_size
dplmc_castle_party_bonus        = 50
dplmc_town_party_bonus          = 60
dplmc_village_party_bonus       = 40
dplmc_marshal_party_bonus       = 50
dplmc_monarch_party_bonus       = 100

#increase/decrease in relation, renown, etc
message_positive = 0x33FF33
message_neutral  = 0xFFFF33
message_negative = 0xFF3333
#notifying defeat of player kingdom messengers, caravans etc
message_defeated = 0xFF0000
#other messages of note
message_alert = 0xF0DD33
message_locked = 0xFFAAAA
###for vc compatibility
color_great_news = 0xCCFFCC
color_good_news = 0xCCFFCC
color_terrible_news = 0xFFCCCC  #0xFF2222
color_bad_news = 0xFFCCCC
color_neutral_news = 0xFFFFFF
color_quest_and_faction_news = 0xCCCCFF
color_hero_news = 0xFFFF99
color_information = 0x00007F


#camera mode constants, see module_strings or info-pages
camera_keyboard = 1
camera_mouse = 2
camera_follow = 3

rename_kingdom    = 1
rename_center     = 2
rename_party      = 3
rename_companion  = 4
rename_legion     = 5
rename_party_2    = 6
rename_month      = 7
rename_aux_inf    = 8
rename_aux_cav    = 9

#recolor modes
recolor_kingdom = 0
recolor_heraldic = 1
recolor_groups = 2

#disguise mods, roughly correspond to bg archetypes or common troops
# slot_troop_player_disguise_choice = slot_troop_met
slot_troop_player_disguise_sets = slot_troop_met_previously
num_disguises = 6

disguise_none = 0
disguise_pilgrim = 1 #default
disguise_farmer = 2 #trp_farmer
disguise_hunter = 4 #trp_forest_bandit
disguise_guard = 8 #trp_caravan_guard
disguise_merchant = 16 #trp_caravan_master
disguise_bard = 32

DPLMC_CURRENT_VERSION_CODE = 160501
DPLMC_VERSION_LOW_7_BITS = 68 #Number that comes after the rest of the version code

DPLMC_DIPLOMACY_VERSION_STRING = "4.3+ for Steam"

# #Perform a check to make sure constants are defined in a reasonable way.
# def _validate_constants(verbose=False):
    # """Makes sure begin/end pairs have length of at least zero."""
    # d = globals()
    # for from_key in d:
        # if not from_key.endswith("_begin"):
            # continue
        # to_key = from_key[:-len("_begin")]+"_end"
        # if not to_key in d:
            # if verbose:
                # print "%s has no matching %s" % (from_key, to_key)
            # continue
        # from_value = d[from_key]
        # to_value = d[to_key]
        # if not type(from_value) in (int, float, long):
            # continue
        # if not from_value <= to_value:
            # raise Exception("ERROR, condition %s <= %s failed [not true that %s <= %s]" % (from_key, to_key, str(from_value), str(to_value)))
        # elif verbose:
            # print "%s <= %s [%s <= %s]" % (from_key, to_key, str(from_value), str(to_value))

# #Automatically run this on module import, so errors are detected
# #during building.
# _validate_constants(verbose=(__name__=="__main__"))
# ##diplomacy end+

#Team Data
slot_team_faction                       = 1
slot_team_starting_x                    = 2
slot_team_starting_y                    = 3
slot_team_reinforcement_stage           = 4

#Reset with every call of Store_Battlegroup_Data
slot_team_size                          = 5
slot_team_adj_size                      = 6 #cavalry double counted for AI considerations
slot_team_num_infantry                  = 7	#class counts
slot_team_num_archers                   = 8
slot_team_num_cavalry                   = 9
slot_team_level                         = 10
slot_team_avg_zrot                      = 11
slot_team_avg_x                         = 12
slot_team_avg_y                         = 13

#Battlegroup slots (1 for each of 9 divisions). A "battlegroup" is uniquely defined by team and division
slot_team_d0_size                       = 14
slot_team_d0_percent_ranged             = 23
slot_team_d0_percent_throwers           = 32
slot_team_d0_low_ammo                   = 41
slot_team_d0_level                      = 50
slot_team_d0_armor                      = 59
slot_team_d0_weapon_length              = 68
slot_team_d0_swung_weapon_length        = 77
slot_team_d0_front_weapon_length        = 86
slot_team_d0_front_agents               = 95	#for calculating slot_team_d0_front_weapon_length
slot_team_d0_is_fighting                = 104
slot_team_d0_enemy_supporting_melee     = 113
slot_team_d0_closest_enemy              = 122
slot_team_d0_closest_enemy_dist         = 131	#for calculating slot_team_d0_closest_enemy
slot_team_d0_closest_enemy_special      = 140	#tracks non-cavalry for AI infantry division, infantry for AI archer division
slot_team_d0_closest_enemy_special_dist = 149	#for calculating slot_team_d0_closest_enemy_special
slot_team_d0_avg_x                      = 158
slot_team_d0_avg_y                      = 167
slot_team_d0_avg_zrot                   = 176
#End Reset Group

slot_team_d0_type                       = 185
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

slot_team_d0_formation                  = 194
formation_none      = 0
formation_default   = 1
formation_ranks     = 2
formation_shield    = 3
formation_wedge     = 4
formation_square    = 5

#Native formation modes
#Constants actually correspond to number of "Stand Closer" commands required by WB to create formation
#Extended to 5 line for WFaS
formation_1_row    = 0
formation_2_row    = -1
formation_3_row    = -2
formation_4_row    = -3
formation_5_row    = -4

slot_team_d0_formation_space            = 203	#number of extra 50cm spaces currently in use
slot_team_d0_move_order                 = 212	#now used only for player divisions
slot_team_d0_fclock                     = 221	#now used only for player divisions
slot_team_d0_first_member               = 230	#-1 if division not in formation
slot_team_d0_prev_first_member          = 239
slot_team_d0_speed_limit                = 248
slot_team_d0_percent_in_place           = 257
slot_team_d0_destination_x              = 266
slot_team_d0_destination_y              = 275
slot_team_d0_destination_zrot           = 284
slot_team_d0_target_team                = 293	#targeted battlegroup (team ID)
slot_team_d0_target_division            = 302	#targeted battlegroup (division ID)
slot_team_d0_formation_num_ranks        = 311
slot_team_d0_exists                     = 320
#NEXT                                   = 329
#Battlegroup slots end

reset_team_stats_begin = slot_team_size
reset_team_stats_end   = slot_team_d0_type

minimum_ranged_ammo = 3	#below this not considered ranged type troop

#Formation tweaks
formation_minimum_spacing	= 75	#historical shieldwall was spaced about 47cm, the width of a man's shoulders. Here we loosen for ease of troop movement.
formation_minimum_spacing_horse_length	= 300
formation_minimum_spacing_horse_width	= 200
formation_start_spread_out	    = 2	#extra 50cm spacings for ease of movement for new formations
formation_min_foot_troops   	  = 15	#minimum to make foot formation
formation_min_cavalry_troops	  = 5	#minimum to make cavalry wedge
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4	#used for M&B 1.011 implementation
formation_reequip	        = 1	#allow troops in formations to switch weapons
formation_reform_interval	= 3 #seconds
formation_rethink_for_formations_only	= 0

#Other constants (not tweaks)
Third_Max_Weapon_Length = 400 / 3 #should be 1/3 of longest weapon, longest weapon is sarissa
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2	#trigger is half-second
Top_Speed	= 13
Far_Away	= 1000000

#positions used through formations and AI triggers
Current_Pos     = 34	#pos34
Speed_Pos       = 36	#pos36
Target_Pos      = 37	#pos37
Enemy_Team_Pos  = 38	#pos38
Temp_Pos        = 39	#pos39

#keys used for old M&B
from header_triggers import *
key_for_ranks       = key_j
key_for_shieldwall  = key_k
key_for_wedge       = key_l
key_for_square      = key_semicolon
key_for_undo        = key_u

#Hold Over There Command Tracking
HOT_no_order           = 0
HOT_F1_pressed         = 1
HOT_F1_held            = 2

#Team Slots SEE SECTION

scratch_team = 7	#Should be used just for above slots. If you use it, check for conflicts.

WB_Implementation   = 0
WFaS_Implementation = 1
Native_Formations_Implementation = WB_Implementation

slot_item_alternate            = 46	#table between swing/noswing versions of same weapon

#Battle Phases
BP_Ready  = 0
BP_Init   = 1
BP_Deploy = 2
BP_Setup  = 3
BP_Jockey = 4
BP_Duel   = 5
BP_Fight  = 6

#Presentations Constants Moto chief
Screen_Border_Width = 24
Screen_Width = 1024-Screen_Border_Width
Screen_Height = 768-Screen_Border_Width
Screen_Text_Height = 35
Screen_Checkbox_Height_Adj = 4
Screen_Numberbox_Width = 64
Screen_Title_Height = Screen_Height-Screen_Border_Width-Screen_Text_Height
Screen_Check_Box_Dimension = 20
Screen_Undistort_Width_Num = 7  #distortion midway between 1024x768 and 1366x768 -- things will appear a little narrow on thin screens and vice versa
Screen_Undistort_Width_Den = 8

#Bit switches for global $first_time for keeping track of what has been done at least once in a given game
# first_time_death_camera    = 0x001
first_time_strategy_camera = 0x002
# first_time_game_rules      = 0x004
# first_time_available       = 0x008
# first_time_available       = 0x010
# first_time_available       = 0x020
# first_time_available       = 0x040
# first_time_load_main_party = 0x080  #this used in reverse
first_time_cam_battle      = 0x100
first_time_hold_F1         = 0x200
first_time_formations      = 0x400

Outfit_Thorax_Length = 60  #length dark ages human thorax
Outfit_Fast_Weapon_Speed = 100

mission_tpl_are_all_agents_spawned     = 1943   # (mission_tpl_are_all_agents_spawned), #agents >300 may keep spawning after ti_after_mission_start (still fires .1 second too early)

# Formations AI v5 by Motomataru

#AI variables
AI_long_range	= 8000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_charge_distance	= 1500 ##nero claudius: was 2000, unit: cm
AI_for_kingdoms_only	= 0
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Max_Reinforcements	= Far_Away	#maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player	= 1
AI_Poor_Troop_Level	= 20	#average level of troops under which a division may lose discipline

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 48	#pos48	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos	= 50	#pos50	used only by ranged AI
Nearest_Threat_Pos	= Nearest_Enemy_Troop_Pos	#used only by cavalry AI
Nearest_Target_Pos	= Nearest_Enemy_Battlegroup_Pos	#used only by cavalry AI
Infantry_Pos	= 51	#pos51
Archers_Pos	= 53	#pos53
Cavalry_Pos	= 54	#pos54
Team_Starting_Point	= 55	#pos55

#positions used through battle
Team0_Cavalry_Destination	= 56	#pos56
Team1_Cavalry_Destination	= 57	#pos57
Team2_Cavalry_Destination	= 58	#pos58
Team3_Cavalry_Destination	= 59	#pos59

#######For Permanent camps (talk with companions) BEGIN
# Cost to build a camp
pcamp_build_cost = 100

# Skill that controls camps
pcamp_build_skill = "skl_leadership"

# First level when you can build one; then increases 1 per level until hard cap
pcamp_build_skill_threshold = 2

# Max allowed distance to nearest center
pcamp_max_center_distance = 10

# Chance for a lord to escape from camp (default for party - 50)
pcamp_lord_escape_chance = 40

# Daily desertion chance of 1% per divisor*10% of debt relative to total wage; max 30/divisor%
pcamp_desertion_divisor = 4

# Percentage of player party's stats that directly carry over to camps
#pcamp_player_party_size_percentage = 70
pcamp_player_prisoner_count_percentage = 0

# Number of additional troops per commander leadership level and charisma
pcamp_commander_leadership_size_bonus = 20
pcamp_commander_charisma_size_bonus = 5

# Number of prisoner slots per commander skill and num troops to gain 1 slot
pcamp_commander_prisoner_skill_bonus = 10
pcamp_troop_count_prisoner_divisor = 4



pcamp_chests_begin = "trp_player_camp_chest_1"
pcamp_chests_end = "trp_player_camp_chest_end"

slot_pcamp_camp_commander       = 25
slot_pcamp_camp_chest           = 26
slot_pcamp_camp_initialized     = 27

slot_pcamp_chest_commander      = 28 #slot_troop_guardian
slot_pcamp_chest_party          = 29 #slot_troop_home
slot_pcamp_chest_center         = 30 #slot_troop_cur_center
slot_pcamp_chest_city           = 31 #slot_troop_present_at_event
slot_pcamp_chest_items          = 32 #slot_troop_renown
slot_pcamp_chest_value          = 33 #slot_troop_wealth
slot_pcamp_chest_sell_prisoners = 33 #slot_troop_player_order_state
#######For Permanent camps (talk with companions) END

##campagin constant for party speed
speed_modifier_campaign = 90

##bards from VC
bardo_begin = "trp_martial"
bardo_end = "trp_bard_end"

##NEW Presentations, barracks and options
##new menus with prsnt.:
DPLMC_NUM_PREFERENCE_OPTIONS = 12 #for prsnt_adv_diplomacy_preferences
#campaign difficulty:
camp_d1        = 11
camp_d2        = 12
camp_d3        = 13
camp_d4        = 14
camp_d5        = 15

#Troop Tree Presentation
Troop_Tree_Area_Height = Screen_Title_Height-4*Screen_Text_Height
Troop_Tree_Area_Width = Screen_Width-2*Screen_Border_Width
Troop_Tree_Line_Color = 0x001380
Troop_Tree_Tableau_Height = 800
Troop_Tree_Tableau_Width = Troop_Tree_Tableau_Height*Screen_Undistort_Width_Num/Screen_Undistort_Width_Den
##For Player Legion

# Custom Troops begin
customizable_troops_begin="trp_custom_infantry"
customizable_troops_end="trp_custom_troops_end"
# Custom  Troops end

##senate system
slot_senate_next_meeting         = 18
slot_senate_support              = 19
slot_senate_topic                = 20
slot_senate_topic_opinion        = 21

slot_senate_backup1        = 22
slot_senate_backup2        = 23
slot_senate_backup3        = 24
slot_senate_backup4        = 25

topic_slaves          = 1
topic_grain           = 2
topic_nobles          = 3
topic_lex_militaris   = 4
topic_lex_julia       = 5
topic_lex_agra        = 6
number_of_senators    = 40

##indian trade:
india_land_caravan_cost = 200000
india_sea_caravan_cost  = 1000000
slot_special_event_1       = 18
slot_special_event_2       = 16
slot_india_event_displayed = 29
slot_india_routes_intro_started = 30
slot_india_sea_route_improved = 31
slot_india_land_route_improved = 32
slot_india_sea_mission_in_progress = 33
slot_india_land_mission_in_progress = 34
slot_india_compass = 35
slot_india_india_sea_caravan_expanded = 36

slot_expedition_silk_stolen    = 29
slot_expedition_progress_east   = 17
slot_expedition_progress_south  = 30
slot_expedition_event_1_shown  = 31
slot_expedition_event_2_shown  = 32
slot_expedition_start_time_2 = 18
slot_expedition_start_time_1 = 19

kingmarshal_gold_bon = 3000#bonus income for king and marshal

minor_towns_begin = "p_gaetulian_town_1"
minor_towns_end   = "p_sartemis"


##for strategic camera
#Camera
camera_trigger_interval = .1  #fastest trigger rate with 1000 agents in scene on my machine is 100 milliseconds
camera_animation_time = camera_trigger_interval * 1300  #the actual call interval is often 20% longer
camera_key_rotate_attenuator = 2
camera_minimum_z = 150
camera_minimum_pitch = 271
camera_maximum_pitch = 450
camera_effective_min_zoom = 35  #engine won't zoom in more than this (though the zoom "setting" will go as low as 1)
camera_fixed_angle_h = 7  #fixed angle to targeted agents/props
camera_fixed_angle_v = 6

#Camera Bit Switches
camera_manual          = 0x001
camera_follow_terrain  = 0x002
camera_reverse_y       = 0x004
camera_pan_to_rotation = 0x008  #camera pans AFTER it is rotated
camera_pan_back_forth  = 0x010  #camera command groups
camera_pan_right_left  = 0x020
camera_pan_up_down     = 0x040
camera_rotate          = 0x080
camera_target_agent    = 0x100
camera_target_prop     = 0x200  #not yet implemented
camera_game_slow       = 0x400

##new way to define global variables:
#use slots of trp_global_variables
#entry controll event

g_is_dev = 0#for cheats
#famous battles
g_alesia              = 1
g_dova                = 2
g_rubicon             = 3
g_famous_battle_1     = 4
g_famous_battle_2     = 5
g_famous_battle_3     = 6
g_famous_battle_4     = 7
g_pillars_of_hercules = 8
#9 reserved for another famous battle
g_controlled          = 10
g_age                 = 11
g_fired_emperor_event = 12
g_firer_event_not     = 13
g_nero_dialogue       = 14
g_fire_talk_girl      = 15
g_nero_intro          = 16
g_nero_intro_feast    = 17
g_otho_intro          = 18
g_lord_event_possible   = 19
g_senate_event_possible = 20
g_poppaea_event         = 21
g_financ_event          = 22
g_province_event        = 23
g_nomad_event_triigered = 24
g_last_random_event     = 25
g_player_villa          = 26
g_player_trench         = 27
g_player_visit_golgotha = 28
g_flavor_event_1        = 29
g_flavor_event_2        = 30
g_flavor_event_3        = 31
g_flavor_event_4        = 32#sussus roast
g_used_cheats           = 33
g_cythus_1                   = 34
g_cythus_2                   = 35
g_cythus_3                   = 36
g_can_recruit_greek          = 37
start_town_conversation      = 38
g_show_troop_banner          = 39

#gather statistics
g_number_smallpox              = 50
g_number_greatpox              = 51
g_number_plague                = 52
g_number_measles               = 53
g_number_camp_fever            = 54
g_number_slow_fever            = 55
g_number_consumption           = 56
g_number_fire                  = 57
g_number_drought               = 58
g_number_earthquake            = 59
g_number_insects               = 60

g_global_player_office    = 61
g_number_of_lat           = 62

g_iazyges_event           = 63
g_batava_event            = 64

g_poppaea_event_chain          = 65

g_number_poor_harvest          = 66
g_number_good_harvest          = 67

g_number_harsh_winters         = 68
g_number_mild_winters          = 69

g_destroyed_rome = 70

g_player_recruitement_limit = 71
gold_tribue     = 75000
gold_praefect   = 120000
gold_legate     = 175000

g_starting_year = 72

g_civil_war_timer = 73

g_galba_intro   = 74
g_germanicus_intro = 75

g_toilet_talk = 76

g_rumours_lover = 77

g_antonia_talk = 78

g_corruption_check = 79

g_last_week_income = 80

#Spain
p_hisp_tarraco = 1
p_hisp_baetica = 2
p_hisp_lusit   = 3
## africa
p_afrc_maur = 4
p_afrc_afrc = 5
p_afrc_cyre = 6 #
p_afrc_egyp = 7 #
##Asien
p_asia_arab   = 8 #
p_asia_jude   = 9 #
p_asia_syr    = 10 #
p_asia_cili   = 11 #
p_asia_capa   = 12 #
p_asia_pontus = 13 #
p_asia_minor  = 14 #
##Balkan
p_balk_thrac      = 15
p_balk_moesia_sup = 16
p_balk_moesia_inf = 17
p_balk_acha       = 18
p_balk_epir       = 19
p_balk_mac        = 20
p_balk_dalm       = 21
##italy
p_ita_sici    = 22
p_ita_magna   = 23
p_ita_ital    = 24
p_ita_cis     = 25
##Gaul
p_gaul_narab  = 26
p_gaul_aqua   = 27
p_gaul_lugd   = 28
p_gaul_belg   = 29
#Germania
p_germ_inf    = 30
p_germ_sup    = 31
p_germ_reat   = 32
p_germ_noric  = 33
##central europe
p_cent_panno  = 34

##britannia
p_brit_brita  = 35
p_brit_cale   = 36
##magna germania
p_germ_magna  = 37
p_germ_herc   = 38
p_germ_sueb   = 39
##dacia
p_cent_dac    = 40
##samatia
p_east_sam    = 41
#krim
p_east_bos    = 42
#scythia, caucaus
p_cauc_scyth  = 43
p_asia_arme   = 44
p_asia_meso   = 45
p_asia_assy   = 46

##isle
p_ins_oc  = 47
p_ins_or  = 48 #

p_asia_cauc = 49

p_asia_persia = 50
p_asia_parthia = 51
p_asia_media = 52

p_provinces_end = p_asia_media + 1


#new province system:
slot_province_governor_begin = 0#ranges from 1 to 48 and stores the province governor

slot_province_senatorial_begin = 100#ranges from 50 to 47 and stores if a province is senatorial, also stores time remaining for governorship

slot_legion_home_begin  = 200#stores which center is current home of a legion

slot_legion_home_end    = 215#stores which center is current home of a legion

slot_legion_commanders_begin = 215
slot_legion_commanders_end   = 230

slot_aux_commander_begin = 250
slot_aux_commander_end = 270 #we have 19 units

slot_aux_legion_begin    = 300

decision_governorship       = 1
decision_honorary_title     = 2
decision_reward             = 3
decision_marshall           = 4
decision_legate             = 5
decision_peace              = 6
decision_war                = 7
decision_bribe              = 8
#influence system
##for easy tweaking
# influence_gain_lover        = 8
# influence_gain_intrigue     = 10
# influence_gain_relation     = 10

# influence_lost_relation     = -8
# influence_lost_intrigue     = -4

g_campaign_story_judea  = 4
g_campaign_story_rome   = 3
g_campaign_sandbox      = 2
g_campaign_lord         = 1
g_campaign_king         = 0
##
# script_mcc_generate_skill_set modes
limit_to_stats                         = 0
equip_the_player                       = 1

# character backgrounds
cb_slave = 0
cb_freeman = 1
cb_noble = 2

cb2_strong = 0
cb2_thin = 1
cb2_weak = 2

cb3_genius = 0
cb3_shrewd = 1
cb3_normal = 2
cb3_dull = 3

#use trp_player_camp_chest_end to store minor faction raider parties and removing a loop over all parties
s_nabatean_parties_begin = 1
s_nabatean_parties_end = s_nabatean_parties_begin+5
s_nubian_parties_begin = s_nabatean_parties_end
s_nubian_parties_end = s_nubian_parties_begin+5
s_gaetuli_parties_begin =  s_nubian_parties_end
s_gaetuli_parties_end =  s_gaetuli_parties_begin+5
s_garamantes_parties_begin =  s_gaetuli_parties_end
s_garamantes_parties_end   =  s_garamantes_parties_begin+5
s_rebell_parties_begin   =  s_garamantes_parties_end
s_rebell_parties_end   =  s_rebell_parties_begin+30
s_saka_parties_begin = s_rebell_parties_end
s_saka_parties_end = s_saka_parties_begin+5

p_port_centers_begin = s_saka_parties_end
p_port_centers_end = p_port_centers_begin + 50 # reserve 50


region_spain                            = 1
region_north_africa                     = 2
region_southitaly                       = 3
region_nile                             = 4
region_syria_palestine                  = 5
region_anatolia_central                 = 6
region_anatolia_coastal                 = 7
region_mesopotamia                      = 8
region_persianhill_green                = 9
region_persianhill_desert               =10
region_caucasus                         =11
region_greece                           =12
region_nile_delta                       =13
region_mountain_europe_alps             =14
region_mountain_europe_spain_france     =15
region_mountain_europe_romania          =16
region_mountain_europe_bohemia          =17

color_region_spain                            = 0xB6FF00
color_region_north_africa                     = 0xFFD800
color_region_southitaly                       = 0xA5FF7F
color_region_nile                             = 0x548241
color_region_syria_palestine                  = 0x52B757
color_region_anatolia_central                 = 0xB0B534
color_region_anatolia_coastal                 = 0xA0FF77
color_region_mesopotamia                      = 0x519E00
color_region_persianhill_green                = 0x0C9B00
color_region_persianhill_desert               = 0x939900
color_region_caucasus                         = 0x499979
color_region_greece                           = 0x51995A
color_region_nile_delta                       = 0x00994C
color_region_mountain_europe_alps             = 0x009399
color_region_mountain_europe_spain_france     = 0x287776
color_region_mountain_europe_romania          = 0x296850
color_region_mountain_europe_bohemia          = 0x486660

color_rt_water 		        = 0x0000FF
color_rt_mountain 		    = 0x646464
color_rt_steppe 		    = 0x649632
color_rt_plain 		        = 0x96C864
color_rt_snow 		        = 0x14A81E
color_rt_desert		        = 0xFFE97F
color_rt_deep_water 		= 0x0026FF
color_rt_bridge 		    = 0x0094FF
color_rt_river  		    = 0x6465FF
color_rt_mountain_forest   	= 0x9EA848
color_rt_steppe_forest     	= 0x789714
color_rt_forest            	= 0x3C6632
color_rt_snow_forest       	= 0x00AA21
color_rt_desert_forest     	= 0xB6FF00

salary_legate = 6000
salary_aux_2 = 4000
salary_aux_1 = 2250


ACAN_CORRUPT_SAVE_CHECK = 103940214

location_tavern = 0
location_hall = 1
location_center = 2
location_center_backstreets = 3
location_barracks = 4

all_types   = 0
white       = 1
brown       = 2
black       = 3

white_faces_begin = str_female_white_face_1
white_faces_end   = str_female_white_face_end + 1

brown_faces_begin   = str_female_brown_face_1
brown_faces_end     = str_female_brown_face_end + 1

black_faces_begin   = str_female_black_face_1
black_faces_end     = str_female_black_face_end + 1

# names

male_britannic_names_begin = "str_britannic_name_01"
male_britannic_names_end   = "str_britannic_name_end"

male_dacian_names_begin = "str_dacian_name_01"
male_dacian_names_end   = "str_dacian_name_end"

male_sarmatian_names_begin = "str_sarmatian_name_01"
male_sarmatian_names_end   = "str_sarmatian_name_end"

male_germanic_names_begin = "str_germanic_name_01"
male_germanic_names_end   = "str_germanic_name_end"

male_caucasian_names_begin = "str_caucasian_name_01"
male_caucasian_names_end   = "str_caucasian_name_end"

male_persian_names_begin = "str_persian_name_01"
male_persian_names_end   = "str_persian_name_end"

male_arabian_names_begin = "str_arabian_name_01"
male_arabian_names_end   = "str_arabian_name_end"

male_hebrew_names_begin = "str_hebrew_name_01"
male_hebrew_names_end   = "str_hebrew_name_end"

male_north_african_names_begin = "str_north_african_name_01"
male_north_african_names_end   = "str_north_african_name_end"

male_nubian_names_begin = "str_nubian_name_01"
male_nubian_names_end   = "str_nubian_name_end"

male_saka_names_begin = "str_saka_name_01"
male_saka_names_end   = "str_saka_name_end"

male_roman_names_begin = "str_roman_name_01"
male_roman_names_end   = "str_roman_name_end"

male_roman_cognomens_begin = "str_roman_cognomen_1"
male_roman_cognomens_end   = "str_roman_cognomen_end"

# female
female_britannic_names_begin = "str_britannic_female_name_01"
female_britannic_names_end   = "str_britannic_female_name_end"

female_dacian_names_begin = "str_dacian_female_name_01"
female_dacian_names_end   = "str_dacian_female_name_end"

female_sarmatian_names_begin = "str_sarmatian_female_name_01"
female_sarmatian_names_end   = "str_sarmatian_female_name_end"

female_germanic_names_begin = "str_germanic_female_name_01"
female_germanic_names_end   = "str_germanic_female_name_end"

female_caucasian_names_begin = "str_caucasian_female_name_01"
female_caucasian_names_end   = "str_caucasian_female_name_end"

female_persian_names_begin = "str_persian_female_name_01"
female_persian_names_end   = "str_persian_female_name_end"

female_arabian_names_begin = "str_arabian_female_name_01"
female_arabian_names_end   = "str_arabian_female_name_end"

female_hebrew_names_begin = "str_hebrew_female_name_01"
female_hebrew_names_end   = "str_hebrew_female_name_end"

female_north_african_names_begin = "str_north_african_female_name_01"
female_north_african_names_end   = "str_north_african_female_name_end"

female_nubian_names_begin = "str_nubian_female_name_01"
female_nubian_names_end   = "str_nubian_female_name_end"

female_saka_names_begin = "str_saka_female_name_01"
female_saka_names_end   = "str_saka_female_name_end"

female_roman_names_begin = "str_roman_female_name_01"
female_roman_names_end   = "str_roman_female_name_end"

female_roman_cognomens_begin = "str_roman_female_cognomen_1"
female_roman_cognomens_end   = "str_roman_female_cognomen_end"

# edict costs
cost_edict1         = 0
cost_edict2         = 0
cost_edict3         = 0
cost_edict4         = 1000
cost_edict5         = 0
cost_edict6         = 0
cost_edict7         = 600
cost_edict8         = 0
cost_edict9         = 500
cost_edict10        = 0
cost_libelli_office = 250

miracle_battle_heal     = 1
miracle_battle_strength = 2
miracle_battle_morale   = 3

# main story:
antonia_relation_threshold = 50

last_static_party = "p_vally_of_kings"

# Define constants for wealth bucket thresholds
wealth_bucket_1     = 10000
wealth_bucket_2     = 25000
wealth_bucket_3     = 40000
wealth_bucket_4     = 60000
wealth_bucket_5     = 80000
wealth_bucket_6     = 100000
wealth_bucket_7     = 120000
wealth_bucket_8     = 140000
wealth_bucket_9     = 160000
wealth_bucket_10    = 200000
wealth_bucket_11    = 1000000
