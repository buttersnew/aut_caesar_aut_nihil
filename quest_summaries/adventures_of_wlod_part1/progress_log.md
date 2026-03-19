# Progress Log for Wlodowiecus Part I Extraction

Date:
- 2026-03-19

Status:
- Complete

Task scope completed:
- Extracted the participating characters for qst_wlodowiecus_adventure_1 into 00_characters.md.
- Extracted the plot as ordered menu/dialogue files into this folder.
- Used only module_system/module_dialogs.py and module_system/module_game_menus.py, as requested.

Processed source blocks:

1. module_system/module_dialogs.py, approx. 99918-99990
Result: Olivarius quest start.

2. module_system/module_dialogs.py, approx. 76843-76865
Result: Ctesiphon magister civium caravan arrangement.

3. module_system/module_game_menus.py, approx. 57002-57029
Result: travel_to_sagala menu.

4. module_system/module_game_menus.py, approx. 57031-57100
Result: travel_to_sagala_2 menu.

5. module_system/module_dialogs.py, approx. 100270-100298
Result: first prison conversation with Wlodowiecus and Hadrianus.

6. module_system/module_dialogs.py, approx. 100035-100065
Result: guard refusal for Queen Karishma audience.

7. module_system/module_dialogs.py, approx. 100266-100340
Result: prison-break follow-up with Wlodowiecus.

8. module_system/module_game_menus.py, approx. 57145-57175
Result: escaped_sagala menu.

9. module_system/module_dialogs.py, approx. 100163-100330
Result: Mancinellus reunion in the cave.

10. module_system/module_game_menus.py, approx. 57176-57200
Result: jungle_final return menu.

11. module_system/module_dialogs.py, approx. 99930-99950
Result: Olivarius quest completion.

12. module_system/module_game_menus.py, approx. 62786-62800
Result: Temple of Mithras aftermath unlock.

Important decision log:
- Excluded a tempting false positive from module_system/module_dialogs.py around 100066-100162 because that scene is gated by qst_wlodowiecus_adventure_2, not qst_wlodowiecus_adventure_1.
- Kept the Temple of Mithras unlock because it is a direct post-quest consequence tied to the completion dialogue.
- Kept character origins limited to what these two files explicitly state or strongly imply.

Files created in this folder:
- 00_index.md
- 00_characters.md
- 01_dialog_olivarius_quest_start.md
- 02_dialog_magister_civium_ctesiphon.md
- 03_menu_travel_to_sagala.md
- 04_menu_arrival_in_sagala.md
- 05_dialog_wlodowiecus_in_prison.md
- 06_dialog_sagala_guard_refusal.md
- 07_dialog_wlodowiecus_prison_break.md
- 08_menu_escaped_sagala.md
- 09_dialog_mancinellus_reunion.md
- 10_menu_return_from_india.md
- 11_dialog_olivarius_quest_completion.md
- 12_menu_temple_of_mithras_unlock.md
- progress_log.md

If this work needs to be continued later:
- The extraction itself is finished.
- The next likely extension would be richer biographies from troop definitions or scene/mission logic, but those files were intentionally not used for this task.
