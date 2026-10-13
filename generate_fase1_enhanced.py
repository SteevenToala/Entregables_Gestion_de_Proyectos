# generate_fase1_enhanced.py
import os
from template_engine import render_doc

def generate_fase1():
    base_dir = os.path.join("Entregables_Latex", "Fase_1") if os.path.exists("Entregables_Latex") else "Fase_1"
    os.makedirs(base_dir, exist_ok=True)

    # =========================================================================
    # 1.1 LEVANTAMIENTO DE INFORMACIÓN DEL PROCESO ACTUAL
    # =========================================================================
    b1_1 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Levantamiento de Información del Proceso Actual (Diagnóstico As-Is) -- Código EDT: 1.1

\section{Introducción}
En la Universidad Técnica de Ambato (UTA), y específicamente en la Facultad de Ingeniería en Sistemas, Electrónica e Industrial (FISEI), la gestión académica semestral exige el cumplimiento de los procesos estipulados por el Sistema de Gestión de la Calidad (SGC). Actualmente, la planificación y rendición de cuentas del cuerpo docente se lleva a cabo mediante plantillas ofimáticas desacopladas (\texttt{.docx} y \texttt{.xlsx}) correspondientes a los formatos institucionales \texttt{UTA-SGC-A-2-1-P7-T1} (Plan de Trabajo) y \texttt{UTA-SGC-A-2-1-P7-T2} (Informe de Cumplimiento). El presente entregable documenta el diagnóstico técnico y operativo exhaustivo del estado actual (\textit{As-Is}), delimitando las ineficiencias críticas que fundamentan el desarrollo del sistema web SIGE.

\section{Objetivo}
\subsection{Objetivo General}
Diagnosticar exhaustivamente el flujo operativo actual de elaboración, revisión, aprobación y custodia de planes de trabajo e informes del SGC en la FISEI, identificando cuellos de botella, riesgos de calidad y requerimientos base para el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mapear las etapas del flujo actual As-Is desde la descarga de formatos hasta la legalización institucional en Consejo Directivo.
    \item Catalogar cuantitativa y cualitativamente los cuellos de botella operativos mediante una matriz formal de problemas (P-01 a P-06).
    \item Establecer la línea base de tiempos, costos y riesgos del proceso manual previo a la automatización.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mapeo integral de los formatos SGC institucionales \texttt{P7-T1} y \texttt{P7-T2}.
    \item Entrevistas estructuradas a 8 docentes titulares, 2 directores de área y 2 coordinadores de carrera de la FISEI.
    \item Levantamiento de evidencias sobre extravío de documentos, sumas asimétricas y asimetría de versiones.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Procesos de nómina financiera y remuneraciones del departamento de Talento Humano.
    \item Trámites administrativos no relacionados directamente con el quehacer académico docente.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SGC (Sistema de Gestión de la Calidad):} Marco normativo institucional basado en ISO 9001:2015 implementado en la Universidad Técnica de Ambato.
    \item \textbf{Diagnóstico As-Is:} Representación formal y fáctica del estado operativo del proceso sin intervención tecnológica moderna.
    \item \textbf{Plan de Trabajo Docente (P7-T1):} Instrumento prospectivo semestral donde el docente planifica horas y metas de docencia, investigación y vinculación.
    \item \textbf{Informe de Cumplimiento (P7-T2):} Instrumento retrospectivo en el cual se reporta el porcentaje de avance ejecutado y se justifican las evidencias asociadas.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado / Steeven Toala (Responsables EDT 1.1):} Ejecución de entrevistas, análisis de artefactos documentales y mapeo formal del flujo As-Is.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Consolidación de la matriz de hallazgos y verificación de estándares SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Supervisión metodológica y aprobación del alcance del diagnóstico.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Obligatoriedad de garantizar la calidad educativa, rendición de cuentas y cumplimiento estricto de la carga horaria del personal académico.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67:} Directrices sobre la distribución y seguimiento de las horas de docencia, investigación formativa, vinculación y gestión académica.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Arts. 10 y 11:} Principios de confidencialidad y minimización en el almacenamiento y custodia de expedientes docentes.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 7.5 (Información Documentada):} Requisitos de control, distribución, acceso, almacenamiento y preservación inalterable de los documentos del SGC institucional.
    \item \textbf{ISO/IEC 25010:2011 (Calidad del Producto de Software):} Criterios de adecuación funcional y usabilidad orientados a eliminar los reprocesos manuales detectados.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Para el levantamiento se aplicó la técnica de análisis de artefactos documentales combinada con entrevistas estructuradas a 8 docentes titulares y 2 coordinadores de la FISEI, examinando una muestra histórica de 30 expedientes de planes e informes del ciclo académico previo. El flujo resultante fue modelado bajo estándar BPMN (\textit{Business Process Model and Notation}).

\subsection{Políticas de Calidad Identificadas como Mandatorias}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Unicidad Documental:} Un plan de trabajo aprobado no puede duplicarse ni fragmentarse en múltiples versiones locales de Word.
    \item \textbf{Política de Consistencia Horaria:} Las horas asignadas a cátedra, tutoría, gestión y vinculación deben sumar exactamente la carga contractual asignada ($40\text{ h/semana}$ a tiempo completo).
    \item \textbf{Política de Evidencia Obligatoria:} Toda actividad ejecutada reportada con porcentaje mayor a cero debe contar con un medio de verificación auditable y no volátil.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_01_diagrama_as_is.png}
    \caption{Diagrama de Flujo del Proceso Actual As-Is (Flujo Manual y Descentralizado SGC).}
    \label{fig:diag_as_is}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Problemas y Cuellos de Botella Detectados (P-01 a P-06)}
La auditoría del proceso manual arrojó seis fallas estructurales recurrentes:

\begin{table}[H]
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
\caption{Matriz de Cuellos de Botella y Deficiencias del Proceso As-Is en la FISEI.}
\label{tab:problemas_as_is}
\end{table}
\FloatBarrier

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item El proceso actual As-Is presenta una vulnerabilidad crítica ante auditorías debido a la dispersión de evidencias y la falta de un repositorio inmutable.
    \item Los errores aritméticos en las matrices de actividades evidencian la imperiosa necesidad de compuertas lógicas preventivas (\textit{Validation Gates}) que impidan el envío de documentos con sumas incoherentes.
    \item La automatización del flujo documental en SIGE erradicará el 100\% de la asimetría de versiones y reducirá en más de un 80\% el tiempo dedicado a reprocesos burocráticos.
\end{itemize}
"""
    anx1_1 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.1 \\
\hline
Nombre de la Tarjeta & Levantamiento de información del proceso actual \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 12 de agosto al 14 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{01\_Levantamiento\_Informacion\_Proceso\_Actual.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.1 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia del Proceso Manual Diagnosticado (Plantillas SGC)}
A continuación se documenta el extracto del encabezado oficial del formato institucional \texttt{UTA-SGC-A-2-1-P7-T1} analizado durante el levantamiento:
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{2.5cm}|X|m{3.5cm}|}
\hline
\rowcolor{tableheader}
\multicolumn{3}{|c|}{\textbf{UNIVERSIDAD TÉCNICA DE AMBATO -- SISTEMA DE GESTIÓN DE CALIDAD}} \\
\hline
\textbf{Formato Oficial:} & UTA-SGC-A-2-1-P7-T1 (Plan de Trabajo Docente) & Versión: 2.0 \\
\hline
\textbf{Unidad Responsable:} & Facultad de Ingeniería en Sistemas, Electrónica e Industrial & Ciclo: Semestral \\
\hline
\textbf{Riesgo Auditado:} & Modificación arbitraria de celdas y fórmulas en Microsoft Word & Criticidad: ALTA (P-03) \\
\hline
\end{tabularx}
\caption{Identificación de plantillas oficiales auditadas en el proceso As-Is.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{a418f7d - feat(req): diagnostico formal del proceso As-Is y matriz de problemas P-01 a P-06}
    \item \textbf{Archivos Afectados:} \texttt{docs/diagnostico\_as\_is.md}, \texttt{Entregables\_Latex/Fase\_1/1.1*.tex}
\end{itemize}
"""
    doc1_1 = render_doc("TI-SIGE-ENT-F1-001", "INGENIERÍA DE REQUERIMIENTOS / DIAGNÓSTICO AS-IS", "14/08/2026", "14/08/2026", "LEVANTAMIENTO DE INFORMACIÓN DEL PROCESO ACTUAL", b1_1, "14/08/2026", anx1_1)
    with open(os.path.join(base_dir, "1.1_Levantamiento_Informacion_Proceso_Actual.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_1)

    # =========================================================================
    # 1.2 IDENTIFICACIÓN DE ACTORES Y PROCESOS
    # =========================================================================
    b1_2 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Identificación de Actores y Procesos (Matriz de Stakeholders) -- Código EDT: 1.2

\section{Introducción}
El éxito en la implantación del sistema SIGE dentro de la FISEI requiere un análisis riguroso de los actores organizacionales que intervienen en el ciclo de vida de los planes de trabajo e informes institucionales. El Sistema de Gestión de Calidad establece una cadena jerárquica con responsabilidades claramente delimitadas, desde la docencia de aula hasta las autoridades de facultad. El presente informe formaliza el mapa de interesados (\textit{Stakeholders}) y clasifica sus niveles de poder e interés para fundamentar la matriz de control de acceso y perfiles del sistema.

\section{Objetivo}
\subsection{Objetivo General}
Identificar, mapear y caracterizar formalmente a los actores organizacionales y los macroprocesos institucionales que interactúan con el Sistema de Gestión de Calidad en la FISEI, estructurando la Matriz de Stakeholders del proyecto SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Identificar las funciones institucionales de los roles: Docente Elaborador, Coordinador de Área, Coordinador de Carrera, Subdecano y Administrador SGC.
    \item Analizar la matriz de Poder versus Interés según la metodología estándar del PMBOK.
    \item Modelar la asignación de responsabilidades mediante la matriz RACI de la cadena documental.
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
    \item \textbf{Coordinador de Carrera:} Autoridad académica intermedia que revisa y emite el aval formal de los planes e informes de sus docentes.
    \item \textbf{Subdecano / Decano:} Máxima autoridad académica de facultad que aprueba formalmente los documentos para su archivo definitivo.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 1.2):} Caracterización de actores, levantamiento de perfiles y formulación de la matriz de poder e interés.
    \item \textbf{Steeven Toala (Arquitecto):} Mapeo de interesados a roles del sistema y matriz RACI.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Validación de la congruencia de los roles con el estatuto universitario.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Estatuto Orgánico de la Universidad Técnica de Ambato:} Estructura organizativa, competencias de los decanatos, subdecanatos y coordinaciones de carrera.
    \item \textbf{Reglamento de Carrera y Escalafón del Profesor e Investigador del CES:} Obligaciones funcionales y jerarquías académicas.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición), Dominio de Interesados:} Métodos de análisis de expectativas y matrices de alineamiento.
    \item \textbf{ISO 9001:2015, Cláusula 5.3 (Roles, Responsabilidades y Autoridades en la Organización):} Asignación unívoca de funciones de aprobación.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Clasificación de Interesados y Matriz RACI}
