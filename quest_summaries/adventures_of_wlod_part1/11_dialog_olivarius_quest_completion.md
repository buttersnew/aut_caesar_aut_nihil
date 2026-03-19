# 11. Olivarius Rewards the Player and Ends the Quest

Source:
- module_system/module_dialogs.py
- Approx. lines 99930-99950

Quest state:
- 6 -> quest succeeded and ended

Speakers:
- Olivarius
- Player

Completion path:

Olivarius: "Any news of the Wlodowiecus expedition?"

Player: "I have found Wlodowiecus and returned with enough marble for dozens of statues!"

Olivarius: "Perfect. I will make a statue for you and one for the Mithras cultists. Thank you very much {playername}. You saved my business."

Mechanical outcome in this block:
- The quest succeeds and ends.
- The player receives the Mithras item.
- Olivarius relation increases by 75.
- The log message says: "The cult of Mithras has established a temple in Rome."

Other line present in the same block:

Player: "I am still working on it."
