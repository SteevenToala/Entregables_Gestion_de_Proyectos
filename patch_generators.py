# -*- coding: utf-8 -*-
"""
Script to patch all generator files with:
1. Relative proportional X columns for all tables, completely eliminating overflows.
2. Removal of all remaining file extensions (.docx, .pdf, .env, Dockerfile, etc.).
3. Replacement of raw code / SQL in tables with professional, structured text descriptions.
"""

import re
import os

def patch_fase1():
    filepath = "generate_fase1_enhanced.py"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Eliminate .docx reference in 1.1
    text, n = re.subn(
        r'M.ltiples archivos \\texttt\{\.docx\} \(\\textit\{v1, final, corregido\}\)',
        r'Múltiples versiones no controladas en procesadores ofimáticos (\\textit{versión 1, final, corregido})',
        text
    )
    print(f"Fase 1 .docx replaced: {n}")

    # 2. General Checklist table replacement
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3. General Trello table replacement
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 4. Custom tables in Fase 1
    # 1.1:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{2.5cm}|X|m{3.5cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    # 1.2:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|c|c|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.5\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.0cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    # 1.3:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    # 1.4:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|X|m{3.2cm}|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    # 1.5:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    # 1.6:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{4.0cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    # 1.7:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|m{2.5cm}|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.5cm}|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    # 1.8:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("generate_fase1_enhanced.py patched successfully.")

def patch_fase2():
    filepath = "generate_fase2_enhanced.py"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Checklist & Trello tables
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.1:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.2:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|c|m{2.2cm}|m{2.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.3:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{1.8cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.0cm}|X|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.4: Clean tables and remove SQL / raw monospace overflows
    old_diccionario_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Clave Primaria} & \textbf{Claves Forneas y Restricciones Principales} & \textbf{Propsito SGC} \\
\hline
\texttt{usuarios} & \texttt{id} (UUID) & \texttt{email} (UNIQUE, CHECK institucional), \texttt{password\_hash} & Catlogo de docentes y administradores. \\
\hline
\texttt{roles} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE: DOCENTE, COORD\_AREA, COORD\_CARRERA) & Perfiles de acceso institucional RBAC. \\
\hline
\texttt{usuario\_roles} & \texttt{id} (UUID) & \texttt{fk\_usuario} $\to$ \texttt{usuarios}, \texttt{fk\_rol} $\to$ \texttt{roles} & Asignacin de mltiples roles a usuarios. \\
\hline
\texttt{periodos\_academicos} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE), \texttt{CHECK(fecha\_fin > fecha\_inicio)} & Ciclos semestrales institucionales UTA. \\
\hline
\texttt{carreras} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE), \texttt{nombre}, \texttt{facultad} & Catlogo de carreras pertenecientes a FISEI. \\
\hline
\texttt{planes\_docente} & \texttt{id} (UUID) & \texttt{fk\_docente}, \texttt{fk\_periodo}, \texttt{fk\_carrera}, \texttt{CHECK(estado)} & Cabecera principal del plan de trabajo P7-T1. \\
\hline
\texttt{secciones\_documento} & \texttt{id} (UUID) & \texttt{fk\_plan} $\to$ \texttt{planes\_docente}, \texttt{contenido\_jsonb} & Contenido enriquecido de secciones del plan. \\
\hline
\texttt{actividades\_matriz} & \texttt{id} (UUID) & \texttt{fk\_plan}, validacin horaria (0 a 40h) y ponderacin total & Filas dinmicas de la matriz SGC. \\
\hline
\texttt{evidencias\_adjuntas} & \texttt{id} (UUID) & \texttt{fk\_actividad}, \texttt{url\_s3}, \texttt{hash\_sha256} (CHAR 64) & Metadatos de archivos PDF en MinIO. \\
\hline
\texttt{observaciones\_comite} & \texttt{id} (UUID) & \texttt{fk\_plan}, \texttt{fk\_usuario}, \texttt{fk\_seccion}, \texttt{resuelto} (BOOLEAN) & Correcciones y observaciones de revisin. \\
\hline
\texttt{firmas\_documento} & \texttt{id} (UUID) & \texttt{fk\_plan}, \texttt{fk\_firmante}, \texttt{hash\_firma}, \texttt{orden} (1, 2, 3) & Registro cronolgico e inmutable de firmas. \\
\hline
\texttt{auditoria\_logs} & \texttt{id} (UUID) & \texttt{fk\_usuario}, \texttt{accion}, \texttt{ip\_origen}, \texttt{created\_at} & Bitcora de seguridad y trazabilidad. \\
\hline
\texttt{notificaciones} & \texttt{id} (UUID) & \texttt{fk\_usuario}, \texttt{titulo}, \texttt{mensaje}, \texttt{leido} (BOOLEAN) & Avisos de cambios de estado y revisiones. \\
\hline
\end{tabularx}"""

    new_diccionario_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Clave Primaria} & \textbf{Claves Foráneas y Restricciones Principales} & \textbf{Propósito SGC} \\
\hline
usuarios & id (UUID) & Correo único institucional, clave encriptada & Catálogo de docentes y administradores. \\
\hline
roles & id (UUID) & Perfiles de acceso institucional RBAC & Perfiles de acceso institucional. \\
\hline
usuario\allowbreak\_roles & id (UUID) & Asociación docente con perfiles asignados & Asignación de múltiples roles a usuarios. \\
\hline
periodos\allowbreak\_academicos & id (UUID) & Código semestral, coherencia de fechas vigentes & Ciclos semestrales institucionales UTA. \\
\hline
carreras & id (UUID) & Código único, nombre oficial, facultad FISEI & Catálogo de carreras de la facultad. \\
\hline
planes\allowbreak\_docente & id (UUID) & Docente, periodo, carrera, validación de estado & Cabecera principal del plan de trabajo P7-T1. \\
\hline
secciones\allowbreak\_documento & id (UUID) & Asociación al plan, contenido en formato estructurado & Contenido enriquecido de secciones del plan. \\
\hline
actividades\allowbreak\_matriz & id (UUID) & Asociación al plan, control de horas y ponderación & Filas dinámicas de la matriz SGC. \\
\hline
evidencias\allowbreak\_adjuntas & id (UUID) & Asociación a actividad, enlace seguro, firma SHA-256 & Metadatos de documentos probatorios en MinIO. \\
\hline
observaciones\allowbreak\_comite & id (UUID) & Asociación al plan, evaluador, sección, estado & Correcciones y observaciones de revisión. \\
\hline
firmas\allowbreak\_documento & id (UUID) & Asociación al plan, firmante, firma digital, turno & Registro cronológico e inmutable de firmas. \\
\hline
auditoria\allowbreak\_logs & id (UUID) & Usuario, acción efectuada, dirección de red, fecha & Bitácora de seguridad y trazabilidad. \\
\hline
notificaciones & id (UUID) & Usuario destinatario, título, mensaje, estado & Avisos de cambios de estado y revisiones. \\
\hline
\end{tabularx}"""

    # Match and replace dictionary table robustly
    if old_diccionario_table in text:
        text = text.replace(old_diccionario_table, new_diccionario_table)
        print("Replaced old_diccionario_table directly!")
    else:
        # Regex replacement if encoding difference
        pattern = re.compile(r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.8\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.5\\hsize[^}]+\}X\|.*?\\end\{tabularx\}', re.DOTALL)
        text, n = pattern.subn(lambda m: new_diccionario_table, text, count=1)
        print(f"Replaced diccionario table via regex: {n}")

    # 2.4 Table 2 (Indices)
    old_indices_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del ndice} & \textbf{Tabla Objetivo} & \textbf{Columnas Indexadas y Tipo de ndice} & \textbf{Propsito} \\
