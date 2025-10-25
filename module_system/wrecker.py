import sys
sys.dont_write_bytecode = True

from os.path import split as path_split, exists as path_exists
import re
try:
    import colorama
    colorama.init()
    COLORAMA = ('\x1b[0m', '\x1b[31m', '\x1b[32m', '\x1b[33m', '\x1b[34m', '\x1b[35m', '\x1b[36m', '\x1b[37m')
except:
    COLORAMA = ('', '', '', '', '', '', '', '')

headers = [
	'header_animations.py',
	'header_common.py',
	'header_dialogs.py',
	'header_factions.py',
	'header_game_menus.py',
	'header_ground_types.py',
	'header_item_modifiers.py',
	'header_items.py',
	'header_map_icons.py',
	'header_meshes.py',
	'header_mission_templates.py',
	'header_mission_types.py',
	'header_music.py',
	'header_operations.py',
	'header_particle_systems.py',
	'header_parties.py',
	'header_postfx.py',
	'header_presentations.py',
	'header_quests.py',
	'header_scene_props.py',
	'header_scenes.py',
	'header_skills.py',
	'header_skins.py',
	'header_sounds.py',
	'header_strings.py',
	'header_tableau_materials.py',
	'header_terrain_types.py',
	'header_triggers.py',
	'header_troops.py'
]
modules = [
	'module_animations.py',
	'module_constants.py',
	'module_dialogs.py',
	'module_factions.py',
	'module_game_menus.py',
	'module_info.py',
	'module_info_pages.py',
	'module_items.py',
	'module_map_icons.py',
	'module_meshes.py',
	'module_mission_templates.py',
	'module_music.py',
	'module_particle_systems.py',
	'module_parties.py',
	'module_party_templates.py',
	'module_postfx.py',
	'module_presentations.py',
	'module_quests.py',
	'module_scene_props.py',
	'module_scenes.py',
	'module_scripts.py',
	'module_simple_triggers.py',
	'module_skills.py',
	'module_skins.py',
	'module_sounds.py',
	'module_strings.py',
	'module_tableau_materials.py',
	'module_triggers.py',
	'module_troops.py'
]

headers_package = path_exists('./headers')

## unused: [, 'tableau_': 'tableau.' 'spr_': 'spr.', ] all quoted references
identifier = {'icon_': 'icon.', 'prsnt_': 'prsnt.', 'p_': 'p.', 'psys_': 'psys.', 'mesh_': 'mesh.', 'itm_': 'itm.', 'qst_': 'qst.', 'pt_': 'pt.', 'trp_': 'trp.', 'ip_': 'ip.', 'mt_': 'mt.', 'anim_': 'anim.', 'pfx_': 'pfx.', 'snd_': 'snd.', 'scn_': 'scn.', 'mnu_': 'mnu.', 'imod_': 'imod.', 'skl_': 'skl.', 'script_': 'script.', 'track_': 'track.', 'fac_': 'fac.'}
old_id = identifier.keys()
new_id = identifier.values()

info = "\n\n\n\n###################################\n#   W.R.E.C.K. Compiler Options   #\n###################################\n\n\n\n# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.\n# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!\n\nwrite_id_files = \"ID_%s.py\"     # default vanilla-compatible option\n#write_id_files = \"ID/ID_%s.py\" # will put ID_* files in ID/ subfolder of module system's folder\n#write_id_files = None          # will suppress generation of ID_*.py files\n\n\n\n# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.\n\nshow_performance_data = False   # default: false\n\n\n\n##########################\n#   W.R.E.C.K. Plugins   #\n##########################\n\n\n\nimport plugin_ms_extension\nimport plugin_presentations\n\n#Plugins from `systems` subfolder are loaded automatically\nfrom systems import *"



quote = '"'
score = "_"

def check_file(string1, string2):
	is_found = string1.find(string2)
	if is_found != -1:
		return True
	else:
		return False

# special_str = re.compile(r'str_1_')
# not_str = re.compile(r'(str_clear|str_is_empty|str_store|str_encode|str_\d)')

# def find_char(string, char): 
#   character = string[:1]
#   if character is char:
#     return -1
#   else:
#     pass

def find_old_ref(string):
	for key in identifier:
		find_id = re.compile(r'[\s|\S]' + re.escape(key) )
		non_ref = re.compile(r'[\w."]' + re.escape(key) )
		found = find_id.findall(string)
		references = [f for f in found if not non_ref.match(f)]
		for ref in references:
			# isquote = find_char(ref, quote) ## Quoteed reference replacement deprecated. The number of errors it generated outweighed any desire for consistency, and it's unecessary anyway.
			# if isquote == -1:
			#   quoted = string.find(quote+old_id[r])
			#   next_quote = string.find(quote, quoted+1)
			#   quoted_reference = string[quoted:next_quote+1]
			#   new_ref = quoted_reference.strip(quote).replace(old_id[r], new_id[r], 1)
			#   new = string.replace(quoted_reference, new_ref)
			#   string = new
			# else:
			new = re.sub(key, identifier[key], ref, 1)
			final = string.replace(ref, new)
			string = final
	return string

