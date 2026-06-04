#!/usr/bin/env python3
import os
import sys
import re
import ast

# Configuration of paths
INPUT_DIR = "companion_dialogues_input"
MODULE_STRINGS_PATH = os.path.normpath("module_system/module_strings.py")

# Suffixes in the exact sequential order they are expected
SUFFIX_LIST = [
    "intro", "intro_response_1", "intro_response_2",
    "backstory_a", "backstory_b", "backstory_c", "backstory_later",
    "backstory_response_1", "backstory_response_2",
    "signup", "signup_2", "signup_response_1", "signup_response_2",
    "payment", "payment_response",
    "morality_speech", "2ary_morality_speech",
    "personalityclash_speech", "personalityclash_speech_b",
    "personalityclash2_speech", "personalityclash2_speech_b",
    "personalitymatch_speech", "personalitymatch_speech_b",
    "retirement_speech", "rehire_speech",
    "home_intro", "home_description", "home_description_2", "home_recap",
    "honorific",
    "kingsupport_1", "kingsupport_2", "kingsupport_2a", "kingsupport_2b", "kingsupport_3",
    "kingsupport_objection", "intel_mission", "fief_acceptance",
    "woman_to_woman", "turn_against"
]

def resolve_string_node(node):
    """
    Safely resolves AST string nodes, handling binary addition operations
    for string concatenations (e.g., "string1" + "string2").
    """
    if hasattr(ast, 'Constant') and isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = resolve_string_node(node.left)
        right = resolve_string_node(node.right)
        if left is not None and right is not None:
            return left + right
    return None

