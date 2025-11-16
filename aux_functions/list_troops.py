import re
import csv
from pathlib import Path

# Simple constants (no CLI)
INPUT = Path("module_system/module_troops.py")
OUTPUT = Path("aux_functions/troops.csv")


def main() -> None:
    text = INPUT.read_text(encoding="utf-8")

    # Try to narrow to the troops block
    m = re.search(r"\btroops\s*=\s*\[", text)
    snippet = text
    if m:
        start = m.end()
        i = start
        depth = 1
        L = len(text)
        while i < L and depth > 0:
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
            i += 1
        if depth == 0:
            snippet = text[start:i-1]

    # Match list/tuple entries like ["id","Singular","Plural", ...]
    pat = re.compile(r'[\[\(]\s*(["\'])(?P<id>.*?)\1\s*,\s*(["\'])(?P<singular>.*?)\3\s*,\s*(["\'])(?P<plural>.*?)\5', re.S)
    rows = []
    for mm in pat.finditer(snippet):
        rows.append((mm.group('id').strip(), mm.group('singular').strip(), mm.group('plural').strip()))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['troop_id', 'name_singular', 'name_plural'])
        for r in rows:
            w.writerow(r)

    print(f"Saved {len(rows)} troops to {OUTPUT}")


if __name__ == '__main__':
    main()