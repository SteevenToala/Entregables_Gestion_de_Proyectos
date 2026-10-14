# -*- coding: utf-8 -*-
"""
Pinpoint, safe patch for generate_fase2_enhanced.py.
"""

def patch_fase2():
    with open("generate_fase2_enhanced.py", "r", encoding="utf-8") as f:
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

    # 2.1:
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.2:
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.2 Anexo 2 infrastructure table
    old_infra_pattern = r"""\begin{tabularx}{\textwidth}{|c|c|m{2.2cm}|m{2.5cm}|X|}
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

    new_infra_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}
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

    if old_infra_pattern in t:
        t = t.replace(old_infra_pattern, new_infra_table)
        print("Replaced 2.2 infra table directly!")
    else:
        # try without encoding chars
        idx = t.find(r"\begin{tabularx}{\textwidth}{|c|c|m{2.2cm}|m{2.5cm}|X|}")
        if idx != -1:
            end_idx = t.find(r"\end{tabularx}", idx) + len(r"\end{tabularx}")
            t = t[:idx] + new_infra_table + t[end_idx:]
            print("Replaced 2.2 infra table via slice!")

    # 2.3:
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|>{\raggedright\arraybackslash\footnotesize}X|>{\raggedright\arraybackslash\footnotesize}X|>{\centering\arraybackslash}m{1.8cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.0cm}|X|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.4: Diccionario de datos table
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

    idx_dicc = t.find(r"\label{tab:diccionario_datos}")
    if idx_dicc != -1:
        start_dicc = t.rfind(r"\begin{tabularx}", 0, idx_dicc)
        end_dicc = t.rfind(r"\end{tabularx}", 0, idx_dicc) + len(r"\end{tabularx}")
        t = t[:start_dicc] + new_diccionario_table + t[end_dicc:]
        print("Replaced 2.4 diccionario table via label search!")

    # 2.4: Indices table
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

    idx_ind = t.find(r"\caption{Matriz de ndices fsicos para optimizacin de consultas.}")
    if idx_ind != -1:
        start_ind = t.rfind(r"\begin{tabularx}", 0, idx_ind)
        end_ind = t.rfind(r"\end{tabularx}", 0, idx_ind) + len(r"\end{tabularx}")
        t = t[:start_ind] + new_indices_table + t[end_ind:]
        print("Replaced 2.4 indices table via caption search!")

    # 2.4 Anexo 2 constraints table
    new_constraints_table = r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}
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

    idx_const = t.find(r"\caption{Restricciones e integridad declarativa en la base de datos.}")
    if idx_const != -1:
        start_const = t.rfind(r"\begin{tabularx}", 0, idx_const)
        end_const = t.rfind(r"\end{tabularx}", 0, idx_const) + len(r"\end{tabularx}")
        t = t[:start_const] + new_constraints_table + t[end_const:]
        print("Replaced 2.4 constraints table via caption search!")

    # 2.5:
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{2.4cm}|X|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.6:
    t = t.replace(
        r"\item Definicin de Dockerfiles optimizados multicapa para el backend y frontend.",
        r"\item Definición de especificaciones de construcción multicapa para el backend y frontend."
    )
    t = t.replace(
        r"\subsection{Matriz de Variables de Entorno del Entorno Local (.env)}",
        r"\subsection{Matriz de Variables de Entorno del Entorno Local}"
    )
    t = t.replace(
        r"Aislamiento de credenciales mediante archivo \texttt{.env} protegido",
        r"Aislamiento de credenciales mediante variables de entorno protegidas"
    )

    # 2.6 Docker table
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

    idx_dock = t.find(r"\label{tab:docker_matrix}")
    if idx_dock != -1:
        start_dock = t.rfind(r"\begin{tabularx}", 0, idx_dock)
        end_dock = t.rfind(r"\end{tabularx}", 0, idx_dock) + len(r"\end{tabularx}")
        t = t[:start_dock] + new_docker_table + t[end_dock:]
        print("Replaced 2.6 docker table via label search!")

    # 2.6 Env table
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

    idx_env = t.find(r"\caption{Variables de entorno clave para la orquestacin local.}")
    if idx_env != -1:
        start_env = t.rfind(r"\begin{tabularx}", 0, idx_env)
        end_env = t.rfind(r"\end{tabularx}", 0, idx_env) + len(r"\end{tabularx}")
        t = t[:start_env] + new_env_table + t[end_env:]
        print("Replaced 2.6 env table via caption search!")

    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|m{4.5cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.7:
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|c|c|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )
    t = t.replace(
        r"\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
        f.write(t)
    print("generate_fase2_enhanced.py patched cleanly and safely!")

if __name__ == "__main__":
    patch_fase2()