## Deprecated; All string references to remain quoted, as they contain special characters(=, +, etc.) which mess with the compiler otherwise.
# def fix_string_refs(string):
#   first = special_str.sub('s.1_', string)
#   string = first
#   find_str = re.compile(r'[\s|\S]' + 'str_')
#   non_ref = re.compile(r'[\w.]' + 'str_' + r'[_]')
#   found = find_str.findall(string)
#   references = [f for f in found if not non_ref.match(f)]
#   for ref in references:
#     isquote = find_char(ref, quote)
#     thing = string.find(ref)
#     skip = not_str.findall(string)
#     if isquote == -1:
#       quoted = string.find('"str_')
#       next_quote = string.find(quote, quoted+1)
#       quoted_reference = string[quoted:next_quote+1]
#       new_ref = quoted_reference.strip(quote).replace('str_', 's.', 1)
#       new = string.replace(quoted_reference, new_ref)
#       string = new
#     elif not_str.match(string[thing+1:]):
#       pass
#     else:
#       new = re.sub('str_', 's.', ref)
#       final = string.replace(ref, new, 1)
#       string = final
#   return string


def wrecker(filename):
	with open(filename, "r", encoding='utf-8') as file:
		lines = file.readlines()

	with open(filename, "w", encoding='utf-8') as file:
		for line in lines:
			start = find_old_ref(line)
			line = start
			# finish = fix_string_refs(line)
			# line = finish
			file.write("%s"%line)

def remove_imports(filename):
	with open(filename, "r", encoding='utf-8') as file:
		lines = file.readlines()
	with open(filename,"w", encoding='utf-8') as file:
		imports = []
		for line in lines:
			if not line.startswith("from"):
				if not line.startswith("# -*- coding"):
					file.write("%s"%line)
			elif line.lower().find('bignum') != -1:
				file.write("%s"%line)

def add_import_compiler(filename):
	with open(filename,"r", encoding='utf-8') as file:
		lines = file.readlines()
	lines.insert(0, "from compiler import *\n")
	with open(filename,"w", encoding='utf-8') as file:
		for line in lines:
			file.write("%s"%line)

def add_wrecker_options(filename):

	test = "W.R.E.C.K. Compiler Options"

	with open(filename,"r") as file:
		lines = file.readlines()

	if test not in lines:
		print("expanding " + filename)
		with open(filename, "a") as file:
			file.write(info)



def print_menu():
		print("")
		print("{1}A note on syntax:{0}".format(*COLORAMA))
		print("")
		print("{2}    a) For files in the same directory, do not add any extra '.py'{0}".format(*COLORAMA))
		print("{2}       Example: module_troops{0}".format(*COLORAMA))
		print(" ")
		print("{2}    b) For files in subdirectories, add the subdirectory with a '/' to{0}".format(*COLORAMA))
		print("{2}       the beginning of the file name{0}".format(*COLORAMA))
		print("{2}       Example: MDL/module_troops{0}".format(*COLORAMA))
		print("")
		print("{6}1) WRECK files{0}".format(*COLORAMA))
		print("{6}2) Input a file to WRECK{0}".format(*COLORAMA))
		print("{6}3) Expand module_info.py - unnecessary if (1) has been done.{0}".format(*COLORAMA))
		print("{6}4) Print this menu again{0}".format(*COLORAMA))
		print("{6}0) Exit{0}".format(*COLORAMA))
		print("")

def process():

	legal_choices = set(["0","1","2","3","4"])
	choice =""
	errors = []
	print_menu()
	while choice != "0":
		choice =""
		while not choice in legal_choices:
			if errors:
				for e in errors:
					print(e)
					print()
				errors = []

			choice = input("Make a choice (4 to display menu again) >").lower().strip()

			if choice == '1':
				print("processing...")
				for module in modules:
					try:
						f = open(module, encoding='utf-8')
						f.readlines()
						f.close()
					except IOError:
						errors.append("{2}Error: no such module {0}{1}".format(module, *COLORAMA))
					except UnicodeDecodeError:
						errors.append("{2}Error: wrong file ecnoding {0}, required 'Utf-8'{1}".format(module, *COLORAMA))
					else:
						print("Fixing references in " + module)
						wrecker(module)
						remove_imports(module)
						add_import_compiler(module)
						
				for header in headers:
					try:
						f = open(header, encoding='utf-8')
						f.readlines()
						f.close()
					except IOError:
						errors.append("{2}Error: no such header {0}{1}".format(header, *COLORAMA))
					except UnicodeDecodeError:
						errors.append("{2}Error: wrong file ecnoding {0}, required 'Utf-8'{1}".format(header, *COLORAMA))
					else:
						print("Fixing imports in " + header)
						remove_imports(header)

				add_wrecker_options("module_info.py")
				print("")

			elif choice == '2':
				response = input('Input a file to process: ') + ".py"
				try:
					f = open(response)
					f.close()
				except IOError:
					print("No such file %s" % response)
				else:
					print("Fixing references in " + response)
					wrecker(response)
					remove_imports(response)
					add_import_compiler(response)
				print("")

			elif choice == '3':
				add_wrecker_options("module_info.py")
				print("")

			elif choice == '4':
				exit()

if __name__ == '__main__':
	process()

