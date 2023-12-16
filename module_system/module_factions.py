from header_factions import *

#from compiler import *
####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.3,[("commoners",-0.6),("player_faction",-0.15),("deserters",-0.6),("forest_bandits",-0.02),("mountain_bandits",-0.02)], [], 0x888888),

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),
  ("dark_knights","Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], [], 0x383838),

  ("culture_1",  "Dacian", 0, 0.9, [], []),
  ("culture_2",  "Britonic", 0, 0.9, [], []),
  ("culture_2_1","Caledonian", 0, 0.9, [], []),
  ("culture_3",  "Sarmatian", 0, 0.9, [], []),
  ("culture_4",  "Germanic", 0, 0.9, [], []),
  ("culture_5",  "Caucasian", 0, 0.9, [], []),
  ("culture_6",  "Parthian", 0, 0.9, [], []),
  ("culture_7",  "Roman", 0, 0.9, [], []),
  ("culture_8",  "Judean", 0, 0.9, [], []),
  ("culture_9",  "Bosporan", 0, 0.9, [], []),
  ("culture_10",  "Arabian", 0, 0.9, [], []),
  ("culture_11",  "Berber", 0, 0.9, [], []),
  ("culture_12",  "Garamantian", 0, 0.9, [], []),
  ("culture_13",  "Nubian", 0, 0.9, [], []),
  ("culture_14",  "Saka", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], [], 0xED1C24),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("black_khergits",-0.9),("picton",-0.05),("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xED1C24), #changed name so that can tell difference if shows up on map

  ("kingdom_1",  "Getai", 0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xCE9246),
  ("kingdom_2",  "Kaledonoi",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",0.5),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x6AB2FF),
  ("kingdom_3",  "Basileion tou Bosporou", 0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x4462A2),
  ("kingdom_4",  "Fris",    0, 0.9, [("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xB82949),
  ("kingdom_5",  "Hayastan",  0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x01796F),
  ("kingdom_6",  "Basileia ton Parthaion",  0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xFE28A2),
  ("kingdom_7",  "Imperium Romanum",  0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("black_khergits",-0.9),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xED1C24),
  ("kingdom_8",  "Dumnones",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xFFEEB6),
  ("kingdom_9",  "Corieltauvi",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xC8B875),
  ("kingdom_10",  "Brigantes",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x365AFF),
  ("kingdom_11",  "Sauromatae", 0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xD6E386),
  ("kingdom_12",  "Sirakoi", 0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x38FF95),
  ("kingdom_13",  "Leugoz",    0, 0.9, [("furor_teutonicus",0.2),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x6B4963),
  ("kingdom_14",  "Markommanoz",    0, 0.9, [("furor_teutonicus",0.2),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x350012),
  ("kingdom_15",  "Rygir",    0, 0.9, [("furor_teutonicus",0.2),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xFF5C00),
  ("kingdom_16",  "Coadui",    0, 0.9, [("furor_teutonicus",0.2),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x249301),
  ("kingdom_17",  "Yehuda",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x19DA60),
  ("kingdom_18",  "Iazyges",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.75),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x988F84),
  ("kingdom_19",  "Batava",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0xA1D193),
  ("kingdom_20",  "Kartli",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x9C695A),
  ("kingdom_21",  "Aghwank",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x3c7549),
  ("kingdom_22",  "Kolcha",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x9C96A5),
  ("kingdom_23",  "Osrhoene",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x845D6B),
  ("kingdom_24",  "Imperium Romanum Pars Otho",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x102810),
  ("kingdom_25",  "Imperium Romanum Pars Vespasianus",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x4A103A),
  ("kingdom_26",  "Imperium Romanum Pars Vitellius",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x4A0400),
  ("kingdom_27",  "Imperium Romanum Pars Galba",    0, 0.9, [("furor_teutonicus",-0.02),("egypt",-0.02),("alans",-0.02),("black_khergits",-0.02),("picton",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", 0.5),("forest_bandits", -0.05),("taiga_bandits", -0.05),("arabian_bandits", -0.05)], [], 0x081429),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),
  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),

  ("black_khergits","Rebelles", 0, 0.5,[("player_faction",-0.9),("outlaws",-0.02),("deserters",-0.02),("forest_bandits",-0.02),("mountain_bandits",-0.02),("kingdom_7",-0.9), ("kingdom_24",-0.9), ("kingdom_25",-0.9), ("kingdom_26",-0.9), ("kingdom_27",-0.9)], [], 0x401344),

  ("deserters","Deserters", 0, 0.05,[("merchants",-0.5),("player_faction",-0.1),("outlaws",-0.6),("forest_bandits",-0.02),("mountain_bandits",-0.02)], [], 0xE3E7CC),
  ("mountain_bandits","Rebelles Iudaicus", 0, 0.5,[("commoners",-0.2),("black_khergits",-0.02),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("forest_bandits",-0.02),("deserters",-0.02),("kingdom_17",0.75),], [], 0xE7AAC2),
  ("forest_bandits","Rebelles Hispanicus", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("mountain_bandits",-0.02),("deserters",-0.02),], [], 0xE7C36E),
  ("taiga_bandits","Rebelles Illyrius", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("mountain_bandits",-0.02),("deserters",-0.02),], [], 0xC1AAE7),
  ("arabian_bandits","Qaydar", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("mountain_bandits",-0.02),("deserters",-0.02),], [], 0xADE7A0),

  ("alans","Alanna", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("black_khergits",-0.6),("mountain_bandits",-0.02),("forest_bandits",-0.02),("deserters",-0.02),], [], 0xAAE7A3),
  ("furor_teutonicus","Teutones", 0, 0.5,[("alans",-0.2),("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("black_khergits",-0.6),("mountain_bandits",-0.02),("forest_bandits",-0.02),("deserters",-0.02),], [], 0xA19D8F),
  ("egypt","Remetjw-men-Maat", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("player_faction",-0.15),("outlaws",-0.6),("black_khergits",-0.6),("mountain_bandits",-0.02),("forest_bandits",-0.02),("deserters",-0.02),], [], 0xFFFF00),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ("picton","Piktoi", 0, 0.9,[("player_supporters_faction",-0.05),("merchants",-0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("deserters",-0.02),("player_faction",-0.4),], [], 0x6AB2FF),

  ##minor factions begin
  ("garamantes","Garamantes", 0, 0.9,[("gaetuli",-0.5),("merchants",-0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xAF8042),
  ("gaetuli","Gaetuli", 0, 0.9,[("garamantes",-0.5),("merchants",-0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xE8C597),
  ("nabataea","Malkuta Nabatu", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xC1460C),
  ("kush","Kusi", 0, 0.9,[("egypt",-0.02),("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xffff00),
  ("irish","Ebdani", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0x34ebbd),
  ("danish","Heruli", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0x917bb6),
  ("slavic","Geloni", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xb6a551),
  ("georgians","Diduroi", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0xA2E774),
  ("dahae","Dahae", 0, 0.9,[("merchants",0.5),("outlaws",-0.6),("mountain_bandits",-0.02),("black_khergits",-0.02),("deserters",-0.02),], [], 0x639652),

  ("minor_kingdoms_end","Greek", 0, 0,[], []),#use this as greek culture dummy for items
  #minor factions end

  ("gladiators","Gladiators", 0, 0.1, [], [], 0x888888),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+
