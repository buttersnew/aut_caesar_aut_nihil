
from __future__ import absolute_import
import os
# Original Windows path for development
#export_dir = "C:/Users/maxim/Dropbox/ACAN Modding/Current PILOS/MB Warband - ACAN/Modules/Aut Caesar aut nihil/"

# Use relative path that works on any platform
module_system_dir = os.path.dirname(os.path.abspath(__file__))
export_dir = os.path.join(os.path.dirname(module_system_dir), "Aut_Caesar_Aut_Nihil") + "/"

###################################
#   W.R.E.C.K. Compiler Options   #
###################################


# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.
# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!
# Default value: "ID_%s.py"

write_id_files = "IDs/ID_%s.py"    # default vanilla-compatible option
#write_id_files = "ID/ID_%s.py" # will put ID_* files in ID/ subfolder of module system's folder
#write_id_files = None          # will suppress generation of ID_*.py files


# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.
# Default value: False

#show_performance_data = True



# ##########################
# #   W.R.E.C.K. Plugins   #
# ##########################

# import plugin_ms_extension
# #import plugin_item_factions_limit_remover
# import plugin_presentations

from systems import *
