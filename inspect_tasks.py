import json

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-16') as f:
            return json.load(f)
    except:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

print("==================================================================")
print("ANALYSIS OF Tablero_EDT_Trello.html (EDT_TASKS)")
print("==================================================================")
try:
    edt = load_json('edt_tasks.json')
    print(f"Total tasks in EDT_TASKS: {len(edt)}")
    phases = {}
    for t in edt:
        p = t.get('phase', 'other')
        if p not in phases:
            phases[p] = []
        phases[p].append(t)
    
    for p, items in phases.items():
        print(f"\n--- PHASE: {p} ({len(items)} items) ---")
        for it in items:
            is_sum = it.get('isSummary', False)
            code = it.get('code', it.get('id'))
            title = it.get('title')
            deliv = it.get('deliverable', 'N/A')
            dates = it.get('dates', 'N/A')
            pct = it.get('percentDone', 0)
            print(f"  [{code}] {'(SUMMARY) ' if is_sum else ''}{title} | Dates: {dates} | %Done: {pct} | Deliv: {deliv}")
except Exception as e:
    print("Error reading edt_tasks.json:", e)

print("\n==================================================================")
print("ANALYSIS OF Visor_Fases_y_Normas_SIGE.html (tasks)")
print("==================================================================")
try:
    visor = load_json('visor_tasks.json')
    print(f"Total tasks in Visor: {len(visor)}")
    for t in visor:
        print(f"  [{t.get('id', t.get('codigo'))}] {t.get('nombre', t.get('titulo'))} | Fase: {t.get('fase')} | Estado: {t.get('estado')}")
except Exception as e:
    print("Error reading visor_tasks.json:", e)
