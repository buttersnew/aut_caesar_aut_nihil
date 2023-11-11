#from compiler import *
####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
##diplomacy start+
from module_constants import DPLMC_DIPLOMACY_VERSION_STRING
##diplomacy end+

info_pages = [
("hoty_keys", " HOT KEYS", "Here is a list of all keys and where they are used:^\
^^SHIFT - KEY: ^^*) Player can right away start a conversation with any town merchant by pressing 'shift' while clicking on 'trade with the XY'. ^*) By pressing 'shift' while clicking on 'visit the Domus Augusti' player will spawn next to advisors. ^*) After the player has visited a Roman temple for the first time he can spawn right next to the priest by pressing shift while clicking on 'visit the temple of XY'. ^*) The administrator of the latifundium can be quickly accessed by pressing 'shift' while clicking on 'visit the villa'.\
^^ENTER - KEY: ^^*) During battle player can open strategic view.\
^^H - KEY:^^*) Allows you to call your horse during battle (if it is still alive) \
^^K - KEY: ^^*) During battle pressing K will start a shield taunt. ^*) While on worldmap, pressing K during freelancing allows player to access the daily missions menu.\
^^T - KEY: ^^*) By pressing T player will perform a warcry during battles. ^*) While entering the lords hall player will make a handkiss by pressing T.\
^^J - KEY: ^^*) Player can change the movement speed of troops during battles by pressing J ^*) Player's horse will start to sprint during horse races by pressing J\
^^Z - KEY: ^^*) Pressing Z allows player to crouch (For German keyboards it is the Y key). Though it can be changed under game options -> controls.\
^^^The keys for the death-camera can be changed under the Diplomacy preference menu."),
("q_and_q", " Important informations", "Battle field fortifications: ^As Roman you can fortify your camp. It requires a set of tools inside your inventory and an engineer skill higher than 5. Once fortified you can no longer move. It is also possible during sieges.\
^^Lending out money: Visit an argentarii (who can be found inside a scriptorium) to lend out money or to just store your money in a safe place. You can lend out a loans between 5,000 and 500,000 denars. The loan will expire after a week. Once it expires the money will be added TO THE NEXT budget report.\
 This can take a while. Depending on when you issued the loan and depending on when your next budget report will show it can take between one or two weeks until your receive the interests.\
 For your loan you have two options. Either you order the argentarius to reinvest the money again, or you order him to send you back all the money. In the first case,\
 you will only receive the interests of your loan and a new loan will be lend out right away after recieving the interests. In the later case you will receive all the money back. Sometimes the interests can be negative. That shall simulate the case\
 when the debtor is not able to repay the loan you offered him.\
^^Diplomacy feature: You can become part of a family. To do this you must talk with a lord, depending the character of the lord you must either be honorable, or dishonorable, \
famous, have a good relation or own a fief or wealth.^^\
You need at least 200 renown to be considered as a full citizen of Rome. With 200 renown you can: Enter the great hall of towns and fortresses and you must pay the punitive tax (Lex Julia et Papia).\
If you are Emperor or have a military rank in the Roman Army your renown won't go beyond: 450 if emperor, 200 if common military rank.^^\
If you own a fief and you are part of the Roman Empire you must pay taxes to the Emperor, taxrate depends on circumstances. (usually 20%)^\
If you are part of the Roman Army (not as mercenary!) you won't have to pay wages for your troops in your party. But you must still pay for garrisons.^^\
Be aware: after some years the great Jewish revolt will start (if not triggered by player)^^\
Player can convert to Judaism (at the great temple in Hierosolyma), this enables the following features: Player can fund Judean rebels at the great temple in Hierosolyma, player can start the Jewish revolt and fight for Judea: Only possible if player hasn't joined any other faction yet.^^\
You can usurp towns from other governors (=Lords) with bad reputation type (quarrelsome, selfrighteous, sadisitic (debauched), cunning): You need more than 25 relation with the town, at least 300 renown and must be in the same faction,\
then you will receive an event when you visit the town. Nero will only give you the town if you don't already own one, and if you have a higher relation with him than the old governor. If your attempt fail, you will gain a new chance after 50 days.^^\
You can become the lover of a married woman. Firstly you must improve your relation with her. Then, depending on your charisma, her personality and luck she may says yes to you.\
But if your relation with her becomes to low (beyond 10) then she will break with you. There is also some random chance that she breaks, because she finds someone more interesting.^\
If you have high enough relation (and a good persuasion skill) with a lady, she may tell you the latest rumor about a love affair. You can use this information to your advantage.^\
Your spouse can have a love affair too. If you think she has one, you can send one of your companions to spy her. \
Depending on the intelligence skill of the companion he may find out if she has a love affair or not. If she has a lover and your companion has found it out you can talk with her and divorce.^^\
As Emperor you should always watch your enemies in your own faction, if they grow too many, they may assassinate you.^^\
As Emperor you can imprison any person you want (town or village walkers and your generals/lords)^^\
If you have a prisoner tower in a town or fort, you can torture your enemies. Simply visit the prison and talk with the torturer.^^\
You can deposit money in Roman towns. Simply talk with the praefectus of the city, who can be found in the scriptorium.^^\
You can buy all Roman weapons, armors, helmets and shields from the merchant Gaius Marius, who can be found in the streets of Rome.^^\
There are some drinking 'mini games' ingame: You can toast with Lords during feasts and you can make a drinking competition with tavern shoppers. A high strength attribute is needed if you want to win.^^\
The players health can decrease over time (see characters report for information about your current status). You will become more unhealthy, if you get knocked down during battle, and due to various other stuff (drinking competitions for example).\
To increase your health visit the baths frequently.^^\
As Emperor, you must answer petitions regularly. If you don't want to do this, talk with your political advisor, who can be found in the Domus Augustus in Rome.^^\
The gold item can used to hire warbands from the Nabateans, Garmantians and Gaetulians, by talking with their respective kings.^^\
You can order your companions to establish permanent camps (option in the camp menu) and to create their own parties (by talking with them via the party screen):^\
The maximal amount of troops you can give depends on the following: base is 100 men + additional two men per charisma attribute and additional 10 men per leadership skill.\
You can also store items and prisoners in the camp. But be aware, the camp can be attacked by enemy parties and if it is destroyed all items and prisoners will be lost.^^\
You can get honorary titles if you ask Emperor Nero for a reward. You need high relation with him for this dialogue option to become available.^^\
Freelancing is only available for Roman legions, talk either with a legate commanding a legion directly or with a Praefectus Castrorum or Praefectus, who can be found in the scriptorium.^^\
For freelancing in the Praetorian guard you need a letter of recommendation, this you can obtain once you reached the rank of Optio, while freelancing in a normal legion.^^\
You can go hunting via the camp menu.^^\
Roman officers provide a skill bonus: High rank officers, like Vexilarius, Aquilifer, Primus Pilus and Tribunus provide a bonus to leadership skill.\
For each 100 men in your party you need two officers (centurio, signifer etc.), otherwise you will get a malus on tactics skill. The only non-Roman 'officer' is currently the hornman.\
The idea behind this is the following: Larger armies are more difficult to lead during battles. The orders you give must reach the soldiers. Officers and musicians can help with that.^^\
Sailors can be found as mercenaries in taverns of port towns. Each sailor in the party increases party speed on water by 1% up to a maximum of 40%. (Also sea raiders in your party will increase speed on water)^^\
Commander panel: With an army large than 40 men you have access to the commander panel before a battle starts. It allows you to make sacrifices to the gods (improves moral, depends on a dice role, is a good choice if you have a low oratory skill), \
give a speech (depending on your oratory, persuasion and leadership skill it is either a success or fail) or to send skirmishers to attack the enemy (success depends on your tactics skill).^^\
Currently the escape change for a hero after battle is: 37%. Note that this also effect the player."),
("names", "Families and Relations", "Every faction consists of lords, who have different relations with other lords.\
 This relations will have also effects on your actions in the game. An example: If you execute a Lord (or Lady) your relationship with all his family members, but also with all his friends will decrease.\
 On the other hand you may even gain relation with enemies of this Lord. Such a system is often used when the player stands before the decision to either support someone or not.\
 In general you can keep the following in mind: If you somehow harm someone (e.g. offending the Emperor in an event), his enemies will like you more, his friends and family members will like you less.\
 On the other hand, if you help someone, his enemies will like you less, while his friends and family members will like you more. Note also that the relations between Lords change during the campaign.\
 But there is something one should keep in mind: Lords with bad personalities, like quarrelsome, will most likely gain many enemies over time.\
 ^^Another note on families: The Roman Empire has the following major families: Sulpicius, Vitellius, Cornelius, Fabius, Salvius Otho, Flavius. One can recognize them via the names of the Lords and Ladies.\
 A Lord from the Flavius family usually names X Flavius, while a woman usually names Flavia Y, where X stands for a generic Roman male name and Y for a generic Roman female name.\
 This may helps you to recognize which Lords/Ladis belong together."),
("roman_empire", "Roman Empire", "Roman Administration:^\
 The Roman Empire is not a feudal state. It has a huge and complex imperial administration.\
 In this mod the Roman administration is represented by governors. Governors only command a little army, a 'bodyguard', which allows them to case bandits.\
 They rule and manage most of the Roman provinces and must pay a part of their income to the Emperor. the Emperor then distributes those funds to the Empire\
 (or buy some nice clothes or host parties etc.).^^\
 Roman military:^\
 The legions and Auxiliary troops fight the wars of Rome. Only a Auxiliary commander or a legatus legionis (commander of a legion) will join military campaigns.\
 There are 11 legions and the Praetorian guard. The Praetorian guard is the 'bodyguard' of the Emperor. The Praefect of the Praetorian guard has an important position. \
 He can decide who becomes Emperor and who not. In fact he could make any poor, smelly peasant Emperor of Rome.^^\
 Military Ranks:^\
 There are two ways for the player to join the Roman faction: Either through raising from a common soldier to a officer position or by bribing officials.\
 Here are all ranks listed, in parenthesis the respective ranks of the Praetorian guard are displayed:^\
 ^Soldier ranks:\
 ^Tiro  (Probatus), requirement: 100 progress points\
 ^Miles  (Immunes), requirement: 200 progress points\
 ^Low officer ranks:\
 ^Optio  (Optio), can command 30 men in battle, requirement: 300 progress points\
 ^Centurio  (Centurio), can command 60 men in battle,, requirement: 400 progress points\
 ^Centurio primi ordinis  (Centurio primi ordinis), can command 70 men in battle,, requirement: 500 progress points\
 ^Centurio primus pilus  (Centurio primus pilus), can command 80 men in battle,, requirement: 600 progress points\
 ^Tribunus laticlavius  (Tribunus urbanae), can command 90 men in battle,, requirement: 700 progress points\
 ^High officer ranks:\
 ^Tribunus militaris, minimum party limit of 100 soldiers (further adjusted by player leadership skill and marshal bonus), requirement: either ask any Roman lord 'I want to join the army of Rome as officer.' or work your way through the lower ranks.\
 ^Praefectus cohortis, minimum party limit of 200 soldiers (further adjusted by player leadership skill and marshal bonus), requirement: 300 renown, at least 10 relation with Emperor, level 10\
 ^Legatus Legionis, minimum party limit of 500 soldiers (further adjusted by player leadership skill and marshal bonus),, requirement: 450 renown, at least 25 relation with Emperor, level 20^^\
 How does promotion work?^\
 As soldier serving in one of the legions you will get an event which informs you about the promotion. As high-rank officer once the requirements are met there is a chance of 35% percent that you get promoted every three days. Alternatively you can also talk with Princeps Nero and ask him for promotion.^^\
  Becoming Emperor^\
 Also you, the player, have the possibility to become Emperor of Rome. You must simply control the city of Rome, then you can claim the title.\
^There is also another way, if you have important friends, like the Praefect of the Praetorian guard, you may get the possibility to take advantage of certain crises and kill\
 the Emperor. If you want to be Emperor of Rome, it is always a good idea to have the Praetorian guard on your side.^^\
 Cursus honorum and Honrary titles:^\
 The offices of the republic still exists during imperial time although they lost most of its influence and became mainly honorary titles. In the game, the titles are assigned by the Emperor (speak with your minister once you are Emperor to assign them).^\
 There are four different titles with different effects:^\
 1. Quaestor: renown wont go below 250, can start senate meetings, can steal taxes of Rome (talk with Praefectus in Rome, who can be found in the Scriptorium and say: 'The Emperor has send me to collect a special tax...', can be used once every week)^\
 2. Aedile: renown wont go below 300, can start senate meetings, can steal taxes, can host games in towns^\
 3. Consul: renown wont go below 350, can start senate meetings, can hold triumph march, can host games in towns^\
 4. Censor: renown wont go below 400, can start senate meetings, can steal imperial taxes (visit the senate and use: 'Inspect the imperial treasury.' high penalty if you are caught), can host games^^\
 Titles are awarded by the Emperor. The following ways to obtain a title are possible for the player:^\
 -) Player can get awarded a title, if an AI lord holding a title loses it. (AI lords will lose their title if their relation with Nero drops down. The Nero decides to revoke the title if he finds someone suitable to give the title. The new candidate must have high relation with Nero, high renown, low controversy)^\
 -) As a reward for special quests.^\
 -) By asking the Emperor for a reward.^\
 -) By bribing a high renown lord who has good relations with the Emperor.^\
"),
("army_stances", "Party stances and Ambushes", "Quite similar to games from the Total War series you can order your party a stance. There are three different stances:^^\
- Default: No effects^\
- Screening: Your party will march more careful and try to avoid ambushes (probability reduced by 50%), but this will decrease movement speed by 30%^\
- Forced march: Your party will march faster (30%), but the probability to get ambushed is higher (33% increase). Additionally, your party consumes 2-times as much food and moral will be reduced over time (as your men get tired from the forced march they need more to eat)^^\
Ambushes:^\
Ambushes can be performed by every non Roman faction once every two hours. But the probability is much higher for Germanic, British and Judean factions.^\
You can decrease ambush probability by increasing your tracking skill and by using the 'screening' stance. During ambushes, you will receive random causalities caused by traps \
which the enemy has laid. Additionally, on the battlefield you will encounter burning fire-balls, which can cause additional causalities."),
# ("christendom", "Christendom", "Early Christendom was quite similar to communism. The ideas that, after death, all people are treated equal, fell on fertile ground among the poor population of the Roman Empire.^\
# In contrast to the 'old' polytheist religions, Christendom was quite intolerant towards other Religions. This leaded to religious conflicts in every city, where Christendom dominated.^\
# That, and the fact, that Christendom does not accept the Imperial state cult, caused the Roman Emperors to pursue Christians and outlaw Christendom."),
##diplomacy start+
("dplmc_info", "Diplomacy Mod", "The Diplomacy mod adds some features to the game. Most of them are accessed via your minister and several new potential employees: a chamberlain, a constable, and a chancellor. \
You gain the opportunity to hire a chamberlain when you get your first village, a constable when you gain your first fortress, and a chancellor when you gain your first town.  \
If you dismiss one of your employees, you may be able to rehire them through a well-connected spouse or one of the travellers who frequent the taverns of Europe.^^\
Aside from these the mod has other features as well, which can be accessed from the Camp menu.^^This mod uses Diplomacy Version "+DPLMC_DIPLOMACY_VERSION_STRING+"."),
#SB : new parameters
("dplmc_autoloot", "Diplomacy Feature: Autoloot", "Autoloot settings are managed through the camp menu. It allows you to have your companions (named heroes, not ordinary soldiers) automatically select equipment from the loot after a battle.\
^^ In order for this feature to be enabled, one of the following must be true: someone in your party must have a Looting score of 2 or better, someone in your party must have an Inventory Management score of 3 or better, or the player {him/her}self must have an Inventory Management score of 2 or better.\
^^ The desired primary damage types (the higher of any swing/thrust damage) for melee and throwing weapons can be set up here. In addition, players can fine-tune weapon selection for two-handed/one-handed weapons, pikes, lances, and bladed polearms.^^This setting is currently:"),
("dplmc_autosell", "Diplomacy Feature: Autosell", "The Autosell feature allows you  to sell many items to a merchant all at once, instead of selling them one at a time. Autosell settings are managed through the Town menu, where you can specify which types of items you want to be able to sell (e.g. you might not want to automatically sell horses) and a price limit (for example, you might not want to automatically sell any items that cost more than 200 denars).^^ There are two primary ways to use autosell.  If you speak to a Horse Merchant, Armorer, or Weapon Merchant in a town, there is a conversation option to sell items of a particular type.  Also, when visiting a town there will be an option in the Marketplace section of the menu to automatically sell your items throughout the town.^^ For people who used Autosell in other mods, note that this sells from your own inventory, according to certain rules.  Items you have equipped will never be sold, and neither will the first three items in your inventory.  After that, autosell also skips anything that it thinks might be your personal equipment (since people often have more than one set).  Regardless of whether you have them equipped, it won't sell your best bow, crossbow, armor, helmet, boots, or gloves. If you have a bow you can use, it won't sell your best three packs of arrows, and if you have a crossbow it won't sell your best three packs of bolts. For shields, one-handed weapons, two-handed weapons, polearms, and horses, it won't sell your best or second-best item. Your best three throwing weapons also will not be sold. However, items that your character is unable to use are considered fair game."),
("dplmc_policy", "Diplomacy Feature: Policy", "Centralization/Decentralization:\
^+3 - very centralized. Tax inefficiency for the ruler is reduced by 15%, and increased by 15% to his vassals. Ruler's relations with his vassals should suffer a -3 hit every month. King's army get 30% percent increase, lords' armies get 9% decrease. Imperial administration: +1500 denars maintenance costs for towns, +150 for fortresses. Imperial tax: maximal tax rate is 90%\
^+2 - quite centralized. Tax inefficiency for the ruler is reduced by 10%,and increased by 10% to his vassals. Ruler's relations with his vassals fiefs should suffer a -2 hit every month. King's army get 20% percent increase, lords' armies get 6% decrease. Imperial administration: +1000 denars maintenance costs for towns, +100 for fortresses. Imperial tax: maximal tax rate is 60%\
^+1 - slightly centralized. Tax inefficiency for the ruler is reduced by 5%, and increased by 5% to his vassals. Ruler's relations with his vassals fiefs should suffer a -1 hit every month. King's army get 10% percent increase, lords' armies get 3% decrease. Imperial administration: +500 denars maintenance costs for towns, +50 for fortresses. Imperial tax: maximal tax rate is 50%\
^ 0 - neither decentralized nor centralized. Imperial administration: no additional costs. Imperial tax: maximal tax rate is 40%\
^-1 - slightly decentralized. Tax inefficiency for the ruler is increased by 5%. Ruler's relations with his vassals increase by +1 every month. King's army get 10% percent decrease, lords' armies get 3% increase. Imperial administration: -500 denars maintenance costs for towns, -50 for fortresses. Imperial tax: maximal tax rate is 30%\
^-2 - quite decentralized. Tax inefficiency for the ruler is increased by 10%. Ruler's relations with his vassals increase by +2 every month. King's army get 20% percent decrease, lords' armies get 6% increase. Imperial administration: -1000 denars maintenance costs for towns, -100 for fortresses. Imperial tax: maximal tax rate is 25%\
^-3 - very decentralized. Tax inefficiency for the ruler is increased by 15%. Ruler's relations with his vassals increase by +3 every month. King's army get 30% percent decrease, lords' armies get 9% increase. Imperial administration: -1500 denars maintenance costs for towns, -150 for fortresses. Imperial tax: maximal tax rate is 20%\
^^Noble rights vs Citizen rights:\
^+3 - very aristocratic.  Trade decreased by 15%. Kings relations with their lords increased by 3 every month. Vassals armies increased by 9%.\
^+2 - quite aristocratic. Trade decreased by 10%. Kings relations with their lords increased by 2 every month. Vassals armies increased by 6%.\
^+1 - somewhat aristocratic. Trade decreased by 5%. Kings relations with their lords increased by 1 every month. Vassals armies increased by 3%.\
^-1 - somewhat plutocratic. Trade increased by 10%. Kings relations with their lords decreased by 1 every month. Vassals armies decreased by 3%.\
^-2 - quite plutocratic. Trade increased by 15%. Kings relations with their lords decreased by 2 every month. Vassals armies decreased by 6%.\
^-3 - very plutocratic. Trade increased by 20%. Kings relations with their lords decreased by 3 every month. Vassals armies decreased by 9%.\
^^Slave laws:\
^+3 - almost all serfs.  Tax inefficiency decreased by 9% for both king and his vassals. Troops of the faction suffer a 6% strength malus in AI fights, kingdom army size increased by 6%.\
^+2 - mostly serfs.  Tax inefficiency decreased by 6% for both king and his vassals. Troops of the faction suffer a 4% strength malus in AI fights, kingdom army size increased by 4%.\
^+1 - usually serfs.  Tax inefficiency decreased by 3% for both king and his vassals. Troops of the faction suffer a 2% strength malus in AI fights, kingdom army size increased by 2%.\
^-1 - usually free subjects.  Tax inefficiency increased by 3% for both king and his vassals. Troops of the faction get a 2% strength bonus in AI fights, kingdom army size decreased by 2%.\
^-2 - mostly free subjects.  Tax inefficiency increased by 6% for both king and his vassals. Troops of the faction get a 4% strength bonus in AI fights, kingdom army size decreased by 4%.\
^-3 - all free subjects.  Tax inefficiency increased by 9% for both king and his vassals. Troops of the faction get a 6% strength bonus in AI fights, kingdom army size decreased by 6%.\
^^Quality/Quantity:\
^+3 - of legendary quality. AI strength of troops increased by 12%, lords' armies decreased by 12%.\
^+2 - of great quality. AI strength of troops increased by 8%, lords' armies decreased by 8%.\
^+1 - of good quality. AI strength of troops increased by 4%, lords' armies decreased by 4%.\
^-1 - of good quanity. AI strength of troops decreased by 4%, lords' armies increased by 4%.\
^-2 - of great quantity. AI strength of troops decreased by 8%, lords' armies increased by 8%.\
^-3 - of legendary quantity. AI strength of troops decreased by 12%, lords' armies increased by 12%."),
#SB : camera mode & disguise blurbs
("dplmc_deathcamera", "Diplomacy Feature: Battle Continuation", "Post-battle continuation allow you to watch the battle unfold after being knocked unconscious. Camera key bindings are available from the Diplomacy preference menus. In general numpad keys are used to rotate while movement keys are used to pan the camera. There are three camera modes available."),
("dplmc_disguise", "Diplomacy Feature: Player Disguise", "The player disguise system allows the player to take on the role of various commoners while attempting to sneak into a town. In addition to the original pilgrim robes, players are able to acquire new sets of equipment from merchants and their chamberlains.\
^ In Native, the chance to be caught depends on the number of men in the party. The new system calculates the chance to be caught based on the player's chosen role instead, but limits what the player can bring in and out of towns in terms of gold and items. The player's inventory will be merged after leaving the town."),

("dplmc_ai_changes", "Diplomacy Option: Campaign AI", "Low:^\
^- Center points for fief allocation are calculated (villages 1 / fortresses 2 / towns 3) instead of (villages 1 / fortresses 1 / towns 2).\
^- For the rescue prisoner and offer gift quests, the relatives that can be a target of the quest have been extended to include uncles and aunts and in-laws.\
^- Alterations to claimant quest calculation for center scores.\
^- When picking a new faction, lords are more likely to return to their original faction (except when that's the faction they're being exiled from), if the ordinary conditions for rejoining are met. A lord's decision may also be influenced by his relations with  other lords in the various factions, instead of just his relations with the faction leaders.\
^^Medium:^\
^- Some changes for lord relation gains/losses when fiefs are allocated.\
^- Kings overrule lords slightly less frequently on faction issues.\
^- In deciding who to support for a fief, minor parameter changes for certain personalities. Some lords will still give priority to fiefless lords or to the lord who conquered the center if they have a slightly negative relation (normally the cutoff is 0 for all personalities).\
^- When a lord can't find any good candidates for a fief under the normal rules, instead of automatically supporting himself he uses a weighted scoring scheme.\
^- In various places where average renown * 3/2 appears, an alternate calculation is sometimes used.\
^- Lords will perform additional upgrades and hiring of mercenaries in towns depending on personality.\
^^High:^\
^- The renown factor when an NPC lord or the player courts and NPC lady is adjusted by the prestige of the lady's guardian.\
^- When a faction has fiefless lords and no free fiefs left, under some circumstances the king will redistribute a village he owns.\
^- When villages are looted any volunteers that were in the village will be killed for both player and NPC.^^Current setting:"),

("dplmc_gold_changes", "Diplomacy Option: Economic AI", "Low:^\
^- Caravan trade benefits both the source and the destination.\
^- When the player surrenders, there is a chance his personal equipment will not be looted, based on who accepted the surrender and the difficulty setting.  (This is meant to address a gameplay issue. In the first 700 days or so, there is no possible benefit to surrendering rather than fighting to the last man.)  Also, a bug that made it possible for books etc. to be looted was corrected.\
^- AI caravans take into consideration distance when choosing their next destination and will be slightly more like to visit their own faction. This strategy is mixed with the Native one, so the trade pattern will differ but not wildly.\
^- Scale town merchant gold by prosperity (up to a maximum 40% change).\
^- Food prices increase in towns that have been under siege for at least 48 hours.\
^- In towns the trade penalty script has been tweaked to make it more efficient to sell goods to merchants specializing in them.\
^- Food has a chance of not spoiling depending on inventory management.\
^- Villages being raided now delays construction projects.\
^- Trading parties will drop off prisoners at walled centers.\
^^Medium:^\
^- Food consumption increases in towns as prosperity increases. Consumption also increases with garrison sizes.\
^- Lords' looting skill affects how much gold they take from the player when they defeat him.\
^- Lords' leadership skill modifies their troop wage costs the same way it does for the player.\
^- The player can lose gold when his fiefs are looted, like lords.\
^- The same way that lord party sizes increase as the player progresses, mercenary party sizes also increase to maintain their relevance. (The rate is the same as for lords: a 1.25% increase per level.)\
^- If the player has a kingdom of his own, his spouse will receive part of the bonus that ordinarily would be due a liege. The extent of this bonus depends on the number of fiefs the players holds. This bonus is non-cumulative with the marshall bonus.\
^- Attrition is inflicted on NPC-owned centers if they can't pay wages, but only above a certain threshold.\
^- Strangers cannot acquire enterprises (enforced at 1 instead of at 0, so you have to do something).\
^- Village prosperity has an impact on bandit infestation (chance of death spiral).\
^- Village elder now receives the gold when you buy cattle.\
^- Village farmer parties carry off extraneous items in the town elder's inventory to sell at market towns.\
^^High:^\
^- The total amount of weekly bonus gold awarded to kings in Europe remains constant: as kings go into exile, their bonuses are divided among the remaining kings.\
^- If any lords run a personal gold surplus after party wages, the extra is divided among the lord and his garrisons budgets (each fortress and town has its own pool of funds to pay for soldiers) on the basis of whether the lord is low on gold or any of his fortresses are. (If none are low on gold, the lord takes everything, like before).\
^- The honor loss from an offense depends in part on the player's honor at the time. The purer the reputation, the greater the effect of a single disgrace.\
^- Raiding change: village gold lost is removed from uncollected taxes before the balance (if any) is removed from the lord.\
^- Cash for prisoners.\
^- Allows canceling improvements (cash goes back to local economy, but relations suffer).^^Current setting:"),
##diplomacy end+
  # ("morale1", "Morale I", "Morale represents the ability and willingness of the troops in a party to summon up the endurance, quality, and discipline they need to face the stresses \
 # of battle and the march. It is not the same thing as the troops' happiness. Elite troops may grumble and whine about the hardships of campaigning -- but then stand together as one when the arrows \
 # start to fly. On the other hand, a commander who gives his men everything they want may find that they grow soft, and waiver before the enemy's charge.^^ Morale's greatest impact is on a party's \
 # behavior in battle, determining how aggressively troops engage the enemy, and how likely they are to break and run if they perceive the tide of battle turning against them.\
 # Morale also affects a party's march speed, as a less motivated party will move more slowly, as the men are not pushing themselves to their physical limit, and pause more frequently, as it waits \
 # for stragglers to catch up. Finally, a party with very low morale will start to suffer desertions.^^ Some factors that affect morale are intuitive. For example, a charismatic commander with a \
 # reputation for winning battles can infuse his or her men with a sense of confidence. Leaders who give their men well ample and varied supplies of food, and pay them on time, demonstrate that they \
 # care about their troops' welfare, and are less likely to lead them into disaster.^^ Other factors are less intuitive -- particularly those related to a party's sense of group cohesion. \
 # In a small tight-knit party, for example, men will often fight hard against daunting odds to avoid showing cowardice before their comrades-in-arms. A large party on the other hand may see its \
 # cohesion strained, as the commander has less time to supervise the men, listen to their grievances, and resolve their disputes. Frequent battles will strengthen the bonds between men, while long \
 # periods without combat will see the troops become bored and quarrelsome.^^ The morale report, accessibly by hitting the 'reports' button will give the player a sense of the factors affecting his \
 # or her men's morale."),

 ("morale2", "Morale Management", "The way the moral of the players party is calculated is different from native. There are several new events which effect moral, for instance: traveling through deserts or campaigning during winter negatively impacts moral. Base moral depends mainly on the party size: if you are near the maximum size you will get high penalties and need to entertain your troops regularly to keep moral high enough (e.g. follower women). Its reasonable to travel not always at full size, but only if needed during campaigns. \
^^You have several ways to improve the moral of your party: ^You can pay them extra wages.  \
 ^You can pay them mead or wine in taverns. ^ If you have Camp Followers, \
 Hunter Women, Camp Defenders, Soldier Wives, refugees or simple Peasant Women in you party, they will improve moral over time (the more you have the more moral will be improved, \
 the maximum is 10 moral points)^You can also improve your party moral with the help of priests\
 ^The Roman Army offers other ways to improve moral through disciplinary action, talk to your officers to get access to them.^Resting at towns and forts regularly also improves moral. If you don't rest regularly your party will accumulate a moral penalty. (this feature can be disabled in options)"),

 ("economy", "Changes to Economy", "Rents ^\
Rents are calculated in a much different way than native. Firstly, on a weekly average the wealth of a center is calculated (its \
not the same as prosperity rating). The wealth formula takes into account the various things a village or town or fortress produces. \
(this information can be found in the town or village or fortress menu)\
It also takes into account the season, i.e. villages with many acres of grain will generate more wealth during harvest. \
The wealth is then taxed, using a certain taxrate. The player can choose between 5 different tax rates: very low (20%), low (30%), \
normal (40%), high (50%), very high (60%) (like in diplomacy), the AI chooses also a taxrate, depending on how much money the AI has \
(the less the AI has, the more the AI will tax). \
High tax rates are usually problematic, and the player should avoid it if possible. (or riots can occur like in diplomacy) \
There are two different random events which can lower the rents and prosperity (and also inflict damage to the garrison) of a village/town/fortress: diseases and fires. \
(if you enact the garbage collection law and build a fire fighters building you can lower the damage those events have and \
lower the probability that they occur) \
Of course, if a village gets raided it won't generate any wealth nor any rents. \
Harvest time is in July, August and September.\
^^\
Imperial taxation^\
Every governor (so lords who dont command a legion nor a auxiliary unit) must pay some fraction of their wealth to the Emperor. \
The taxrate can be set by the player, if he is the Emperor. The AI emperor Nero wont change the taxrate (its 20%). \
If the player owns a village or fortress or town, he must pay taxes too (but note, that only the rents of the village or fortresses or towns you \
own are taxed, for enterprises or other sources of income you don't have to pay a tax). \
^^\
Empire maintenance^\
The emperor must pay empire maintenance. For every fortress, you must pay either 1100 denars (hard campaign difficulty), 1000 denars (medium campaign difficulty) or 900 denars (poor campaign difficulty), and for every town 5000 denars (hard campaign difficulty), 4000 denars (medium campaign difficulty) or 3000 denars (poor campaign difficulty), which are owned by \
the Empire. The lex julia et papia increases the costs by 1000 denars per town and the lex frumentaria by 500 denars per town \
and per fortress. The edictum securitas publicas also increases the maintenance costs by 400 denars per town and per fortress. The Lex Alimenta adds another 300 denars per walled center. Additionally, the centralization level effects maintenance costs too (see 'Diplomacy Feature: Policy')\
^^\
Tax inefficiency^\
At some point, tax  inefficiency will become the main reason why you have a negative income and there are ways to lower it. \
First of all, how is tax inefficiency calculated: \
Tax inefficiency only occurs, if you own more centers (if you are Emperor, all centers of your faction are taken into account, \
if you are a common lord, only the ones you really own) than a certain threshold. The threshold depends on campaign difficulty, \
your relation with your prime minister (roughly speaking higher relation, less tax loses), and if you have hired the additional \
tax collectors. It is possible to gain a certain percentage of lost taxes back (if you have a quaestor (=chamberlain) the percentage \
is shown in brackets in the weekly budget report). The percentage is effected by: You gain 10% points for having a quaestor or chamberlain, \
12% points for having the additional tax collectors and 3% points for having the census conducted. \
To sum up, if you want to lower tax inefficiency increase your minister relation (higher than 50 is optimal), higher a chamberlain, \
hire additional tax collectors and conduct a census (if you are emperor). \
^^\
Note, that lords may build buildings too, if they have enough funds. The construction time and costs are modified by: \
faction serfdom: the higher the faster it will be build, engineer skill of the town lord. Additionally, building time will be reduced by prisoners in the town. (this applies for AI lords and player) \
^^\
Note, that whenever a town or fortress is sacked, there is a probability of 60 percent that a building will be destroyed. \
Forums, Theatres, Triumphal arches, baths and barracks can't be destroyed at all. \
^^\
An additional way of income is through slaves: You can let your slaves work in villages you own. Each slave will generate between \
60 and 100 denars additional rents. If the village has iron or silver deposits, additional 40 denars will be added, if it has iron \
or silver mine building constructed, additional 40 denars will be added. To place your slaves in the mine, you must own the village, \
and you must construct a manor first. Then you can manage the prisoners and garrison. Place the slaves simply as prisoners \
in your village. You shouldn't add more than 100 slaves, otherwise, there is a certain probability that they escape and spawn \
as bandits next to your village. Also, if the village is raided, slaves can escape.^^\
The AI will sell prisoners from towns, fortresses and villages over time. The new money will be distributed between the lord and his fiefs."),

 # ("courtship", "Changes to courtship", "Additional to the native features, courtship got much more flavour now.^^\
 # There are now additional ways to conquer the heart of a lady: You can now bring her presents (jewellery, ivory or other treasures), do quests for her or simply flirt with her.\
 # If you have success depends mainly on how much attraction she feels towards you (which depends on your charisma skill) and her personality. (e.g. moralists are harder to conquer).\
 # Success in flirting depends on attraction, charisma and persuasion skill.\
 # "),

 # ("military_campaigns", "Military Campaigns", "When kingdoms and Empires in Europe go to war, their armies have two basic offensive options. They can try to attack villages and lay waste \
 # to the countryside, damaging their enemy's prestige and economy. Or, they can try to seize and hold fortresses or towns, taking territory This second option can involve long, bloody sieges, \
 # but will yield more decisive results.^^It is important to note that the realms of Europe do not field standing armies, which remain in the field as long as the ruler desires. Rather, \
 # European realms are protected by feudal levies comprised of the major nobles and their individual retinues.  Sometimes, these nobles launch their own private attacks into enemy territory, \
 # but the most decisive events will usually take place when the great hosts are assembled. The kingdom's marshal, a noble appointed by the king, will summon the host before the campaign and lead \
 # them out to battle. However, he should be careful not to keep them in the field too long. Otherwise, the host will begin to disintegrate, as the vassals drift off to pursue their own business, \
 # and the army will be vulnerable to a counter-attack.^^For this reason, the rhythm of wars in Europe often resemble the rhythm of a duel between two individual combatants. One side will gather \
 # its strength and seek to land a blow against the enemy's territory. If the marshal spends too little time gathering the vassals, he may not be able to do any real damage. If he spends too much \
 # time, then the campaign may end before it has even begun. A large realm will have an advantage over a smaller one, just as a brawny combatant has an edge over a smaller foe, but a realm's political \
 # cohesion can also be a factor, just as a fighter with great stamina can outlast her opponent. Sometimes, the armies of two realms will meet head on, resulting in a major battle in which both numbers \
 # and morale will decide the outcome.^^Kingdoms will have imperfect intelligence about their enemies. Attacking lords will need to frequently scout enemy territory to determine which fortresses may be \
 # vulnerable. An army defending its homeland will benefit from the alarms raised by fortresses and towns, which broadcast intelligence about enemy movements in the area. \
 # Such intelligence will be imprecise, however, particularly when it comes to numbers. A defending force which sets out to raise a siege or rescue a village may be able \
 # to overwhelm an unprepared attacker -- or it may miscalculate, and find that it is the one to be overwhelmed. Attackers, in turn, must be careful how far they advance into enemy territory, \
 # with aggressive marshals venturing further than cautious ones.^^Players will be expected to join in their faction's military campaign, either by joining the host, or by scouting ahead into \
 # enemy territory. Some players may find that their realm's marshal is too cautious, or too aggressive, for their tastes. In this case, they can intrigue with other lords to try to replace the marshal, \
 # or build support to become the marshal themselves.^^Most wars are of limited duration. A king who goes to war will, for the sake of honor, feel obligated to pursue the conflict \
 # for a short while. However, unless he is soundly beating his enemy. he may soon start looking for a way out of the conflict, lest he leave himself vulnerable to an attack by a third party. \
 # Europe's rulers are keenly aware that today's ally may be tomorrow's enemy, and vice versa."),


("follower_party", "Follower party", "For creating a follower party you need to have at least 60 men in your main party, have 10 non-wounded women and 2,500 denars for hiring a physician and mules.\
 Once created, the follower party will automatically disband if you either get defeated or your party size goes below 40 men.^^\
 You can manage the follower party over the camp menu. There you can add more women to the party, store items on the mules or use the physician to treat major wounds. You can also add sailors to the follower party which will grant you a speed bonus when on water. But the troops in the follower party wont fight during battles. You can also manually disband the follower party.^^\
 Other advantages of the follower party:^^\
 Having soldier wives in your follower party improves your surgery skill (up to 3)^\
 Having camp followers, hunter women, camp defender or soldier wives in your follower party improves your wound treatment skill (up to 3)^\
 For women in your follower party you gain a moral bonus.^\
 Women in your follower party won't fight on the battlefield and you don't have to pay wages.^^\
 As a disadvantage, a follower party will significantly slow down your army."),

("aor", " AOR Recruitment", "All Auxiliary cohorts are listed here:^^\
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

("companions", " Companions", "Companions do no longer spawn randomly in taverns. They all have fixed locations or quests which enable them. Here is a complete list of all companions:^^"
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


# ("battle_speed", "Special Battle Features", "Once all enemies are routing, the battle won't automatically end to give the player a chance to kill routing soldiers. But by pressing the tab key you still can end the battle successfully.^^\
# Battle speed: You can change the speed of troops during battle by pressing the 'J' key. \
# ^^Shield taunt: You can make a shield taunt by pressing the 'K' key.^^\
# Battlecry: You can perform a battlecry by pressing the 'T' key. The battle cry improves moral of your troops. (You and your troops will perform an animation. This animation can be displayed in mod options)^^\
# Heroes (e.g. companions, generals/lords) encourage ally troops during battle whenever an ally is killed or wounded.\
# ^^Using horns improve moral during battle. (Either if player or AI uses them.)^^If a hero falls, allies will gain a moral hit. (For kings the penalty is more severe.)"),
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

# ("roman_military", "Roman Army", "Vigiles:^\
# Vigiles were not a proper military unit: they were the policemen and firefighters of Rome, and since Rome is a gigantic metropolis made of wood and desperate proletarians, it requires a sizeable force of vigiles to ensure that crime and fires are kept at a manageable level. \
# Established by Augustus, they quickly grew from 600 to 7,000, and Septimius Severus integrated them into the army: in times of danger these men can act as a lightly armed militia force, \
# thanks to the training they received during their years of service in the Caput Mundi, where a small spark can burn a city, and a riot at the Coloseum can turn into a battle with hundreds of victims \
# (without counting the hundreds of gladiators already dead before the riot started).\
# ^^Legionarii:^\
# The military reforms of Gaius Marius in 104BC transformed the Roman army into a professional fighting force. Recruits were no longer required \
# to own land in order to be soldiers: Roman citizenship was enough. Without farms to return to, men were willing to make the army their career, \
# fighting lengthy campaigns in return for the pay, glory and retirement benefits. The Legions were equipped at the expense of the state, and each \
# man carried a pilum, a gladius and a large shield, emblazoned with their Legion's insignia. Under Marius men were expected to carry their own \
# equipment, removing the need for large baggage trains manned by non-combatants. \
# Unfortunately for the men this meant that they were carrying kit that weighed around 45 kilos, earning them the nickname 'Marius' mules'.\
# ^^Praetorianii:^\
# The word 'praetorian' comes from the elite guards of the Praetor, the commanding general. Founded in the 6th century BC, \
# the cohors praetoria consisted of the hand-picked infantry or cavalry who guarded their general and his command tent. \
# At first, they were recruited exclusively from among Roman citizens, but later other Latin peoples were allowed to join. The \
# praetorians enjoyed prestigious status in the Roman army and, when Augustus came to power, they were the only soldiers allowed \
# inside Rome. Augustus anticipated that they could be used politically as well as militarily, something of a gamble for the new \
# Emperor, as he was keen to assert the Republican nature of his regime. Barracked just outside Rome, the praetorians were charged \
# with keeping order during all public events. Later, as the Imperial bodyguard, they served in military campaigns only when the Emperor \
# himself was present. \
# This happened frequently as later Emperors emerged from the ranks of the army during the 1st century AD.\
# ^^Milites Tungrorum:^\
# Fierce Germanic soldiers from the Rhine delta offer Rome superior medium cavalry.\
# ^^Milites Batavorum:^\
# The Batavi are a Germanic tribe living around Rhine delta. They supply Rome with excellent soldiers.\
# ^^Ballistarii:^\
# These troops use small ballistae, which fire bolts that can pass through a man.\
# ^^Auxilia Sagittarii:^\
# Many local peasants can use a bow. Rome gives them proper training and equipment to obtain decent archers.\
# ^^Auxilia Sagittarii Syrorum:\
# ^Citizens of the rich province of Syria (mainly Antiochia) have a long tradition of archery, \
# protecting their capital from surrounding nomads that might try to take their wealth.\
# ^^Auxilia Funditores:\
# ^Those slingers are recruited among the shepherds of the Balearic Islands, which train with a sling from childhood, \
# and are some of the most deadly slingers in the world."),

("latifundium", "Latifunidum", "In the game you can buy land next to the village. Talk with the local leader. You need to have more than 10 relation with the owning faction and at least 250 renown.^^\
The land you buy will only have one building on it: a grain field.\
There are buildings which will only produce rents during harvest. Harvest is during Julius, Augustus and September.\
Those buildings are: grain fields, vineyards, fruit gardens and olive groves. But you can build production sides which will use the goods produced, those are:^^\
-bakery (needs the grain field, when build, the grain field no longer gives you money during harvest, as the grain will be used for the bakery, but the bakery will produce \
during all months money, additionally, the total yearly income is more than the total yearly income of the grain field),^\
-winepress (needs vineyard, works like the bakery)^\
-oilpress (needs olive grove, works like the bakery)^^\
There are other buildings which will either add rents or increase the efficiency of the productions.^^\
Another thing you must consider is your slave population: You need slaves to work on certain buildings and if you don't have enough the efficiency will be lowered. If you have more slaves than needed the efficiency will be increased (every 5 slaves over the limit will make a difference)^\
You can place 100 slaves to your estate, but you can increase this number if you build a barracks building. Then you can add 200 slaves.\
^The slave population can grow, but only if you build a wall around your estate, and/or if you build barracks for guards.\
^^You can also change how your slaves are treated and if manumission happen. The harsher you treat them, the more money you get, but your reputation will decrease. But if you treat them too harsh, and if you allow manumissions to happen very frequently, your slave population will decrease. \
(Since, once the slaves are free, they will move to another place.)^Also note: The way you treat your slaves will also effect the slaves working in your villages! \
You can also change the slave treatment by taking with a local leader of a village you own, if you have a manor build there."),

("roman_society", "Roman Society", "The status of a Roman was established by:^\
Ancestry: patrician or plebeian^\
Census: rank based on wealth and political privilege, with the senatorial and equestrian ranks elevated above the ordinary citizen^\
Attainment of honors: the novus homo or self-made man established his family as nobilis (noble) and thus there were noble plebeians^\
citizenship: of which there were grades with varying rights and privileges.^^\
In the game this is mostly simulated by renown. If you reach a certain level of renown you are considered as citizen of the Roman Empire."),

("custom_player_legion", "Custom Player Legion", "You can found your own legion and equip it with Roman weapons and armours.^\
To do that, you must either have the rank of a legatus legionis, or be Emperor of Rome. Then, visit a barrack in a town or fortress you own and talk with the praetor. He will demand \
125000 denars. When you have paid you can equip your new troops in the courtyard, by talking with them. You can always change their equipment by talking to the soldiers from the party screen. Finally, \
you must choose a name for your legion. Now you can recruit your own legion in all your towns or fortresses with a barrack building constructed."),  #copied from str_tactical_controls
("tryphe", "Tryphe", "Tryphe is a concept that drew attention and severe criticism in Roman antiquity when it became a significant factor in the reign of the Ptolemaic dynasty. \
Classical authors such as Aeshines and Plutarch condemned the tryphe of Romans such as Crassus and Lucullus, which included lavish dinner parties and ostentatious buildings. But there was more to \
Ptolemaic tryphe than dissipative excess, which after all can be pursued in residential or geographical seclusion, and for purely private purposes. It was a component of a calculated political strategy, \
in that it deployed not just conspicuous consumption but \
also conspicuous magnificence, beneficence and feminine delicacy, as a self-reinforcing cluster of signal \
propaganda concepts in the Ptolemaic dynasty.^^\
In game, lords will spend a certain fraction of their wealth to various things, e.g. his court, his family etc. \
The more they spend, the more their renown increases."),
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
 CS - Corsica et Sardinia"),
 ("mythology", "Gods and Religion", "The player can worship different gods. For this, player must talk with a priest of the respective god and vow to worship the god.\
 A list of all gods and where to find their priests is below. Once the player worships a god, he can pray under the camp menu. For polytheistic gods, the player must fight against ancient heroes.\
 For Christus and YHWH, the reputation of the player is considered, both demand high reputation. If the player succeeds in the challenge, he gains artifacts or improves his attribute points.^\
 Worshiping Christus and YHWH offers additional unique features: As Christian, the player can always visit the undergroud chapel in Rome via the 'visit the sights of Rome' option and pray there.\
 Being Christian also allows you to visit Golgotha in Hierosolyma. As a Jew, the player can fund Judean rebels in the temple of Hierosolyma and even start the Jewish revolt if he is powerful enough.^^\
 Temples can be build at towns and your latifundium. You can consecrate the temple to a god of your choice. Non-Roman gods are only available if the player worships them.\
 ^^The mod features the following deities to worship:\
 ^^\
 ^Baduhenna: Germanic goddess, can be worshiped at Baduhenna sanctuary, sacrifices at her temple can improve strength attribute\
 ^Dunraz: Germanic god, can be worshiped at Dunraz sanctuary, sacrifices at his temple can improve charisma attribute\
 ^Frijo: Germanic goddess, can be worshiped at Frijo sanctuary, sacrifices at her temple can improve intelligence attribute\
 ^Alcis: Germanic gods, can be worshiped at Sleza, sacrifices at their temple can improve agility attribute\
 ^Mars: Roman god, can be worshiped at Rome, sacrifices at his temple can improve strength attribute\
 ^Vesta: Roman goddess, can be worshiped at Rome, sacrifices at her temple can improve ironflesh skill\
 ^Saturn: Roman god, can be worshiped at Rome, sacrifices at his temple can improve intelligence attribute\
 ^Aphrodite: Roman god, can be worshiped at Rome, sacrifices at her temple can improve players health\
 ^Jupiter: Roman god, can be worshiped at Rome, sacrifices at his temple can improve charisma attribute\
 ^Castor et Pollux: Roman gods, can be worshiped at Roma, sacrifices at their temple can improve agility attribute\
 ^Christus: the god of the Christians, no sacrifices possible, instead the player can pray together with a priest, which can heal your whole party. Converting to Christianity is possible after the fire of Rome has happened (under camp menu -> take an action), or by talking with Memercius at the underground chapel in Roma.\
 ^YHWH: god of the Jews, can be worshiped at Hierosolyma, sacrifices at his temple can either improve intelligence, charisma, agility or strength.\
 ^^Other effects of worshiping a god:^\
 Before the battle starts, there is a random chance that the god helps the player in the fight either, by healing the player, increasing the strength of the player, increasing the moral of the player troops.\
 ^^A side note on monotheism:^\
 Religion is portrayed from a polytheistic point of view.\
 Thus being a Christ or being a Jew is more related to worshiping the Christian god (Christus) or the Jewish god (YHWH).\
 From a modern point of view this may be wrong, but from the point of view of a polytheist it is the natural way.^^\
 Other holy sides:^\
 In Delphi, the player can question the oracle. In Olympia, the player can visit the great statue of Zeus. At Stonehenge, the player can make sacrifices to the Celtic gods."),
 ("crafting_orders", "Crafting orders", "You can order any weapon, shields, armour, boots et cetera from weapon or armour merchants or you latifundia smith via a dialogue option.\
 An ordered item will take some time till it is crafted and you will have to pay for the materials too. Once the item has finished talk with the merchant to get it.\
 The merchant will send the finished item to you if you haven't collected it by yourself. Though this takes much longer than collecting it yourself (by talking with the respective merchant).^^\
 Similarly you can import horses from any horse merchant or your latifundia breeder."),
 ]