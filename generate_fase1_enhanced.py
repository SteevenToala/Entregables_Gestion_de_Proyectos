# generate_fase1_enhanced.py
import os
from template_engine import render_doc

def generate_fase1():
    base_dir = os.path.join("Entregables_Latex", "Fase_1") if os.path.exists("Entregables_Latex") else "Fase_1"
    os.makedirs(base_dir, exist_ok=True)

    def write_tex(filename, content):
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

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
\textbf{Código} & \textbf{Problema Detectado} & \textbf{Evidencia Fáctica en FISEI} & \textbf{Impacto en Calidad SGC} \\
\hline
\textbf{P-01} & Dispersión de Versiones Word & Múltiples archivos \texttt{.docx} (\textit{v1, final, corregido}) en correos personales. & Pérdida de trazabilidad y aprobación de versiones obsoletas. \\
\hline
\textbf{P-02} & Inconsistencia de Carga Horaria & Planes entregados con sumatorias erróneas ($38\text{ h}$ o $44\text{ h}$ en lugar de $40\text{ h}$). & Incumplimiento del RRA-CES y reprocesos en Consejo Directivo. \\
\hline
\textbf{P-03} & Ponderación Asimétrica Matriz & Actividades de la Tabla 1 con sumatorias porcentuales distintas al $100\%$. & Distorsión en la evaluación docente semestral. \\
\hline
\textbf{P-04} & Pérdida de Medios Verificables & Enlaces rotos en Google Drive y carpetas locales no compartidas. & No conformidades graves en auditorías del CACES. \\
\hline
\textbf{P-05} & Dilación en la Cadena de Firmas & Trámite en papel con demoras de hasta 22 días laborables por coordinador. & Vencimiento de los plazos reglamentarios institucionales. \\
\hline
\textbf{P-06} & Inexistencia de Auditoría Central & Ausencia de bitácoras sobre quién modificó un texto u observación. & Vulnerabilidad en la custodia de expedientes oficiales. \\
\hline
\end{tabularx}
\caption{Matriz oficial de problemas detectados en el proceso manual As-Is.}
\label{tab:problemas_as_is}
\end{table}

\subsection{Línea Base Cuantitativa del Diagnóstico As-Is}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Indicador Operativo} & \textbf{Valor Medido As-Is} & \textbf{Meta con SIGE} & \textbf{Beneficio Institucional Esperado} \\
\hline
Tiempo promedio de tramitación & 18 a 22 días hábiles & $<3$ días hábiles & Reducción del $85\%$ en el ciclo de aprobación. \\
\hline
Tasa de reproceso por sumas erradas & $42\%$ de los expedientes & $0\%$ (Bloqueo automático) & Eliminación absoluta de errores aritméticos. \\
\hline
Extravío de evidencias documentales & $18\%$ de los casos auditados & $0\%$ (Custodia en objetos S3) & Respaldo auditable permanente y centralizado. \\
\hline
Uso de papel impreso por docente & $\sim 45$ hojas / semestre & $0$ hojas (Digital nativo) & Ahorro ecológico y económico institucional. \\
\hline
\end{tabularx}
\caption{Indicadores de la línea base operativa del proceso manual As-Is.}
\end{table}
"""

    anx1_1 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.1 en el Tablero Trello}
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
Entregable Oficial & \texttt{01\_Levantamiento\_Informacion\_Proceso\_Actual.pdf} (Mapeo As-Is) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.1 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia del Proceso Manual Diagnosticado (Plantillas SGC)}
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

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Identificación de Formatos & Mapeo de plantillas oficiales \texttt{P7-T1} y \texttt{P7-T2} de la UTA & 100\% CONFORME & Heidi Villavicencio \\
\hline
Muestra Representativa & Entrevistas a 8 docentes titulares y 2 coordinadores de FISEI & 100\% CONFORME & Nixon Hurtado \\
\hline
Matriz de Fallas P-01 a P-06 & Evidencia documental de problemas operativos As-Is & 100\% CONFORME & Steeven Toala \\
\hline
Aprobación del Diagnóstico & Revisión metodológica del alcance y problemas detectados & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.1.}
\end{table}
"""
    write_tex("1.1_Levantamiento_Informacion_Proceso_Actual.tex",
              render_doc("TI-SIGE-ENT-F1-001", "INGENIERÍA DE REQUERIMIENTOS / DIAGNÓSTICO AS-IS", "14/08/2026", "14/08/2026", "LEVANTAMIENTO DE INFORMACIÓN DEL PROCESO ACTUAL", b1_1, "14/08/2026", anx1_1))

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
    \item Mapeo de interesados en las cuatro carreras de la FISEI (Software, TI, Telecomunicaciones, Computación).
    \item Asignación de responsabilidades para el flujo documental de planificación semestral y rendición de cuentas.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Personal administrativo externo al Decanato y Subdecanato de la FISEI.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Stakeholder (Interesado):} Individuo o grupo que puede afectar, verse afectado o percibirse como afectado por una decisión, actividad o resultado del proyecto.
    \item \textbf{Matriz RACI:} Modelo de asignación de responsabilidades que clasifica la participación de los actores en: Responsable (\textit{R}), Aprobador (\textit{A}), Consultado (\textit{C}) e Informado (\textit{I}).
    \item \textbf{Comisión Académica:} Órgano colegiado de carrera encargado de auditar la pertinencia de las actividades y medios de verificación docentes.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 1.2):} Identificación de roles y caracterización de procesos.
    \item \textbf{Andrea Vásquez (Analista de Procesos):} Construcción de la matriz RACI y diagramas de interacción.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del mapa institucional de actores.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Estatuto Orgánico de la Universidad Técnica de Ambato:} Atribuciones de subdecanos, directores y coordinadores de carrera.
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Gestión de interesados y análisis de expectativas.
    \item \textbf{ISO 9001:2015, Cláusula 5.3 (Roles, responsabilidades y autoridades en la organización).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se aplicó el modelo de categorización de interesados del PMI, evaluando a los 5 roles clave según su nivel de autoridad formal e interés operativo en el sistema. Asimismo, se documentaron los macroprocesos de Gestión Curricular y Aseguramiento de la Calidad.

\subsection{Políticas de Gestión de Interesados}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Segregación de Funciones:} El docente elaborador no puede auto-aprobarse ni revisar su propio plan de trabajo.
    \item \textbf{Política de Jerarquía de Firma:} La firma del Subdecano solo puede registrarse tras el visado formal del Coordinador de Carrera.
    \item \textbf{Política de Notificación Inmediata:} Cualquier observación emitida por el comité debe notificarse automáticamente al docente.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_02_macroprocesos.png}
    \caption{Mapa de Macroprocesos del Sistema de Gestión de Calidad en la FISEI.}
    \label{fig:macroprocesos}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz RACI de la Cadena Documental Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|c|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Actividad del Proceso SGC} & \textbf{Docente} & \textbf{Coord. Área} & \textbf{Coord. Carrera} & \textbf{Subdecano} & \textbf{Admin SGC} \\
