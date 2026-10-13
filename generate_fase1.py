import os
from template_engine import render_doc

def generate_fase1():
    base_dir = os.path.join("Entregables_Latex", "Fase_1")
    os.makedirs(base_dir, exist_ok=True)

    # 1.1
    b1_1 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Levantamiento de Información del Proceso Actual (Diagnóstico As-Is) -- Código EDT: 1.1

\section{Introducción}
En la Universidad Técnica de Ambato (UTA), específicamente en la Facultad de Ingeniería en Sistemas, Electrónica e Industrial (FISEI), la gestión académica semestral exige el cumplimiento de los procesos estipulados por el Sistema de Gestión de Calidad (SGC). Actualmente, la planificación y rendición de cuentas del cuerpo docente se lleva a cabo mediante plantillas ofimáticas desacopladas (\texttt{.docx} y \texttt{.xlsx}) correspondientes a los formatos institucionales \texttt{UTA-SGC-A-2-1-P7-T1} (Plan de Trabajo) y \texttt{UTA-SGC-A-2-1-P7-T2} (Informe de Cumplimiento). El presente entregable documenta el diagnóstico técnico y operativo exhaustivo del estado actual (\textit{As-Is}), delimitando las ineficiencias críticas que motivan el desarrollo del sistema web SIGE.

\section{Objetivo}
\subsection{Objetivo General}
Diagnosticar exhaustivamente el flujo operativo actual de elaboración, revisión, aprobación y custodia de planes de trabajo e informes del SGC en la FISEI, identificando cuellos de botella y requerimientos base para el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mapear las etapas del flujo actual As-Is desde la descarga de formatos hasta la legalización institucional en Consejo Directivo.
    \item Catalogar cuantitativa y cualitativamente los cuellos de botella operativos mediante una matriz de problemas (P-01 a P-06).
    \item Establecer la línea base de tiempos, costos y riesgos del proceso manual previo a la automatización.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mapeo integral de los formatos SGC institucionales \texttt{P7-T1} y \texttt{P7-T2}.
    \item Entrevistas a docentes titulares, coordinadores de área y coordinadores de carrera de la FISEI.
    \item Levantamiento de evidencias sobre extravío de documentos y asimetría de versiones.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Procesos de nómina financiera y remuneraciones del departamento de Talento Humano.
    \item Trámites administrativos no relacionados directamente con el quehacer académico docente.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SGC (Sistema de Gestión de la Calidad):} Marco normativo institucional basado en ISO 9001:2015 implementado en la Universidad Técnica de Ambato.
    \item \textbf{As-Is:} Modelo descriptivo del estado operacional actual del proceso sin intervención tecnológica moderna.
    \item \textbf{Plan de Trabajo Docente (P7-T1):} Instrumento prospectivo semestral donde el docente planifica horas y metas de docencia, investigación y vinculación.
    \item \textbf{Informe de Cumplimiento (P7-T2):} Instrumento retrospectivo en el cual se reporta el porcentaje de avance ejecutado y se justifican las horas asignadas.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado / Steeven Toala (Responsables EDT 1.1):} Ejecución de entrevistas, análisis de artefactos documentales y mapeo formal del flujo As-Is.
    \item \textbf{Heidi Villavicencio (Analista):} Consolidación de la matriz de hallazgos y verificación de estándares SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Supervisión metodológica y aprobación del alcance del diagnóstico.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Reglamento de Carrera y Escalafón del Profesor e Investigador del CES:} Disposiciones de dedicación horaria y rendición de cuentas.
    \item \textbf{Norma ISO 9001:2015 (Cláusula 7.5):} Control de la información documentada institucional.
    \item \textbf{Manual de Procesos SGC - FISEI UTA:} Procedimientos \texttt{P7} de gestión de la docencia y evaluación semestral.
\end{itemize}

\section{Método, Políticas y Contenidos}
Para el levantamiento se aplicaron entrevistas estructuradas a 8 docentes y 2 coordinadores de carrera, análisis documental de 30 planes e informes del período precedente, y diagramación de flujo bajo estándar BPMN.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_01_diagrama_as_is.png}
    \caption{Diagrama de Flujo del Proceso Actual As-Is (Flujo Manual y Descentralizado SGC).}
    \label{fig:diag_as_is}
\end{figure}

\section{Descripción de actividades}
\subsection{Matriz de Problemas y Cuellos de Botella (P-01 a P-06)}
A continuación se sintetizan los hallazgos críticos detectados en la auditoría del proceso actual:

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Problema Detectado} & \textbf{Impacto Operativo} & \textbf{Evidencia Observada} \\
\hline
\textbf{P-01} & Asimetría de versiones & Docentes y coordinadores manejan archivos distintos enviados por correo electrónico. & Se encontraron hasta 4 versiones preliminares en bandejas de entrada sin control. \\
\hline
\textbf{P-02} & Extravío de evidencias & Enlaces de Google Drive caídos o permisos privados impiden la auditoría. & El 35\% de los informes no contaba con anexos accesibles durante auditorías de calidad. \\
\hline
\textbf{P-03} & Errores de cálculo en matrices & Inconsistencias aritméticas en sumas de ponderación horaria que no totalizan el 100\%. & Discrepancias recurrentes entre horas planificadas y porcentajes declarados. \\
\hline
\textbf{P-04} & Carga burocrática excesiva & El docente invierte 8 horas hombre por informe en maquetación y transcripción manual. & Más de 1,800 horas docentes anuales desperdiciadas en burocracia de oficina. \\
\hline
\textbf{P-05} & Ausencia de control temporal & Modificaciones extemporáneas sin sellado de tiempo ni registro de auditoría. & Informes fechados manualmente sin trazabilidad cronológica verificable. \\
\hline
\textbf{P-06} & Desconexión Plan vs Informe & El docente debe volver a copiar y pegar las actividades del Plan al generar el Informe. & Errores de tipeo y alteración involuntaria de objetivos originales. \\
\hline
\end{tabularx}
\caption{Matriz de Cuellos de Botella y Deficiencias del Proceso As-Is.}
\label{tab:problemas_as_is}
\end{table}

