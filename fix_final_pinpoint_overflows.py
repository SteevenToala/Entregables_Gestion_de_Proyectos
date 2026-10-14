import re

def fix_fase2():
    fname = "generate_fase2_enhanced.py"
    txt = open(fname, encoding="utf-8").read()

    # 2.3 classes table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Clase de Dominio} & \textbf{Atributos Principales} & \textbf{Métodos de Negocio Clave} & \textbf{Multiplicidad} \\
\hline
\texttt{PlanDocente} & \texttt{id}, \texttt{periodo\_id}, \texttt{docente\_id}, \texttt{estado}, \texttt{horas\_totales} & \texttt{validarHorasMinimas()}, \texttt{avanzarEstado()}, \texttt{solicitarRevision()} & 1 \\
\hline
\texttt{SeccionDocumento} & \texttt{id}, \texttt{plan\_id}, \texttt{orden}, \texttt{titulo}, \texttt{contenido\_html} & \texttt{actualizarContenido()}, \texttt{sanitizarHtml()}, \texttt{bloquearEdicion()} & $1 \dots N$ \\
\hline
\texttt{ActividadMatriz} & \texttt{id}, \texttt{plan\_id}, \texttt{nombre}, \texttt{horas}, \texttt{ponderacion}, \texttt{cronograma} & \texttt{calcularAvance()}, \texttt{asignarMedio()}, \texttt{recalcularPonderacion()} & $1 \dots N$ \\
\hline
\texttt{EvidenciaAdjunta} & \texttt{id}, \texttt{actividad\_id}, \texttt{nombre\_archivo}, \texttt{url\_s3}, \texttt{hash\_sha256} & \texttt{verificarIntegridad()}, \texttt{generarUrlLectura()}, \texttt{asociarHash()} & $0 \dots N$ \\
\hline
\texttt{ObservacionComite} & \texttt{id}, \texttt{plan\_id}, \texttt{usuario\_id}, \texttt{seccion\_id}, \texttt{comentario}, \texttt{resuelto} & \texttt{registrarObservacion()}, \texttt{marcarResuelto()}, \texttt{auditarCambio()} & $0 \dots N$ \\
\hline
\texttt{FirmaDocumento} & \texttt{id}, \texttt{plan\_id}, \texttt{firmante\_id}, \texttt{rol\_firma}, \texttt{fecha\_firma}, \texttt{hash\_firma} & \texttt{estamparFirma()}, \texttt{validarSecuencia()}, \texttt{sellarDocumento()} & $0 \dots 3$ \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Clase de Dominio} & \textbf{Atributos Principales} & \textbf{Métodos de Negocio Clave} & \textbf{Multiplicidad} \\
\hline
\texttt{PlanDocente} & \texttt{id}, \texttt{periodo\_id}, \texttt{docente\_id}, \texttt{estado}, \texttt{horas} & \texttt{validarHorasMinimas()}, \texttt{avanzarEstado()} & 1 \\
\hline
\texttt{Seccion\allowbreak Documento} & \texttt{id}, \texttt{plan\_id}, \texttt{orden}, \texttt{titulo}, \texttt{contenido} & \texttt{actualizarContenido()}, \texttt{sanitizarHtml()} & $1 \dots N$ \\
\hline
\texttt{Actividad\allowbreak Matriz} & \texttt{id}, \texttt{plan\_id}, \texttt{nombre}, \texttt{horas}, \texttt{ponderacion} & \texttt{calcularAvance()}, \texttt{recalcularPond()} & $1 \dots N$ \\
\hline
\texttt{Evidencia\allowbreak Adjunta} & \texttt{id}, \texttt{actividad\_id}, \texttt{url\_s3}, \texttt{hash\_sha256} & \texttt{verificarIntegridad()}, \texttt{generarUrl()} & $0 \dots N$ \\
\hline
\texttt{Observacion\allowbreak Comite} & \texttt{id}, \texttt{plan\_id}, \texttt{usuario\_id}, \texttt{comentario} & \texttt{registrarObservacion()}, \texttt{marcarResuelto()} & $0 \dots N$ \\
\hline
\texttt{Firma\allowbreak Documento} & \texttt{id}, \texttt{plan\_id}, \texttt{firmante\_id}, \texttt{rol\_firma} & \texttt{estamparFirma()}, \texttt{validarSecuencia()} & $0 \dots 3$ \\
\hline
\end{tabularx}"""
    )

    # 2.4 indices table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del Índice} & \textbf{Tabla Objetivo} & \textbf{Columnas Indexadas y Tipo de Índice} & \textbf{Propósito} \\
\hline
\texttt{idx\_planes\_docente\_periodo} & \texttt{planes\_docente} & \texttt{(fk\_docente, fk\_periodo)} -- B-Tree & Búsqueda rápida de expedientes activos. \\
\hline
\texttt{idx\_actividades\_plan} & \texttt{actividades\_matriz} & \texttt{(fk\_plan)} -- B-Tree & Agrupación de actividades de la matriz. \\
\hline
\texttt{idx\_secciones\_jsonb} & \texttt{secciones\_documento} & \texttt{contenido\_jsonb} -- GIN (\texttt{jsonb\_path\_ops}) & Búsqueda rápida de texto en secciones. \\
\hline
\texttt{idx\_firmas\_plan\_orden} & \texttt{firmas\_documento} & \texttt{(fk\_plan, orden)} -- B-Tree UNIQUE & Garantiza secuencia estricta de firmas. \\
\hline
\texttt{idx\_evidencias\_hash} & \texttt{evidencias\_adjuntas} & \texttt{hash\_sha256} -- B-Tree & Prevención de duplicados de archivos. \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.25\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del Índice} & \textbf{Tabla Objetivo} & \textbf{Columnas y Tipo} & \textbf{Propósito} \\
\hline
\texttt{idx\_planes\_\allowbreak doc\_periodo} & \texttt{planes\_\allowbreak docente} & \texttt{(fk\_doc, fk\_per)} B-Tree & Búsqueda rápida de expedientes activos. \\
\hline
\texttt{idx\_actividades\_\allowbreak plan} & \texttt{actividades\_\allowbreak matriz} & \texttt{(fk\_plan)} B-Tree & Agrupación de actividades de la matriz. \\
\hline
\texttt{idx\_secciones\_\allowbreak jsonb} & \texttt{secciones\_\allowbreak documento} & \texttt{contenido} GIN & Búsqueda rápida de texto en secciones. \\
\hline
\texttt{idx\_firmas\_\allowbreak plan\_orden} & \texttt{firmas\_\allowbreak documento} & \texttt{(fk\_plan, orden)} UNIQUE & Garantiza secuencia estricta de firmas. \\
\hline
\texttt{idx\_evidencias\_\allowbreak hash} & \texttt{evidencias\_\allowbreak adjuntas} & \texttt{hash\_sha256} B-Tree & Prevención de duplicados de archivos. \\
\hline
\end{tabularx}"""
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Fixed Fase 2 pinpoint overflows")

