import re

# ==========================================
# 1. THE RAW DATA
# ==========================================
raw_data = """
<trp=686>Pravare Ytarim</> (Parthian): Likely in <p=27>Chersonesus</> (Streets).
     +) Likes <trp=687>Marius Gaius</>
     -) Hates <trp=692>Lavia</>
     -) Hates <trp=701>Titocuna</>
<trp=687>Marius Gaius</> (Roman): Likely in <p=42>Antiochia</> (Streets).
     +) Likes <trp=686>Pravare Ytarim</>
     -) Hates <trp=690>Satibarzanes</>
     -) Hates <trp=694>Aturius Spurus</>
<trp=688>Pulchra</> (Roman): Likely in <p=58>Nicomedia</> (Tavern).
     +) Likes <trp=694>Aturius Spurus</>
     -) Hates <trp=699>Titus</>
     -) Hates <trp=693>Hildr</>
<trp=689>Abadutiker</> (Germanic): Likely in <p=45>Tur</> (Streets).
     +) Likes <trp=690>Satibarzanes</>
     -) Hates <trp=695>Attaklos</>
     -) Hates <trp=692>Lavia</>
<trp=690>Satibarzanes</> (Parthian): Likely in <p=59>Ecbatana</> (Streets).
     +) Likes <trp=689>Abadutiker</>
     -) Hates <trp=687>Marius Gaius</>
     -) Hates <trp=696>Dionysia</>
<trp=691>Firentrix</> (Britonic): Likely in <p=50>Corduba</> (Tavern).
     +) Likes <trp=697>Jeremus</>
     -) Hates <trp=696>Dionysia</>
     -) Hates <trp=698>Chanakya</>
<trp=692>Lavia</> (Egyptian): Likely in <p=40>Alexandria</> (Streets).
     +) Likes <trp=701>Titocuna</>
     -) Hates <trp=686>Pravare Ytarim</>
     -) Hates <trp=689>Abadutiker</>
<trp=693>Hildr</> (Germanic): Likely in <p=65>Uburzis</> (Tavern).
     +) Likes <trp=698>Chanakya</>
     -) Hates <trp=697>Jeremus</>
     -) Hates <trp=688>Pulchra</>
<trp=694>Aturius Spurus</> (Roman): Likely in <p=32>Lugdunum</> (Tavern).
     +) Likes <trp=688>Pulchra</>
     -) Hates <trp=698>Chanakya</>
     -) Hates <trp=687>Marius Gaius</>
<trp=695>Attaklos</> (Roman): Likely in <p=57>Athenae</> (Tavern).
     +) Likes <trp=696>Dionysia</>
     -) Hates <trp=689>Abadutiker</>
     -) Hates <trp=699>Titus</>
<trp=696>Dionysia</> (Roman): Likely in <p=55>Thessalonica</> (Streets).
     +) Likes <trp=695>Attaklos</>
     -) Hates <trp=691>Firentrix</>
     -) Hates <trp=690>Satibarzanes</>
<trp=697>Jeremus</> (Roman): Likely in <p=22>Lutetia</> (Tavern).
     +) Likes <trp=691>Firentrix</>
     -) Hates <trp=693>Hildr</>
     -) Hates <trp=700>Artimenus</>
<trp=698>Chanakya</> (Sarmatian): Likely in <p=47>Ctesiphon</> (Streets).
     +) Likes <trp=693>Hildr</>
     -) Hates <trp=694>Aturius Spurus</>
     -) Hates <trp=691>Firentrix</>
<trp=699>Titus</> (Roman): Likely in <p=25>Mediolanum</> (Tavern).
     +) Likes <trp=700>Artimenus</>
     -) Hates <trp=688>Pulchra</>
     -) Hates <trp=695>Attaklos</>
<trp=700>Artimenus</> (Roman): Likely in <p=76>Vindobona</> (Hall).
     +) Likes <trp=699>Titus</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=697>Jeremus</>
<trp=701>Titocuna</> (Britonic): Likely in <p=21>Deva</> (Tavern).
     +) Likes <trp=692>Lavia</>
     -) Hates <trp=700>Artimenus</>
     -) Hates <trp=686>Pravare Ytarim</>
<trp=702>Anicetus</> (Roman): Likely in <p=34>Phasis</> (Tavern).
<trp=703>Arminius Octavianus</> (Roman): Likely in <p=67>Palmyra</> (Streets).
     +) Likes <trp=704>Tertius Maior</>
     -) Hates <trp=722>Josephus</>
     -) Hates <trp=696>Dionysia</>
<trp=704>Tertius Maior</> (Roman): Likely in <p=67>Palmyra</> (Tavern).
     +) Likes <trp=725>Kara Boga</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=705>Secundus Minor</> (Roman): Likely in <p=60>Dura Europos</> (Streets).
     +) Likes <trp=727>Chaditox</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=706>Drusus</> (Roman): Likely in <p=56>Dyrrachium</> (Tavern).
     +) Likes <trp=707>Libertus Tiro</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=707>Libertus Tiro</> (Roman): Likely in <p=52>Tarraco</> (Tavern).
     +) Likes <trp=701>Titocuna</>
     -) Hates <trp=708>Lucius Varrus Drusus</>
     -) Hates <trp=712>Lucullus Caepio</>
<trp=708>Lucius Varrus Drusus</> (Roman): Likely in <p=51>Augusta Emerita</> (Streets).
<trp=709>Sidonius Apollinaris</> (Roman): Likely in <p=39>Hierosolyma</> (Tavern).
     +) Likes <trp=710>Sollius Modestus</>
     -) Hates <trp=727>Chaditox</>
     -) Hates <trp=696>Dionysia</>
<trp=710>Sollius Modestus</> (Roman): Likely in <p=68>Thebae</> (Streets).
     +) Likes <trp=711>Albinus Basilius</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=711>Albinus Basilius</> (Roman): Likely in <p=70>Mtskheta</> (Tavern).
     +) Likes <trp=712>Lucullus Caepio</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=712>Lucullus Caepio</> (Roman): Likely in <p=55>Thessalonica</> (Tavern).
     +) Likes <trp=718>Lucius Modius minor</>
     -) Hates <trp=716>Ra Karak</>
     -) Hates <trp=722>Josephus</>
<trp=713>Anicius</> (Roman): Likely in <p=24>Massilia</> (Tavern).
     +) Likes <trp=714>Fabianus</>
     -) Hates <trp=725>Kara Boga</>
     -) Hates <trp=696>Dionysia</>
<trp=714>Fabianus</> (Roman): Likely in <p=23>Augusta</> (Tavern).
     +) Likes <trp=715>Rombus</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=715>Rombus</> (Roman): Likely in <p=28>Ancyra</> (Streets).
     +) Likes <trp=688>Pulchra</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=696>Dionysia</>
<trp=716>Ra Karak</> (Berber): Joins during quest.
<trp=717>Gaius Lemonius</> (Roman): Likely in <p=54>Neapolis</> (Streets).
     -) Hates <trp=718>Lucius Modius minor</>
<trp=718>Lucius Modius minor</> (Roman): Likely in <p=53>Tarentum</> (Streets).
     -) Hates <trp=717>Gaius Lemonius</>
<trp=719>Ligia</> (Germanic): Likely in <p=26>Roma</> (Backstreets).
     +) Likes <trp=721>Marcus Vinicius</>
     -) Hates <trp=723>Elazar Bar Yochai</>
     -) Hates <trp=725>Kara Boga</>
<trp=720>Ursus</> (Germanic): Joins together with Ligia.
     -) Hates <trp=725>Kara Boga</>
<trp=721>Marcus Vinicius</> (Roman): Likely in <p=26>Roma</> (Tavern).
     +) Likes <trp=719>Ligia</>
     -) Hates <trp=723>Elazar Bar Yochai</>
<trp=722>Josephus</> (Judean): Likely in <p=116>Masada</> (Streets).
     +) Likes <trp=690>Satibarzanes</>
     -) Hates <trp=712>Lucullus Caepio</>
     -) Hates <trp=703>Arminius Octavianus</>
<trp=723>Elazar Bar Yochai</> (Judean): Likely in <p=49>Leptis Magna</> (Streets).
     +) Likes <trp=722>Josephus</>
     -) Hates <trp=721>Marcus Vinicius</>
     -) Hates <trp=719>Ligia</>
<trp=724>Mathildiz</> (Germanic): Joins during quest.
<trp=725>Kara Boga</> (Egyptian): Likely in <p=40>Alexandria</> (Tavern).
     +) Likes <trp=703>Arminius Octavianus</>
     -) Hates <trp=713>Anicius</>
     -) Hates <trp=719>Ligia</>
<trp=726>Eamane Turakina</> (Saka): Joins during quest.
<trp=727>Chaditox</> (Sarmatian): Likely in <p=46>Siracena</> (Streets).
     +) Likes <trp=705>Secundus Minor</>
     -) Hates <trp=709>Sidonius Apollinaris</>
"""

# ==========================================
# 2. PARSING LOGIC
# ==========================================
def parse_data(data):
    companions = set()
    conflicts = {} # Key: Troop Name, Value: List of hated names

    current_companion = None

    lines = data.split('\n')
    for line in lines:
        line = line.strip()

        # Check for main companion definition
        main_match = re.search(r"<trp=\d+>(.*?)</>", line)

        if main_match and not line.startswith(("+", "-")):
            current_companion = main_match.group(1).strip()
            companions.add(current_companion)
            if current_companion not in conflicts:
                conflicts[current_companion] = []

        # Check for Hate lines
        elif current_companion and "-) Hates" in line:
            hated_match = re.search(r"<trp=\d+>(.*?)</>", line)
            if hated_match:
                hated_person = hated_match.group(1).strip()
                conflicts[current_companion].append(hated_person)

                # Ensure hated person is in the master list
                companions.add(hated_person)
                if hated_person not in conflicts:
                    conflicts[hated_person] = []

    return list(companions), conflicts

# ==========================================
# 3. SOLVER ALGORITHM
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
    comps, conflicts = parse_data(raw_data)

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