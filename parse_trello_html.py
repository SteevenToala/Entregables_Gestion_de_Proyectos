import re

html_path = r'../AlcanceInforme/Tablero_EDT_Trello.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

vars_found = re.findall(r'(?:const|let|var)\s+(\w+)\s*=\s*', content)
print("Variables in Tablero_EDT_Trello.html:", vars_found)

# Also check Diagrama_Fases_SIGE.html and Visor_Fases_y_Normas_SIGE.html
for other in ['Diagrama_Fases_SIGE.html', 'Visor_Fases_y_Normas_SIGE.html', 'Presentacion_Informe_del_Alcance.html']:
    p = f'../AlcanceInforme/{other}'
    try:
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        v = re.findall(r'(?:const|let|var)\s+(\w+)\s*=\s*', c)
        print(f"Variables in {other}:", v)
    except Exception as e:
        print(f"Error reading {other}:", e)
