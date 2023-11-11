from header_skins import *
from IDs.ID_particle_systems import *

#from compiler import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(240,0,-0.4,0.3, "Chin Size"),
(230,0,-0.4,0.8, "Chin Shape"),
(250,0,-0.25,0.55, "Chin Forward"),
(130,0,-0.5,1.0, "Jaw Width"),
(120,0,-0.5,0.6, "Lower Lip"),
(110,0,-0.2,0.6, "Upper Lip"),
(100,0,0.2,-0.2, "Mouth-Nose Distance"),
(90,0,0.55,-0.55, "Mouth Width"),

(30,0,-0.3,0.3, "Nostril Size"),
(60,0,0.25,-0.25, "Nose Height"),
(40,0,-0.2,0.3, "Nose Width"),
(70,0,-0.3,0.4, "Nose Size"),
(50,0,0.2,-0.3, "Nose Shape"),
(80,0,-0.3,0.65, "Nose Bridge"),

(160,0,-0.2,0.25, "Eye Width"),
(190,0,-0.25,0.15, "Eye to Eye Dist"),
(170,0,-0.85,0.85, "Eye Shape"),
(200,0,-0.3,0.7, "Eye Depth"),
(180,0,-1.5,1.5, "Eyelids"),

(20,0,0.6,-0.25, "Cheeks"),
(260,0,-0.6,0.5, "Cheek Bones"),
(220,0,0.8,-0.8, "Eyebrow Height"),
(210,0,-0.75,0.75, "Eyebrow Shape"),
(10,0,-0.6,0.5, "Temple Width"),

(270,0,-0.3,1.0, "Face Depth"),
(150,0,-0.25,0.45, "Face Ratio"),
(140,0,-0.4,0.5, "Face Width"),

(280,0,1.0,1.0, "Post-Edit"),
]

