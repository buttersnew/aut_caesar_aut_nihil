-------------------
| Compatibilities |
-------------------

1) WRECK works on Python version 3! Doesn't work with 2.
2) [WRECK integrated] Doesn't support ModMerger Framework and KT0 autoresolver script. Use WRECK plugin system instead.
3) Global variables in quotes are not case sensitive (unlike vanilla compiler "built_module.bat") - "$g_My_Variable" and "$g_my_variable" are the same variable in WRECK but Vanilla compiler thinks they are different. Advanced expressions should be all lower case.
4) WRECK doesn't track usage of global variables. Native compiler add +1 to entry in the file "variable_uses.txt". So the warning "Global variable declared but never used" is shown only when you add new global variable but not when you remove code where it was used. You need to delete file "variable_uses.txt" to see this warning. This file together with "variables.txt" is used to create reserved global variables for compatibility with new updates. For this you need to add reserved global variable to file "variables.txt" and add 1 to the same line in the file "variable_uses.txt". This is redundant work. Also why you need reserved order of identificators for global variables? There is no operators like try_for_global_variables. Use slots of troops instead.
5) [WRECK integrated] Unlike vanilla it was not possible to copy with python entities (party, item, troop, etc) because they are complex recursive wreck objects. Example - generattion of no-swing weapons in Motomataru formation script. For this use new function <newcopy()> it was added in v1.0.3.
6) Viking Conquest module system adds trigger to all mission templates automatically. So you need to add code for WRECK in the end of "module_mission_templates.py".
CODE:
-----------------------------------------------------------------
import __main__
if __main__.__file__ == 'compile.py':#This is WRECK compiler?
   for mission in mission_templates:
      mission[5].append(*global_common_triggers)
-----------------------------------------------------------------


--------------
| Change log |
--------------

v1.1.4
1) Added an error of using this_or_next without closing condtion.
2) New macro operands from 'Universal Mission Scripts Handler'.
       (push_script_with_params, <time_out_msec>, <script_callback>, <param1>, [<param2>, ...]),
       (get_params, <param1>, [<param2>,...]),
   For example, when agent is spawning you don't know if he is a rider because horses are not spawned yet.
       So you can deal with this agent in the same frame after non-timer triggers.
   For more info, examples and vanilla compatible code look into:
       https://forums.taleworlds.com/index.php?threads/python-script-scheme-exchange.8652/post-9906974
      


v1.1.3
1) New warnings of nested performance heavy loops. By default this notices are turned off. To turn them on remove <nested_loops> from command line in the file "compile.bat". You can customise operations in the file "header_operations.py" by changing/creating list "performance_heavy_loops". Default performance_heavy_loops = [try_for_agents, try_for_parties, try_for_prop_instances]. If this list is present it will replace default values.
2) Fixed error 'TypeError' has no attribute 'message' caused by migrating from Python 2 to 3.
3) Fixed bug of processing animations. If there were no subsequent animation then string "none 0 0" was added wich crashed engine at loading.
4) Added support for items plural name. Just add string to items 3d position. ("tutorial_axe", "Axe", "Axes"), Can be used with operand
(str_store_item_name_plural, <string_register>, <item_id>),
5) Changed <colorama> syntax for compatibility with python 3.12.
6) Removed header folder loading.
7) Fixed error when using property of entities like trp.knight.level.
8) Added items difficulty check of troops equipment.

v1.1.2
1) Added "plugin_item_factions_limit_remover.py". It helps to bypass 16 faction limit for items. Uncomment in 'module_info.py' for usage.
2) Updated to WSE v1.1.1.0 

v1.1.1
1) Troops flags moved to trp_troop_flags to fix auto_menu entering when game started.
2) Added placeholder strings of animation's names up to 200 so it is possible to add new animations.
3) Added triggers_paranoia mode that checks non-timer triggers in mission_templates that used more than once if trigger parameters changed. This usually caused by operators that fires different non-timer trigger inside another non-timer trigger. On release remove parameter `triggers_paranoia` from compile.bat.
4) WSE updated up to v1.1.0.7

v1.1.0
1) Works on python version 3 wich has improved performance.
2) New command line parameter: 'test'. WRECK will compile the module but won't save anything on disk. Essentially a syntax check.
3) New command line parameter: 'time' - showing performace.
4) New command line parameter: 'prsnt_helper' - add scripted help panel to presentations to speed up layout process, required plugin_presentations.py and plugin_ms_extension.py.
   This panel can change any overlay position and size. HotKey [F]- switch panel position (bottom/top/hide). When mouse cursor hovering over overlay its ID will be displayed in log.
   Scripted code added by compiler to all presentations. If overlay created with macros then information about its type, size and position will be remembered.
   When changed unknown overlays its information also remembered. There are some bugs, for example when panel intersects with other containers. Some buttons don't work yet.
5) Added Lav's license information
6) Added integrated module system with WSE v1.0.9.9
7) Added modified WRECKER originally devoloped by mercury19.

v1.0.6
1) Improved compatibility with vanilla compiler. WRECK produces 99% of vanilla code. Exceptions are mission template triggers. They have counters (trigger_ID) in the last number of fake (useless) operand. Items don't generate hit_point values if they don't have them.
2) Identifiers and global variables decapitilised and white spaces changed to underscore. WRECK shows notices about capital characters. You need to change them for compatibility with vanilla compiler wich not always "cure" identifiers. To disable decapitalisation add "cap" to command line. Only music tracks are exception for this rule.
3) Faction relations use the last relation value in module like vanilla. WRECK shows conflicts to resolve. To reduce notices add "fac" to command line.

Keep in mind that "cap" and "fac" options are only temporary. Better to fix all notices for compatibility with vanilla compiler and reducing bugs.
compile.bat CODE:
---------------------------------------------------------
python compile.py tag cap fac %1 %2 %3 %4 %5 %6 %7 %8 %9
---------------------------------------------------------



v1.0.5
1) Added more detailed explanation to hint of syntax errors.

v1.0.4
1) In mission templates added unused operand to the end of each trigger: <(lt, -1, id),>
where ID is the number of this trigger starting from 0. Helper for debugging engine error messages.
2) Removed duplicate notices about unused local variable of repeatable mission triggers.
3) When compiler message show trigger name, it will be more informative - with each of the three timers if trigger is not simple. Previously was only the first.

v1.0.3
1) [WRECK integrated] fixed expressions in module_mission_template.py triggers. They were bugged if used more than once.
2) Added checking audio file extensions.
3) WRECK will check output dialog states like in Native compiler.

v1.0.2
1) Script that can fail will be checked for letters "cf_" in the begining of its name.
2) Local variables that have "unused" in their name will not be checked for warning "Variable declared but never used".
3) [WRECK integrated] Warning "Variable declared but never used" will now check expressions.
4) [WRECK integrated] Local variables declared by WRECK expressions in the loop conditions (try_for_range) will not be overriden by temp variable inside loop body.

v1.0.1
1) Fixed processing module_skins.py - removed extra spaces wich led to errors in OpenBrf
2) Fixed processing module_sounds.py - sound file can now be declared as list with faction ["sound_file.flac", fac_outlaw]. WRECK works with WithFire&Sword and NapoleonicWars MS now.
3) try_for_range_backwards will not show unused variable warning.