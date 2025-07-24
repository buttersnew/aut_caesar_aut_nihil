# -*- coding: cp1254 -*-
import string
from header_common import *
from header_presentations import *
from header_mission_templates import *
from IDs.ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_terrain_types import *
from module_items import *
from header_skills import *
from module_info_pages import *
from module_factions import *
from IDs.ID_postfx_params import *
from IDs.ID_factions import *
from header_parties import *

presentations_wse2 = [
#prsnt_wse_mission_debug_window
# Called each time a mission debug window is opened (ctrl + R with enabled edit mode)
# TRIGGERS
# ti_on_presentation_run
# Trigger param 1 = how much time has passed since presentation has been started (in milliseconds)
# Trigger param 2 = selected agent no
# ("wse_mission_debug_window", 0, 0, [
# 	# (ti_on_presentation_load, [
# 	# 	(set_fixed_point_multiplier, 1000),

# 	# 	(presentation_set_duration, 999999),
# 	# ]),

# 	# (ti_on_presentation_run, [
# 	# 	(store_trigger_param_1, ":cur_time"),
# 	# 	(store_trigger_param_2, ":selected_agent_no"),

# 	# ]),
# ]),
]