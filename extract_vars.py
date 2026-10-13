import re
import json

def extract_js_var(file_path, var_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = rf'(?:const|let|var)\s+{var_name}\s*=\s*(\[.*?\]|\{{.*?\}});'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        js_str = m.group(1)
        # Use node to parse js_str safely if valid JS
        return js_str
    return None

js_edt = extract_js_var(r'../AlcanceInforme/Tablero_EDT_Trello.html', 'EDT_TASKS')
if js_edt:
    with open('edt_tasks_raw.js', 'w', encoding='utf-8') as out:
        out.write("const tasks = " + js_edt + ";\nconsole.log(JSON.stringify(tasks));")
    print("Saved edt_tasks_raw.js")

js_tasks = extract_js_var(r'../AlcanceInforme/Visor_Fases_y_Normas_SIGE.html', 'tasks')
if js_tasks:
    with open('visor_tasks_raw.js', 'w', encoding='utf-8') as out:
        out.write("const tasks = " + js_tasks + ";\nconsole.log(JSON.stringify(tasks));")
    print("Saved visor_tasks_raw.js")