\subsection{Línea Base del Proceso}
El diagnóstico confirmó que el proceso actual presenta una tasa de reproceso del 42\% en la primera revisión por parte de los coordinadores de área, originada principalmente por falta de evidencias y sumatorias inconsistentes. Esta línea base sustenta la necesidad de implementar compuertas lógicas preventivas (Validation Gates).
"""
    anx1_1 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Formato Oficial \texttt{UTA-SGC-A-2-1-P7-T1} (Plan de Trabajo).
\item \textbf{Anexo 2:} Formato Oficial \texttt{UTA-SGC-A-2-1-P7-T2} (Informe de Cumplimiento).
\end{itemize}"""
    doc1_1 = render_doc("TI-SIGE-ENT-F1-001", "INGENIERÍA DE REQUERIMIENTOS / DIAGNÓSTICO AS-IS", "14/08/2026", "14/08/2026", "LEVANTAMIENTO DE INFORMACIÓN DEL PROCESO ACTUAL", b1_1, "14/08/2026", anx1_1)
    with open(os.path.join(base_dir, "1.1_Levantamiento_Informacion_Proceso_Actual.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_1)

    # 1.2
    b1_2 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Identificación de Actores y Procesos (Matriz de Stakeholders) -- Código EDT: 1.2

\section{Introducción}
El éxito en la adopción del sistema SIGE dentro de la FISEI requiere un análisis riguroso de los actores organizacionales que intervienen en el ciclo de vida de los planes de trabajo e informes institucionales. El Sistema de Gestión de Calidad establece una cadena jerárquica con responsabilidades claramente delimitadas, desde la docencia de aula hasta las autoridades de facultad. El presente informe formaliza el mapa de macroprocesos institucionales y la matriz de interesados (Stakeholders), clasificando a cada actor según su nivel de poder e interés para orientar el diseño de roles en la plataforma.

\section{Objetivo}
\subsection{Objetivo General}
Identificar, mapear y caracterizar formalmente a los actores organizacionales y los macroprocesos institucionales que interactúan con el Sistema de Gestión de Calidad en la FISEI, estructurando la Matriz de Stakeholders del proyecto SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Identificar las funciones institucionales de los roles: Docente Elaborador, Coordinador de Área, Coordinador de Carrera, Subdecano y Administrador SGC.
    \item Analizar la matriz de Poder versus Interés según la metodología estándar del PMBOK.
    \item Modelar la taxonomía de macroprocesos académicos y de gestión de la facultad.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Comunidad académica de la FISEI: cuerpo docente titular y ocasional, directores de área y autoridades.
    \item Mapeo de expectativas, canales de comunicación y requerimientos clave por actor.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Entidades externas fuera del organigrama de la Universidad Técnica de Ambato.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Stakeholder (Interesado):} Individuo o grupo que puede afectar, verse afectado o percibirse afectado por las decisiones o resultados del proyecto.
    \item \textbf{Docente Elaborador:} Profesor responsable de la carga horaria semestral y de registrar sus avances y evidencias.
    \item \textbf{Coordinador de Área:} Autoridad académica intermedia que revisa la pertinencia técnica de las asignaturas afines.
    \item \textbf{Coordinador de Carrera:} Máxima autoridad de la carrera responsable de la consolidación curricular y aprobación previa.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 1.2):} Elaboración de la matriz de interesados, diagramación de cuadrantes y mapeo de roles.
    \item \textbf{Steeven Toala (Líder Técnico):} Revisión de coherencia arquitectónica y asignación de permisos preliminares.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la matriz institucional de actores.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Estatuto Orgánico de la Universidad Técnica de Ambato:} Estructura orgánica y funciones de directores, coordinadores y docentes.
    \item \textbf{Guía del PMBOK (7ma Edición):} Gestión del involucramiento de las partes interesadas.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó el modelo bidimensional de Poder e Interés. Se realizaron talleres de alineación con directores de área para verificar responsabilidades y evitar solapamientos funcionales.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/s1_02_macroprocesos.png}
    \caption{Mapa de Macroprocesos Institucionales de la FISEI y Articulación con SIGE.}
    \label{fig:s1_02_macro}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth,height=5.0cm,keepaspectratio]{images/s1_02_quadrant_chart.png}
    \caption{Matriz de Cuadrantes Poder vs. Interés para Interesados del Proyecto SIGE.}
    \label{fig:s1_02_quad}
\end{figure}

\section{Descripción de actividades}
\subsection{Matriz Detallada de Actores y Roles Organizacionales}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.8cm}|c|c|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Rol Institucional} & \textbf{Poder} & \textbf{Interés} & \textbf{Estrategia de Gestión} & \textbf{Requerimiento Central en SIGE} \\
\hline
Docente Elaborador & Medio & Alto & Mantener Informado / Facilitar Trabajo & Interfaz ágil, autoguardado, cálculo automático y alertas de entrega. \\
\hline
Coordinador de Área & Alto & Alto & Gestionar de Cerca & Panel de observaciones granulares por sección y devolución ágil. \\
\hline
Coordinador de Carrera & Alto & Alto & Gestionar de Cerca & Vista consolidada de la carrera, métricas de avance y firma digital. \\
\hline
Subdecano / Consejo Directivo & Muy Alto & Medio & Mantener Satisfecho & Reportes consolidados ejecutivos, exportación oficial SGC y actas. \\
\hline
Administrador SGC & Alto & Alto & Colaborar Estrechamente & Parametrización de catálogos, fechas límite y auditoría de cambios. \\
\hline
\end{tabularx}
\caption{Matriz de Caracterización y Estrategia de Interesados.}
\label{tab:stakeholders}
\end{table}

\subsection{Definición de Canales de Interacción y Estados}
Se definieron tres fases secuenciales de interacción: Elaboración Docente, Evaluación Colegiada y Legalización Institucional.
"""
    anx1_2 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Ficha de Caracterización de Roles de la FISEI.
\end{itemize}"""
    doc1_2 = render_doc("TI-SIGE-ENT-F1-002", "INGENIERÍA DE REQUERIMIENTOS / GESTIÓN DE INTERESADOS", "18/08/2026", "18/08/2026", "IDENTIFICACIÓN DE ACTORES Y PROCESOS", b1_2, "18/08/2026", anx1_2)
    with open(os.path.join(base_dir, "1.2_Identificacion_Actores_y_Procesos.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_2)

    # 1.3
    b1_3 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Especificación de Requisitos de Software (SRS IEEE 830) -- Código EDT: 1.3

\section{Introducción}
La especificación rigurosa de los requerimientos constituye el cimiento para el diseño y construcción del sistema SIGE. Siguiendo el estándar internacional IEEE 830 y los lineamientos de calidad ISO/IEC 25010, se formalizan en este informe los 24 requerimientos funcionales (RF-01 a RF-24) y 10 requerimientos no funcionales (RNF-01 a RNF-10) que rigen la arquitectura y el comportamiento del software. Cada requerimiento ha sido clasificado por módulo de negocio y ponderado por criticidad para garantizar la completa digitalización de los formatos SGC \texttt{P7-T1} y \texttt{P7-T2}.

\section{Objetivo}
\subsection{Objetivo General}
Especificar de manera formal, completa y verificable los requisitos funcionales y no funcionales del sistema SIGE bajo el estándar IEEE 830, alineados con el Sistema de Gestión de Calidad institucional de la FISEI.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Formalizar los 24 requerimientos funcionales estructurados en 7 módulos del sistema.
    \item Definir los 10 requisitos no funcionales bajo las dimensiones de ISO/IEC 25010 (Seguridad, Rendimiento, Usabilidad, Confiabilidad).
    \item Construir la matriz de trazabilidad entre necesidades SGC y requisitos técnicos.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Módulos de Autenticación RBAC, Wizard de Edición, Matriz Dinámica, MinIO S3, Revisión de Comité, Asistencia Ortográfica y Motor de Exportación.
    \item Criterios de aceptación comprobables y métricas objetivas de cumplimiento.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Requerimientos de sistemas externos de matriculación no cubiertos por las APIs expuestas.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{IEEE 830-1998:} Práctica recomendada para la especificación de requerimientos de software.
    \item \textbf{ISO/IEC 25010:} Modelo de calidad para sistemas y productos de software.
    \item \textbf{RF (Requisito Funcional):} Declaración de servicios que el sistema debe prestar y cómo debe reaccionar ante entradas específicas.
    \item \textbf{RNF (Requisito No Funcional):} Restricción sobre los servicios o funciones ofrecidos por el sistema (rendimiento, seguridad, disponibilidad).
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio / Andrea Vásquez (Responsables EDT 1.3):} Redacción formal de la especificación IEEE 830, criterios de aceptación y RNFs.
    \item \textbf{Steeven Toala (Arquitecto de Software):} Validación de viabilidad arquitectónica de los requisitos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación técnica del pliego de requisitos SRS.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{IEEE Std 830-1998:} Recommended Practice for Software Requirements Specifications.
    \item \textbf{ISO/IEC 25010:2011:} Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE).