def fix_fase3():
    fname = "generate_fase3_enhanced.py"
    txt = open(fname, encoding="utf-8").read()

    # 3.6 table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Módulo Editor} & \textbf{Librería Base} & \textbf{Funcionalidad SGC Brindada} & \textbf{Seguridad} \\
\hline
\texttt{StarterKit} & \texttt{@tiptap/starter-kit} & Párrafos, negrita, cursiva, listas ordenadas y viñetas. & Estándar W3C \\
\hline
\texttt{Heading} & \texttt{@tiptap/extension-heading} & Subsecciones estructuradas (niveles H2 y H3). & Filtrado de atributos \\
\hline
\texttt{Table} & \texttt{@tiptap/extension-table} & Tablas con celdas combinadas para anexos descriptivos. & Limpieza de scripts \\
\hline
\texttt{Placeholder} & \texttt{@tiptap/extension-placeholder} & Texto guía institucional cuando la sección está vacía. & No persistido \\
\hline
\texttt{CharacterCount} & \texttt{@tiptap/extension-character-count} & Límite máximo de 2500 palabras por sección institucional. & Validación cliente \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.85\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Módulo Editor} & \textbf{Librería Base} & \textbf{Funcionalidad SGC Brindada} & \textbf{Seguridad} \\
\hline
Editor Básico & TipTap StarterKit & Párrafos, negrita, cursiva, listas ordenadas y viñetas. & Estándar W3C \\
\hline
Encabezados & TipTap Heading & Subsecciones estructuradas (niveles H2 y H3). & Filtrado W3C \\
\hline
Tablas Dinámicas & TipTap Table & Tablas con celdas combinadas para anexos descriptivos. & Limpieza scripts \\
\hline
Texto Guía & TipTap Placeholder & Texto guía institucional cuando la sección está vacía. & No persistido \\
\hline
Control Longitud & TipTap CharCount & Límite máximo de 2500 palabras por sección institucional. & Validación cliente \\
\hline
\end{tabularx}"""
    )

    # 3.7 endpoints table
    txt = txt.replace(
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Controlador} & \textbf{Carga Útil / Parámetros} & \textbf{Código HTTP} \\
\hline
\texttt{GET} & \texttt{/api/planes} & \texttt{listarPlanes} & Filtros: \texttt{?periodo\_id=\&estado=} & 200 OK \\
\hline
\texttt{POST} & \texttt{/api/planes} & \texttt{crearPlan} & \texttt{\{periodo\_id, carrera\_id, dedicacion\}} & 201 Created \\
\hline
\texttt{GET} & \texttt{/api/planes/:id} & \texttt{obtenerPlan} & Parámetro URL \texttt{id} (UUID) & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/planes/:id} & \texttt{actualizarPlan} & \texttt{\{horas\_totales, estado\}} & 200 OK \\
\hline
\texttt{GET} & \texttt{/api/secciones/:planId} & \texttt{listarSecciones} & Parámetro URL \texttt{planId} & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/secciones/batch} & \texttt{actualizarBatch} & \texttt{\{secciones: [\{id, contenido\}]\}} & 200 OK \\
\hline
\end{tabularx}""",
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Controlador} & \textbf{Carga Útil / Parámetros} & \textbf{Código HTTP} \\
\hline
\texttt{GET} & \texttt{/api/planes} & \texttt{listarPlanes} & Filtros: \texttt{?periodo\_id=\&estado=} & 200 OK \\
\hline
\texttt{POST} & \texttt{/api/planes} & \texttt{crearPlan} & \texttt{\{periodo\_id, carrera\_id, dedicacion\}} & 201 Created \\
\hline
\texttt{GET} & \texttt{/api/planes/:id} & \texttt{obtenerPlan} & Parámetro URL \texttt{id} (UUID) & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/planes/:id} & \texttt{actualizarPlan} & \texttt{\{horas\_totales, estado\}} & 200 OK \\
\hline
\texttt{GET} & \texttt{/api/secciones/\allowbreak :planId} & \texttt{listarSecciones} & Parámetro URL \texttt{planId} & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/secciones/\allowbreak batch} & \texttt{actualizarBatch} & \texttt{\{secciones: [\{id, contenido\}]\}} & 200 OK \\
\hline
\end{tabularx}"""
    )

    # 3.15 preview endpoint
    txt = txt.replace(
        r"\texttt{GET} & \texttt{/api/export/:id/preview} & Vista previa para visor institucional integrado & Streaming \\",
        r"\texttt{GET} & \texttt{/api/export/\allowbreak :id/preview} & Vista previa para visor institucional integrado & Streaming \\"
    )
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.05\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.20\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.75\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 3.16 Línea Base table
    txt = txt.replace(
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 5} \\""",
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 5} \\"""
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Fixed Fase 3 pinpoint overflows")

if __name__ == "__main__":
    fix_fase2()
    fix_fase3()
    print("All pinpoint fixes complete!")
