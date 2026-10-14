# fix_final_overfull_lines.py

# 1. Update generate_fase1_enhanced.py
with open("generate_fase1_enhanced.py", "r", encoding="utf-8") as f:
    c1 = f.read()
c1 = c1.replace(r"\item \textbf{Auditoría de Plantillas Físicas y Ofimáticas SGC:}", r"\item \textbf{Auditoría de Plantillas SGC:}")
with open("generate_fase1_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c1)

# 2. Update fase3_annexes_part1.py and fase3_annexes_part2.py
with open("fase3_annexes_part1.py", "r", encoding="utf-8") as f:
    cp1 = f.read()
cp1 = cp1.replace(
    r"\item \textbf{Protocolo de Revocación Inmediata de Sesiones:} Se programó el endpoint \texttt{POST /api/v1/auth/logout}",
    r"\item \textbf{Revocación Inmediata de Sesiones:} Se programó el endpoint \texttt{POST} \texttt{/api/v1/auth/logout}"
)
with open("fase3_annexes_part1.py", "w", encoding="utf-8") as f:
    f.write(cp1)

with open("fase3_annexes_part2.py", "r", encoding="utf-8") as f:
    cp2 = f.read()
cp2 = cp2.replace(
    r"\texttt{POST /api/v1/planes/:id/enviar-revision}",
    r"\texttt{POST /api/v1/}\allowbreak\texttt{planes/:id/}\allowbreak\texttt{enviar-revision}"
)
cp2 = cp2.replace(
    r"\item \textbf{Generación de Huella Criptográfica SHA-256:}",
    r"\item \textbf{Generación de Huella SHA-256:}"
)
cp2 = cp2.replace(
    r"\item \textbf{Emisión de URLs Prefirmadas con Expiración a 900 Segundos (15 min):}",
    r"\item \textbf{Emisión de URLs Prefirmadas (15 min):}"
)
cp2 = cp2.replace(
    r"\item \textbf{Estructura Inmutable del Registro de Firma:}",
    r"\item \textbf{Registro Inmutable de Firma:}"
)
with open("fase3_annexes_part2.py", "w", encoding="utf-8") as f:
    f.write(cp2)

print("Final overfull lines patched!")