\end{itemize}

\section{Método, Políticas y Contenidos}
La especificación se organizó modularmente. En la Figura \ref{fig:s1_03_rf} se ilustra la distribución de los 24 Requisitos Funcionales en los módulos del sistema SIGE.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/s1_03_modulos_rf.png}
    \caption{Arquitectura Modular de Requerimientos Funcionales del Sistema SIGE.}
    \label{fig:s1_03_rf}
\end{figure}

\section{Descripción de actividades}
\subsection{Catálogo de Requerimientos Funcionales (RF-01 a RF-24)}

\begin{table}[htbp]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.6cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Módulo} & \textbf{Descripción Funcional} & \textbf{Prioridad} \\
\hline
\textbf{RF-01} & Autenticación & Inicio de sesión seguro con credenciales institucionales y generación de JWT. & Alta \\
\hline
\textbf{RF-02} & Autenticación & Control de acceso basado en roles (Docente, Coordinador, Subdecano, Admin). & Alta \\
\hline
\textbf{RF-03} & Wizard Edición & Creación y gestión de borradores de Plan de Trabajo e Informe de Cumplimiento. & Alta \\
\hline
\textbf{RF-04} & Wizard Edición & Navegación modular por pestañas con validación previa de avance de paso. & Alta \\
\hline
\textbf{RF-05} & Editor TipTap & Edición de texto enriquecido para secciones descriptivas del formato SGC. & Alta \\
\hline
\textbf{RF-06} & Editor TipTap & Mecanismo de autoguardado asíncrono con debounce de 1500 ms y aviso visual. & Alta \\
\hline
\textbf{RF-07} & Matriz Dinámica & Registro dinámico de actividades académicas con horas y fechas de ejecución. & Alta \\
\hline
\textbf{RF-08} & Matriz Dinámica & Validación automática de suma de ponderaciones que obligue al 100\%. & Crítica \\
\hline
\textbf{RF-09} & Matriz Dinámica & Cálculo matemático ponderado en tiempo real del porcentaje de avance global. & Alta \\
\hline
\textbf{RF-10} & MinIO S3 & Carga en streaming de archivos PDF de evidencia hacia almacenamiento S3. & Alta \\
\hline
\textbf{RF-11} & MinIO S3 & Cálculo y persistencia del hash SHA-256 inmutable de cada archivo cargado. & Alta \\
\hline
\textbf{RF-12} & MinIO S3 & Generación de URLs prefirmadas de visualización segura con expiración de 60 min. & Media \\
\hline
\textbf{RF-13} & Validation Gates & Bloqueo preventivo de envío si el avance es mayor a 0\% y no hay evidencias. & Crítica \\
\hline
\textbf{RF-14} & Validation Gates & Validación de fechas de actividades contra el calendario académico oficial. & Alta \\
\hline
\textbf{RF-15} & Revisión Comité & Bandeja de revisión para Coordinadores de Área y Carrera con filtro por estado. & Alta \\
\hline
\textbf{RF-16} & Revisión Comité & Motor de observaciones granulares a nivel de sección o actividad específica. & Alta \\
\hline
\textbf{RF-17} & Cascada Firmas & Circuito de firmas de 3 niveles (Elaborador, Revisor, Aprobador) en serie. & Alta \\
\hline
\textbf{RF-18} & Cascada Firmas & Bloqueo de edición del documento una vez estampado el primer nivel de firma. & Crítica \\
\hline
\textbf{RF-19} & Corrección Texto & Integración con microservicio local LanguageTool para corrección ortográfica. & Media \\
\hline
\textbf{RF-20} & Asistencia Redacción & Asistencia de redacción académica formal mediante Google Gemini API. & Media \\
\hline
\textbf{RF-21} & Motor Exportación & Generación de archivos PDF oficiales idénticos a los formatos SGC P7-T1 y P7-T2. & Alta \\
\hline
\textbf{RF-22} & Motor Exportación & Generación de archivos DOCX editables con cabeceras y logos institucionales. & Media \\
\hline
\textbf{RF-23} & Auditoría & Registro inmutable de bitácora con estampas de tiempo, usuario y acción. & Alta \\
\hline
\textbf{RF-24} & Gestión Extemporánea & Solicitud y desbloqueo supervisado de edición fuera de plazo con justificación. & Media \\
\hline
\end{tabularx}
\caption{Catálogo de Requisitos Funcionales del Sistema SIGE.}
\label{tab:rf}
\end{table}

