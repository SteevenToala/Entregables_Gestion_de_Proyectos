import re

print("Starting fix_tables_and_code.py...")

# ==============================================================================
# 1. FIX GENERATE_FASE2_ENHANCED.PY
# ==============================================================================
f2_path = "generate_fase2_enhanced.py"
f2_txt = open(f2_path, encoding="utf-8").read()

# Fix 2.3 clases de dominio table
f2_txt = f2_txt.replace(
    r"\texttt{PlanDocente} & \texttt{id}, \texttt{periodo\_id}, \texttt{docente\_id}, \texttt{estado}, \texttt{horas\_totales} & \texttt{validarHorasMinimas()}, \texttt{avanzarEstado()}, \texttt{solicitarRevision()} & 1 \\",
    r"PlanDocente & Identificador, periodo, docente, estado, horas totales & Validar horas mínimas, avanzar estado, solicitar revisión & 1 \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{SeccionDocumento} & \texttt{id}, \texttt{plan\_id}, \texttt{orden}, \texttt{titulo}, \texttt{contenido\_html} & \texttt{actualizarContenido()}, \texttt{sanitizarHtml()}, \texttt{bloquearEdicion()} & $1 \dots N$ \\",
    r"SeccionDocumento & Identificador, plan, orden, título, contenido & Actualizar contenido, sanitizar texto, bloquear edición & $1 \dots N$ \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{ActividadMatriz} & \texttt{id}, \texttt{plan\_id}, \texttt{nombre}, \texttt{horas}, \texttt{ponderacion}, \texttt{cronograma} & \texttt{calcularAvance()}, \texttt{asignarMedio()}, \texttt{recalcularPonderacion()} & $1 \dots N$ \\",
    r"ActividadMatriz & Identificador, plan, nombre, horas, ponderación & Calcular avance, asignar medio, recalcular balance & $1 \dots N$ \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{EvidenciaAdjunta} & \texttt{id}, \texttt{actividad\_id}, \texttt{nombre\_archivo}, \texttt{url\_s3}, \texttt{hash\_sha256} & \texttt{verificarIntegridad()}, \texttt{generarUrlLectura()}, \texttt{asociarHash()} & $0 \dots N$ \\",
    r"EvidenciaAdjunta & Identificador, actividad, nombre, URL S3, hash & Verificar integridad, generar URL segura, auditar & $0 \dots N$ \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{ObservacionComite} & \texttt{id}, \texttt{plan\_id}, \texttt{usuario\_id}, \texttt{seccion\_id}, \texttt{comentario}, \texttt{resuelto} & \texttt{registrarObservacion()}, \texttt{marcarResuelto()}, \texttt{auditarCambio()} & $0 \dots N$ \\",
    r"ObservacionComite & Identificador, plan, usuario, sección, detalle & Registrar observación, marcar resuelto, auditar & $0 \dots N$ \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{FirmaDocumento} & \texttt{id}, \texttt{plan\_id}, \texttt{firmante\_id}, \texttt{rol\_firma}, \texttt{fecha\_firma}, \texttt{hash\_firma} & \texttt{estamparFirma()}, \texttt{validarSecuencia()}, \texttt{sellarDocumento()} & $0 \dots 3$ \\",
    r"FirmaDocumento & Identificador, plan, firmante, rol, fecha, sello & Estampar firma, validar secuencia, sellar documento & $0 \dots 3$ \\"
)

# Fix 2.4 text line 145
f2_txt = f2_txt.replace(r"(\texttt{CHECK horas >= 0}, \texttt{CHECK ponderacion <= 100})", "(restricciones declarativas de horas no negativas y balance de ponderación)")

