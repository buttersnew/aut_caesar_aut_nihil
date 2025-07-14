from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from IDs.ID_sounds import *

#from compiler import *
####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale.
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.4
avatar_scale = 0.2

# ground_trigger = (ti_on_init_map_icon,
      # [
        # (store_trigger_param_1, ":party_no"),

      # ])

map_icons = [
  ("player",0,"slave", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("player_horseman",0,"slave_donkey", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("gray_knight",0,"vexillifer_icon_combinedd", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("vaegir_knight",0,"mercenary_infantry", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("flagbearer_a",0,"player_horseman1", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("khergit",0,"arab", avatar_scale,snd_gallop, 0.16, 0.173, 0),
  ("khergit_horseman_b",0,"steppbandit", avatar_scale,snd_gallop, 0.16, 0.173, 0),
  ("axeman",0,"bandit", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("hord",0,"horde", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),

  ("wonder_pyramids_egy",mcn_no_shadow,"wonder_pyramids_egy", 0.50,0),
  ("wonder_parthenon",mcn_no_shadow,"wonder_parthenon", 0.16,0),
  ("wonder_artemis",mcn_no_shadow,"wonder_artemis", 0.4,0),

  ("village_barbarian",mcn_no_shadow,"village_barbarian", 0.47, 0),
  ("village_barbarian_burned",mcn_no_shadow,"village_barbarian_burned", 0.47, 0),
  ("village_barbarian_deserted",mcn_no_shadow,"village_barbarian_burned", 0.47, 0),
  ("village_roman",mcn_no_shadow,"village_roman", 0.35,0),
  ("village_roman_burned",mcn_no_shadow,"village_roman_burned", 0.35,0),
  ("village_roman_deserted",mcn_no_shadow,"village_roman_burned", 0.35,0),
  ("village_greek",mcn_no_shadow, "village_greek", 0.35,0),
  ("village_greek_burned",mcn_no_shadow, "village_greek_burned", 0.35,0),
  ("village_greek_deserted",mcn_no_shadow, "village_greek_burned", 0.35,0),

  ("camp",mcn_no_shadow,"camp", 0.13, 0),
  ("camp_fort",mcn_no_shadow,"camp_fort", 0.13, 0),
  ("ship",mcn_no_shadow,"boat_sail", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"boat_sail_0", 0.23, 0),

  ("castle_a",mcn_no_shadow,"horde_camp", 0.15,0),
  ("castle_c",mcn_no_shadow,"farmstead", 0.42,0),

  ("map_island",mcn_no_shadow,"map_island", 0.5,0),
  ("map_stone_circle",mcn_no_shadow,"map_stone_circle", 0.35,0),
  ("map_temple",mcn_no_shadow,"map_temple", 0.37,0),
  ("map_persian_temple",mcn_no_shadow,"map_persian_temple", 0.37,0),
  ("map_bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),
  ("map_ludus",mcn_no_shadow,"map_ludus", 0.35,0),

  ("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.16, 0.173, 0),
  ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.16, 0.173, 0),

  ##free mapicons
  ("crucified_slave",mcn_no_shadow,"crucified_slave", 0.35,0),
  ("forest",mcn_no_shadow,"forest", 0.9,0),
  ("forest_palms",mcn_no_shadow,"forest_palms", 2.0,0),
  ("gaetulian_town",mcn_no_shadow,"icon_gaetulian",  0.34,0),
  ("arab_town",mcn_no_shadow,"icon_arab",  0.34,0),
  ("garamantian_town",mcn_no_shadow,"icon_garama",  0.28,0),
  ("village_desert",mcn_no_shadow,"icon_village_desert",  0.30,0),
  ("nubian_town",mcn_no_shadow,"icon_nubia",  0.33,0),

  ("mine",mcn_no_shadow,"mine", 0.45, 0),
  ("kingdom_1_soldier_b",0,"dac1_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("kingdom_2_soldier_b",0,"brit2_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("kingdom_3_soldier_b",0,"sarm2_re", avatar_scale, snd_gallop, 0.16, 0.173, 0),
  ("kingdom_4_soldier_b",0,"german1_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("kingdom_5_soldier_b",0,"eastern1_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("kingdom_6_soldier_b",0,"eastern1_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("kingdom_7_soldier_b",0,"rom_re", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),

  ("mountain_bandit",0,"banditrom", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),
  ("forest_bandit",0,"bandithisp", avatar_scale, snd_footstep_grass, 0.16, 0.173, 0),

  ("german1",0,"german1", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("brit1",0,"brit1", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("dac1",0,"dac1", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("eastern1",0,"eastern1", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),
  ("sarm1",0,"sarm1", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),

  ("numider",0,"numider", avatar_scale,snd_footstep_grass, 0.16, 0.173, 0),

  ("pretorian_eques",0,"pretorian_eques", avatar_scale,snd_gallop, 0.16, 0.173, 0),
  ("legat",0,"legat", avatar_scale,snd_gallop, 0.16, 0.173, 0),
  ("aux2",0,"aux2", avatar_scale,snd_gallop, 0.16, 0.173, 0),


  ("opidumn_rock_Reduced",mcn_no_shadow,"opidumn_rock_Reduced", 0.30,0),
  ("opidumn_rock1_Reduced",mcn_no_shadow,"opidumn_rock1_Reduced", 0.30,0),
  ("opidumn_wood_gl1_Reduced",mcn_no_shadow,"opidumn_wood_gl1_Reduced", 0.30,0),
  ("opidumn_wood_gl_Reduced",mcn_no_shadow,"opidumn_wood_gl_Reduced", 0.30,0),

  ("fort_roman",mcn_no_shadow,"fort_roman", 0.35,0),
  ("fort_greek",mcn_no_shadow,"fort_greek", 0.35,0),
  ("fort_persian",mcn_no_shadow,"fort_persian", 0.35,0),

  ("town_roman",mcn_no_shadow,"town_roman", 0.35,0),
  ("town_greek",mcn_no_shadow,"town_greek", 0.35,0),
  ("town_persian",mcn_no_shadow,"town_persian", 0.35,0),

  ("town_rome",mcn_no_shadow,"town_rome", 0.35,0),
  ("town_rome_after_fire",mcn_no_shadow,"town_rome_after_fire", 0.35,0),
  ("town_rome_before_fire",mcn_no_shadow,"town_rome_before_fire", 0.35,0),

  ("town_athen",mcn_no_shadow, "town_athen", 0.35,0),
  ("town_jerusalem_temple",mcn_no_shadow, "town_jerusalem_temple", 0.35,0),
  ("town_jerusalem_without_temple",mcn_no_shadow, "town_jerusalem_without_temple", 0.35,0),
  ("town_alexandria",mcn_no_shadow,"town_alexandria", 0.35,0),
  ("town_alexandria_lighthouse",mcn_no_shadow,"town_alexandria_lighthouse", 0.5,0),

  ("opidumn_wood_br_Reduced",mcn_no_shadow,"opidumn_wood_br_Reduced", 0.30,0),
  ("opidumn_wood_br1_Reduced",mcn_no_shadow,"opidumn_wood_br1_Reduced", 0.30,0),
  ("opidumn_wood_dc1_Reduced",mcn_no_shadow,"opidumn_wood_dc1_Reduced", 0.30,0),
  ("opidumn_wood_dc_Reduced",mcn_no_shadow,"opidumn_wood_dc_Reduced", 0.30,0),
  ("opidumn_rock_dc_Reduced",mcn_no_shadow,"opidumn_rock_dc_Reduced", 0.30,0),
  ("opidumn_rock_dc1_Reduced",mcn_no_shadow,"opidumn_rock_dc1_Reduced", 0.30,0),
  ("ferry_station",mcn_no_shadow,"ferry_station", 1.0,0),
  ("grain_fields",mcn_no_shadow,"grain_fields", 0.35,0),

  ("camp_siege",mcn_no_shadow,"camp_siege", 0.13, 0),
  ("ship_merchant",mcn_no_shadow,"boat_sail_on7_Reduced", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
  ("boat_simple",mcn_no_shadow,"boat_sail_on71", 0.23, snd_footstep_grass, 0.0, 0.05, 0),

  ("white_flag",0,"custom_map_banner_02", banner_scale, 0, [
     (ti_on_init_map_icon,
      [
          (troop_set_slot, "trp_temp_troop", slot_troop_custom_banner_bg_color_1, 0xFFFFFFFF),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", "trp_temp_troop"),
        ]),
  ]),

  ("landing_point", mcn_no_shadow, "empty", 0, 0),
  ("villa_icon",mcn_no_shadow,"villa_icon", 0.35,0),
  ("sartemis_icon",mcn_no_shadow,"hanging_gardens_icon", 0.95,0),
  ("valley_of_kings_combined",mcn_no_shadow,"valley_of_kings_combined", 0.95,0),

  ("roman_house",mcn_no_shadow,"icon_roman_house", 0.5,0),
  ("barbarian_estate",mcn_no_shadow,"barbarian_estate", 0.5,0),

##there is limit for map icons, however, this limit does not apply to banners

  ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", "trp_player"),
        ]),
     ]),
  ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", "trp_player"),
        ]),
     ]),
  ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", "trp_player"),
        ]),
     ]),

  # Banners
  ##kingdom banners
  ("map_flag_kingdom_1",0,"map_flag_kingdom_1", banner_scale,0),
  ("map_flag_kingdom_2",0,"map_flag_kingdom_2", banner_scale,0),
  ("map_flag_kingdom_3",0,"map_flag_kingdom_3", banner_scale,0),
  ("map_flag_kingdom_4",0,"map_flag_kingdom_4", banner_scale,0),
  ("map_flag_kingdom_5",0,"map_flag_kingdom_5", banner_scale,0),
  ("map_flag_kingdom_6",0,"map_flag_kingdom_6", banner_scale,0),
  ("map_flag_kingdom_7",0,"map_flag_kingdom_7", banner_scale,0),
  ("map_flag_kingdom_8",0,"map_flag_kingdom_8", banner_scale,0),
  ("map_flag_kingdom_9",0,"map_flag_kingdom_9", banner_scale,0),
  ("map_flag_kingdom_10",0,"map_flag_kingdom_10", banner_scale,0),
  ("map_flag_kingdom_11",0,"map_flag_kingdom_11", banner_scale,0),
  ("map_flag_kingdom_12",0,"map_flag_kingdom_12", banner_scale,0),
  ("map_flag_kingdom_13",0,"map_flag_kingdom_13", banner_scale,0),
  ("map_flag_kingdom_14",0,"map_flag_kingdom_14", banner_scale,0),
  ("map_flag_kingdom_15",0,"map_flag_kingdom_15", banner_scale,0),
  ("map_flag_kingdom_16",0,"map_flag_kingdom_16", banner_scale,0),
  ("map_flag_kingdom_17",0,"map_flag_kingdom_17", banner_scale,0),
  ("map_flag_kingdom_18",0,"map_flag_kingdom_18", banner_scale,0),
  ("map_flag_19",0,"map_flag_19", banner_scale,0),
  ("map_flag_20",0,"map_flag_20", banner_scale,0),
  ("map_flag_21",0,"map_flag_21", banner_scale,0),
  ("map_flag_22",0,"map_flag_22", banner_scale,0),
  ("map_flag_23",0,"map_flag_23", banner_scale,0),
  ("map_flag_24",0,"map_flag_24", banner_scale,0),
  ("map_flag_25",0,"map_flag_25", banner_scale,0),
  ("map_flag_26",0,"map_flag_26", banner_scale,0),
  ("map_flag_27",0,"map_flag_27", banner_scale,0),
  ("map_flag_28",0,"map_flag_28", banner_scale,0),
  ("map_flag_29",0,"map_flag_29", banner_scale,0),
  ("map_flag_30",0,"map_flag_30", banner_scale,0),
  ("map_flag_31",0,"map_flag_31", banner_scale,0),
  ("map_flag_32",0,"map_flag_32", banner_scale,0),
  ("map_flag_33",0,"map_flag_33", banner_scale,0),
  ("map_flag_34",0,"map_flag_34", banner_scale,0),
  ("map_flag_35",0,"map_flag_35", banner_scale,0),
  ("map_flag_36",0,"map_flag_36", banner_scale,0),
  ("map_flag_37",0,"map_flag_37", banner_scale,0),
  ("map_flag_38",0,"map_flag_38", banner_scale,0),
  ("map_flag_39",0,"map_flag_39", banner_scale,0),
  ("map_flag_40",0,"map_flag_40", banner_scale,0),
  ("map_flag_41",0,"map_flag_41", banner_scale,0),
  ("map_flag_42",0,"map_flag_42", banner_scale,0),

  ("map_legion_vexilium_italica_ii",0,"map_legion_vexilium_italica_ii", banner_scale,0),
  ("map_legion_vexilium_scythica_iv",0,"map_legion_vexilium_scythica_iv", banner_scale,0),
  ("map_legion_vexilium_fulminata_xii",0,"map_legion_vexilium_fulminata_xii", banner_scale,0),
  ("map_legion_vexilium_amogus_lxix",0,"map_legion_vexilium_amogus_lxix", banner_scale,0),
  ("map_legion_vexilium_minervia_i",0,"map_legion_vexilium_minervia_i", banner_scale,0),
  ("map_legion_vexilium_uplia_victrix_xxx",0,"map_legion_vexilium_uplia_victrix_xxx", banner_scale,0),
  ("map_legion_vexilium_biggus_dickus_cdxx",0,"map_legion_vexilium_biggus_dickus_cdxx", banner_scale,0),
  ("map_legion_vexilium_texticulus_xxx",0,"map_legion_vexilium_texticulus_xxx", banner_scale,0),
  ("map_legion_vexilium_parthica_i",0,"map_legion_vexilium_parthica_i", banner_scale,0),
  ("map_legion_vexilium_valeria_xx",0,"map_legion_vexilium_valeria_xx", banner_scale,0),
  ("map_legion_vexilium_hispania_ix",0,"map_legion_vexilium_hispania_ix", banner_scale,0),
  ("map_legion_vexilium_apollinaris_xv",0,"map_legion_vexilium_apollinaris_xv", banner_scale,0),
  ("map_legion_vexilium_primigenia_xxii",0,"map_legion_vexilium_primigenia_xxii", banner_scale,0),
  ("map_legion_vexilium_deitoriana_xxi",0,"map_legion_vexilium_deitoriana_xxi", banner_scale,0),
  ("map_legion_vexilium_gallica_xvi",0,"map_legion_vexilium_gallica_xvi", banner_scale,0),
  ("map_legion_vexilium_germanica_i",0,"map_legion_vexilium_germanica_i", banner_scale,0),
  ("map_legion_vexilium_praetorian",0,"map_legion_vexilium_praetorian", banner_scale,0),
  ("map_legion_vexilium_adiutrix_i",0,"map_legion_vexilium_adiutrix_i", banner_scale,0),
  ("map_legion_vexilium_victrix_vi",0,"map_legion_vexilium_victrix_vi", banner_scale,0),
  ("map_legion_vexilium_rapax_xxi",0,"map_legion_vexilium_rapax_xxi", banner_scale,0),
  ("map_legion_vexilium_alaudae_v",0,"map_legion_vexilium_alaudae_v", banner_scale,0),
  ("map_legion_vexilium_augusta_iii",0,"map_legion_vexilium_augusta_iii", banner_scale,0),
  ("map_legion_vexilium_claudia_xi",0,"map_legion_vexilium_claudia_xi", banner_scale,0),
  ("map_legion_vexilium_ferrata_vi",0,"map_legion_vexilium_ferrata_vi", banner_scale,0),
  ("map_legion_vexilium_fretensis_x",0,"map_legion_vexilium_fretensis_x", banner_scale,0),
  ("map_legion_vexilium_macedonica_v",0,"map_legion_vexilium_macedonica_v", banner_scale,0),
  ("map_legion_vexilium_gemina_xiii",0,"map_legion_vexilium_gemina_xiii", banner_scale,0),
  ("map_legion_vexilium_galbiana_vii",0,"map_legion_vexilium_galbiana_vii", banner_scale,0),

  ("banners_end",0,"map_flag_42", banner_scale,0),
 ]
