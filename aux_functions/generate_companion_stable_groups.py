import os
import re

# ==========================================
# 1. DATA LOADING FROM MODULE SYSTEM
# ==========================================
def load_companion_data():
    """
    Parse companion names and relationships directly from:
      - module_system/module_troops.py  (name map)
      - module_system/module_scripts.py (personality/hate slots)

    Returns the same (companions_list, conflicts_dict) as the old
    parse_data(raw_data) helper, so the solver below is unchanged.
    """
    module_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'module_system'
    )

    # --- 1. Build trp_id -> display_name map from module_troops.py ---
    # Match the first two fields of every troop list entry:
    #   ["npc1", "Pravare Ytarim", ...] or ["mathildiz", "Mathildiz", ...]
    name_map = {}  # e.g. "trp_npc1" -> "Pravare Ytarim"
    troops_path = os.path.join(module_dir, 'module_troops.py')
    with open(troops_path, encoding='utf-8') as f:
        troops_text = f.read()
    for m in re.finditer(r'\[\s*"([^"]+)"\s*,\s*"([^"]+)"', troops_text):
        troop_id, display_name = m.group(1), m.group(2)
        if not display_name.startswith('{!}'):
            name_map[f"trp_{troop_id}"] = display_name

    # --- 2. Extract personality/hate slots from module_scripts.py ---
    culture_map = {
        "fac_culture_parthian":  "Parthian",
        "fac_culture_roman":     "Roman",
        "fac_culture_germanic":  "Germanic",
        "fac_culture_celtic":    "Britonic",
        "fac_culture_egyptian":  "Egyptian",
        "fac_culture_judean":    "Judean",
        "fac_culture_sarmatian": "Sarmatian",
        "fac_culture_berber":    "Berber",
        "fac_culture_saka":      "Saka",
    }

    clash1 = {}   # trp_id -> hated trp_id (primary)
    clash2 = {}   # trp_id -> hated trp_id (secondary)
    cultures = {} # trp_id -> culture label

    scripts_path = os.path.join(module_dir, 'module_scripts.py')
    with open(scripts_path, encoding='utf-8') as f:
        scripts_text = f.read()

    match_obj = {}  # trp_id -> liked trp_id

    slot_re = re.compile(
        r'\(\s*troop_set_slot\s*,\s*"(trp_[^"]+)"\s*,\s*'
        r'(slot_troop_personalityclash_object'
        r'|slot_troop_personalityclash2_object'
        r'|slot_troop_personalitymatch_object'
        r'|slot_troop_culture)'
        r'\s*,\s*(-?\d+|"[^"]+")'
    )
    for m in slot_re.finditer(scripts_text):
        trp  = m.group(1)
        slot = m.group(2)
        raw  = m.group(3).strip('"')

        if slot == 'slot_troop_personalityclash_object':
            clash1[trp] = None if raw in ('-1', '0') else raw
        elif slot == 'slot_troop_personalityclash2_object':
            clash2[trp] = None if raw in ('-1', '0') else raw
        elif slot == 'slot_troop_personalitymatch_object':
            match_obj[trp] = None if raw in ('-1', '0') else raw
        elif slot == 'slot_troop_culture':
            cultures[trp] = culture_map.get(raw, raw)

    # --- 3. Build companions set, conflicts (hates) and likes dicts ---
    all_trps = sorted(set(clash1) | set(clash2) | set(match_obj))
    companions = set()
    conflicts  = {}  # name -> [hated names]
    likes      = {}  # name -> liked name

    for trp in all_trps:
        if trp not in name_map:
            continue
        name = name_map[trp]
        companions.add(name)
        if name not in conflicts:
            conflicts[name] = []

        for hate_trp in (clash1.get(trp), clash2.get(trp)):
            if hate_trp and hate_trp in name_map:
                hate_name = name_map[hate_trp]
                companions.add(hate_name)
                if hate_name not in conflicts:
                    conflicts[hate_name] = []
                if hate_name not in conflicts[name]:
                    conflicts[name].append(hate_name)

        liked_trp = match_obj.get(trp)
        if liked_trp and liked_trp in name_map:
            likes[name] = name_map[liked_trp]

    # name -> culture label
    name_cultures = {
        name_map[trp]: label
        for trp, label in cultures.items()
        if trp in name_map
    }

    return list(companions), conflicts, name_cultures, likes


# ==========================================
# 2. SOLVER ALGORITHM
# ==========================================

