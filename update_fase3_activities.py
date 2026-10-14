# update_fase3_activities.py
import re
from fase3_activities_part1 import ACTIVITIES_F3_PART1
from fase3_activities_part2 import ACTIVITIES_F3_PART2

ALL_ACTIVITIES = {**ACTIVITIES_F3_PART1, **ACTIVITIES_F3_PART2}

with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace activities section in each b3_i
for i in range(1, 17):
    new_act = ALL_ACTIVITIES[i].strip()
    # Pattern matching from \section{Descripción de actividades} up to \begin{table}
    pattern = rf'(\\section\{{Descripci[oó]n de actividades\}}.*?)(\\begin\{{table\}})'
    
    # We find within b3_{i}
    body_pattern = rf'(b3_{i}\s*=\s*r""".*?""")'
    bm = re.search(body_pattern, content, flags=re.DOTALL)
    if not bm:
        print(f"ERROR: Could not find b3_{i} in generate_fase3_enhanced.py!")
        continue
    
    body_str = bm.group(1)
    # Replace in body_str
    sub_pattern = r'\\section\{Descripci[oó]n de actividades\}.*?(?=\\begin\{table\})'
    new_body_str = re.sub(
        sub_pattern,
        lambda m, na=new_act: na + "\n",
        body_str,
        count=1,
        flags=re.DOTALL
    )
    
    # Replace the body in content
    content = re.sub(
        body_pattern,
        lambda m, nb=new_body_str: nb,
        content,
        count=1,
        flags=re.DOTALL
    )
    print(f"Updated b3_{i} activities description successfully.")

# Also clean any remaining "Paso X" in Wizard tables or text
content = content.replace("Paso 1 & Datos Generales", "Etapa 1 & Configuración Inicial")
content = content.replace("Paso 2 & Docencia y Horas", "Etapa 2 & Carga Horaria y Docencia")
content = content.replace("Paso 3 & Matriz Dinámica", "Etapa 3 & Matriz de Actividades")
content = content.replace("Paso 4 & Medios de Verificación", "Etapa 4 & Custodia de Evidencias")
content = content.replace("Paso 5 & Revisión y Firmas", "Etapa 5 & Revisión y Firmas")
content = re.sub(r'\\textbf\{Paso\s*\d+:\s*', r'\\textbf{', content, flags=re.I)
content = re.sub(r'\bpaso\s*1\b', 'etapa inicial', content, flags=re.I)
content = re.sub(r'\bpaso\s*2\b', 'etapa descriptiva', content, flags=re.I)
content = re.sub(r'\bpaso\s*3\b', 'etapa matricial', content, flags=re.I)
content = re.sub(r'\bpaso\s*4\b', 'etapa de evidencias', content, flags=re.I)
content = re.sub(r'\bpaso\s*5\b', 'etapa de firmas', content, flags=re.I)

with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
    f.write(content)

print("generate_fase3_enhanced.py bodies updated with rich activities!")
