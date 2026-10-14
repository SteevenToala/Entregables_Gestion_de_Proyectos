# patch_fase2_trello.py
import re

with open("generate_fase2_enhanced.py", "r", encoding="utf-8") as f:
    c = f.read()

# Replace Cobertura in lines 54 and 711
c = re.sub(
    r"Verificaci.n de cobertura con la matriz de trazabilidad RF-01 a RF-24\.",
    "Verificación de correspondencia funcional con los requisitos RF-01 a RF-24.",
    c
)
c = re.sub(
    r"Verificaci.n de cobertura de los requisitos del sistema",
    "Verificación de correspondencia y consistencia de los requisitos del sistema",
    c
)

# Replace in 2.7
c = re.sub(
    r"Auditar el cumplimiento del 100\\% de las tareas t.cnicas asignadas a la Fase 2 en el Tablero Trello\.",
    "Auditar el cumplimiento del 100\\% de las especificaciones y modelos arquitectónicos de la Fase 2.",
    c
)

c = re.sub(
    r"Asimismo, se cotej. el estado de cada tarjeta en el Tablero Kanban de Trello frente a los artefactos compilados, certificando el 100\\% de avance f.sico y cronol.gico\.",
    "Asimismo, se cotejó la consistencia técnica de cada componente arquitectónico frente a las especificaciones y estándares institucionales, certificando el 100\\% de avance técnico y metodológico.",
    c
)

# Replace Trello figures in 2.7
new_fig_arch = r"""\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/s2_07_consolidado_s2.png}
    \caption{Consolidado Arquitectónico y Vista General de Modelado del Sistema SIGE.}
    \label{fig:consolidado_fase2}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_02_contenedores_c4.png}
    \caption{Diagrama C4 de Contenedores Aprobado como Línea Base para la Fase de Construcción.}
    \label{fig:c4_baseline_fase2}
\end{figure}
\FloatBarrier"""

c = re.sub(r'\\begin\{figure\}\[H\]\s*\\centering\s*\\includegraphics\[width=0\.88\\textwidth,height=6\.0cm,keepaspectratio\]\{images/trello_tablero_captura_real\.png\}.*?\\end\{figure\}\s*\\FloatBarrier\s*\\begin\{figure\}\[H\]\s*\\centering\s*\\includegraphics\[width=0\.88\\textwidth,height=5\.8cm,keepaspectratio\]\{images/trello_gantt_cronograma\.png\}.*?\\end\{figure\}\s*\\FloatBarrier',
           lambda m: new_fig_arch, c, flags=re.DOTALL)

# Replace Cobertura total in 2.7 tables
c = re.sub(
    r"Cobertura total de los 24 RF y actores del SGC bajo notaci.n OMG UML 2\.5\.1\.",
    "Mapeo formal y verificación de los 24 RF y actores del SGC bajo notación OMG UML 2.5.1.",
    c
)

with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c)

print("generate_fase2_enhanced.py patched successfully!")
