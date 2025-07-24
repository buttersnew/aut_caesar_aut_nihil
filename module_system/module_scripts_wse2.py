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


scripts_wse2 = [
# #script_wse_multiplayer_message_received
# # Called each time a composite multiplayer message is received
# # INPUT
# # script param 1 = sender player no
# # script param 2 = event no
# ("wse_multiplayer_message_received", [
# 	# (store_script_param, ":player_no", 1),
# 	# (store_script_param, ":event_no", 2),
# ]),

# #script_wse_game_saved
# # Called each time after game is saved successfully
# ("wse_game_saved", [
# 	# (store_script_param, ":savegame_no", 1),
# ]),

# #script_wse_savegame_loaded
# # Called each time after savegame is loaded successfully
# ("wse_savegame_loaded", [
# 	# (store_script_param, ":savegame_no", 1),
# ]),

# #script_wse_chat_message_received
# # Called each time a chat message is received (both for servers and clients)
# # INPUT
# # script param 1 = sender player no
# # script param 2 = chat type (0 = global, 1 = team)
# # s0 = message
# # OUTPUT
# # trigger result = anything non-zero suppresses default chat behavior. Server will not even broadcast messages to clients.
# # result string = changes message text for default chat behavior (if not suppressed).
# ("wse_chat_message_received", [
# 	# (store_script_param, ":player_no", 1),
# 	# (store_script_param, ":chat_type", 2),
# ]),

# #script_wse_console_command_received
# # Called each time a command is typed on the dedicated server console or received with RCON (after parsing standard commands)
# # INPUT
# # script param 1 = command type (0 - local, 1 - remote)
# # script param 2 = num parts if bAutoSplitModuleConsoleCommands enabled
# # s0 = text
# # OUTPUT
# # trigger result = anything non-zero if the command succeeded
# # result string = message to display on success (if empty, default message will be used)
# ("wse_console_command_received", [
# 	# (store_script_param, ":command_type", 1),
# 	# (store_script_param, ":num_parts", 2),
# ]),

# #script_wse_get_agent_scale
# # Called each time an agent is created
# # INPUT
# # script param 1 = troop no
# # script param 2 = horse item no
# # script param 3 = horse item modifier
# # script param 4 = player no
# # OUTPUT
# # trigger result = agent scale (fixed point)
# ("wse_get_agent_scale", [
# 	# (store_script_param, ":troop_no", 1),
# 	# (store_script_param, ":horse_item_no", 2),
# 	# (store_script_param, ":horse_item_modifier", 3),
# 	# (store_script_param, ":player_no", 4),
# ]),

# #script_wse_window_opened
# # Called each time a window (party/inventory/character) is opened
# # INPUT
# # script param 1 = window no
# # script param 2 = window param 1
# # script param 3 = window param 2
# # OUTPUT
# # trigger result = presentation that replaces the window (if not set or negative, window will open normally)
# ("wse_window_opened", [
# 	# (store_script_param, ":window_no", 1),
# 	# (store_script_param, ":window_param_1", 2),
# 	# (store_script_param, ":window_param_2", 3),
# ]),

# #script_wse_get_server_info
# # Called each time a http request for server info received (http://server_ip:server_port/)
# # OUTPUT
# # trigger result = anything non-zero replace message text for response info
# # result string =  message text for response info
# ("wse_get_server_info", [
# ]),

# #script_wse_initial_window_start
# # Called each time after initial window started with bMainMenuScene=true (requires WSE2)
# ("wse_initial_window_start", [
# ]),
]#end of file