def parse_companion_file(filepath):
    """
    Parses a companion file into a dictionary of {string_id: string_value}.
    Uses AST parsing for safety and falls back to regex if syntax fails.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    wrapped_content = f"[\n{content}\n]"

    try:
        tree = ast.parse(wrapped_content)
    except SyntaxError as e:
        print(f"Warning: AST parse failed for {filepath}: {e}")
        print("Attempting fallback line-by-line regex parsing...")
        return parse_companion_file_regex(content)

    strings_dict = {}
    if len(tree.body) > 0 and isinstance(tree.body[0], ast.Expr):
        expr = tree.body[0].value
        if isinstance(expr, ast.List):
            for elt in expr.elts:
                if isinstance(elt, ast.Tuple) and len(elt.elts) >= 2:
                    id_val = resolve_string_node(elt.elts[0])
                    str_val = resolve_string_node(elt.elts[1])
                    if id_val and str_val is not None:
                        strings_dict[id_val] = str_val
    return strings_dict

def parse_companion_file_regex(content):
    """
    Fallback regex parser to match tuples in case AST parsing fails.
    """
    strings_dict = {}
    pattern = re.compile(r'\(\s*["\'](npc\d+_\w+)["\']\s*,\s*["\'](.*?)["\']\s*\)', re.DOTALL)
    for match in pattern.finditer(content):
        strings_dict[match.group(1)] = match.group(2)
    return strings_dict

def insert_dialogues_structured(npc_id, strings_dict):
    """
    Finds the correct dialogue block for each individual suffix and inserts
    the string immediately following the last companion's dialogue in that group.
    """
    if not os.path.exists(MODULE_STRINGS_PATH):
        print(f"Error: Target file '{MODULE_STRINGS_PATH}' not found.")
        return False

    # Extract numeric companion index (e.g., 'npc44' -> 44)
    match_num = re.search(r'\d+', npc_id)
    if not match_num:
        print(f"Error: Companion ID '{npc_id}' does not contain numbers.")
        return False
    target_num = int(match_num.group())

    required_ids = [f"{npc_id}_{sfx}" for sfx in SUFFIX_LIST]
    missing_ids = [req_id for req_id in required_ids if req_id not in strings_dict]
    if missing_ids:
        print(f"\n[WARNING] Missing {len(missing_ids)} required string ID(s) for '{npc_id}':")
        for m_id in missing_ids:
            print(f"  - {m_id}")
    else:
        print(f"All {len(required_ids)} required dialogue IDs verified for '{npc_id}'.")

    # Read the current module_strings.py lines
    with open(MODULE_STRINGS_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Idempotent cleanup: Purge any existing lines belonging to this target NPC ID
    clean_lines = []
    removed_count = 0
    npc_prefix_double = f'"{npc_id}_'
    npc_prefix_single = f"'{npc_id}_"

    for line in lines:
        if npc_prefix_double in line or npc_prefix_single in line:
            removed_count += 1
            continue
        clean_lines.append(line)

    if removed_count > 0:
        print(f"Purged {removed_count} out-of-order/old dialogue lines for '{npc_id}' first.")

    # Insert dialogue strings one suffix at a time
    inserted_count = 0
    for sfx in SUFFIX_LIST:
        string_id = f"{npc_id}_{sfx}"
        if string_id not in strings_dict:
            continue

        val = strings_dict[string_id].replace('"', '\\"')
        formatted_line = f'  ("{string_id}", "{val}"),\n'

        best_idx = -1
        max_seen_num = -1

        # Word boundaries ensure 'signup' matches but does not false-positive on 'signup_2'
        pattern = re.compile(r'npc(\d+)_' + re.escape(sfx) + r'\b')

        for idx, line in enumerate(clean_lines):
            match = pattern.search(line)
            if match:
                seen_num = int(match.group(1))
                # We want to find the highest companion index smaller than our target index
                if seen_num < target_num and seen_num > max_seen_num:
                    max_seen_num = seen_num
                    best_idx = idx

        if best_idx != -1:
            # Insert immediately after the preceding companion's line for this group
            clean_lines.insert(best_idx + 1, formatted_line)
            inserted_count += 1
        else:
            # Fallback 1: If there is no companion with a smaller ID, insert after any companion in the group
            any_idx = -1
            for idx, line in enumerate(clean_lines):
                if pattern.search(line):
                    any_idx = idx

            if any_idx != -1:
                clean_lines.insert(any_idx + 1, formatted_line)
                inserted_count += 1
            else:
                # Fallback 2: Insert right before the closing '#NPC companion changes end' marker
                marker_pattern = re.compile(r'#\s*NPC\s+companion\s+changes\s+end', re.IGNORECASE)
                marker_idx = -1
                for idx, line in enumerate(clean_lines):
                    if marker_pattern.search(line):
                        marker_idx = idx
                        break

                if marker_idx != -1:
                    clean_lines.insert(marker_idx, formatted_line)
                    inserted_count += 1
                else:
                    # Final Fallback: Append before list closing bracket
                    for idx in range(len(clean_lines) - 1, -1, -1):
                        if ']' in clean_lines[idx]:
                            clean_lines.insert(idx, formatted_line)
                            inserted_count += 1
                            break

    # Write changes back to module_strings.py
    with open(MODULE_STRINGS_PATH, 'w', encoding='utf-8') as f:
        f.writelines(clean_lines)

    print(f"Successfully processed and grouped {inserted_count} dialogues for '{npc_id}' inside '{MODULE_STRINGS_PATH}'.")
    return True

def main():
    if len(sys.argv) > 1:
        # Process a specific file passed via CLI arguments
        arg = sys.argv[1]
        filename = os.path.basename(arg)
        npc_id = os.path.splitext(filename)[0]

        if not re.match(r'^npc\d+$', npc_id):
            print(f"Error: Parameter '{arg}' doesn't resolve to a companion pattern like 'npc44'.")
            sys.exit(1)

        filepath = os.path.join(INPUT_DIR, f"{npc_id}.py") if not os.path.exists(arg) else arg
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            sys.exit(1)

        print(f"Running targeted grouping insert for file: {filepath}")
        strings_dict = parse_companion_file(filepath)
        insert_dialogues_structured(npc_id, strings_dict)
    else:
        # No arguments: Batch process all files inside the input directory
        if not os.path.exists(INPUT_DIR):
            print(f"Error: Folder '{INPUT_DIR}' does not exist.")
            sys.exit(1)

        files = [f for f in os.listdir(INPUT_DIR) if f.startswith("npc") and f.endswith(".py")]
        if not files:
            print(f"No companion files found in '{INPUT_DIR}'.")
            sys.exit(0)

        print(f"Found {len(files)} companion file(s) in '{INPUT_DIR}'. Beginning structured update...")
        for file in sorted(files, key=lambda name: int(re.search(r'\d+', name).group() if re.search(r'\d+', name) else 0)):
            npc_id = os.path.splitext(file)[0]
            filepath = os.path.join(INPUT_DIR, file)
            print(f"\n--- Structuring {npc_id} ---")
            strings_dict = parse_companion_file(filepath)
            insert_dialogues_structured(npc_id, strings_dict)

if __name__ == "__main__":
    main()