# Fix 2.4 diccionario de datos table
f2_txt = f2_txt.replace(
    r"\texttt{idx\_planes\_docente\_periodo} & \texttt{planes\_docente} & \texttt{(fk\_docente, fk\_periodo)} -- B-Tree & Búsqueda rápida de expedientes activos. \\",
    r"Índice Docente-Periodo & planes\_docente & B-Tree sobre docente y periodo académico & Búsqueda rápida de expedientes activos. \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{idx\_actividades\_plan} & \texttt{actividades\_matriz} & \texttt{(fk\_plan)} -- B-Tree & Agrupación de actividades de la matriz. \\",
    r"Índice Actividades-Plan & actividades\_matriz & B-Tree sobre clave foránea del plan & Agrupación de actividades de la matriz. \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{idx\_secciones\_jsonb} & \texttt{secciones\_documento} & \texttt{contenido\_jsonb} -- GIN (\texttt{jsonb\_path\_ops}) & Búsqueda rápida de texto en secciones. \\",
    r"Índice Estructurado GIN & secciones\_documento & GIN optimizado sobre contenido estructurado & Búsqueda rápida de texto en secciones. \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{idx\_firmas\_plan\_orden} & \texttt{firmas\_documento} & \texttt{(fk\_plan, orden)} -- B-Tree UNIQUE & Garantiza secuencia estricta de firmas. \\",
    r"Índice de Firma Secuencial & firmas\_documento & B-Tree UNIQUE sobre plan y orden & Garantiza secuencia estricta de firmas. \\"
)
f2_txt = f2_txt.replace(
    r"\texttt{idx\_evidencias\_hash} & \texttt{evidencias\_adjuntas} & \texttt{hash\_sha256} -- B-Tree & Prevención de duplicados de archivos. \\",
    r"Índice Huella Digital & evidencias\_adjuntas & B-Tree sobre huella criptográfica SHA-256 & Prevención de duplicados de archivos. \\"
)

# Fix 2.6 docker variables table
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{4.2cm}|X|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries\footnotesize}m{3.2cm}|>{\raggedright\arraybackslash\footnotesize}m{3.8cm}|>{\raggedright\arraybackslash\footnotesize}X|}"
)

with open(f2_path, "w", encoding="utf-8") as f:
    f.write(f2_txt)
print("Fase 2 tables and code cleaned.")

# ==============================================================================
# 2. FIX GENERATE_FASE3_ENHANCED.PY
# ==============================================================================
f3_path = "generate_fase3_enhanced.py"
f3_txt = open(f3_path, encoding="utf-8").read()

# Fix 3.1 line 136
f3_txt = f3_txt.replace(
    r"(\texttt{UUID}, \texttt{VARCHAR}, \texttt{JSONB}, \texttt{TIMESTAMPTZ})",
    "utilizando identificadores únicos universales, campos de texto enriquecido estructurado y marcas de tiempo con zona horaria"
)

# Fix 3.3 line 136
f3_txt = f3_txt.replace(
    r"(\texttt{POST /api/auth/login}) y verificación (\texttt{GET /api/auth/verify})",
    "de autenticación mediante credenciales universitarias y verificación continua de sesión"
)

# Fix 3.7 endpoints table
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/planes} & \texttt{listarPlanes} & Filtros: \texttt{?periodo\_id=\&estado=} & 200 OK \\",
    r"\textbf{GET} & /api/planes & Listado General & Consulta filtrada por periodo académico y estado & 200 OK \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{POST} & \texttt{/api/planes} & \texttt{crearPlan} & \texttt{\{periodo\_id, carrera\_id, dedicacion\}} & 201 Created \\",
    r"\textbf{POST} & /api/planes & Creación de Plan & Registro inicial con dedicación horaria y carrera & 201 Created \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/planes/:id} & \texttt{obtenerPlan} & Parámetro URL \texttt{id} (UUID) & 200 OK \\",
    r"\textbf{GET} & /api/planes/:id & Detalle de Plan & Recuperación completa del expediente por identificador & 200 OK \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{PUT} & \texttt{/api/planes/:id} & \texttt{actualizarPlan} & \texttt{\{horas\_totales, estado\}} & 200 OK \\",
    r"\textbf{PUT} & /api/planes/:id & Actualizar Estado & Modificación de horas acumuladas y estado del ciclo & 200 OK \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/secciones/:planId} & \texttt{listarSecciones} & Parámetro URL \texttt{planId} & 200 OK \\",
    r"\textbf{GET} & /api/secciones/:planId & Cargar Secciones & Recuperación de contenido estructurado por plan & 200 OK \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{PUT} & \texttt{/api/secciones/batch} & \texttt{actualizarBatch} & \texttt{\{secciones: [\{id, contenido\}]\}} & 200 OK \\",
    r"\textbf{PUT} & /api/secciones/batch & Guardado por Lotes & Persistencia transaccional ACID de múltiples secciones & 200 OK \\"
)