\subsection{Requisitos No Funcionales (RNF-01 a RNF-10)}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{2.8cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Dimensión} & \textbf{Especificación Técnica} & \textbf{Métrica} \\
\hline
\textbf{RNF-01} & Rendimiento & Tiempo de respuesta de endpoints de persistencia y consultas. & $< 500$ ms \\
\hline
\textbf{RNF-02} & Rendimiento & Tiempo de generación y descarga de informes consolidados en PDF. & $< 3$ s \\
\hline
\textbf{RNF-03} & Seguridad & Cifrado de contraseñas con algoritmo bcrypt (factor de costo 10). & Inalterable \\
\hline
\textbf{RNF-04} & Seguridad & Tokens JWT firmados con HMAC-SHA256 y expiración máxima de 2 horas. & 120 min \\
\hline
\textbf{RNF-05} & Integridad & Hashes SHA-256 inmutables para toda evidencia almacenada en MinIO. & 256 bits \\
\hline
\textbf{RNF-06} & Disponibilidad & Disponibilidad de los servicios orquestados en contenedores Docker. & $99.5\%$ \\
\hline
\textbf{RNF-07} & Usabilidad & Diseño responsivo para pantallas móviles (375px) hasta escritorio (1920px). & CSS Fluido \\
\hline
\textbf{RNF-08} & Accesibilidad & Contraste cromático y navegación accesible según estándar WCAG 2.1. & Nivel AA \\
\hline
\textbf{RNF-09} & Mantenibilidad & Arquitectura modular desacoplada con separación estricta de capas. & Clean Arch \\
\hline
\textbf{RNF-10} & Portabilidad & Despliegue estandarizado de dependencias mediante Docker Compose. & Multiplataforma \\
\hline
\end{tabularx}
\caption{Especificación de Requisitos No Funcionales bajo ISO/IEC 25010.}
\label{tab:rnf}
\end{table}
"""
    anx1_3 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Matriz de Trazabilidad Requisitos vs. Estándar SGC.
\end{itemize}"""
    doc1_3 = render_doc("TI-SIGE-ENT-F1-003", "INGENIERÍA DE REQUERIMIENTOS / ESPECIFICACIÓN FORMAL", "21/08/2026", "21/08/2026", "DEFINICIÓN DE REQUISITOS FUNCIONALES Y NO FUNCIONALES", b1_3, "21/08/2026", anx1_3)
    with open(os.path.join(base_dir, "1.3_Definicion_Requisitos_Funcionales_y_No_Funcionales.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_3)

    # 1.4
    b1_4 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Definición del Alcance, Restricciones y Objetivos SGC -- Código EDT: 1.4

\section{Introducción}
La delimitación formal del alcance del software previene la dispersión del esfuerzo técnico (Scope Creep) y asegura que todos los entregables converjan hacia la modernización de los procesos SGC de la FISEI. En este documento se especifican con precisión los límites del sistema, las integraciones con servicios institucionales, las restricciones técnicas y los objetivos estratégicos formulados bajo criterios SMART.

\section{Objetivo}
\subsection{Objetivo General}
Definir de manera formal las fronteras, restricciones técnicas, supuestos y objetivos SMART del sistema SIGE, garantizando el cumplimiento irrestricto de los formatos SGC de la FISEI.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Delimitar las funcionalidades formalmente incluidas (In-Scope) y las exclusiones explícitas (Out-of-Scope).
    \item Formular los objetivos SMART del proyecto con metas cuantificables a corto y mediano plazo.
    \item Identificar las restricciones de arquitectura, licenciamiento de software libre y calendarios.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Digitalización integral de los formatos \texttt{UTA-SGC-A-2-1-P7-T1} y \texttt{UTA-SGC-A-2-1-P7-T2}.
    \item Interfaz Web SPA, API Backend RESTful, Base de Datos PostgreSQL 18, MinIO S3 y LanguageTool.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Módulos de nómina o pagos y control biométrico físico de asistencia docente.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Scope Creep:} Expansión incontrolada del alcance de un proyecto sin ajustes en tiempo ni costos.
    \item \textbf{Objetivos SMART:} Objetivos Específicos (Specific), Medibles (Measurable), Alcanzables (Achievable), Relevantes (Relevant) y Temporales (Time-bound).
    \item \textbf{Frontera del Sistema:} Perímetro que define qué responsabilidades residen dentro de la plataforma y cuáles son externas.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Heidi Villavicencio (Responsables EDT 1.4):} Delimitación de fronteras, definición de objetivos SMART y análisis de restricciones.
    \item \textbf{Nixon Hurtado (Backend):} Validación de restricciones de almacenamiento y base de datos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del alcance y límites del proyecto.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición):} Gestión del Alcance del Proyecto.
    \item \textbf{Manual de Calidad Institucional UTA:} Sección de Control Operacional de Documentos.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó análisis de límites y descomposición funcional. En la Figura \ref{fig:s1_04_alcance} se ilustra el esquema de límites y fronteras del sistema.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/s1_04_alcance.png}
    \caption{Diagrama de Fronteras y Alcance Operacional del Sistema SIGE.}
    \label{fig:s1_04_alcance}
\end{figure}

\section{Descripción de actividades}
\subsection{Objetivos SMART del Sistema SIGE}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{No.} & \textbf{Objetivo SMART} & \textbf{Mecanismo de Verificación} & \textbf{Meta} \\
\hline
\textbf{Obj-01} & Reducción de tiempo docente & Medición de tiempo invertido en la elaboración del informe semestral. & Reducir de 8h a 1.5h ($81\%$) \\
\hline
\textbf{Obj-02} & Cero errores aritméticos & Validación estricta por Validation Gate de sumatorias del 100\%. & $0\%$ errores de cálculo \\
\hline
\textbf{Obj-03} & Evidencias auditables & Almacenamiento seguro en MinIO con hash SHA-256 y URLs prefirmadas. & $100\%$ evidencias íntegras \\
\hline
\textbf{Obj-04} & Agilidad en revisiones & Reducción del ciclo de observaciones de coordinadores de área. & De 15 días a 3 días hábiles \\
\hline
\textbf{Obj-05} & Adopción en FISEI & Registro y legalización de informes en la carrera de Software. & $100\%$ docentes involucrados \\
\hline
\end{tabularx}
\caption{Matriz de Objetivos SMART del Proyecto SIGE.}
\label{tab:smart}
\end{table}

\subsection{Restricciones Técnicas y Operativas}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Restricción de Infraestructura:} Despliegue completo sobre Docker sin dependencias de licencias propietarias de pago.
    \item \textbf{Restricción de Almacenamiento:} Cuota de 25 MB por archivo adjunto y formatos limitados estrictamente a PDF.
    \item \textbf{Restricción de Formato:} La salida exportada debe mantener idéntica fidelidad tipográfica con los formatos SGC oficiales.
\end{itemize}
"""
    anx1_4 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Matriz de Criterios de Aceptación del Alcance.
\end{itemize}"""
    doc1_4 = render_doc("TI-SIGE-ENT-F1-004", "GESTIÓN DEL ALCANCE / ALINEACIÓN INSTITUCIONAL", "21/08/2026", "21/08/2026", "DEFINICIÓN DEL ALCANCE, RESTRICCIONES Y OBJETIVOS SGC", b1_4, "21/08/2026", anx1_4)
    with open(os.path.join(base_dir, "1.4_Definicion_Alcance_Restricciones_y_Objetivos_SGC.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_4)

    # 1.5
    b1_5 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Reglas de Negocio y Validation Gates Lógicas -- Código EDT: 1.5

\section{Introducción}
Las fallas en los procesos de acreditación y auditoría de la calidad documental en las instituciones de educación superior obedecen, en su gran mayoría, a la falta de mecanismos automáticos de control preventivo. En los formatos manuales, el documento fluye hacia instancias de revisión aun conteniendo inconsistencias aritméticas, evidencias faltantes o períodos extemporáneos. El sistema SIGE introduce formalmente el concepto de \textbf{Validation Gates} (Compuertas Lógicas de Control), las cuales actúan como filtros estrictos e inquebrantables que impiden la transición de estados documentales a menos que se satisfagan todas las condiciones lógicas y matemáticas del SGC.

\section{Objetivo}
\subsection{Objetivo General}
Formalizar matemática y conceptualmente las reglas de negocio y las compuertas de validación lógica (Validation Gates) que gobernarán el ciclo de vida documental en el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Formular las ecuaciones matemáticas para la validación de ponderaciones y cálculo del avance global.
    \item Especificar las compuertas de bloqueo preventivo por evidencias no adjuntas y fechas extemporáneas.
    \item Modelar la máquina de estados y las precondiciones para la cascada secuencial de firmas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Especificación de 15 Reglas de Negocio Institucionales (RN-01 a RN-15).
    \item Definición lógica de las 4 Validation Gates fundamentales del sistema.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementación a nivel de código de frameworks (cubierta en la Fase 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Validation Gate:} Punto de control algorítmico que bloquea la persistencia o cambio de estado si no se cumplen las precondiciones.
    \item \textbf{Ponderación Horaria ($P_i$):} Porcentaje de dedicación horaria asignado a una actividad específica respecto al total planificado.
    \item \textbf{Avance Consolidado ($A_G$):} Promedio ponderado acumulado de cumplimiento de todas las actividades académicas.
    \item \textbf{Cascada de Firmas:} Circuito secuencial e irreversible donde la firma del nivel $k$ requiere la firma previa y validada del nivel $k-1$.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Nixon Hurtado (Responsables EDT 1.5):} Formulación matemática de las compuertas y matriz de reglas de negocio.
    \item \textbf{Heidi Villavicencio (Analista):} Validación de correspondencia con la normativa SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la lógica formal de compuertas.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Norma ISO 9001:2015 (Cláusula 8.5.1):} Control de la producción y de la provisión del servicio con criterios de aceptación explícitos.
    \item \textbf{Reglamento Interno de Evaluación y Régimen Académico FISEI.}
