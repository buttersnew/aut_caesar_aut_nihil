from header_music import *

#from compiler import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [

  ("bogus", "silentio.ogg", 0, 0),
  ("main_theme_1", "main_theme_1.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
  ("main_theme_2", "main_theme_2.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
  ("main_theme_3", "farya_hymn_of_legion.ogg", mtf_sit_main_title|mtf_start_immediately, 0),#
  ("thermae_romanae_main_theme", "thermae_romanae_main_theme.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
  ("ambushed_neutral", "middle_eastern_action.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("ambushed_by_nord1",    "germ_war_1.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_nord2",    "germ_war_2.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_nord3",    "germ_war_3.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_nord4",    "germ_war_4.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("ambushed_by_rhodok1",  "armenian_war.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok2",  "armenian_war_1.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok3",  "parthian_war_1.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok4",  "parthian_war_2.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok5",  "eastern_battle_new.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok6",  "eastern_battle_1.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_rhodok7",  "eastern_war_1.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("ambushed_by_swadian1", "dacian_war_1.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_swadian2", "dacian_war_2.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_swadian3", "dacian_war_3.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("ambushed_by_vaegir1",  "celtic_war_1.ogg", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("ambushed_by_sarranid1", "roman_war_1.ogg", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_sarranid2", "roman_war_2.ogg", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_sarranid3", "farya_hymn_of_legion.ogg", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

 ##new nomadic fight music
  ("ambushed_by_khergit1", "nomad_war_1.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit2", "nomad_war_2.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit3", "nomad_war_3.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit4", "nomad_war_4.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit5", "nomad_war_5.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit6", "ambushed_caoyuan_01.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("ambushed_by_khergit7", "ambushed_caoyuan_02.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),

  ("germanic_track_1", "germanic_track_1.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_sit_town|mtf_sit_travel, mtf_sit_fight|mtf_culture_all),
  ("germanic_track_2", "germanic_track_2.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_sit_town|mtf_sit_travel, mtf_sit_fight|mtf_culture_all),
  ("germanic_track_3", "germanic_track_3.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_sit_town|mtf_sit_travel, mtf_sit_fight|mtf_culture_all),

  ("arena_1", "arena_1.ogg", mtf_sit_arena, 0),
  ("armorer", "armorer.ogg", mtf_sit_travel, 0),
  ("bandit_fight", "bandit_fight.ogg", mtf_sit_fight|mtf_sit_ambushed, 0),

  ("calm_night_1", "calm_night_2.ogg", mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral_2", "defeated_1.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_4", "defeated_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("killed_by_khergit2", "killed_by_caoyuan_01.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_romans", "lost_battle.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

  ("fight_1", "battle_music_1.ogg", mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_2", "battle_theme_1.ogg", mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("fight_3", "battle_theme_2.ogg", mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("fight_4", "western_greek_theme.ogg", mtf_sit_siege, mtf_sit_tavern|mtf_sit_night|mtf_sit_travel|mtf_culture_all),
  ("fight_5", "eastern_battle_2.ogg", mtf_sit_siege, mtf_sit_tavern|mtf_sit_night|mtf_sit_travel|mtf_culture_all),

  ("neutral_infiltration", "wolf_1.ogg", mtf_sit_town_infiltrate, 0),
  ("neutral_infiltration_2", "birds_1.ogg", mtf_sit_town_infiltrate, 0),
  ("neutral_infiltration_3", "birds_2.ogg", mtf_sit_town_infiltrate, 0),
  ("infiltration_eastern", "eastern_tragic.ogg", mtf_culture_5|mtf_sit_town_infiltrate, mtf_culture_all),

  ("lords_hall_khergit1", "town_caoyuan_01.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),


  ("siege_attempt", "siege_attempt.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),

  ("tavern_1", "tavern_1.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "tavern_2.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_3", "tavern_3.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_roman_1", "roman_tavern_1.ogg", mtf_culture_6|mtf_sit_tavern|mtf_sit_feast|mtf_sit_thermae, 0),

  ("roman_feast_1", "roman_feast_1.ogg", mtf_sit_feast|mtf_sit_thermae, mtf_culture_6),

  ("town_neutral_0", "wolf_1.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_night, mtf_culture_all),
  ("town_neutral_1", "birds_1.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("town_neutral_2", "birds_2.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("town_neutral_3", "birds_3.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("town_neutral_4", "birds_4.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("town_neutral_5", "birds_5.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
  ("town_neutral_6", "birds_6.ogg", mtf_culture_all|mtf_sit_town|mtf_sit_travel|mtf_sit_siege|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),

  ("town_khergit1", "lords_hall_caoyuan_01.ogg", mtf_culture_3|mtf_sit_town, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("town_nord1", "germ_peace_4.ogg", mtf_culture_4|mtf_sit_town, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("town_rhodok1", "armenian_peace_3.ogg", mtf_culture_5|mtf_sit_town, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok2", "armenian_peace_4.ogg", mtf_culture_5|mtf_sit_town, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("town_swadian1", "dacian_peace_1.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian2", "dacian_peace_2.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("town_vaegir1", "celtic_peace_1.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir2", "celtic_peace_2.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir3", "celtic_peace_3.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("celtic_track_1", "celtic_track_1.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),


  ("town_roman", "roman_peace_1.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman1", "roman_peace_2.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman2", "roman_peace_3.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman3", "roman_peace_4.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman4", "common_roman_2.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman5", "common_sound.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman6", "roman_peace_5.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_roman7", "roman_peace_6.ogg", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_sit_thermae, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_khergit1", "nomad_peace_1.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_khergit2", "nomad_peace_2.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_khergit3", "nomad_peace_3.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_khergit4", "nomad_peace_4.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_khergit5", "travel_caoyuan_01.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_neutral0", "generic_1.ogg", mtf_culture_all|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_neutral2", "generic_2.ogg", mtf_culture_all|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_neutral3", "generic_3.ogg", mtf_culture_all|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_neutral4", "generic_4.ogg", mtf_culture_all|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),

  ("travel_nord1",    "germ_peace_1.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_nord2",    "germ_peace_2.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_nord3",    "germ_peace_3.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_rhodok1",  "eastern_peacefull.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok2",  "eastern_peacefull_2.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok3",  "eastern_peacefull_3.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok4",  "parhtian_peace_1.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok5",  "eastern_peacefull.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok6",  "eastern_peacefull_2.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok7",  "eastern_peacefull_3.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok8",  "parhtian_peace_1.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok9",  "arabian_music_1.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral", "victoria.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_new_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  ("final_glory", "finalglory.ogg", mtf_persist_until_finished, 0),
  ("triumph_track", "dream_of_babylon.ogg", mtf_persist_until_finished, 0),
  ("senate", "senatus.ogg", mtf_sit_multiplayer_fight, 0),
  ("legio_aeterna", "legio_aeterna.ogg", mtf_persist_until_finished, 0),
  ("cutscene_1_track", "western_greek_theme.ogg", mtf_persist_until_finished, 0),

  ("trailer_0", "eastern_battle_2.ogg", 0, mtf_sit_main_title),
  ("trailer_1", "legio_aeterna.ogg", 0, mtf_sit_main_title),
  ("trailer_2", "farya_hymn_of_legion.ogg", 0, mtf_sit_main_title),
  ("cutscene_2_track", "eastern_tragic.ogg", mtf_persist_until_finished, 0),
  ("cutscene_3_track", "eastern_battle_new.ogg", mtf_persist_until_finished, 0),
  ("cutscene_4_track", "dacian_war_2.ogg", mtf_persist_until_finished, 0),
  ("cutscene_5_track", "germ_war_4.ogg", mtf_persist_until_finished, 0),
  ("cutscene_fire_track", "generic_4.ogg", mtf_persist_until_finished, 0),
  ("cutscene_intro_1", "generic_2.ogg", mtf_persist_until_finished, 0),
  ("cutscene_to_hades", "to_hades.ogg", mtf_persist_until_finished, 0),

  ("cutscene_wedding", "to_hades.ogg", mtf_persist_until_finished, 0),
  ("cutscene_fleet", "cutscene_fleet.ogg", mtf_persist_until_finished, 0),
  ("cutscene_battle", "cutscene_battle.ogg", mtf_persist_until_finished, 0),
]
