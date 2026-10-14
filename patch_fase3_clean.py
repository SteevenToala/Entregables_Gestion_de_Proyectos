# -*- coding: utf-8 -*-
"""
Pinpoint, safe patch for generate_fase3_enhanced.py using exact caption/label boundaries.
"""

def patch_fase3():
    with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
        t = f.read()

    # Checklist & Trello tables
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 3.1: Table names and volumetria
    t = t.replace(r"\texttt{planes\_docente}", r"planes\allowbreak\_docente")
    t = t.replace(r"\texttt{secciones\_documento}", r"secciones\allowbreak\_documento")
    t = t.replace(r"\texttt{actividades\_matriz}", r"actividades\allowbreak\_matriz")
    t = t.replace(r"\texttt{firmas\_documento}", r"firmas\allowbreak\_documento")

    # Volumetria table in 3.1
    idx_vol = t.find(r"\caption{Volumetra estimada para el ciclo acadmico de la FISEI.}")
    if idx_vol != -1:
        s_vol = t.rfind(r"\begin{tabularx}", 0, idx_vol)
        e_vol = t.find(r"}", s_vol + len(r"\begin{tabularx}{\textwidth}")) + 1
        t = t[:s_vol] + r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.55\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.55\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|}" + t[e_vol:]
        print("Replaced 3.1 volumetria table spec!")

    # 3.6: XSS table
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

    idx_xss = t.find(r"\caption{Pruebas de seguridad XSS y desempeo de debounce.}")
    if idx_xss != -1:
        s_xss = t.rfind(r"\begin{tabularx}", 0, idx_xss)
        e_xss = t.rfind(r"\end{tabularx}", 0, idx_xss) + len(r"\end{tabularx}")
        t = t[:s_xss] + new_3_6_table + t[e_xss:]
        print("Replaced 3.6 XSS table!")

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

    idx_red = t.find(r"\caption{Estructura de acciones inmutables del componente React.}")
    if idx_red != -1:
        s_red = t.rfind(r"\begin{tabularx}", 0, idx_red)
        e_red = t.rfind(r"\end{tabularx}", 0, idx_red) + len(r"\end{tabularx}")
        t = t[:s_red] + new_3_9_table + t[e_red:]
        print("Replaced 3.9 Reducer table!")

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

    idx_endp = t.find(r"\caption{Endpoints RESTful para evidencias documentales.}")
    if idx_endp != -1:
        s_endp = t.rfind(r"\begin{tabularx}", 0, idx_endp)
        e_endp = t.rfind(r"\end{tabularx}", 0, idx_endp) + len(r"\end{tabularx}")
        t = t[:s_endp] + new_3_11_table + t[e_endp:]
        print("Replaced 3.11 endpoints table!")

    # 3.13: Observaciones severidad table
    idx_obs = t.find(r"\caption{Clasificacin y comportamiento de observaciones de revisin.}")
    if idx_obs != -1:
        s_obs = t.rfind(r"\begin{tabularx}", 0, idx_obs)
        e_obs = t.find(r"}", s_obs + len(r"\begin{tabularx}{\textwidth}")) + 1
        t = t[:s_obs] + r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}" + t[e_obs:]
        print("Replaced 3.13 observaciones table spec!")

    # 3.14: Reglas gramaticales table
    idx_gram = t.find(r"\caption{Reglas de calidad gramatical y ortogrfica implementadas.}")
    if idx_gram != -1:
        s_gram = t.rfind(r"\begin{tabularx}", 0, idx_gram)
        e_gram = t.find(r"}", s_gram + len(r"\begin{tabularx}{\textwidth}")) + 1
        t = t[:s_gram] + r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\centering\arraybackslash\footnotesize}X|}" + t[e_gram:]
        print("Replaced 3.14 gramatical rules table spec!")

    # 3.15: Parametros exportacion table
    idx_exp = t.find(r"\label{tab:export_matrix}")
    if idx_exp != -1:
        s_exp = t.rfind(r"\begin{tabularx}", 0, idx_exp)
        e_exp = t.find(r"}", s_exp + len(r"\begin{tabularx}{\textwidth}")) + 1
        t = t[:s_exp] + r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}" + t[e_exp:]
        print("Replaced 3.15 export parameters table spec!")

    # 3.16: Hito 5 auditoria table
    idx_hit5 = t.find(r"\label{tab:auditoria_fase3}")
    if idx_hit5 != -1:
        s_hit5 = t.rfind(r"\begin{tabularx}", 0, idx_hit5)
        e_hit5 = t.find(r"}", s_hit5 + len(r"\begin{tabularx}{\textwidth}")) + 1
        t = t[:s_hit5] + r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}" + t[e_hit5:]
        print("Replaced 3.16 Hito 5 auditoria table spec!")

    with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t)
    print("generate_fase3_enhanced.py patched cleanly and safely!")

if __name__ == "__main__":
    patch_fase3()