\hline
Creación y Llenado del Plan P7-T1 & \textbf{R / A} & C & I & I & I \\
\hline
Revisión Técnica y Observaciones & I & \textbf{R} & \textbf{R / A} & I & I \\
\hline
Subsanación de Observaciones & \textbf{R / A} & C & C & I & I \\
\hline
Aprobación y Firma de Comisión & I & C & \textbf{R / A} & I & I \\
\hline
Legalización en Consejo Directivo & I & I & I & \textbf{R / A} & I \\
\hline
Apertura de Prórrogas y Catálogos & I & I & C & C & \textbf{R / A} \\
\hline
\end{tabularx}
\caption{Matriz RACI oficial de la cadena de responsabilidades SGC.}
\label{tab:matriz_raci}
\end{table}
"""

    anx1_2 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.2 en el Tablero Trello}
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
Responsables Técnicos & Nixon Hurtado (NH), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{02\_Identificacion\_Actores\_Procesos.pdf} (Matriz de Stakeholders) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.2 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Poder versus Interés de Stakeholders}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Rol Institucional} & \textbf{Nivel Poder} & \textbf{Nivel Interés} & \textbf{Estrategia de Gestión PMI} \\
\hline
Subdecano de FISEI & Alto & Alto & Gestionar atentamente; clave para legalización. \\
\hline
Coordinador de Carrera & Alto & Alto & Gestionar activamente; líder de revisión. \\
\hline
Docente Elaborador & Medio & Alto & Mantener informado y satisfecho; usuario primario. \\
\hline
Administrador SGC & Alto & Medio & Mantener satisfecho; soporte técnico y parametrización. \\
\hline
\end{tabularx}
\caption{Clasificación estratégica de los interesados del proyecto.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Delimitación de Roles & Cobertura de los 5 roles institucionales de FISEI & 100\% CONFORME & Nixon Hurtado \\
\hline
Consistencia RACI & Verificación de un único aprobador principal por actividad & 100\% CONFORME & Andrea Vásquez \\
\hline
Marco de Acreditación & Conformidad con Estatuto UTA y normativa CACES & 100\% CONFORME & Heidi Villavicencio \\
\hline
Aprobación del Mapa & Validación formal de la cadena de interesados & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.2.}
\end{table}
"""
    write_tex("1.2_Identificacion_Actores_y_Procesos.tex",
              render_doc("TI-SIGE-ENT-F1-002", "INGENIERÍA DE REQUERIMIENTOS / STAKEHOLDERS Y PROCESOS", "18/08/2026", "18/08/2026", "IDENTIFICACIÓN DE ACTORES Y PROCESOS", b1_2, "18/08/2026", anx1_2))

    # =========================================================================
    # 1.3 DEFINICIÓN DE REQUISITOS FUNCIONALES Y NO FUNCIONALES (SRS)
    # =========================================================================
    b1_3 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Definición de Requisitos Funcionales y No Funcionales (SRS) -- Código EDT: 1.3

\section{Introducción}
La Especificación de Requisitos de Software (SRS) define con precisión las capacidades que el sistema SIGE debe proporcionar a la comunidad universitaria. Bajo el estándar internacional ISO/IEC/IEEE 29148:2018, este informe consolida el catálogo oficial de 24 Requisitos Funcionales (RF-01 a RF-24) y 8 Requisitos No Funcionales (RNF-01 a RNF-08). Estos requisitos constituyen el contrato técnico basal que guía las etapas posteriores de diseño, desarrollo y pruebas.

\section{Objetivo}
\subsection{Objetivo General}
Especificar de manera inequívoca, trazable y verificable los requisitos funcionales y no funcionales del sistema SIGE bajo estándares internacionales de ingeniería de requisitos.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Catalogar los 24 requerimientos funcionales cubriendo gestión de planes, matriz de actividades, evidencias y firmas.
    \item Definir los 8 requerimientos no funcionales de rendimiento, seguridad, usabilidad y mantenibilidad.
    \item Construir la matriz de trazabilidad bidireccional entre requisitos y objetivos del SGC.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Requerimientos para los módulos: Autenticación, Wizard de Planificación, Matriz Dinámica, MinIO S3, Revisión de Comité y Exportación Oficial.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Especificaciones de arquitectura de bajo nivel o código fuente (Fases 2 y 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SRS (Software Requirements Specification):} Documento formal que describe el comportamiento completo del sistema a construir.
    \item \textbf{Requisito Funcional (RF):} Declaración de un servicio o función que el sistema debe proveer.
    \item \textbf{Requisito No Funcional (RNF):} Restricción sobre los servicios o funciones ofrecidas (e.g., latencia, seguridad, disponibilidad).
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 1.3):} Redacción y formalización del SRS bajo norma IEEE 29148.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de viabilidad arquitectónica de los requisitos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la especificación oficial de requisitos.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149.}
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 32.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO/IEC/IEEE 29148:2018 (Systems and software engineering -- Requirements engineering).}
    \item \textbf{ISO/IEC 25010:2011 (Systems and software Quality Requirements and Evaluation).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuraron los requisitos utilizando plantillas estandarizadas con identificador único, nombre, descripción detallada, criterios de aceptación comprobables y prioridad según el método MoSCoW (\textit{Must have, Should have, Could have, Won't have}).

\subsection{Políticas de Calidad de Requisitos}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de No Ambigüedad:} Todo requisito debe ser verificable mediante una prueba objetiva binaria (Pasa / No Pasa).
    \item \textbf{Política de Trazabilidad Total:} Todo requisito funcional debe mapearse a al menos un objetivo de calidad del SGC.
    \item \textbf{Política de Congelamiento de Alcance:} Los requisitos aprobados en este documento quedan congelados como línea base del proyecto.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_03_modulos_rf.png}
    \caption{Mapa de Módulos Funcionales y Distribución de los 24 Requerimientos en SIGE.}
    \label{fig:modulos_rf}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Catálogo Oficial de Requisitos Funcionales Nucleares (RF-01 a RF-12)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Requisito} & \textbf{Descripción Funcional del Sistema} & \textbf{Módulo} & \textbf{Prioridad} \\
\hline
\textbf{RF-01} & Autenticación JWT & Acceso seguro con credenciales institucionales y generación de token. & Auth & Must \\
\hline
\textbf{RF-02} & Control RBAC & Restricción de permisos y vistas según los 5 roles institucionales. & Auth & Must \\
\hline
\textbf{RF-03} & Creación de Plan & Generación estructurada de planes semestrales asignados a periodos. & Planes & Must \\
\hline
\textbf{RF-04} & Carga Horaria 40h & Validación en tiempo real de que la jornada semanal sume exactamente 40h. & Wizard & Must \\
\hline
\textbf{RF-05} & Matriz Dinámica & Registro de actividades, cronograma semanal y ponderación exacta al 100\%. & Matriz & Must \\
\hline
\textbf{RF-06} & Autoguardado & Guardado automático de secciones enriquecidas con debounce de 800 ms. & Editor & Must \\
\hline
\textbf{RF-07} & Carga MinIO S3 & Almacenamiento seguro de evidencias PDF con cálculo de hash SHA-256. & Storage & Must \\
\hline
\textbf{RF-08} & URLs Prefirmadas & Visualización de archivos mediante enlaces temporales de 15 minutos. & Storage & Must \\
\hline
\textbf{RF-09} & Revisión Comité & Panel para coordinadores con observaciones granulares por sección. & Revisión & Must \\
\hline
\textbf{RF-10} & Cascada Firmas & Estampado digital secuencial e irreversible: Elaborador $\to$ Revisor $\to$ Aprobador. & Firmas & Must \\
\hline
\textbf{RF-11} & Exportación PDF & Generación de documentos oficiales A4 idénticos al SGC con código QR. & Export & Must \\
\hline
\textbf{RF-12} & Exportación DOCX & Descarga de planes en formato Word editable manteniendo estilos. & Export & Should \\
\hline
\end{tabularx}
\caption{Requisitos funcionales nucleares del sistema SIGE.}
\label{tab:rf_nucleares}
\end{table}
"""

    anx1_3 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.3 en el Tablero Trello}
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
Período de Ejecución & 14 de agosto al 18 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{03\_Definicion\_Requisitos\_Funcionales\_No\_Funcionales.pdf} (SRS) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.3 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Requisitos No Funcionales (ISO/IEC 25010)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Característica} & \textbf{Especificación Técnica Cuantitativa} & \textbf{Métrica} \\
\hline
RNF-01 & Rendimiento & Tiempo de respuesta de endpoints de consulta bajo carga normal. & $<300\text{ ms}$ (P95) \\
\hline
RNF-02 & Seguridad & Hashing de contraseñas con Argon2id y tokens JWT HMAC-SHA256. & Cero fallas OWASP \\
\hline
RNF-03 & Usabilidad & Conformidad con directrices de accesibilidad web W3C WCAG 2.1. & Nivel AA ($4.5:1$) \\
\hline
RNF-04 & Disponibilidad & Operación ininterrumpida de los contenedores en entorno local. & $99.5\%$ Uptime \\
\hline
\end{tabularx}
\caption{Requisitos no funcionales evaluados en el sistema.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Norma IEEE 29148 & Estructura formal con criterios de aceptación cuantificables & 100\% CONFORME & Heidi Villavicencio \\
\hline
Cobertura de Procesos & Cobertura total de los formatos SGC \texttt{P7-T1} y \texttt{P7-T2} & 100\% CONFORME & Nixon Hurtado \\
\hline
Priorización MoSCoW & Clasificación clara de prioridades pactada con usuarios & 100\% CONFORME & Steeven Toala \\
\hline
Aprobación del SRS & Validación y firma del documento de requisitos oficial & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.3.}
\end{table}
"""
    write_tex("1.3_Definicion_Requisitos_Funcionales_y_No_Funcionales.tex",
              render_doc("TI-SIGE-ENT-F1-003", "INGENIERÍA DE REQUERIMIENTOS / ESPECIFICACIÓN SRS", "18/08/2026", "18/08/2026", "DEFINICIÓN DE REQUISITOS (SRS)", b1_3, "18/08/2026", anx1_3))

    # =========================================================================
    # 1.4 DEFINICIÓN DEL ALCANCE, RESTRICCIONES Y OBJETIVOS SGC
    # =========================================================================
    b1_4 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Definición del Alcance, Restricciones y Objetivos SGC -- Código EDT: 1.4