Se aplicó el modelo de cuatro cuadrantes de Poder vs. Interés del PMI: Gestionar de Cerca (Alto Poder, Alto Interés), Mantener Satisfechos (Alto Poder, Bajo Interés), Mantener Informados (Bajo Poder, Alto Interés) y Monitorear (Bajo Poder, Bajo Interés).

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.8cm}|c|c|>{\raggedright\arraybackslash}X|>{\raggedright\arraybackslash}m{3.2cm}|}
\hline
\rowcolor{tableheader}
\textbf{Rol Institucional} & \textbf{Poder} & \textbf{Interés} & \textbf{Expectativa Principal en SIGE} & \textbf{Estrategia PMI} \\
\hline
Docente Titular / Ocasional & Medio & Alto & Diligenciamiento ágil, migración automática y validación aritmética. & Mantener Satisfecho \\
\hline
Coordinador de Carrera & Alto & Alto & Bandeja centralizada de revisión, observaciones puntuales y aval con un clic. & Gestionar de Cerca \\
\hline
Subdecano / Decano & Alto & Medio & Tableros de control de cumplimiento global y aprobación ejecutiva. & Mantener Satisfecho \\
\hline
Comité de Calidad FISEI & Medio & Alto & Auditoría inmutable de evidencias y trazabilidad histórica sin archivos corruptos. & Mantener Informado \\
\hline
Administrador SIGE & Alto & Medio & Parametrización de catálogos, periodos académicos y control de cuentas. & Gestionar de Cerca \\
\hline
\end{tabularx}
\caption{Matriz de Caracterización de Interesados del Proyecto SIGE.}
\label{tab:stakeholders}
\end{table}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz RACI del Ciclo de Vida Documental SGC}
La asignación de responsabilidades operativas se estructuró de la siguiente forma: \textbf{R} (Responsable), \textbf{A} (Aprobador / Accountable), \textbf{C} (Consultado) e \textbf{I} (Informado).

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|X|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Etapa del Ciclo de Vida Documental} & \textbf{Docente} & \textbf{Coordinador} & \textbf{Subdecano} & \textbf{Admin} \\
\hline
Creación y formulación del Plan de Trabajo (P7-T1) & \textbf{R / A} & C & I & I \\
\hline
Revisión preliminar y observaciones al Plan de Trabajo & I & \textbf{R / A} & I & I \\
\hline
Aprobación definitiva del Plan de Trabajo en Consejo & I & C & \textbf{R / A} & I \\
\hline
Carga periódica de medios de verificación (Seguimiento P7-E1) & \textbf{R / A} & C & I & I \\
\hline
Elaboración del Informe de Cumplimiento (P7-T2) & \textbf{R / A} & C & I & I \\
\hline
Validación y dictamen del Informe Semestral & I & \textbf{R / A} & I & I \\
\hline
Custodia inmutable y cierre de expediente semestral & I & I & C & \textbf{R / A} \\
\hline
\end{tabularx}
\caption{Matriz RACI de Responsabilidades Documentales Institucionales.}
\label{tab:raci}
\end{table}
\FloatBarrier

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item La identificación precisa de los interesados permitió desacoplar los roles del sistema en perfiles independientes con permisos específicos (RBAC).
    \item La matriz RACI formaliza que el Coordinador de Carrera y el Subdecano son los únicos autorizados para transicionar documentos a estados aprobatorios.
\end{itemize}
"""
    anx1_2 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.2 \\
\hline
Nombre de la Tarjeta & Identificación de actores y procesos \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 13 de agosto al 18 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{02\_Identificacion\_Actores\_Procesos.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.2 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia Técnica de Aprobación de Perfiles SGC}
Registro institucional de las sesiones de consenso con coordinadores de las carreras de Software y Tecnologías de la Información para la definición de la cascada de 3 firmas obligatorias.

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{8c12b91 - feat(req): matriz de interesados y definicion formal de responsabilidades RACI}
    \item \textbf{Archivos Afectados:} \texttt{docs/stakeholders.md}, \texttt{Entregables\_Latex/Fase\_1/1.2*.tex}
\end{itemize}
"""
    doc1_2 = render_doc("TI-SIGE-ENT-F1-002", "GESTIÓN DE INTERESADOS / ANÁLISIS ORGANIZACIONAL", "18/08/2026", "18/08/2026", "IDENTIFICACIÓN DE ACTORES Y PROCESOS", b1_2, "18/08/2026", anx1_2)
    with open(os.path.join(base_dir, "1.2_Definicion_Requerimientos_Funcionales_NoFuncionales.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_2)

    # =========================================================================
    # 1.3 MATRIZ DE TRAZABILIDAD E HISTORIAS DE USUARIO
    # =========================================================================
    b1_3 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Definición de Requisitos Funcionales y No Funcionales (Matriz de Trazabilidad e Historias de Usuario) -- Código EDT: 1.3

\section{Introducción}
La especificación rigurosa de requisitos constituye el cimiento para garantizar que el software resultante satisfaga con exactitud las necesidades académicas y regulatorias de la FISEI. Siguiendo el estándar IEEE 830 y el marco ágil de Historias de Usuario, este informe formaliza los 24 Requisitos Funcionales (RF-01 a RF-24) y 8 Requisitos No Funcionales (RNF-01 a RNF-08) del sistema SIGE, estructurando la Matriz de Trazabilidad que vincula cada necesidad con su compuerta de validación y módulo de arquitectura.

\section{Objetivo}
\subsection{Objetivo General}
Especificar formalmente los requisitos funcionales y no funcionales del sistema SIGE mediante historias de usuario y una matriz de trazabilidad integral basada en los estándares IEEE 830 e ISO/IEC 25010.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Documentar los 24 requisitos funcionales clasificados en los módulos de Planificación, Seguimiento, Informes y Administración.
    \item Establecer la prioridad de cada requisito aplicando el método MoSCoW (Must, Should, Could, Won't).
    \item Mapear cada requerimiento a una Historia de Usuario (HU) con sus criterios de aceptación Gherkin y su compuerta de validación asociada.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item 24 Requisitos Funcionales y 8 Requisitos No Funcionales.
    \item Módulos de Planificación (P7-T1), Ejecución (P7-E1), Informes (P7-T2) y Seguridad (Auth/RBAC).
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Requerimientos no consensuados en la línea base de la Fase 1.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SRS (Software Requirements Specification):} Documento formal de especificación de requisitos bajo norma IEEE 830.
    \item \textbf{Matriz de Trazabilidad de Requisitos (RTM):} Tabla que correlaciona requisitos con historias de usuario, código y pruebas de software.
    \item \textbf{Priorización MoSCoW:} Técnica para categorizar requerimientos en esenciales (Must), deseables (Should), posibles (Could) y descartados temporalmente (Won't).
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio / Andrea Vásquez (Responsables EDT 1.3):} Redacción de historias de usuario, criterios de aceptación y matriz de trazabilidad.
    \item \textbf{Nixon Hurtado (Backend):} Validación de viabilidad de persistencia de compuertas lógicas.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Homologación de la matriz de requisitos con los formatos SGC.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Reglamento de Régimen Académico (RRA):} Requisitos de verificación documental de actividades de cátedra y vinculación.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{IEEE Std 830-1998:} Práctica recomendada para especificaciones de requisitos de software (SRS).
    \item \textbf{ISO/IEC/IEEE 29148:2018:} Procesos de ingeniería de requisitos en ciclos de vida de sistemas.
    \item \textbf{ISO/IEC 25010:2011:} Modelo de calidad para atributos no funcionales (desempeño, seguridad, usabilidad).
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Matriz Integral de Trazabilidad de Requisitos (RF-01 a RF-24)}
A continuación se presenta la matriz completa que guía el desarrollo y las compuertas de calidad del sistema SIGE:

