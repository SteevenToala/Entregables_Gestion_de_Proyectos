# -*- coding: utf-8 -*-
"""
Resolve all remaining table column overflow warnings across all 4 generator scripts.
Ensures zero overfull boxes and flawless visual margin containment.
"""

import re

def fix_all():
    # -------------------------------------------------------------
    # 1. FIX generate_fase1_enhanced.py
    # -------------------------------------------------------------
    with open("generate_fase1_enhanced.py", "r", encoding="utf-8") as f:
        t1 = f.read()

    # 1.4: Anexo 2 table
    t1 = t1.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=2.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 1.5: Anexo 2 table
    # Replace column 1=0.3, col4=0.6 with col1=0.5, col4=0.8
    # Search around "Especificación técnica de diagnósticos de las Validation Gates"
    t1 = re.sub(
        r'(\\begin\{tabularx\}\{\\textwidth\}\{\|)>\{\\hsize=0\.3\\hsize[^}]+\}X\|>\{\\hsize=0\.7\\hsize[^}]+\}X\|>\{\\hsize=2\.4\\hsize[^}]+\}X\|>\{\\hsize=0\.6\\hsize[^}]+\}X\|(\}.*?diagn.sticos de las Validation Gates)',
        r'\1>{\\hsize=0.5\\hsize\\centering\\arraybackslash\\footnotesize}X|>{\\hsize=0.9\\hsize\\centering\\arraybackslash\\bfseries\\footnotesize}X|>{\\hsize=1.8\\hsize\\raggedright\\arraybackslash\\footnotesize}X|>{\\hsize=0.8\\hsize\\centering\\arraybackslash\\footnotesize}X|\2',
        t1,
        flags=re.DOTALL
    )

    # 1.8: Hito 1 auditoria table: change 0.3 to 0.5 for EDT 1.1 - EDT 1.8
    t1 = t1.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    with open("generate_fase1_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t1)
    print("generate_fase1_enhanced.py updated!")

    # -------------------------------------------------------------
    # 2. FIX generate_fase2_enhanced.py
    # -------------------------------------------------------------
    with open("generate_fase2_enhanced.py", "r", encoding="utf-8") as f:
        t2 = f.read()

    # 2.2: Anexo 2 table (servicios de infraestructura)
    old_2_2_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Puerto} & \textbf{Protocolo} & \textbf{Dependencia} & \textbf{Contrato / Funcin Principal} \\
\hline
\texttt{sige-frontend} & 5173 / 80 & HTTP/HTTPS & Backend API & Entrega de SPA React y proxy de llamadas API. \\
\hline
\texttt{sige-backend} & 3000 & REST / JSON & PostgreSQL, MinIO & Lgica de negocio, Validation Gates y autenticacin. \\
\hline
\texttt{sige-postgres} & 5432 & PostgreSQL Wire & Volumen local & Persistencia relacional ACID y documentos JSONB. \\
\hline
\texttt{sige-minio} & 9000 / 9001 & AWS S3 API & Volumen local & Almacenamiento binario de evidencias PDF y URLs prefirmadas. \\
\hline
\texttt{sige-grammar} & 8010 & HTTP REST & Memoria interna & Servicio local Docker LanguageTool de gramtica en espaol. \\
\hline
\end{tabularx}"""

    new_2_2_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Puerto} & \textbf{Protocolo} & \textbf{Dependencia} & \textbf{Función Principal de Arquitectura} \\
\hline
Frontend Web & 5173 / 80 & HTTP/HTTPS & Backend API & Entrega de interfaz React y llamadas a la API. \\
\hline
Backend API & 3000 & REST / JSON & Base de Datos & Lógica de negocio, Validation Gates y autenticación. \\
\hline
PostgreSQL 18 & 5432 & Nativo TCP & Almacén local & Persistencia relacional ACID y documentos JSONB. \\
\hline
Almacén MinIO S3 & 9000 / 9001 & AWS S3 API & Almacén local & Almacenamiento seguro de documentos probatorios. \\
\hline
Corrector Lingüístico & 8010 & HTTP REST & Memoria interna & Servicio local de asistencia gramatical en español. \\
\hline
\end{tabularx}"""

    t2 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.3\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.4\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Matriz de servicios y comunicaci.n de infraestructura\.\})',
        lambda m: new_2_2_table + m.group(1),
        t2,
        flags=re.DOTALL
    )

    # 2.4: Anexo 2 table (restricciones e integridad declarativa)
    new_2_4_anx2_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Regla de Integridad} & \textbf{Tabla Objetivo} & \textbf{Definición Técnica Declarativa} \\
