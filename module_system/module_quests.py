from header_quests import *

#from compiler import *
####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

quests = [
  # Note : This is defined as the first governer quest in module_constants.py:
  ("deliver_message", "Generic Quest: Deliver message to {s13}", qf_random_quest,
  "{!}{s9} asked you to take a message to {s13}. {s13} was at {s4} when you were given this quest."
  ),
  ("deliver_message_to_enemy_lord", "Generic Quest: Deliver message to {s13}", qf_random_quest,
  "{!}{s9} asked you to take a message to {s13} of {s15}. {s13} was at {s4} when you were given this quest."
  ),
  ("raise_troops", "Generic Quest: Obtain {reg1} {s14} as prisoners", qf_random_quest,
  "{!}{s9} asked you to obtain {reg1} {s14} as prisoners and bring them to him."
  ),
  ("escort_lady", "Generic Quest: Escort {s13} to {s14}", qf_random_quest,
  "{!}None"
  ),
  ## ("rescue_lady_under_siege", "Rescue {s3} from {s4}", qf_random_quest,
  ##  "{s1} asked you to rescue his {s7} {s3} from {s4} and return her back to him."
  ##  ),
  ## ("deliver_message_to_lover", "Deliver Message to {s3}", qf_random_quest,
  ##  "{s1} asked you to take a message to his lover {s3} at {s4}."
  ##  ),
  ## ("bring_prisoners_to_enemy", "Bring Prisoners to {s4}", qf_random_quest,
  ##  "{s1} asked you to bring {reg1} {s3} as prisoners to the guards at {s4}."
  ##  ),
  ## ("bring_reinforcements_to_siege", "Bring Reinforcements to the Siege of {s5}", qf_random_quest,
  ##  "{s1} asked you to bring {reg1} {s3} to {s4} at the siege of {s5}."
  ##  ),
  ## ("deliver_supply_to_center_under_siege", "Deliver Supplies to {s5}", qf_random_quest,
  ##  "TODO: Take {reg1} cartloads of supplies from constable {s3} and deliver them to constable {s4} at {s5}."
  ##  ),
  ("deal_with_bandits_at_lords_village", "Generic Quest: Save the village of {s15} from bandits", qf_random_quest,
  "{!}{s13} asked you to deal with the bandits who took refuge in his village of {s15} and then report back to him."
  ),
  ("collect_taxes", "Generic Quest: Collect taxes from {s3}", qf_random_quest,
  "{!}{s9} asked you to collect taxes from {s3}. He offered to leave you one-fifth of all the money you collect there."
  ),
  ("hunt_down_fugitive", "Generic Quest: Hunt down {s4}", qf_random_quest,
  "{!}{s9} asked you to hunt down the fugitive named {s4}. He is currently believed to be at {s3}."
  ),
  ## ("capture_messenger", "Capture {s3}", qf_random_quest,
  ##  "{s1} asked you to capture a {s3} and bring him back."
  ##  ),
  ## ("bring_back_deserters", "Bring {reg1} {s3}", qf_random_quest,
  ##  "{s1} asked you to bring {reg1} {s3}."
  ##  ),
  ("kill_local_merchant", "Generic Quest: Assassinate local merchant at {s3}", qf_random_quest,
  "{!}{s9} asked you to assassinate a local merchant at {s3}."
  ),
  ("bring_back_runaway_serfs", "Generic Quest: Bring back runaway slaves", qf_random_quest,
  "{!}{s9} asked you to bring back the three groups of runaway slaves back to {s2}. He said all three groups must be running away in the direction of {s3}."
  ),
  ("follow_spy", "Generic Quest: Follow the spy", qf_random_quest,
  "{!}{s11} asked you to follow the spy that will leave {s12}. You must be careful not to be seen by the spy during his travel, or else he may get suspicious and turn back. Once the spy meets with his accomplice, you are to ambush and capture them and bring them both back to {s11}."
  ),
  ("capture_enemy_hero", "Generic Quest: Capture a Lord from {s13}", qf_random_quest,
  "{!}TODO: {s11} asked you to capture a lord from {s13}."
  ),
  ("lend_companion", "Generic Quest: Lend your companion {s3} to {s9}", qf_random_quest,
  "{!}{s9} asked you to lend your companion {s3} to him for a week."
  ),
  ("collect_debt", "Generic Quest: Collect the debt {s3} owes to {s9}", qf_random_quest,
  "{!}{s9} asked you to collect the debt of {reg4} denars {s3} owes to him."
  ),
  ## ("capture_conspirators", "Capture Conspirators", qf_random_quest,
  ##  "TODO: {s1} asked you to capture all troops in {reg1} conspirator parties that plan to rebel against him and join {s3}."
  ##  ),
  ## ("defend_nobles_against_peasants", "Defend Nobles Against Peasants", qf_random_quest,
  ##  "TODO: {s1} asked you to defend {reg1} noble parties against peasants."l
  ##  ),
  ("incriminate_loyal_commander", "Generic Quest: Incriminate the loyal commander of {s13}, {s16}", qf_random_quest,
  "{!}None"
  ),
  # ("raid_caravan_to_start_war", "Raid {reg13} Caravans of {s13}", qf_random_quest,   #This is now a dynamic quest, integrated into the provocation system
  #  "None"
  #  ),
  ("meet_spy_in_enemy_town", "Generic Quest: Meet spy in {s13}", qf_random_quest,
  "{!}None"
  ),
  ("capture_prisoners", "Generic Quest: Bring {reg1} {s3} prisoners", qf_random_quest,
  "{!}{s9} wanted you to bring him {reg1} {s3} as prisoners."
  ),

  ## ("hunt_down_raiders", "Hunt Down Raiders",qf_random_quest,
  ##  "{s1} asked you to hunt down and punish the raiders that attacked a village near {s3} before they reach the safety of their base at {s4}."
  ##  ),

  ##################
  # Enemy Kingdom Lord quests
  ##################
  # Note : This is defined as the first enemy lord quest in module_constants.py:
  ("lend_surgeon", "Generic Quest: Lend your surgeon {s3} to {s1}", qf_random_quest,
  "{!}Lend your experienced surgeon {s3} to {s1}."
  ),

  ##################
  # Kingdom Army quests
  ##################
  # Note : This is defined as lord quests end in module_constants.py:
  ("follow_army", "Army Quest: Follow {s9}'s army", qf_random_quest,
  "{!}None"
  ),
  ("report_to_army", "Army Quest: Report to {s13}, the marshall", qf_random_quest,
  "{!}None"
  ),
  # Note : This is defined as the first army quest in module_constants.py:
  # maybe disable these army quests, except as volunteer quests that add to the capacity of the army
  ("deliver_cattle_to_army", "Army Quest: Deliver {reg3} heads of cattle to {s13}", qf_random_quest,
  "{!}None"
  ),
  ("join_siege_with_army", "Army Quest: Join the siege of {s14}", qf_random_quest,
  "{!}None"
  ),
  ("screen_army", "Army Quest: Screen the advance of {s13}'s Army", qf_random_quest,
  "{!}None"
  ),
  ("scout_waypoints", "Army Quest: Scout {s13}, {s14} and {s15}", qf_random_quest,
  "{!}None"
  ),


  ##################
  # Kingdom Lady quests
  ##################
  # Note : This is defined as the first kingdom lady quest in module_constants.py:
  #Rescue lord by replace will become a
  ("rescue_lord_by_replace", "Generic Quest: Rescue {s13} from {s14}", qf_random_quest,
  "{!}None"
  ),
  ("deliver_message_to_prisoner_lord", "Generic Quest: Deliver message to {s13} at {s14}", qf_random_quest,
  "{!}None"
  ),

  #Courtship quests
  ("duel_for_lady", "Generic Quest: Challenge {s13} to a duel", qf_random_quest,
  "{!}None"
  ),

  ("duel_courtship_rival", "Optinal Quest: Challenge {s13} to a duel", qf_random_quest,
  "{!}None"
  ),

  #Other duel quests
  ("duel_avenge_insult", "Generic Quest: Challenge {s13} to a duel", qf_random_quest,
  "{!}None"
  ),

  ##################
  # Mayor quests
  ##################
  # Note : This is defined as the first mayor quest in module_constants.py:
  ("move_cattle_herd", "Generic Quest: Move cattle herd to {s13}", qf_random_quest,
  "{!}Guildmaster of {s10} asked you to move a cattle herd to {s13}."
  ),
  ("escort_merchant_caravan", "Generic Quest: Escort merchant caravan to {s8}", qf_random_quest, #make this a non-random quest?
  "{!}Escort the merchant caravan to the town of {s8}."
  ),
  ("deliver_wine", "Generic Quest: Deliver {reg5} units of {s6} to {s4}", qf_random_quest,
  "{!}{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} in 7 days."
  ),
  ("troublesome_bandits", "Generic Quest: Hunt down troublesome bandits", qf_random_quest,
  "{!}{s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town."
  ),

  ("kidnapped_girl", "Generic Quest: Ransom girl from bandits", qf_random_quest,
  "{!}Guildmaster of {s4} gave you {reg12} denars to pay the ransom of a girl kidnapped by bandits.\
  You are to meet the bandits near {s3} and pay them the ransom fee.\
  After that you are to bring the girl back to {s4}."
  ),

  ("persuade_lords_to_make_peace", "Generic Quest: Make sure two Lords don't object to peace", qf_random_quest, #possibly deprecate., or change effects
  "{!}Guildmaster of {s4} promised you {reg12} denars if you can make sure that\
  {s12} and {s13} no longer pose a threat to a peace settlement between {s15} and {s14}.\
  In order to do that, you must either convince them or make sure they fall captive and remain so until a peace agreement is made."
  ),

  ("deal_with_looters", "Generic Quest: Deal with looters", qf_random_quest,
  "{!}The Guildmaster of {s4} has asked you to deal with several bands of looters around {s4}, and bring back any goods you recover."
  ),
  ("deal_with_night_bandits", "Generic Quest: Deal with night bandits", qf_random_quest,
  "{!}TODO: The Guildmaster of {s14} has asked you to deal with night bandits at {s14}."
  ),

  ("elusive_bandits", "Generic Quest: Elusive bandits", qf_random_quest,
  "{!}New quest."
  ),

  ############
  # Village Elder quests
  ############
  # Note : This is defined as the first village elder quest in module_constants.py:
  ("deliver_grain", "Generic Quest: Bring wheat to {s3}", qf_random_quest,
  "{!}The elder of the village of {s3} asked you to bring them {reg5} packs of wheat.."
  ),
  ("deliver_cattle", "Generic Quest: Deliver {reg5} heads of cattle to {s3}", qf_random_quest,
  "{!}The elder of the village of {s3} asked you to bring {reg5} heads of cattle."
  ),
  ("train_peasants_against_bandits", "Generic Quest: Train peasants of {s13}", qf_random_quest,
  "{!}None"
  ),
  ("water_dispute", "Generic Quest: Water dispute", qf_random_quest,
  "{!}None"
  ),
  ("dry_wells", "Generic Quest: Dry wells", qf_random_quest,
  "{!}None"
  ),
  ("need_tools", "Generic Quest: Villagers need tools", qf_random_quest,
  "{!}None"
  ),

  # Note : This is defined as the last village elder quest in module_constants.py:
  ("eliminate_bandits_infesting_village", "Generic Quest: Save the village of {s7} from bandits", qf_random_quest,
  "{!}A villager from {s7} begged you to save their village from the bandits that took refuge there."
  ),

  #Courtship and marriage quests begin here
  ("visit_lady", "Generic Quest: Visit Lady", qf_random_quest,
  "{!}None"
  ),
  ("formal_marriage_proposal", "Generic Quest: Formal marriage proposal", qf_random_quest,
  "{!}None"
  ),  #Make a formal proposal to a bride's father or brother
  ("obtain_liege_blessing", "Generic Quest: Formal marriage proposal", qf_random_quest,
  "{!}None"
  ),  #The equivalent of the above -- ask permission of a groom's liege. Is currently not used
  ("wed_betrothed", "Generic Quest: Wed your betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the father or guardian of the bride, object troop is the bride
  ("wed_betrothed_female", "Generic Quest: Wed your betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the spouse


  # Join Kingdom quest
  ("join_faction", "Special Quest: Join the {s1}", qf_random_quest, # has been removed
  "{!}Find {s1} and give him your oath of homage."
  ),

  # Rebel against Kingdom quest
  ("rebel_against_kingdom", "Help {s13} Claim the Throne of {s14}", qf_random_quest,
  "{!}None"
  ),

  #Political quests begin here
  ("consult_with_minister", "Generic Quest: Consult with minister", qf_random_quest, "{!}Consult your minister, {s11}, currently at {s12}"),

  ("organize_feast",        "Generic Quest: Organize feast", qf_random_quest,        "{!}Bring goods for a feast to your spouse {s11}, currently at {s12}"),
  ("resolve_dispute",       "Generic Quest: Resolve dispute", qf_random_quest,       "{!}Resolve the dispute between {s11} and {s12}"),
  ("offer_gift",            "Generic Quest: Procure gift", qf_random_quest,          "{!}Give {s10} a gift to provide to {reg4?her:his} {s11}, {s12}"),
  ("denounce_lord",         "Generic Quest: Denunciation", qf_random_quest,         "{!}Denounce {s11} in Public"),
  ("intrigue_against_lord", "Generic Quest: Scheme", qf_random_quest, "{!}Criticize {s11} in Private"),


  #Dynamic quests begin here
  #These quests are determined dynamically by external conditions -- bandits who have carried out a raid, an impending war, etc...
  ("track_down_bandits", "Generic Quest: Track down bandits", qf_random_quest,
  "{!}{s9} of {s4} asked you to track down {s6}, who attacked travellers on the roads near town."
  ), #this is a fairly simple quest for the early game to make the town guildmaster's description of the economy a little more relevant, and also to give the player a reason to talk to other neutral parties on the map

  ("track_down_provocateurs", "Generic Quest: Track down provocateurs", qf_random_quest,
  "{!}{s9} of {s4} asked you to track down a group of thugs, hired to create a border incident between {s5} and {s6}."
  ),
  ("retaliate_for_border_incident", "Generic Quest: Retaliate for a border incident", qf_random_quest,
  "{!}{s9} of {s4} asked you to defeat {s5} of the {s7} in battle, defusing tension in the {s8} to go to war."
  ), #perhaps replaces persuade_lords_to_make_peace

  ("raid_caravan_to_start_war", "Generic Quest: Attack a neutral caravan to provoke war", qf_random_quest,
  "{!}placeholder",
  ),

  ("cause_provocation", "Generic Quest: Provocations", qf_random_quest,
  "{!}placeholder",
  ), #replaces raid_caravan_to_start_war

  ("rescue_prisoner", "Generic Quest: Rescue or ransom a prisoner", qf_random_quest,
  "{!}placeholder"
  ), #possibly replaces rescue lord

  ("destroy_bandit_lair", "Generic Quest: Destroy bandit lair", qf_random_quest,
  "{!}{s9} of {s4} asked you to discover a {s6} and destroy it."
  ),

  ("raid_german_temple", "Generic Quest: Raid {s14}", qf_random_quest,
  "{s11} asked you to destroy the temple at {s14}, near {s34}."
  ),

  ("deliver_bribe", "Generic Quest: 'Gifts' for 'friends'", qf_random_quest,
  "{s11} asked you to deliver a gift of 10,000 denars to a senator in Roma."
  ),
  ("spy_on_spouse", "Generic Quest: Jealous husband", qf_random_quest,
  "{s11} asked you to spy on his spouse {s14}."
  ),

  ("vc_wounds", "Viking Conquest wound system.", 0, "{!}placeholder."),

  ### has to be changed for Otho/Vitellius choice
  ("blank_quest_2", "Main Story: Conquer Rome!", qf_random_quest,
  "Now you have the possibility to become Caesar. Conquer Roma, the eternal city! But civil war will await you. Hint: March to Rome and see what happens."
  ),

  ### has to be changed for Otho/Vitellius choice
  ("blank_quest_3", "Main Story: End the Civil War", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_4", "Generic Quest: Libelli (petitions)", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_5", "Main Story: Katabasis (Journey into the underworld)", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_6","Generic Quest: Capture and bring {reg5} women to {s3}", qf_random_quest,
  "The local leader of the village of {s3} asked you to bring {reg5} women to the village (as prisoners)."),

  ("blank_quest_7", "Generic Quest: Return runaway slave to {s3}", qf_random_quest,
  "The leader of the village of {s3} asked you to bring a runaway slave back to the village."
  ),

  ("blank_quest_8", "Special Quest: Worshippers of Chrestos", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_9", "Generic Quest: Bring {reg33} units of Mead to {s3}", qf_random_quest,
  "The priest at {s3} asked you to bring him {reg33} units of mead."
  ),

  ("blank_quest_10", "Generic Quest: Recover a {s13} stolen from {s9} of {s3}", qf_random_quest,
  "The {s9} of {s3} asked you to recover a {s13} stolen from him.^^Look Into:^{s10}"
  ),

  ("blank_quest_11", "Generic Quest: Bring {reg33} loads of {s33} to {s3}", qf_random_quest,
  "The {s9} of {s3} asked you to bring {reg33} loads of {s33} to him."
  ),

  ("blank_quest_12", "Generic Quest: Bring {reg33} Pallets of Timber to {s3}", qf_random_quest,
  "The abbot at {s3} asked you to bring him {reg33} pallets of timber."
  ),

  ("blank_quest_13", "Generic Quest: A Blast from the Past", 0, "{s11} asked you to deal with her 'ghost' ex-lover who is believed to be in {s33}."
  ),

  ("blank_quest_14", "Reveal Assassination Plot", 0, "Someone attempted to murder you. You can try to find out who wanted you dead by meeting the killers' contact in {s3}."
    ),

  ("blank_quest_15", "Reveal Assassination Plot",0, "The contact has given away the lord who ordered the assassination - it is {s9}. It's time to confront the lord directly. "
  ),

  ("blank_quest_16", "Generic Quest: Bring {reg25} {reg1?pieces:piece} of {s17} to {s11}", qf_random_quest,
  "{s11} asked you to bring her {reg25} {reg1?pieces:piece} of {s17}."),

  ("blank_quest_17", "Generic Quest: Bring foodstuffs to {s11}", qf_random_quest,
  "{s11} asked you to bring her two pieces of cheese and {reg25} {reg1?bottles:bottle} of wine."
  ),

  ("blank_quest_18", "Generic Quest: Deliver message to {s3}", qf_random_quest,  "{s11} asked you to take a message to her lover {s3}."
  ),

  ("blank_quest_19", "Main Story: Aut Caesar Aut Nihil", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_20", "Special Quest: Blossom in the desert", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_21", "Generic Quest: Corruption", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_22", "Special Quest: Conquest of Germania", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_23", "Special Quest: Conquest of Mesopotamia", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_24", "Special Quest: Conquest of Dacia", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_25", "Special Quest: Conquest of Britannia", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_26", "Optional Quest: Talk with {s30}", qf_random_quest,
  "{!}placeholder"
  ),

  ("blank_quest_27", "Optional Quest: Talk with {s31}", qf_random_quest,
  "{!}placeholder"
  ),

  ### this here are the start up quests
  ("collect_men", "Main Story: Recruit five men", 0,
  "{!}{s9} asked you to collect at least 5 more men before you move against the bandits threatening the townsmen. You can recruit soldiers from villages as well as town taverns. You can find {s9} at the tavern in {s4} when you have think you have enough men."
  ),

  ("learn_where_merchant_brother_is", "Main Story: Learn where the hostages are held.", 0,
  "{!}placeholder."
  ),

  ("save_relative_of_merchant", "Main Story: Attack the bandit lair", 0,
  "{!}placeholder."
  ),

  ("save_town_from_bandits", "Main Story: Bandit cartel", 0,
  "{!}placeholder."
  ),
  ### end start up quests

  ("conspiracy", "Special Quest: Conspiracy", qf_random_quest,
  "{!}placeholder"
  ),

  ("usurp_province", "Special Quest: Tyranny and despotism", qf_random_quest,
  "{!}placeholder"
  ),

  ("join_roman_army", "Main Story: Serve in the legion", qf_random_quest,
  "{!}placeholder"
  ),
  ("gain_renown", "Main Story: Become a rich landowner", qf_random_quest,
  "{!}placeholder"
  ),
  ("important_friends", "Main Story: The Secret of Kaeso Flavius", qf_random_quest,
  "{!}placeholder"
  ),

  ("slave_revolt", "Special Quest: The Slave Albus", qf_random_quest,
  "{!}placeholder"
  ),
  ("widow", "Special Quest: Tussit", qf_random_quest,
  "{!}placeholder"
  ),
  ("petrus", "Special Quest: Paulus the Christ", qf_random_quest,
  "{!}placeholder"
  ),
  ("town_trade", "Special Quest: A meeting", qf_random_quest,
  "{!}placeholder"
  ),
  ("town_trade_2", "Special Quest: The merchant Lucillus", qf_random_quest,
  "{!}placeholder"
  ),
  ("the_eagle", "Special Quest: The Eagle", qf_random_quest,
  "{!}placeholder"
  ),
  ("new_hope", "Main Story: A new hope", qf_random_quest,
  "{!}placeholder"
  ),
  ("grain_supply", "Senate Quest: Grain supply", qf_random_quest,
  "{!}placeholder"
  ),
  ("talk_with_the_emperor", "Senate Quest: Talk with the Princeps", qf_random_quest,
  "{!}placeholder"
  ),
  ("bribes_bribes", "Main Story: Bribes", qf_random_quest,
  "{!}placeholder"
  ),
  ("freelancing", "Special Quest: Serve an Empire", qf_random_quest,
  "{!}placeholder"
  ),
  ("thunder", "Special Quest: Parthian Thundergod", qf_random_quest,
  "{!}placeholder"
  ),

  ("avaritia", "Special Quest: Gang activities", qf_random_quest,
  "{!}placeholder"
  ),

  ("become_pharao", "Special Quest: Become Pharaoh", qf_random_quest,
  "{!}placeholder"
  ),

  ("governor_corruption", "Generic Quest: Corrupt Governor", qf_random_quest,
  "{!}placeholder"
  ),

  ("money_stinks", "Special Quest: Money doesn't stink", qf_random_quest,
  "{!}placeholder"
  ),
  ("pirates", "Special Quest: Fast ships", qf_random_quest,
  "{!}placeholder"
  ),
  ("philosopher", "Special Quest: The philosopher", qf_random_quest,
  "{!}placeholder"
  ),
  ("nero_special_quest", "Special Quest: Nero's wishes", qf_random_quest,
  "{!}placeholder"
  ),
  ("elephant_hunt", "Generic Quest: Dangerous Hunt", qf_random_quest,
  "{!}placeholder"
  ),
  ("gardens_of_pleasure", "Special Quest: Gardens of Pleasure", qf_random_quest,
  "{!}placeholder"
  ),
  ("amor_quest", "Special Quest: Te amo, tu me non amare", qf_random_quest,
  "{!}placeholder"
  ),
  ("wlodowiecus_adventure", "Special Quest: The Adventure of Wlodowiecus (I)", qf_random_quest,
  "{!}placeholder"
  ),
  ("wlodowiecus_adventure_2", "Special Quest: The Adventure of Wlodowiecus (II)", qf_random_quest,
  "{!}placeholder"
  ),
  ("wlodowiecus_adventure_3", "Special Quest: The Adventure of Wlodowiecus (III)", qf_random_quest,
  "{!}placeholder"
  ),
  ("bacchhus_quest", "Special Quest: Dionysus rege!", qf_random_quest,
  "{!}placeholder"
  ),
  ("hadrian_letter", "Special Quest: Lugian Forests", qf_random_quest,
  "{!}placeholder"
  ),
  ("arminius_sword", "Special Quest: Arminius' tomb", qf_random_quest,
  "{!}placeholder"
  ),
  ("nero_reborn", "Special Quest: Nero reborn", qf_random_quest,
  "{!}placeholder"
  ),
  ("elysium", "Special Quest: Elyisum", qf_random_quest,
  "{!}placeholder"
  ),
  ("olympic_games", "Special Quest: Olympic Games", qf_random_quest,
  "{!}placeholder"
  ),
  ("langobard_arrive", "Special Quest: The invasion of the Winnili", qf_random_quest,
  "{!}placeholder"
  ),
  ("investment", "Generic Quest: Investment Opportunity", qf_random_quest,
  "{!}placeholder"
  ),

  ("collect_requested_money", "Generic Quest: Collect the requested money", 0,
  "{!}placeholder."
  ),
  ("collect_requested_influence", "Generic Quest: Meet with friends", 0,
  "{!}placeholder."
  ),
  ("collect_requested_senate", "Generic Quest: Meet with senators", 0,
  "{!}placeholder."
  ),
  ("rags_to_riches", "Special Quest: A lightning from the past", 0,
  "{!}placeholder."
  ),
  ("poking_the_lion", "Main Story: Poke the lion", 0,
  "{!}placeholder."
  ),
  ("four_emperors", "Main Story: The four Caesars", 0,
  "{!}placeholder."
  ),
  ("player_treason", "Special Quest: Treason", 0,
  "{!}placeholder."
  ),
  ("neros_fate", "Special Quest: Fate of an artist", 0,
  "{!}placeholder."
  ),
  ("zarinaia", "Special Quest: Zarinaia, the golden one", 0,
  "{!}placeholder."
  ),
  ("quests_end", "Quests End", 0, "{!}."),
]
