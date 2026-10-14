# clean_f3_annexes_pasos.py
import re

for filename in ["fase3_annexes_part1.py", "fase3_annexes_part2.py"]:
    with open(filename, "r", encoding="utf-8") as f:
        c = f.read()

    # Replace \textbf{Paso X: with descriptive titles
    c = c.replace(r"\item \textbf{Paso 1: Datos Generales y Carga Horaria:}", r"\item \textbf{Configuración Inicial de Carrera y Carga Horaria:}")
    c = c.replace(r"\item \textbf{Paso 2: Justificación y Objetivos de la Labor:}", r"\item \textbf{Redacción Descriptiva y Objetivos Académicos:}")
    c = c.replace(r"\item \textbf{Paso 3: Matriz Dinámica de Actividades:}", r"\item \textbf{Distribución Semanal en Matriz Dinámica:}")
    c = c.replace(r"\item \textbf{Paso 4: Custodia de Respaldos y Evidencias:}", r"\item \textbf{Custodia Digital de Evidencias en MinIO:}")
    c = c.replace(r"\item \textbf{Paso 5: Revisión General y Cascada de Firmas:}", r"\item \textbf{Revisión General y Legalización con Firmas:}")

    # General replacements of remaining Paso X
    c = re.sub(r'\\textbf\{Paso\s*\d+:\s*', r'\\textbf{', c, flags=re.I)
    c = re.sub(r'Paso 1', 'Etapa Inicial', c)
    c = re.sub(r'Paso 2', 'Etapa Descriptiva', c)
    c = re.sub(r'Paso 3', 'Etapa Matricial', c)
    c = re.sub(r'Paso 4', 'Etapa de Evidencias', c)
    c = re.sub(r'Paso 5', 'Etapa de Firmas', c)
    c = re.sub(r'pasos 1 y 2', 'las etapas inicial y descriptiva', c, flags=re.I)
    c = re.sub(r'pasos 3, 4 y 5', 'las etapas matricial, de evidencias y de firmas', c, flags=re.I)
    c = re.sub(r'5 pasos lógicos', '5 etapas modulares', c, flags=re.I)
    c = re.sub(r'5 pasos secuenciales', '5 etapas secuenciales', c, flags=re.I)
    c = re.sub(r'5 pasos con datos', '5 etapas con datos', c, flags=re.I)
    c = re.sub(r'10 pasos', '10 etapas operativas', c, flags=re.I)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(c)

print("fase3_annexes_part1.py and fase3_annexes_part2.py cleaned of Paso X!")