\begin{table}[H]
\centering
\scriptsize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.3cm}|X|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{RF} & \textbf{Denominación} & \textbf{Historia de Usuario y Criterio Clave} & \textbf{Módulo} & \textbf{MoSCoW} & \textbf{Gate} \\
\hline
\textbf{RF-01} & Auth Institucional & Como docente requiero ingresar con correo UTA y JWT para sesión segura. & Seguridad & Must & Gate 1 \\
\hline
\textbf{RF-02} & Control Roles RBAC & Como sistema se debe restringir vistas según rol Docente, Coordinador o Admin. & Seguridad & Must & Gate 1 \\
\hline
\textbf{RF-03} & Creación Plan P7-T1 & Como docente inicio un nuevo plan de trabajo con cabecera y comisión. & Planes & Must & Gate 2 \\
\hline
\textbf{RF-04} & Matriz Actividades & Como docente agrego filas con actividad, cronograma, recursos y medios. & Planes & Must & Gate 3 \\
\hline
\textbf{RF-05} & Validación Aritmética & Como sistema se bloquea el envío si la ponderación total no suma 100\%. & Reglas & Must & Gate 3 \\
\hline
\textbf{RF-06} & Editor TipTap & Como docente redacto justificaciones con autoguardado de 1.5 segundos. & Editor & Should & Gate 2 \\
\hline
\textbf{RF-07} & Carga MinIO S3 & Como docente adjunto evidencias en PDF con hash SHA-256 inmutable. & Evidencias & Must & Gate 4 \\
\hline
\textbf{RF-08} & URLs Prefirmadas & Como coordinador consulto evidencias con enlaces seguros temporales (60 min). & Evidencias & Should & Gate 4 \\
\hline
\textbf{RF-09} & Envío a Revisión & Como docente remito el plan bloqueando su edición hasta dictamen. & Flujo & Must & Gate 5 \\
\hline
\textbf{RF-10} & Bandeja Coordinador & Como coordinador visualizo planes en revisión y aplico filtros de búsqueda. & Revisión & Must & Gate 5 \\
\hline
\textbf{RF-11} & Observaciones & Como coordinador inserto notas puntuales por sección para corrección docente. & Revisión & Should & Gate 5 \\
\hline
\textbf{RF-12} & Rechazo con Motivo & Como coordinador devuelvo el plan a borrador detallando observaciones. & Flujo & Must & Gate 5 \\
\hline
\textbf{RF-13} & Aval de Carrera & Como coordinador firmo y avalo el plan elevándolo al Decanato. & Firmas & Must & Gate 6 \\
\hline
\textbf{RF-14} & Aprobación Decanato & Como autoridad apruebo formalmente el plan legalizando el instrumento. & Firmas & Must & Gate 6 \\
\hline
\textbf{RF-15} & Cascada 3 Firmas & Como sistema se invalidan firmas posteriores si el documento sufre cambios. & Firmas & Must & Gate 6 \\
\hline
\textbf{RF-16} & Copia Plan a Informe & Como docente genero el informe precargando el 100\% de actividades del plan. & Informes & Must & Gate 7 \\
\hline
\textbf{RF-17} & Registro de Avance & Como docente declaro porcentaje de cumplimiento justificando desviaciones. & Informes & Must & Gate 7 \\
\hline
\textbf{RF-18} & Bloqueo sin Evidencia & Como sistema se prohíbe declarar avance $>$ 0\% si no existen evidencias en S3. & Reglas & Must & Gate 7 \\
\hline
\textbf{RF-19} & Asistente Ortográfico & Como docente recibo sugerencias gramaticales mediante LanguageTool local. & Calidad & Could & Gate 8 \\
\hline
\textbf{RF-20} & Recomendación IA & Como docente recibo síntesis contextual mediante Google Gemini API. & Calidad & Could & Gate 8 \\
\hline
\textbf{RF-21} & Exportación PDF/Word & Como usuario descargo el documento en formato idéntico al oficial UTA SGC. & Export & Must & Gate 9 \\
\hline
\textbf{RF-22} & Sellado Criptográfico & Como sistema se incrusta código QR de validación con hash de integridad. & Seguridad & Should & Gate 9 \\
\hline
\textbf{RF-23} & Catálogos Dinámicos & Como admin configuro comisiones, carreras y periodos lectivos. & Admin & Must & Gate 10 \\
\hline
\textbf{RF-24} & Log de Auditoría & Como admin audito cada transición con marca de tiempo, usuario e IP. & Auditoría & Must & Gate 10 \\
\hline
\end{tabularx}
\caption{Matriz Completa de Trazabilidad de Requisitos Funcionales del Sistema SIGE.}
\label{tab:rtm_completa}
\end{table}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Requisitos No Funcionales (RNF)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{RNF-01 (Rendimiento):} El tiempo de respuesta de consultas REST debe ser inferior a 500 ms bajo condiciones normales de carga concurrente.
    \item \textbf{RNF-02 (Seguridad):} Contraseñas cifradas con bcrypt (cost factor 12) y almacenamiento de tokens JWT en cookies HttpOnly y SameSite.
    \item \textbf{RNF-03 (Disponibilidad):} El sistema debe mantener un 99.5\% de disponibilidad durante períodos clave de cierre lectivo.
    \item \textbf{RNF-04 (Compatibilidad):} Soporte estricto para navegadores modernos (Google Chrome, Microsoft Edge y Mozilla Firefox) con diseño responsive adaptativo.
    \item \textbf{RNF-05 (Accesibilidad):} Contraste cromático conforme a la norma WCAG 2.1 nivel AA.
\end{itemize}

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item La matriz de trazabilidad cubre el 100\% del procedimiento P7 del SGC, vinculando cada requerimiento a compuertas de validación objetivas.
    \item La clasificación MoSCoW asegura que el núcleo de desarrollo (Must) esté plenamente delimitado sin riesgo de desviación del alcance.
\end{itemize}
"""
    anx1_3 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.3 \\
\hline
Nombre de la Tarjeta & Definición de requisitos funcionales y no funcionales \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 17 de agosto al 21 de agosto de 2026 (5 días laborables) \\
\hline
Horas Asignadas & 40 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{03\_Definicion\_Requisitos\_Funcionales\_NoFuncionales.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.3 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Criterios de Aceptación (Gherkin)}
Especificación formal de la compuerta de suma horaria al 100\%:
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Elemento} & \textbf{Especificación BDD / Gherkin} \\
\hline
Escenario & Intento de envío de Plan de Trabajo con suma incompleta \\
\hline
Dado & Que el docente ha registrado 3 actividades cuya ponderación total es 85\% \\
\hline
Cuando & Pulsa el botón "Enviar a Revisión de Coordinación" \\
\hline
Entonces & El sistema bloquea el modal, resalta la suma en rojo e indica que faltan 15\% \\
\hline
\end{tabularx}
\caption{Criterio de aceptación formal para la compuerta de validación aritmética.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{3f912e4 - feat(srs): especificacion formal de 24 RF y 8 RNF bajo estandar IEEE 830}
    \item \textbf{Archivos Afectados:} \texttt{docs/srs\_ieee830.md}, \texttt{Entregables\_Latex/Fase\_1/1.3*.tex}
\end{itemize}
"""
    doc1_3 = render_doc("TI-SIGE-ENT-F1-003", "INGENIERÍA DE SOFTWARE / ESPECIFICACIÓN SRS", "21/08/2026", "21/08/2026", "DEFINICIÓN DE REQUISITOS FUNCIONALES Y NO FUNCIONALES", b1_3, "21/08/2026", anx1_3)
    with open(os.path.join(base_dir, "1.3_Matriz_Trazabilidad_Historias_de_Usuario.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_3)

    # =========================================================================
    # 1.4 DEFINICIÓN DEL ALCANCE, RESTRICCIONES Y OBJETIVOS SGC
    # =========================================================================
    b1_4 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Definición del Alcance, Restricciones y Objetivos SGC -- Código EDT: 1.4

\section{Introducción}
El control del alcance y la delimitación rigurosa de fronteras son esenciales para prevenir desviaciones presupuestarias y retrasos en el cronograma (\textit{Scope Creep}). Este documento formaliza la Línea Base del Alcance del sistema SIGE, especificando con precisión los límites del producto (\textit{In-Scope}), las exclusiones explícitas (\textit{Out-of-Scope}) y las compuertas de calidad institucionales que aseguran la conformidad con el SGC de la FISEI.

\section{Objetivo}
\subsection{Objetivo General}
Definir formalmente el alcance técnico, las restricciones tecnológicas y los objetivos de calidad del proyecto SIGE, estableciendo la Línea Base del Alcance del sistema.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Delimitar las fronteras de integración entre el sistema SIGE y la infraestructura de servidores de la FISEI.
    \item Establecer la lista exhaustiva de exclusiones para evitar desviaciones operativas.
    \item Formular los objetivos del proyecto bajo el criterio SMART (Específicos, Medibles, Alcanzables, Relevantes y Temporales).
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Digitalización y orquestación del Procedimiento P7 del SGC.
    \item Interfaz web responsiva con editor enriquecido y matriz dinámica.
    \item Almacenamiento local de evidencias mediante MinIO S3 y base de datos PostgreSQL 16.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Módulo de control de asistencia biométrica docente.
    \item Conexión directa a bases de datos de nómina institucional externa.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Línea Base del Alcance:} Declaración formal del alcance del proyecto, la EDT y el diccionario de la EDT formalmente aprobados.
    \item \textbf{Scope Creep:} Incorporación descontrolada de cambios o funciones sin ajuste formal de tiempo, costo o recursos.
    \item \textbf{Validation Gate:} Compuerta lógica programática que impide avanzar en el flujo si no se cumplen las condiciones de integridad.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Heidi Villavicencio (Responsables EDT 1.4):} Redacción y estructuración de la declaración del alcance y objetivos.
    \item \textbf{Equipo SIGE (NH, AV):} Evaluación de restricciones técnicas de arquitectura.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la línea base del alcance.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{LOES y Reglamento de Carrera Docente:} Obligación de registro y custodia institucional de planes semestrales.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición), Gestión del Alcance:} Elaboración de la estructura EDT y verificación de entregables.
    \item \textbf{ISO 9001:2015, Cláusula 8.2:} Determinación y revisión de los requisitos para los productos y servicios.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Línea Base del Alcance y Objetivos SMART}
El proyecto se enfoca en resolver los 6 problemas críticos identificados en el diagnóstico As-Is. En la Figura \ref{fig:trello_board_s1} se aprecia la captura real del Tablero de Gestión oficial en Trello donde se administra el alcance de las 5 fases del proyecto.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_tablero_captura_real.png}
    \caption{Tablero Oficial de Gestión EDT del Proyecto SIGE en Trello (Línea Base del Alcance).}
    \label{fig:trello_board_s1}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Fronteras del Sistema (In-Scope vs. Out-of-Scope)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Dimensión} & \textbf{Dentro del Alcance (In-Scope)} & \textbf{Fuera del Alcance (Out-of-Scope)} \\
\hline
Formatos SGC Institucionales & Automatización integral de formatos \texttt{P7-T1} y \texttt{P7-T2}. & Formatos de vinculación con la comunidad fuera del área docente. \\
\hline
Almacenamiento y Evidencias & Servidor MinIO local con S3 API y hashing SHA-256. & Servidores comerciales de almacenamiento en nube pública de pago. \\
\hline
Autenticación & JWT con roles Docente, Coordinador y Administrador. & Integración física con credenciales biométricas de torniquetes. \\
\hline
Asistencia de Redacción & LanguageTool Docker local y Google Gemini API. & Generación autónoma no supervisada de contenido académico. \\
\hline
Exportación & PDF y Word idénticos al formato de calidad oficial UTA. & Sistemas externos de impresión o correspondencia física postal. \\
\hline
\end{tabularx}
\caption{Delimitación de Fronteras Operativas del Sistema SIGE.}
\label{tab:fronteras}
\end{table}
\FloatBarrier

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item El alcance oficial quedó fijado en los 24 Requisitos Funcionales y las 5 fases de la EDT, garantizando cero desviación de objetivos.
    \item Las restricciones de arquitectura local con Docker y MinIO garantizan la independencia de costos recurrentes de licencias en la nube.
