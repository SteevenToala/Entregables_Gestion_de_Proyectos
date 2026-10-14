import re
import os

print("Starting fix_all_deliverables.py...")

# ==============================================================================
# 1. FIX GENERATE_FASE1_ENHANCED.PY
# ==============================================================================
f1_path = "generate_fase1_enhanced.py"
f1_txt = open(f1_path, encoding="utf-8").read()

# Fix Anexo 1 deliverable lines in Fase 1
f1_entregables = {
    "1.1": "Informe Técnico de Diagnóstico y Mapeo del Proceso As-Is",
    "1.2": "Matriz de Identificación de Actores y Mapa de Procesos SGC",
    "1.3": "Especificación de Requisitos de Software (SRS - IEEE 29148)",
    "1.4": "Documento de Línea Base del Alcance y Restricciones SGC",
    "1.5": "Catálogo de Reglas de Negocio y Validación Gates Lógicas",
    "1.6": "Caso de Negocio, Estudio de Retorno de Inversión y Project Charter",
    "1.7": "Cronograma Oficial del Proyecto y Estructura de Desglose del Trabajo",
    "1.8": "Expediente Técnico de Aprobación de Fase 1 e Hito Institucional",
}

for idx, title in f1_entregables.items():
    # Replace Entregable Oficial line in anx1_{idx}
    sub_idx = idx.split(".")[1]
    anx_var = f"anx1_{sub_idx}"
    pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?Entregable Oficial & )[^\\]+(\\\\)'
    f1_txt = re.sub(pat, rf'\g<1>{title} \g<2>', f1_txt)

# Fix Línea Base table in 1.8: replace rigid columns with flexible X columns
f1_txt = f1_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\bfseries}X|>{\centering\arraybackslash}m{3.0cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{1.5cm}|>{\centering\arraybackslash}m{3.0cm}|}"
)

# Remove .docx and .xlsx file extension mentions in 1.1
f1_txt = f1_txt.replace(r"(\texttt{.docx} y \texttt{.xlsx})", "de procesadores de texto y hojas de cálculo")

# Update figure width in Anexo 2 to 0.92\textwidth without height restriction
f1_txt = re.sub(r'\\includegraphics\[width=[0-9.]+.*?\]\{', r'\\includegraphics[width=0.92\\textwidth,keepaspectratio]{', f1_txt)

with open(f1_path, "w", encoding="utf-8") as f:
    f.write(f1_txt)
print("Fase 1 updated successfully.")

# ==============================================================================
# 2. FIX GENERATE_FASE2_ENHANCED.PY
# ==============================================================================
f2_path = "generate_fase2_enhanced.py"
f2_txt = open(f2_path, encoding="utf-8").read()

f2_entregables = {
    "2.1": "Documento de Especificación y Modelado de Casos de Uso UML",
    "2.2": "Documento de Arquitectura de Software (SAD - Modelo C4)",
    "2.3": "Especificación de Diagramas UML Dinámicos y de Dominio",
    "2.4": "Diseño Físico y Diccionario del Modelo Relacional",
    "2.5": "Especificación de Interfaces de Usuario y Design System",
    "2.6": "Infraestructura y Orquestación de Microservicios Contenerizados",
    "2.7": "Expediente Integral de Aprobación de Arquitectura de Software",
}

for idx, title in f2_entregables.items():
    sub_idx = idx.split(".")[1]
    anx_var = f"anx2_{sub_idx}"
    pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?Entregable Oficial & )[^\\]+(\\\\)'
    f2_txt = re.sub(pat, rf'\g<1>{title} \g<2>', f2_txt)

# Fix Línea Base table in 2.7
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\bfseries}X|>{\centering\arraybackslash}m{3.0cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{1.5cm}|>{\centering\arraybackslash}m{3.0cm}|}"
)

# Fix table in 2.3: espec_clases
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{1.8cm}|}"
)

# Fix table in 2.4: diccionario_datos and indices
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{2.5cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries\footnotesize}m{3.0cm}|>{\centering\arraybackslash}m{2.2cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}m{3.8cm}|}"
)
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{1.8cm}|X|X|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\centering\arraybackslash}m{1.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|}"
)

# In 2.4, remove raw code CHECK(horas >= 0) in text and tables
f2_txt = f2_txt.replace(r"\texttt{CHECK(horas >= 0)}, \texttt{CHECK(ponderacion <= 100)}", "validación horaria (0 a 40h) y ponderación total")
f2_txt = f2_txt.replace(r"(\texttt{CHECK horas >= 0}, \texttt{CHECK ponderacion <= 100})", "(validación de horas no negativas y ponderación acumulada al 100%)")