\end{itemize}

\section{Método, Políticas y Contenidos}
Las reglas se definieron mediante tablas de decisión y formalismo matemático. En la Figura \ref{fig:s1_05_gates} se presenta el diagrama de decisión de las Validation Gates.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/s1_05_validation_gates.png}
    \caption{Arquitectura Lógica de las Validation Gates en el Flujo Documental SIGE.}
    \label{fig:s1_05_gates}
\end{figure}

\section{Descripción de actividades}
\subsection{Formalización Matemática de las Reglas de Validación}
\subsubsection{Gate 1: Validación de Ponderaciones Horarias (Suma 100\%)}
Sea $N$ el número total de actividades registradas en la Matriz de Cumplimiento, y $P_i$ el porcentaje ponderado asignado a la actividad $i$:
\begin{equation}
    \sum_{i=1}^{N} P_i = 100.00\% \quad \text{donde} \quad 0 < P_i \le 100, \quad \forall i \in \{1, \dots, N\}
\end{equation}
\textbf{Regla de Bloqueo:} Si $|(\sum_{i=1}^{N} P_i) - 100| > 0.01$, el sistema rechaza la solicitud de transición con error semántico \texttt{ERR\_SUM\_INVALID}.

\subsubsection{Gate 2: Cálculo del Avance Global y Compuerta de Evidencia Obligatoria}
Sea $A_i \in [0, 100]$ el porcentaje de avance reportado para la actividad $i$. El avance global consolidado $A_G$ se calcula como:
\begin{equation}
    A_G = \sum_{i=1}^{N} \left( \frac{P_i}{100} \times A_i \right)
\end{equation}
\textbf{Compuerta de Evidencia:} Para toda actividad donde $A_i > 0\%$, es condición sine qua non la existencia de al menos un registro de evidencia en MinIO con hash SHA-256 verificado, o un texto formal de justificación debidamente aprobado:
\begin{equation}
    \forall i, \; A_i > 0 \implies \left( \text{Count}(\text{Evidencias}_i) \ge 1 \; \lor \; \text{Length}(\text{Justificacion}_i) \ge 50 \right)
\end{equation}

\subsection{Matriz de Reglas de Negocio del Sistema (RN-01 a RN-15)}
\begin{table}[htbp]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entidad / Contexto} & \textbf{Condición Lógica y Comportamiento del Sistema} & \textbf{Efecto en UI / API} \\
\hline
\textbf{RN-01} & Documento & Un docente solo puede tener un Plan en estado 'Borrador' por período lectivo. & Bloqueo de creación \\
\hline
\textbf{RN-02} & Período & Las fechas de las actividades deben estar contenidas dentro del período académico. & Error de validación \\
\hline
\textbf{RN-03} & Ponderación & La sumatoria de ponderaciones de la matriz debe totalizar exactamente 100.00\%. & Botón Envío Inactivo \\
\hline
\textbf{RN-04} & Evidencias & Actividades con avance $>0\%$ sin evidencia cargada impiden el envío del informe. & Error HTTP 422 \\
\hline
\textbf{RN-05} & Archivos & Los archivos de evidencia deben ser formato PDF y tamaño no superior a 25 MB. & Rechazo de subida \\
\hline
\textbf{RN-06} & Inmutabilidad & Una vez firmado por el Elaborador, las secciones y matriz entran en modo solo lectura. & Campos Disabled \\
\hline
\textbf{RN-07} & Observaciones & Un Coordinador no puede aprobar un informe si existen observaciones no resueltas. & Bloqueo de aprobación \\
\hline
\textbf{RN-08} & Cascada Firmas & La firma del Revisor requiere obligatoriamente la firma previa válida del Elaborador. & Secuencia forzada \\
\hline
\textbf{RN-09} & Cascada Firmas & La firma del Aprobador requiere obligatoriamente la firma previa válida del Revisor. & Secuencia forzada \\
\hline
\textbf{RN-10} & Extemporáneo & El envío fuera de la fecha límite requiere solicitud formal y código de desbloqueo. & Bloqueo temporal \\
\hline
\textbf{RN-11} & Auditoría & Todo cambio de estado genera un registro en la tabla de bitácora con IP y estampa de tiempo. & Transacción atómica \\
\hline
\textbf{RN-12} & Autoguardado & El autoguardado de TipTap solo se dispara tras 1500 ms de inactividad de teclado. & Debounce Timer \\
\hline
\textbf{RN-13} & Secciones & No se permite enviar documentos con secciones descriptivas vacías o con texto genérico. & Validación regex \\
\hline
\textbf{RN-14} & Hashes SHA-256 & Si el hash recalculado del archivo en MinIO no coincide con la base, se genera alerta. & Alerta de Integridad \\
\hline
\textbf{RN-15} & Exportación & Los PDFs generados deben incluir obligatoriamente el código QR institucional. & Estampado visual \\
\hline
\end{tabularx}
\caption{Catálogo de Reglas de Negocio y Validation Gates.}
\label{tab:rn_gates}
\end{table}
"""
    anx1_5 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Tabla de Códigos de Error Semánticos de Validation Gates.
\end{itemize}"""
    doc1_5 = render_doc("TI-SIGE-ENT-F1-005", "REGLAS DE NEGOCIO / VALIDATION GATES LÓGICAS", "24/08/2026", "24/08/2026", "REGLAS DE NEGOCIO Y VALIDATION GATES LÓGICAS", b1_5, "24/08/2026", anx1_5)
    with open(os.path.join(base_dir, "1.5_Reglas_de_Negocio_y_Validation_Gates_Logicas.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_5)

    # 1.6
    b1_6 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Elaboración de Caso de Negocio, Retorno de Inversión (ROI) y Project Charter Oficial -- Código EDT: 1.6

\section{Introducción}
Todo proyecto de ingeniería de software en el ámbito institucional debe sustentarse en un análisis riguroso de viabilidad económica, técnica y operacional. Aunque la Universidad Técnica de Ambato es una institución pública sin fines de lucro, la optimización de los recursos públicos exige cuantificar el ahorro de horas-hombre docentes y la reducción de costos operativos. Este documento consolida el Caso de Negocio, los indicadores financieros (VAN, TIR, ROI, Payback) y formaliza el Acta de Constitución del Proyecto (Project Charter) con el respaldo de las autoridades académicas.

\section{Objetivo}
\subsection{Objetivo General}
Evaluar cuantitativamente la rentabilidad económica y social del proyecto SIGE mediante indicadores de retorno de inversión (ROI), formulando el Project Charter oficial que autoriza formalmente su ejecución.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Calcular el presupuesto detallado de inversión directa en hardware, hosting y licenciamiento open source (\$630.30).
    \item Cuantificar el ahorro anual generado por la automatización de horas docentes (\$23,700).
    \item Calcular los indicadores financieros: VAN (\$84,212 a tasa social 12\%), ROI (+3,660\%) y Payback (1.8 meses).
    \item Redactar el Acta de Constitución del Proyecto (Project Charter) con asignación de recursos y firmas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Análisis de costos operativos de los 65 docentes de la facultad y personal de coordinación.
    \item Project Charter formal con designación del equipo y patrocinadores.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Gastos de infraestructura institucional preexistente (computadores personales docentes).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Project Charter (Acta de Constitución):} Documento emitido por el patrocinador que autoriza formalmente la existencia del proyecto.
    \item \textbf{ROI (Return on Investment):} Métrica que evalúa la eficiencia de una inversión: $\text{ROI} = ((\text{Beneficios} - \text{Costos}) / \text{Costos}) \times 100$.
    \item \textbf{VAN (Valor Actual Neto):} Suma de los flujos de caja futuros actualizados menos la inversión inicial.
    \item \textbf{Payback (Período de Recuperación):} Tiempo requerido para que los beneficios acumulados igualen el costo inicial.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Equipo Completo SIGE (Responsables EDT 1.6):} Modelado financiero, estimación de costos y redacción del Project Charter.
    \item \textbf{Steeven Toala (Líder del Proyecto):} Dirección general de estimaciones.
    \item \textbf{Ing. Paulo Torres (Docente Patrocinador):} Validación de viabilidad y suscripción del Project Charter.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición):} Gestión de los Costos y Acta de Constitución del Proyecto.
    \item \textbf{Lineamientos de Eficiencia en el Gasto Público - SENESCYT Ecuador.}
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó un horizonte de evaluación de 4 años a una tasa de descuento social del 12\%. En la Figura \ref{fig:s1_06_roi} se ilustra la distribución porcentual de los beneficios institucionales generados por el proyecto.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth,height=5.2cm,keepaspectratio]{images/s1_06_beneficios_pie.png}
    \caption{Distribución de Beneficios y Ahorro Institucional Generado por SIGE.}
    \label{fig:s1_06_roi}