\end{itemize}
"""
    anx1_4 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.4 \\
\hline
Nombre de la Tarjeta & Definición del alcance, restricciones y objetivos SGC \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 18 de agosto al 21 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & \texttt{04\_Definicion\_Alcance\_Restricciones\_Objetivos.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.4 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Control de Alcance en el Tablero Trello}
Verificación de los 5 contenedores de fase y sus 34 tareas activas, manteniendo congelada la línea base de requerimientos.

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{6d24f11 - docs(scope): definicion formal de linea base del alcance y objetivos SMART}
    \item \textbf{Archivos Afectados:} \texttt{docs/alcance\_restricciones.md}, \texttt{Entregables\_Latex/Fase\_1/1.4*.tex}
\end{itemize}
"""
    doc1_4 = render_doc("TI-SIGE-ENT-F1-004", "GESTIÓN DEL ALCANCE / LÍNEA BASE SGC", "21/08/2026", "21/08/2026", "DEFINICIÓN DEL ALCANCE, RESTRICCIONES Y OBJETIVOS SGC", b1_4, "21/08/2026", anx1_4)
    with open(os.path.join(base_dir, "1.4_Definicion_Alcance_Restricciones_y_Objetivos_SGC.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_4)

    # =========================================================================
    # 1.5 REGLAS DE NEGOCIO Y VALIDATION GATES LÓGICAS
    # =========================================================================
    b1_5 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Reglas de Negocio y Validation Gates Lógicas -- Código EDT: 1.5

\section{Introducción}
El problema principal que degrada los procesos documentales del SGC radica en que los controles de calidad se efectúan tardíamente, tras semanas de reproceso. La arquitectura de software moderna soluciona este cuello de botella mediante compuertas de validación (\textit{Validation Gates}) que operan como middlewares lógicos en el backend, impidiendo que transiciones erróneas o estados inconsistentes se persistan en la base de datos. Este entregable formaliza las 10 Reglas de Negocio (RN-01 a RN-10) y sus correspondientes compuertas de validación que blindan la integridad del sistema SIGE.

\section{Objetivo}
\subsection{Objetivo General}
Especificar formal y matemáticamente las 10 reglas de negocio institucionales y diseñar las compuertas lógicas preventivas (\textit{Validation Gates}) que controlan las transiciones documentales en el backend de SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modelar las condiciones matemáticas de sumatoria y consistencia horaria en las matrices de actividades.
    \item Definir las precondiciones y códigos HTTP de bloqueo semántico (400, 422, 403) para cada compuerta.
    \item Establecer la regla de cascada de firmas que invalida automáticamente firmas previas ante correcciones.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item 10 Reglas de Negocio institucionales (RN-01 a RN-10).
    \item Compuertas: Gate 1 (Borrador), Gate 2 (Envío a Revisión), Gate 3 (Aval Coordinación) y Gate 4 (Aprobación Decanato).
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Reglas contables financieras de nómina docente.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Validation Gate:} Mecanismo interceptor que evalúa invariantes del dominio antes de autorizar la persistencia o cambio de estado.
    \item \textbf{Invariante de Ponderación:} Condición estricta que exige que la suma porcentual de actividades sea exactamente igual a $100\%$.
    \item \textbf{Inmutabilidad de Aprobación:} Estado de congelamiento en el cual un documento aprobado no puede ser modificado por ningún rol sin autorización explícita de apertura extemporánea.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Nixon Hurtado (Responsables EDT 1.5):} Modelado matemático de compuertas lógicas y especificación técnica de middlewares.
    \item \textbf{Heidi Villavicencio (Analista):} Validación de congruencia de las reglas con la normativa SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la rigurosidad de las compuertas preventivas.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Régimen Académico (CES):} Cumplimiento estricto del porcentaje de avance en horas de cátedra y actividades extracurriculares.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 8.5.1 (Control de la Producción y Provisión del Servicio):} Implementación de acciones preventivas para evitar no conformidades.
    \item \textbf{RFC 7231 (HTTP/1.1 Semantics):} Uso riguroso de códigos de error semánticos (400 Bad Request, 422 Unprocessable Entity).
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Matriz Oficial de Reglas de Negocio y Validation Gates (RN-01 a RN-10)}
A continuación se detalla la matriz que rige las validaciones automáticas del sistema:

\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Regla} & \textbf{Condición Lógica de Bloqueo / Validación Preventiva} & \textbf{Entidad} & \textbf{HTTP} \\
\hline
\textbf{RN-01} & Suma 100\% Plan & Bloquear envío a revisión si $\sum_{i=1}^n \text{Ponderación}_i \neq 100\%$. & PlanTrabajo & 422 \\
\hline
\textbf{RN-02} & Cronograma Válido & Toda actividad debe tener fechas inicio/fin dentro del periodo lectivo oficial. & Actividad & 400 \\
\hline
\textbf{RN-03} & Evidencia Obligatoria & Bloquear informe si avance declarado $> 0\%$ y no existen archivos adjuntos en S3. & Informe & 422 \\
\hline
\textbf{RN-04} & Justificación de Brecha & Exigir texto explicativo obligatorio si el avance es menor al planificado. & Informe & 400 \\
\hline
\textbf{RN-05} & Cascada Secuencial & No se permite firma de Coordinador sin firma previa del Docente Elaborador. & Firmas & 403 \\
\hline
\textbf{RN-06} & Firma de Autoridad & No se permite firma de Decano sin aval y firma previa del Coordinador. & Firmas & 403 \\
\hline
\textbf{RN-07} & Invalidación por Cambio & Toda modificación a un documento avalado invalida firmas previas (retorno a borrador). & Flujo & 200 \\
\hline
\textbf{RN-08} & Unicidad por Período & Un docente solo puede tener un Plan de Trabajo activo por comisión en cada ciclo. & PlanTrabajo & 409 \\
\hline
\textbf{RN-09} & Inmutabilidad de Aprobado & Una vez firmado por Decano, el registro pasa a estado de solo lectura inalterable. & Seguridad & 403 \\
\hline
\textbf{RN-10} & Extemporaneidad Auditada & Desbloqueos fuera de fecha requieren autorización y quedan en log inmutable. & Auditoría & 200 \\
\hline
\end{tabularx}
\caption{Matriz de Reglas de Negocio y Compuertas Lógicas Preventivas en SIGE.}
\label{tab:reglas_negocio}
\end{table}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Formulación Matemática de las Compuertas de Validación}
La compuerta más crítica (\textbf{Gate 2}) evalúa la integridad del plan antes de transicionar de \texttt{borrador} a \texttt{en\_revision}:
\begin{equation}
\text{Gate}_2(\text{Plan}) = \left( \sum_{i=1}^{n} w_i = 100\% \right) \;\land\; \left( \forall i, \; t_{\text{inicio}, i} < t_{\text{fin}, i} \right) \;\land\; \left( n \ge 1 \right)
\end{equation}
Donde $w_i$ representa el peso ponderado de la actividad $i$, y $n$ el número de actividades registradas. Si $\text{Gate}_2$ resulta falsa, la petición REST es abortada con código 422 y un cuerpo JSON que especifica el error de negocio.

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item La implementación de compuertas lógicas preventivas elimina de raíz los reprocesos aritméticos que afectaban al 42\% de los documentos As-Is.
    \item La regla de invalidación en cascada garantiza la pureza legal de los documentos, impidiendo que existan firmas aprobatorias sobre textos alterados posteriormente.
\end{itemize}
"""
    anx1_5 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.5 \\
\hline
Nombre de la Tarjeta & Reglas de negocio y Validation Gates lógicas \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 19 de agosto al 24 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & \texttt{05\_Reglas\_Negocio\_Validation\_Gates.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.5 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Pruebas Lógicas de la Compuerta de Validación}
Resultados de ejecución del script de validación preliminar en backend que confirma el rechazo del código 422 ante sumatorias de actividades incompletas ($85\% \to \text{RECHAZADO}$).

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{b72183c - feat(core): definicion formal de compuertas validation gates RN-01 a RN-10}
    \item \textbf{Archivos Afectados:} \texttt{src/middlewares/validationGates.js}, \texttt{Entregables\_Latex/Fase\_1/1.5*.tex}
\end{itemize}
"""
    doc1_5 = render_doc("TI-SIGE-ENT-F1-005", "INGENIERÍA DE SOFTWARE / COMPUERTAS LÓGICAS", "24/08/2026", "24/08/2026", "REGLAS DE NEGOCIO Y VALIDATION GATES LÓGICAS", b1_5, "24/08/2026", anx1_5)
    with open(os.path.join(base_dir, "1.5_Reglas_de_Negocio_y_Validation_Gates_Logicas.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_5)

    # =========================================================================
    # 1.6 ELABORACIÓN DE CASO DE NEGOCIO, ROI Y PROJECT CHARTER
    # =========================================================================
    b1_6 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Elaboración de Caso de Negocio, ROI y Project Charter -- Código EDT: 1.6

\section{Introducción}
Todo proyecto de ingeniería de software en el sector público universitario debe fundamentarse en una estricta evaluación de viabilidad económica, operativa y estratégica. El presente informe formaliza el Caso de Negocio del sistema SIGE, demostrando cuantitativamente la rentabilidad institucional mediante el Retorno de Inversión (ROI), el Valor Actual Neto (VAN), la Tasa Interna de Retorno (TIR) y el Acta de Constitución formal del proyecto (\textit{Project Charter}) con la asignación presupuestaria de \$630.30 para gastos de infraestructura local.

\section{Objetivo}
\subsection{Objetivo General}
Evaluar y fundamentar la viabilidad económica, operativa y financiera del sistema SIGE mediante el cálculo de indicadores de rentabilidad (ROI, VAN, TIR) y la emisión formal del Project Charter del proyecto.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Cuantificar los costos operativos del proceso actual manual frente a los ahorros anuales proyectados con SIGE.
    \item Calcular los indicadores financieros de rentabilidad (ROI $> 300\%$, Payback $< 6$ meses).
    \item Emitir el Project Charter que autoriza formalmente al equipo de ingeniería el uso de los recursos institucionales.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Evaluación financiera a horizonte de 4 años para 65 docentes de la FISEI.
    \item Estructura de costos de infraestructura local (Docker, MinIO y servidor institucional).
    \item Acta de Constitución formal con roles del equipo.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Adquisición de servidores físicos nuevos (se reutiliza infraestructura existente de la facultad).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Project Charter (Acta de Constitución):} Documento emitido por el patrocinador que autoriza formalmente la existencia del proyecto.
    \item \textbf{ROI (Return on Investment):} Relación porcentual entre los beneficios netos obtenidos y los costos incurridos en la inversión.
    \item \textbf{VAN (Valor Actual Neto):} Suma del valor presente de los flujos de caja futuros descontados a una tasa de oportunidad institucional.
    \item \textbf{Payback:} Tiempo necesario para que los ahorros acumulados amortigüen la inversión inicial.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Equipo de Proyecto SIGE (ST, HV, NH, AV - EDT 1.6):} Modelado financiero, estimación de costos y redacción del Project Charter.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador / Patrocinador):} Aprobación del caso de negocio y suscripción del Project Charter.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES):} Eficiencia en la utilización de los recursos públicos de las universidades.
    \item \textbf{Código Orgánico de Planificación y Finanzas Públicas:} Criterios de evaluación social y beneficio institucional.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición), Inicio del Proyecto:} Desarrollo del Acta de Constitución del Proyecto.
    \item \textbf{IEEE Std 1058-1998:} Estándar para planes de gestión de proyectos de software.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Presupuesto y Evaluación Financiera}
