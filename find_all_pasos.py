# find_all_pasos.py
import re, glob

files = glob.glob('generate_fase*.py') + glob.glob('fase3_annexes_*.py')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    matches = []
    for i, line in enumerate(lines):
        m = re.search(r'\bpaso\s*\d+\b', line, re.I)
        if m:
            matches.append((i+1, line.strip()[:100]))
    if matches:
        print(f'=== {fpath}: {len(matches)} occurrences of Paso X ===')
        for lno, text in matches[:10]:
            print(f'  L{lno}: {text}')
        if len(matches) > 10:
            print(f'  ... and {len(matches)-10} more')
