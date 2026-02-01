#from compiler import *
####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
##diplomacy start+
from __future__ import absolute_import
from module_constants import DPLMC_DIPLOMACY_VERSION_STRING, triumph_threshold
##diplomacy end+

info_pages = [
("overview", " Overview", "Overview"),

## diplomacy
("dplmc_autoloot", "Diplomacy Feature: Autoloot", "Autoloot settings are managed through the camp menu. It allows you to have your companions (named heroes, not ordinary soldiers) automatically select equipment from the loot after a battle.d^^ In order for this feature to be enabled, one of the following must be true: someone in your party must have a Looting score of 2 or better, someone in your party must have an Inventory Management score of 3 or better, or the player {him/her}self must have an Inventory Management score of 2 or better.d^^ The desired primary damage types (the higher of any swing/thrust damage) for melee and throwing weapons can be set up here. In addition, players can fine-tune weapon selection for two-handed/one-handed weapons, pikes, lances, and bladed polearms.^^This setting is currently:"),
("dplmc_autosell", "Diplomacy Feature: Autosell", "The Autosell feature allows you  to sell many items to a merchant all at once, instead of selling them one at a time. Autosell settings are managed through the Town menu, where you can specify which types of items you want to be able to sell (e.g. you might not want to automatically sell horses) and a price limit (for example, you might not want to automatically sell any items that cost more than 200 denarii).^^ There are two primary ways to use autosell.  If you speak to a Horse Merchant, Armorer, or Weapon Merchant in a town, there is a conversation option to sell items of a particular type.  Also, when visiting a town there will be an option in the Marketplace section of the menu to automatically sell your items throughout the town.^^ For people who used Autosell in other mods, note that this sells from your own inventory, according to certain rules.  Items you have equipped will never be sold, and neither will the first three items in your inventory.  After that, autosell also skips anything that it thinks might be your personal equipment (since people often have more than one set).  Regardless of whether you have them equipped, it won't sell your best bow, crossbow, armor, helmet, boots, or gloves. If you have a bow you can use, it won't sell your best three packs of arrows, and if you have a crossbow it won't sell your best three packs of bolts. For shields, one-handed weapons, two-handed weapons, polearms, and horses, it won't sell your best or second-best item. Your best three throwing weapons also will not be sold. However, items that your character is unable to use are considered fair game."),

("dplmc_deathcamera", "Diplomacy Feature: Battle Continuation", "Post-battle continuation allow you to watch the battle unfold after being knocked unconscious. Camera key bindings are available from the Diplomacy preference menus. In general numpad keys are used to rotate while movement keys are used to pan the camera. There are three camera modes available."),

("dplmc_disguise", "Diplomacy Feature: Player Disguise",
"The player disguise system allows the player to take on the role of various commoners while attempting to sneak into a town. In addition to the original pilgrim robes, players are able to acquire new sets of equipment from merchants and their chamberlains."
+"^In Native, the chance to be caught depends on the number of men in the party. The new system calculates the chance to be caught based on the player's chosen role instead, but limits what the player can bring in and out of towns in terms of gold and items."
+" The player's inventory will be merged after leaving the town."),

("hoty_keys", "HOT KEYS", "Here is a list of all keys and where they are used:^"
+"^^CONTROL - KEY: ^^*) By pressing control while clicking on 'trade with the goods merchant' or 'Buy supplies from the peasants.' player can automatically buy all food items. If player has a follower party, food will be added to the follower party."
+"^*) Player can modify time-flow by keeping control pressed an clicking one of the numpad-keys:"
+"^    -) 0 Key: sets time-flow to lowest, almost pausing game.^    -) 1 key: sets time-flow to 25%^    -) 2 key: sets time-flow to 50%^    -) 3 key: sets time-flow to 75%^    -) 4 key: sets time-flow to 100% (normal)^    -) 5 key: sets time-flow to 125%^    -) 6 key: sets time-flow to 150%^    -) 7 key: sets time-flow to 175%^    -) 8 key: sets time-flow to 200%^    -) 9 key: sets time-flow to 225%"
+"^^SHIFT - KEY: ^^*) By pressing Shift while clicking on 'Visit the Great Hall/Praetorium/Atrium, etc.,' a selection menu will pop up, allowing the player to talk with lords or ladies instantaneously.^*) Player can right away start a conversation with any town merchant by pressing 'shift' while clicking on 'trade with the XY'. ^*) By pressing 'shift' while clicking on 'visit the Domus Augusti' player will spawn next to advisors. ^*) After the player has visited a Roman temple for the first time he can spawn right next to the priest by pressing shift while clicking on 'visit the temple of XY'. ^*) The administrator of the latifundium can be quickly accessed by pressing 'shift' while clicking on 'visit the villa'."
+"^^ENTER - KEY: ^^*) During battle player can open strategic view, which allows player an overview over the battlefield. This camera follows the player. While activated, one may increase distance with the F key and reduce it with the V key. +/- for zoom, numpad for game speed (when cheats are enabled), and mouse wheel for camera speed."
+"^^H - KEY: ^^*) Allows you to call your horse during battle (if it is still alive) "
+"^^K - KEY: ^^*) During battle pressing K will start a shield taunt. ^*) While on worldmap, pressing K during freelancing allows player to access the daily missions menu."
+"^^T - KEY: ^^*) By pressing T player will perform a warcry during battles. ^*) While entering the lords hall player will make a handkiss by pressing T."
+"^^J - KEY: ^^*) Player can change the movement speed of troops during battles by pressing J"
+"^^G - KEY: ^^*) Player's horse will start to sprint during horse races by pressing J"
+"^^Z - KEY: ^^*) Pressing Z allows player to crouch (For German keyboards it is the Y key). Though it can be changed under game options -> controls."
+"^^^The keys for the death-camera can be changed under the Diplomacy preference menu."),

("companions", "Companions", "Companions do no longer spawn randomly in taverns. They all have fixed locations or quests which enable them. Here is a complete list of all companions:^^"
+"^*)  Pravare Ytarim               Location: Chersonesos, location in town: stables."
+"^*)  Marius Gaius                 Location: Antiocha, location in town: market."
+"^*)  Pulchra                      Location: Nicomedia, location in town: tavern."
+"^*)  Abadutiker                   Location: Truso, location in town: Castle Courtyard (next to gate)."
+"^*)  Satibarzanes                 Location: Ectabana, location in town: stable."
+"^*)  Firentrix                    Location: Corduba, location in town: tavern."
+"^*)  Lavia                        Location: Alexadria, location in town: streets."
+"^*)  Hildr                        Location: Uburzis, location in town: tavern."
+"^*)  Aturius Spurus               Location: Lugdunum, location in town: tavern."
+"^*)  Attaklos                     Location: Athenai, location in town: tavern."
+"^*)  Dionysia                     Location: Thessalonica, location in town: marketplace."
+"^*)  Jeremus                      Location: Lutetia, location in town: tavern."
+"^*)  Chanakya                     Location: Ctesiphon, location in town: center."
+"^*)  Titus                        Location: Mediolanum, location in town: tavern."
+"^*)  Artimenus                    Location: Vindobona, location in town: castle hall."
+"^*)  Titocuna                     Location: Deva, location in town: tavern."
+"^*)  Anicetus                     Location: Phasis, location in town: tavern."
+"^*)  Arminius                     Location: Palmyra, location in town: center."
+"^*)  Tertius Maior                Location: Palmyra, location in town: tavern."
+"^*)  Secundus Minor               Location: Dura Europos, location in town: center."
+"^*)  Drusus                       Location: Dyrrachium, location in town: tavern."
+"^*)  Libertus Tiro                Location: Tarraco, location in town: tavern."
+"^*)  Marcus Tullius               Location: Augusta Emerita, location in town: center."
+"^*)  Sidonius Apollinaris         Location: Hierosolyma, location in town: tavern."
+"^*)  Sollius Modestus             Location: Thebae, location in town: center."
+"^*)  Albinus Basilius             Location: Mtskheta, location in town: tavern."
+"^*)  Lucullus Caepio              Location: Carthago, location in town: center."
+"^*)  Anicius                      Location: Massilia, location in town: tavern."
+"^*)  Fabianus                     Location: Augusta, location in town: tavern."
+"^*)  Rombus                       Location: Ancyra, location in town: tavern."
+"^*)  Gaius Lemonius               Location: Neapolis, location in town: center."
+"^*)  Lucius Modius minor          Location: Tarentum, location in town: center."
+"^*)  Ra Karak                     Location: None, joins when doing the 'blossom in the desert' quest."
+"^*)  Ligia (and Ursus)            Location: Rome, location in town: side street (where Olivarius is)."
+"^*)  Marcus Vinicius              Location: Rome, location in town: tavern."
+"^*)  Josephus                     Location: Masada, location in town: center."
+"^*)  Elazar Bar Yochai            Location: Leptis Magna, location in town: center."
),

("provinces", "Provinces", "Every town, fortress and village is part of a province. The respective province can be seen under the center notes.\
 But it is also possible to display the province name in the center name. The option is only available at game start.^\
 One can choose between three different naming schemes for the centers:\
 ^^Normal: The normal name is displayed, like in native.\
 ^^Accurate: The accurate province name which is also displayed in the center notes, will also be displayed in the center name.\
 ^^Simple: A simplified province name will be displayed in the center name.^^^\
 Note, that the simplified province names are more general than the accurate ones. Here is a list of the abbreviations used:^^\
 HS - Hispania^\
 GL - Gallia^\
 BR - Britannia^\
 MG - Magna Germania^\
 IT - Italia^\
 IL - Illyria^\
 GR - Graecia ^\
 DA - Dacia^\
 TH - Thracia^\
 AN - Anatolia^\
 AR - Armenia^\
 MS - Mesopotamia^\
 SY - Syria^\
 JD - Judea^\
 EG - Aegyptus^\
 AF - Africa^\
 SM - Sarmatia^\
 CA - Caucasus^\
 RN - Reatia et Noricum^\
 CY - Cyprus^\
 CS - Corsica et Sardinia\
 PR - Persia and Media"
),

("provinces_abbreviations", "Settlement naming settings", "At the start of the game, player can choose between three different naming schemes for the centers:\
 ^^Normal: The normal name is displayed, like in native.\
 ^^Accurate: The accurate province name which is also displayed in the center notes, will also be displayed in the center name.\
 ^^Simple: A simplified province name will be displayed in the center name.^^^\
 Note, that the simplified province names are more general than the accurate ones. Here is a list of all abbreviations used:^^\
 HS - Hispania^\
 GL - Gallia^\
 BR - Britannia^\
 MG - Magna Germania^\
 IT - Italia^\
 IL - Illyria^\
 GR - Graecia ^\
 DA - Dacia^\
 TH - Thracia^\
 AN - Anatolia^\
 AR - Armenia^\
 MS - Mesopotamia^\
 SY - Syria^\
 JD - Judea^\
 EG - Aegyptus^\
 AF - Africa^\
 SM - Sarmatia^\
 CA - Caucasus^\
 RN - Reatia et Noricum^\
 CY - Cyprus^\
 CS - Corsica et Sardinia\
 PR - Persia and Media"
),

("q_and_q", "Useful informations",
"Triumphs:^As Roman player may gets a triumph awarded. For this you need at least " + str(triumph_threshold) + " gravitas. You obtain gravitas by winning battles as marshal. Gravitas will decline over time though. You can see your current gravitas in the character notes. As Emperor you can also hold a triumph with less gravitas but this will upset the Romans."
+"^^Battle field fortifications: ^As Roman you can fortify your camp. It requires a set of tools inside your inventory and an engineer skill higher than 5. Once fortified you can no longer move. It is also possible during sieges."
+"^^Lending out money: ^Visit an argentarii (who can be found inside a scriptorium) to lend out money or to just store your money in a safe place. You can lend out a loans between 5,000 and 500,000 denarii. The loan will expire after a week. Once it expires the money will be added TO THE NEXT budget report."
+" This can take a while. Depending on when you issued the loan and depending on when your next budget report will show it can take between one or two weeks until your receive the interests."
+" For your loan you have two options. Either you order the argentarius to reinvest the money again, or you order him to send you back all the money. In the first case,"
+" you will only receive the interests of your loan and a new loan will be lend out right away after recieving the interests. In the later case you will receive all the money back. Sometimes the interests can be negative. That shall simulate the case"
+" when the debtor is not able to repay the loan you offered him."
+"^^Diplomacy feature:^ You can become part of a family. To do this you must talk with a lord, depending the character of the lord you must either be hounorable, or dishounorable, "
+"famous, have a good relation or own a fief or wealth.^^"
+"You need at least 200 renown to be considered as a full citizen of Rome. With 200 renown you can: Enter the great hall of towns and fortresses and you must pay the punitive tax (Lex Julia et Papia)."
+"If you are Emperor or have a military rank in the Roman Army your renown won't go beyond: 450 if emperor, 200 if common military rank.^^"
+"If you own a fief and you are part of the Roman Empire you must pay taxes to the Emperor, taxrate depends on circumstances. (usually 20%)^"
+"If you are part of the Roman Army (not as mercenary!) you won't have to pay wages for your troops in your party. But you must still pay for garrisons.^^"
+"Be aware: after some years the great Jewish revolt will start (if not triggered by player)^^"
+"Player can convert to Judaism (at the great temple in Hierosolyma), this enables the following features: Player can fund Judean rebels at the great temple in Hierosolyma, player can start the Jewish revolt and fight for Judea: Only possible if player hasn't joined any other faction yet.^^"
+"You can usurp towns from other governors (=Lords) with bad reputation type (quarrelsome, selfrighteous, sadisitic (debauched), cunning): You need more than 25 relation with the town, at least 300 renown and must be in the same faction,"
+"then you will receive an event when you visit the town. Nero will only give you the town if you don't already own one, and if you have a higher relation with him than the old governor. If your attempt fail, you will gain a new chance after 50 days.^^"
+"You can become the lover of a married woman. Firstly you must improve your relation with her. Then, depending on your charisma, her personality and luck she may says yes to you."
+"But if your relation with her becomes to low (beyond 10) then she will break with you. There is also some random chance that she breaks, because she finds someone more interesting.^"
+"If you have high enough relation (and a good persuasion skill) with a lady, she may tell you the latest rumor about a love affair. You can use this information to your advantage.^"
+"Your spouse can have a love affair too. If you think she has one, you can send one of your companions to spy her. "
+"Depending on the intelligence skill of the companion he may find out if she has a love affair or not. If she has a lover and your companion has found it out you can talk with her and divorce.^^"
+"As Emperor you should always watch your enemies in your own faction, if they grow too many, they may assassinate you.^^"
+"As Emperor you can imprison any person you want (town or village walkers and your generals/lords)^^"
+"If you have a prisoner tower in a town or fort, you can torture your enemies. Simply visit the prison and talk with the torturer.^^"
+"You can deposit money in Roman towns. Simply talk with the praefectus of the city, who can be found in the scriptorium.^^"
+"You can buy all Roman weapons, armors, helmets and shields from the merchant Gaius Marius, who can be found in the streets of Rome.^^"
+"There are some drinking 'mini games' ingame: You can toast with Lords during feasts and you can make a drinking competition with tavern shoppers. A high strength attribute is needed if you want to win.^^"
+"The players health can decrease over time (see characters report for information about your current status). You will become more unhealthy, if you get knocked down during battle, and due to various other stuff (drinking competitions for example)."
+"To increase your health visit the baths frequently.^^"
+"As Emperor, you must answer petitions regularly. If you don't want to do this, talk with your political advisor, who can be found in the Domus Augustus in Rome.^^"
+"The gold item can used to hire warbands from the Nabateans, Garmantians and Gaetulians, by talking with their respective kings.^^"
+"You can order your companions to establish permanent camps (option in the camp menu) and to create their own parties (by talking with them via the party screen):^"
+"You can also store items and prisoners in the camp. But be aware, the camp can be attacked by enemy parties and if it is destroyed all items and prisoners will be lost.^^"
+"You can get honorary titles if you ask Emperor Nero for a reward. You need high relation with him for this dialogue option to become available.^^"
+"Freelancing is only available for Roman legions, talk either with a legate commanding a legion directly or with a Praefectus Castrorum or Praefectus, who can be found in the scriptorium.^^"
+"For freelancing in the Praetorian guard you need a letter of recommendation, this you can obtain once you reached the rank of Optio, while freelancing in a normal legion.^^"
+"You can go hunting via the camp menu.^^"
+"Roman officers provide a skill bonus: ^High rank officers, like Vexilarius, Aquilifer, Primus Pilus and Tribunus provide a bonus to leadership skill."
+"For each 100 men in your party you need two officers (centurio, signifer etc.), otherwise you will get a malus on tactics skill. The only non-Roman 'officer' is currently the hornman."
+"The idea behind this is the following: Larger armies are more difficult to lead during battles. The orders you give must reach the soldiers. Officers and musicians can help with that.^^"
+"Sailors can be found as mercenaries in taverns of port towns. Each sailor in the party increases party speed on water by 1% up to a maximum of 40%. (Also sea raiders in your party will increase speed on water)^^"
+"Commander panel: ^With an army large than 40 men you have access to the commander panel before a battle starts. It allows you to make sacrifices to the gods (improves moral, depends on a dice role, is a good choice if you have a low oratory skill), "
+"give a speech (depending on your oratory, persuasion and leadership skill it is either a success or fail) or to send skirmishers to attack the enemy (success depends on your tactics skill).^^"
+"Currently the escape change for a hero after battle is: 37%. Note that this also effect the player."),

("army_stances", "Party stances and Ambushes", "Quite similar to games from the Total War series you can order your party a stance. There are three different stances:^^\
- Default: No effects^\
- Screening: Your party will march more careful and try to avoid ambushes (probability reduced by 50%), but this will decrease movement speed by 30%^\
- Forced march: Your party will march faster (40%), but the probability to get ambushed is higher (40% increase). Additionally, your party consumes 2-times as much food and moral will be reduced over time (as your men get tired from the forced march they need more to eat)^^\
Ambushes:^\
Ambushes can be performed by every non Roman faction once every two hours. But the probability is much higher for Germanic, British and Judean factions.^\
You can decrease ambush probability by increasing your tracking skill and by using the 'screening' stance. During ambushes, you will receive random causalities caused by traps \
which the enemy has laid. Additionally, on the battlefield you will encounter burning fire-balls, which can cause additional causalities."),

("morale2", "Morale Management", "The way the moral of the players party is calculated is different from native. There are several new events which effect moral, for instance: traveling through deserts or campaigning during winter negatively impacts moral. Base moral depends mainly on the party size: if you are near the maximum size you will get high penalties and need to entertain your troops regularly to keep moral high enough (e.g. follower women). Its reasonable to travel not always at full size, but only if needed during campaigns. \
^^You have several ways to improve the moral of your party: ^You can pay them extra wages.  \
 ^You can pay them mead or wine in taverns. ^ If you have Camp Followers, \
 Hunter Women, Camp Defenders, Soldier Wives, refugees or simple Peasant Women in you party, they will improve moral over time (the more you have the more moral will be improved, \
 the maximum is 10 moral points)^You can also improve your party moral with the help of priests\
 ^The Roman Army offers other ways to improve moral through disciplinary action, talk to your officers to get access to them.^Resting at towns and forts regularly also improves moral. If you don't rest regularly your party will accumulate a moral penalty. (this feature can be disabled in options)"),

("follower_party", "Follower party",
    "For creating a follower party you need to have at least 60 men in your main party, have 10 non-wounded women and 2,500 denarii for hiring a physician and mules."
    +" Once created, the follower party will automatically disband if you either get defeated or your party size goes below 40 men.^^"
    +" You can manage the follower party over the camp menu. There you can add more women to the party, store items on the mules or use the physician to treat major wounds. You can also add sailors to the follower party which will grant you a speed bonus when on water. But the troops in the follower party wont fight during battles. You can also manually disband the follower party.^^"
    +" Other advantages of the follower party:^"
    +"^-) Food items stored on the mules will be consumed by your party, saving space in your inventory."
    +"^-) If you enable to automatically buy food after leaving a town, the food will be added to your follower party, if you have one (saving your own inventory space)."
    +"^-) Having soldier wives in your follower party improves your surgery skill (up to 3)"
    +"^-) Having camp followers, hunter women, camp defender or soldier wives in your follower party improves your wound treatment skill (up to 3)"
    +"^-) For women in your follower party you gain a moral bonus."
    +"^-) Women in your follower party won't fight on the battlefield and you don't have to pay wages for them."
    +"^^As a disadvantage, a follower party will significantly slow down your army."
),

("aor", "AOR Recruitment", "All Auxiliary cohorts are listed here:^^\
Cohors Alporum: recruitable in barracks in: Augusta Vindelicorum, Vindobona, Mediolanum, Genua^\
Cohors Maurorum: recruitable in barracks in: Cirta, Carthago, Leptis Magna, Utika^\
Cohors Hispanorum: recruitable in barracks in: Augusta, Tarraco, Tolosa, Carthago Nova, Cordoba, Gades, Augusta Emerita^\
Cohors Tungrorum: recruitable in barracks in: Treverorum,  Colonia Agrippina, Tulisurquium, Flevum Tulifurdum^\
Cohors Gallorum: recruitable in barracks in: Lugdunum, Burdigala, Massalia, Lutetia^\
Cohors Batavorum: recruitable in barracks in: Mogantiacum, Argentorate, Rhetindovinum, Lugidunum, Ekolisma, Uburzis^\
Cohors Brittonum: recruitable in barracks in: Londinium, Deva, Castellum, Eboracum, Durnovaria^\
Cohors Thracum: recruitable in barracks in: Byzantium, Novae, Tomis, Nicopolis_ad_Haemun, Heraclea,  Viminacium^\
Cohors Petreorum (recruitable in barracks in: Petra, Masada, Tyrus, Hierosolyma, Miletus^\
Ala Batavorum: recruitable in barracks in: can be recruited where cohors batavorum can be recruited^\
Ala Commagenorum: recruitable in barracks in: Panticapaeum, Melitene, Trapezus, Nikomedia ^\
Ala Gallorum: recruitable in barracks in where cohors gallorum can be recruited^\
Ala Ituraeorum: recruitable in barracks in: Antiochia, Jotapata, Tarsus^\
Ala Auxiliarum: can be recruited in every barrack^\
Cohors Auxiliarum: can be recruited in every barrack^\
Ala Praetoriani: can be recruited in every barrack"),

("formations", "Advanced Formations", "The Complex Formations on the Battle Menu are:^^\
- RANKS with best troops up front^\
- SHIELD WALL, ranks with shields in front and longer weapons in back^\
- WEDGE with best troops up front^\
- SQUARE in no particular order^\
- NO FORMATION^^\
Even in the last case, the player can make formations up to four lines by ordering Stand Closer enough times.^^\
    Division Placement:^\
When ONE division is selected, the center of its front rank is placed at the spot indicated.^^\
When MANY divisions are selected, they are separated and spread out as if the player were standing at the spot indicated.^^\
One may memorize the placement of selected divisions relative to the player by pressing F2, F7. Default is infantry to the left, cavalry right, and ranged forward. Placement is overridden for any division the player chooses to personally head through the Formations Options menu.^^\
If the camp menu game option is set, divisions will rotate to face the enemy. Otherwise, they will maintain the facing that the player had when they were placed.^^\
    Tactical Controls:^\
Use the keyboard NUMBERS to select a division. Press 0 to select your entire force.^^\
Use F1-F4 to order selected divisions. Keep the F1 key down to place selected divisions. You may target an enemy division through this mechanism."),

("crafting_orders", "Crafting orders", "You can order any weapon, shields, armour, boots et cetera from weapon or armour merchants or you latifundia smith via a dialogue option.\
An ordered item will take some time till it is crafted and you will have to pay for the materials too. Once the item has finished talk with the merchant to get it.\
The merchant will send the finished item to you if you haven't collected it by yourself. Though this takes much longer than collecting it yourself (by talking with the respective merchant).^^\
Similarly you can import horses from any horse merchant or your latifundia breeder."),

("legio_1", "- Legio XXII Primigenia", "This legion has been disbanded."),#
("legio_2", "- Legio III Augusta", "This legion has been disbanded."),#
("legio_3", "- Legio V Alaudae", "This legion has been disbanded."),#
("legio_4", "- Legio XXI Rapax", "This legion has been disbanded."),#
("legio_5", "- Legio XX Valeria Victrix", "This legion has been disbanded."),#
("legio_6", "- Legio VI Victrix", "This legion has been disbanded."),#
("legio_7", "- Legio XI Claudia", "This legion has been disbanded."),#
("legio_8", "- Legio XIII Gemina", "This legion has been disbanded."),#
("legio_9", "- Legio V Macedonica", "This legion has been disbanded."),#
("legio_10", "- Legio VI Ferrata", "This legion has been disbanded."),#
("legio_11", "- Legio X Fretensis", "This legion has been disbanded."),#
("legio_12", "- Cohortes Praetoriae", "This legion has been disbanded."),

]#end of file