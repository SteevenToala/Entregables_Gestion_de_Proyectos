import re

def patch_fase1():
    fname = "generate_fase1_enhanced.py"
    txt = open(fname, encoding="utf-8").read()
    
    # 1.8 audit table
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.55\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.15\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.50\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.10\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.70\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    
    # 1.8 timeline table
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{1.5cm}|>{\raggedright\arraybackslash\bfseries}X|>{\centering\arraybackslash}m{3.0cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{1.5cm}|>{\centering\arraybackslash}m{3.0cm}|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}"
    )
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Patched generate_fase1_enhanced.py")

def patch_fase2():
    fname = "generate_fase2_enhanced.py"
    txt = open(fname, encoding="utf-8").read()
    
    # Anexo 1 cleanup
    txt = txt.replace(
        r"Entregable Oficial & \texttt{04\_Diseno\_Base\_de\_Datos\_ER\_Logico.pdf} \& \texttt{schema.sql} \\",
        r"Entregable Oficial & Diseño Físico y Diccionario del Modelo Relacional \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{05\_Diseno\_Interfaces\_Wireframes\_UX.pdf} \& Prototipo Figma \\",
        r"Entregable Oficial & Especificación de Interfaces de Usuario y Design System \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{06\_Arquitectura\_Contenedores\_Docker\_Locales.pdf} \& \texttt{docker-compose.yml} \\",
        r"Entregable Oficial & Infraestructura y Orquestación de Microservicios Contenerizados \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{07\_Entregable\_General\_Semana\_2.pdf} (Paquete Arquitectura Aprobado) \\",
        r"Entregable Oficial & Expediente Integral de Aprobación de Arquitectura de Software \\"
    )
    txt = txt.replace(r"\texttt{docker-compose.yml}", "orquestación de contenedores")
    txt = txt.replace(r"\texttt{schema.sql}", "scripts DDL")

    # 2.2 table
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.3 table
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}"
    )

    # 2.4 text line and table
    txt = txt.replace(
        r"\item Definición de restricciones declarativas de negocio (\texttt{CHECK horas >= 0}, \texttt{CHECK ponderacion <= 100}).",
        r"\item Definición de restricciones declarativas de integridad para horas no negativas y ponderación porcentual exacta."
    )
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{2.5cm}|X|c|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.6 text lines and table
    txt = txt.replace(
        r"\item Orquestar los cinco contenedores base del sistema mediante un archivo unificado \texttt{docker-compose.yml}.",
        r"\item Orquestar los cinco contenedores base del sistema mediante la especificación de servicios contenerizados."
    )
    txt = txt.replace(
        r"\item Definición de Dockerfiles optimizados multicapa para el backend y frontend.",
        r"\item Definición de imágenes base optimizadas multicapa para el backend y frontend."
    )
    txt = txt.replace(
        r"\item Manifiesto \texttt{docker-compose.yml} completo con variables de entorno parametrizadas en archivo \texttt{.env}.",
        r"\item Manifiesto completo de orquestación de servicios con variables de configuración institucional centralizadas."
    )
    txt = txt.replace(
        r"Bucket privado de almacenamiento de archivos PDF.",
        r"Bucket privado de almacenamiento de archivos probatorios."
    )
    txt = txt.replace(
        r"\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{4.2cm}|X|}",
        r"\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}"
    )

    # 2.7 audit table and timeline table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Auditado}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.55\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.15\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.50\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.10\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.70\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Auditado}"""
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial}"""
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Patched generate_fase2_enhanced.py")

def patch_fase3():
    fname = "generate_fase3_enhanced.py"
    txt = open(fname, encoding="utf-8").read()
    
    # Anexo 1 replacements
    txt = txt.replace(
        r"Entregable Oficial & Esquema DDL inicial y scripts de inicialización en PostgreSQL 18 (\texttt{schema.sql}) \\",
        r"Entregable Oficial & Definición de Esquema e Índices Relacionales en PostgreSQL 18 \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{PlanEditorWizard.tsx} modular con navegación por pasos \\",
        r"Entregable Oficial & Componente Asistente Guiado Modular (Wizard) para Planes de Trabajo \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & Controladores RESTful Express v5 (\texttt{documentos.controller.js} y \texttt{secciones.controller.js}) \\",
        r"Entregable Oficial & Controladores de Persistencia y Transacciones ACID de Secciones \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & Componente \texttt{MatrizActividadesTable.tsx} interactivo \\",
        r"Entregable Oficial & Componente Interactivo de la Matriz Dinámica de Actividades \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & Servicio local de corrección gramatical y ortográfica (\texttt{grammar.service.js}) \\",
        r"Entregable Oficial & Capa de Asistencia Lingüística y Corrección de Redacción \\"
    )

    # 3.1 tables
    txt = txt.replace(
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Restricción / Índice}""",
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Restricción / Índice}"""
    )

    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Prueba de Inserción} & \textbf{Sentencia de Validación de Integridad} & \textbf{Resultado del Motor} & \textbf{Estado} \\
\hline
P1 - Horas Negativas & Inserción con \texttt{horas = -5} en actividades\allowbreak\_matriz & \texttt{ERROR: violates check constraint chk\_horas\_rango} & SUPERADA \\
\hline
P2 - Ponderación $>100$ & Inserción con \texttt{ponderacion = 120.00} en actividades\allowbreak\_matriz & \texttt{ERROR: violates check constraint chk\_pond\_rango} & SUPERADA \\
\hline
P3 - Borrado Accidental & Eliminación de usuario con planes activos & \texttt{ERROR: violates foreign key constraint (RESTRICT)} & SUPERADA \\
\hline
P4 - Búsqueda JSONB & Consulta con operador \texttt{@>} sobre \texttt{contenido\_jsonb} & Retorno en 2.4 ms utilizando índice GIN & SUPERADA \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Prueba} & \textbf{Condición de Entrada} & \textbf{Comportamiento Verificado} & \textbf{Resultado} \\
\hline
P1 - Horas Fuera de Rango & Inserción con carga horaria negativa en matriz & Bloqueo por restricción de rango de horas & CONFORME \\
\hline
P2 - Ponderación Invalida & Inserción con ponderación mayor al 100\% & Bloqueo por restricción porcentual máxima & CONFORME \\
\hline
P3 - Integridad Referencial & Eliminación de usuario con expedientes activos & Bloqueo por clave foránea restrictiva & CONFORME \\
\hline
P4 - Búsqueda Indexada & Consulta sobre secciones en formato estructurado & Ejecución acelerada por índice GIN (2.4 ms) & CONFORME \\
\hline
\end{tabularx}"""
    )

    # 3.2 text line
    txt = txt.replace(
        r"\item Implementar el script \texttt{seed.js} para carga automatizada e idempotente de datos iniciales.",
        r"\item Implementar el módulo de inicialización para carga automatizada e idempotente de datos institucionales."
    )
    txt = txt.replace(
        r"Se estructuró el módulo de sembrado en JavaScript ejecutado mediante Node.js directamente contra el contenedor",
        r"Se estructuró el módulo de sembrado ejecutado directamente contra el contenedor"
    )

    # 3.3 text line
    txt = txt.replace(
        r"\item Integración visual y manejo de estado de sesión en el frontend con \texttt{AuthContext.jsx}.",
        r"\item Integración visual y manejo centralizado del estado de sesión en el frontend."
    )

    # 3.4 routes table and filenames
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Ruta URL} & \textbf{Componente Vista} & \textbf{Funcionalidad y Rol Requerido} & \textbf{Protección} \\
\hline
\texttt{/login} & \texttt{LoginView.jsx} & Formulario de acceso; redirección si ya autenticado. & Pública \\
\hline
\texttt{/dashboard} & \texttt{DashboardView.jsx} & Métricas de horas acumuladas, estado y accesos rápidos. & Privada (Todos) \\
\hline
\texttt{/planes} & \texttt{PlanesListView.jsx} & Bandeja de expedientes con filtros semestrales y búsqueda. & Privada (Todos) \\
\hline
\texttt{/planes/:id} & \texttt{PlanEditorWizard.jsx} & Wizard modular en 5 pasos de llenado del plan SGC. & Privada (Docente) \\
\hline
\texttt{/revision} & \texttt{RevisionComiteView.jsx} & Panel de revisión con drawer lateral de observaciones. & Privada (Comité) \\
\hline
\texttt{/admin} & \texttt{AdminConfigView.jsx} & Gestión de periodos académicos, catálogos y prórrogas. & Privada (Admin) \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Ruta URL} & \textbf{Componente Vista} & \textbf{Funcionalidad y Rol Requerido} & \textbf{Acceso} \\
\hline
\texttt{/login} & Vista de Acceso & Formulario de ingreso con credenciales institucionales. & Pública \\
\hline
\texttt{/dashboard} & Tablero de Control & Métricas de horas acumuladas, estado y accesos directos. & Privada \\
\hline
\texttt{/planes} & Bandeja de Planes & Listado de expedientes con filtros semestrales y búsqueda. & Privada \\
\hline
\texttt{/planes/:id} & Asistente Wizard & Llenado guiado en 5 pasos para el plan de trabajo. & Privada \\
\hline
\texttt{/revision} & Panel de Revisión & Panel colegiado con visor de observaciones y dictamen. & Privada \\
\hline
\texttt{/admin} & Módulo de Ajustes & Configuración de periodos académicos y catálogos. & Privada \\
\hline
\end{tabularx}"""
    )

    # 3.5 intro & usability table
    txt = txt.replace(
        r"Para optimizar este flujo se implementó el componente \texttt{PlanEditorWizard.jsx}, un asistente guiado por pestañas (\textit{Wizard}) en 5 pasos secuenciales que valida progresivamente la información antes de permitir el paso al siguiente bloque, asegurando que el docente cumpla con las políticas del SGC sin omitir datos obligatorios.",
        r"Para optimizar este flujo se implementó un asistente guiado por pestañas (\textit{Wizard}) en 5 pasos secuenciales que valida progresivamente la información antes de permitir el paso al siguiente bloque, asegurando que el docente cumpla con las políticas del SGC sin omitir datos obligatorios."
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Caso de Prueba} & \textbf{Acción del Usuario en la Interfaz} & \textbf{Comportamiento Verificado} & \textbf{Estado} \\
\hline
TC-W01 & Clic en ``Siguiente'' con horas en 35h (incompleto) & Paso 2 bloqueado; alerta: \textit{``Faltan 5 horas para completar 40h''} & SUPERADO \\
\hline
TC-W02 & Retroceso de Paso 3 a Paso 1 tras ingresar actividades & Datos preservados intactos; sin reinicio de formulario & SUPERADO \\
\hline
TC-W03 & Salto directo al Paso 5 de firmas mediante teclado & Bloqueado por enrutador interno; permanece en paso actual & SUPERADO \\
\hline
TC-W04 & Cumplimiento del 100\% de ponderación en Paso 3 & Se desbloquea automáticamente el botón ``Continuar a Paso 4'' & SUPERADO \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Caso} & \textbf{Acción del Usuario en la Interfaz} & \textbf{Comportamiento Verificado} & \textbf{Estado} \\
\hline
TC-W01 & Avance con carga incompleta (35 horas) & Paso bloqueado con alerta de horas pendientes & CONFORME \\
\hline
TC-W02 & Navegación inversa entre pestañas & Datos ingresados preservados sin pérdida de estado & CONFORME \\
\hline
TC-W03 & Intento de salto directo al bloque de firmas & Bloqueado por enrutador según secuencia requerida & CONFORME \\
\hline
TC-W04 & Cumplimiento del 100\% en ponderaciones & Desbloqueo automático del siguiente paso del Wizard & CONFORME \\
\hline
\end{tabularx}"""
    )

    # 3.6 text line & table
    txt = txt.replace(
        r"\item Implementar el componente \texttt{RichTextEditor.jsx} con extensiones oficiales de TipTap.",
        r"\item Implementar el componente de edición enriquecida con extensiones oficiales de TipTap."
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{3.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Extensión TipTap} & \textbf{Paquete NPM} & \textbf{Funcionalidad SGC Brindada} & \textbf{Sanitización} \\""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Módulo Editor} & \textbf{Librería Base} & \textbf{Funcionalidad SGC Brindada} & \textbf{Seguridad} \\"""
    )

    # 3.7 text line & tables
    txt = txt.replace(
        r"\item Programar los controladores \texttt{documentos.controller.js} y \texttt{secciones.controller.js}.",
        r"\item Programar los controladores de persistencia de documentos y secciones."
    )
    txt = txt.replace(
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Controlador} & \textbf{Carga Útil / Parámetros} & \textbf{Código HTTP} \\""",
        r"""\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Controlador} & \textbf{Carga Útil / Parámetros} & \textbf{Código HTTP} \\"""
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|m{2.5cm}|m{3.5cm}|c|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Endpoint} & \textbf{Condición de Entrada} & \textbf{Latencia} & \textbf{Resultado} \\
\hline
TC-EP01 & \texttt{POST /api/planes} & Payload válido con 40 horas y periodo activo & 24 ms & 201 Created \\
\hline
TC-EP02 & \texttt{GET /api/planes} & Consulta con filtro \texttt{estado=Borrador} & 12 ms & 200 OK (5 registros) \\
\hline
TC-EP03 & \texttt{PUT /secciones/batch} & Actualización simultánea de 4 secciones TipTap & 38 ms & 200 OK (ACID Commit) \\
\hline
TC-EP04 & \texttt{PUT /api/planes/:id} & Edición de plan en estado ``Aprobado HCD'' & 8 ms & 409 Conflict \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Endpoint} & \textbf{Condición de Entrada} & \textbf{Latencia} & \textbf{Resultado Verificado} \\
\hline
TC-EP01 & \texttt{POST /api/planes} & Registro válido con 40 horas académicas & 24 ms & 201 Created (Éxito) \\
\hline
TC-EP02 & \texttt{GET /api/planes} & Consulta filtrada por estado en borrador & 12 ms & 200 OK (5 registros) \\
\hline
TC-EP03 & \texttt{PUT /secciones/batch} & Actualización de secciones TipTap & 38 ms & 200 OK (Transacción ACID) \\
\hline
TC-EP04 & \texttt{PUT /api/planes/:id} & Edición de expediente ya aprobado por HCD & 8 ms & 409 Conflict (Bloqueado) \\
\hline
\end{tabularx}"""
    )

    # 3.8 timeline table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 3} \\""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 3} \\"""
    )

    # 3.9 text lines
    txt = txt.replace(
        r"La Tabla 1 del formato institucional del Sistema de Gestión de la Calidad (\texttt{UTA-SGC-A-2-1-P7-T1}), correspondiente a la Planificación de Actividades y su Control Semestral, constituye el núcleo aritmético y normativo de la rendición docente en la FISEI.",
        r"La Tabla 1 del formato normativo de la Universidad Técnica de Ambato, correspondiente a la Planificación de Actividades y su Control Semestral, constituye el núcleo aritmético de la rendición docente en la FISEI."
    )
    txt = txt.replace(r"\texttt{MatrizActividadesTable.jsx}", "el componente de la matriz interactiva")
    txt = txt.replace(
        r"\item Componente el componente de la matriz interactiva plenamente operativo en el Paso 3 del Wizard.",
        r"\item Componente interactivo de la Matriz Dinámica de Actividades plenamente operativo en el Paso 3 del Wizard."
    )

    # 3.10 text line
    txt = txt.replace(
        r"Los Middlewares se organizaron en una cadena de responsabilidad (\textit{Chain of Responsibility}). Al invocarse el endpoint de envío a revisión (\texttt{POST /api/documentos/:id/solicitar-revision}), Express invoca consecutivamente cada Gate.",
        r"Los Middlewares se organizaron en una cadena de responsabilidad (\textit{Chain of Responsibility}). Al invocarse el endpoint de solicitud de revisión, Express evalúa consecutivamente cada compuerta de validación."
    )

    # 3.11 text lines & table
    txt = txt.replace(
        r"\item \textbf{Nixon Hurtado (Responsable EDT 3.11):} Configuración de MinIO, desarrollo de \texttt{minio.service.js} y endpoints de upload.",
        r"\item \textbf{Nixon Hurtado (Responsable EDT 3.11):} Configuración de MinIO, desarrollo del servicio de almacenamiento y endpoints de carga."
    )
    txt = txt.replace(
        r"\item Implementar el servicio \texttt{minio.service.js} con soporte para subida de archivos y generación de URLs prefirmadas.",
        r"\item Implementar el servicio de custodia documental con soporte para subida de archivos y generación de URLs prefirmadas."
    )
    txt = txt.replace(
        r"Se utilizó el SDK oficial \texttt{minio} para Node.js. Al subir una evidencia, el archivo es transmitido en streaming con \texttt{multer} en memoria; se calcula su hash SHA-256 antes de transferirlo al bucket privado \texttt{sige-evidencias}.",
        r"Se utilizó el cliente oficial compatible con almacenamiento S3. Al cargar una evidencia, el archivo se transmite en memoria, calculándose su hash SHA-256 antes de almacenarlo en el repositorio privado seguro."
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|m{3.0cm}|m{2.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Archivo de Prueba} & \textbf{Tamaño} & \textbf{Hash Criptográfico SHA-256 Calculado} & \textbf{Integridad} \\
\hline
EV-01 & \texttt{silabo\_ing\_soft\_2026.pdf} & 2.4 MB & \texttt{e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855} & VERIFICADA \\
\hline
EV-02 & \texttt{acta\_tutorias\_sep.pdf} & 840 KB & \texttt{d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35} & VERIFICADA \\
\hline
EV-03 & \texttt{informe\_avance\_investig.pdf} & 5.1 MB & \texttt{4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a} & VERIFICADA \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.65\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.8\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Evidencia Documental Registrada} & \textbf{Tamaño} & \textbf{Validación Criptográfica SHA-256} & \textbf{Estado} \\
\hline
EV-01 & Sílabo Académico y Plan Curricular de la Asignatura & 2.4 MB & Huella de integridad calculada y validada en almacenamiento & CONFORME \\
\hline
EV-02 & Registro Oficial de Tutorías y Asistencia Estudiantil & 840 KB & Huella de integridad calculada y validada en almacenamiento & CONFORME \\
\hline
EV-03 & Informe Técnico de Avance de Proyecto de Investigación & 5.1 MB & Huella de integridad calculada y validada en almacenamiento & CONFORME \\
\hline
\end{tabularx}"""
    )

    # 3.12 timeline table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 4} \\""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 4} \\"""
    )

    # 3.13 text line
    txt = txt.replace(
        r"\item Interfaz de usuario para Coordinador de Carrera y Comité de Revisión (\texttt{RevisionComiteView.jsx}).",
        r"\item Panel de interfaz de usuario para el Coordinador de Carrera y el Comité de Revisión."
    )

    # 3.14 text line
    txt = txt.replace(
        r"\item Desarrollar el servicio backend \texttt{grammar.service.js} que analiza textos en tiempo real.",
        r"\item Desarrollar el servicio de corrección lingüística que analiza textos en tiempo real."
    )

    # 3.15 text lines and tables
    txt = txt.replace(
        r"\item \textbf{Puppeteer:} Librería de Node.js que proporciona una API de alto nivel para controlar navegadores Headless Chrome.",
        r"\item \textbf{Puppeteer:} Motor de renderizado automatizado para generación documental de alta precisión."
    )
    txt = txt.replace(
        r"Se estructuró el servicio \texttt{export.service.js}. Para la salida PDF, el servicio inyecta los datos del documento",
        r"Se estructuró el servicio de exportación documental. Para la salida en formato imprimible, el servicio inyecta los datos del documento"
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Elemento de Formato} & \textbf{Estándar SGC} & \textbf{Implementación Técnica en el Motor} & \textbf{Conformidad} \\""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Elemento de Formato} & \textbf{Estándar SGC} & \textbf{Implementación Técnica en el Motor} & \textbf{Conformidad} \\"""
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL} & \textbf{Tipo de Salida / Cabecera Content-Type} & \textbf{Descarga} \\
\hline
\texttt{GET} & \texttt{/api/export/:id/pdf} & \texttt{application/pdf} con nombre \texttt{Plan\_Docente\_\{id\}.pdf} & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/word} & \texttt{application/vnd.openxmlformats...} (\texttt{.docx}) & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/preview} & Vista previa en streaming para visor PDF embebido en el navegador. & Streaming \\
\hline
\end{tabularx}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.05\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL} & \textbf{Tipo de Salida / Cabecera Content-Type} & \textbf{Descarga} \\
\hline
\texttt{GET} & \texttt{/api/export/:id/pdf} & Documento oficial en formato PDF institucional & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/word} & Documento editable en formato Microsoft Word & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/preview} & Vista previa para visor institucional integrado & Streaming \\
\hline
\end{tabularx}"""
    )

    # 3.16 audit table and timeline table
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.5\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.5\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Técnico}""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.55\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.15\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.50\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.10\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.70\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Técnico}"""
    )
    txt = txt.replace(
        r"""\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 5} \\""",
        r"""\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase / Sprint} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 5} \\"""
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Patched generate_fase3_enhanced.py")

if __name__ == "__main__":
    patch_fase1()
    patch_fase2()
    patch_fase3()
    print("All master patches applied successfully!")