\section{Introducción}
El control del alcance constituye uno de los factores más críticos para el éxito de proyectos de software en el ámbito universitario. Un alcance mal delimitado expone al equipo a corrupción del alcance (\textit{scope creep}), desviaciones presupuestarias y retrasos en la entrega de hitos. El presente entregable formaliza los límites exactos de inclusión y exclusión del proyecto SIGE, documenta las restricciones tecnológicas y normativas impuestas por la infraestructura de la FISEI, y alinea el software con los objetivos de calidad institucional.

\section{Objetivo}
\subsection{Objetivo General}
Delimitar formalmente el alcance operativo y técnico del sistema SIGE, estableciendo las restricciones de infraestructura y garantizando la alineación directa con los objetivos de calidad del SGC de la UTA.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Definir los entregables oficiales incluidos en el producto de software.
    \item Declarar explícitamente las exclusiones fuera del alcance para proteger el cronograma.
    \item Formalizar las restricciones de entorno (Docker local, Node.js, PostgreSQL 18, MinIO S3).
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Automatización integral de los formatos \texttt{P7-T1} y \texttt{P7-T2} en las carreras de la FISEI.
    \item Soporte para despliegue reproducible en contenedores locales mediante Docker Compose.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Procesamiento de pagos, honorarios docentes o nómina con el sistema financiero institucional.
    \item Trámites de matriculación estudiantil o registro de calificaciones de asignaturas.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Línea Base del Alcance (Scope Baseline):} Versión aprobada del enunciado del alcance, la EDT y su diccionario asociado.
    \item \textbf{Restricción de Proyecto:} Factor limitante que afecta la ejecución de un proyecto o proceso (e.g., tecnológica, temporal o presupuestaria).
    \item \textbf{Objetivo SGC:} Meta cuantificable establecida por la institución para asegurar la mejora continua y satisfacción de la comunidad académica.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 1.4):} Definición de límites técnicos y restricciones de arquitectura.
    \item \textbf{Heidi Villavicencio (Calidad):} Alineación con la política de calidad del SGC de la UTA.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la línea base del alcance.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122.}
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Gestión del Alcance del Proyecto.
    \item \textbf{ISO 9001:2015, Cláusula 4.3 (Determinación del alcance del sistema de gestión de la calidad).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se aplicó la técnica de descomposición analítica y consulta a expertos para fijar los límites del sistema. Se establecieron las tolerancias del proyecto y los criterios de aceptación contractuales pactados con la dirección académica.

\subsection{Políticas de Control de Alcance}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inmutabilidad de la Línea Base:} Toda solicitud de cambio que modifique las características aprobadas debe ingresar formalmente por el Comité de Control de Cambios.
    \item \textbf{Política de Prioridad al Core Académico:} Las funciones auxiliares no esenciales quedan supeditadas a la finalización y aprobación del núcleo transaccional.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_04_alcance.png}
    \caption{Diagrama de Fronteras del Sistema: Límites de Inclusión y Exclusión del Proyecto SIGE.}
    \label{fig:alcance_fronteras}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Alineación entre Objetivos del SGC y Módulos de SIGE}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|X|m{3.2cm}|c|}
\hline
\rowcolor{tableheader}
\textbf{Objetivo Institucional SGC} & \textbf{Meta Cuantitativa de Calidad} & \textbf{Módulo de Soporte en SIGE} & \textbf{Impacto} \\
\hline
O-01: Reducción de Tiempos & Disminuir el ciclo de trámite a menos de 3 días laborables. & Wizard + Cascada de Firmas & Alto \\
\hline
O-02: Integridad de Horas & Garantizar 100\% de planes con 40h exactas contractuales. & Validation Gate 1 & Crítico \\
\hline
O-03: Evidencias Centralizadas & Custodiar el 100\% de medios probatorios en formato digital. & Almacenamiento MinIO S3 & Crítico \\
\hline
O-04: Transparencia y Auditoría & Registrar 100\% de modificaciones y observaciones en bitácora. & Logs de Auditoría y Trazabilidad & Alto \\
\hline
\end{tabularx}
\caption{Matriz de alineación estratégica entre el SGC y el sistema SIGE.}
\label{tab:sgc_alignment}
\end{table}
"""

    anx1_4 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.4 en el Tablero Trello}
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
Período de Ejecución & 15 de agosto al 18 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & \texttt{04\_Definicion\_Alcance\_Restricciones\_Objetivos.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.4 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Restricciones del Proyecto SIGE}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Tipo} & \textbf{Restricción} & \textbf{Detalle de la Limitante Técnica} & \textbf{Impacto} \\
\hline
Tecnológica & Entorno Docker & Despliegue obligatorio mediante contenedores orquestados localmente. & Alto \\
\hline
Normativa & Formatos Oficiales & Los reportes PDF deben coincidir con \texttt{P7-T1} y \texttt{P7-T2} de la UTA. & Crítico \\
\hline
Temporal & Fechas Semestrales & El sistema debe estar probado antes del inicio del ciclo 2026-B. & Crítico \\
\hline
Recursos & Equipo de Trabajo & 4 ingenieros de desarrollo con asignación de 832 horas hombre totales. & Medio \\
\hline
\end{tabularx}
\caption{Restricciones técnicas y normativas del proyecto.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Definición de Límites & Declaración unívoca de inclusiones y exclusiones del sistema & 100\% CONFORME & Steeven Toala \\
\hline
Alineación SGC & Correspondencia con metas institucionales de la UTA & 100\% CONFORME & Heidi Villavicencio \\
\hline
Factibilidad Operativa & Validación de restricciones tecnológicas del entorno Docker & 100\% CONFORME & Nixon Hurtado \\
\hline
Aprobación del Alcance & Conformidad del docente evaluador con la línea base pactada & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.4.}
\end{table}
"""
    write_tex("1.4_Definicion_Alcance_Restricciones_y_Objetivos_SGC.tex",
              render_doc("TI-SIGE-ENT-F1-004", "INGENIERÍA DE REQUERIMIENTOS / LÍNEA BASE DEL ALCANCE", "18/08/2026", "18/08/2026", "DEFINICIÓN DEL ALCANCE Y RESTRICCIONES", b1_4, "18/08/2026", anx1_4))

    # =========================================================================
    # 1.5 REGLAS DE NEGOCIO Y VALIDATION GATES LÓGICAS
    # =========================================================================
    b1_5 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Reglas de Negocio y Validation Gates Lógicas -- Código EDT: 1.5

\section{Introducción}
Los procesos del Sistema de Gestión de Calidad se rigen por principios ineludibles de integridad académica. Tradicionalmente, la verificación del cumplimiento de estas normas recaía sobre el coordinador de carrera de manera puramente visual, lo que conllevaba errores humanos, omisiones involuntarias y aprobación de planes con sumas distorsionadas. El presente entregable formaliza el catálogo de las 6 Reglas de Negocio institucionales (RN-01 a RN-06) y modela el concepto lógico de las \textit{Validation Gates}: compuertas lógicas automatizadas que operan como barreras ineludibles en el software para impedir transiciones de estado indebidas.

