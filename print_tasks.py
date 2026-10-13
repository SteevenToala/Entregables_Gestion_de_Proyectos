import json

with open('Entregables_Latex/trello_tasks_utf8.json', 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f"Total tasks in Trello HTML: {len(tasks)}\n")
for t in tasks:
    print(f"[{t['id']}] Fase: {t.get('fase')} | Sem: {t.get('semana')} | Fechas: {t.get('fechas')} | Resp: {t.get('resp')}")
    print(f"  Titulo: {t.get('titulo')}")
    print(f"  Entregable: {t.get('entregable')}")
    print(f"  Desc: {t.get('desc')[:140]}...")
    print("-" * 70)
