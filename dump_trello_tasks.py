import json

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-16') as f:
            return json.load(f)
    except:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

edt = load_json('edt_tasks.json')
with open('trello_tasks_dump.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total tasks in EDT_TASKS: {len(edt)}\n\n")
    for t in edt:
        code = t.get('code', t.get('id', 'N/A'))
        title = t.get('title', 'N/A')
        phase = t.get('phase', 'N/A')
        phaseName = t.get('phaseName', 'N/A')
        is_sum = t.get('isSummary', False)
        deliv = t.get('deliverable', 'N/A')
        dates = t.get('dates', 'N/A')
        pct = t.get('percentDone', 0)
        desc = t.get('description', 'N/A')
        out.write(f"ID: {t.get('id')} | CODE: {code} | SUMMARY: {is_sum}\n")
        out.write(f"PHASE: {phase} ({phaseName})\n")
        out.write(f"TITLE: {title}\n")
        out.write(f"DATES: {dates} | %DONE: {pct}%\n")
        out.write(f"DELIVERABLE: {deliv}\n")
        out.write(f"DESC: {desc}\n")
        out.write("-" * 80 + "\n")

print("Dumped to trello_tasks_dump.txt successfully!")
