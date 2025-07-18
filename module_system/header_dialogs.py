###################################################
# header_dialogs.py
# This file contains declarations for dialogs
# DO NOT EDIT THIS FILE!
###################################################

speaker_pos = 0
ipt_token_pos = 1
sentence_conditions_pos = 2
text_pos = 3
opt_token_pos = 4
sentence_consequences_pos = 5


anyone      = 0x00000fff
repeat_for_factions = 0x00001000
repeat_for_parties  = 0x00002000
repeat_for_troops   = 0x00003000
repeat_for_100      = 0x00004000
repeat_for_1000     = 0x00005000

plyr                = 0x00010000
party_tpl           = 0x00020000
auto_proceed        = 0x00040000
multi_line          = 0x00080000

suf_other_bits   = 20

def other(other_troop_id): # max troop-id shouldnt be higher than 2047 because of this
  return other_troop_id << suf_other_bits
