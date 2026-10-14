import re

print("Starting fix_final_tables.py...")

# ==============================================================================
# 1. FASE 2
# ==============================================================================
f2_txt = open("generate_fase2_enhanced.py", encoding="utf-8").read()

# Replace diccionario_datos column spec with all relative X columns
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.4cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Replace indices column spec with all relative X columns
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries\footnotesize}m{3.0cm}|>{\centering\arraybackslash}m{2.2cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}m{3.8cm}|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Replace docker_matrix column spec with all relative X columns
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.4cm}|>{\raggedright\arraybackslash\footnotesize}m{2.6cm}|>{\centering\arraybackslash\footnotesize}m{1.8cm}|>{\centering\arraybackslash\footnotesize}m{2.2cm}|>{\raggedright\arraybackslash\footnotesize}X|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Replace docker variables column spec with all relative X columns
f2_txt = f2_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries\footnotesize}m{3.2cm}|>{\raggedright\arraybackslash\footnotesize}m{3.8cm}|>{\raggedright\arraybackslash\footnotesize}X|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
    f.write(f2_txt)
print("generate_fase2_enhanced.py updated.")

# ==============================================================================
# 2. FASE 3
# ==============================================================================
f3_txt = open("generate_fase3_enhanced.py", encoding="utf-8").read()

# Fix 3.1 table
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Fix 3.2 seed table
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{2.5cm}|X|c|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Fix 3.6 Anexo 2 TC-SEC table
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
)

# Fix 3.7 endpoints table
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\footnotesize}m{2.8cm}|>{\centering\arraybackslash\footnotesize}m{2.0cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash\footnotesize}m{2.0cm}|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.35\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.65\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
)

# Fix 3.10 line 179 and table
f3_txt = f3_txt.replace(
    r"(\texttt{POST /api/documentos/:id/solicitar-revision})",
    "mediante el servicio de solicitud formal de revisión"
)
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.4cm}|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{1.4cm}|>{\raggedright\arraybackslash\footnotesize}X|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.4\hsize\centering\arraybackslash}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
)

# Fix 3.11 line 188 and endpoints table
f3_txt = f3_txt.replace(
    r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\footnotesize}m{3.6cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{2.2cm}|}",
    r"\begin{tabularx}{\textwidth}{|>{\hsize=0.4\hsize\centering\arraybackslash}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}"
)

with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
    f.write(f3_txt)
print("generate_fase3_enhanced.py updated.")

# ==============================================================================
# 3. FASE 4
# ==============================================================================
f4_txt = open("generate_fase4_enhanced.py", encoding="utf-8").read()

# Fix 4.2 line 187
f4_txt = f4_txt.replace(
    r"mediante \texttt{helmet}",
    "mediante la librería de cabeceras seguras Helmet"
)

with open("generate_fase4_enhanced.py", "w", encoding="utf-8") as f:
    f.write(f4_txt)
print("generate_fase4_enhanced.py updated.")

print("All final table fixes applied!")