# Fix 2.6: docker_matrix table and commands
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|m{3.2cm}|c|m{2.5cm}|X|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.4cm}|>{\raggedright\arraybackslash\footnotesize}m{2.6cm}|>{\centering\arraybackslash\footnotesize}m{1.8cm}|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\raggedright\arraybackslash\footnotesize}X|}"
)
f2_txt = f2_txt.replace(r"\texttt{curl -f http://localhost:5173 || exit 1}", "Sondeo HTTP puerto 5173 (frontend activo)")
f2_txt = f2_txt.replace(r"\texttt{curl -f http://localhost:3000/api/health}", "Verificación /api/health con código 200")
f2_txt = f2_txt.replace(r"\texttt{pg\_isready -U sige\_user -d sige\_db}", "Comprobación de conexión con base de datos")
f2_txt = f2_txt.replace(r"\texttt{curl -f http://localhost:9000/minio/health/live}", "Chequeo de disponibilidad en puerto 9000")
f2_txt = f2_txt.replace(r"\texttt{curl -f http://localhost:8010/v2/languages}", "Consulta de catálogo de idiomas en puerto 8010")
f2_txt = f2_txt.replace(r"(\texttt{docker-compose.yml})", "mediante la especificación de orquestación de contenedores")

# Update figure width in Anexo 2
f2_txt = re.sub(r'\\includegraphics\[width=[0-9.]+.*?\]\{', r'\\includegraphics[width=0.92\\textwidth,keepaspectratio]{', f2_txt)

with open(f2_path, "w", encoding="utf-8") as f:
    f.write(f2_txt)
print("Fase 2 updated successfully.")

# ==============================================================================
# 3. FIX GENERATE_FASE3_ENHANCED.PY
# ==============================================================================
f3_path = "generate_fase3_enhanced.py"
f3_txt = open(f3_path, encoding="utf-8").read()

f3_entregables = {
    "3.1": "Definición de Esquema e Índices Relacionales en PostgreSQL 18",
    "3.2": "Módulo de Inicialización de Datos y Catálogos Maestros",
    "3.3": "Servicio de Autenticación, Control de Acceso y Gestión de Roles",
    "3.4": "Arquitectura del Cliente Web y Sistema de Navegación Institucional",
    "3.5": "Componente Asistente Guiado Modular (Wizard) para Planes de Trabajo",
    "3.6": "Editor Enriquecido de Texto con Persistencia Automática Asíncrona",
    "3.7": "Controladores de Persistencia y Transacciones ACID de Secciones",
    "3.8": "Expediente de Revisión del Incremento Sprint 2: Wizard y Persistencia",
    "3.9": "Componente Interactivo de la Matriz Dinámica de Actividades",
    "3.10": "Módulo de Validación Estricta y Compuertas Lógicas de Negocio",
    "3.11": "Servicio de Almacenamiento Seguro de Evidencias en MinIO S3",
    "3.12": "Expediente de Revisión del Incremento Sprint 3: Matriz y Evidencias S3",
    "3.13": "Módulo de Revisión Jerárquica y Cascada de Firmas Digitales",
    "3.14": "Capa de Asistencia Lingüística y Corrección de Redacción",
    "3.15": "Motor de Generación y Exportación Documental en Formato Institucional",
    "3.16": "Expediente Integral de Cierre de Construcción del Sistema Core",
}

for idx, title in f3_entregables.items():
    sub_idx = idx.split(".")[1]
    anx_var = f"anx3_{sub_idx}"
    pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?Entregable Oficial & )[^\\]+(\\\\)'
    f3_txt = re.sub(pat, rf'\g<1>{title} \g<2>', f3_txt)

# Fix Línea Base table in 3.8, 3.12, 3.16
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\bfseries}X|>{\centering\arraybackslash}m{3.0cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{1.5cm}|>{\centering\arraybackslash}m{3.0cm}|}"
)

# Eliminate all code file names across Fase 3
file_replaces = {
    r"\texttt{schema.sql}": "los scripts de definición DDL",
    r"\texttt{seed.js}": "el componente de inicialización de datos",
    r"\texttt{validation.middleware.js}": "el middleware de validación",
    r"\texttt{minio.service.js}": "el servicio de almacenamiento S3",
    r"\texttt{documentos.controller.js}": "el controlador de documentos",
    r"\texttt{secciones.controller.js}": "el controlador de secciones",
    r"\texttt{export.service.js}": "el servicio de exportación",
    r"\texttt{grammar.service.js}": "el servicio de corrección ortográfica",
    r"\texttt{LoginView.jsx}": "la vista de autenticación",
    r"\texttt{DashboardView.jsx}": "el panel principal",
    r"\texttt{PlanesListView.jsx}": "la bandeja de planes",
    r"\texttt{PlanEditorWizard.jsx}": "el componente de asistente guiado",
    r"\texttt{RichTextEditor.jsx}": "el componente de edición enriquecida",
    r"\texttt{MatrizActividadesTable.jsx}": "la tabla dinámica de actividades",
    r"\texttt{RevisionComiteView.jsx}": "el panel de revisión colegiada",
    r"\texttt{AdminConfigView.jsx}": "el módulo de configuración administrativa",
    r"\texttt{AuthContext.jsx}": "el contexto global de sesión",
    r"\texttt{docker-compose.yml}": "la especificación de contenedores Docker",
}
for old_f, new_f in file_replaces.items():
    f3_txt = f3_txt.replace(old_f, new_f)

