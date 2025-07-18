from header_common import *
from IDs.ID_animations import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *
from IDs.ID_info_pages import *

#from compiler import *
####################################################################################################################
#  Each tableau material contains the following fields:
#  1) Tableau id (string): used for referencing tableaux in other files. The prefix tab_ is automatically added before each tableau-id.
#  2) Tableau flags (int). See header_tableau_materials.py for a list of available flags
#  3) Tableau sample material name (string).
#  4) Tableau width (int).
#  5) Tableau height (int).
#  6) Tableau mesh min x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  7) Tableau mesh min y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  8) Tableau mesh max x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  9) Tableau mesh max y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  10) Operations block (list): A list of operations. See header_operations.py for reference.
#     The operations block is executed when the tableau is activated.
#
####################################################################################################################

#banner height = 200, width = 85 with wood, 75 without wood

tableaus = [

   ##character displayed on the screen for selecting the skills and attributes
  ("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532,
   [

    (assign, "$tableau_active", 2),
    (assign, "$character_sheet_is_active", 1),

    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_character_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_character_alpha_mask", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 300),


       ]),

  ("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270,
   [(assign, "$tableau_active", 1),
    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_inventory_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_inventory_alpha_mask", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 300),


       ]),

  ("game_profile_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480, [

    (assign, "$tableau_active", 1),

    (store_script_param, ":profile_no", 1),
    (assign, ":gender", ":profile_no"),
    (val_mod, ":gender", 2),
    (try_begin),
      (eq, ":gender", 0),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_male"),
    (else_try),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_female"),
    (try_end),
    (troop_set_face_key_from_current_profile, ":troop_no"),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_alpha_mask", ":troop_no", pos1, 0, 0),


    ]),

  ("game_party_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300,
   [
    (assign, "$tableau_active", 1),
    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_party_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_party_alpha_mask", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 300),


       ]),

  ("game_troop_label_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256,[
    (assign, "$tableau_active", 1),
    #(store_script_param, ":banner_mesh", 1),
    (store_script_param, ":banner_troop", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
    (try_begin),
        (ge, ":banner_troop", 0),
        (troop_slot_eq, ":banner_troop", slot_troop_banner_scene_prop, -1),
        (call_script, "script_draw_banner_to_region", ":banner_troop", 0, 0, 5120, 5120, 10000, 10000, 10000, 10000, 0),
    (else_try),
        (call_script, "script_agent_troop_get_banner_mesh", ":banner_troop"),
        (assign, ":banner_mesh", reg0),
        (init_position, pos1),
        (position_set_y, pos1, 120),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 120, 0),
    (try_end),
  ]),

  ("troop_tree_pic", 0, "tableau_with_transparency", 1024, 1024, 0, 0, Troop_Tree_Tableau_Width, Troop_Tree_Tableau_Height, [
   (assign, "$tableau_active", 1),
    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0x00888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (call_script, "script_add_troop_to_cur_tableau_for_party", ":troop_no"),


  ]),
  ("troop_detail_dummy_pic", 0, "tableau_with_transparency", 1024, 1024, 0, 0, Troop_Tree_Tableau_Width, Troop_Tree_Tableau_Height, [

   (assign, "$tableau_active", 1),
    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0x00888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (call_script, "script_add_troop_to_cur_tableau_for_troop_detail_dummy", ":troop_no"),


  ]),

  ("troop_note_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFC6BB94),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no", 0),
       ]),

  ("troop_note_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no", 0),
       ]),

  ("troop_kingdom_selection_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFC6BB94),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no", 1),
       ]),

  ("troop_kingdom_selection_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no", 1),
       ]),

  ("troop_character_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
       ]),

  ("troop_character_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [(assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFE0CFB1),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
       ]),

  ("troop_inventory_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_inventory", ":troop_no"),
       ]),

  ("troop_inventory_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [  (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF6A583A),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_inventory", ":troop_no"),


       ]),

  ("troop_profile_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
    [(assign, "$tableau_active", 1),
        (store_script_param, ":troop_no", 1),
        (cur_tableau_set_background_color, 0x00888888),
        (cur_tableau_set_ambient_light, 10,11,15),
        (cur_tableau_render_as_alpha_mask),
        #SB : redirect script call
        (try_begin),
            (this_or_next|eq, ":troop_no", "trp_multiplayer_profile_troop_male"),
            (eq, ":troop_no", "trp_multiplayer_profile_troop_female"),
            (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
        (else_try),
            (call_script, "script_add_troop_to_cur_tableau_for_presentation", ":troop_no"),
        (try_end),


    ]),

  ("troop_profile_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
    [ (assign, "$tableau_active", 1),
        (store_script_param, ":troop_no", 1),
        (cur_tableau_set_background_color, 0xFFF9E7A8),
        (cur_tableau_set_ambient_light, 10,11,15),
        #SB : redirect script call
        (try_begin),
            (this_or_next|eq, ":troop_no", "trp_multiplayer_profile_troop_male"),
            (eq, ":troop_no", "trp_multiplayer_profile_troop_female"),
            (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
        (else_try),
            (call_script, "script_add_troop_to_cur_tableau_for_presentation", ":troop_no"),
        (try_end),

    ]),


  ("troop_party_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_party", ":troop_no"),

       ]),

  ("troop_party_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [ (assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFBE9C72),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_party", ":troop_no"),

       ]),

  ("troop_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350,
   [(assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_note_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_note_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       (cur_tableau_add_mesh, "mesh_portrait_blend_out", pos1, 0, 0),

       ]),

  ("kingdom_selection_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350,
   [(assign, "$tableau_active", 1),
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_kingdom_selection_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_kingdom_selection_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       (cur_tableau_add_mesh, "mesh_portrait_blend_out", pos1, 0, 0),

       ]),

  ("center_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
    (assign, "$tableau_active", 1),
        (store_script_param, ":center_no", 1),
        (set_fixed_point_multiplier, 100),
        (cur_tableau_set_background_color, 0x00888888),
        (cur_tableau_set_ambient_light, 10,11,15),

        (init_position, pos8),
        (position_set_x, pos8, -210),
        (position_set_y, pos8, 200),
        (position_set_z, pos8, 300),
        (cur_tableau_add_point_light, pos8, 550,500,450),


##       (party_get_slot, ":troop_no", ":center_no", slot_town_lord),
##       (try_begin),
##         (ge, ":troop_no", 0),
##         (troop_get_slot, ":banner_spr", ":troop_no", slot_troop_banner_scene_prop),
##         (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
##         (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
##         (val_sub, ":banner_spr", banner_scene_props_begin),
##         (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
##       (try_end),
##
##       (init_position, pos1),
##       (position_set_x, pos1, -60),
##       (position_set_y, pos1, -100),
##       (position_set_z, pos1, 230),
##       (position_rotate_x, pos1, 90),
##       (assign, ":banner_scale", 105),

       (cur_tableau_set_camera_parameters, 1, 10, 10, 10, 10000),

##       (position_set_x, pos1, -100),
       (init_position, pos1),
       (position_set_z, pos1, 0),
       (position_set_z, pos1, -500),


       (init_position, pos1),
       (position_set_y, pos1, -100),
       (position_set_x, pos1, -100),
       (position_set_z, pos1, 100),
       (position_rotate_z, pos1, 200),

##       (cur_tableau_add_mesh, ":banner_mesh", pos1, ":banner_scale", 0),
       (party_get_icon, ":map_icon", ":center_no"),
       (try_begin),
         (ge, ":map_icon", 0),
         (cur_tableau_add_map_icon, ":map_icon", pos1, 0),
       (try_end),

       (init_position, pos5),
       (position_set_x, pos5, -90),
       (position_set_z, pos5, 500),
       (position_set_y, pos5, 480),
       (position_rotate_x, pos5, -90),
       (position_rotate_z, pos5, 180),
       (position_rotate_x, pos5, -35),
       (cur_tableau_set_camera_position, pos5),
       ]),