\section{Objetivo}
\subsection{Objetivo General}
Formalizar y modelar las reglas de negocio institucionales y compuertas lógicas (\textit{Validation Gates}) que gobernarán el procesamiento, validación y aprobación de planes e informes en SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Definir formalmente las 6 reglas de negocio nucleares del SGC institucional.
    \item Diseñar el pipeline lógico de Validation Gates que se implementará en el backend.
    \item Establecer los criterios de bloqueo y códigos de excepción aplicables.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Reglas para: Carga horaria ($40\text{ h}$), Ponderación ($100\%$), Evidencias obligatorias, Fechas vigentes, Cascada de firmas y Resolución de observaciones.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Codificación de los middlewares en Node.js (correspondiente a Fase 3, EDT 3.10).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Regla de Negocio (Business Rule):} Directriz u obligación institucional que define o restringe aspectos de la operación académica.
    \item \textbf{Validation Gate:} Barrera lógica que evalúa precondiciones obligatorias antes de autorizar un cambio de estado en el ciclo documental.
    \item \textbf{Bloqueo Preventivo:} Rechazo inmediato de una acción no conforme antes de registrar datos erróneos en el sistema.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 1.5):} Mapeo de reglas institucionales y definición lógica de las compuertas.
    \item \textbf{Steeven Toala (Arquitecto de Negocio):} Diseño del árbol de decisión y pipeline lógico.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del rigor de las reglas institucionales.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149.}
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Semantics of Business Vocabulary and Business Rules (SBVR - OMG).}
    \item \textbf{ISO 9001:2015, Cláusula 8.5.1 (Condiciones controladas).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuraron las reglas de negocio bajo el formato estándar: Condición Lógica $\to$ Acción Requerida $\to$ Efecto en caso de Incumplimiento. Cada regla se vinculó con su correspondiente artículo normativo institucional.

\subsection{Políticas de Calidad de Reglas de Negocio}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inviolabilidad Normativa:} Ninguna regla de negocio puede ser desactivada mediante configuraciones de usuario en tiempo de ejecución.
    \item \textbf{Política de Retroalimentación Explícita:} Toda compuerta que bloquee un avance debe emitir un mensaje de diagnóstico que indique exactamente el valor actual, el esperado y la acción correctiva.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_05_validation_gates.png}
    \caption{Árbol Lógico de Decisión y Secuencia de Validation Gates en el Sistema SIGE.}
    \label{fig:gates_logica}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Catálogo Oficial de Reglas de Negocio del Sistema (RN-01 a RN-06)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Nombre de Regla} & \textbf{Expresión de la Regla Institucional} & \textbf{Efecto de Incumplimiento} & \textbf{Gate} \\
\hline
\textbf{RN-01} & Carga Horaria 40h & Las horas de docencia, investigación y gestión deben sumar exactamente 40h. & Bloqueo de paso a revisión; marca error en horas. & Gate 1 \\
\hline
\textbf{RN-02} & Ponderación 100\% & La suma porcentual de actividades de la matriz debe totalizar exactamente 100.00\%. & Bloqueo de guardado final; alerta roja de diferencia. & Gate 2 \\
\hline
\textbf{RN-03} & Evidencias Obligatorias & Toda actividad ejecutada con avance $>0\%$ debe adjuntar al menos un archivo en MinIO. & Bloqueo de reporte de informe; exige subir respaldo. & Gate 3 \\
\hline
\textbf{RN-04} & Plazos Vigentes & Los documentos solo pueden entregarse dentro del periodo lectivo oficial. & Bloqueo por extemporaneidad; exige prórroga admin. & Gate 4 \\
\hline
\textbf{RN-05} & Cascada de Firmas & Una firma jerárquica exige que el nivel previo haya firmado válidamente. & Bloqueo de firma; previene saltos en la cadena. & Gate 5 \\
\hline
\textbf{RN-06} & Resolución Total & No se puede aprobar un plan con observaciones pendientes sin subsanar. & Bloqueo de aprobación de comité; exige resolver observaciones. & Gate 6 \\
\hline
\end{tabularx}
\caption{Matriz oficial de Reglas de Negocio y correspondencia con Validation Gates.}
\label{tab:reglas_negocio_matrix}
\end{table}
"""

    anx1_5 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.5 en el Tablero Trello}
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
Período de Ejecución & 17 de agosto al 18 de agosto de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{05\_Reglas\_Negocio\_Validation\_Gates.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.5 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Decisiones Lógicas y Códigos de Diagnóstico}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Compuerta} & \textbf{Condición Booleana} & \textbf{Diagnóstico Emitido al Usuario} & \textbf{Código HTTP} \\
\hline
Gate 1 & $\sum \text{horas} == 40$ & \textit{``La dedicación semanal debe totalizar 40 horas contractuales''} & 422 Unprocessable \\
\hline
Gate 2 & $\sum \text{pond} == 100.00$ & \textit{``La ponderación de la matriz debe sumar exactamente 100\%''} & 422 Unprocessable \\
\hline
Gate 3 & $\text{archivos} \ge 1$ si $A_i > 0$ & \textit{``Debe adjuntar al menos un medio de verificación auditable''} & 422 Unprocessable \\
\hline
Gate 5 & $\text{orden} == \text{orden\_prev} + 1$ & \textit{``La firma digital requiere la validación del firmante anterior''} & 409 Conflict \\
\hline
\end{tabularx}
\caption{Especificación técnica de diagnósticos de las Validation Gates.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Completitud de Reglas & Cobertura de las 6 reglas nucleares del SGC institucional & 100\% CONFORME & Nixon Hurtado \\
\hline
Lógica No Evadible & Diseño de compuertas lógicas con bloqueo preventivo & 100\% CONFORME & Steeven Toala \\
\hline
Alineación RRA-CES & Verificación de correspondencia con normativas de carga horaria & 100\% CONFORME & Heidi Villavicencio \\
\hline
Aprobación Metodológica & Conformidad del docente evaluador con el diseño de las compuertas & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.5.}
\end{table}
"""
    write_tex("1.5_Reglas_de_Negocio_y_Validation_Gates_Logicas.tex",
              render_doc("TI-SIGE-ENT-F1-005", "INGENIERÍA DE REQUERIMIENTOS / REGLAS DE NEGOCIO", "18/08/2026", "18/08/2026", "REGLAS DE NEGOCIO Y VALIDATION GATES", b1_5, "18/08/2026", anx1_5))

    # =========================================================================
    # 1.6 ELABORACIÓN DE CASO DE NEGOCIO, ROI Y PROJECT CHARTER
    # =========================================================================
    b1_6 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Elaboración de Caso de Negocio, ROI y Project Charter -- Código EDT: 1.6

\section{Introducción}
Todo proyecto de desarrollo de software institucional debe fundamentarse en un sólido análisis de viabilidad financiera, operativa y estratégica. El desarrollo del sistema web SIGE no solo resuelve deficiencias de gestión documental en la FISEI, sino que genera retornos tangibles en optimización de horas-hombre docentes, erradicación del gasto en papelería e impresiones, y mitigación de riesgos de auditoría ante el CACES. El presente informe formaliza el Caso de Negocio (\textit{Business Case}), el cálculo del Retorno de la Inversión (ROI) y el Acta de Constitución del Proyecto (\textit{Project Charter}) oficial.