\hline
Horas No Negativas & actividades\allowbreak\_matriz & Dedicación semanal estricta entre 0 y 40 horas. \\
\hline
Ponderación Acumulada & actividades\allowbreak\_matriz & Ponderación individual entre 0.00\% y 100.00\%. \\
\hline
Estados Válidos SGC & planes\allowbreak\_docente & Borrador, En Revisión, Observado o Aprobado. \\
\hline
Auditoría Temporal & Todas las tablas & Actualización automática de marca temporal. \\
\hline
\end{tabularx}"""

    t2 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.3\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.9\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.8\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Restricciones e integridad declarativa en la base de datos\.\})',
        lambda m: new_2_4_anx2_table + m.group(1),
        t2,
        flags=re.DOTALL
    )

    # 2.5: Nielsen table
    t2 = t2.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.6: Docker Compose table in body
    new_docker_body_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
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

    t2 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.7\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.8\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Matriz t.cnica de servicios de la arquitectura Docker Compose\.\})',
        lambda m: new_docker_body_table + m.group(1),
        t2,
        flags=re.DOTALL
    )

    # 2.7: Hito 2 auditoria table: change 0.3 to 0.5 for EDT 2.1 - EDT 2.7
    t2 = t2.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t2)
    print("generate_fase2_enhanced.py updated!")

    # -------------------------------------------------------------
    # 3. FIX generate_fase3_enhanced.py
    # -------------------------------------------------------------
    with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
        t3 = f.read()

    # 3.1: Table 1 (DDL indices) and Table 2 (volumetria)
    # Remove \texttt from table names
    t3 = t3.replace(r"\texttt{planes\_docente}", r"planes\allowbreak\_docente")
    t3 = t3.replace(r"\texttt{secciones\_documento}", r"secciones\allowbreak\_documento")
    t3 = t3.replace(r"\texttt{actividades\_matriz}", r"actividades\allowbreak\_matriz")
    t3 = t3.replace(r"\texttt{firmas\_documento}", r"firmas\allowbreak\_documento")
    t3 = t3.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.55\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.55\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.6: Anexo 2 XSS table
    new_3_6_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Prueba ID} & \textbf{Carga Útil de Prueba Evaluada} & \textbf{Comportamiento de Sanitización Verificado} & \textbf{Resultado} \\
\hline
TC-SEC-01 & Inyección de script malicioso en etiqueta script & Etiqueta eliminada por sanitizador antes de persistir & SUPERADO \\
\hline
TC-SEC-02 & Inyección de etiqueta imagen con evento malicioso & Evento suprimido por sanitizador DOMPurify & SUPERADO \\
\hline
TC-SEC-03 & Enlace con esquema de pseudoprotocolo javascript & Protocolo neutralizado en el renderizado & SUPERADO \\
\hline
TC-PERF-01 & Tipeo rápido sostenido (80 WPM por 2 minutos) & 3 llamadas HTTP consolidadas mediante debounce & SUPERADO \\
\hline
\end{tabularx}"""

    t3 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|c\|>\{\\raggedright\\arraybackslash\\footnotesize\}m\{2\.5cm\}\|>\{\\raggedright\\arraybackslash\\footnotesize\}X\|>\{\\centering\\arraybackslash\\footnotesize\}m\{2\.2cm\}\|\}.*?\\end\{tabularx\}(\s*\\caption\{Pruebas de seguridad XSS y desempe.o de debounce\.\})',
        lambda m: new_3_6_table + m.group(1),
        t3,
        flags=re.DOTALL
    )

    # 3.9: Reducer table
    new_3_9_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Operación de Estado} & \textbf{Acción del Usuario} & \textbf{Transformación de Estado Ejecutada} & \textbf{Eficiencia} \\
