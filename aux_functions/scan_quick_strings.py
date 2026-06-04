import os
import re
from collections import Counter, defaultdict

# Files to scan for quick strings
FILES_TO_SCAN = [
    "module_system/module_scripts.py",
    "module_system/module_dialogs.py",
    "module_system/module_game_menus.py",
    "module_system/module_presentations.py",
    "module_system/module_simple_triggers.py",
    "module_system/module_triggers.py",
    "module_system/module_mission_templates.py"
]

# Regex designed to capture:
# Group 1: Triple-double quotes ("""@content""")
# Group 2: Triple-single quotes ('''@content''')
# Group 3: Single-double quotes ("@content")
# Group 4: Single-single quotes ('@content')
QUICK_STRING_RE = re.compile(
    r'"""@(?P<td_val>[\s\S]*?)"""|'
    r"'''@(?P<ts_val>[\s\S]*?)'''|"
    r'"@(?P<sd_val>[^"\\]*(?:\\.[^"\\]*)*)"|'
    r"'@(?P<ss_val>[^'\\]*(?:\\.[^'\\]*)*)'"
)

def scan_file(filename, occurrences_map):
    if not os.path.exists(filename):
        print(f"Warning: File {filename} not found. Skipping.")
        return 0

    count = 0
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            # Skip comments to avoid false positives
            stripped = line.strip()
            if stripped.startswith('#'):
                continue

            for match in QUICK_STRING_RE.finditer(line):
                # Retrieve whichever group was matched
                group_dict = match.groupdict()
                text = next((val for val in group_dict.values() if val is not None), None)

                if text is not None:
                    # Clean up escaping if necessary
                    text = text.replace('\\"', '"').replace("\\'", "'")
                    occurrences_map[text].append((filename, line_num))
                    count += 1
    return count

def main():
    occurrences = defaultdict(list)
    total_found = 0

    print("Scanning Warband Module files for quick strings...")
    print("-" * 60)

    for filename in FILES_TO_SCAN:
        count = scan_file(filename, occurrences)
        if count > 0:
            print(f"Parsed {filename}: found {count} quick strings.")
        total_found += count

    print("-" * 60)
    print(f"Total quick strings found: {total_found}")
    print(f"Unique quick strings found: {len(occurrences)}")
    print("-" * 60)

    # Sort by frequency of usage descending
    sorted_occurrences = sorted(occurrences.items(), key=lambda x: len(x[1]), reverse=True)

    # Print top 15 most used to console
    print("Top 15 most frequent quick strings:")
    for idx, (text, locs) in enumerate(sorted_occurrences[:15], 1):
        truncated_text = text if len(text) < 50 else text[:47] + "..."
        print(f"{idx:2d}. [Used {len(locs):2d}x] \"{truncated_text}\"")

    # Write a detailed report to a file for ease of refactoring
    report_file = "quick_strings_report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=== DETAILED QUICK STRINGS REPORT ===\n")
        f.write(f"Total Occurrences: {total_found}\n")
        f.write(f"Unique Strings: {len(occurrences)}\n\n")
        f.write("Ordered by frequency of usage:\n")
        f.write("=" * 60 + "\n\n")

        for idx, (text, locs) in enumerate(sorted_occurrences, 1):
            f.write(f"#{idx} [Used {len(locs)} times]\n")
            f.write(f"Text: \"{text}\"\n")
            f.write("Locations:\n")
            for file, line in locs:
                f.write(f"  - {file} : Line {line}\n")
            f.write("-" * 60 + "\n\n")

    print("-" * 60)
    print(f"Detailed report saved to: {report_file}")

if __name__ == "__main__":
    main()