# apply_zero_overfull_fixes.py

# 1. Update 3.1 and 3.6 in fase3_annexes_part1.py
with open("fase3_annexes_part1.py", "r", encoding="utf-8") as f:
    c = f.read()

# 3.1: Aprovisionamiento and DDL script lines
c = c.replace(
    r"\item \textbf{Aprovisionamiento del Contenedor de Base de Datos:} Se configuró el servicio en \texttt{docker-compose.yml} utilizando un volumen persistente \texttt{pgdata} montado en \texttt{/var/lib/\allowbreak postgresql/\allowbreak data}, definiendo el juego de caracteres \texttt{UTF-8} y la configuración de memoria compartida optimizada para PostgreSQL 18.",
    r"\item \textbf{Aprovisionamiento de Base de Datos:} Se configuró el servicio Docker con volumen persistente montado en el directorio de datos, codificación UTF-8 y memoria compartida optimizada para PostgreSQL 18."
)

c = c.replace(
    r"\item \textbf{Ejecución Secuencial del Script DDL:} Se desplegó el script estructurado \texttt{schema.sql} creando las 13 tablas relacionales en tercera forma normal (3NF): las tablas \texttt{users}, \texttt{roles}, \texttt{carreras}, \texttt{periodos}, \texttt{comisiones}, \texttt{planes\allowbreak\_docente}, \texttt{secciones\allowbreak\_documento}, \texttt{actividades\allowbreak\_matriz}, \texttt{plan\allowbreak\_seguimiento}, \texttt{seguimiento\allowbreak\_evidencias}, \texttt{firmas\allowbreak\_documento}, \texttt{audit\allowbreak\_logs} y \texttt{refresh\allowbreak\_tokens}.",
    r"\item \textbf{Ejecución del Script DDL:} Se desplegó el script \texttt{schema.sql} creando las 13 tablas relacionales en 3NF (usuarios, roles, comisiones, carreras, períodos, planes, matrices, secciones, evidencias, firmas y auditoría)."
)

c = c.replace(
    r"\noindent \textbf{Explicación Técnica del Artefacto Visual:}",
    r"\textbf{Explicación Técnica del Artefacto Visual:}"
)

# 3.6: Autoguardado
c = c.replace(
    r"\item \textbf{Mecanismo de Autoguardado con Debounce de 1500 ms:} Se implementó el hook \texttt{useDebounce}. Mientras el docente escribe continuamente, los temporizadores se reinician. Exactamente 1500 ms después de la última pulsación de teclado, se despacha la petición asíncrona \texttt{PATCH /api/v1/}\allowbreak\texttt{planes/:id/}\allowbreak\texttt{secciones}.",
    r"\item \textbf{Autoguardado con Debounce de 1500 ms:} Se implementó el hook \texttt{useDebounce}. Mientras el docente escribe, los temporizadores se reinician; tras 1500 ms de inactividad, se despacha la petición asíncrona al backend."
)

with open("fase3_annexes_part1.py", "w", encoding="utf-8") as f:
    f.write(c)

# 2. Update 4.2 in generate_fase4_enhanced.py
with open("generate_fase4_enhanced.py", "r", encoding="utf-8") as f:
    c4 = f.read()

c4 = c4.replace(
    r"\item \textbf{Pruebas de Cross-Site Scripting (XSS):} Inserción de payloads de prueba (\texttt{<script>alert(1)</script>}, directivas de evento \texttt{onload} e imágenes rotas) en el editor de texto enriquecido TipTap. El componente procesa el contenido mediante un pipeline de sanitización estricta que remueve cualquier etiqueta potencialmente peligrosa antes de la persistencia en formato JSONB.",
    r"\item \textbf{Pruebas de Scripting XSS:} Inserción de payloads (\texttt{<script>} alert, directivas de evento \texttt{onload}) en el editor TipTap. El pipeline de sanitización remueve cualquier etiqueta potencialmente peligrosa antes de persistir el JSONB."
)

with open("generate_fase4_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c4)

print("Zero-overfull fixes applied cleanly!")
