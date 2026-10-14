# fix_soft_breaks.py

with open("fase3_annexes_part1.py", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("/var/lib/postgresql/data", "/var/lib/\\allowbreak postgresql/\\allowbreak data")
c = c.replace(
    r"\texttt{users}, \texttt{roles}, \texttt{carreras}, \texttt{periodos}, \texttt{comisiones}, \texttt{planes\_docente}, \texttt{secciones\_documento}, \texttt{actividades\_matriz}, \texttt{plan\_seguimiento}, \texttt{seguimiento\_evidencias}, \texttt{firmas\_documento}, \texttt{audit\_logs} y \texttt{refresh\_tokens}.",
    r"las tablas \texttt{users}, \texttt{roles}, \texttt{carreras}, \texttt{periodos}, \texttt{comisiones}, \texttt{planes\allowbreak\_docente}, \texttt{secciones\allowbreak\_documento}, \texttt{actividades\allowbreak\_matriz}, \texttt{plan\allowbreak\_seguimiento}, \texttt{seguimiento\allowbreak\_evidencias}, \texttt{firmas\allowbreak\_documento}, \texttt{audit\allowbreak\_logs} y \texttt{refresh\allowbreak\_tokens}."
)
c = c.replace(
    r"\texttt{verifyRole(['Docente', 'Coordinador', 'Subdecano', 'Admin'])}",
    r"el middleware \texttt{verifyRole} con los roles institucionales"
)
c = c.replace(
    r"\texttt{PATCH /api/v1/planes/:id/secciones}",
    r"\texttt{PATCH /api/v1/}\allowbreak\texttt{planes/:id/}\allowbreak\texttt{secciones}"
)

with open("fase3_annexes_part1.py", "w", encoding="utf-8") as f:
    f.write(c)

with open("fase3_annexes_part2.py", "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace(r"\texttt{seguimiento\_evidencias}", r"\texttt{seguimiento\allowbreak\_evidencias}")
c2 = c2.replace(r"\texttt{presignedGetObject()}", r"\texttt{presigned}\allowbreak\texttt{GetObject()}")
c2 = c2.replace(r"\texttt{firmas\_documento}", r"\texttt{firmas\allowbreak\_documento}")

with open("fase3_annexes_part2.py", "w", encoding="utf-8") as f:
    f.write(c2)

# Fix generate_fase4_enhanced.py
with open("generate_fase4_enhanced.py", "r", encoding="utf-8") as f:
    c4 = f.read()

c4 = c4.replace(
    r"\texttt{<script>alert('xss')</script>}",
    r"\texttt{<script>}\allowbreak\texttt{alert('xss')}\allowbreak\texttt{</script>}"
)

with open("generate_fase4_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c4)

print("Soft linebreaks applied cleanly!")