("faction_note_mesh_for_menu", 0, "pic_arms_rom", 1024, 512, 0, 0, 450, 225,[
    (assign, "$tableau_active", 1),
    (store_script_param, ":faction_no", 1),
    (cur_tableau_set_background_color, 0xFFFFFFFF),
    (set_fixed_point_multiplier, 100),
    (try_begin),
        (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (faction_get_slot, ":banner_mesh", ":faction_no", slot_faction_icon),
        (init_position, pos1),
        (position_set_y, pos1, -5),
        (position_set_x, pos1, -45),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
        (cur_tableau_set_camera_parameters, 0, 160, 80, 0, 100000),
    (try_end),
]),


("faction_note_mesh", 0, "pic_arms_garamantes", 1024, 512, 0, 0, 500, 250,[
    (assign, "$tableau_active", 1),
    (store_script_param, ":faction_no", 1),
    (cur_tableau_set_background_color, 0xFFFFFFFF),
    (set_fixed_point_multiplier, 100),
    (try_begin),
        (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (faction_get_slot, ":banner_mesh", ":faction_no", slot_faction_icon),
        (init_position, pos1),
        (position_set_y, pos1, -5),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
        (cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
    (try_end),
]),

  ("minor_faction_note_mesh", 0, "pic_arms_nabataea", 1024, 512, 0, 0, 500, 250,
   [(assign, "$tableau_active", 1),
     (store_script_param, ":faction_no", 1),
     (cur_tableau_set_background_color, 0xFFFFFFFF),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (is_between, ":faction_no", minor_kingdoms_begin, minor_kingdoms_end), #Excluding player kingdom
       (store_add, ":banner_mesh", "mesh_pic_arms_gaetuli", ":faction_no"),
       (val_sub, ":banner_mesh", minor_kingdoms_begin),
       (init_position, pos1),
       (position_set_y, pos1, -5),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
	   # (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
     (try_end),


     ]),

  ("faction_note_mesh_banner", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":faction_no", 1),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
     (try_end),


     ]),

  ("2_factions_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":faction_no", 1),
     (store_mod, ":faction_no_2", ":faction_no", 128),
     (val_div, ":faction_no", 128),
     (val_add, ":faction_no", kingdoms_begin),
     (val_add, ":faction_no_2", kingdoms_begin),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
     (try_end),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no_2", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_x, pos1, 50),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
     (try_end),
     (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
     ]),

("civil_war_factions", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300,[
    (assign, "$tableau_active", 1),
    (set_fixed_point_multiplier, 100),
    (try_begin),
        (faction_get_slot, ":leader_troop", "fac_kingdom_24", slot_faction_leader),
        (ge, ":leader_troop", 0),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
        (init_position, pos1),
        (position_set_x, pos1, -30),
        (position_set_y, pos1, 100),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 50, 0),
    (try_end),
    (try_begin),
        (faction_get_slot, ":leader_troop", "fac_kingdom_25", slot_faction_leader),
        (ge, ":leader_troop", 0),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
        (init_position, pos1),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, 100),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 50, 0),
    (try_end),
    (try_begin),
        (faction_get_slot, ":leader_troop", "fac_kingdom_26", slot_faction_leader),
        (ge, ":leader_troop", 0),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
        (init_position, pos1),
        (position_set_x, pos1, -30),
        (position_set_y, pos1, 0),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 50, 0),
    (try_end),
    (try_begin),
        (faction_get_slot, ":leader_troop", "fac_kingdom_27", slot_faction_leader),
        (ge, ":leader_troop", 0),
        (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
        (init_position, pos1),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, 0),
        (cur_tableau_add_mesh, ":banner_mesh", pos1, 50, 0),
    (try_end),
    (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
]),

  ("color_picker", 0, "objects", 32, 32, 0, 0, 0, 0,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":color", 1),
     (set_fixed_point_multiplier, 100),
     (init_position, pos1),
     (cur_tableau_add_mesh, "mesh_color_picker", pos1, 0, 0),
     (position_move_z, pos1, 1),
     (position_move_x, pos1, -2),
     (position_move_y, pos1, -2),
     (cur_tableau_add_mesh_with_vertex_color, "mesh_white_plane", pos1, 200, 0, ":color"),
     (cur_tableau_set_camera_parameters, 0, 20, 20, 0, 100000),
     ]),

  ("custom_banner_square_no_mesh", 0, "objects", 512, 512, 0, 0, 300, 300,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":troop_no", 1),
     #(val_max, ":troop_no", 0),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", ":troop_no", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
     ]),

  ("custom_banner_default", 0, "objects", 512, 256, 0, 0, 0, 0,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":troop_no", 1),
     #(val_max, ":troop_no", 0),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", ":troop_no", -9, -2, 7450, 19400, 7200, 18000, 9000, 10000, 0),
     (init_position, pos1),
     (position_set_z, pos1, 10),
     (cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner", pos1, 0, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
     ]),

  ("custom_banner_tall", 0, "objects", 512, 256, 0, 0, 0, 0,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":troop_no", 1),
     #(val_max, ":troop_no", 0),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", ":troop_no", -9, 12, 8250, 18000, 8000, 21000, 10000, 10000, 0),
     (init_position, pos1),
     (position_set_z, pos1, 10),
     (cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner", pos1, 0, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
     ]),

  ("custom_banner_square", 0, "objects", 256, 256, 0, 0, 0, 0,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":troop_no", 1),
     #(val_max, ":troop_no", 0),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", ":troop_no", -11, 10, 7700, 7700, 7500, 7500, 8300, 10000, 0),
     (init_position, pos1),
     (position_set_z, pos1, 10),
     (cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner_square", pos1, 0, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
     ]),

  ("custom_banner_short", 0, "objects", 256, 512, 0, 0, 0, 0,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":troop_no", 1),
     #(val_max, ":troop_no", 0),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", ":troop_no", -10, 0, 8050, 5000, 4200, 4800, 6600, 10000, 0),
     (init_position, pos1),
     (position_set_z, pos1, 10),
     (cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner_short", pos1, 0, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
     ]),

  ("background_selection", 0, "objects", 512, 512, 0, 0, 100, 100,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":banner_bg", 1),
     (troop_get_slot, ":old_bg", "trp_player", slot_troop_custom_banner_bg_type),
     (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_type, ":banner_bg"),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", "trp_player", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
     (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_type, ":old_bg"),
     ]),

  ("positioning_selection", 0, "objects", 512, 512, 0, 0, 100, 100,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":positioning", 1),
     (troop_get_slot, ":old_positioning", "trp_player", slot_troop_custom_banner_positioning),
     (troop_set_slot, "trp_player", slot_troop_custom_banner_positioning, ":positioning"),
     (set_fixed_point_multiplier, 100),
     (call_script, "script_draw_banner_to_region", "trp_player", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
     (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
     (troop_set_slot, "trp_player", slot_troop_custom_banner_positioning, ":old_positioning"),
     ]),

  ("retired_troop_alpha_mask", 0, "mat_troop_portrait_mask", 2048, 2048, 0, 0, 600, 600,
   [
    (assign, "$tableau_active", 1),
       (store_script_param, ":type", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_retirement", ":type"),
       ]),

  ("retired_troop_color", 0, "mat_troop_portrait_color", 2048, 2048, 0, 0, 600, 600,
   [
    (assign, "$tableau_active", 1),
       (store_script_param, ":type", 1),
       (cur_tableau_set_background_color, 0xFFe7d399),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_retirement", ":type"),
       ]),

  ("retirement_troop", 0, "tableau_with_transparency", 2048, 2048, 0, 0, 600, 600,
   [
    (assign, "$tableau_active", 1),
     (store_script_param, ":type", 1),
     (cur_tableau_set_background_color, 0xFF888888),
     (cur_tableau_set_ambient_light, 10,11,15),
     (set_fixed_point_multiplier, 100),
     (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

     (init_position, pos1),
     (position_set_z, pos1, 100),
     (position_set_x, pos1, -20),
     (position_set_y, pos1, -20),
     (cur_tableau_add_tableau_mesh, "tableau_retired_troop_color", ":type", pos1, 0, 0),
     (position_set_z, pos1, 200),
     (cur_tableau_add_tableau_mesh, "tableau_retired_troop_alpha_mask", ":type", pos1, 0, 0),
     ]),

  ("dplmc_lord_profile", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480, [

    (assign, "$tableau_active", 1),

    (store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_alpha_mask", ":troop_no", pos1, 0, 0),
    ]),

  ("flag_pole_new", 0, "sample_roman_spears_banner", 1024, 1024, 0, 0, 0, 0,
   [
       (store_script_param, ":troop_no", 1),
       (call_script, "script_agent_troop_get_banner_mesh", ":troop_no"),
       (assign, ":banner_mesh", reg0),
       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_rotate_x, pos1, 180),
       (position_set_x, pos1, -6.1),
       (position_set_y, pos1, -41), #135

       (position_set_x, pos2, 62),
       (position_set_y, pos2, 70),

      #  (cur_tableau_add_mesh_with_scale_and_vertex_color, ":banner_mesh", pos1, pos2, 0, 0), # 62
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 62, 0), # 62
       (init_position, pos1),
       (position_set_z, pos1, 10),

       (cur_tableau_add_mesh, "mesh_tableau_mesh_roman_spear_banner", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
      ]),

  ("draw_info_page_legion_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256,[
    (assign, "$tableau_active", 1),
    (store_script_param, ":page_number", 1),
    (store_sub, ":legion", ":page_number", ip_legio_1 - 1),
    (call_script, "script_get_legion_banner", ":legion"),
    (assign, ":banner_mesh", reg0),


    (cur_tableau_set_background_color, 0x00FFFFFF),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),

    (val_sub, ":banner_mesh", banner_scene_props_begin),
    (val_add, ":banner_mesh", arms_meshes_begin),
    (init_position, pos1),
    (position_set_y, pos1, 45),
    (position_set_x, pos1, 0),
    (cur_tableau_add_mesh, ":banner_mesh", pos1, 85, 0),
  ]),
]