\section{Objetivo}
\subsection{Objetivo General}
Estructurar el Caso de Negocio, cuantificar el Retorno de la Inversión (ROI) y formalizar el Project Charter que autoriza formalmente el inicio y asignación de recursos para el proyecto SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Evaluar los costos del proceso manual As-Is frente a los costos de inversión del desarrollo.
    \item Calcular el ROI y el período de recuperación de la inversión (\textit{Payback Period}).
    \item Emitir el Project Charter formal con objetivos, hitos, presupuesto y gobernanza.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Análisis económico proyectado a un horizonte de 3 años lectivos (6 ciclos semestrales).
    \item Asignación de gobernanza entre el equipo de desarrollo, analista de calidad y docente evaluador.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Presupuestos de adquisición de hardware para data centers institucionales de la universidad.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Project Charter (Acta de Constitución):} Documento emitido por el patrocinador que autoriza formalmente la existencia del proyecto y otorga autoridad al director.
    \item \textbf{ROI (Return on Investment):} Razón financiera que compara el beneficio neto obtenido respecto a los costos de inversión inicial.
    \item \textbf{Payback Period:} Tiempo requerido para que los ahorros acumulados igualen el costo total de la inversión en el software.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder de Proyecto):} Redacción del Project Charter y análisis económico de costos.
    \item \textbf{Heidi Villavicencio (Analista Financiero/Calidad):} Cuantificación de ahorros operativos y cálculo del ROI.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador / Patrocinador):} Aprobación del Project Charter institucional.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Uso eficiente y transparente de los recursos institucionales.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Iniciación del proyecto y desarrollo del Acta de Constitución.
    \item \textbf{ISO 9001:2015, Cláusula 6.2 (Objetivos de la calidad y planificación para lograrlos).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se utilizó el análisis de flujo de caja descontado proyectado a 3 años, considerando el ahorro en horas de reprocesos de 120 docentes de la FISEI valoradas a un costo promedio hora de \$12.50 USD, sumado al ahorro en papel y tóners. La fórmula de cálculo del ROI aplicada es:
\begin{equation}
    \text{ROI} = \frac{\text{Ahorros Netos Acumulados} - \text{Costo de Inversión}}{\text{Costo de Inversión}} \times 100\%
\end{equation}

\subsection{Políticas de Viabilidad Económica}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inversión Eficiente:} El proyecto debe autofinanciarse mediante ahorros operativos en un plazo menor a 1.5 años.
    \item \textbf{Política de Sostenibilidad Ecológica:} Compromiso de reducción del 100\% en el uso de papel físico para la gestión de planes.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s1_06_beneficios_pie.png}
    \caption{Distribución Porcentual de Ahorros Operativos Proyectados con la Implementación de SIGE.}
    \label{fig:beneficios_pie}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Cuantificación Financiera del Proyecto y Retorno de la Inversión (ROI)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{4.0cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Rubro Financiero} & \textbf{Proceso Manual (Anual)} & \textbf{Con SIGE (Anual)} & \textbf{Ahorro Neto Anual} \\
\hline
Horas-hombre en revisión manual & \$18,000 USD & \$2,400 USD & +\$15,600 USD (Ahorro en tiempo) \\
\hline
Papelería, impresiones y archivo & \$2,800 USD & \$200 USD & +\$2,600 USD (Cero papel) \\
\hline
Costos por reprocesos y extravíos & \$4,500 USD & \$0 USD & +\$4,500 USD (Eliminación de fallas) \\
\hline
\textbf{TOTAL COSTO ANUAL:} & \textbf{\$25,300 USD} & \textbf{\$2,600 USD} & \textbf{+\$22,700 USD / año} \\
\hline
\end{tabularx}
\caption{Comparativa económica anual entre el proceso manual As-Is y el sistema SIGE.}
\label{tab:comparativa_financiera}
\end{table}

\subsection{Indicadores Clave de Viabilidad Financiera}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Costo Total de Desarrollo (832 h netas equipo):} \$10,400 USD estimado.
    \item \textbf{Retorno de la Inversión (ROI a 3 años):} \textbf{+554.8\%}.
    \item \textbf{Período de Recuperación (Payback Period):} \textbf{5.5 meses} desde el despliegue.
\end{itemize}
"""

    anx1_6 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.6 en el Tablero Trello}
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
Período de Ejecución & 17 de agosto al 18 de agosto de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & \texttt{06\_Caso\_de\_Negocio.md} \& Project Charter Oficial \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.6 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Ficha Resumen del Project Charter Oficial de SIGE}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA DE CONSTITUCIÓN DEL PROYECTO (PROJECT CHARTER) -- SIGE}} \\
\hline
\textbf{Título del Proyecto:} & Sistema Integrado de Gestión y Evaluación Académica (SIGE) -- FISEI \\
\hline
\textbf{Patrocinador / Evaluador:} & Ing. Paulo Torres, Mg. (Docente de Gestión de Proyectos) \\
\hline
\textbf{Líder de Proyecto:} & Steeven Toala (Estudiante de Ingeniería de Software) \\
\hline
\textbf{Propósito Central:} & Automatizar el flujo de planes e informes institucionales del SGC de la FISEI. \\
\hline
\textbf{Presupuesto de Esfuerzo:} & 832 horas hombre distribuidas en 4 Fases de trabajo estructurado. \\
\hline
\end{tabularx}
\caption{Resumen del Acta de Constitución del Proyecto SIGE.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Viabilidad Financiera & Cuantificación precisa de costos y ahorro neto proyectado & 100\% CONFORME & Heidi Villavicencio \\
\hline
Cálculo de ROI y Payback & Métodos estándar de análisis financiero (Payback $<6$ meses) & 100\% CONFORME & Steeven Toala \\
\hline
Gobernanza Formal & Asignación inequívoca de roles en el Project Charter & 100\% CONFORME & Nixon Hurtado \\
\hline
Aprobación del Charter & Firma y autorización formal del docente evaluador & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.6.}
\end{table}
"""
    write_tex("1.6_Elaboracion_Caso_de_Negocio_ROI_Project_Charter.tex",
              render_doc("TI-SIGE-ENT-F1-006", "GESTIÓN DE PROYECTOS / CASO DE NEGOCIO Y CHARTER", "18/08/2026", "18/08/2026", "CASO DE NEGOCIO, ROI Y CHARTER", b1_6, "18/08/2026", anx1_6))

    # =========================================================================
    # 1.7 PLANIFICACIÓN DEL PROYECTO Y CRONOGRAMA DE TRABAJO
    # =========================================================================
    b1_7 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Planificación del Proyecto y Cronograma de Trabajo -- Código EDT: 1.7

\section{Introducción}
La planificación temporal estructurada y la descomposición del trabajo constituyen el eje sobre el cual se coordina el esfuerzo de desarrollo en el proyecto SIGE. Para garantizar la entrega a tiempo antes del inicio del ciclo académico semestral, se elaboró la Estructura de Desglose del Trabajo (EDT / WBS) dividida en 4 Fases y 34 tareas no resumen, articulada con un cronograma formal en Microsoft Project y el Tablero Kanban oficial en Trello. El presente informe formaliza la línea base del cronograma y la ruta crítica del proyecto.

