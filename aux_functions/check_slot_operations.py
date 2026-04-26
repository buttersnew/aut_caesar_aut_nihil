#!/usr/bin/env python3
"""
check_slot_operations.py
========================
Detects mismatched slot operations in module_*.py files.

A "mismatch" is when e.g. `party_slot_eq` is used with a `slot_faction_*`
constant, or `faction_slot_eq` is used with a `slot_center_*` constant.

The tool works in two passes:
  1. Parse module_constants.py (section-header based) to build a full
     mapping  slot_name -> entity_type  that covers every named slot
     including aliases.
  2. Walk the AST of every module_*.py and check each slot operation tuple.

Unknown slot identifiers (e.g. bare numeric expressions or exotic aliases
that can't be categorised) are silently skipped – no false positives.

Usage:
    python aux_functions/check_slot_operations.py
    python aux_functions/check_slot_operations.py --verbose   # also show skipped unknowns
"""

import ast
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 1.  Slot operations: name -> (expected_entity_type, slot_arg_index_in_tuple)
#     index 0 = the operation name itself, 1 = first arg, etc.
# ---------------------------------------------------------------------------
SLOT_OPERATIONS: dict[str, tuple[str, int]] = {
    # party ------------------------------------------------------------------
    "party_set_slot":   ("party", 2),   # (op, party_id, slot_no, value)
    "party_get_slot":   ("party", 3),   # (op, dest, party_id, slot_no)
    "party_slot_eq":    ("party", 2),   # (op, party_id, slot_no, value)
    "party_slot_ge":    ("party", 2),
    "party_slot_lt":    ("party", 2),
    # faction ----------------------------------------------------------------
    "faction_set_slot":  ("faction", 2),
    "faction_get_slot":  ("faction", 3),
    "faction_slot_eq":   ("faction", 2),
    "faction_slot_ge":   ("faction", 2),
    "faction_slot_lt":   ("faction", 2),
    # troop ------------------------------------------------------------------
    "troop_set_slot":   ("troop", 2),
    "troop_get_slot":   ("troop", 3),
    "troop_slot_eq":    ("troop", 2),
    "troop_slot_ge":    ("troop", 2),
    "troop_slot_lt":    ("troop", 2),
    # item -------------------------------------------------------------------
    "item_set_slot":    ("item", 2),
    "item_get_slot":    ("item", 3),
    "item_slot_eq":     ("item", 2),
    "item_slot_ge":     ("item", 2),
    "item_slot_lt":     ("item", 2),
    # agent ------------------------------------------------------------------
    "agent_set_slot":   ("agent", 2),
    "agent_get_slot":   ("agent", 3),
    "agent_slot_eq":    ("agent", 2),
    "agent_slot_ge":    ("agent", 2),
    # scene ------------------------------------------------------------------
    "scene_set_slot":   ("scene", 2),
    "scene_get_slot":   ("scene", 3),
    "scene_slot_eq":    ("scene", 2),
    # quest ------------------------------------------------------------------
    "quest_set_slot":   ("quest", 2),
    "quest_get_slot":   ("quest", 3),
    "quest_slot_eq":    ("quest", 2),
    # scene-prop / prop_instance ---------------------------------------------
    "prop_instance_set_slot": ("prop_instance", 2),
    "prop_instance_get_slot": ("prop_instance", 3),
    "prop_instance_slot_eq":  ("prop_instance", 2),
}

# ---------------------------------------------------------------------------
# 2.  Prefix fallback: covers slots that aren't declared in module_constants
#     but follow the naming convention found in other header/module files.
#     Ordered longest-first so more specific prefixes match first.
# ---------------------------------------------------------------------------
PREFIX_TO_ENTITY: list[tuple[str, str]] = sorted([
    # party (towns, villages and centers ARE parties in the game)
    ("slot_party_",               "party"),
    ("slot_town_",                "party"),
    ("slot_village_",             "party"),
    ("slot_center_",              "party"),
    ("slot_cohort_",              "party"),
    ("slot_grounds_",             "party"),
    ("slot_lat_",                 "party"),
    ("slot_cattle_",              "party"),
    ("slot_donate_",              "party"),
    ("slot_rebellion_",           "party"),
    ("dplmc_slot_party_",         "party"),
    ("dplmc_slot_center_",        "party"),
    # faction
    ("slot_faction_",             "faction"),
    ("dplmc_slot_faction_",       "faction"),
    # troop
    ("slot_troop_",               "troop"),
    ("slot_slave_",               "troop"),
    ("slot_crafting_",            "troop"),
    # item
    ("slot_item_",                "item"),
    # agent
    ("slot_agent_",               "agent"),
    ("slot_real_troop",           "agent"),   # exact name, checked via startswith too
    ("slot_possessed",            "agent"),
    ("slot_horse_",               "agent"),
    # scene
    ("slot_scene_",               "scene"),
    # prop_instance
    ("slot_scene_prop_",          "prop_instance"),
    # quest
    ("slot_quest_",               "quest"),
], key=lambda t: -len(t[0]))   # longest prefix first