# Fix 3.1: Table indices_ddl - remove raw SQL code in cells
f3_txt = f3_txt.replace(
    r"\texttt{chk\_estado\_valido} & \texttt{CHECK (estado IN ('Borrador', 'En Revision', 'Observado', 'Aprobado'))} & Ciclo de vida estricto del plan P7-T1. \\",
    r"Restricción de Estados & Estados permitidos: Borrador, En Revisión, Observado, Aprobado & Ciclo de vida estricto del plan P7-T1. \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{chk\_horas\_rango} & \texttt{CHECK (horas >= 0 AND horas <= 40)} & Previene carga horaria irreal. \\",
    r"Rango Horario Semanal & Carga horaria positiva entre 0 y 40 horas semanales & Previene carga horaria irreal. \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{chk\_pond\_rango} & \texttt{CHECK (ponderacion >= 0.00 AND ponderacion <= 100.00)} & Integridad de sumatoria al 100\%. \\",
    r"Ponderación de Avance & Ponderación porcentual entre 0.00\% y 100.00\% & Integridad de sumatoria al 100\%. \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{idx\_plan\_doc\_per} & Índice B-Tree en \texttt{(fk\_docente, fk\_periodo)} & Aceleración de bandeja docente. \\",
    r"Índice Docente-Periodo & B-Tree sobre docente y ciclo académico & Aceleración de bandeja docente. \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{idx\_sec\_jsonb} & Índice GIN en \texttt{contenido\_jsonb} & Búsqueda rápida de texto enriquecido. \\",
    r"Índice Estructurado JSONB & GIN sobre contenido de texto estructurado & Búsqueda rápida de texto enriquecido. \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{idx\_firma\_sec} & B-Tree UNIQUE en \texttt{(fk\_plan, orden)} & Garantiza secuencia 1 $\to$ 2 $\to$ 3. \\",
    r"Índice de Firma Única & B-Tree exclusivo sobre plan y orden secuencial & Garantiza secuencia 1 $\to$ 2 $\to$ 3. \\"
)

# Fix 3.1: Anexo 2 Table - replace raw SQL error messages
f3_txt = f3_txt.replace(
    r"P1 - Horas Negativas & Inserción con \texttt{horas = -5} en \texttt{actividades\_matriz} & \texttt{ERROR: violates check constraint chk\_horas\_rango} & SUPERADA \\",
    r"Validación Carga Negativa & Ensayo de asignación de -5 horas a la actividad & Rechazo automático por compuerta horaria & CONFORME \\"
)
f3_txt = f3_txt.replace(
    r"P2 - Ponderación $>100$ & Inserción con \texttt{ponderacion = 120.00} en \texttt{actividades\_matriz} & \texttt{ERROR: violates check constraint chk\_pond\_rango} & SUPERADA \\",
    r"Validación Ponderación Excedida & Ensayo de asignación de 120\% a la actividad & Rechazo automático por límite de 100\% & CONFORME \\"
)
f3_txt = f3_txt.replace(
    r"P3 - Borrado Accidental & Eliminación de usuario con planes activos & \texttt{ERROR: violates foreign key constraint (RESTRICT)} & SUPERADA \\",
    r"Integridad en Cascada & Intento de supresión de usuario con expedientes activos & Bloqueo estricto por integridad referencial & CONFORME \\"
)
f3_txt = f3_txt.replace(
    r"P4 - Búsqueda JSONB & Consulta con operador \texttt{@>} sobre \texttt{contenido\_jsonb} & Retorno en 2.4 ms utilizando índice GIN & SUPERADA \\",
    r"Búsqueda Estructurada & Consulta de contenido enriquecido en secciones & Tiempo de respuesta óptimo de 2.4 ms & CONFORME \\"
)