\section{Objetivo}
\subsection{Objetivo General}
Planificar, programar y estructurar el cronograma de trabajo y la Estructura de Desglose del Trabajo (EDT) del proyecto SIGE, estableciendo la secuencia lógica de ejecución de las 34 tareas del tablero oficial.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Construir la EDT jerárquica de 4 niveles para las 4 fases del proyecto.
    \item Determinar la ruta crítica y holguras del cronograma en Microsoft Project.
    \item Configurar el tablero Kanban interactivo en Trello sincronizado con el cronograma.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Programación temporal desde el 12 de agosto hasta el 13 de octubre de 2026.
    \item Asignación de 832 horas-hombre netas entre los 4 integrantes del equipo.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Planificación de fases de mantenimiento correctivo a desarrollarse en el año 2027.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{EDT / WBS (Work Breakdown Structure):} Descomposición jerárquica orientada al producto entregable del trabajo que será ejecutado por el equipo.
    \item \textbf{Ruta Crítica (CPM):} Secuencia de actividades dependientes que determina la duración más corta posible del proyecto.
    \item \textbf{Hito (Milestone):} Punto o evento significativo dentro del cronograma sin duración asociada.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 1.7):} Elaboración de la EDT, cronograma Gantt y análisis de ruta crítica.
    \item \textbf{Nixon Hurtado (Especialista en Planificación):} Estimación de horas y dependencias lógicas.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la línea base del cronograma.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Calendario Académico Oficial de la Universidad Técnica de Ambato.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Gestión del Cronograma y Estructura de Desglose del Trabajo.
    \item \textbf{Practice Standard for Work Breakdown Structures (PMI).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se utilizó el método del diagrama de precedencias (PDM) en Microsoft Project. El proyecto se organizó en 4 fases secuenciales: Fase 1 (Análisis y Planificación, 8 tareas), Fase 2 (Diseño y Arquitectura, 7 tareas), Fase 3 (Implementación y Desarrollo, 16 tareas) y Fase 4 (Pruebas, Capacitación y Cierre, 3 tareas).

\subsection{Políticas de Gestión del Cronograma}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Cero Holgura en Hitos Críticos:} Los hitos de aprobación no admiten prórrogas que comprometan el inicio de las fases subsiguientes.
    \item \textbf{Política de Registro Diario en Tablero:} Cada tarea en Trello debe reflejar fielmente su avance porcentual y estado operativo.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_gantt_cronograma.png}
    \caption{Cronograma Gantt Oficial de la Planificación del Proyecto SIGE en MS Project.}
    \label{fig:gantt_cronograma}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Resumen de la Línea Base del Cronograma por Fases de la EDT}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.5cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial} & \textbf{Fechas de Ejecución} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Hito Asociado} \\
\hline
\textbf{Fase 1} & Análisis y Planificación & 12 ago -- 18 ago 2026 & 8 & 192 h & Hito 1 (Aprobación F1) \\
\hline
\textbf{Fase 2} & Diseño y Arquitectura & 19 ago -- 31 ago 2026 & 7 & 192 h & Hito 2 (Aprobación Arq.) \\
\hline
\textbf{Fase 3} & Implementación y Desarrollo & 01 sep -- 12 oct 2026 & 16 & 400 h & Hitos 3, 4 y 5 (Core) \\
\hline
\textbf{Fase 4} & Pruebas y Cierre Formal & 12 oct -- 13 oct 2026 & 3 & 48 h & Cierre Final SIGE \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL CONSOLIDADO DEL PROYECTO:}} & \textbf{34} & \textbf{832 h} & \textbf{4 Hitos de Control} \\
\hline
\end{tabularx}
\caption{Línea base del cronograma y esfuerzo planificado del proyecto SIGE.}
\label{tab:cronograma_resumen}
\end{table}
"""

    anx1_7 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.7 en el Tablero Trello}
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
Período de Ejecución & 17 de agosto al 18 de agosto de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & \texttt{07\_Planificacion\_Proyecto\_Cronograma\_EDT.md} \& Cronograma MS Project \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.7 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de la Ruta Crítica en MS Project}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Tarea en Ruta Crítica} & \textbf{Duración} & \textbf{Holgura Total} & \textbf{Impacto en Hito} \\
\hline
EDT 1.3 & Definición de Requisitos SRS & 4 días & 0 días & Crítico para inicio de F2 \\
\hline
EDT 2.2 & Arquitectura SAD y C4 & 4 días & 0 días & Crítico para inicio de F3 \\
\hline
EDT 2.4 & Base de Datos Relacional 3NF & 4 días & 0 días & Crítico para scripts DDL \\
\hline
EDT 3.9 & Matriz Dinámica de Actividades & 4 días & 0 días & Crítico para Hito 4 \\
\hline
\end{tabularx}
\caption{Ruta crítica identificada en la planificación temporal.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Consistencia EDT & Correspondencia exacta de las 34 tareas con el Tablero Trello & 100\% CONFORME & Steeven Toala \\
\hline
Presupuesto Horas & Balance exacto de 832 horas asignadas entre los 4 integrantes & 100\% CONFORME & Nixon Hurtado \\
\hline
Ruta Crítica Calculada & Secuencia PDM validada sin lazos cíclicos en MS Project & 100\% CONFORME & Heidi Villavicencio \\
\hline
Aprobación del Cronograma & Validación formal de la línea base por el docente evaluador & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.7.}
\end{table}
"""
    write_tex("1.7_Planificacion_del_Proyecto_y_Cronograma_de_Trabajo.tex",
              render_doc("TI-SIGE-ENT-F1-007", "GESTIÓN DE PROYECTOS / CRONOGRAMA Y EDT", "18/08/2026", "18/08/2026", "PLANIFICACIÓN Y CRONOGRAMA DE TRABAJO", b1_7, "18/08/2026", anx1_7))

    # =========================================================================
    # 1.8 HITO 1: APROBACIÓN DE FASE 1 Y ENTREGABLE GENERAL SEMANA 1 (COHERENTE)
    # =========================================================================
    b1_8 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 1: Aprobación de Fase 1 y Entregable General Semana 1 -- Código EDT: 1.8

\section{Introducción}
El cierre exitoso de la Fase 1 (Análisis y Planificación) marca el congelamiento formal de la Línea Base de Requisitos, Alcance y Cronograma del proyecto SIGE. La reunión de revisión de Hito 1 (\textit{Stage-Gate Review 1}), celebrada el 18 de agosto de 2026, constituye el punto de control de calidad institucional donde el equipo de proyecto y el docente evaluador auditan la completitud y rigor metodológico de los 7 entregables técnicos previos (EDT 1.1 a 1.7). El presente informe consolida la evaluación de la fase de análisis, certificando que el diagnóstico As-Is, el catálogo de 24 requisitos funcionales y el cronograma cumplen con todos los estándares del SGC antes de autorizar el inicio de la Fase 2 de Diseño y Arquitectura.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, auditar y legalizar la aprobación formal de la Fase 1 de Análisis y Planificación del proyecto SIGE correspondiente al Hito 1 de la EDT, autorizando el inicio de la fase de diseño arquitectónico.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditar el cumplimiento del 100\% de las 8 tareas técnicas asignadas a la Fase 1 en el Tablero Trello.
    \item Presentar los diagramas analíticos de soporte: Diagrama de Causa-Efecto (Ishikawa) del diagnóstico As-Is y el Run Chart de latencia histórica del trámite manual anterior.
    \item Formalizar el Acta Oficial de Aprobación de Fase 1 y la Línea Base del Cronograma para las fases subsiguientes.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditoría técnica y aprobación de los entregables EDT 1.1 al 1.7.
    \item Consolidación de las 192 horas-hombre netas programadas y ejecutadas en la Fase 1.
    \item Firma y emisión del paquete general de aprobación de la Semana 1.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modelado arquitectónico C4 o diagramas UML (objeto de la Fase 2).
    \item Implementación de código de software (objeto de la Fase 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito de Control (Stage-Gate):} Punto formal de decisión donde se verifica que todos los criterios de aceptación de una fase están cumplidos para autorizar el avance a la siguiente fase.
    \item \textbf{Línea Base de Requisitos:} Conjunto formalmente aprobado de requerimientos funcionales y no funcionales que sirve de base inmutable para el diseño.
    \item \textbf{Diagnóstico As-Is:} Análisis del estado actual del proceso manual en Word y Excel previo a la intervención del sistema web SIGE.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder de Proyecto):} Sustentación técnica del paquete de entregables de Fase 1.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Verificación de criterios de aceptación de los requisitos SRS.
    \item \textbf{Nixon Hurtado / Andrea Vásquez (Equipo de Análisis):} Presentación del diagnóstico de problemas y matriz RACI.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Evaluación y aprobación formal del Hito 1.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Obligatoriedad de rendición de cuentas y calidad en la planificación docente.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Control de puertas de decisión (\textit{Stage-Gate Reviews}) y gestión del alcance.
    \item \textbf{ISO 9001:2015, Cláusula 8.2 (Requisitos para los productos y servicios) y Cláusula 8.3 (Diseño y desarrollo).}
    \item \textbf{ISO/IEC/IEEE 29148:2018:} Procesos de validación y congelamiento de especificaciones de requisitos.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Para la aprobación del Hito 1 se ejecutó una sesión formal de revisión colegiada. Se contrastaron los problemas detectados en el levantamiento As-Is frente a los 24 Requisitos Funcionales del SRS, comprobando que cada cuello de botella cuente con una solución técnica planificada. Se analizaron las causas fundamentales mediante el Diagrama de Ishikawa y se examinó la latencia histórica del trámite manual anterior mediante un Diagrama de Comportamiento (Run Chart).