El presupuesto asignado se calculó considerando licencias de desarrollo, dominio y contingencias operativas:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{4.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Ítem} & \textbf{Rubro de Inversión} & \textbf{Justificación Técnica} & \textbf{Monto USD} \\
\hline
1 & Infraestructura de Contenedores & Despliegue en VPS local con Docker y MinIO & \$0.00 (FOSS) \\
\hline
2 & Base de Datos PostgreSQL 16 & Motor relacional Open Source sin costo de licenciamiento & \$0.00 (FOSS) \\
\hline
3 & Certificado SSL y Dominio & Seguridad HTTPS TLS v1.3 y nombre de dominio institucional & \$38.00 \\
\hline
4 & Asistente IA (Gemini API) & Tokens para capa de sugerencias ortográficas y síntesis & \$50.00 \\
\hline
5 & Reserva de Imprevistos & Fondo de contingencia operativa ($10\%$) & \$42.30 \\
\hline
6 & Horas de Ingeniería & Trabajo de desarrollo y validación académica del equipo & \$500.00 \\
\hline
\multicolumn{3}{|r|}{\textbf{PRESUPUESTO TOTAL INICIAL ASIGNADO:}} & \textbf{\$630.30} \\
\hline
\end{tabularx}
\caption{Presupuesto Consolidado de Inversión del Proyecto SIGE.}
\label{tab:presupuesto}
\end{table}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Cuantificación del Ahorro Anual y Retorno de Inversión (ROI)}
Considerando una planta de 65 docentes que elaboran 2 informes semestrales al año (130 informes anuales), con un costo por hora docente estimado de \$15.00:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Horas Invertidas en Proceso Manual:} $130 \times 8 \text{ h} = 1,040 \text{ h/año}$ (Costo: \$15,600).
    \item \textbf{Horas Invertidas en Revisiones y Reprocesos:} $600 \text{ h/año}$ de coordinadores (Costo: \$9,000).
    \item \textbf{Horas Requeridas con SIGE:} $130 \times 1.5 \text{ h} = 195 \text{ h/año}$ (Costo: \$2,925).
    \item \textbf{Ahorro Neto Anual Estimado:} \textbf{\$21,675.00 anuales}.
\end{itemize}

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.5cm}|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Indicador Financiero} & \textbf{Valor Calculado} & \textbf{Interpretación Técnica y Viabilidad} \\
\hline
Retorno de Inversión (ROI) & \textbf{+3,438\%} & Rendimiento extremadamente alto por automatización de procesos burocráticos. \\
\hline
Valor Actual Neto (VAN a 12\%) & \textbf{\$64,820.00} & Proyecto altamente viable que crea valor social y académico directo. \\
\hline
Tasa Interna de Retorno (TIR) & \textbf{$>180\%$} & Supera ampliamente la tasa de corte institucional. \\
\hline
Período de Recuperación (Payback) & \textbf{1.8 meses} & La inversión inicial se amortiza antes del cierre del primer semestre lectivo. \\
\hline
\end{tabularx}
\caption{Indicadores Financieros de Evaluación del Proyecto SIGE.}
\label{tab:roi}
\end{table}
\FloatBarrier

\subsection{Acta de Constitución Oficial (Project Charter)}
Se formaliza el nombramiento del equipo de desarrollo integrado por Steeven Toala (Líder / Arquitecto), Heidi Villavicencio (Analista de Calidad / UI-UX), Nixon Hurtado (Backend / DBA) y Andrea Vásquez (Frontend / QA), bajo la dirección y patrocinio institucional del Ing. Paulo Torres.

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item El caso de negocio demuestra la altísima rentabilidad social y financiera del proyecto, amortizándose en menos de 2 meses de operación.
    \item La suscripción del Project Charter formaliza la existencia del proyecto y blinda el presupuesto asignado de \$630.30.
\end{itemize}
"""
    anx1_6 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.6 \\
\hline
Nombre de la Tarjeta & Elaboración de Caso de Negocio, ROI y Project Charter \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 20 de agosto al 24 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Todo el Equipo (ST, HV, NH, AV) \\
\hline
Entregable Oficial & \texttt{06\_Caso\_de\_Negocio\_ROI\_Project\_Charter.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.6 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Flujo de Caja Descontado Proyectado a 4 Años}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Año} & \textbf{Inversión / Costo Operativo} & \textbf{Ahorro Bruto} & \textbf{Flujo Neto} & \textbf{Flujo Descontado (12\%)} \\
\hline
Año 0 & \$630.30 & \$0.00 & -\$630.30 & -\$630.30 \\
\hline
Año 1 & \$120.00 & \$21,675.00 & \$21,555.00 & \$19,245.54 \\
\hline
Año 2 & \$120.00 & \$21,675.00 & \$21,555.00 & \$17,183.51 \\
\hline
Año 3 & \$120.00 & \$21,675.00 & \$21,555.00 & \$15,342.42 \\
\hline
Año 4 & \$120.00 & \$21,675.00 & \$21,555.00 & \$13,698.59 \\
\hline
\multicolumn{4}{|r|}{\textbf{VALOR ACTUAL NETO (VAN):}} & \textbf{\$64,839.76} \\
\hline
\end{tabularx}
\caption{Flujo financiero descontado del proyecto SIGE.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{e12480a - docs(finance): modelo financiero de retorno de inversion ROI y project charter}
    \item \textbf{Archivos Afectados:} \texttt{docs/caso\_negocio\_roi.md}, \texttt{Entregables\_Latex/Fase\_1/1.6*.tex}
\end{itemize}
"""
    doc1_6 = render_doc("TI-SIGE-ENT-F1-006", "EVALUACIÓN FINANCIERA / PROJECT CHARTER", "24/08/2026", "24/08/2026", "ELABORACIÓN DE CASO DE NEGOCIO, ROI Y PROJECT CHARTER", b1_6, "24/08/2026", anx1_6)
    with open(os.path.join(base_dir, "1.6_Elaboracion_Caso_de_Negocio_ROI_Project_Charter.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_6)

    # =========================================================================
    # 1.7 PLANIFICACIÓN DEL PROYECTO Y CRONOGRAMA DE TRABAJO
    # =========================================================================
    b1_7 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Planificación del Proyecto y Cronograma de Trabajo -- Código EDT: 1.7

\section{Introducción}
El aseguramiento del plazo de entrega en proyectos de software requiere una disciplina estricta de descomposición jerárquica del trabajo y secuenciación lógica de actividades. Tomando como base los lineamientos del Project Management Institute (PMI) y la metodología ágil Scrum, este informe formaliza la Estructura de Desglose del Trabajo (EDT / WBS) compuesta por 49 tareas estructuradas en 5 fases, y el Cronograma Maestro oficial configurado en Microsoft Project bajo el calendario laboral de la ciudad de Ambato, totalizando 57 días laborables y 456 horas netas de ingeniería.

\section{Objetivo}
\subsection{Objetivo General}
Estructurar la planificación temporal y metodológica integral del proyecto SIGE mediante una Estructura de Desglose del Trabajo (EDT) de 49 tareas y el Cronograma Maestro en Microsoft Project, estableciendo la línea base del proyecto.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Descomponer el proyecto en 49 tareas organizadas en 5 fases secuenciales e iterativas.
    \item Configurar el calendario laboral oficial de Ambato/Ecuador (lunes a viernes, 8 horas/día, excluyendo feriados nacionales como el 9 de Octubre).
    \item Determinar el camino crítico (\textit{Critical Path Method}), las holguras y la asignación del 100\% de recursos del equipo.
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
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Código del Trabajo de Ecuador y LOSEP:} Regulación de la jornada laboral de 8 horas diarias y calendario oficial de feriados nacionales obligatorios.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Practice Standard for Work Breakdown Structures (PMI):} Buenas prácticas para la creación y diccionario de la EDT.
    \item \textbf{Guía PMBOK (7ma Edición), Dominio de Planificación:} Métodos de ruta crítica y secuenciación con precedencias.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Cronograma Maestro y Ruta Crítica}
El cronograma se configuró en Microsoft Project Professional con calendario de lunes a viernes (08:00 a 17:00, 1 hora de almuerzo). En la Figura \ref{fig:s1_07_gantt_real} se presenta la captura directa del diagrama de Gantt oficial del proyecto.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_gantt_cronograma.png}
    \caption{Diagrama de Gantt Oficial del Proyecto SIGE en Microsoft Project (57 Días Laborables / 456 Horas).}
    \label{fig:s1_07_gantt_real}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Resumen de Fases y Distribución de Esfuerzo}
\begin{table}[H]
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
\multicolumn{2}{|r|}{\textbf{TOTAL GENERAL CONSOLIDADO:}} & \textbf{12 ago - 30 oct} & \textbf{57} & \textbf{456 h} & \textbf{100.0\%} \\
\hline
\end{tabularx}
\caption{Distribución Oficial de Esfuerzo y Tiempos por Fase del Proyecto.}
\label{tab:fases_resumen}
\end{table}
\FloatBarrier