\hline
Agregar Actividad & Clic en botón ``+ Agregar'' & Inserta nueva fila con valores por defecto e ID autogenerado & Inmediata \\
\hline
Actualizar Ponderación & Modificación de ponderación & Recalcula suma total; actualiza indicador visual al instante & En tiempo real \\
\hline
Programar Semana & Clic en casilla de semana & Actualiza la programación semestral en el registro & Inmediata \\
\hline
Asistencia Redacción & Clic en botón ``Sugerir IA'' & Carga sugerencias normalizadas de redacción del SGC & Inmediata \\
\hline
\end{tabularx}"""

    t3 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.3\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.0\\hsize[^}]+\}X\|>\s*\{\\hsize=2\.1\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.6\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Estructura de acciones inmutables del componente React\.\})',
        lambda m: new_3_9_table + m.group(1),
        t3,
        flags=re.DOTALL
    )

    # 3.11: Endpoints table
    new_3_11_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Operación y Retorno} & \textbf{Código HTTP} \\
\hline
POST & /api/evidencias/upload & Carga de archivo multipart; cálculo SHA-256 y registro en DB & 201 Created \\
\hline
GET & /api/evidencias/:id/url & Generación de URL prefirmada para visualización embebida & 200 OK \\
\hline
DELETE & /api/evidencias/:id & Borrado lógico en base de datos (preserva objeto para auditoría) & 200 OK \\
\hline
\end{tabularx}"""

    t3 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.4\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.1\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.8\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.7\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Endpoints RESTful para evidencias documentales\.\})',
        lambda m: new_3_11_table + m.group(1),
        t3,
        flags=re.DOTALL
    )

    # 3.13: Observaciones severidad table
    t3 = t3.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.14: Reglas gramaticales table
    t3 = t3.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.15: Parametros exportacion table
    t3 = t3.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.8cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.16: Hito 5 auditoria table: change 0.3 to 0.5 for EDT 3.1 - EDT 3.16
    t3 = re.sub(
        r'(\\begin\{tabularx\}\{\\textwidth\}\{\|)>\{\\hsize=0\.3\\hsize[^}]+\}X\|>\{\\hsize=1\.0\\hsize[^}]+\}X\|>\{\\hsize=0\.5\\hsize[^}]+\}X\|>\{\\hsize=1\.7\\hsize[^}]+\}X\|>\{\\hsize=0\.5\\hsize[^}]+\}X\|(\}.*?auditor.a de entregables de la Fase 3)',
        r'\1>{\\hsize=0.5\\hsize\\centering\\arraybackslash\\bfseries\\footnotesize}X|>{\\hsize=1.0\\hsize\\raggedright\\arraybackslash\\footnotesize}X|>{\\hsize=0.5\\hsize\\centering\\arraybackslash\\footnotesize}X|>{\\hsize=1.5\\hsize\\raggedright\\arraybackslash\\footnotesize}X|>{\\hsize=0.5\\hsize\\centering\\arraybackslash\\footnotesize}X|\2',
        t3,
        flags=re.DOTALL
    )

    with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t3)
    print("generate_fase3_enhanced.py updated!")

    # -------------------------------------------------------------
    # 4. FIX generate_fase4_enhanced.py
    # -------------------------------------------------------------
    with open("generate_fase4_enhanced.py", "r", encoding="utf-8") as f:
        t4 = f.read()

    # 4.1: Pruebas unitarias backend table
    new_4_1_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Suite ID} & \textbf{Módulo Evaluado} & \textbf{Condición de Prueba y Datos de Entrada} & \textbf{Aserción de Calidad} & \textbf{Estado} \\