woman_face_keys = [
(230,0,0.8,-1.0, "Chin Size"),
(220,0,-1.0,1.0, "Chin Shape"),
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"),
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.6,1.0, "Nose Width"),
(80,0,-1.5,0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.4,1.0, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
#old head
# Face width-Jaw width Temple width
# woman_face_keys = [
# (230,0,0.5,-0.8, "Chin Size"),
# (220,0,-0.7,0.5, "Chin Shape"),
# (10,0,-0.7,0.7, "Chin Forward"),
# (20,0,-0.7,0.7, "Jaw Width"),
# (40,0,-1.0,0.5, "Jaw Position"),
# (90,0,-0.7,0.7, "Jaw Neck"),
# (50,0,-0.7,0.7, "Cheeks"),
# (100,0,-0.7,0.7, "Cheek Bones"),
# (270,0,0.5,-0.3, "Mouth-Nose Distance"),
# (30,0,-0.7,0.5, "Mouth Width"),
# (160,0,0.7,-0.5, "Lips Position"),

# (60,0,0.5,-0.5, "Nose Height"),
# (70,0,-0.5,0.7, "Nose Width"),
# (80,0,1.0,-1.0, "Nose Size"),
# (240,0,0.4,-0.4, "Nose Shape"),

# (150,0,-0.5,0.5, "Eye Width"),
# (110,0,0.5,-0.5, "Eye to Eye Dist"),
# (120,0,0.9,-0.9, "Eye Shape"),
# (130,0,-0.7,0.7, "Eye Position"),
# (140,0,-1.0,1.5, "Eyelids"),

# (170,0,-0.9,0.7, "Eyebrow Height"),
# (180,0,-0.5,1.0, "Eyebrow Shape"),
# (260,0,0.5,-0.5, "Temple Width"),

# (200,0,0.7,-0.7, "Face tall-short"),
# (210,0,-0.7,0.7, "Face Depth"),
# (250,0,-0.4,0.4, "Face Ratio"),
# (190,0,-0.9,0.7, "Face Width"),

# (280,0,0.0,1.0, "Post-Edit"),]
#childs
boy_face_keys = [
(240,0,-0.4,0.3, "Chin Size"),
(230,0,-0.4,0.8, "Chin Shape"),
(250,0,-0.25,0.55, "Chin Forward"),
(130,0,-0.5,1.0, "Jaw Width"),
(120,0,-0.5,0.6, "Lower Lip"),
(110,0,-0.2,0.6, "Upper Lip"),
(100,0,0.2,-0.2, "Mouth-Nose Distance"),
(90,0,0.55,-0.55, "Mouth Width"),

(30,0,-0.3,0.3, "Nostril Size"),
(60,0,0.25,-0.25, "Nose Height"),
(40,0,-0.2,0.3, "Nose Width"),
(70,0,-0.3,0.4, "Nose Size"),
(50,0,0.2,-0.3, "Nose Shape"),
(80,0,-0.3,0.65, "Nose Bridge"),

(160,0,-0.2,0.25, "Eye Width"),
(190,0,-0.25,0.15, "Eye to Eye Dist"),
(170,0,-0.85,0.85, "Eye Shape"),
(200,0,-0.3,0.7, "Eye Depth"),
(180,0,-1.5,1.5, "Eyelids"),

(20,0,0.6,-0.25, "Cheeks"),
(260,0,-0.6,0.5, "Cheek Bones"),
(220,0,0.8,-0.8, "Eyebrow Height"),
(210,0,-0.75,0.75, "Eyebrow Shape"),
(10,0,-0.6,0.5, "Temple Width"),

(270,0,-0.3,1.0, "Face Depth"),
(150,0,-0.25,0.45, "Face Ratio"),
(140,0,-0.4,0.5, "Face Width"),

(280,0,1.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
girl_face_keys = [
(230,0,0.5,-0.8, "Chin Size"),
(220,0,-0.7,0.5, "Chin Shape"),
(10,0,-0.7,0.7, "Chin Forward"),
(20,0,-0.7,0.7, "Jaw Width"),
(40,0,-1.0,0.5, "Jaw Position"),
(90,0,-0.7,0.7, "Jaw Neck"),
(50,0,-0.7,0.7, "Cheeks"),
(100,0,-0.7,0.7, "Cheek Bones"),
(270,0,0.5,-0.3, "Mouth-Nose Distance"),
(30,0,-0.7,0.5, "Mouth Width"),
(160,0,0.7,-0.5, "Lips Position"),

(60,0,0.5,-0.5, "Nose Height"),
(70,0,-0.5,0.7, "Nose Width"),
(80,0,1.0,-1.0, "Nose Size"),
(240,0,0.4,-0.4, "Nose Shape"),

(150,0,-0.5,0.5, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,0.9,-0.9, "Eye Shape"),
(130,0,-0.7,0.7, "Eye Position"),
(140,0,-1.0,1.5, "Eyelids"),

(170,0,-0.9,0.7, "Eyebrow Height"),
(180,0,-0.5,1.0, "Eyebrow Shape"),
(260,0,0.5,-0.5, "Temple Width"),

(200,0,0.7,-0.7, "Face tall-short"),
(210,0,-0.7,0.7, "Face Depth"),
(250,0,-0.4,0.4, "Face Ratio"),
(190,0,-0.9,0.7, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
undead_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.5,-0.9, "Eye to Eye Dist"),
(120,0,1.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.3,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.1,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]

chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,
    "malebody_u", "malefoot_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o","man_hair_p","man_hair_r","man_hair_q","shortlayer","shoulderhair","hairmessy","slickedback","shortbob","straightshoulder", "longshoulder", "longstraight","ponytail","courthair","shortcut"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
    #the numbers here are hex colors with aplha values (last to values are for alpha, first 6 for rgb)
     ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),#0
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),#1
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),#2
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),#3
     ("manface_7",0xffdceded,["hair_blonde"],[0xff171313, 0xff007080c]),#4
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),#5
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),#6
     #0xFF22120C
     #0xEA1F100C
     #0xff807c8a
     #0xB9473837
     #0xFF442A30
     ("manface_african",0xFF362F30,["hair_blonde"],[0xff120808, 0xff007080c]),#7
     ("manface_asian1",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),#8
     ("manface_asian2",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),#9
     ("manface_asian3",0xffbbb6ae,["hair_blonde"],[0xff171313, 0xff007080c]),#10
     ("manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),#11
  	 ("manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),#12
     ("manface_mideast3",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),#13
     ("manface_black1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#14
	 ("manface_black2",0xff5a3d34,["hair_blonde"],[0xff171313, 0xff007080c]),#15
	 ("manface_black3",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),#16
	 ("manface_white1",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),#17
	 ("manface_white2",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),#18
	 ("manface_white3",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),#19

     ("manface_brown1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#20
     ("manface_brown2",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#21


     ("manface_young_4",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),#22
     ("manface_young_5",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),#23
     ("manface_young_6",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),#24
     ("manface_midage_3",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),#25

     ("manface_brown3",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#26
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),

  (
    "woman", skf_use_morph_key_10,
    "femalebody_u", "femalefoot_l", "f_handL",
    "female_head", woman_face_keys,
    ["woman_hair_01","woman_hair_02","woman_hair_03","woman_hair_04","woman_hair_05","woman_hair_06","woman_hair_07","woman_hair_08","woman_hair_09",
    "woman_hair_10","woman_hair_11","woman_hair_12","woman_hair_13","woman_hair_14","woman_hair_15","woman_hair_16","woman_hair_17","woman_hair_18",
    "woman_hair_19","woman_hair_20","woman_hair_21","woman_hair_22","woman_hair_23","woman_hair_24","woman_hair_25","woman_hair_26","woman_hair_27",
    "woman_hair_28","woman_hair_30",], #woman_hair_meshes
#    ["woman_hair_a","woman_hair_b","woman_hair_c","woman_hair_d","woman_hair_e","woman_hair_f","woman_hair_g"], #woman_hair_meshes
    ["rus_eyelashes","rus_mascara","acc4","acc5","acc6","acc7","acc8","acc9","acc10","acc11","acc12","byz_earring"], #jewellery,
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["lucheyelashes_blonde"],
    [
     ("womanface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #0
     ("womanface_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]), #1
     ("womanface_a",0xffe3e8ef,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]), #2
     ("womanface_white_1",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #3
     ("womanface_white_2",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #4
     ("womanface_white_3",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #5
     ("womanface_white_4",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #6
     ("womanface_white_5",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #7

     ("womanface_brown",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]), #8
     ("womanface_brown_1",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]), #9
     ("womanface_dark_1",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),#10
     ("womanface_dark_2",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),#11

     ("womanface_african",0xff797979,["hair_blonde"],[0xff120808, 0xff007080c]), #12
     ("womanface_african_1",0xff3E3E3E,["hair_blonde"],[0xff120808, 0xff007080c]),#13
     ("womanface_african_2",0xff3E3E3E,["hair_blonde"],[0xff120808, 0xff007080c]),#14

     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_grunt,"snd_woman_grunt"),(voice_grunt_long,"snd_woman_grunt_long"),(voice_yell,"snd_woman_yell"),(voice_stun,"snd_woman_stun"),(voice_victory,"snd_woman_victory")], #voice sounds
    "skel_human_female_old", 0.91,
    psys_game_blood,psys_game_blood_2,
  ),
  (
    "boy", 0,
    "malebody_u", "malefoot_l", "m_handL",
    "male_head", boy_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4",], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
   #  ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
   #  ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
    # ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
    # ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
    # ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
    # ("manface_asian1",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     #("manface_asian2",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_asian3",0xffbbb6ae,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_mideast3",0xffe0e8e8,["hair_blonde"],[0xff171313, 0xff007080c]),
   #  ("manface_black1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_black2",0xff5a342d,["hair_blonde"],[0xff171313, 0xff007080c]),
	# ("manface_black3",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_white1",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
	 ("manface_white2",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
	 ("manface_white3",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),

#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.78,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),

  (
    "girl", skf_use_morph_key_10,
    "femalebody_u",  "femalefoot_l", "f_handL",
    "female_head", girl_face_keys,
    ["woman_hair_01","woman_hair_02","woman_hair_03","woman_hair_04","woman_hair_05","woman_hair_06","woman_hair_07","woman_hair_08","woman_hair_09",
    "woman_hair_10","woman_hair_11","woman_hair_12","woman_hair_13","woman_hair_14","woman_hair_15","woman_hair_16","woman_hair_17","woman_hair_18",
    "woman_hair_19","woman_hair_20","woman_hair_21","woman_hair_22","woman_hair_23","woman_hair_24","woman_hair_25","woman_hair_26","woman_hair_27",
    "woman_hair_28","woman_hair_30",], #woman_hair_meshes
#    ["woman_hair_a","woman_hair_b","woman_hair_c","woman_hair_d","woman_hair_e","woman_hair_f","woman_hair_g"], #woman_hair_meshes
    [], #jewellery,
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [
    ("womanface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #0
    ("womanface_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]), #1
    ("womanface_a",0xffe3e8ef,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]), #2
    ("womanface_white_1",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #3
    ("womanface_white_2",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #4
    ("womanface_white_3",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]), #5
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_grunt,"snd_woman_grunt"),(voice_grunt_long,"snd_woman_grunt_long"),(voice_yell,"snd_woman_yell"),(voice_stun,"snd_woman_stun"),(voice_victory,"snd_woman_victory")], #voice sounds
    "skel_human_female_old", 0.73,
    psys_game_blood,psys_game_blood_2,
  ),
    (
    "elephant", 0,
    "empty", "empty", "empty",
    "empty", undead_face_keys,
    [],
    [],
    ["hair_blonde"], #hair textures
    [],
    [
     ("manface_african",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ],
    [(voice_die,"snd_elephant"),(voice_hit,"snd_elephant"),(voice_grunt,"snd_elephant"),(voice_grunt_long,"snd_elephant"),(voice_yell,"snd_elephant"),(voice_stun,"snd_elephant"),(voice_victory,"snd_elephant")], #voice sounds
    "skel_human", 0.5,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
    (
    "wild_cats", 0,
    "empty", "empty", "empty",
    "empty", undead_face_keys,
    [],
    [],
    ["hair_blonde"], #hair textures
    [],
    [
     ("manface_african",0xfff7ece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ],
    [(voice_die,"snd_wild_cat"),(voice_hit,"snd_wild_cat"),(voice_grunt,"snd_wild_cat"),(voice_grunt_long,"snd_wild_cat"),(voice_yell,"snd_wild_cat"),(voice_stun,"snd_wild_cat"),(voice_victory,"snd_wild_cat")], #voice sounds
    "skel_human", 0.5,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
  (
    "wolf", 0,
    "empty", "empty", "empty",
    "empty", undead_face_keys,
    [],
    [],
    ["hair_blonde"], #hair textures
    [],
    [
     ("manface_african",0xfff7ece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ],
    [(voice_die,"snd_wolf"),(voice_hit,"snd_wolf"),(voice_grunt,"snd_wolf"),(voice_grunt_long,"snd_wolf"),(voice_yell,"snd_wolf"),(voice_stun,"snd_wolf"),(voice_victory,"snd_wolf")], #voice sounds
    "skel_human", 0.5,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),


  (
    "man_barbarian", 0,
    "malebody_u", "malefoot_l", "m_handL",
    "male_head", man_face_keys,
    ["hairmessy","longshoulder","longstraight","man_hair_p","man_hair_q","shortcut","slickedback","straightshoulder"],
    ["beard_b","beard_c","beard_e","beard_h","beard_j","beard_m","beard_n","beard_o","beard_p","beard_q","beard_r","beard_v","beard_y","beard_z"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
    #the numbers here are hex colors with aplha values (last to values are for alpha, first 6 for rgb)
    ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),#0
    ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),#1
    ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),#2
    ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),#3
    ("manface_7",0xffdceded,["hair_blonde"],[0xff171313, 0xff007080c]),#4
    ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),#5

    ("manface_white1",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),#17
    ("manface_white2",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),#18
    ("manface_white3",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),#19

    ("manface_young_4",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_young_5",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_young_6",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_midage_3",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),

     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),
  (
    "man_black", 0,
    "malebody_u", "malefoot_l", "m_handL",
    "male_head", man_face_keys,
    ["hairmessy","man_hair_m","man_hair_s","shoulderhair","slickedback","man_hair_u","man_hair_y12","man_hair_y4","man_hair_y8"],
    ["beard_h","beard_i","beard_j","beard_g"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
    ("manface_african",0xFF362F30,["hair_blonde"],[0xff120808, 0xff007080c]),#7
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),
  (
    "man_eastern", 0,
    "malebody_u", "malefoot_l", "m_handL",
    "male_head", man_face_keys,
    ["courthair","longshoulder","longstraight","man_hair_n","man_hair_s","shoulderhair","man_hair_u","man_hair_y10","man_hair_y9"],
    ["beard_y","beard_n","beard_j","beard_i","beard_h","beard_v",],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),#6
     ("manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),#11
  	 ("manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),#12
     ("manface_mideast3",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),#13

     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),

("man_north_african", 0,
  "malebody_u", "malefoot_l", "m_handL",
  "male_head", man_face_keys,
    ["hairmessy","man_hair_m","man_hair_s","shoulderhair","slickedback","man_hair_u","man_hair_y12","man_hair_y4","man_hair_y8"],
    ["beard_h","beard_i","beard_j","beard_g"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
      ("manface_brown1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#0
      ("manface_brown2",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#1
      ("manface_brown3",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#2
      ("manface_black1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),#3
      ("manface_black2",0xff5a3d34,["hair_blonde"],[0xff171313, 0xff007080c]),#4
      ("manface_black3",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),#5
    ],[
      (voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")
    ],
      "skel_human", 0.95,
      psys_game_blood,psys_game_blood_2,
	[
    [1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
    [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
    [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
    [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
    [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
]),

]