\end{figure}

\section{Descripción de actividades}
\subsection{Estructura de Costos de Inversión Inicial (CAPEX y OPEX Inicial)}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{4.5cm}|X|r|}
\hline
\rowcolor{tableheader}
\textbf{Ítem} & \textbf{Concepto} & \textbf{Especificación / Proveedor} & \textbf{Costo (USD)} \\
\hline
1 & VPS Hostinger KVM 4 (1 Año) & 4 vCPU, 16 GB RAM, 200 GB NVMe, IP dedicada & \$191.88 \\
\hline
2 & Dominio institucional (.org/.edu) & Registro anual y DNS administrado Cloudflare & \$15.00 \\
\hline
3 & Certificado SSL y Seguridad & Let's Encrypt Wildcard SSL + Cloudflare Free & \$0.00 \\
\hline
4 & Storage MinIO S3 y Docker & Suite Open Source desplegada en VPS local & \$0.00 \\
\hline
5 & Motor LanguageTool Local & Despliegue en contenedor Docker sin costo de API & \$0.00 \\
\hline
6 & Consumo Google Gemini API & Capa de soporte inteligente y fallback & \$60.00 \\
\hline
7 & Respaldo Offsite y Contingencia & Almacenamiento externo cifrado S3 (100 GB) & \$36.00 \\
\hline
8 & Gastos Administrativos Menores & Documentación física, impresiones y actas & \$45.00 \\
\hline
9 & Fondo de Reserva de Imprevistos & Contingencia de gestión de riesgos ($10\%$) & \$282.42 \\
\hline
\multicolumn{3}{|r|}{\textbf{PRESUPUESTO TOTAL ASIGNADO:}} & \textbf{\$630.30} \\
\hline
\end{tabularx}
\caption{Presupuesto Total Consolidado del Proyecto SIGE.}
\label{tab:presupuesto}
\end{table}

\subsection{Cuantificación del Ahorro Anual y Retorno de Inversión}
Considerando una planta de 65 docentes que elaboran 2 informes semestrales al año (130 informes anuales), con un costo por hora docente estimado de \$15.00:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Horas Invertidas en Proceso Manual:} $130 \times 8 \text{ h} = 1,040 \text{ h/año}$ (Costo: \$15,600).
    \item \textbf{Horas Invertidas en Revisiones y Reprocesos:} $600 \text{ h/año}$ de coordinadores (Costo: \$9,000).
    \item \textbf{Horas Requeridas con SIGE:} $130 \times 1.5 \text{ h} = 195 \text{ h/año}$ (Costo: \$2,925).
    \item \textbf{Ahorro Neto Anual Estimado:} \textbf{\$21,675.00 a \$23,700.00 anuales}.
\end{itemize}

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.5cm}|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Indicador Financiero} & \textbf{Valor Calculado} & \textbf{Interpretación Técnica y Viabilidad} \\
\hline
Retorno de Inversión (ROI) & \textbf{+3,660\%} & Rendimiento extremadamente alto por automatización de procesos. \\
\hline
Valor Actual Neto (VAN a 12\%) & \textbf{\$84,212.00} & Proyecto altamente viable y creador de valor institucional. \\
\hline
Tasa Interna de Retorno (TIR) & \textbf{$>300\%$} & Supera con creces la tasa de oportunidad institucional. \\
\hline
Período de Recuperación (Payback) & \textbf{1.8 meses} & La inversión inicial se amortiza en el primer semestre de uso. \\
\hline
\end{tabularx}
\caption{Indicadores Financieros de Evaluación del Proyecto SIGE.}
\label{tab:roi}
\end{table}