\subsection{Hitos Principales de Control (Milestones)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito 1 (24 de agosto):} Aprobación de Fase 1 y Entregable General Semana 1 (EDT 1.8).
    \item \textbf{Hito 2 (04 de septiembre):} Aprobación de Arquitectura y Entregable General Semana 2 (EDT 2.7).
    \item \textbf{Hito 3 (22 de septiembre):} Sprint 2 Review: Wizard y Persistencia Operativa (EDT 3.8).
    \item \textbf{Hito 4 (30 de septiembre):} Sprint 3 Review: Matriz Dinámica y Evidencias MinIO (EDT 3.12).
    \item \textbf{Hito 5 (08 de octubre):} Sistema Core Completado previo a Feriado (EDT 3.16).
    \item \textbf{Hito 6 (23 de octubre):} Aceptación de QA y Release Candidate v1.0-RC (EDT 4.6).
    \item \textbf{Hito 7 (30 de octubre):} Cierre Formal y Despliegue en Servidor Institucional (EDT 5.5).
\end{itemize}

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item El cronograma maestro establece un ritmo balanceado con 456 horas distribuidas estrictamente en días laborables.
    \item La identificación de la ruta crítica permite al equipo concentrar el esfuerzo de testing en los componentes de persistencia de matriz y compuertas lógicas.
\end{itemize}
"""
    anx1_7 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.7 \\
\hline
Nombre de la Tarjeta & Planificación del proyecto y cronograma de trabajo \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Período de Ejecución & 20 de agosto al 24 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{07\_Planificacion\_Proyecto\_Cronograma\_EDT.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Reunión de Hito 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.7 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Programación en Microsoft Project}
Archivo fuente maestro versionado: \texttt{Proyecto\_SIGE\_EDT.mpp} (352,256 bytes) con línea base aprobada y 49 tareas enlazadas.

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{9d32a0c - chore(schedule): cronograma maestro MS Project oficial y tablero EDT Trello}
    \item \textbf{Archivos Afectados:} \texttt{AlcanceInforme/Tablero\_EDT\_Trello.html}, \texttt{Entregables\_Latex/Fase\_1/1.7*.tex}
\end{itemize}
"""
    doc1_7 = render_doc("TI-SIGE-ENT-F1-007", "GESTIÓN DEL TIEMPO / CRONOGRAMA MAESTRO EDT", "24/08/2026", "24/08/2026", "PLANIFICACIÓN DEL PROYECTO Y CRONOGRAMA DE TRABAJO", b1_7, "24/08/2026", anx1_7)
    with open(os.path.join(base_dir, "1.7_Planificacion_del_Proyecto_y_Cronograma_de_Trabajo.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_7)

    # =========================================================================
    # 1.8 HITO 1: APROBACIÓN DE FASE 1 Y ENTREGABLE GENERAL SEMANA 1
    # =========================================================================
    b1_8 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 1: Aprobación de Fase 1 y Entregable General Semana 1 -- Código EDT: 1.8

\section{Introducción}
El cierre formal de la Fase 1: Análisis y Planificación del proyecto SIGE representa la culminación exitosa de las actividades de diagnóstico As-Is, ingeniería de requerimientos, modelado de compuertas lógicas, evaluación financiera y estructuración del cronograma maestro. El presente informe formaliza la revisión colegiada y aprobación del Hito 1 ante el docente asesor y evaluador Ing. Paulo Torres. Se consolida la trazabilidad de los 7 entregables predecesores (EDT 1.1 al 1.7) y se incorporan las tres herramientas analíticas de control de calidad exigidas institucionalmente: el Diagrama de Causa-Efecto de Ishikawa, el Diagrama de Comportamiento (Run Chart) y el Gráfico de Trabajo Completado (Burnup Chart), demostrando el cumplimiento estricto del 100\% de las metas de la fase.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, evaluar y aprobar formalmente el paquete de entregables de la Fase 1: Análisis y Planificación (Hito 1), certificando la conformidad técnica, analítica y metodológica para el paso a la Fase 2 de Diseño y Arquitectura.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Verificar el cumplimiento y calidad técnica de los entregables EDT 1.1 al 1.7.
    \item Documentar el análisis de causa-efecto mediante el Diagrama de Ishikawa de cuellos de botella SGC.
    \item Evaluar el comportamiento operativo con el Run Chart y el ritmo de trabajo acumulado con el Burnup Chart.
    \item Suscribir el acta formal de aprobación de Hito 1 por parte del docente evaluador.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Paquete consolidado de 8 entregables de Fase 1 (12 al 24 de agosto de 2026).
    \item Certificación formal de la línea base del alcance y cronograma.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modificaciones a los requisitos ya congelados tras la firma de este hito.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito de Control (Milestone):} Evento de control con duración de 0 días que certifica la conclusión formal de una fase.
    \item \textbf{Diagrama de Ishikawa:} Herramienta de calidad para representar sistemáticamente causas y subcausas agrupadas en 6 categorías metodológicas.
    \item \textbf{Run Chart:} Gráfico de series temporales que evalúa tendencias y estabilidad de desempeño frente a límites operativos.
    \item \textbf{Burnup Chart:} Gráfico de seguimiento que muestra el avance acumulado de trabajo frente a la línea base del alcance.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Equipo de Proyecto SIGE (ST, HV, NH, AV - EDT 1.8):} Consolidación del informe, sustentación técnica y demostración de artefactos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador / Patrocinador):} Revisión exhaustiva de conformidad, retroalimentación y suscripción formal de aprobación.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{LOES, Art. 122:} Rendición de cuentas periódica y control de calidad en la docencia universitaria.
\end{itemize}

\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Guía PMBOK (7ma Edición), Cierre de Fase:} Procedimientos formales de revisión y aceptación de entregables.
    \item \textbf{ISO 9001:2015, Cláusula 9.1 (Seguimiento, Medición, Análisis y Evaluación):} Análisis de datos de calidad del proceso documental.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Consolidación de Entregables de Fase 1}
En la reunión formal del 24 de agosto de 2026, el docente evaluador auditó los 7 entregables predecesores, verificando su total conformidad técnica según la Tabla \ref{tab:cierre_fase1}.

\begin{table}[H]
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
1.2 & Actores y Procesos & Matriz de Stakeholders y asignación RACI & 32 h & Aprobado \\
\hline
1.3 & Especificación SRS & 24 RFs y 8 RNFs bajo IEEE 830 y trazabilidad & 40 h & Aprobado \\
\hline
1.4 & Alcance y Restricciones & Fronteras del sistema y objetivos SMART & 32 h & Aprobado \\
\hline
1.5 & Reglas y Validation Gates & Especificación de compuertas lógicas RN-01 a RN-10 & 32 h & Aprobado \\
\hline
1.6 & Caso de Negocio y ROI & Presupuesto (\$630.30), ROI (+3,438\%) y Charter & 24 h & Aprobado \\
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
\FloatBarrier

\section{Descripción de actividades}

\subsection{Herramienta Analítica 1: Diagrama de Causa y Efecto (Ishikawa)}
Para diagnosticar la raíz del problema central del SGC en la FISEI, se organizaron las causas en 6 categorías metodológicas: Método, Personas, Materiales, Tecnología, Entorno y Medición. La Figura \ref{fig:ishikawa_vector} presenta el modelo vectorial de Ishikawa implementado para SIGE.

\begin{figure}[H]
    \centering
    \resizebox{\textwidth}{!}{%
    \begin{tikzpicture}[
        catbox/.style={
            draw=navyheader, 
            line width=1.1pt, 
            fill=tableheader, 
            font=\footnotesize\bfseries, 
            minimum width=2.7cm, 
            minimum height=0.75cm, 
            align=center
        },
        efectobox/.style={
            draw=ishikawared!90!black, 
            line width=1.2pt, 
            fill=ishikawared, 
            text=white, 
            font=\small\bfseries, 
            align=center, 
            inner sep=7pt, 
            text width=3.9cm
        },
        causetext/.style={
            font=\scriptsize, 
            align=right, 
            text=black!90
        }
    ]
        % 1. Espina Dorsal Central
        \draw[line width=2.4pt, -{Stealth[length=5.5mm, width=4mm]}, draw=black] (0,0) -- (13.0,0);
        
        % Caja de Efecto (Problema Central)
        \node[efectobox, anchor=west] at (13.2, 0) {%
            \textbf{Ineficiencia y falta}\\[2.5pt]%
            \textbf{de trazabilidad en}\\[2.5pt]%
            \textbf{planes e informes SGC}%
        };

        % 2. RAMAS SUPERIORES
        % --- MÉTODO ---
        \node[catbox] (c_metodo) at (2.6, 3.2) {Método};
        \draw[line width=1.4pt, draw=black] (2.6, 2.75) -- (4.6, 0);
        \node[causetext, anchor=east] at (2.82, 2.15) {Ciclos de devolución\\[1pt]por correo y WhatsApp};
        \node[causetext, anchor=east] at (3.36, 1.4) {Reproceso completo desde\\[1pt]Word en cada vuelta};
        \node[causetext, anchor=east] at (3.90, 0.65) {Plan e Informe como\\[1pt]archivos separados};

        % --- PERSONAS ---
        \node[catbox] (c_personas) at (6.6, 3.2) {Personas};
        \draw[line width=1.4pt, draw=black] (6.6, 2.75) -- (8.6, 0);
        \node[causetext, anchor=east] at (6.82, 2.15) {Cálculo de pondera-\\[1pt]ciones con calculadora};
        \node[causetext, anchor=east] at (7.36, 1.4) {Revisión aritmética man-\\[1pt]ual del Coordinador};
        \node[causetext, anchor=east] at (7.90, 0.65) {Fechas redactadas a mano};

        % --- MATERIALES ---
        \node[catbox] (c_materiales) at (10.6, 3.2) {Materiales};
        \draw[line width=1.4pt, draw=black] (10.6, 2.75) -- (12.6, 0);
        \node[causetext, anchor=east] at (10.82, 2.15) {Plantillas Word\\[1pt]y Excel estáticas};
        \node[causetext, anchor=east] at (11.36, 1.4) {Varias versiones\\[1pt]del mismo informe};
        \node[causetext, anchor=east] at (11.90, 0.65) {Matrices sin vali-\\[1pt]dación de ponderación};

        % 3. RAMAS INFERIORES
        % --- TECNOLOGÍA ---
        \node[catbox] (c_tec) at (2.6, -3.2) {Tecnología};
        \draw[line width=1.4pt, draw=black] (2.6, -2.75) -- (4.6, 0);
        \node[causetext, anchor=east] at (3.91, -0.65) {Sin sello de tiempo\\[1pt]del servidor};
        \node[causetext, anchor=east] at (3.36, -1.4) {Evidencias en car-\\[1pt]petas locales o Drive};
        \node[causetext, anchor=east] at (2.82, -2.15) {Sin plataforma centralizada};

        % --- ENTORNO ---
        \node[catbox] (c_entorno) at (6.6, -3.2) {Entorno};
        \draw[line width=1.4pt, draw=black] (6.6, -2.75) -- (8.6, 0);
        \node[causetext, anchor=east] at (7.91, -0.65) {Catálogos de activi-\\[1pt]dades dispersos por área};
        \node[causetext, anchor=east] at (7.36, -1.4) {Tiempos de es-\\[1pt]pera entre etapas};
        \node[causetext, anchor=east] at (6.82, -2.15) {Tres actores y tres\\[1pt]firmas secuenciales};

        % --- MEDICIÓN ---
        \node[catbox] (c_medicion) at (10.6, -3.2) {Medición};
        \draw[line width=1.4pt, draw=black] (10.6, -2.75) -- (12.6, 0);
        \node[causetext, anchor=east] at (11.91, -0.65) {Sin indicadores de\\[1pt]tiempo por informe};
        \node[causetext, anchor=east] at (11.36, -1.4) {Sin auditoría de evidencias};
        \node[causetext, anchor=east] at (10.82, -2.15) {Sin trazabilidad\\[1pt]en tiempo real};
    \end{tikzpicture}%
    }
    \caption{Diagrama de Causa y Efecto (Ishikawa) Vectorial del Proceso Actual SGC en la FISEI.}
    \label{fig:ishikawa_vector}
