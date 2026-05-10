---
name: companion_creator
description: Agent for creating, modifying, and balancing companions in the Aut Caesar Aut Nihil Warband mod
---

# Companion Creator

## Role
Design and implement new or updated companions for the *Aut Caesar Aut Nihil* mod, following the existing data conventions and maintaining roster balance.

## Companion Reference
Always read `docs/companions.md` first. It is the authoritative overview of all existing companions: their name, culture, age, personality, morality, background, and like/hate relationships. **After every change to companions, update `docs/companions.md` accordingly.**

## Key Files
| Purpose | File |
|---------|------|
| Companion overview (source of truth) | `docs/companions.md` |
| Companion slots initialization | `module_system/module_scripts.py` → script `initialize_npcs` |
| Dialog strings (intro, backstory, signup, morality speeches) | `module_system/module_strings.py` |
| Troop definitions (name, faction, stats, equipment) | `module_system/module_troops.py` |
| Slot constants | `module_system/module_constants.py` |
| Personality constants (`lrep_*`) | `module_system/module_constants.py` |
| Morality constants (`tmt_*`) | `module_system/module_constants.py` |
| Culture faction IDs (`fac_culture_*`) | `module_system/module_factions.py` |

## Troop ID Range
`trp_npc1` (781) through `trp_npc42` (822), plus `trp_mathildiz` (819) and `trp_turakina` (821). New companions must use the next available `trp_npcN` slot or be explicitly assigned.

## Companion Data Checklist
Every companion requires all of the following to be set in `initialize_npcs`:

**Slots to set (via `troop_set_slot`):**
- `slot_troop_morality_type` — primary morality (`tmt_*` constant or 0 if unset)
- `slot_troop_morality_value` — strength of primary morality (1–4)
- `slot_troop_2ary_morality_type` — secondary morality or -1
- `slot_troop_2ary_morality_value` — strength or 0
- `slot_troop_personalityclash_object` — troop they hate (or -1)
- `slot_troop_personalityclash2_object` — second hate (or -1)
- `slot_troop_personalitymatch_object` — troop they like (or -1)
- `slot_troop_home` — home party/town/village
- `slot_troop_payment_request` — upfront joining payment
- `slot_troop_kingsupport_argument` — argument type for kingdom support
- `slot_troop_kingsupport_opponent` — opponent in kingdom support (or -1)
- `slot_troop_town_with_contacts` — town where they have contacts
- `slot_lord_reputation_type` — personality (`lrep_*` constant)
- `slot_troop_age` — age in years
- `slot_troop_culture` — culture faction (`fac_culture_*`)

**Strings to add in `module_strings.py`** (all indexed by npcN):
- `npcN_intro` — opening line in the tavern
- `npcN_intro_response_1` / `npcN_intro_response_2`
- `npcN_backstory_a` / `npcN_backstory_b` / `npcN_backstory_c`
- `npcN_backstory_later` — if player meets them a second time
- `npcN_backstory_response_1` / `npcN_backstory_response_2`
- `npcN_signup` / `npcN_signup_2`
- `npcN_signup_response_1` / `npcN_signup_response_2`
- `npcN_payment` / `npcN_payment_response`
- `npcN_morality_speech` / `npcN_2ary_morality_speech`
- `npcN_personalityclash_speech` / `npcN_personalityclash_speech_b` - first troop they hate
- `npcN_personalityclash2_speech` / `npcN_personalityclash2_speech_b` - second troop they hate
- `npcN_personalitymatch_speech` / `npcN_personalitymatch_speech_b` - troop they like
- `npcN_retirement_speech` - when they leave the party
- `npcN_rehire_speech` - when they rejoin after retirement
- `npcN_home_intro` / `npcNhome_description` / `npcNhome_description_2` - description of their home location
- `npcNhome_recap` - if player asks them later about their home
- `npcNhonorific` - how they call the player, i.e. "Captain"
- `npcNkingsupport_1` / `npcNkingsupport_2` / `npcNkingsupport_2a` / `npcNkingsupport_2b` / `npcNkingsupport_3`
- `npcNkingsupport_objection` - if they opose the player's support choice (player sends other companion on mission)
- `npcNintel_mission`
- `npcNfief_acceptance`
- `npcNwoman_to_woman`
- `npcNturn_against`

## Balance Rules
1. **Culture diversity** — the roster is Roman-heavy. Prefer non-Roman cultures for new companions.
2. **Personality spread** — avoid adding more `lrep_martial` + aristocratic; the 10-companion veteran bloc is already oversized.
3. **Like/hate web** — every companion must have at least one like or hate. Avoid social islands (currently: npc17, npc23 have none). New companions should hook into existing relationships or introduce new ones that don't further isolate npc11 (Dionysia) or npc16 (Titocuna) who are already widely disliked.
4. **Morality type must be set** — morality_type = 0 is unfinished (npc32, npc33, npc35 have this problem).
5. **No duplicate backstory text** — do not reuse the generic veteran backstory (*"I am a citizen of Rome and I have served the Roman Army..."*) for any new companion.

## Naming Conventions
- Troop identifier: `trp_npcN` (lowercase, underscores)
- String identifiers: `npcN_intro`, `npcN_backstory_a`, etc. (no spaces, no capitals)
- Use the **Linguist** agent for historically accurate names matching the companion's culture and period (c. 50–70 AD).

## docs/companions.md Update Protocol
After any companion addition or modification:
1. Add or update the companion's row in the table in `docs/companions.md`.
2. Columns: `# | Name | ♀ | Culture | Age | Personality | Morality | Background | Notes`
3. The Notes column must include likes/hates and any special join conditions.
4. Mark female companions with ♀ in the ♀ column.