\hline
ndice Docente-Periodo & planes\_docente & B-Tree sobre docente y periodo acadmico & Bsqueda rpida de expedientes activos. \\
\hline
ndice Actividades-Plan & actividades\_matriz & B-Tree sobre clave fornea del plan & Agrupacin de actividades de la matriz. \\
\hline
ndice Estructurado GIN & secciones\_documento & GIN optimizado sobre contenido estructurado & Bsqueda rpida de texto en secciones. \\
\hline
ndice de Firma Secuencial & firmas\_documento & B-Tree UNIQUE sobre plan y orden & Garantiza secuencia estricta de firmas. \\
\hline
ndice Huella Digital & evidencias\_adjuntas & B-Tree sobre huella criptogrfica SHA-256 & Prevencin de duplicados de archivos. \\
\hline
\end{tabularx}"""

    new_indices_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del Índice} & \textbf{Tabla Objetivo} & \textbf{Columnas Indexadas y Tipo de Índice} & \textbf{Propósito} \\
\hline
Índice Docente-Periodo & planes\allowbreak\_docente & B-Tree sobre docente y periodo académico & Búsqueda rápida de expedientes activos. \\
\hline
Índice Actividades-Plan & actividades\allowbreak\_matriz & B-Tree sobre clave foránea del plan & Agrupación de actividades de la matriz. \\
\hline
Índice Estructurado GIN & secciones\allowbreak\_documento & GIN optimizado sobre contenido estructurado & Búsqueda rápida de texto en secciones. \\
\hline
Índice Firma Secuencial & firmas\allowbreak\_documento & B-Tree UNIQUE sobre plan y orden & Garantiza secuencia estricta de firmas. \\
\hline
Índice Huella Digital & evidencias\allowbreak\_adjuntas & B-Tree sobre huella criptográfica SHA-256 & Prevención de duplicados de registros. \\
\hline
\end{tabularx}"""

    if old_indices_table in text:
        text = text.replace(old_indices_table, new_indices_table)
        print("Replaced old_indices_table directly!")
    else:
        pattern = re.compile(r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.8\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.6\\hsize[^}]+\}X\|.*?\\end\{tabularx\}', re.DOTALL)
        text, n = pattern.subn(lambda m: new_indices_table, text, count=1)
        print(f"Replaced indices table via regex: {n}")

    # 2.5:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{2.4cm}|X|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.6: Docker and .env fixes
    text = text.replace(
        r"\item Definicin de Dockerfiles optimizados multicapa para el backend y frontend.",
        r"\item Definición de especificaciones de construcción multicapa para el backend y frontend."
    )
    text = text.replace(
        r"\item Definición de Dockerfiles optimizados multicapa para el backend y frontend.",
        r"\item Definición de especificaciones de construcción multicapa para el backend y frontend."
    )
    text = text.replace(
        r"\subsection{Matriz de Variables de Entorno del Entorno Local (.env)}",
        r"\subsection{Matriz de Variables de Entorno del Entorno Local}"
    )
    text = text.replace(
        r"Aislamiento de credenciales mediante archivo \texttt{.env} protegido",
        r"Aislamiento de credenciales mediante variables de entorno protegidas"
    )

    old_docker_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Imagen Base / Dockerfile} & \textbf{Puertos} & \textbf{Volumen Nombrado} & \textbf{Healthcheck / Comando} \\