# Fix 3.9 line 129
f3_txt = f3_txt.replace(
    r"(\texttt{UTA-SGC-A-2-1-P7-T1})",
    "(Formato Oficial de Plan de Trabajo)"
)

# Fix 3.10 line 179 and table
f3_txt = f3_txt.replace(
    r"(\textit{Chain of Responsibility})",
    "bajo el patrón arquitectónico de cadena de responsabilidad"
)
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{2.8cm}|X|c|X|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.4cm}|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{1.4cm}|>{\raggedright\arraybackslash\footnotesize}X|}"
)

# Fix 3.11 line 188 and endpoints table
f3_txt = f3_txt.replace(
    r"Solo se admiten archivos \texttt{application/pdf} con tamaño máximo de $10\text{ MB}$",
    r"Solo se admiten archivos PDF vectoriales con tamaño máximo de $10\text{ MB}$"
)
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\footnotesize}m{3.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}"
)

# Fix 3.15 endpoints table
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/export/:id/pdf} & \texttt{application/pdf} con nombre \texttt{Plan\_Docente\_\{id\}.pdf} & Directa \\",
    r"\textbf{GET} & /api/export/:id/pdf & Generación y descarga directa de documento oficial en PDF & Descarga Directa \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/export/:id/word} & \texttt{application/vnd.openxmlformats...} (\texttt{.docx}) & Directa \\",
    r"\textbf{GET} & /api/export/:id/word & Generación y descarga directa de documento oficial en Word & Descarga Directa \\"
)
f3_txt = f3_txt.replace(
    r"\texttt{GET} & \texttt{/api/export/:id/preview} & Vista previa en streaming para visor PDF embebido en el navegador. & Streaming \\",
    r"\textbf{GET} & /api/export/:id/preview & Flujo de datos para visor documental embebido en navegador & Vista Previa \\"
)

with open(f3_path, "w", encoding="utf-8") as f:
    f.write(f3_txt)
print("Fase 3 tables and code cleaned.")

# ==============================================================================
# 3. FIX GENERATE_FASE4_ENHANCED.PY
# ==============================================================================
f4_path = "generate_fase4_enhanced.py"
f4_txt = open(f4_path, encoding="utf-8").read()

# Fix 4.1 test console table in Anexo 2
f4_txt = f4_txt.replace(
    r"\begin{tabularx}{\textwidth}{|m{3.0cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}"
)
f4_txt = f4_txt.replace(
    r"\texttt{validation-gates.test} & \texttt{PASS Módulo de pruebas de compuertas de validación (8 tests passed, 0 failed)} & 342 ms \\",
    r"Compuertas de Negocio & 8 pruebas unitarias de balance horario y reglas SGC: 100\% superadas & 342 ms \\"
)
f4_txt = f4_txt.replace(
    r"\texttt{matriz-calc.test} & \texttt{PASS Módulo de pruebas de cálculo matricial (12 tests passed, 0 failed)} & 189 ms \\",
    r"Matriz de Actividades & 12 pruebas de cálculo reactivo y sumatoria al 100\%: 100\% superadas & 189 ms \\"
)
f4_txt = f4_txt.replace(
    r"\texttt{auth-jwt.test} & \texttt{PASS Módulo de pruebas de autenticación (9 tests passed, 0 failed)} & 215 ms \\",
    r"Autenticación y RBAC & 9 pruebas de firmas JWT y permisos de rol docente: 100\% superadas & 215 ms \\"
)
f4_txt = f4_txt.replace(
    r"\texttt{firmas-cascade.test} & \texttt{PASS Módulo de pruebas de cascada de firmas (6 tests passed, 0 failed)} & 164 ms \\",
    r"Cascada de Firmas & 6 pruebas de secuencia cronológica e inmutabilidad: 100\% superadas & 164 ms \\"
)

# Fix 4.2 line 187
f4_txt = f4_txt.replace(
    r"La API debe implementar cabeceras seguras mediante \texttt{helmet} y restricciones CORS estrictas",
    r"La API debe implementar cabeceras seguras mediante el middleware Helmet y restricciones de origen CORS"
)

with open(f4_path, "w", encoding="utf-8") as f:
    f.write(f4_txt)
print("Fase 4 tables and code cleaned.")

print("All generator files updated with zero-overflow tables and zero raw code!")