# Fix 3.6: Table tiptap_extensions - simplify and wrap
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{3.0cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|}"
)
f3_txt = f3_txt.replace(r"\texttt{@tiptap/starter-kit}", "Módulo Base TipTap")
f3_txt = f3_txt.replace(r"\texttt{@tiptap/extension-heading}", "Módulo de Encabezados")
f3_txt = f3_txt.replace(r"\texttt{@tiptap/extension-table}", "Módulo de Tablas")
f3_txt = f3_txt.replace(r"\texttt{@tiptap/extension-placeholder}", "Módulo Guía Visual")
f3_txt = f3_txt.replace(r"\texttt{@tiptap/extension-character-count}", "Módulo de Conteo Léxico")

# Fix 3.6: Anexo 2 table - wrap payloads and outputs
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|X|c|c|}",
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}"
)

# Fix 3.7: Table of endpoints
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|m{3.5cm}|m{2.5cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}m{2.8cm}|>{\centering\arraybackslash\footnotesize}m{2.0cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.0cm}|}"
)
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|m{2.5cm}|m{3.5cm}|c|c|}",
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}m{2.5cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\centering\arraybackslash\footnotesize}m{2.2cm}|}"
)

# Fix 3.11: Anexo 2 table - remove file names and 64-char hashes
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|m{3.0cm}|m{2.0cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|>{\centering\arraybackslash}m{1.8cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.4cm}|}"
)
f3_txt = f3_txt.replace(
    r"EV-01 & \texttt{silabo\_ing\_soft\_2026.pdf} & 2.4 MB & \texttt{e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855} & VERIFICADA \\",
    r"EV-01 & Sílabo Institucional Aprobado & 2.4 MB & Huella SHA-256 calculada y validada en almacenamiento & CONFORME \\"
)
f3_txt = f3_txt.replace(
    r"EV-02 & \texttt{acta\_tutorias\_sep.pdf} & 840 KB & \texttt{d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35} & VERIFICADA \\",
    r"EV-02 & Acta de Tutorías y Seguimiento & 840 KB & Huella SHA-256 calculada y validada en almacenamiento & CONFORME \\"
)
f3_txt = f3_txt.replace(
    r"EV-03 & \texttt{informe\_avance\_investig.pdf} & 5.1 MB & \texttt{4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a} & VERIFICADA \\",
    r"EV-03 & Informe de Avance de Investigación & 5.1 MB & Huella SHA-256 calculada y validada en almacenamiento & CONFORME \\"
)

# Update figure width in Anexo 2
f3_txt = re.sub(r'\\includegraphics\[width=[0-9.]+.*?\]\{', r'\\includegraphics[width=0.92\\textwidth,keepaspectratio]{', f3_txt)

with open(f3_path, "w", encoding="utf-8") as f:
    f.write(f3_txt)
print("Fase 3 updated successfully.")

# ==============================================================================
# 4. FIX GENERATE_FASE4_ENHANCED.PY
# ==============================================================================
f4_path = "generate_fase4_enhanced.py"
f4_txt = open(f4_path, encoding="utf-8").read()

f4_entregables = {
    "4.1": "Suite Automatizada de Pruebas Unitarias de Backend",
    "4.2": "Informe de Auditoría de Seguridad y Pruebas de Integración OWASP",
    "4.3": "Informe de Pruebas de Interfaz, Accesibilidad WCAG y Diseño Adaptable",
}

for idx, title in f4_entregables.items():
    sub_idx = idx.split(".")[1]
    anx_var = f"anx4_{sub_idx}"
    pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?Entregable Oficial & )[^\\]+(\\\\)'
    f4_txt = re.sub(pat, rf'\g<1>{title} \g<2>', f4_txt)

# Fix Línea Base table in 4.3
f4_txt = f4_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\bfseries}X|>{\centering\arraybackslash}m{3.0cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{1.5cm}|>{\centering\arraybackslash}m{3.0cm}|}"
)

# Fix contrast table in 4.3: replace rigid columns with relative X
f4_txt = f4_txt.replace(
    r"\begin{tabularx}{\textwidth}{|m{3.2cm}|c|c|c|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.0cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\centering\arraybackslash\footnotesize}m{2.4cm}|}"
)

# In 4.2 Anexo 2: add consola real de npm test/auditoría
f4_txt = f4_txt.replace(
    r"\includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_03_seguridad_jwt_rbac.png}",
    r"\includegraphics[width=0.92\textwidth,keepaspectratio]{images/f4_01_consola_npm_test.png}"
)

# Update figure width in Anexo 2
f4_txt = re.sub(r'\\includegraphics\[width=[0-9.]+.*?\]\{', r'\\includegraphics[width=0.92\\textwidth,keepaspectratio]{', f4_txt)

with open(f4_path, "w", encoding="utf-8") as f:
    f.write(f4_txt)
print("Fase 4 updated successfully.")

print("All generator scripts updated!")
