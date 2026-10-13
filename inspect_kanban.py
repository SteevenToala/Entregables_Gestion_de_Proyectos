import json
import re

with open(r'../AlcanceInforme/Tablero_EDT_Trello.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the renderKanban() function or how cards are created in the HTML
m = re.search(r'function renderKanban\(\)\s*\{(.*?)\n\s*function', html, re.DOTALL)
if m:
    print("Found renderKanban function!")
    print(m.group(0)[:500])

# Let's check what phases are defined in renderKanban
phases_m = re.search(r'const phases\s*=\s*(\[.*?\]);', html, re.DOTALL)
if phases_m:
    print("Phases in Kanban:", phases_m.group(1))

# Let's check how EDT_TASKS are filtered or mapped to columns
print("\nInspecting tasks per phase in EDT_TASKS:")
with open('edt_tasks.json', 'r', encoding='utf-16') as f:
    tasks = json.load(f)

by_phase = {}
for t in tasks:
    if not t.get('isSummary'):
        p = t.get('phase')
        by_phase.setdefault(p, []).append(t)

for p, tlist in by_phase.items():
    print(f"\nPhase: {p} ({len(tlist)} cards):")
    for t in tlist:
        print(f"  {t.get('code')} - {t.get('title')} (Dates: {t.get('dates')})")