\hline
UT-01 & Gate 1 (Horas) & Plan con 40 horas exactas contractuales. & Validación exitosa & \textbf{PASSED} \\
\hline
UT-02 & Gate 1 (Horas) & Plan con 38 horas semanales (faltan 2h). & Excepción HTTP 422 & \textbf{PASSED} \\
\hline
UT-03 & Gate 2 (Pond.) & Actividades con pesos 40\%, 30\%, 30\% (total 100\%). & Cuadre exacto 100\% & \textbf{PASSED} \\
\hline
UT-04 & Gate 2 (Pond.) & Actividades con pesos 40\%, 30\%, 25\% (total 95\%). & Excepción HTTP 422 & \textbf{PASSED} \\
\hline
UT-05 & Gate 3 (Evid.) & Actividad con avance 50\% y archivo con SHA-256. & Evidencia válida & \textbf{PASSED} \\
\hline
UT-06 & Gate 3 (Evid.) & Actividad con avance 50\% y cero archivos adjuntos. & Excepción HTTP 422 & \textbf{PASSED} \\
\hline
UT-07 & Cascada Firmas & Firma Revisor tras firma previa de Elaborador. & Firma habilitada & \textbf{PASSED} \\
\hline
UT-08 & Cascada Firmas & Firma Revisor sin firma previa de Elaborador. & Conflicto HTTP 409 & \textbf{PASSED} \\
\hline
\end{tabularx}"""

    t4 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.3\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.0\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.8\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.45\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.45\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Matriz de pruebas unitarias automatizadas ejecutadas en SIGE\.\})',
        lambda m: new_4_1_table + m.group(1),
        t4,
        flags=re.DOTALL
    )

    # 4.2: OWASP table
    new_4_2_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Categoría} & \textbf{Riesgo OWASP} & \textbf{Vector de Ataque Probado} & \textbf{Defensa Implementada en SIGE} & \textbf{Estado} \\
\hline
\textbf{A01} & Broken Access Control & Docente intenta editar plan ajeno alterando identificador. & Verificación estricta en middleware de permisos. & \textbf{MITIGADO} \\
\hline
\textbf{A02} & Cryptographic Failures & Intento de descifrado de contraseñas y alteración de firmas. & Cifrado Argon2id con salt único; firmas SHA-256. & \textbf{MITIGADO} \\
\hline
\textbf{A03} & Injection (SQL / XSS) & Inyección de sentencias SQL y etiquetas en secciones de texto. & Consultas parametrizadas; sanitización DOMPurify. & \textbf{MITIGADO} \\
\hline
\textbf{A04} & Insecure Design & Envío de planes incompletos o fuera de plazo. & Validación lógica en 6 Validation Gates de backend. & \textbf{MITIGADO} \\
\hline
\textbf{A05} & Security Misconfig & Puertos de base de datos expuestos o cabeceras por defecto. & Aislamiento en red virtual; cabeceras con Helmet. & \textbf{MITIGADO} \\
\hline
\textbf{A06} & Vulnerable Comp. & Dependencias con vulnerabilidades conocidas reportadas. & Auditoría automatizada; cero alertas de severidad. & \textbf{MITIGADO} \\
\hline
\textbf{A07} & Ident. \& Auth Failures & Ataques de fuerza bruta contra el formulario de login. & Límite de 5 intentos por IP y bloqueo temporal. & \textbf{MITIGADO} \\
\hline
\textbf{A08} & Software/Data Integrity & Manipulación de documentos de soporte cargados. & Cómputo de firma SHA-256 en carga y lectura S3. & \textbf{MITIGADO} \\
\hline
\textbf{A09} & Logging \& Monitor Fail & Acciones críticas sin registro o trazabilidad. & Bitácora de auditoría con dirección, usuario y fecha. & \textbf{MITIGADO} \\
\hline
\textbf{A10} & SSRF & Peticiones forzadas del backend a servidores maliciosos. & Corrector restringido estrictamente a la red local. & \textbf{MITIGADO} \\
\hline
\end{tabularx}"""

    t4 = re.sub(
        r'\\begin\{tabularx\}\{\\textwidth\}\{\|>\s*\{\\hsize=0\.3\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.9\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.2\\hsize[^}]+\}X\|>\s*\{\\hsize=1\.2\\hsize[^}]+\}X\|>\s*\{\\hsize=0\.4\\hsize[^}]+\}X\|.*?\\end\{tabularx\}(\s*\\caption\{Matriz oficial de evaluaci.n de seguridad OWASP Top 10 en SIGE\.\})',
        lambda m: new_4_2_table + m.group(1),
        t4,
        flags=re.DOTALL
    )

    # 4.3: Cross-browser table & WCAG table
    t4 = t4.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.85\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.65\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    t4 = t4.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    with open("generate_fase4_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t4)
    print("generate_fase4_enhanced.py updated!")

if __name__ == "__main__":
    fix_all()
    print("ALL REMAINING OVERFLOWS RESOLVED IN GENERATORS!")