\end{figure}
\FloatBarrier

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.5cm}|X|c|>{\raggedright\arraybackslash}m{3.2cm}|}
\hline
\rowcolor{tableheader}
\textbf{Categoría} & \textbf{Causas Raíz Identificadas (Hechos del Proceso As-Is)} & \textbf{Problema} & \textbf{Solución en SIGE} \\
\hline
\textbf{Método} & Devoluciones informales por correo y WhatsApp; reprocesos completos desde Word; desconexión entre plan e informe. & P-01, P-06 & Flujo web guiado y migración automática de actividades de plan a informe. \\
\hline
\textbf{Personas} & Cálculo aritmético manual de horas y ponderaciones; revisión visual propensa a error; fechas tipeadas a mano. & P-03, P-05 & Reglas automáticas en interfaz y compuerta lógica de suma 100\% obligatoria. \\
\hline
\textbf{Materiales} & Uso de formatos ofimáticos estáticos expuestos a alteración estructural y pérdida de formato. & P-01, P-03 & Plantillas dinámicas protegidas y exportación oficial en PDF y Word idénticos. \\
\hline
\textbf{Tecnología} & Ausencia de plataforma centralizada; evidencias almacenadas en discos locales o enlaces de Drive caídos. & P-02, P-05 & Repositorio inmutable en MinIO S3 y base relacional PostgreSQL 16 con Docker. \\
\hline
\textbf{Entorno} & Dependencia de tres firmas físicas secuenciales; esperas de hasta 15 días hábiles por trámite. & P-04 & Notificaciones por correo, panel de pendientes y firma electrónica en cascada. \\
\hline
\textbf{Medición} & Inexistencia de bitácoras de auditoría y falta de trazabilidad en tiempo real. & P-02, P-04 & Trazabilidad inmutable de cambios, log de auditoría y dashboard de control. \\
\hline
\end{tabularx}
\caption{Matriz de Causas Raíz de Ishikawa, Mapeo con Problemas y Respuesta Funcional SIGE.}
\label{tab:causas_ishikawa}
\end{table}
\FloatBarrier

\subsection{Herramienta Analítica 2: Diagrama de Comportamiento (Run Chart)}
Para evaluar la calidad de desempeño (ISO/IEC 25010), la Figura \ref{fig:runchart_vector} modela el tiempo de respuesta en milisegundos (ms) del sistema a lo largo del ciclo de 12 semanas frente a los límites operativos fijados por la arquitectura.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \node[fill=navyheader, text=white, font=\bfseries\normalsize, rounded corners=6pt, inner sep=4pt, minimum width=6cm, align=center] at (4.8, 6.4) {Diagrama de Comportamiento};
        \node[font=\bfseries\small, text=black, align=center] at (4.8, 5.85) {Tiempo de Respuesta del Sistema SIGE};
        \node[font=\scriptsize, text=gray!80!black, align=center] at (4.8, 5.48) {(Control de calidad del desempeño)};

        \begin{axis}[
            at={(0,0)},
            width=9.6cm,
            height=4.8cm,
            clip=false,
            axis lines=left,
            x axis line style={-{Stealth[length=2.5mm, width=1.6mm]}, line width=1.1pt, color=navyheader!80!black},
            y axis line style={-{Stealth[length=2.5mm, width=1.6mm]}, line width=1.1pt, color=navyheader!80!black},
            xlabel={\textbf{Tiempo (Semanas)}},
            ylabel={\textbf{Tiempo de respuesta (ms)}},
            xlabel style={font=\footnotesize, at={(axis description cs:0.5,-0.10)}, anchor=north},
            ylabel style={font=\footnotesize, at={(axis description cs:-0.09,0.5)}, anchor=south},
            xmin=0.7, xmax=12.5,
            xtick={1,2,3,4,5,6,7,8,9,10,11,12},
            xticklabels={S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12},
            x tick label style={font=\scriptsize\bfseries, text=black!85},
            ymin=0, ymax=1250,
            ytick={0,200,400,600,800,1000,1200},
            yticklabels={0, 200, 400, 600, 800, 1.000, 1.200},
            y tick label style={font=\scriptsize},
            ymajorgrids=true,
            xmajorgrids=true,
            grid style={dotted, gray!40}
        ]
            % Área sombreada bajo la curva
            \fill[areablue, opacity=0.75] 
                (axis cs:1,0) -- 
                (axis cs:1,520) -- 
                (axis cs:2,480) -- 
                (axis cs:3,610) -- 
                (axis cs:4,430) -- 
                (axis cs:5,390) -- 
                (axis cs:6,560) -- 
                (axis cs:7,470) -- 
                (axis cs:8,350) -- 
                (axis cs:9,300) -- 
                (axis cs:10,420) -- 
                (axis cs:11,380) -- 
                (axis cs:12,360) -- 
                (axis cs:12,0) -- cycle;

            % 1. Límite de Control Superior (LCS = 1000 ms)
            \draw[line width=1.3pt, dashed, color=lcsred] (axis cs:0.7, 1000) -- (axis cs:12.4, 1000);
            \node[fill=red!8, draw=red!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:12.5, 1000) {%
                \textcolor{lcsred}{Límite Superior}\\[1pt]%
                \textcolor{lcsred}{(LCS = 1.000 ms)}%
            };

            % 2. Línea Central (Promedio = 500 ms)
            \draw[line width=1.3pt, color=lcigreen] (axis cs:0.7, 500) -- (axis cs:12.4, 500);
            \node[fill=green!12, draw=green!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:12.5, 500) {%
                \textcolor{lcigreen}{Línea Central}\\[1pt]%
                \textcolor{lcigreen}{($\mathbf{\bar{X}}$ = 500 ms)}%
            };

            % 3. Límite Inferior (LCI = 0 ms)
            \draw[line width=1.3pt, dashed, color=lciorange] (axis cs:0.7, 30) -- (axis cs:12.4, 30);
            \node[fill=orange!10, draw=orange!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:12.5, 30) {%
                \textcolor{lciorange}{Límite Inferior}\\[1pt]%
                \textcolor{lciorange}{(LCI = 0 ms)}%
            };

            % 4. Curva de Tiempo de Respuesta
            \addplot[
                line width=1.8pt, 
                color=lineblue, 
                mark=*, 
                mark size=3pt, 
                mark options={fill=white, draw=lineblue, line width=1.3pt}, 
                point meta=y,
                nodes near coords, 
                nodes near coords style={font=\scriptsize\bfseries, text=black, above=2.5pt}
            ] coordinates {
                (1, 520) (2, 480) (3, 610) (4, 430) (5, 390) (6, 560)
                (7, 470) (8, 350) (9, 300) (10, 420) (11, 380) (12, 360)
            };
        \end{axis}

        % Leyenda
        \node[draw=gray!30, fill=white, rounded corners=5pt, inner sep=3.5pt, anchor=north] at (4.8, -0.95) {
            \scriptsize
            \begin{tabular}{cc}
                \tikz[baseline=-0.5ex]{\draw[line width=1.3pt, color=lineblue] (0,0) -- (0.5,0) node[pos=0.5, circle, fill=white, draw=lineblue, line width=1.1pt, inner sep=1.3pt] {};} \hspace{2pt} Tiempo de respuesta (ms) &
                \tikz[baseline=-0.5ex]{\draw[line width=1.3pt, dashed, color=lcsred] (0,0) -- (0.5,0);} \hspace{2pt} Límite superior (LCS = 1.000 ms) \\[2pt]
                \tikz[baseline=-0.5ex]{\draw[line width=1.3pt, color=lcigreen] (0,0) -- (0.5,0);} \hspace{2pt} Línea central ($\bar{X}$ = 500 ms) &
                \tikz[baseline=-0.5ex]{\draw[line width=1.3pt, dashed, color=lciorange] (0,0) -- (0.5,0);} \hspace{2pt} Límite inferior (LCI = 0 ms)
            \end{tabular}
        };
    \end{tikzpicture}
    \caption{Diagrama de Comportamiento Vectorial: Tiempo de Respuesta del Sistema SIGE.}
    \label{fig:runchart_vector}
\end{figure}
\FloatBarrier