\subsection{Políticas de Calidad de Cierre de Hito 1}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Aprobación Plena de Fase 1:} Las 8 tareas de la Fase 1 deben encontrarse al 100\% completadas en el Tablero Trello para formalizar el cierre de hito.
    \item \textbf{Política de Congelamiento de Requisitos:} Una vez firmado el Hito 1, los 24 requisitos funcionales no pueden modificarse sin una solicitud formal de control de cambios.
    \item \textbf{Política de Coherencia Cronológica:} El equipo certifica que a la fecha de este hito (18 de agosto de 2026) se han completado 192 horas de análisis y que las fases de diseño y construcción están programadas a futuro.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_tablero_captura_real.png}
    \caption{Captura Real del Tablero Trello con el 100\% de Tareas de Fase 1 Completadas al Hito 1.}
    \label{fig:trello_fase1}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Herramienta Analítica 1: Diagrama de Causa y Efecto de Ishikawa (Diagnóstico As-Is)}
Para identificar las causas raíces de las demoras y extravíos en el proceso manual anterior de la FISEI, se estructuró el Diagrama de Ishikawa en 4 categorías: Método, Personal, Materiales y Medición:

\begin{figure}[H]
    \centering
    \begin{tikzpicture}[
        scale=0.92, every node/.style={transform shape},
        spine/.style={line width=2.2pt, color=navyheader, -{Stealth[length=3.5mm, width=2.5mm]}},
        bone/.style={line width=1.3pt, color=lineblue, -{Stealth[length=2.5mm, width=1.8mm]}},
        subbone/.style={line width=0.8pt, color=darkblue, dashed, -{Stealth[length=2.0mm, width=1.4mm]}}
    ]
        % Columna vertebral
        \draw[spine] (-0.5, 0) -- (10.5, 0);

        % Caja de efecto
        \node[efectobox, anchor=west] at (10.5, 0) {%
            \textbf{DEMORAS Y PÉRDIDA}\\[2pt]
            \textbf{DE EXPEDIENTES EN}\\[2pt]
            \textbf{EL PROCESO MANUAL SGC}
        };

        % Categorías Superiores
        \node[catbox] (metodo) at (2.2, 3.4) {MÉTODO};
        \draw[bone] (metodo.south) -- (3.5, 0);
        \node[causetext, anchor=south east] at (3.2, 1.8) {Flujo no estandarizado};
        \node[causetext, anchor=south east] at (2.8, 1.0) {Formatos Word desincronizados};

        \node[catbox] (personal) at (6.8, 3.4) {PERSONAL};
        \draw[bone] (personal.south) -- (8.1, 0);
        \node[causetext, anchor=south east] at (7.8, 1.8) {Falta de capacitación SGC};
        \node[causetext, anchor=south east] at (7.4, 1.0) {Carga horaria calculada a mano};

        % Categorías Inferiores
        \node[catbox] (materiales) at (2.2, -3.4) {MATERIALES};
        \draw[bone] (materiales.north) -- (3.5, 0);
        \node[causetext, anchor=north east] at (3.2, -1.8) {Múltiples versiones locales};
        \node[causetext, anchor=north east] at (2.8, -1.0) {Uso excesivo de papel impreso};

        \node[catbox] (medicion) at (6.8, -3.4) {MEDICIÓN};
        \draw[bone] (medicion.north) -- (8.1, 0);
        \node[causetext, anchor=north east] at (7.8, -1.8) {Cero bitácoras de auditoría};
        \node[causetext, anchor=north east] at (7.4, -1.0) {Sumatorias de horas erradas};
    \end{tikzpicture}
    \caption{Diagrama de Causa y Efecto de Ishikawa Vectorial: Diagnóstico As-Is del Proceso Manual.}
    \label{fig:ishikawa_vector}
\end{figure}
\FloatBarrier

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Categoría} & \textbf{Causa Raíz Diagnosticada} & \textbf{Problema} & \textbf{Respuesta del Sistema SIGE} \\
\hline
\textbf{Método} & Descentralización en la recolección de firmas y revisiones en comités. & P-01, P-05 & Wizard guiado en 5 pasos y cascada secuencial de firmas. \\
\hline
\textbf{Personal} & Errores humanos de tipeo y cálculo manual de horas y ponderaciones. & P-02, P-03 & Validación automática de 40h y cálculo reactivo al 100\%. \\
\hline
\textbf{Materiales} & Uso de formatos Word dispersos y almacenamiento en carpetas locales. & P-01, P-04 & Base de datos relacional y repositorio MinIO S3 centralizado. \\
\hline
\textbf{Medición} & Falta de trazabilidad y ausencia de bitácoras sobre cambios en planes. & P-02, P-06 & Registro de auditoría inmutable y drawer de observaciones. \\
\hline
\end{tabularx}
\caption{Matriz de causas raíces del diagrama de Ishikawa y solución funcional en SIGE.}
\label{tab:causas_ishikawa}
\end{table}

\subsection{Herramienta Analítica 2: Diagrama de Comportamiento Histórico (Run Chart As-Is)}
Para justificar empíricamente el proyecto SIGE ante el Comité de Calidad, se analizó la demora en días hábiles de la aprobación manual de planes de trabajo durante los últimos 10 ciclos semestrales en la FISEI (2021 a 2025). El gráfico demuestra que el proceso manual tomaba entre 12 y 22 días hábiles (promedio de 16.5 días), excediendo sistemáticamente el límite institucional aceptable:

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \node[fill=navyheader, text=white, font=\bfseries\normalsize, rounded corners=6pt, inner sep=4pt, minimum width=6cm, align=center] at (4.8, 6.4) {Diagrama de Comportamiento Histórico};
        \node[font=\bfseries\small, text=black, align=center] at (4.8, 5.85) {Demora del Proceso Manual As-Is en la FISEI};
        \node[font=\scriptsize, text=gray!80!black, align=center] at (4.8, 5.48) {(Días hábiles de tramitación por ciclo semestral previo a SIGE)};

        \begin{axis}[
            at={(0,0)},
            width=9.6cm,
            height=4.8cm,
            clip=false,
            axis lines=left,
            x axis line style={-{Stealth[length=2.5mm, width=1.6mm]}, line width=1.1pt, color=navyheader!80!black},
            y axis line style={-{Stealth[length=2.5mm, width=1.6mm]}, line width=1.1pt, color=navyheader!80!black},
            xlabel={\textbf{Ciclos Semestrales Anteriores (Histórico FISEI)}},
            ylabel={\textbf{Días Hábiles de Trámite}},
            xlabel style={font=\footnotesize, at={(axis description cs:0.5,-0.12)}, anchor=north},
            ylabel style={font=\footnotesize, at={(axis description cs:-0.09,0.5)}, anchor=south},
            xmin=0.7, xmax=10.5,
            xtick={1,2,3,4,5,6,7,8,9,10},
            xticklabels={21-A, 21-B, 22-A, 22-B, 23-A, 23-B, 24-A, 24-B, 25-A, 25-B},
            x tick label style={font=\scriptsize\bfseries, text=black!85},
            ymin=0, ymax=26,
            ytick={0,5,10,15,20,25},
            yticklabels={0, 5, 10, 15, 20, 25 d},
            y tick label style={font=\scriptsize},
            ymajorgrids=true,
            xmajorgrids=true,
            grid style={dotted, gray!40}
        ]
            % Área sombreada bajo la curva
            \fill[areablue, opacity=0.75] 
                (axis cs:1,0) -- (axis cs:1,18) -- (axis cs:2,16) -- (axis cs:3,21) -- 
                (axis cs:4,19) -- (axis cs:5,15) -- (axis cs:6,22) -- (axis cs:7,17) -- 
                (axis cs:8,14) -- (axis cs:9,16) -- (axis cs:10,15) -- (axis cs:10,0) -- cycle;

            % Límite Superior de Control (LCS = 22 días)
            \draw[line width=1.3pt, dashed, color=lcsred] (axis cs:0.7, 22) -- (axis cs:10.4, 22);
            \node[fill=red!8, draw=red!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:10.5, 22) {%
                \textcolor{lcsred}{Límite Superior}\\[1pt]%
                \textcolor{lcsred}{(LCS = 22 días)}%
            };

            % Línea Central (Promedio = 16.5 días)
            \draw[line width=1.3pt, color=lcigreen] (axis cs:0.7, 16.5) -- (axis cs:10.4, 16.5);
            \node[fill=green!12, draw=green!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:10.5, 16.5) {%
                \textcolor{lcigreen}{Promedio As-Is}\\[1pt]%
                \textcolor{lcigreen}{($\mathbf{\bar{X}}$ = 16.5 d)}%
            };

            % Meta de Proyecto SIGE (3 días)
            \draw[line width=1.3pt, dashed, color=lineblue] (axis cs:0.7, 3) -- (axis cs:10.4, 3);
            \node[fill=blue!10, draw=blue!40, rounded corners=3pt, inner sep=2pt, font=\tiny\bfseries, align=left, anchor=west] at (axis cs:10.5, 3) {%
                \textcolor{lineblue}{Meta SIGE}\\[1pt]%
                \textcolor{lineblue}{($\le 3$ días)}%
            };

            % Curva de latencia histórica
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
                (1, 18) (2, 16) (3, 21) (4, 19) (5, 15) 
                (6, 22) (7, 17) (8, 14) (9, 16) (10, 15)
            };
        \end{axis}
    \end{tikzpicture}
    \caption{Diagrama de Comportamiento (Run Chart): Demora Histórica en Días del Proceso Manual As-Is.}
    \label{fig:runchart_historico}