\hline
\texttt{sige-frontend} & \texttt{node:20-alpine} & \texttt{5173:5173} & Ninguno & Sondeo HTTP puerto 5173 (frontend activo) \\
\hline
\texttt{sige-backend} & \texttt{node:20-alpine} & \texttt{3000:3000} & Ninguno & Verificacin /api/health con cdigo 200 \\
\hline
\texttt{sige-postgres} & \texttt{postgres:18-alpine} & \texttt{5432:5432} & \texttt{pgdata\_sige} & Comprobacin de conexin con base de datos \\
\hline
\texttt{sige-minio} & \texttt{minio/minio:latest} & \texttt{9000:9000} \newline \texttt{9001:9001} & \texttt{minio\_data} & Chequeo de disponibilidad en puerto 9000 \\
\hline
\texttt{sige-grammar} & \texttt{erikvl87/languagetool} & \texttt{8010:8010} & Ninguno & Consulta de catlogo de idiomas en puerto 8010 \\
\hline
\end{tabularx}"""

    new_docker_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Tecnología y Entorno} & \textbf{Puertos} & \textbf{Persistencia} & \textbf{Comprobación de Estado} \\
\hline
Interfaz Web & Node.js 20 Alpine & 5173 & Aislado & Sondeo de disponibilidad del frontend \\
\hline
Servicios API & Node.js 20 Alpine & 3000 & Aislado & Verificación del servicio con código 200 \\
\hline
Base de Datos & PostgreSQL 18 Alpine & 5432 & Volumen pgdata & Comprobación de conexión relacional activa \\
\hline
Almacenamiento Objetos & Servidor MinIO S3 & 9000 / 9001 & Volumen minio & Sondeo de respuesta del almacén de objetos \\
\hline
Revisión Gramatical & Motor LanguageTool & 8010 & Aislado & Consulta de catálogo lingüístico activo \\
\hline
\end{tabularx}"""

    if old_docker_table in text:
        text = text.replace(old_docker_table, new_docker_table)
        print("Replaced old_docker_table directly!")
    else:
        pattern = re.compile(r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.7\\hsize[^}]+\}X\|.*?\\end\{tabularx\}', re.DOTALL)
        text, n = pattern.subn(lambda m: new_docker_table, text, count=1)
        print(f"Replaced docker table via regex: {n}")

    old_env_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Variable de Entorno} & \textbf{Valor Local Parametrizado} & \textbf{Propsito en el Ecosistema} \\