# ---------------------------------------------------------------------------
# 3.  Entity detection: prefix-only.
#
#     We deliberately do NOT use section-header-based classification from
#     module_constants.py because many mods place custom game-state slots
#     (e.g. slot_senate_*, slot_india_*) under the "## QUEST SLOTS" header
#     while intentionally accessing them via troop_set_slot / party_set_slot.
#     A section-based oracle would generate hundreds of false positives for
#     that pattern.
#
#     Instead we rely solely on the naming-convention prefix list above,
#     which covers the "unambiguous" prefixes (slot_faction_, slot_troop_,
#     slot_center_, etc.).  Slots with no matching prefix are skipped.
# ---------------------------------------------------------------------------

def build_slot_map(_constants_path: Path) -> dict[str, str]:
    """Stub – prefix-only mode, no section parsing needed."""
    return {}


def entity_from_slot(slot_name: str, _slot_map: dict[str, str]) -> str | None:
    """Return entity type for a slot name via prefix, or None if unknown."""
    for prefix, entity in PREFIX_TO_ENTITY:
        if slot_name.startswith(prefix):
            return entity
    return None


# ---------------------------------------------------------------------------
# 4.  AST helpers
# ---------------------------------------------------------------------------

def get_op_name(node: ast.expr) -> str | None:
    """Extract the operation identifier, handling  neg|op  patterns."""
    if isinstance(node, ast.Name):
        return node.id
    # neg|party_slot_eq  ->  BinOp(left=Name('neg'), op=BitOr, right=Name(...))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return get_op_name(node.right)
    return None


def get_name(node: ast.expr) -> str | None:
    """Return identifier name if node is a Name, else None."""
    return node.id if isinstance(node, ast.Name) else None


# ---------------------------------------------------------------------------
# 5.  File checker
# ---------------------------------------------------------------------------

def check_file(
    filepath: Path,
    slot_map: dict[str, str],
    verbose: bool = False,
) -> list[dict]:
    issues = []
    try:
        source = filepath.read_text(encoding="utf-8", errors="ignore")
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as exc:
        print(f"  [WARN] Cannot parse {filepath.name}: {exc}")
        return issues

    for node in ast.walk(tree):
        if not isinstance(node, ast.Tuple):
            continue
        if len(node.elts) < 2:
            continue

        op_name = get_op_name(node.elts[0])
        if op_name not in SLOT_OPERATIONS:
            continue

        expected_entity, slot_idx = SLOT_OPERATIONS[op_name]
        if slot_idx >= len(node.elts):
            continue

        slot_node = node.elts[slot_idx]
        slot_name = get_name(slot_node)
        if slot_name is None:
            # Slot argument is a number, expression, or local variable string –
            # can't determine type statically.
            continue

        if not (slot_name.startswith("slot_") or slot_name.startswith("dplmc_slot_")):
            continue  # Not a slot constant

        actual_entity = entity_from_slot(slot_name, slot_map)
        if actual_entity is None:
            if verbose:
                print(
                    f"  [SKIP] {filepath.name}:{node.lineno}  "
                    f"{op_name}(..., {slot_name}, ...)  → slot type unknown"
                )
            continue

        if actual_entity != expected_entity:
            issues.append(
                {
                    "file": filepath,
                    "line": node.lineno,
                    "op": op_name,
                    "slot": slot_name,
                    "expected": expected_entity,
                    "actual": actual_entity,
                }
            )

    return issues


# ---------------------------------------------------------------------------
# 6.  Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    repo_root = Path(__file__).resolve().parent.parent
    module_dir = repo_root / "module_system"
    constants_path = module_dir / "module_constants.py"

    if not constants_path.exists():
        sys.exit(f"Cannot find {constants_path}")

    slot_map = build_slot_map(constants_path)

    files = sorted(module_dir.glob("module_*.py"))
    all_issues: list[dict] = []
    for f in files:
        issues = check_file(f, slot_map, verbose=verbose)
        all_issues.extend(issues)

    if not all_issues:
        print("No slot operation mismatches found.")
        return

    # Group by file for readable output
    by_file: dict[Path, list[dict]] = {}
    for issue in all_issues:
        by_file.setdefault(issue["file"], []).append(issue)

    print(f"Found {len(all_issues)} mismatch(es) across {len(by_file)} file(s):\n")
    print("=" * 72)
    for filepath in sorted(by_file):
        rel = filepath.relative_to(repo_root)
        print(f"\n{rel}  ({len(by_file[filepath])} issue(s))")
        print("-" * 72)
        for issue in sorted(by_file[filepath], key=lambda x: x["line"]):
            print(
                f"  line {issue['line']:>4}  {issue['op']}(..., {issue['slot']}, ...)"
            )
            print(
                f"            Operation expects a '{issue['expected']}' slot, "
                f"but '{issue['slot']}' belongs to '{issue['actual']}' slots"
            )
    print()


if __name__ == "__main__":
    main()
