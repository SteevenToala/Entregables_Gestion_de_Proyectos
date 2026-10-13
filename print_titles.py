import json

with open('cards_manifest.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for c in cards:
    print(f"{c['code']} | {c['phase']} | {c['title']} | {c.get('deliverable', '')}")
