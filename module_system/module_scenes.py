from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

#from compiler import *
####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}.
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
####################################################################################################################

scenes = [
  ("random_scene", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], []),
  ("conversation_scene", 0, "encounter_spot", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("water", 0, "none", "none", (-1000, -1000), (1000, 1000), -0.5, "0",[], []),
  ("random_scene_steppe", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000229602800000691a400003efe00004b34000059be",[], [], "outer_terrain_steppe"),
  ("random_scene_plain", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000229602800000691a400003efe00004b34000059be",[], [], "outer_terrain_plain"),
  ("random_scene_snow", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000229602800000691a400003efe00004b34000059be",[], [], "outer_terrain_plain_1"),
  ("random_scene_desert", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000229602800000691a400003efe00004b34000059be",[], [], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_plain"),
  ("random_scene_plain_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_plain"),
  ("random_scene_snow_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_mountain"),
  ("random_scene_desert_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_desert"),
  ("camp_scene", sf_generate|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_plain"),
  ("camp_scene_horse_track", sf_generate|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be",[], [], "outer_terrain_plain"),
  ("four_ways_inn", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030015f2b000350d4000011a4000017ee000054af",[], [], "outer_terrain_plain"),
  ("test_scene", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0230817a00028ca300007f4a0000479400161992",[], [], "outer_terrain_plain"),
  ("quick_battle_1", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001ca00989e000c0300000000b30000480700006d62",[], [], "outer_terrain_plain"),
  ("quick_battle_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0xa0425ccf0004a92a000063d600005a8a00003d9a",[], [], "outer_terrain_steppe"),
  ("quick_battle_3", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x4c6024e3000691a400001b7c0000591500007b52",[], [], "outer_terrain_steppe"),
  ("quick_battle_4", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00001d63c005114300006228000053bf00004eb9",[], [], "outer_terrain_plain"),
  ("quick_battle_5", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001c00005000004651a000000b30000480700006d62",[], [], "outer_terrain_plain"),
  ("quick_battle_6", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0xa0425ccf0004a92a000063d600005a8a00003d9a",[], [], "outer_terrain_steppe"),
  ("quick_battle_7", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x314d060900036cd70000295300002ec9000025f3",[], [], "outer_terrain_plain"),
  ("novice_ground", sf_indoors, "training_house_a", "bo_training_house_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("reserved4", sf_generate, "none", "none", (0, 0), (120, 120), -100, "28791",[], []),
  ("reserved5", sf_generate, "none", "none", (0, 0), (120, 120), -100, "117828",[], []),
  ("reserved6", sf_generate, "none", "none", (0, 0), (100, 100), -100, "6849",[], []),
  ("reserved7", sf_generate, "none", "none", (0, 0), (100, 100), -100, "6849",[], []),
  ("reserved8", sf_generate, "none", "none", (0, 0), (100, 100), -100, "13278",[], []),
  ("reserved9", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100, -100), (100, 100), -100, "0",[], []),
  ("reserved10", 0, "none", "none", (-100, -100), (100, 100), -100, "0",[], []),
  ("reserved11", 0, "none", "none", (-100, -100), (100, 100), -100, "0",[], []),
  ("reserved12", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100, -100), (100, 100), -100, "0",[], []),
  ("training_ground", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x30000500400360d80000189f00002a8380006d91",[], ["town_27_seneschal", "town_28_seneschal"], "outer_terrain_plain_1"),
  ("tutorial_1", sf_indoors, "tutorial_1_scene", "bo_tutorial_1_scene", (-100, -100), (100, 100), -100, "0",[], []),
  ("tutorial_2", sf_indoors, "tutorial_2_scene", "bo_tutorial_2_scene", (-100, -100), (100, 100), -100, "0",[], []),
  ("tutorial_3", sf_indoors, "tutorial_3_scene", "bo_tutorial_3_scene", (-100, -100), (100, 100), -100, "0",[], []),
  ("tutorial_4", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x30000500400360d80000189f00002a8380006d91",[], [], "outer_terrain_plain"),
  ("tutorial_5", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x3a06dca80005715c0000537400001377000011fe",[], [], "outer_terrain_plain"),

  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_plain"),
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_steppe"),
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),
  ("training_ground_ranged_melee_1", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001350455c20005194a000041cb00005ae800000ff5",
  [], [], "outer_terrain_plain"),
  ("training_ground_ranged_melee_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000532c8dccb0005194a000041cb00005ae800001bdd",
  [], [], "outer_terrain_plain"),
  ("training_ground_ranged_melee_3", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000054327dcba0005194a00001b1d00005ae800004d63",
  [], [], "outer_terrain_plain"),
  ("training_ground_ranged_melee_4", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000012247dcba0005194a000041ef00005ae8000050af",
  [], [], "outer_terrain_steppe"),
  ("training_ground_ranged_melee_5", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001324a9cba0005194a000041ef00005ae800003c55",
  [], [], "outer_terrain_plain"),

  ("town_1_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300000000005e97e00005bda0000da66000033a2",[], [], "outer_terrain_plain"),
  ("town_2_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000050000500400370e000002236000043df0000369c",[], [], "outer_terrain_steppe"),
  ("town_3_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_4_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x3002cd340002b4ac00002ccd800026dc00000c1d",[], [], "outer_terrain_plain"),
  ("town_15_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000005f57b00005885000046bd00006d9c",[], [], "outer_terrain_plain"),
  ("town_22_center", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",[], [], "outer_terrain_steppe"),
  ("town_1_castle", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_2_castle", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x0000000050000500400370e000002236000043df0000369c",[], []),
  ("town_3_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_4_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_15_castle", sf_indoors, "none", "none", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_22_castle", sf_indoors, "gallic_interior_a", "bo_gallic_interior_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_1_tavern", sf_indoors, "oil_press_interior", "bo_oil_press_interior", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_2_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_3_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_4_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_15_tavern", sf_indoors, "celt_tavern_interior", "bo_celt_tavern_interior", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_22_tavern", sf_indoors, "celt_tavern_interior", "bo_celt_tavern_interior", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_1_store", sf_indoors, "smithy_interior", "bo_smithy_interior", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_2_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_3_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_4_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_15_store", sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_22_store", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_1_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("town_2_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000005f57b00005885000046bd00006d9c",[], [], "outer_terrain_steppe"),
  ("town_3_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_4_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("town_15_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("town_22_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000811ff00007c1000000733000040f4",[], [], "outer_terrain_steppe"),
  ("town_1_prison", sf_indoors, "smithy_interior", "bo_smithy_interior", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_2_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_3_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_4_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("town_15_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_22_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_1_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300000000005e97e00005bda0000da66000033a2",[], [], "outer_terrain_plain"),
  ("town_2_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000050000500400370e000002236000043df0000369c",[], [], "outer_terrain_steppe"),
  ("town_3_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_4_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_plain"),
  ("town_15_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000005f57b00005885000046bd00006d9c",[], [], "outer_terrain_plain"),
  ("town_22_walls", sf_generate, "none", "none", (0, 0), (220, 220), -100, "0x0000000220000500000811ff00007c1000000733000040f4",[], [], "outer_terrain_steppe"),
  #this is used for start mission
  ("town_1_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932",[], [], "outer_terrain_plain"),

  ("dacian_castle_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_mountain_2"),
  ("dacian_castle_in", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacian_castle_prison", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_germanic_east_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_mountain"),
  ("castle_germanic_east_in", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_germanic_east_prison", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_germanic_sea_1_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_beach"),
  ("castle_germanic_sea_1_in", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_germanic_sea_1_prison", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("carnuntum_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_plain"),
  ("carnuntum_in", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("carnuntum_prison", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_island_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_beach"),
  ("castle_island_in", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_island_prison", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_island_2_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_beach"),
  ("castle_island_2_in", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),


  ("castle_1_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300000000006a9a7000015ef0000d7a600005095",[], [], "outer_terrain_steppe"),
  ("castle_1_interior", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_1_prison", sf_indoors, "smithy_interior", "bo_smithy_interior", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_2_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130025cb20006097f00005b1400000e2f00005fd9",[], [], "outer_terrain_plain"),
  ("castle_2_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_2_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_3_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000049d2a00003c37000040ef000037cd",[], [], "outer_terrain_steppe"),
  ("castle_3_interior", sf_indoors, "none", "none", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_3_prison", sf_indoors, "none", "none", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_4_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007a3b20005795e0000706d0000381800000bbc",[], [], "outer_terrain_plain"),
  ("castle_4_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_4_prison", sf_indoors, "interior_prison_h", "bo_interior_prison_h", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_5_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007b23200049d2a00003c37000040ef000037cd",[], [], "outer_terrain_plain"),
  ("castle_5_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_5_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_6_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000061d84000059e200002ff200000e3d",[], [], "outer_terrain_plain"),
  ("castle_6_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_6_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_7_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130025cb20006097f00005b1400000e2f00005fd9",[], [], "outer_terrain_plain"),
  ("castle_7_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_7_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ("roman_castle_1_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007858000049d2a00003c37000040ef000037cd",[], [], "outer_terrain_plain"),
  ("roman_castle_1_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("roman_castle_2_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),
  ("roman_castle_2_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

  #parthian villages
  ("village_parthian_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000022007a7b200045d19000004920000076d00003b0a",[], [], "outer_terrain_steppe"),
  ("village_parthian_2", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000085e190000131d000064ff00003ac0",[], [], "outer_terrain_steppe"),
  ("village_43", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000022002de4c00077ddd00007e1300000af400006de1",[], [], "outer_terrain_steppe"),
  #end parthian villages

  #fac_culture_2,fac_culture_1
  ("village_7", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023009629a0005615800005564000023590000579e",[], [], "outer_terrain_plain"),
  ("village_19", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002b00000000006e5be00008f330000e9130000533d",[], [], "outer_terrain_plain"),
  #fac_culture_1 only
  ("village_95", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002314008e300098a6300005d7100001aac00005cb6",[], [], "outer_terrain_plain_2"),

  #Roman villages begin
  ("village_41", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220031f6300076dda000056f100004f6d000070b3",[], [], "outer_terrain_plain"),
  ("village_roman_town", sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000007a1e800000b5400003ad100005795 ",  [],[],"outer_terrain_plain"),
  ("village_roman_b_river", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4 ",  [],[],"outer_terrain_plain_2"),
  ("village_roman_b", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4 ",  [],[],"outer_terrain_plain_1"),
  ("village_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030081763000589620000338e00004f2c00005cfb",[], [], "outer_terrain_plain"),
  #Roman villages end

  #fac_culture_3
  ("village_42", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000811ff000072770000522d00001d47",[], [], "outer_terrain_steppe"),
  ("village_100", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000811ff000072770000522d00001d47",[], [], "outer_terrain_steppe"),

  #fac_culture_5
  ("village_44", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001200513940005314c00001f6d00006d7700006698",[], [], "outer_terrain_steppe"),

  #fac_culture_4
  ("village_98", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000081204000034c4000020f200000e60",[], [], "outer_terrain_plain"),
  ("village_74", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_plain"),

  #ctesiphon villages
  ("village_94", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001500410320005a96800006b5300004edc00000d11",[], [], "outer_terrain_desert"),

  #generic desert village
  ("village_102", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001500410320005a96800006b5300004edc00000d11",[], [], "outer_terrain_desert"),

  #other speical villages
  ("village_103", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300005000003a8ea00006acd0000637600004d7f",[], [], "outer_terrain_plain"),
  ("village_104", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300005000003ccf300005ffe0000621800003824",[], [], "outer_terrain_plain_1"),
  ("village_152", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000234a01c3c0005e97900002ad30000589000000c2b",[], [], "outer_terrain_plain"),
  ("village_153", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023a003239000579610000351b000013a60000135f",[], [], "outer_terrain_plain_1"),
  ("village_154", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000024a002d320006398b0000044f0000590600001011",[], [], "outer_terrain_plain"),
  ("village_58", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000232200ebc0005e9790000280900003a9c00006d70",[], [], "outer_terrain_plain_1"),

  ("village_egypt", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001500003e3000fffff0000074800005c49000021c5",[], [], "outer_terrain_desert"),
  ("village_egypt_delta", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000025c600606000926470000240d0000747200007110",[], [], "outer_terrain_desert_b"),

  ("village_judea", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000255c0050000076ddb000065a900005a1700006e50",[], [], "outer_terrain_desert"),

  ("village_caledonian", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain_2"),

  ("village_dacian", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000300000170003ed06000041ef00005ae800003c55",[], [], "outer_terrain_mountain"),

  ("village_east_germanic", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_plain_1"),

  ("village_east_germanic_coastal", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002a0000500000d234800007d8e00006aca00005ad8",[], [], "outer_terrain_beach"),

  ("village_germanic_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain_1"),

  ("village_island", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_beach_med"),

  ("village_palma", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000242c005000006c1b1000055bb00007699000051a2",[], [], "outer_terrain_beach_med"),

  ("village_palmyra", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], [], "outer_terrain_desert"),
  ("village_euphrat", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000240c005630007e9fa0000750f0000246e00000c0b",[], [], "outer_terrain_desert"),
  ("village_babylon", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], [], "outer_terrain_desert"),

  ("village_spain", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000242c005000006c1b1000055bb00007699000051a2",[], [], "outer_terrain_plain"),

  ("village_patrae", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000024a000ee300081e070000718f00004c1400000f0a",[], [], "outer_terrain_beach_med"),

  ("village_ephesus", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000023000050000087a1f0000222c00004f4b00004a95",[], [], "outer_terrain_mountain"),

  ("village_africa_coastal", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_beach_med"),

  ("roman_village_african", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000250000500000755d5000015f5000061ff0000122e",[], [], "outer_terrain_desert"),

  ("village_bosporan", sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004c13100001d3100006d4100001edd",  [],[],"outer_terrain_beach"),


  ("village_spain_1", sf_generate,"none", "none", (0,0),(100,100),-100, "0x0000000020004500000719c400002bac000064fb00005e4a",  [],[],"outer_terrain_plain_2"),
  ("village_spain_2", sf_generate,"none", "none", (0,0),(100,100),-100, "0x00000000200005000008ee3d00007f2800006a9100006095",  [],[],"outer_terrain_plain_3"),
  ("village_spain_3", sf_generate,"none", "none", (0,0),(100,100),-100, "0x000000003000050000063992000001970000443d000036c3",  [],[],"outer_terrain_plain"),
  ("village_spain_4", sf_generate,"none", "none", (0,0),(100,100),-100, "0x000000003000050000063992000001970000443d000036c3",  [],[],"outer_terrain_plain"),
  ("village_spain_5", sf_generate,"none", "none", (0,0),(100,100),-100, "0x000000003000050000059d670000359600004ac200003dcf",  [],[],"outer_terrain_plain"),

  ("village_persia_1", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002000050000059d670000359600004ac200003dcf",  [],[],"outer_terrain_plain"),
  ("village_persia_2", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002000050000059d670000359600004ac200003dcf",  [],[],"outer_terrain_plain"),
  ("village_persia_3", sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002000050000059d670000359600004ac200003dcf",  [],[],"outer_terrain_plain"),

  ("roman_village_mountain", sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300000000005194a000041ef00005ae800003c55",  [],[],"outer_terrain_mountain_2"),

  ("field_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000033a059a5a0009525600002005000060e300001175",[], [], "outer_terrain_plain"),
  ##useless
  ("field_2", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000033a079a3f000a3a8000006dfd000030a100006522",[], [], "outer_terrain_steppe"),
  ("test2", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000b0078cb20003fd0000005e480000288c0000286f",[], [], "outer_terrain_steppe"),
  ("test3", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000b00511d98004b12e0000039f00004e6300005c7d",[], [], "outer_terrain_plain"),

  ("wedding", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000300005000004c131000024c70000030f00000363",[], [], "outer_terrain_plain"),
  ("lair_steppe_bandits", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000200c69ac80043d0d0000556b0000768400003ea9",[], [], "outer_terrain_steppe"),
  ("lair_saka", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000200c69ac80043d0d0000556b0000768400003ea9",[], [], "outer_terrain_steppe"),
  ("lair_taiga_bandits", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000004c079c3e000499280000420f0000495d000048d6",[], [], "outer_terrain_plain"),
  ("lair_desert_bandits", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000005024cd120005595400003882000037a90000673e",[], [], "outer_terrain_desert"),
  ("lair_forest_bandits", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000b00326d90003ecfb0000657e0000213500002461",[], [], "outer_terrain_plain"),
  ("lair_mountain_bandits", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000200434070004450c000022bf00006ad6000060ed",[], [], "outer_terrain_desert"),
  ("lair_sea_raiders", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000b00562e200040900000063f40000679f00006cda",[], [], "outer_terrain_beach"),
  ("lair_african", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000005024cd120005595400003882000037a90000673e",[], [], "outer_terrain_desert"),
  ("lair_african_2", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000005024cd120005595400003882000037a90000673e",[], [], "outer_terrain_desert"),
  ("lair_arabian", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000005024cd120005595400003882000037a90000673e",[], [], "outer_terrain_desert"),
  ("lair_pirates", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000003000000000036cd5000041ef00005ae800003c55",[], [], "outer_terrain_beach"),

  ("quick_battle_scene_1", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001ca00989e000c0300000000b30000480700006d62",[], [], "outer_terrain_plain"),
  ("quick_battle_scene_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000250001d630005114300006228000053bf00004eb9",[], [], "outer_terrain_desert_b"),
  ("quick_battle_scene_3", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000023002b76300046d2400000190000076300000692a",[], [], "outer_terrain_plain"),
  ("quick_battle_scene_4", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000025a00f23700057d5f00006d6a000050ba000036df",[], [], "outer_terrain_desert_b"),
  ("quick_battle_scene_5", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001c00005000004651a000000b30000480700006d62",[], [], "outer_terrain_plain"),
  ("quick_battle_maps_end", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300389800003a4ea000058340000637a0000399b",[], [], "outer_terrain_plain"),
  ("tutorial_training_ground", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], [], "outer_terrain_plain"),

  ##vila of starting merchant player can buy
  ("town_6_room", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], ["tutorial_chest_2"], "outer_terrain_plain"),

  ("meeting_scene_steppe", 0, "ch_meet_steppe_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_plain", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_snow", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_desert", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_steppe_forest", 0, "ch_meet_steppe_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_plain_forest", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_snow_forest", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("meeting_scene_desert_forest", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_tannery", sf_generate, "ch_meet_steppe_a", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0x000000012004480500040902000041cb00005ae800000ff5",[], []),
  ("enterprise_winery", sf_indoors, "winery_interior", "bo_winery_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_mill", sf_indoors, "mill_interior", "bo_mill_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_smithy", sf_indoors, "smithy_interior", "bo_smithy_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_dyeworks", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_linen_weavery", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_wool_weavery", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_brewery", sf_indoors, "brewery_interior", "bo_brewery_interior", (-40, -40), (40, 40), -100, "0",[], []),
  ("enterprise_oil_press", sf_indoors, "oil_press_interior", "bo_oil_press_interior", (-40, -40), (40, 40), -100, "0",[], []),

  ("camp_scene_snow", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000054327dcba0005194a00001b1d00005ae800004d63",[], [], "outer_terrain_plain_1"),
  ("camp_scene_steppe", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000012247dcba0005194a000041ef00005ae8000050af",[], [], "outer_terrain_steppe"),
  ("camp_scene_plain", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001324a9cba0005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("camp_scene_desert", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_desert_b"),

  ##ambush maps
  ("river_ambush_1", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000003001ce100006097d0000134c000016d8000042a2",[], [], "outer_terrain_plain"),
  ("river_ambush_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000004300005008005b57000004e31800017d80000754b",[], [], "outer_terrain_plain"),
  ("river_ambush_3", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_plain"),

  ("ambushed_mountains", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_mountain"),
  ("ambushed_mountains_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000003300005000008f642000004c900005f7f0000071c",[], [], "outer_terrain_mountain_2"),

  ("ambushed_mountains_desert", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_desert_mountain"),
  ("ambushed_mountains_desert_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000003200005000008f642000041ae000050c30000695a",[], [], "outer_terrain_desert_mountain"),

  ("ambushed_desert", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_desert"),
  ("ambushed_desert_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000003d2a005000008f642000064a50000561600005c6b",[], [], "outer_terrain_desert"),

  ##ambsuch med
  ("ambushed_mediterran_forest", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002cc62a45a0005f17c00006c5a00004529000034f8",[], [], "outer_terrain_plain"),
  ("ambushed_mediterran_forest_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000003c2a005000008f642000064a50000561600005c6b",[], [], "outer_terrain_plain"),

  ("ambushed_mediterran", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000004b4354940005f17900003c3c0000439900003972",[], [], "outer_terrain_plain"),
  ("ambushed_mediterran_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000003400005000008f642000064a50000561600005c6b",[], [], "outer_terrain_plain"),

  ("ambushed_forest", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000002bc6261630006799d000025a700000eac000014c1",[], [], "outer_terrain_plain"),
  ("ambushed_forest_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000003b28005000008f6420000084f0000561600003f43",[], [], "outer_terrain_plain"),

  ("ambushed_plain", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_plain"),
  ("ambushed_plain_2", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x00000003300005000008f642000041ae000050c30000695a",[], [], "outer_terrain_plain"),

  ("ambush_scenes_end", sf_generate, "none", "none", (0, 0), (240, 240), -100, "0x000000013002541c00062d8b00000a01000068cb00006d9b",[], [], "outer_terrain_plain"),

  #special scenes
  ("temple_of_bacchus", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_mars", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_jupiter", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_aphrodite", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_castorpollux", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_mithras", sf_indoors, "dungeon_cell_mithras", "bo_dungeon_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("temple_of_concordia", sf_generate, "none", "none", (0, 0), (100, 100), -200, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_saturn", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("temple_of_vesta", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("random_scene_mountain", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000235e201c40005194a0000a29f00005ae800003c55",[], [], "outer_terrain_mountain"),
  ("imperial_palace", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002300000000004fd4a000041ef00005ae800003c55",[], ["bonus_chest_7"], "outer_terrain_plain"),
  ("imperial_garden", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002300000000004fd4a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("imperial_dinning_room", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("imperial_bed_room", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_12"]),
  ("imperial_palace_augusta_room", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_13"]),
  ("underworld", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000235e201c40005194a0000a29f00005ae800003c55",[], [], "outer_terrain_plain"),

  ("castle_56_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007941f0005415000007e650000225f00003b3e",[], [], "outer_terrain_plain"),
  ("castle_56_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_56_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",["exit"], []),


  ("town_germanic_east_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_mountain"),
  ("town_germanic_east_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_mountain"),
  ("town_germanic_east_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023000050000076ddb000029ba000027660000651a",[], [], "outer_terrain_mountain"),
  ("town_germanic_east_castle", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_germanic_east_tavern", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_germanic_east_store", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_germanic_east_prison", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("town_26_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_26_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_26_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_26_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_26_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_26_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_26_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("town_34_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("town_34_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_34_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x3002cd340002b4ac00002ccd800026dc00000c1d",[], [], "outer_terrain_plain"),
  ("town_34_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_34_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_34_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_34_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_plain"),
  ("town_20_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("town_20_castle", sf_indoors|sf_force_skybox, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_20_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_desert"),
  ("town_20_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_20_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_20_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_20_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_plain"),
  ## large battlemaps

  #REGIONAL MAPS
  # done
  ("battle_persian_hills_desert", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d4a0098000092a4a00007ee00000704600005611 ",[], [], "outer_terrain_desert"),
  ("battle_persian_hills_desert_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c005000009926300000dbc000049c400005816 ",[], [], "outer_terrain_desert"),
  ("battle_persian_hills_desert_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c0050000099263000045140000011d000072c7 ",[], [], "outer_terrain_desert"),
  ("battle_persian_hills_desert_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c00500000992630000794800007da900001d87 ",[], [], "outer_terrain_desert"),
  ("battle_persian_hills_desert_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002d8c005000009926300000ace00007da900000096 ",[], [], "outer_terrain_desert"),
  ("battle_persian_hills_desert_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000005a024714000d23480000076300004ce100002de9 ",[], [], "outer_terrain_desert_mountain"),
  ("battle_persian_hills_desert_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000005a191e00000d234800003cce0000047a00005bc2 ",[], [], "outer_terrain_desert_mountain"),
  ("battle_persian_hills_desert_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000005a024714000d23480000076300004ce100002de9 ",[], [], "outer_terrain_desert_mountain"),

  #done
  ("battle_spain", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000098000092a4a00007aec000020060000135c ",[], [], "outer_terrain_plain_2"),
  ("battle_spain_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000241200f000009aa6c00005b9f0000010e00001f4c ",[], [], "outer_terrain_steppe_2"),
  ("battle_spain_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000f000009aa6c0000717a0000541600005727 ",[], [], "outer_terrain_steppe"),
  ("battle_spain_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200005000009aa6c00006b7b00007984000029cb ",[], [], "outer_terrain_steppe"),
  ("battle_spain_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200009800009aa6c000011f900007984000029cb ",[], [], "outer_terrain_steppe_2"),

  #done
  ("battle_mesopotamia", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024560050000092a4a00005d5f00004f6000006eed ",[], [], "outer_terrain_beach_desert"),
  ("battle_mesopotamia_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002200008e300095a5900005a7c000009d100001667 ",[], [], "outer_terrain_beach_desert"),
  ("battle_mesopotamia_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002432008e300095a5900006d970000621600006a47 ",[], [], "outer_terrain_desert"),
  ("battle_mesopotamia_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024320056300095a590000384e00005d9500001ead ",[], [], "outer_terrain_desert"),
  ("battle_mesopotamia_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000056300095a59000075ba0000694f00001fc2 ",[], [], "outer_terrain_desert_b"),

  #done
  ("battle_syria", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245c00b0000092a4a0000707100004fa700002266 ",[], [], "outer_terrain_steppe_3"),
  ("battle_syria_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a000f810008fe4200004bc200006e8000000586 ",[], [], "outer_terrain_steppe_3"),
  ("battle_syria_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a000f810008fe42000027970000714600000586 ",[], [], "outer_terrain_steppe_3"),
  ("battle_syria_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000f810008fe420000724200006717000034ca ",[], [], "outer_terrain_steppe_3"),
  ("battle_syria_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000f810008fe4200002ae1000002cb00006f0c ",[], [], "outer_terrain_steppe_3"),
  #done
  ("battle_nile", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024000050000092a4a000073b600002e1d00006385 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005010009124400006d24000064da000056e5 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300009810009124400004c390000765d00007454 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002400005010009124400006d24000064da000056e5 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000240000501000912440000389c000069c200003811 ",[], [], "outer_terrain_beach_desert_flat"),
  #done
  ("battle_nile_delta", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024000050000092a4a00002048000027c400006e2f ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_delta_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002400005000009124400001d78000046ec00005b45 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_delta_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005000009124400001d78000046ec00005b45 ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_delta_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002300005000009124400005e5c0000147800000d0c ",[], [], "outer_terrain_beach_desert_flat"),
  ("battle_nile_delta_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023000050000091244000023850000152c00001670 ",[], [], "outer_terrain_beach_desert_flat"),

  #done
  ("battle_anatolia_coastal", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024a1909e30008aa2b00005ac600004cf300000143 ",[], [], "outer_terrain_beach_med"),
  ("battle_anatolia_coastal_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c4c01a800009a66a00006a2400000c8000007f4f ",[], [], "outer_terrain_beach_med"),
  ("battle_anatolia_coastal_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000024b000e000009e2780000253e000027db00007fd1 ",[], [], "outer_terrain_steppe_2"),
  ("battle_anatolia_coastal_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000244c014000009a66a0000690a0000787200005016 ",[], [], "outer_terrain_steppe_2"),
  ("battle_anatolia_coastal_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000244c014000009a66a00006aca00001f7b000016ee ",[], [], "outer_terrain_steppe_2"),

  ("battle_caucasian_mountains", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a520108000091e470000627b0000786a00007f58",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a788b20009364e00002ebf000067560000174d",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a789630009364e000060510000724400003221",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a789630009364e00000a5f0000475a00002ea3",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b3a789630009364e0000697200005efa00003e36",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000230000500000329e400005cce00003f9200002e90",[], [], "outer_terrain_mountain"),
  ("battle_caucasian_mountains_7", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002bc60138000089e2900003837000010160000044c",[], [], "outer_terrain_mountain_2"),
  ("battle_caucasian_mountains_8", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030000913400d2348000030c40000600500006b66",[], [], "outer_terrain_mountain_2"),
  ("battle_caucasian_mountains_9", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030000913400d2348000030c40000600500006b66",[], [], "outer_terrain_mountain_2"),
  ("battle_caucasian_mountains_10", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030000500000d2348000030c4000053ae00001d83",[], [], "outer_terrain_mountain_2"),

  ("battle_central_anatolia", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002206006e30008be27000060d50000026e000003de",[], [], "outer_terrain_steppe_3"),
  ("battle_central_anatolia_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000200012e30009725e000024bc000066590000127e",[], [], "outer_terrain_steppe_3"),
  ("battle_central_anatolia_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000200012e30009725e00007f1a0000629a00001b19",[], [], "outer_terrain_steppe_3"),
  ("battle_central_anatolia_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000020000ce30009725e00007f1a0000629a00004017",[], [], "outer_terrain_steppe_3"),
  ("battle_central_anatolia_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000020000ce30009725e000053370000024c00000ada",[], [], "outer_terrain_steppe_3"),

  ("battle_europe_mountains", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023c0151e30008160200005d1e0000559000000edb",[], [], "outer_terrain_mountain_2"),
  ("battle_europe_mountains_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002bc60158000087a1e00001d6d00003ee8000008cb",[], [], "outer_terrain_mountain_3"),
  ("battle_europe_mountains_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c005000009926300003fed0000064d00006e9d",[], [], "outer_terrain_mountain_2"),
  ("battle_europe_mountains_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c00500000992630000763b000033b800000501",[], [], "outer_terrain_mountain_3"),
  ("battle_europe_mountains_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000238c00500000992630000267800006700000071b3",[], [], "outer_terrain_mountain_2"),
  ("battle_europe_mountains_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000030000500000d2348000030c4000053ae00001d83",[], [], "outer_terrain_mountain_3"),
  ("battle_europe_mountains_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000030000500000d2348000030c4000053ae00001d83",[], [], "outer_terrain_mountain_2"),

  #maps from oliver
  ("custom_battle_forest_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000001bc61cee200093e53000056430000221c0000208f", [],[], "outer_terrain_mountain_3"), #hills 1 forest
  #needs fix
  ("custom_battle_forest_2",sf_generate,"none", "none", (0,0),(250,250),-0.5,"0x00000000300005800007c9f4000040a10000421300000192", [],[], "outer_terrain_mountain_2"), #flat forest
  ("custom_battle_forest_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005800007c9f4000040a10000421300000192", [],[], "outer_terrain_mountain_3"), #river - plains/forest
  #
  ("custom_battle_forest_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000002bc6088e28009be7900000a740000455f00003f08", [],[], "outer_terrain_mountain_3"), #river - forest

  ("battle_europe_mountains_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000030000913400d2348000030c40000600500006b66",[], [], "outer_terrain_mountain_3"),

  ("battle_persian_hills_green", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022000160000089e2b00006f7200002a3400003b51",[], [], "outer_terrain_steppe_3"),
  ("battle_persian_hills_green_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000009bd00002031000076c1",[], [], "outer_terrain_steppe_3"),
  ("battle_persian_hills_green_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a6400000175000056a60000146c",[], [], "outer_terrain_steppe_3"),
  ("battle_persian_hills_green_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000067d400001d0d000014bc",[], [], "outer_terrain_steppe_3"),
  ("battle_persian_hills_green_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012201907e300599a64000001eb000014bc0000411e",[], [], "outer_terrain_steppe_3"),

  ("battle_italian_greek", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000247c4caa3000982610000689f00000bda00002412 ",[], [], "outer_terrain_plain_2"),
  ("battle_italian_greek_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000124a1907e300599a6400001dc2000050d600002850 ",[], [], "outer_terrain_plain_2"),
  ("battle_italian_greek_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000124a1907e300599a6400002ee9000074da0000423d ",[], [], "outer_terrain_plain_2"),
  ("battle_italian_greek_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012401907e300599a64000061ae00006617000033aa ",[], [], "outer_terrain_plain_2"),
  ("battle_italian_greek_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000012400007e300599a6400007ec300000ad900006f54 ",[], [], "outer_terrain_plain_2"),

  #NORTH AFRICA
  ("river_battle_north_africa", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000248600500000b0ac6000016a200000dff00007268 ",[], [], "outer_terrain_steppe"),
  ("random_scene_north_africa_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000145800863000abaae0000274a00004eb700003ff9",[], [], "outer_terrain_steppe"), #hills/valley 1
  ("random_scene_north_africa_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000146e00563000d2348000073b90000447500000f05",[], [], "outer_terrain_steppe"), #flatlands 1
  ("random_scene_north_africa_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000014c601163000d234800007a2d00006ac200005744",[], [], "outer_terrain_steppe"), #hills/valley 2
  ("random_scene_north_africa_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000014c600d63000d23480000267d0000754c00006fca",[], [], "outer_terrain_steppe"), #hills 2


  ("random_scene_new_steppe_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf0000381400001e040000112d",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf00004d66000013330000593c",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf000074e00000524c00002aec",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220800500000afebf00001e120000059000005a37",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220400500000afebf00002440000051c60000229d",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf0000376a00002c26000018f6",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf000002bc000075c0000003db",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf00006bc9000047da000060aa",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf000058250000326800001a29",[], [], "outer_terrain_steppe"),
  ("random_scene_new_steppe_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220000500000afebf00005f9600004b2f000073b3",[], [], "outer_terrain_steppe"),

  #the old steppe scenes are now also used for plain
  ("random_scene_steppe_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a000a6300098a6300005a3f00003d51000066dd",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a000a6300098a6300000ec1000024f000005294",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a000a6300098a6300000e1c0000513d00006600",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00066300098a6300003f60000061d800005214",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00066300098a630000461400007f4c0000639f",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00066300098a630000629e00000e1500000049",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00066300098a630000514400002ba300000d02",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00096300098a63000011a80000265900003fa9",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00096300098a63000064d70000737b00000fd8",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00096300098a6300001259000037a800005987",[], [], "outer_terrain_steppe_2"),
  ("random_scene_steppe_custom_11", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000022a00096300098a630000478300004f3b0000796d",[], [], "outer_terrain_steppe_2"),

  ("random_scene_plain_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023a00096300098a63000005d6000038400000015e",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023240096300098a63000008610000085300002096",[], [], "outer_terrain_plain_2"),
  ("random_scene_plain_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a63000026700000795a000021ad",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a6300002742000011ff00007b9a",[], [], "outer_terrain_plain_2"),
  ("random_scene_plain_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002324007e300098a6300006db90000329e000074ed",[], [], "outer_terrain_plain_2"),
  ("random_scene_plain_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023280086300098a6300001e9000000b2000006c18",[], [], "outer_terrain_plain_1"),
  ("random_scene_plain_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a0086300098a63000025b70000051200007f9d",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000233a0056300098a6300002c0c00003cd00000025e",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235c008e300098a6300003d0900001f2600000f9c",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a6300005d7100001aac00005cb6",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_11", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a63000023c700000cd500007908",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_12", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002314008e300098a630000278100006dbb00004d39",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_13", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a63000014c000005c3f000011dc",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_14", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a6300002d1d0000753e0000502d",[], [], "outer_terrain_plain_2"),
  ("random_scene_plain_custom_15", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000232e00ae300098a630000218a0000064900001c8c",[], [], "outer_terrain_plain"),
  ("random_scene_plain_custom_16", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a6300004b690000757300007722",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_17", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a63000048b200000f2000003774",[], [], "outer_terrain_plain_2"),
  ("random_scene_plain_custom_18", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a630000177d00000e2d00002165",[], [], "outer_terrain_plain_3"),
  ("random_scene_plain_custom_19", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a630000647f0000005f00004d32",[], [], "outer_terrain_plain_2"),

  #maps from oliver
  ("custom_battle_plains_1",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300012e30007c5f1000036660000112a00006486", [],[], "outer_terrain_plain"), #valley 1 forest/plains
  #needs fix
  ("custom_battle_plains_3",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300007630007bdf1000020360000064a00007b83", [],[], "outer_terrain_plain"), #hills 1 forest/plains
  ("custom_battle_plains_4",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000130000d6300093e4f00006024000006620000100a", [],[], "outer_terrain_plain"), #hills 2 forest/plains
  ("custom_battle_plains_6",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x000000023c604780000b72df00000b7c00003503000067fc", [],[], "outer_terrain_plain"), #hills 3 forest/plains
  ("custom_battle_plains_7",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000231000580000c0b0500006b520000720600007ff0", [],[], "outer_terrain_plain"), #plains

  ("random_scene_plain_custom_20", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000231c0086300098a63000007fd0000723c000032c7",[], [], "outer_terrain_plain_3"),

  ("random_scene_desert_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a630000260a0000532f00003eb5",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a63000039ba000048ae00002407",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025559050000098a63000019d60000425e00002a7e",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9050000098a6300003dfc000009af00003990",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9050000098a630000436f000048c500000caf",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9068000098a63000027a4000032c000007042",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000251d9068000098a630000097a00001c900000259e",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a63000066fc0000756500004946",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a63000073c200002f6c000013be",[], [], "outer_terrain_desert_b"),
  ("random_scene_desert_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000025019058000098a630000730b0000759600006b12",[], [], "outer_terrain_desert_b"),

  ("random_scene_steppe_forest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a299050000098a63000059f400003fcf00005d07",[], [], "outer_terrain_forest_steppe"),
  ("random_scene_steppe_forest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a7f9050000098a6300007198000010fe000010a5",[], [], "outer_terrain_forest_steppe"),
  ("random_scene_steppe_forest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ac60056300098a6300006c9c000068c600006a56",[], [], "outer_terrain_forest_steppe"),
  ("random_scene_steppe_forest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a5e0056300098a63000056240000623100001b09",[], [], "outer_terrain_forest_steppe"),
  ("random_scene_steppe_forest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002a5e0056300098a63000064670000419400003ab1",[], [], "outer_terrain_forest_steppe"),

  ("random_scene_plain_forest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a63000064670000419400003ab1",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a630000635e0000473800004cd3",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b5e0056300098a630000517600007b16000039a4",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a6300007d63000067ce00004a61",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a6300005ef9000041f300002200",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b82006e300098a630000250600003c4c00004ac9",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a6300006d46000067fb00007796",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a630000104b00003e0f00002ef9",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a630000717a000052e200007d13",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b820086300098a63000009d60000490000005972",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_11", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b680086300098a630000243900001253000003d5",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_12", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b680086300098a630000243900001253000003d5",[], [], "outer_terrain_forest"),
  ("random_scene_plain_forest_custom_13", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002bc6007800007bdf90000536a000053ee000059ec",[], [], "outer_terrain_forest"),

  ("random_scene_plain_mountain_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0010e30009565200001cfd00000fd900001a25",[], [], "outer_terrain_mountain_2"),
  ("random_scene_plain_mountain_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0010e300095652000012b800003878000013a2",[], [], "outer_terrain_mountain_2"),
  ("random_scene_plain_mountain_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0010e30009565200007aa3000019880000734a",[], [], "outer_terrain_mountain_2"),
  ("random_scene_plain_mountain_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a1910800009565200007eb30000158a0000681e",[], [], "outer_terrain_mountain_2"),
  ("random_scene_plain_mountain_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a1910800009565200004ffb00002999000038aa",[], [], "outer_terrain_mountain_2"),
  ("random_scene_plain_mountain_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0014800009565200003b9000003cee000013b0",[], [], "outer_terrain_mountain"),
  ("random_scene_plain_mountain_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0014800009565200000ac7000063ae00005d48",[], [], "outer_terrain_mountain"),
  ("random_scene_plain_mountain_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a00148000095652000030220000276f00002ee0",[], [], "outer_terrain_mountain"),
  ("random_scene_plain_mountain_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033a0014800009565200004d720000557e0000375f",[], [], "outer_terrain_mountain"),
  ("random_scene_plain_mountain_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000033c601480000956520000433200003237000075eb",[], [], "outer_terrain_mountain"),

  ("random_scene_plain_river_custom_1", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235a005000008c6310000543c000056bf0000078e",[], [], "outer_terrain_river_1"),
  ("random_scene_plain_river_custom_2", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235a005000008c631000001eb000073c1000056ff",[], [], "outer_terrain_river_1"),
  ("random_scene_plain_river_custom_3", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235a005000008c63100003d1100007356000023cb",[], [], "outer_terrain_river_1"),
  ("random_scene_plain_river_custom_4", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235a005000008c631000007fa000049e900003f2c",[], [], "outer_terrain_river_1"),

  # map from oli with swamp land
  ("custom_battle_swamp_1",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07", [],[], "outer_terrain_plain"), #plains
  ("custom_battle_swamp_2",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007bdef0000750f000056d900005a07", [],[], "outer_terrain_forest"), #forest
  # map from oli with river
  ("custom_battle_plains_5",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x00000000300005000007b5ed0000750f000056d900005a07", [],[], "outer_terrain_plain"), #river 2 plains
  #needs fix
  ("custom_battle_plains_2",sf_generate,"none", "none", (0,0),(100,100),-0.5,"0x0000000030000763000785e300004b920000090a0000418d", [],[], "outer_terrain_plain"), #river 1 plains

  ("random_scene_plain_river_custom_5", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000235a005000008c63100003773000049e9000025a8",[], [], "outer_terrain_river_1"),

  ("random_scene_snow_river_custom_1", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245a005000008c6310000543c000056bf0000078e",[], [], "outer_terrain_river_2"),
  ("random_scene_snow_river_custom_2", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245a005000008c631000001eb000073c1000056ff",[], [], "outer_terrain_river_2"),
  ("random_scene_snow_river_custom_3", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245a005000008c63100003d1100007356000023cb",[], [], "outer_terrain_river_2"),
  ("random_scene_snow_river_custom_4", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245a005000008c631000007fa000049e900003f2c",[], [], "outer_terrain_river_2"),
  ("random_scene_snow_river_custom_5", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000245a005000008c63100003773000049e9000025a8",[], [], "outer_terrain_river_2"),

  ("random_scene_desert_forest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca720000504d000006e5000020d8",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca7200006f4b000068770000566d",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002da0005000009ca720000209a0000793200003452",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002dc6005000009ca720000345800000507000022b7",[], [], "outer_terrain_desert"),
  ("random_scene_desert_forest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002dc6005000009ca720000073180007cf700005e67",[], [], "outer_terrain_desert"),

  ##med battle maps
  # ("random_scene_plain_custom_1_new", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000034400925000d23480000659c00004d18000006c9",[], [], "outer_terrain_plain"),
  ("random_scene_snow_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002430005000009ca720000233d8000498000005178",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002494005000009ca7200001b46800064ca000068f2",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002494005000009ca72000078a580000c2e00004bb8",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002494005000009ca7200000c0180004f4c0000484a",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002436005000009ca7200001f6780006c6000005988",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002436005000009ca7200001a7080006c6000004259",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002436005000009ca7200001bdd80007cbd0000439f",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000243600a000009ca72000073d380007b9500007624",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000243600a000009ca7200003d4d8000306100002e10",[], [], "outer_terrain_steppe"),
  ("random_scene_snow_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000243600a000009ca720000366c800051f900002434",[], [], "outer_terrain_steppe"),

  ("random_scene_snowforest_custom_1", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c8400a000009ca720000366c800051f900002434",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_2", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c8400a000009ca72000036168000185c000066da",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_3", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c8400a000009ca720000645280001b3100004347",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_4", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c84006000009ca7200001b638000471a000039c7",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_5", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002c84006000009ca7200003817800030a20000413f",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_6", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca72000043b6800070850000229e",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_7", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca7200001554800071af00007437",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_8", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca7200004e9b800079a900006684",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_9", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca7200003cbf800023ad00003eaa",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_10", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca720000714d8000444700007ac7",[], [], "outer_terrain_steppe_2"),
  ("random_scene_snowforest_custom_end", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002ca2006000009ca7200003af08000444700001e7b",[], [], "outer_terrain_steppe_2"),

  #castlesscenes
  ("castle_500_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130025cb20006097f00005b1400000e2f00005fd9",[], [], "outer_terrain_plain"),
  ("castle_500_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_500_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ("castle_10_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000230000500000759d600000529000064e800003cb9",[], [], "outer_terrain_plain_1"),
  ("castle_10_interior", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_10_prison", sf_indoors, "interior_prison_l", "bo_interior_prison_l", (-100, -100), (100, 100), -100, "0",[], []),

  ("castle_11_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),
  ("castle_11_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_11_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_12_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),
  ("castle_12_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_12_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_32_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130025cb20006097f00005b1400000e2f00005fd9",[], [], "outer_terrain_plain"),
  ("castle_32_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_32_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_34_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007a3b20005795e0000706d0000381800000bbc",[], [], "outer_terrain_plain"),
  ("castle_34_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_34_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  # ("castle_36_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000130025cb20006097f00005b1400000e2f00005fd9",[], [], "outer_terrain_plain"),
  # ("castle_36_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  # ("castle_36_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ("roman_african_castle_ex",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500005000004fd3f0000315e0000201a0000697b",
    [],[],"outer_terrain_beach_desert"),
  ("roman_african_castle_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("salona_ex",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000004fd3f0000315e0000201a0000697b",
    [],[],"outer_terrain_beach"),
  ("salona_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("salona_in", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_caledonian_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000230029cb2000709c200003c9500004b9b00002f4d",[], [], "outer_terrain_plain"),
  ("castle_caledonian_in", sf_indoors, "none", "none", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_caledonian_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",[], []),

  ("commu_exterrior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002b00dd2908005795e0000706d8000044400004309",[], [], "outer_terrain_plain"),
  ("commu_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], ["castle_7_seneschal"]),
  ("commu_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),

  ("castle_47_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000254c2ec0000042509000016da0000017200000ed3",[], [], "outer_terrain_desert"),
  ("castellum", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013000000000083e1200009d1f00000fbb0000a6f0",[], [], "outer_terrain_plain_1"),
  # ("castle_21_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000020000500000721e6000011ab000063ff000007ad",[], [], "outer_terrain_desert"),
  # ("castle_20_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000020000500000721e6000011ab000063ff000007ad",[], [], "outer_terrain_desert"),

  ("londinium", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013000000000083e1200009d1f00000fbb0000a6f0",[], ["bonus_chest_6"], "outer_terrain_plain"),
  ("londinium_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("londinium_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("arbela_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002200005000006a5aa000046e400006d5d0000526a",[], [], "outer_terrain_steppe"),

  ("arbela_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("susa_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001a00005000005695c00001ebe0000028e00007e37",[], [], "outer_terrain_desert_b"),
  ("samosata_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001a00005000005695c00001ebe0000028e00007e37",[], [], "outer_terrain_desert_b"),
  ("samosata_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("samosata_prison", sf_indoors, "interior_prison_h", "bo_interior_prison_h", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("parthian_castle_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001a00005000005695c00001ebe0000028e00007e37",[], [], "outer_terrain_steppe"),
  ("parthian_castle_in", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("parthian_castle_pr", sf_indoors, "interior_prison_h", "bo_interior_prison_h", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("africa_roman_castle", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002500005000009d678000050790000525a00006c76",[], [], "outer_terrain_desert"),
  ("africa_in", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("africa_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("petra_ex", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002500005000009d678000050790000525a00006c76",[], [], "outer_terrain_desert"),
  ("petra_in", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("petra_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("germanic_castle_1_exterior", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000023007a3b20005795e0000706d0000381800000bbc",[], [], "outer_terrain_plain_1"),
  ("germanic_castle_1_prison", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("germanic_castle_1_interior", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ##twon scenes
  ("germanic_town_walls", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_plain_3"),
  ("germanic_town_center", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_plain"),
  ("germanic_town_arena", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030015f2b000350d4000011a4000017ee000054af",[], [], "outer_terrain_plain"),
  ("germanic_town_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("germanic_town_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("germanic_town_store", sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("germanic_town_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),


  ("town_7_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_beach_desert"),
  ("town_7_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], ["legatus_6"]),
  ("town_7_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_7_store", sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_7_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030015f2b000350d4000011a4000017ee000054af",[], [], "outer_terrain_beach_desert"),
  ("town_7_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_7_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_beach_desert"),
  ("town_13_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain_3"),
  ("town_13_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_13_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_13_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_13_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_13_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain_3"),
  ("town_9_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_beach"),
  ("town_9_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], ["legatus_8"]),
  ("town_9_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_9_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_9_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_9_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_beach"),
  ("town_41_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], ["orgie_fem2"], "outer_terrain_plain_3"),
  ("town_41_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",["exit"], ["senator_1"]),
  ("town_41_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_41_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_41_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_41_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain_3"),
  ("town_32_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain_1"),
  ("town_32_castle", sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100, -100), (100, 100), -100, "0",["exit"], ["statthalter_4"]),
  ("town_32_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_32_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_32_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_32_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain_1"),
  #nisbis
  ("town_48_center", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], [], "outer_terrain_desert"),
  ("town_48_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_48_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100, -100), (100, 100), -100, "0",[], []),
  ("town_48_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("town_48_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], [], "outer_terrain_desert"),
  ("town_48_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_48_walls", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], [], "outer_terrain_desert"),
  ##colchis
  ("colchis_center", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000083a0b000044da00005dc9000009eb",[], [], "outer_terrain_beach"),
  ("colchis_castle", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("colchis_tavern", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000083a0b000044da00005dc9000009eb",[], [], "outer_terrain_beach"),
  ("colchis_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("colchis_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("colchis_arena", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], [], "outer_terrain_plain"),
  ("colchis_walls", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x000000022000050000083a0b000044da00005dc9000009eb",[], [], "outer_terrain_beach"),

  ##athen
  ("athen_center", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x00000002300005000007c9f1000040f000005ae90000562f",[], [], "outer_terrain_beach_med"),
  ("athen_castle", sf_indoors, "parthenon_in", "bo_parthenon_in", (-100, -100), (100, 100), -100, "0",[], []),
  ("athen_tavern",  sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("athen_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("athen_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("athen_arena", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002300005000007c9f1000040f000005ae90000562f",[], [], "outer_terrain_beach_med"),
  ("athen_walls", sf_generate|sf_muddy_water, "none", "none", (0, 0), (100, 100), -100, "0x00000002300005000007c9f1000040f000005ae90000562f",[], [], "outer_terrain_beach_med"),

  ("dacian_capital_center", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain_2"),
  ("dacian_capital_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacian_capital_prison", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacian_capital_walls", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain_2"),
  ("dacian_capital_tavern", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacian_capital_store", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacian_capital_arena", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain_2"),

  ("town_bosporan_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",[],[],"outer_terrain_beach"),
  ("town_bosporan_tavern",sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",["exit"],[]),
  ("town_bosporan_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",["exit"],[]),
  ("town_bosporan_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",[],[],"outer_terrain_plain"),
  ("town_bosporan_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",["exit"],[]),
  ("town_bosporan_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000500000541500000755400006cf4000001ec",[],[],"outer_terrain_beach"),
  ("town_bosporan_castle", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("castle_bosporan_ex",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000a00005000005715c00000935000076e80000443a",[],[],"outer_terrain_beach"),
  ("castle_bosporan_in", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("castle_bosporan_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",["exit"],[]),

  ("castle_caucasus_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000007a2600c0000054150000075280000575900001853", #ujarma
    [],[],"outer_terrain_steppe"),
  ("castle_caucasus_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_63_seneschal"]),
  ("castle_caucasus_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("town_caucasus_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_steppe"),
  ("town_caucasus_castle",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_caucasus_tavern",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_caucasus_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_caucasus_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_steppe"),
  ("town_caucasus_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_caucasus_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000050000054150000045e10000331000005af7",
    [],[],"outer_terrain_steppe"),

  ("theben_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300005000005054100002d0b00003a0200002ca5",[], [], "outer_terrain_desert_b"),
  ("theben_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_desert_b"),
  ("theben_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("theben_tavern", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000200005000002c8ae00000114000078710000692c",["exit"], []),

  ("dacidava_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300005000005054100002d0b00003a0200002ca5",[], [], "outer_terrain_mountain"),
  ("dacidava_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000000300005000005054100002d0b00003a0200002ca5",[], [], "outer_terrain_mountain"),
  ("dacidava_castle", sf_indoors, "lofotrinterior", "bo_lofotrInteriorCollision", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("dacidava_tavern", sf_indoors, "lofotrinterior", "bo_lofotrInteriorCollision", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("carthago_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "sea_outer_terrain_2"),
  ("carthago_center", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], ["bonus_chest_9"], "sea_outer_terrain_2"),
  ("carthago_castle", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("antiochia", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "outer_terrain_beach_med"),
  ("antiochia_wall", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "outer_terrain_beach_med"),
  ("antiochia_tavern", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100, -100), (100, 100), -100, "0",[], []),
  ("antiochia_castle", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100, -100), (100, 100), -100, "0",[], []),
  ("antiochia_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ##palmyra scene
  ("palmyra_store", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("palmyra_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("palmyra", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ("palmyra_wall", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ("palmyra_tavern", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ("palmyra_castle", sf_indoors, "greek_castle1", "bo_greek_castle1", (-100, -100), (100, 100), -100, "0",[], []),
  ("palmyra_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ##ctesiphon scene
  ("town_19_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_19_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("ctesiphon", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000d2348000063f500001bbd00005d54",[], [], "outer_terrain_desert"),
  ("ctesiphon_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000220000500000d2348000063f500001bbd00005d54",[], [], "outer_terrain_desert"),
  ("town_19_tavern", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("town_19_castle", sf_indoors, "arabian_interior_keep_c", "bo_arabian_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], ["kingdom_17_lord"]),
  ("ctesiphon_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ##nisha
  ("nisha_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("nisha_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("nisha_tavern", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("nisha_castle", sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100, -100), (100, 100), -100, "0",["exit"], ["kingdom_17_lord"]),

  ("nisha", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ("nisha_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),
  ("nisha_arena", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002532005000009425300006a2500002b1200007456",[], [], "outer_terrain_desert"),

  ##Rome
  ("rome_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("rome_walls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013001c98d0005b56d000072a70000240a00001e09",[], [], "outer_terrain_plain"),
  ("roman_town_hall", sf_indoors, "none", "none", (-120, -120), (120, 120), -100, "0",["exit"], []),
  ("town_romewalls", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000013301c85000059224800072a70000240a00001e090",[], [], "outer_terrain_plain"),

  # if player builds special building
  ("colosseum", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030015f2b000350d4000011a4000017ee000054af",[], [], "outer_terrain_plain"),
  ("colosseum_2", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030015f2b000350d4000011a4000017ee000054af",[], [], "outer_terrain_plain"),

  ##special senes
  ("stonehenge", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030e009a7000d234800001f5800001f5300001b9f",[], [], "outer_terrain_plain"),
  ("stonehenge_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000004300005008005b57000004e31800017d80000754b",[], [], "outer_terrain_plain"),

  ("dacian_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000230000500000902480000548b00003e5c0000152e",[], [], "outer_terrain_plain_1"),
  ("dacian_holy_side_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002300005000009024800002f1d000055a100006eef",[], [], "outer_terrain_plain"),

  ("sarmatian_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000022000050000090248000071b6000055a100000ad2",[], [], "outer_terrain_steppe"),
  ("sarmatian_holy_side_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002200005000009024800004c78000055a100000ad2",[], [], "outer_terrain_steppe_2"),

  ("persian_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002200005000009024800001d5900001d8900007bd0",[], [], "outer_terrain_mountain"),
  ("persian_holy_side_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002200005000009024800002ced00001975000049f9",[], [], "outer_terrain_mountain_2"),

  ("caucasian_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000023000050000090248000027e200006aa600007f52",[], [], "outer_terrain_mountain"),
  ("caucasian_holy_side_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000002300005000009024800003296000053fc00007eb8",[], [], "outer_terrain_mountain_2"),

  ("african_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000022000050000090248000046e500000a880000272a",[], [], "outer_terrain_desert"),
  ("arabian_holy_side_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000240000500000902480000375e0000472f00007cb3",[], [], "outer_terrain_desert"),

  ("african_holy_side_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000022000050000090248000046e500000a880000272a",[], [], "outer_terrain_desert"),
  ("african_holy_side_3", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000022000050000090248000046e500000a880000272a",[], [], "outer_terrain_desert"),

  ("forest", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000001bc65d6ad8005e97600004fe5000072ea00007ce2",[], [], "outer_terrain_plain"),
  ("german_temple_1", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000000bc634eb20003d0f20000135000004cf100002af3",[], [], "outer_terrain_plain"),
  ("german_temple_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000001bc6170b68003d0f2000062e900007b2500006111",[], [], "outer_terrain_plain"),
  ("german_temple_3", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000033a0797428005614e000023608000708d00007a0d",[], [], "outer_terrain_plain"),
  ("pyramid", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x000000005a060700000d234800005ab500002c3c00005703",[], ["bonus_chest_1"], "outer_terrain_desert"),
  #special scenes
  ("mine_plain", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x000000013a00376300055154000019dc0000466900001afc",[], [], "outer_terrain_plain"),
  ("mine_desert", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000001da00376300055154000019dc0000466900001afc",[], [], "outer_terrain_desert"),
  ("olympia", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x0000000237823232800abaae000018320000544d000048a9",[], [], "outer_terrain_plain_1"),
  ("delphi", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x000000023441b344000abaae000069aa00001baa000057ae",[], [], "outer_terrain_mountain_2"),
  ("pythia", sf_indoors, "greek_castle1", "bo_greek_castle1", (-100, -100), (100, 100), -100, "0",[], []),
  ("olympia_in", sf_indoors, "parthenon_in", "bo_parthenon_in", (-100, -100), (100, 100), -100, "0",[], []),
  ##special scenes
  ("church", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("temple_jerusalem", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x00000001d24a96b0000751cf000041ef00005ae800003c55",[], [], "outer_terrain_desert"),

  ("villa_player", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x0000000240a3773b80062d8b000051df00003be000001e13",[], ["tutorial_chest_1"], "outer_terrain_beach"),
  ("hord", sf_generate|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000224400a0c00076ddd000079ef00005d26000057ea",[], [], "outer_terrain_steppe"),

  ##special scenes
  ("scriptorium", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("triumph_marsh", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("gaetulian_town_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002dc6005088007d5f70000759c00007438000002c6",[], [], "outer_terrain_desert"),
  ("garmantian_town_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002d32005088007d5f70000687180004e89000002c6",[], [], "outer_terrain_desert_b"),
  ("arabian_town_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002d32023e30007d5f700004d8400003ad2000049db",[], [], "outer_terrain_desert_b"),
  ("nubian_town_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000002d42005000007d1f70000194c00000c1f000067f5",[], [], "outer_terrain_desert_b"),
  ("irish_town_1", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x000000013005213200077dda0000733300002edf000052ba",[], [], "outer_terrain_plain_1 "),
  ("slavic_town_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",[],[],"outer_terrain_plain"),
  ("danish_town_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",[],[],"outer_terrain_plain"),
  ("georgian_town_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",[],[],"outer_terrain_mountain_2"),
  ("dahae_town_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220000500000811ff00007c1000000733000040f4",[],[],"outer_terrain_steppe_2"),

  ("slavemarket", sf_indoors, "oil_press_interior", "bo_oil_press_interior", (-100, -100), (100, 100), -100, "0",[], []),
  ##sea scenes
  ("sea_barbarian", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030000000c00d2348000000008000000000000000",[], [], "outer_terrain_beach"),
  ("sea_roman", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030000000c00d2348000000008000000000000000",[], [], "outer_terrain_beach"),
  ("meeting_scene_water", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030000000c00d2348000000008000000000000000",[], [], "sea_outer_terrain_2"),

  ("lugdunum_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275", [],[],"outer_terrain_plain"),
  ("lugdunum_castle",sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("lugdunum_tavern",sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100,-100),(100,100),-100,"0",["exit"],[]),
  ("lugdunum_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("lugdunum_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c", [],[],"outer_terrain_plain"),
  ("lugdunum_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",[],[]),
  ("lugdunum_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",[],[],"outer_terrain_plain"),

  ("town_10_center", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000200149b2000d2348000073b700002a2f00003f89",[], [], "outer_terrain_steppe"),
  ("town_10_castle", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000007300005000002308c00004a840000624700004fda",[], [], "outer_terrain_steppe"),
  ("town_10_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100, -100), (100, 100), -100, "0",[], []),
  ("town_10_walls", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000200149b2000d2348000073b700002a2f00003f89",[], [], "outer_terrain_steppe"),
  ("town_10_arena", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000200149b2000d2348000073b700002a2f00003f89",[], [], "outer_terrain_steppe"),

  ("castle_17_exterior", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000a000050000086a1a000077300000250a00005b03 ",[], [], "outer_terrain_steppe"),
  ("castle_17_interior", sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_17_prison", sf_indoors, "interior_prison_cell_a", "bo_interior_prison_cell_a", (-100, -100), (100, 100), -100, "0",[], []),

  ("castle_30_exterior", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x0000000220035e32000611840000147f00003dac00000660",[], [], "outer_terrain_plain"),
  ("castle_30_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_30_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ("castle_masada_ex", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000250000500000a268900000be200001df20000582b",[], [], "outer_terrain_desert"),
  ("castle_masada_in", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",[], []),
  ("castle_masada_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ("ceasarea_ex", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000250000500000a268900000be200001df20000582b",[], [], "outer_terrain_beach_desert"),
  ("ceasarea_in", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000250000500000a268900000be200001df20000582b",[], [], "outer_terrain_beach_desert"),
  ("ceasarea_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),
  ("jotopata_ex", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000240000500000721cc00006cc20000053f0000591f",[], [], "outer_terrain_mountain"),
  ("jotopata_in", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000240000500000721cc00006cc20000053f0000591f",[], [], "outer_terrain_mountain"),
  ("jotopata_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100, -100), (100, 100), -100, "0",[], []),

  ##scpecial scenes
  ("grove", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x00000000ba031de30008922700006a3000005c8c00003bfb",[], [], "outer_terrain_mountain"),
  ("vally_of_kings", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x0000000051ef626300095e54000024e1000072a800003ce2",[], ["bonus_chest_2"], "outer_terrain_desert"),
  ("barracks", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),
  ("barracks_eastern", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),
  ("barracks_barbarian", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),
  ("barracks_nomadic", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),

  ("roman_burns", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),

  ("lucias_villa", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], [], "outer_terrain_plain"),

  ("oubliette", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100, -100), (100, 100), -100, "0",[], []),
  ("house_1", sf_indoors, "winery_interior", "bo_winery_interior", (-100, -100), (100, 100), -100, "0",[], []),
  ("house_2", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x00000002300005000004e53a0000483e0000673c0000553f",[], ["bonus_chest_3"], "outer_terrain_plain"),
  ("duel_plain_forest", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000300005000005495000002ee4000032f600000753",[], [], "outer_terrain_plain"),
  ##small camp scenes
  ("camp_scene_snow_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000054327dcba0005194a00001b1d00005ae800004d63",[], [], "outer_terrain_plain_1"),
  ("camp_scene_steppe_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000012247dcba0005194a000041ef00005ae8000050af",[], [], "outer_terrain_steppe"),
  ("camp_scene_plain_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000001324a9cba0005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),
  ("camp_scene_desert_2", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x000000005007d4a10002589600001e2300004fae00006204",[], [], "outer_terrain_desert_b"),
  ##water visit your ships
  ("camp_water", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030000000c00d2348000000008000000000000000",[], [], "sea_outer_terrain_2"),
  ##special scenes
  ("grove_witch", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000bc6785328005455200001243800011c5000050f6",[], [], "outer_terrain_plain"),
  ("grove_witch_2", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x00000000bc6032000006bdaf000022ec00006b8a00006550",[], [], "outer_terrain_plain"),
  ("senate", sf_indoors, "none", "none", (0, 0), (240, 240), -100, "0",[], []),
  ("horse_race_arena", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], [], "outer_terrain_plain"),

  ("latifundium_desert", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000035000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_desert_b"),

  ("latifundium_plain", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_plain"),
  ("latifundium_plain_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_plain"),
  ("barbarian_estate", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_plain"),

  ("temple_your", sf_indoors, "greek_castle1", "bo_greek_castle1", (-100, -100), (100, 100), -100, "0",[], []),
  ("follower_camp", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),
  ("commander_camp", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),

  ("camp_scene_snow_rome", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000343c00b0200060d8400000762000030290000059f",[], [], "outer_terrain_plain_1"),
  ("camp_scene_steppe_rome", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000323c00b0200060d84000053fd00005ec6000071dd",[], [], "outer_terrain_steppe"),
  ("camp_scene_plain_rome", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_plain"),

  ("bandit_camp", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_plain"),
  ("small_forest", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003c601d000004c13600000c3200004cff000025ee",[], [], "outer_terrain_plain"),
  ("homestead_raid", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_plain"),
  ("marsh_with_the_legion", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_steppe"),
  ("town_riot_rome", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_steppe"),
  ("pandateria", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "sea_outer_terrain_2"),
  ("faustus_villa", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "outer_terrain_plain_1"),
  ("attack_thundergod", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000025a07a04e0004611a00002fd700002a400000748d",[], [], "outer_terrain_desert"),
  ("lair_jungle", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x0000000030000500000d2348000043230000429700002c21",[], [], "outer_terrain_plain"),
  ("nile_attack", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001500003e3000fffff0000074800005c49000021c5",[], [], "outer_terrain_desert"),
  ("slavic_holy_side", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain"),
  ("sartemis", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002564005630008f23b0000549f00004ba500006801",[], ["bonus_chest_18"], "outer_terrain_desert"),
  ("library", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "outer_terrain_plain_1"),
  ("cave", sf_indoors, "cave-p01", "bo_cave-p01", (-100, -100), (100, 100), -100, "0",[], ["bonus_chest_4"]),
  ("cave_outside", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "outer_terrain_plain_1"),
  ("sacred_grove", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], ["bonus_chest_5"], "outer_terrain_plain_1"),
  ("starting_villa", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000242c005000006c1b1000055bb00007699000051a2",[], [], "outer_terrain_plain"),
  ("akademia", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002300005000005755b000016cc00004d020000497c",[], [], "outer_terrain_plain_1"),
  ("mount_olymp", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033000050000084a1200006aaa000036e000000581",[], [], "outer_terrain_mountain_2"),

  ("domus_mare_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_8"]),
  ("domus_mare_interior_2", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_8"]),

  ("collusseum", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0xa0001d9300031ccb0000156f000048ba0000361c",[], [], "outer_terrain_plain"),
  ("labyrinth", sf_indoors, "cave-p01", "bo_cave-p01", (-100, -100), (100, 100), -100, "0",[], []),
  ("sagala",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000005695d00007fbc00005de100006275",[],[],"outer_terrain_plain"),
  ("jungle_camp",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300005000002589600005bbe000065a000001b43 ",[],[],"outer_terrain_plain"),
  ("follower_camp_desert", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_desert_b"),
  ("elysium", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000013a01c85000057ddf700072a70000240a00001e090",[], [], "sea_outer_terrain_2"),
  ("arminius_tomb", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000bc6789000009024400004abd0000424f000078dd",[], ["zendar_chest"], "outer_terrain_plain"),
  ("petrus_event",sf_generate,"none", "none", (0,0),(240,240),-100,"0x00000000300005000002acab0000094d0000144a00003cc5",[],[],"outer_terrain_plain"),
  ("cythnus",sf_generate,"none", "none", (0,0),(240,240),-100,"0x000000033a079f32000a4e93000012c200000b2c0000564a",[],[],"sea_outer_terrain_2"),
  ("greek_game", sf_indoors, "cave-p01", "bo_cave-p01", (-100, -100), (100, 100), -100, "0",[], []),
  ("horse_race_arena_olympia", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], [], "outer_terrain_plain"),

  ("manc_house", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),
  ("scene_camp_desert", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000005c600563000d2348000052d4000067d5000029c1",[], [], "outer_terrain_desert_b"),
  ("subsaharan_african_village", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000044e00d63800d234800000a290000355400005080",[], [], "outer_terrain_steppe"),
  ("cutscene_parthia", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000004c6020e3000baeed0000587d00002e3200000ceb",[], [], "outer_terrain_mountain"),
  ("langobard_landing", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002b6800b63800a2286000036ec00004264000028ae",[], [], "outer_terrain_forest"),
  ("langobard_village", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000023009629a0005615800005564000023590000579e ",[], [], "outer_terrain_beach"),
  ("village_garamantian", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000002562005000008da3800006e27000071660000587a ",[], [], "outer_terrain_desert"),

  ("lair_egypt_bandits", sf_generate, "none", "none", (0, 0), (240, 240), -20, "0x000000005a060700000d234800005ab500002c3c00005703",[], ["bonus_chest_1"], "outer_terrain_desert"),
  ("roman_intro_1", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], [], "outer_terrain_plain"),
  ("roman_intro_2", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000230000500000d2348000034fc00006520000020cb",[], [], "outer_terrain_beach"),
  ("antonias_house", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000230000500000d2348000034fc00006520000020cb",[], [], "outer_terrain_beach"),

  ("players_tent", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain"),
  ("tarquinii", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003640050000992e4e000002ed0000006900006953",[], [], "outer_terrain_plain"),
  ("tarquinii_tomb_1", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_16"]),

  ("pillars", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], ["bonus_chest_10"], "outer_terrain_beach_2"),
  ("grave_anatolia", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], ["bonus_chest_11"], "outer_terrain_beach"),

  ("parthian_palace_garden", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x000000003000050000046d1b0000189f00002a8380006d91",[], ["bonus_chest_17"], "outer_terrain_desert"),

  ("gardens_of_manacea", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000230000500000a9ea90000654a0000214300005720",[], [], "outer_terrain_plain"),

  ("camp_scene_snow_barbarian", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000343c00b0200060d8400000762000030290000059f",[], [], "outer_terrain_plain_1"),
  ("camp_scene_steppe_barbarian", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000323c00b0200060d84000053fd00005ec6000071dd",[], [], "outer_terrain_steppe"),
  ("camp_scene_plain_barbarian", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000333c00b0200060d84000054e1000036930000335b",[], [], "outer_terrain_plain"),
  ("camp_scene_desert_barbarian", sf_generate, "none", "none", (0, 0), (240, 240), -0.5, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_desert_b"),

  ("mount_golgotha", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x00000001300010c800054d5c00004af000005d3f00002ca0",[], [], "outer_terrain_desert"),

  ("royal_tombs", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000300005000007d9f90000724900003f8e00007b69",[], [], "outer_terrain_mountain_2"),
  ("old_mine", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000300005000007d9f9000038b600001e7d00006b54",[], ["bonus_chest_15"], "outer_terrain_mountain_2"),
  ("royal_tombs_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_14"]),

  ("sacred_forests_seraca", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000002bc60138000089e2900003837000010160000044c",[], [], "outer_terrain_mountain_2"),

  ("alexanders_tomb", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x00000000300005000007d9f90000724900003f8e00007b69",[], [], "outer_terrain_beach_desert"),
  ("cutscene_fleet", sf_generate, "none", "none", (0, 0), (200, 200), -0.5, "0x0000000330000500000d23480000766b00001c13000046e9",[],[], "sea_outer_terrain_2"),

  ("second_battle_of_bedriacum", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x000000033c60130000084e15000022e300004eff00000447",[], [], "outer_terrain_plain_2"),
  ("speech_second_battle_of_bedriacum", sf_generate, "none", "none", (0, 0), (120, 120), -100, "0x0000000030044e900003dd02000077b20000400100005697",[], [], "outer_terrain_plain_2"),

  ("cutscene_rome_victory", sf_generate, "none", "none", (0, 0), (100, 100), -200, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),

  ("cave_olympia", sf_indoors, "cave-p01", "bo_cave-p01", (-100, -100), (100, 100), -100, "0",[], ["bonus_chest_20"]),

  ("scene_camp_forest", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000003c600563000d2348000052d4000067d5000029c1",[], [], "outer_terrain_forest"),
  ("baltic_town", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000000300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_forest"),

  ("kurgan", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220600500000afebf000002bc000075c0000003db",[], [], "outer_terrain_steppe"),
  ("kurgan_enter", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_16"]),

  ("roman_latrina", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], ["bonus_chest_19"]),

  ("shitty_tavern", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100, -100), (100, 100), -100, "0",[], []),

  ("holy_lance_cave",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500007630005a56b00006e200000319300002f0b", [],[], "outer_terrain_desert_mountain"),

  ("werdheri_bandit_lair",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9", [],[], "outer_terrain_plain"),

  ("cutscene_rome_victory_2", sf_generate, "none", "none", (0, 0), (100, 100), -200, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain"),


  ("public_baths", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("villa_baths", sf_indoors, "roman_baths_3", "bo_baths", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("presentation_scene", sf_indoors, "ch_meet_plain_a", "bo_encounter_spot", (-100, -100), (100, 100), -100, "0",["exit"], []),


  ("walhalla_outdoor", sf_generate, "none", "none", (0, 0), (100, 100), -200, "0x00000003300000000005194a000041ef00005ae800003c55",[], [], "outer_terrain_plain_2"),
  ("walhalla_indoors", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100, -100), (100, 100), -100, "0",["exit"], []),

  ("lybian_villa", sf_generate, "none", "none", (0, 0), (100, 100), -200, "0x000000003000050000051142000015bc000023e200007a41",[], [], "outer_terrain_desert"),

  ("cutscene_steppe", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf0000381400001e040000112d",[], [], "outer_terrain_steppe"),
  ("xiongnu_camp", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000220200500000afebf0000381400001e040000112d",[], [], "outer_terrain_steppe_mountain"),

  ("sogdian_town", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x000000012002a0b20004992700006e54000007fe00001fd2",[], [], "outer_terrain_steppe_mountain"),

  ("jilu_fortress", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x0000000120000500000a0e87000000000000000000000000",[], [], "outer_terrain_steppe_mountain"),
  ("kashar", sf_generate, "none", "none", (0, 0), (100, 100), -0.5, "0x00000001200005000009023c00001ad500007e3f00001828",[], [], "outer_terrain_desert_mountain"),

  ("luparnium", sf_indoors, "lupanar", "bo_lupanar", (-100, -100), (100, 100), -100, "0",[], []),

  ("ruins_of_carthage", sf_generate, "none", "none", (-100, -100), (100, 100), -100, "0x0000000040000532000741d00000705300003aad00000ac4", [], ["bonus_chest_21"], "outer_terrain_beach_desert_flat"),
]#end of file
#