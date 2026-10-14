# update_fase3_deep.py
import re
from fase3_annexes_part1 import PART1_ANNEXES
from fase3_annexes_part2 import PART2_ANNEXES

ALL_ANNEXES = {**PART1_ANNEXES, **PART2_ANNEXES}

with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up b3_16 of any Trello and Cobertura references
content = content.replace(
    r"certificando la cobertura total de los requerimientos funcionales del SGC.",
    r"certificando la correspondencia total con los requerimientos funcionales del SGC."
)
content = re.sub(
    r"Auditar el cumplimiento de las 16 tareas t.cnicas que integran la Fase 3 en el Tablero Trello y Cronograma Gantt\.",
    r"Auditar el cumplimiento y funcionamiento operativo de los 16 componentes técnicos que integran la Fase 3.",
    content
)
content = content.replace(
    r"\item \textbf{Política de Cobertura Total de Requisitos:} Todas y cada una de las 24 Historias de Usuario",
    r"\item \textbf{Política de Completitud de Requisitos:} Todas y cada una de las 24 Historias de Usuario"
)
content = re.sub(
    r"\\begin\{figure\}\[H\]\s*\\centering\s*\\includegraphics\[width=0\.88\\textwidth,height=5\.8cm,keepaspectratio\]\{images/trello_gantt_cronograma\.png\}.*?\\caption\{Cronograma Gantt en MS Project evidenciando el Cumplimiento al 100\\% del Hito 5\.\}\s*\\label\{fig:hito5_gantt\}\s*\\end\{figure\}\s*\\FloatBarrier",
    r"""\\begin{figure}[H]
    \\centering
    \\includegraphics[width=0.88\\textwidth,height=5.8cm,keepaspectratio]{images/s4_03_cascada_firmas.png}
    \\caption{Flujo de Cascada de Firmas Digitales y Verificación Criptográfica Implementada en el Sistema Core.}
    \\label{fig:hito5_firmas}
\\end{figure}
\\FloatBarrier""",
    content,
    flags=re.DOTALL
)

# 2. Replace all 16 annexes
for i in range(1, 17):
    new_anx = ALL_ANNEXES[i].strip()
    pattern = rf'(anx3_{i}\s*=\s*r""".*?""")'
    match = re.search(pattern, content, flags=re.DOTALL)
    if not match:
        print(f"ERROR: Could not find anx3_{i} in generate_fase3_enhanced.py!")
    else:
        # Use lambda replacement to avoid any regex escape errors with backslashes
        replacement = f'anx3_{i} = r"""\n{new_anx}\n"""'
        content = re.sub(
            pattern,
            lambda m, rep=replacement: rep,
            content,
            count=1,
            flags=re.DOTALL
        )
        print(f"Replaced anx3_{i} successfully.")

# 3. Save updated file
with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
    f.write(content)

print("\ngenerate_fase3_enhanced.py successfully updated with all 16 deep technical annexes!")