def solve_stable_groups(all_companions, raw_conflicts):
    # 1. Build Symmetric Conflict Graph (Adjacency Matrix of Hate)
    # If A hates B, then B cannot be with A. This is a bidirectional incompatibility.
    hate_graph = {c: set() for c in all_companions}

    for person, enemies in raw_conflicts.items():
        for enemy in enemies:
            if enemy in all_companions:
                hate_graph[person].add(enemy)
                hate_graph[enemy].add(person)

    # 2. Build Compatibility Graph (Complement Graph)
    # Connect A and B if they DO NOT hate each other.
    comp_neighbors = {c: set() for c in all_companions}

    # Optimization: Map names to integers for faster set operations
    name_to_id = {name: i for i, name in enumerate(all_companions)}
    id_to_name = {i: name for i, name in enumerate(all_companions)}
    n = len(all_companions)

    for i in range(n):
        for j in range(i + 1, n):
            p1 = all_companions[i]
            p2 = all_companions[j]

            # If no conflict, add edge in compatibility graph
            if p2 not in hate_graph[p1]:
                comp_neighbors[p1].add(p2)
                comp_neighbors[p2].add(p1)

    # 3. Bron-Kerbosch Algorithm with Pivoting
    # Finds maximal cliques in the compatibility graph
    final_cliques = []

    def bron_kerbosch(r, p, x):
        if not p and not x:
            final_cliques.append(r)
            return

        # Pivot: choose node in P U X with most neighbors in P
        pivot_candidates = p.union(x)
        if not pivot_candidates:
            return

        # Find pivot with max neighbors in P
        # Note: comp_neighbors uses names, r/p/x use names
        pivot = max(pivot_candidates, key=lambda u: len(p.intersection(comp_neighbors[u])))

        for v in p.difference(comp_neighbors[pivot]):
            bron_kerbosch(
                r.union({v}),
                p.intersection(comp_neighbors[v]),
                x.intersection(comp_neighbors[v])
            )
            p.remove(v)
            x.add(v)

    # Run algorithm
    bron_kerbosch(set(), set(all_companions), set())

    # 4. STRICT DEDUPLICATION & CLEANUP
    # Convert to sorted tuples to make them hashable and check uniqueness
    unique_groups = set()
    for clique in final_cliques:
        sorted_clique = tuple(sorted(list(clique)))
        unique_groups.add(sorted_clique)

    # Convert back to list
    result_list = list(unique_groups)

    # 5. Remove Subsets (Ensure Maximality)
    # Bron-Kerbosch guarantees maximal cliques, but we double check to be safe
    # Sort by size descending
    result_list.sort(key=len, reverse=True)

    final_filtered = []
    for i, group in enumerate(result_list):
        is_subset = False
        group_set = set(group)
        # Check if this group is a subset of any larger group already accepted
        for larger in final_filtered:
            if group_set.issubset(set(larger)):
                is_subset = True
                break
        if not is_subset:
            final_filtered.append(group)

    return final_filtered

# ==========================================
# 4. EXECUTION
# ==========================================
def main():
    print("Analyzing Companion Data...")
    comps, conflicts, _cultures, _likes = load_companion_data()

    print(f"Total Companions: {len(comps)}")

    groups = solve_stable_groups(comps, conflicts)

    print(f"\nFound {len(groups)} distinct maximal stable groups.")
    print("="*60)

    print("="*60)
    print("AGGREGATED STATISTICS")
    print("="*60)

    # Group by size (groups are already sorted by size descending)
    from itertools import groupby

    # Filter for groups containing BOTH specific companions
    filtered_groups = [
        g for g in groups
        if "Titocuna" not in g and "Dionysia" not in g
    ]

    # Create a dictionary to store filtered_groups by size
    groups_by_size = {}
    for key, group_iter in groupby(filtered_groups, key=len):
        groups_by_size[key] = list(group_iter)

    # Print summary stats
    print(f"{'GROUP SIZE':<15} | {'VARIATIONS FOUND'}")
    print("-" * 35)

    for size, variations in groups_by_size.items():
        print(f"{size:<15} | {len(variations)}")

    # print("\n" + "="*60)
    # print("DETAILED LISTINGS BY SIZE")
    # print("="*60)

    # # Print detailed listings
    # for size, variations in groups_by_size.items():
    #     print(f"\n>> SIZE: {size} ({len(variations)} Variations)")
    #     print("-" * 30)
    #     for i, group in enumerate(variations):
    #         print(f"  Var {i+1}: {', '.join(group)}")

    # if not groups:
    #     print("No groups found.")
    #     return

    # max_size = len(groups[0])
    # print(f"Maximum Stable Party Size: {max_size}")

    # # Only keep the best groups (Max Size and Max Size - 1)
    # best_groups = [g for g in groups if len(g) >= max_size - 1]

    # print(f"Number of 'Best' Groups (Size {max_size} or {max_size-1}): {len(best_groups)}")

    # # Group by size for display
    # from itertools import groupby
    # groups_by_size = {}
    # for key, group_iter in groupby(best_groups, key=len):
    #     groups_by_size[key] = list(group_iter)

    # for size, variations in groups_by_size.items():
    #     print(f"\n>> SIZE: {size} ({len(variations)} Variations)")
    #     # Just print the first 5 examples of each size to check
    #     for i, group in enumerate(variations[:5]):
    #         print(f"  Ex {i+1}: {', '.join(sorted(group))}")

    # Group results by size
    # size_buckets = {}
    # for group in groups:
    #     size = len(group)
    #     if size not in size_buckets:
    #         size_buckets[size] = []
    #     size_buckets[size].append(group)

    # # Display
    # sorted_sizes = sorted(size_buckets.keys(), reverse=True)

    # for size in sorted_sizes:
    #     party_list = size_buckets[size]
    #     print(f"\n=== SIZE: {size} ({len(party_list)} variations) ===")

    #     for i, party in enumerate(party_list):
    #         print(f"Option {i+1}: {', '.join(party)}")

    # for i, group in enumerate(groups[:20]):
    #     print(f"GROUP #{i+1} (Size: {len(group)})")
    #     print(f"Members: {', '.join(group)}")
    #     print("-" * 60)

if __name__ == "__main__":
    main()