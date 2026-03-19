# Troop Classes and Equipment

Source:
- `module_system/module_troops.py`
- `module_system/module_items.py`
- `module_system/module_factions.py`

Scope and inference rules:
- Only troops assigned to `fac_culture_*` factions are included.
- Heroes, civilians, followers, slaves, guards, officers, standards, hornmen, looters, bandits, and rebels are excluded.
- Troop classes are inferred from troop ids, troop names, mounted state, and whether the troop inventory includes bows or thrown weapons.
- If a troop id or troop name already says `light`, `medium`, `heavy`, or `cataphract`/`kataphraktos`, that explicit label stays in that file even for `exp` or `vet` variants.
- If a troop has no explicit weight label, `exp` and `vet` variants are used as heavier follow-up tiers, with level used as a fallback.
- Equipment is shown as normalized item ids. Numeric variant suffixes are collapsed, so `celtic_mail_noble_1` and `celtic_mail_noble_2` are both listed as `celtic_mail_noble`.
- Each troop file groups entries by culture and lists equipment as categorized item-id summaries.

Melee troops:
- [01_light_infantry.md](01_light_infantry.md) - Light Infantry (43 troops)
- [02_medium_infantry.md](02_medium_infantry.md) - Medium Infantry (42 troops)
- [03_heavy_infantry.md](03_heavy_infantry.md) - Heavy Infantry (70 troops)
- [04_light_cavalry.md](04_light_cavalry.md) - Light Cavalry (6 troops)
- [05_medium_cavalry.md](05_medium_cavalry.md) - Medium Cavalry (14 troops)
- [06_heavy_cavalry.md](06_heavy_cavalry.md) - Heavy Cavalry (20 troops)
- [07_super_heavy_cavalry.md](07_super_heavy_cavalry.md) - Super Heavy Cavalry (13 troops)

Missile troops:
- [08_light_skirmishers.md](08_light_skirmishers.md) - Light Skirmishers (12 troops)
- [09_medium_skirmishers.md](09_medium_skirmishers.md) - Medium Skirmishers (21 troops)
- [10_light_archers.md](10_light_archers.md) - Light Archers (14 troops)
- [11_medium_archers.md](11_medium_archers.md) - Medium Archers (19 troops)
- [12_heavy_archers.md](12_heavy_archers.md) - Heavy Archers (17 troops)
- [13_light_horse_archer.md](13_light_horse_archer.md) - Light Horse Archer (4 troops)
- [14_medium_horse_archers.md](14_medium_horse_archers.md) - Medium Horse Archers (14 troops)
- [15_heavy_horse_archers.md](15_heavy_horse_archers.md) - Heavy Horse Archers (14 troops)
- [16_light_skirmisher_cavalry.md](16_light_skirmisher_cavalry.md) - Light Skirmisher Cavalry (2 troops)
- [17_medium_skirmisher_cavalry.md](17_medium_skirmisher_cavalry.md) - Medium Skirmisher Cavalry (8 troops)
- [18_heavy_skirmisher_cavalry.md](18_heavy_skirmisher_cavalry.md) - Heavy Skirmisher Cavalry (5 troops)

Overview:
- [19_troop_class_cultural_summary.md](19_troop_class_cultural_summary.md) - Human-readable class summary by culture, role, and named equipment
