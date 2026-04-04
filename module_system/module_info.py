
from __future__ import absolute_import
import subprocess

_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
if _branch == "main":
    export_dir = "C:/Users/maxim/Dropbox/ACAN Modding/Current PILOS/MB Warband - ACAN/Modules/Aut Caesar aut nihil/"
    print("Exporting to main branch directory:", export_dir)
else:
    export_dir = "C:/Users/maxim/Dropbox/ACAN Modding/Current PILOS/MB Warband - ACAN/Modules/Aut Caesar aut nihil dev/"
    print("Exporting to dev branch directory:", export_dir)

## Build release txt files in the <Module> subfolder
#export_dir = path + "/Module/"

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