\end{figure}
\FloatBarrier

\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 1 (1.1 a 1.8)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Técnico} & \textbf{Horas} & \textbf{Criterio de Aceptación Verificado} & \textbf{Resultado} \\
\hline
\textbf{EDT 1.1} & Levantamiento As-Is & 24 h & Diagnóstico de formatos Word y matriz de problemas P-01 a P-06. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.2} & Actores y Procesos & 32 h & Matriz RACI, roles institucionales y mapa de macroprocesos. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.3} & Requisitos SRS & 32 h & 24 Requisitos Funcionales y 8 No Funcionales bajo IEEE 29148. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.4} & Alcance y Restricciones & 24 h & Fronteras del proyecto, exclusiones y alineación con metas SGC. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.5} & Reglas de Negocio & 24 h & Catálogo de 6 reglas de negocio y diseño de Validation Gates. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.6} & Caso de Negocio y ROI & 24 h & Justificación económica con ROI proyectado de +554\% y Charter. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.7} & Cronograma y EDT & 16 h & Planificación de 34 tareas en Trello y MS Project con ruta crítica. & \textbf{APROBADO} \\
\hline
\textbf{EDT 1.8} & Hito 1: Aprobación F1 & 16 h & Auditoría colegiada, Ishikawa, Run Chart y cierre formal. & \textbf{APROBADO} \\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL HORAS FASE 1:}} & \textbf{192 h} & \multicolumn{2}{l|}{\textbf{100\% de Tareas de Fase 1 Completadas (Semana 1)}} \\
\hline
\end{tabularx}
\caption{Matriz oficial de auditoría y aprobación de entregables de la Fase 1.}
\label{tab:auditoria_fase1}
\end{table}

\subsection{Línea Base del Cronograma del Proyecto SIGE al Cierre del Hito 1}
A continuación se detalla el estado global del proyecto a la fecha de este corte (18 de agosto de 2026), certificando que la Fase 1 se encuentra concluida al 100\% y que las fases de desarrollo y pruebas se encuentran programadas para su ejecución futura:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|m{2.5cm}|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 1} \\
\hline
\textbf{Fase 1} & Análisis y Planificación & 12 ago -- 18 ago 2026 & 8 & 192 h & \textbf{100\% CUMPLIDO (Aprobado)} \\
\hline
\textbf{Fase 2} & Diseño y Arquitectura & 19 ago -- 31 ago 2026 & 7 & 192 h & \textit{0\% PROGRAMADO (Siguiente)} \\
\hline
\textbf{Fase 3} & Implementación y Desarrollo & 01 sep -- 12 oct 2026 & 16 & 400 h & \textit{0\% PROGRAMADO (Futuro)} \\
\hline
\textbf{Fase 4} & Pruebas y Cierre Formal & 12 oct -- 13 oct 2026 & 3 & 48 h & \textit{0\% PROGRAMADO (Futuro)} \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL GENERAL DEL PROYECTO:}} & \textbf{34} & \textbf{832 h} & \textbf{Avance Global: 23.5\%} \\
\hline
\end{tabularx}
\caption{Línea Base del Cronograma del Proyecto SIGE al cierre del Hito 1 (18 de agosto de 2026).}
\label{tab:linea_base_hito1}
\end{table}
"""

    anx1_8 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 1.8 en el Tablero Trello}
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
Período de Ejecución & 18 de agosto de 2026 (1 día laborable) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV), Nixon Hurtado (NH), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{08\_Entregable\_General\_Semana\_1.pdf} (Paquete Completo Aprobado) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado Formalmente \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 1.8 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Acta Formal de Aprobación de Fase 1 (Hito 1)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA INSTITUCIONAL DE CIERRE DE HITO 1 -- SISTEMA SIGE}} \\
\hline
\textbf{Fecha de Sesión:} & 18 de agosto de 2026 \\
\hline
\textbf{Lugar:} & Sala de Juntas / Sesión Virtual Teams -- FISEI \\
\hline
\textbf{Participantes:} & Steeven Toala (Líder Técnico), Heidi Villavicencio (Calidad), Nixon Hurtado (Analista), Andrea Vásquez (Diseñadora), Ing. Paulo Torres (Docente Evaluador). \\
\hline
\textbf{Resolución Oficial:} & Habiendo verificado el cumplimiento del 100\% de los entregables de análisis (EDT 1.1 a 1.7), el rigor del diagnóstico As-Is y la consistencia de los 24 Requisitos Funcionales del SRS, el Docente Evaluador declara APROBADA formalmente la Fase 1 y autoriza el inicio de la Fase 2 de Diseño y Arquitectura a partir del 19 de agosto de 2026. \\
\hline
\end{tabularx}
\caption{Acta oficial de aprobación de Fase 1.}
\end{table}

\subsection*{Anexo 3: Lista de Chequeo y Criterios de Aceptación Institucional (SGC ISO 9001:2015)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Criterio de Calidad SGC} & \textbf{Mecanismo de Verificación Técnica} & \textbf{Conformidad} & \textbf{Responsable} \\
\hline
Cumplimiento de Fase 1 & 8 de 8 tareas finalizadas en el Tablero Trello & 100\% CONFORME & Steeven Toala \\
\hline
Línea Base Congelada & Especificación SRS de 24 requisitos firmada y aprobada & 100\% CONFORME & Heidi Villavicencio \\
\hline
Horas de Esfuerzo & 192 horas-hombre netas ejecutadas según lo planificado & 100\% CONFORME & Nixon Hurtado \\
\hline
Aprobación del Hito & Acta de cierre firmada por el docente evaluador & 100\% CONFORME & Ing. Paulo Torres \\
\hline
\end{tabularx}
\caption{Lista de verificación y control de calidad institucional del entregable 1.8.}
\end{table}
"""
    write_tex("1.8_HITO_1_Aprobacion_Fase_1_Entregable_General.tex",
              render_doc("TI-SIGE-ENT-F1-008", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 1 ANÁLISIS", "18/08/2026", "18/08/2026", "HITO 1: APROBACIÓN DE FASE 1", b1_8, "18/08/2026", anx1_8))

    print("Fase 1 generation completed successfully with complete temporal coherence!")

if __name__ == "__main__":
    generate_fase1()