\subsection{Project Charter Oficial (Acta de Constitución)}
Se designa a Steeven Toala como Líder y Arquitecto, Heidi Villavicencio como Analista de Calidad, Nixon Hurtado como Desarrollador Backend y Andrea Vásquez como Desarrolladora Frontend, bajo el patrocinio y dirección académica del Ing. Paulo Torres.
"""
    anx1_6 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Acta de Constitución del Proyecto (Project Charter Firmada).
\item \textbf{Anexo 2:} Flujo de Caja Descontado Proyectado a 4 Años.
\end{itemize}"""
    doc1_6 = render_doc("TI-SIGE-ENT-F1-006", "EVALUACIÓN FINANCIERA / PROJECT CHARTER", "24/08/2026", "24/08/2026", "ELABORACIÓN DE CASO DE NEGOCIO, ROI Y PROJECT CHARTER", b1_6, "24/08/2026", anx1_6)
    with open(os.path.join(base_dir, "1.6_Elaboracion_Caso_de_Negocio_ROI_Project_Charter.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_6)

    # 1.7
    b1_7 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Planificación del Proyecto, Cronograma de Trabajo y EDT -- Código EDT: 1.7

\section{Introducción}
El aseguramiento del plazo de entrega en proyectos de software requiere una disciplina estricta de descomposición jerárquica del trabajo y secuenciación lógica de actividades. Tomando como base los lineamientos del Project Management Institute (PMI) y la metodología ágil Scrum, este informe formaliza la Estructura de Desglose del Trabajo (EDT / WBS) compuesta por 49 tareas estructuradas en 5 fases, y el Cronograma Maestro oficial configurado en Microsoft Project bajo el calendario laboral de la ciudad de Ambato, totalizando 57 días laborables y 456 horas netas de ingeniería.

\section{Objetivo}
\subsection{Objetivo General}
Estructurar la planificación temporal y metodológica integral del proyecto SIGE mediante una Estructura de Desglose del Trabajo (EDT) de 49 tareas y el Cronograma Maestro en Microsoft Project, estableciendo la línea base del proyecto.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Descomponer el proyecto en 49 tareas organizadas en 5 fases secuenciales e iterativas.
    \item Configurar el calendario laboral oficial de Ambato/Ecuador (lunes a viernes, 8 horas/día, excluyendo feriados nacionales).
    \item Determinar el camino crítico (Critical Path), las holguras y la asignación del 100\% de recursos del equipo.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Planificación desde el 12 de agosto de 2026 hasta el 30 de octubre de 2026.
    \item 5 fases: Análisis, Arquitectura, Desarrollo Core, Pruebas/QA y Cierre/Despliegue.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mantenimientos evolutivos posteriores a la fecha de entrega-recepción del 30 de octubre de 2026.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{EDT (Estructura de Desglose del Trabajo):} Descomposición jerárquica orientada a entregables del trabajo que ejecutará el equipo del proyecto.
    \item \textbf{Línea Base del Cronograma:} Versión aprobada del modelo de programación que solo puede modificarse mediante procedimientos formales de control de cambios.
    \item \textbf{Ruta Crítica (CPM):} Secuencia de actividades que determina la duración total mínima del proyecto; no tiene holgura.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 1.7):} Elaboración del cronograma en Microsoft Project, cálculo de holguras y gestión del tiempo.
    \item \textbf{Equipo SIGE (HV, NH, AV):} Estimación de esfuerzo por paquete de trabajo y compromiso de entregas.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la línea base del cronograma.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Practice Standard for Work Breakdown Structures (PMI).}
    \item \textbf{Ley Orgánica del Servicio Público (LOSEP) y Código de Trabajo de Ecuador:} Calendario de feriados nacionales obligatorios.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó Microsoft Project con calendario laboral de 40 horas semanales. En las Figuras \ref{fig:s1_07_gantt} y \ref{fig:s1_07_cronograma} se aprecian el diagrama general por fases y el cronograma detallado.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/gantt_fases_sige.png}
    \caption{Diagrama Gantt de las 5 Fases del Proyecto SIGE.}
    \label{fig:s1_07_gantt}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/cronograma_detallado_sige.png}
    \caption{Cronograma Maestro Detallado y Ruta Crítica del Proyecto SIGE.}
    \label{fig:s1_07_cronograma}
\end{figure}

\section{Descripción de actividades}
\subsection{Resumen de Fases y Distribución de Esfuerzo}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{4.2cm}|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación de Fase} & \textbf{Fechas} & \textbf{Días} & \textbf{Horas} & \textbf{\% Esfuerzo} \\
\hline
\textbf{Fase 1} & Análisis y Planificación & 12 ago - 24 ago & 9 & 72 h & $15.8\%$ \\
\hline
\textbf{Fase 2} & Diseño y Arquitectura & 25 ago - 04 sep & 9 & 72 h & $15.8\%$ \\
\hline
\textbf{Fase 3} & Desarrollo Core & 07 sep - 08 oct & 24 & 192 h & $42.1\%$ \\
\hline
\textbf{Fase 4} & Pruebas y Control de Calidad & 12 oct - 23 oct & 10 & 80 h & $17.5\%$ \\
\hline
\textbf{Fase 5} & Despliegue y Cierre & 26 oct - 30 oct & 5 & 40 h & $8.8\%$ \\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL GENERAL:}} & \textbf{12 ago - 30 oct} & \textbf{57} & \textbf{456 h} & \textbf{100.0\%} \\
\hline
\end{tabularx}
\caption{Distribución de Esfuerzo y Tiempos por Fase del Proyecto.}
\label{tab:fases}
\end{table}

\subsection{Hitos Clave del Proyecto (Milestones)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito 1 (24 ago):} Aprobación de Fase 1 y Paquete Entregables Semana 1.
    \item \textbf{Hito 2 (04 sep):} Aprobación de Arquitectura y Entregable General Semana 2.
    \item \textbf{Hito 3 (22 sep):} Sprint 2 Review: Wizard y Persistencia Operativa.
    \item \textbf{Hito 4 (30 sep):} Sprint 3 Review: Matriz Dinámica y Evidencias MinIO.
    \item \textbf{Hito 5 (08 oct):} Sistema Core Completado (Code Freeze previo a feriado de 9 de octubre).
    \item \textbf{Hito 6 (23 oct):} Aceptación de QA y Release Candidate v1.0-RC.
    \item \textbf{Hito 7 (30 oct):} Cierre Formal del Proyecto y Sistema en Producción.
