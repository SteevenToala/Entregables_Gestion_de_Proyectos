# update_fase3_deep_v2.py
# -*- coding: utf-8 -*-
"""
Script para:
1. Eliminar cualquier residuo de 'paso' / 'pasos' en fase3_activities_part1.py, fase3_annexes_part1.py, fase3_annexes_part2.py y generate_fase3_enhanced.py.
2. Inyectar las actividades y anexos actualizados en generate_fase3_enhanced.py.
"""

import re

print(">>> Limpiando fase3_activities_part1.py...")
with open("fase3_activities_part1.py", "r", encoding="utf-8") as f:
    act1 = f.read()

act1 = act1.replace("gestiona el paso activo", "gestiona la etapa activa")
act1 = act1.replace("Cada paso completado se tiñe de verde", "Cada etapa completada se tiñe de verde")
act1 = act1.replace("facilitar la navegación entre pasos", "facilitar la navegación entre etapas")

with open("fase3_activities_part1.py", "w", encoding="utf-8") as f:
    f.write(act1)


print(">>> Limpiando fase3_annexes_part1.py...")
with open("fase3_annexes_part1.py", "r", encoding="utf-8") as f:
    anx1 = f.read()

anx1 = anx1.replace("constituyó el paso indispensable", "constituyó el hito indispensable")
anx1 = anx1.replace("# 3.5 Implementación del Asistente por Pasos (Wizard)", "# 3.5 Implementación del Asistente Modular (Wizard)")
anx1 = anx1.replace('El botón de navegación "Siguiente Paso"', 'El botón de navegación "Siguiente Etapa"')
anx1 = anx1.replace("Asistente Modular por Pasos (Wizard)", "Asistente Modular (Wizard)")
anx1 = anx1.replace('P3: Navegación Reversa & Clic en "Paso Anterior" desde el Etapa Matricial hacia el Etapa Descriptiva',
                    'P3: Navegación Reversa & Clic en "Etapa Anterior" desde la Etapa Matricial hacia la Etapa Descriptiva')
anx1 = anx1.replace('Clic en "Paso Anterior"', 'Clic en "Etapa Anterior"')
anx1 = anx1.replace("asistente interactivo por pasos", "asistente interactivo modular")
anx1 = anx1.replace("facilitar la navegación entre pasos", "facilitar la navegación entre etapas")
anx1 = anx1.replace("Recorrido de los 5 etapas", "Recorrido de las 5 etapas modulares")

with open("fase3_annexes_part1.py", "w", encoding="utf-8") as f:
    f.write(anx1)


print(">>> Limpiando fase3_annexes_part2.py...")
with open("fase3_annexes_part2.py", "r", encoding="utf-8") as f:
    anx2 = f.read()

anx2 = anx2.replace("en el Etapa Matricial", "en la Etapa Matricial")

with open("fase3_annexes_part2.py", "w", encoding="utf-8") as f:
    f.write(anx2)


print(">>> Actualizando generate_fase3_enhanced.py...")
with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
    c = f.read()

# Reemplazos de "paso/pasos" en generate_fase3_enhanced.py
c = c.replace("constituyó el paso indispensable", "constituyó el hito indispensable")
c = c.replace("Llenado guiado en 5 pasos", "Llenado guiado en 5 etapas modulares")
c = c.replace("Wizard modular guiado por pasos", "Wizard modular por etapas")
c = c.replace("navegación secuencial en 5 pasos", "navegación secuencial en 5 etapas")
c = c.replace("Estructura del Wizard con 5 pasos:", "Estructura del Wizard en 5 etapas:")
c = c.replace(r"\item \textbf{Paso Bloqueante:}", r"\item \textbf{Etapa Bloqueante:}")
c = c.replace("no se puede acceder al paso de firmas", "no se puede acceder a la etapa de firmas")
c = c.replace("Cada paso insatisfecho muestra un resumen", "Cada etapa insatisfecha muestra un resumen")
c = c.replace("Validación de Pasos y Transiciones", "Validación de Etapas y Transiciones")
c = c.replace(r"\textbf{Paso} & \textbf{Nombre de Pestaña}", r"\textbf{Etapa} & \textbf{Nombre de Pestaña}")
c = c.replace("estructura técnica de los 5 pasos del Wizard", "estructura técnica de las 5 etapas del Wizard")
c = c.replace('El botón de navegación "Siguiente Paso"', 'El botón de navegación "Siguiente Etapa"')
c = c.replace("Asistente Modular por Pasos", "Asistente Modular")
c = c.replace('Clic en "Paso Anterior"', 'Clic en "Etapa Anterior"')
c = c.replace("asistente interactivo por pasos", "asistente interactivo modular")
c = c.replace("gestiona el paso activo", "gestiona la etapa activa")
c = c.replace("Cada paso completado se tiñe de verde", "Cada etapa completada se tiñe de verde")
c = c.replace("facilitar la navegación entre pasos", "facilitar la navegación entre etapas")
c = c.replace("Recorrido de los 5 etapas", "Recorrido de las 5 etapas modulares")
c = c.replace("No se autoriza el paso al Sprint 4", "No se autoriza el avance al Sprint 4")
c = c.replace("guiado en 5 pasos con barra", "guiado en 5 etapas con barra")
c = c.replace("en el Etapa Matricial", "en la Etapa Matricial")

with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c)

print("generate_fase3_enhanced.py actualizado con éxito.")