\hline
\texttt{DB\_HOST} & \texttt{sige-postgres} & Hostname interno en la red Docker bridge. \\
\hline
\texttt{DB\_PORT} & \texttt{5432} & Puerto de conexin a PostgreSQL 18. \\
\hline
\texttt{DB\_NAME} & \texttt{sige\_sgc\_db} & Nombre de la base de datos relacional. \\
\hline
\texttt{MINIO\_ENDPOINT} & \texttt{sige-minio:9000} & Endpoint interno para API S3 de almacenamiento. \\
\hline
\texttt{MINIO\_BUCKET} & \texttt{sige-evidencias} & Bucket privado de almacenamiento de archivos PDF. \\
\hline
\texttt{JWT\_SECRET} & \texttt{sige\_uta\_fisei\_secret\_2026} & Clave privada para firma criptogrfica HMAC-SHA256. \\
\hline
\end{tabularx}"""

    new_env_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Variable de Entorno} & \textbf{Valor Parametrizado} & \textbf{Propósito en el Ecosistema} \\
\hline
Host de Base de Datos & sige-postgres & Nombre de host en la red virtual bridge. \\
\hline
Puerto de Base de Datos & 5432 & Puerto de conexión a PostgreSQL 18. \\
\hline
Nombre de Base de Datos & sige\_sgc\_db & Instancia relacional del sistema. \\
\hline
Servicio de Almacenamiento & sige-minio (puerto 9000) & Punto de acceso interno para objetos. \\
\hline
Espacio de Almacenamiento & sige-evidencias & Espacio institucional de almacenamiento seguro. \\
\hline
Clave Secreta de Tokens & Clave criptográfica institucional & Clave privada para firma digital con HMAC-SHA256. \\
\hline
\end{tabularx}"""

    if old_env_table in text:
        text = text.replace(old_env_table, new_env_table)
        print("Replaced old_env_table directly!")
    else:
        pattern = re.compile(r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.8\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.9\\hsize[^}]+\}X\|.*?\\end\{tabularx\}', re.DOTALL)
        text, n = pattern.subn(lambda m: new_env_table, text, count=1)
        print(f"Replaced env table via regex: {n}")

    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{4.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.7:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("generate_fase2_enhanced.py patched successfully.")

def patch_fase3():
    filepath = "generate_fase3_enhanced.py"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Checklist & Trello tables
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.1: Text line with UUID and tables
    text = re.sub(
        r'Desplegar f.sicamente las 13 tablas con tipos de datos nativos \(\\texttt\{UUID\}, \\texttt\{VARCHAR\}, \\texttt\{NUMERIC\(5,2\)\}, \\texttt\{JSONB\}\)\.',
        r'Desplegar físicamente las 13 tablas con tipos de datos nativos (identificadores UUID, cadenas alfanuméricas, campos numéricos y documentos estructurados JSONB).',
        text
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.2:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{4.0cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.3:
    text = re.sub(
        r'Desarrollar los endpoints de login \(\\texttt\{POST /api/auth/login\}\) y verificaci.n \(\\texttt\{GET /api/auth/me\}\)\.',
        r'Desarrollar los servicios web de autenticación y verificación de sesión del usuario.',
        text
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.5\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.8cm}|m{2.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.4:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|m{3.2cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.5cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.5:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.6:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.5cm}|m{2.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.7:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}m{2.5cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\centering\arraybackslash\footnotesize}m{2.2cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.8:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.9:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|m{2.8cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|X|c|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.10: CRITICAL OVERFLOW FIX
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.11: CRITICAL MIME / FILE FIX
    text = re.sub(
        r'Solo se admiten archivos \\texttt\{application/pdf\} de hasta 25 MB',
        r'Solo se admiten documentos portables PDF institucionales de hasta 25 MB',
        text
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.12:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|>{\centering\arraybackslash}m{1.8cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.4cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.13:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{2.8cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.14:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.8cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|X|c|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.15: Remove .pdf and .docx mentions
    text = re.sub(
        r'formatos oficiales \(\\texttt\{\.pdf\} vectorial no editable y \\texttt\{\.docx\} interoperable\)',
        r'formatos oficiales (documentos portables PDF estandarizados y procesadores ofimáticos Word)',
        text
    )
    text = re.sub(
        r'generador de archivos Microsoft Word \(\\texttt\{\.docx\}\) estructurado',
        r'generador de documentos Microsoft Word estructurado',
        text
    )
    text = re.sub(
        r'documentos ofim.ticos editables en formato \\texttt\{\.docx\}',
        r'documentos ofimáticos editables en procesador Word',
        text
    )

    # 3.16:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.2cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("generate_fase3_enhanced.py patched successfully.")

def patch_fase4():
    filepath = "generate_fase4_enhanced.py"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Checklist & Trello tables
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 4.1:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 4.2: Helmet line fix
    text = re.sub(
        r'La API debe implementar cabeceras seguras mediante la librer.a de cabeceras seguras Helmet \(\\texttt\{Content-Security-Policy\}, \\texttt\{X-Frame-Options: DENY\}, \\texttt\{X-Content-Type-Options: nosniff\}\)\.',
        r'La API debe implementar cabeceras seguras mediante Helmet, aplicando políticas de restricción de recursos CSP, denegación de marcos y prevención de suplantación MIME.',
        text
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 4.3:
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|m{2.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.8cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    text = text.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.0cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\centering\arraybackslash\footnotesize}m{2.4cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("generate_fase4_enhanced.py patched successfully.")

if __name__ == "__main__":
    patch_fase1()
    patch_fase2()
    patch_fase3()
    patch_fase4()
    print("ALL GENERATORS PATCHED SUCCESSFULLY!")