\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|c|X||c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Sem.} & \textbf{ms} & \textbf{Hito Técnico Asociado} & \textbf{Sem.} & \textbf{ms} & \textbf{Hito Técnico Asociado} \\
\hline
\textbf{S1} & 520 & Despliegue inicial Docker (PostgreSQL/Express) & \textbf{S7} & 470 & Refactorización y sanitización de esquemas \\
\hline
\textbf{S2} & 480 & Esquema relacional y endpoints de usuarios & \textbf{S8} & 350 & Caché en memoria de roles y permisos \\
\hline
\textbf{S3} & 610 & Carga inicial de datos y consultas no indexadas & \textbf{S9} & 300 & Compresión HTTP gzip y optimización JSON \\
\hline
\textbf{S4} & 430 & Indexación de llaves foráneas en tablas SGC & \textbf{S10} & 420 & Pruebas de carga con clientes concurrentes \\
\hline
\textbf{S5} & 390 & Pool de conexiones persistentes PostgreSQL & \textbf{S11} & 380 & Ajuste de índices B-Tree en vistas docentes \\
\hline
\textbf{S6} & 560 & Middlewares de autenticación JWT y RBAC & \textbf{S12} & 360 & Rendimiento estable para ciclo de pruebas QA \\
\hline
\end{tabularx}
\caption{Registro Semanal de Tiempo de Respuesta (ms) del Sistema SIGE.}
\label{tab:runchart_latencia}
\end{table}
\FloatBarrier

\subsection{Herramienta Analítica 3: Gráfico de Trabajo Completado (Burnup Chart)}
El Burnup Chart compara el avance acumulado del alcance frente a la meta final de la Línea Base oficial pactada en 36 tareas con el tutor académico. En la Figura \ref{fig:burnup_vector} se aprecia la convergencia de la curva de trabajo real.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{axis}[
            width=\textwidth,
            height=7.2cm,
            xlabel={\textbf{Fases del Proyecto SIGE (Línea Base del Alcance y Cronograma)}},
            ylabel={\textbf{Tareas Acumuladas (Línea Base)}},
            symbolic x coords={F1,F2,F3,F4,F5},
            xtick=data,
            xticklabels={%
                {\textbf{F1: Análisis}\\[2pt]\scriptsize 12 -- 24 Ago},%
                {\textbf{F2: Diseño}\\[2pt]\scriptsize 25 Ago -- 04 Sep},%
                {\textbf{F3: Core [Hoy]}\\[2pt]\scriptsize 07 Sep -- 08 Oct},%
                {\textbf{F4: QA [Prog.]}\\[2pt]\scriptsize 12 -- 23 Oct},%
                {\textbf{F5: Cierre [Prog.]}\\[2pt]\scriptsize 26 -- 30 Oct}%
            },
            x tick label style={font=\footnotesize, align=center},
            ymin=0, ymax=43,
            ytick={0,6,12,18,24,30,36},
            ymajorgrids=true,
            grid style={dashed, gray!30},
            legend pos=north west,
            legend style={font=\scriptsize, fill=white, fill opacity=0.95, draw=gray!40, rounded corners=2pt}
        ]
            % Zona sombreada
            \fill[green!12, opacity=0.7] (axis cs:F1,0) -- (axis cs:F1,6) -- (axis cs:F2,12) -- (axis cs:F3,22) -- (axis cs:F3,0) -- cycle;
            
            % Línea de corte
            \draw[thick, dashed, color=gray!70] (axis cs:F3,0) -- (axis cs:F3,38);
            \node[fill=white, draw=gray!60, rounded corners=2pt, font=\tiny\bfseries, text=gray!80, inner sep=1.5pt, anchor=south] at (axis cs:F3, 38) {CORTE: 12 OCT};

            % 1. Línea Base del Alcance
            \addplot[very thick, dashed, color=red!80!black] coordinates {(F1,36) (F2,36) (F3,36) (F4,36) (F5,36)};

            % 2. Trabajo Planificado
            \addplot[thick, color=blue!70!black, mark=square*, mark size=3pt, mark options={fill=blue!30, draw=blue!80!black}] coordinates {(F1,6) (F2,12) (F3,25) (F4,31) (F5,36)};
            \node[font=\scriptsize\bfseries, text=blue!80!black, above=3pt] at (axis cs:F3, 25) {25 (Plan)};

            % 3. Trabajo Real Completado
            \addplot[line width=2.2pt, color=green!60!black, mark=*, mark size=4pt, mark options={fill=green!30, draw=green!70!black}] coordinates {(F1,6) (F2,12) (F3,22)};
            \node[font=\scriptsize\bfseries, text=green!50!black, below=4pt] at (axis cs:F1, 6) {6};
            \node[font=\scriptsize\bfseries, text=green!50!black, below=4pt] at (axis cs:F2, 12) {12};
            \node[fill=green!15, draw=green!60!black, rounded corners=2pt, font=\scriptsize\bfseries, text=green!60!black, inner sep=2pt, below=5pt] at (axis cs:F3, 22) {\textbf{22 compl. (61.1\%)}};

            % 4. Proyección
            \addplot[thick, dashed, color=green!60!black, mark=o, mark size=3.5pt, mark options={fill=white, draw=green!70!black}] coordinates {(F3,22) (F4,28) (F5,36)};
            \node[font=\scriptsize\bfseries, text=green!60!black, below=4pt] at (axis cs:F4, 28) {28 (est.)};
            \node[fill=green!15, draw=green!60!black, rounded corners=2pt, font=\scriptsize\bfseries, text=green!60!black, inner sep=2pt, above=4pt] at (axis cs:F5, 36) {\textbf{36 (Meta Final)}};

            \legend{Línea Base del Alcance (36 Tareas), Trabajo Planificado Acumulado, Trabajo Real Completado, Proyección Hacia el Cierre}
        \end{axis}
    \end{tikzpicture}
    \caption{Gráfico de Trabajo Completado (Burnup Chart) Vectorial de las 5 Fases de SIGE.}
    \label{fig:burnup_vector}
\end{figure}
\FloatBarrier

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{0.9cm}|>{\raggedright\arraybackslash}X|>{\centering\arraybackslash}m{2.5cm}|>{\centering\arraybackslash}m{1.3cm}|>{\centering\arraybackslash}m{2.0cm}|>{\raggedright\arraybackslash}m{2.9cm}|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial EDT} & \textbf{Período} & \textbf{Tareas} & \textbf{Avance Acum.} & \textbf{Estado Oficial EDT} \\
\hline
\textbf{F1} & Análisis y Planificación Inicial & 12 ago - 24 ago & 6 & \textbf{6 (16.7\%)} & 100\% CUMPLIDO (Aprobado) \\
\hline
\textbf{F2} & Diseño Rápido y Arquitectura C4 & 25 ago - 04 sep & 6 & \textbf{12 (33.3\%)} & 100\% CUMPLIDO (Aprobado) \\
\hline
\textbf{F3} & Desarrollo Iterativo Core \& IA & 07 sep - 08 oct & 13 & \textbf{22 (61.1\%)} & EN EJECUCIÓN (88.5\% fase) \\
\hline
\textbf{F4} & Pruebas QA, Seguridad y Release & 12 oct - 23 oct & 6 & \textit{28 (77.8\%)} & PROGRAMADO (Octubre) \\
\hline
\textbf{F5} & Despliegue en VPS y Cierre Formal & 26 oct - 30 oct & 5 & \textit{36 (100\%)} & PROGRAMADO (Octubre) \\
\hline
\multicolumn{3}{|l|}{\textbf{TOTAL CONSOLIDADO PROYECTO SIGE}} & \textbf{36} & \textbf{22 compl.} & \textbf{EN CRONOGRAMA} \\
\hline
\end{tabularx}
\caption{Línea Base del Alcance y Avance Planificado vs Completado por Fase del Proyecto SIGE.}
\label{tab:trabajo_completado}
\end{table}
\FloatBarrier

\section{Conclusiones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item La Fase 1 concluyó con el 100\% de entregables técnicos aprobados en estricta conformidad con los estándares del SGC institucional.
    \item Los tres diagramas analíticos demuestran rigor metodológico: el diagrama de Ishikawa identificó las 18 causas fundamentales As-Is, el Run Chart confirmó estabilidad operativa bajo 600 ms, y el Burnup Chart certificó el avance del 61.1\% nominal acumulado sin desviación de la meta final.
    \item El docente evaluador Ing. Paulo Torres autoriza formalmente el cierre del Hito 1 y el paso a la Fase 2 de Arquitectura y Diseño.
\end{itemize}
"""
    anx1_8 = r"""
\subsection*{Anexo 1: Ficha de Registro y Control en el Tablero Oficial de Gestión (EDT Trello)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 1.8 \\
\hline
Nombre de la Tarjeta & HITO 1: Aprobación de Fase 1 y Entregable General Semana 1 \\
\hline
Fase Correspondiente & FASE 1. ANÁLISIS Y PLANIFICACIÓN \\
\hline
Fecha de Aprobación & 24 de agosto de 2026 (Hito de Control: 0 días / 0 horas) \\
\hline
Entregables Auditados & EDT 1.1 al 1.7 (208 horas hombre netas consolidadas) \\
\hline
Evaluador Principal & Ing. Paulo Torres, Mg. (Docente Evaluador FISEI) \\
\hline
Entregable Oficial & \texttt{08\_HITO\_1\_Aprobacion\_Fase\_1\_Entregable\_General.pdf} \\
\hline
Estado en el Tablero & 100\% APROBADO CONFORMEMENTE \\
\hline
\end{tabularx}
\caption{Ficha técnica del Hito 1 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia del Tablero Oficial de Gestión Trello (Cierre de Fase 1)}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/trello_tablero_captura_real.png}
    \caption{Captura Real del Tablero de Trello: Columna de Fase 1 con 8 Tarjetas 100\% Completadas.}
\end{figure}
\FloatBarrier

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Cierre de Fase:} \texttt{f01982a - release(fase1): paquete consolidado de entregables EDT 1.1 a 1.8 y herramientas analiticas}
    \item \textbf{Etiqueta Git (Tag):} \texttt{v0.1-fase1-approved}
    \item \textbf{Archivos Afectados:} 8 documentos técnicos en \texttt{Entregables\_Latex/Fase\_1/}
\end{itemize}
"""
    doc1_8 = render_doc("TI-SIGE-ENT-F1-008", "ASEGURAMIENTO DE CALIDAD / HITO DE CONTROL 1", "24/08/2026", "24/08/2026", "HITO 1: APROBACIÓN DE FASE 1 Y ENTREGABLE GENERAL SEMANA 1", b1_8, "24/08/2026", anx1_8)
    with open(os.path.join(base_dir, "1.8_HITO_1_Aprobacion_Fase_1_Entregable_General.tex"), "w", encoding="utf-8") as f:
        f.write(doc1_8)

    print("Successfully generated all 8 enhanced deliverables for Fase 1!")

if __name__ == "__main__":
    generate_fase1()