\end{itemize}
"""
    anx1_7 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Archivo Oficial \texttt{Cronograma\_SIGE\_Oficial.mpp} (Microsoft Project).
\end{itemize}"""
    doc1_7 = render_doc("TI-SIGE-ENT-F1-007", "GESTIÓN DEL TIEMPO / CRONOGRAMA MAESTRO EDT", "24/08/2026", "24/08/2026", "PLANIFICACIÓN DEL PROYECTO Y CRONOGRAMA DE TRABAJO", b1_7, "24/08/2026", anx1_7)
    with open(os.path.join(base_dir, "1.7_Planificacion_del_Proyecto_y_Cronograma_de_Trabajo.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_7)

    # 1.8
    b1_8 = r"""
\section{Título}
\textbf{Denominación del Entregable:} HITO 1: Aprobación de Fase 1 y Entregable General Semana 1 -- Código EDT: 1.8

\section{Introducción}
El cierre formal de la Fase 1: Análisis y Planificación del proyecto SIGE representa la culminación exitosa de las actividades de diagnóstico, ingeniería de requerimientos, modelado de compuertas lógicas y formulación presupuestaria. El presente informe formaliza la revisión colegiada y aprobación del Hito 1 ante el docente asesor y evaluador Ing. Paulo Torres. Se consolida la trazabilidad de los 7 entregables predecesores (1.1 a 1.7) y se incorporan las herramientas analíticas de control de calidad institucional: Diagrama de Causa-Efecto de Ishikawa, Gráfica de Comportamiento (Run Chart) y Gráfica de Trabajo Completado (Burnup Chart), demostrando el cumplimiento estricto del 100\% de los objetivos de la primera semana de gestión.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, evaluar y aprobar formalmente el paquete de entregables de la Fase 1: Análisis y Planificación (Hito 1), certificando la conformidad técnica y metodológica para el paso a la Fase 2 de Arquitectura y Diseño.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Verificar el cumplimiento y calidad técnica de los entregables EDT 1.1 al 1.7.
    \item Documentar el análisis de causa-efecto mediante el Diagrama de Ishikawa de cuellos de botella SGC.
    \item Evaluar el comportamiento estadístico de errores con el Run Chart y el ritmo de trabajo con el Burnup Chart.
    \item Suscribir el acta formal de aprobación de Hito 1 por parte del docente evaluador.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Consolidado de los 8 entregables de Fase 1 ejecutados entre el 12 y el 24 de agosto de 2026.
    \item Certificación de requisitos SRS IEEE 830 y línea base del cronograma.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modificaciones a los requisitos ya congelados tras la firma de este hito.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito de Control (Milestone):} Evento significativo en el proyecto con duración de 0 días que marca la finalización de una fase o entrega crítica.
    \item \textbf{Diagrama de Ishikawa (Causa-Efecto):} Herramienta visual para identificar y clasificar las causas raíz de un problema específico.
    \item \textbf{Run Chart (Gráfica de Comportamiento):} Gráfico temporal para monitorear tendencias, medias y variabilidad de un proceso.
    \item \textbf{Burnup Chart:} Gráfico que muestra el trabajo completado frente al alcance total a lo largo del tiempo.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Equipo de Proyecto SIGE (Responsables EDT 1.8):} Consolidación del informe, sustentación técnica y demostración de artefactos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador / Patrocinador):} Revisión exhaustiva de conformidad, retroalimentación y suscripción formal de aprobación.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición):} Gestión de la Calidad del Proyecto y Cierre de Fase.
    \item \textbf{Norma ISO 9001:2015 (Cláusula 9.1):} Seguimiento, medición, análisis y evaluación.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se realizó una sesión formal de revisión de calidad y sustentación técnica el 24 de agosto de 2026. En la Figura \ref{fig:s1_08_cons} se presenta el mapa consolidado de entregables de Fase 1.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/s1_07_consolidado_s1.png}
    \caption{Mapa Consolidado de la Fase 1: Análisis y Planificación.}
    \label{fig:s1_08_cons}
\end{figure}

\section{Descripción de actividades}
\subsection{Matriz de Verificación y Conformidad de Entregables de Fase 1}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{4.0cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{EDT} & \textbf{Entregable Oficial} & \textbf{Artefacto Verificado} & \textbf{Horas} & \textbf{Estado} \\
\hline
1.1 & Diagnóstico As-Is & Mapeo As-Is y matriz de problemas P-01 a P-06 & 24 h & Aprobado \\
\hline
1.2 & Actores y Procesos & Matriz de Stakeholders y análisis de cuadrantes & 32 h & Aprobado \\
\hline
1.3 & Especificación SRS & 24 RFs y 10 RNFs bajo IEEE 830 e ISO 25010 & 40 h & Aprobado \\
\hline
1.4 & Alcance y Restricciones & Fronteras del sistema y objetivos SMART & 32 h & Aprobado \\
\hline
1.5 & Reglas y Validation Gates & Especificación formal de compuertas lógicas & 32 h & Aprobado \\
\hline
1.6 & Caso de Negocio y ROI & Presupuesto (\$630.30), ROI (+3,660\%) y Charter & 24 h & Aprobado \\
\hline
1.7 & Cronograma Maestro & EDT 49 tareas, MS Project (57 días, 456h) & 24 h & Aprobado \\
\hline
1.8 & Hito 1: Aprobación Fase 1 & Paquete Completo Aprobado y Análisis Calidad & 0 h & Aprobado \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL HORAS INVERTIDAS EN FASE 1:}} & \textbf{208 h} & \textbf{100\%} \\
\hline
\end{tabularx}
\caption{Matriz de Conformidad y Cierre de Entregables de Fase 1.}
\label{tab:cierre_fase1}
\end{table}

\subsection{Herramientas Analíticas de Calidad SGC}
Como parte de la rigurosidad analítica exigida para la aprobación de la Fase 1, se ejecutaron tres análisis formales de aseguramiento de la calidad:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Diagrama de Ishikawa (Análisis Causa-Efecto):} Se identificaron las causas raíz de la ineficiencia en la gestión documental SGC en 6 dimensiones: Métodos, Personas, Tecnología, Entorno, Medición y Materiales (ver Figura \ref{fig:ishikawa}).
    \item \textbf{Gráfica de Comportamiento (Run Chart):} Monitoreo de la tasa de reprocesos por informe a lo largo de 10 ciclos académicos, evidenciando una media histórica inaceptable de 3.8 rondas de corrección por documento (ver Figura \ref{fig:runchart}).
    \item \textbf{Gráfica de Trabajo Completado (Burnup Chart):} Registro del avance de horas y entregables planificados vs reales en la Fase 1, demostrando convergencia total al día 24 de agosto de 2026 (ver Figura \ref{fig:burnup}).
\end{enumerate}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/pdf_page_ishikawa.png}
    \caption{Diagrama de Causa y Efecto (Ishikawa) de Ineficiencias en el Proceso Actual SGC.}
    \label{fig:ishikawa}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/pdf_page_runchart.png}
    \caption{Gráfica de Comportamiento (Run Chart) de Ciclos de Reproceso Históricos.}
    \label{fig:runchart}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/pdf_page_burnup.png}
    \caption{Gráfica de Trabajo Completado (Burnup Chart) de la Fase 1.}
    \label{fig:burnup}
\end{figure}

\subsection{Acta de Declaración de Conformidad}
El docente evaluador Ing. Paulo Torres, tras revisar el pliego de requerimientos y la línea base del proyecto, certifica la aprobación formal del Hito 1, autorizando el inicio inmediato de la Fase 2: Diseño y Arquitectura a partir del 25 de agosto de 2026.
"""
    anx1_8 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Acta de Aprobación de Hito 1 (Semana 1).
\item \textbf{Anexo 2:} Informe de Conformidad Metodológica SGC.
\end{itemize}"""
    doc1_8 = render_doc("TI-SIGE-ENT-F1-008", "HITO DE CONTROL / APROBACIÓN DE FASE 1", "24/08/2026", "24/08/2026", "HITO 1: APROBACIÓN DE FASE 1 Y ENTREGABLE GENERAL", b1_8, "24/08/2026", anx1_8)
    with open(os.path.join(base_dir, "1.8_HITO_1_Aprobacion_Fase_1_Entregable_General.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_8)

    print("Fase 1 generated successfully via template_engine!")

if __name__ == "__main__":
    generate_fase1()
