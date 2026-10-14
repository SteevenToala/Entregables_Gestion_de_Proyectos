# generate_fase2_enhanced.py
import os
from template_engine import render_doc

def generate_fase2():
    base_dir = os.path.join("Entregables_Latex", "Fase_2") if os.path.exists("Entregables_Latex") else "Fase_2"
    os.makedirs(base_dir, exist_ok=True)

    # =========================================================================
    # 2.1 DIAGRAMAS GENERAL Y DETALLADO DE CASOS DE USO
    # =========================================================================
    b2_1 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Diagramas General y Detallado de Casos de Uso del Sistema SIGE -- Código EDT: 2.1

\section{Introducción}
El modelado de Casos de Uso bajo el estándar de la Object Management Group (OMG) en UML constituye el pilar fundamental para formalizar las fronteras funcionales y operativas del sistema web SIGE. A partir de los 24 Requisitos Funcionales consolidados en la Fase 1, el presente entregable estructura el catálogo y las relaciones entre los actores institucionales del Sistema de Gestión de la Calidad (SGC) de la FISEI y los módulos del sistema. Se definen las dependencias de inclusión (\texttt{<<include>>}) y extensión (\texttt{<<extend>>}), junto con las especificaciones textuales detalladas para los escenarios primarios, alternos y de excepción en la elaboración de planes, matrices dinámicas y flujos de revisión colegiada.

\section{Objetivo}
\subsection{Objetivo General}
Modelar formalmente el comportamiento funcional e interacciones del sistema SIGE mediante diagramas UML de casos de uso generales y detallados, garantizando la integración de los roles institucionales y los procesos del SGC de la FISEI.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Elaborar el Diagrama General de Casos de Uso agrupando los 8 casos de uso centrales (CU-01 a CU-08).
    \item Especificar la plantilla formal de casos de uso detallados para los flujos críticos: Elaboración de Plan, Gestión de la Matriz Dinámica y Cascada de Firmas.
    \item Documentar los escenarios de excepción, controles transaccionales y mecanismos de gestión de extemporaneidad.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Mapeo completo de interacciones para: Docente Titular/Ocasional, Coordinador de Área, Coordinador de Carrera, Subdecano y Administrador SGC.
    \item Especificación formal de precondiciones, disparadores, secuencias de eventos y postcondiciones en 3NF conceptual.
    \item Trazabilidad directa con los requisitos funcionales RF-01 a RF-24 aprobados en EDT 1.3.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Codificación de controladores en Node.js o construcción de vistas JSX en React (correspondientes a Fase 3).
    \item Modelos físicos relacionales DDL (abordados en EDT 2.4).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Caso de Uso (Use Case):} Conjunto de secuencias de acciones realizadas por el sistema que producen un resultado observable de valor para un actor específico según UML 2.5.1.
    \item \textbf{Actor Primario:} Entidad institucional que inicia una interacción con el sistema para alcanzar un objetivo funcional directo (e.g., Docente Elaborador).
    \item \textbf{Relación de Inclusión (\texttt{<<include>>}):} Vínculo donde el caso de uso base incorpora explícitamente y de forma no opcional el comportamiento del caso de uso incluido.
    \item \textbf{Relación de Extensión (\texttt{<<extend>>}):} Vínculo que especifica que el comportamiento de un caso de uso puede ser incrementado condicionalmente por otro en puntos de extensión definidos.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 2.1):} Diagramación UML formal, redacción de especificaciones textuales y diseño de escenarios alternos.
    \item \textbf{Steeven Toala (Líder Técnico / Arquitecto):} Validación de consistencia arquitectónica y trazabilidad con el modelo C4.
    \item \textbf{Nixon Hurtado (Analista de Requisitos):} Verificación de correspondencia funcional con los requisitos RF-01 a RF-24.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación metodológica de los casos de uso institucionales.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Garantía de calidad, transparencia y rendición obligatoria de la labor docente ante organismos directivos.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67:} Distribución legal de actividades de docencia, tutoría, investigación y gestión institucional.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Arts. 10 y 11:} Delimitación de perfiles y confidencialidad en el acceso a los datos de evaluación y seguimiento académico.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{OMG Unified Modeling Language (OMG UML), Versión 2.5.1:} Especificación formal de sintaxis y semántica para modelado de casos de uso.
    \item \textbf{ISO/IEC/IEEE 29148:2018 (Requirements Engineering):} Estructura y especificación formal de casos de uso y requerimientos operacionales.
    \item \textbf{ISO 9001:2015, Cláusula 7.5:} Aseguramiento de la información documentada en procesos de revisión y aprobación institucional.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se empleó la metodología orientada a objetos bajo el marco de desarrollo guiado por casos de uso (\textit{Use-Case Driven Development}). Se derivaron los actores y límites del sistema mediante matrices de correspondencia con los requerimientos funcionales aprobados. Para cada caso de uso se elaboró una ficha normalizada compuesta por: identificador, nombre, actor principal, precondiciones, flujo principal o camino feliz (\textit{happy path}), flujos alternos, flujos de excepción y postcondiciones comprobables.

\subsection{Políticas de Calidad del Modelado}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Completitud Funcional:} Cada uno de los 24 requerimientos funcionales debe estar cubierto por al menos un caso de uso primario o extendido.
    \item \textbf{Política de Trazabilidad Bidireccional:} Cada especificación textual debe declarar explícitamente sus dependencias de requisitos y entidades del modelo de dominio.
    \item \textbf{Política de Control de Acceso por Roles:} Ningún caso de uso puede ejecutarse sin la previa resolución de identidad y verificación de permisos RBAC del actor en sesión.
    \item \textbf{Política de Atomicidad de Escenarios:} Los flujos de excepción deben garantizar que un fallo en la validación mantenga el sistema en un estado consistente sin corrupción de datos.
\end{enumerate}

\section{Descripción de actividades}
El modelado de casos de uso constituyó la base para traducir los 24 requisitos funcionales del SRS hacia contratos de interacción precisos entre los actores del SGC y el sistema web SIGE. El equipo de análisis y modelado desarrolló las siguientes actividades técnicas:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Identificación de Actores Primarios y Perímetros de Interacción:} Con base en el estatuto de la FISEI y la matriz RACI de la Fase 1, se delimitaron formalmente las fronteras de los roles autorizados: Docente Elaborador (titular/ocasional), Coordinador de Área Académica, Coordinador de Carrera, Subdecano de Facultad y Administrador del SGC. Se garantizó que ninguna interacción viole el principio de segregación de funciones.
    \item \textbf{Estructuración del Catálogo de Casos de Uso (CU-01 a CU-08):} Se agruparon las operaciones del sistema en 8 casos de uso de alta cohesión funcional, asegurando cobertura directa de la gestión de credenciales, llenado de planes, cálculo de matrices, carga probatoria, revisión colegiada, firmas digitales y gestión de prórrogas.
    \item \textbf{Modelado de Relaciones de Inclusión y Extensión:} Aplicando la notación estándar OMG UML 2.5.1, se formalizó que el caso de uso base CU-02 (\textit{Elaborar Plan de Trabajo}) incluye obligatoriamente (\texttt{<<include>>}) la autenticación en sesión (CU-01) y la gestión matricial (CU-03), mientras que la solicitud de prórroga extemporánea (CU-08) extiende condicionalmente (\texttt{<<extend>>}) el flujo principal únicamente ante ventanas de fecha vencidas.
    \item \textbf{Redacción de Especificaciones Textuales Normalizadas:} Para cada caso de uso se redactó una plantilla formal con identificador, precondiciones, disparador, curso básico (camino feliz), flujos alternos, escenarios de excepción y postcondiciones verificables en base de datos.
\end{itemize}

\subsection{Matriz Oficial de Casos de Uso del Sistema (CU-01 a CU-08)}
A continuación se detalla la matriz general de casos de uso estructurada para el sistema SIGE:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Nombre del Caso de Uso} & \textbf{Actores y Propósito Funcional} & \textbf{Requisitos} & \textbf{Criticidad} \\
\hline
\textbf{CU-01} & Iniciar Sesión en SIGE & Docente, Coordinadores, Admin: Validación credenciales JWT y carga de roles. & RF-01, RF-02 & Alta \\
\hline
\textbf{CU-02} & Elaborar Plan de Trabajo & Docente Elaborador: Diligenciamiento estructurado de datos generales y carga horaria. & RF-03, RF-04 & Crítica \\
\hline
\textbf{CU-03} & Gestionar Matriz Dinámica & Docente Elaborador: Registro de actividades, cronograma semanal y ponderación 100\%. & RF-05, RF-06 & Crítica \\
\hline
\textbf{CU-04} & Cargar Evidencias en MinIO & Docente Elaborador: Carga de respaldos PDF, cálculo de hash SHA-256 y URLs prefirmadas. & RF-07, RF-08 & Alta \\
\hline
\textbf{CU-05} & Revisar en Comité & Coordinador de Área / Carrera: Auditoría técnica y observaciones granulares. & RF-09, RF-10 & Alta \\
\hline
\textbf{CU-06} & Cascada de Firmas Digitales & Docente, Revisor, Aprobador: Estampado cronológico irreversible de firmas digitales. & RF-11, RF-12 & Crítica \\
\hline
\textbf{CU-07} & Exportar Documento SGC & Todos los Roles: Generación de salidas oficiales en formato PDF vectorial y Word. & RF-13, RF-14 & Alta \\
\hline
\textbf{CU-08} & Gestionar Extemporaneidad & Docente y Administrador: Solicitud auditada de prórroga para apertura de plazos. & RF-15, RF-16 & Media \\
\hline
\end{tabularx}
\caption{Matriz del catálogo oficial de Casos de Uso del Sistema SIGE.}
\label{tab:matriz_casos_uso}
\end{table}

\subsection{Especificación Textual Detallada: CU-03 (Gestión de Matriz Dinámica)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.7\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{FORMATO OFICIAL DE ESPECIFICACIÓN DE CASO DE USO -- CU-03}} \\
\hline
Nombre del Caso de Uso & Gestión de Matriz Dinámica de Actividades SGC \\
\hline
Actor Principal & Docente Elaborador \\
\hline
Precondiciones & El usuario posee una sesión activa en el sistema y ha seleccionado un documento en estado ``Borrador''. \\
\hline
Disparador (Trigger) & El docente navega a la pestaña ``Matriz de Actividades'' dentro del Wizard del Plan de Trabajo. \\
\hline
Flujo Principal (Happy Path) & 
\begin{enumerate}[leftmargin=1.2em, itemsep=1pt]
    \item El sistema renderiza la tabla interactiva de actividades recuperadas de PostgreSQL 18.
    \item El docente hace clic en ``Agregar Actividad'' o selecciona ``Sugerir con IA''.
    \item El docente ingresa la descripción de la actividad, medios de verificación y horas semanales.
    \item El docente asigna la ponderación porcentual y marca las semanas del cronograma (1 a 16).
    \item El sistema recalcula en tiempo real la sumatoria de ponderación y horas acumuladas.
    \item Al alcanzar el 100\% de ponderación, el sistema habilita el botón de guardado definitivo.
    \item El sistema persiste las filas en la base de datos y confirma el estado ``Guardado''.
\end{enumerate} \\
\hline
Flujos Alternos & 
\begin{itemize}[leftmargin=1.2em, itemsep=1pt]
    \item \textbf{A1 - Asistencia de IA:} El docente solicita sugerencias automáticas de redacción acordes al catálogo institucional de actividades del SGC.
    \item \textbf{A2 - Reordenamiento:} El docente arrastra filas para ordenar prioridades sin alterar las sumatorias.
\end{itemize} \\
\hline
Flujos de Excepción & 
\begin{itemize}[leftmargin=1.2em, itemsep=1pt]
    \item \textbf{E1 - Ponderación Distinta de 100\%:} La Validation Gate bloquea la transición de estado y resalta en color carmesí la diferencia porcentual faltante o excedente.
    \item \textbf{E2 - Actividad sin Medios de Verificación:} El sistema impide el avance a la etapa de firmas hasta que cada ítem posea al menos un medio auditable.
\end{itemize} \\
\hline
Postcondiciones & La matriz de actividades queda almacenada con integridad relacional en la tabla \texttt{actividades\_\allowbreak matriz}. \\
\hline
\end{tabularx}
\caption{Especificación textual detallada del caso de uso crítico CU-03.}
\label{tab:cu_03_detalle}
\end{table}
"""

    anx2_1 = r"""
\subsection*{Anexo: Evidencias de Modelado y Especificación de Casos de Uso}

\subsubsection*{1. Especificación Formal y Trazabilidad de Casos de Uso}
Para garantizar que el modelado funcional responda estrictamente a la operativa institucional y no a conjeturas aisladas, los Casos de Uso se derivaron directamente del formato oficial \texttt{UTA- SGC- A-\allowbreak 2-\allowbreak 1- P7-\allowbreak T1} (Plan de Trabajo Docente) y de los 24 Requisitos Funcionales aprobados en la Fase 1.

El desarrollo del modelado se ejecutó en cuatro etapas secuenciales:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Identificación de Actores Primarios y Secundarios:} A partir del estatuto orgánico de la UTA y la matriz de actores de la FISEI, se formalizaron los roles del sistema: Docente Elaborador (usuario primario de planificación y carga de evidencias), Coordinador de Comisión (revisor de actividades específicas), Coordinador de Carrera (auditor de carga horaria y primer validador), Subdecano (aprobador de facultad) y Administrador SGC (gestor de catálogos y prórrogas).
    \item \textbf{Estructuración del Catálogo de 8 Casos de Uso (CU-01 a CU-08):} Se definieron los límites del sistema agrupando las interacciones en CU-01 (Iniciar Sesión JWT), CU-02 (Elaborar Plan en Wizard), CU-03 (Gestionar Matriz Dinámica 100\%), CU-04 (Custodiar Evidencias en MinIO S3), CU-05 (Revisar Expediente en Comité), CU-06 (Cascada Secuencial de Firmas), CU-07 (Exportar Documento Oficial SGC) y CU-08 (Gestionar Prórrogas Extemporáneas).
    \item \textbf{Definición de Relaciones de Inclusión y Extensión:} Se identificaron las dependencias funcionales: todos los casos de uso incluyen obligatoriamente la resolución de identidad (\texttt{<<include>> CU-\allowbreak 01}); la elaboración de plan incluye el cálculo automático de 40 horas; y la gestión de extemporaneidad extiende condicionalmente (\texttt{<<extend>> CU-\allowbreak 08}) la edición cuando la fecha actual sobrepasa el cronograma lectivo.
    \item \textbf{Redacción de Especificaciones Textuales Normalizadas:} Se redactaron fichas detalladas para cada caso de uso declarando precondiciones, flujo principal (\textit{happy path}), flujos alternos de asistencia y flujos de excepción transaccionales.
\end{enumerate}

\subsubsection*{2. Evidencia Visual del Diagrama de Casos de Uso y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_01_casos_de_uso.png}
    \caption{Diagrama General de Casos de Uso del Sistema SIGE bajo Estándar OMG UML 2.5.1.}
    \label{fig:casos_uso_general}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural de Casos de Uso (UML 2.5.1):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Perímetros del Sistema y Actores Institucionales:} El diagrama delimita la frontera del sistema web SIGE, ubicando a los 5 actores según sus privilegios estatutarios: Docente Elaborador, Coordinador de Comisión, Director de Carrera, Subdecano y Administrador SGC.
    \item \textbf{Subsistemas Operativos y Casos de Uso Primarios:} Se estructuran los casos de uso nucleares: Elaboración y Edición del Plan (CU-02), Matriz Dinámica de Actividades (CU-03), Repositorio de Evidencias (CU-04), Revisión Colegiada de Comisiones (CU-05), Legalización y Firmas (CU-06) y Exportación Oficial en PDF/Word (CU-07).
    \item \textbf{Relaciones de Inclusión Obligatoria (\texttt{<<include>>}):} Cada operación de guardado o avance incluye obligatoriamente la verificación de credenciales activas (CU-01) y la evaluación previa de Validation Gates lógicas, garantizando que ninguna transacción omita las reglas de negocio.
    \item \textbf{Relaciones de Extensión Condicional (\texttt{<<extend>>}):} El flujo de observaciones granulares extiende el caso de uso de revisión (CU-05), activándose de forma condicional únicamente cuando una comisión académica detecta no conformidades en el expediente.
\end{itemize}

\subsubsection*{3. Matriz de Trazabilidad Requisitos Funcionales vs Casos de Uso}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.55\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{RF ID} & \textbf{Requisito Funcional} & \textbf{Caso de Uso} & \textbf{Criterio de Aceptación y Regla de Negocio SGC} \\
\hline
RF-01 & Autenticación de Usuarios & CU-01 & Validación estricta con Argon2id y emisión de token JWT con expiración a 15 min. \\
\hline
RF-03 & Configuración del Plan & CU-02 & Verificación del total exacto de 40 horas semanales según Art. 45 del RRA. \\
\hline
RF-05 & Matriz de Actividades & CU-03 & Recálculo reactivo con suma obligatoria al 100.00\% y asignación semanal en 16 semanas. \\
\hline
RF-07 & Custodia de Evidencias & CU-04 & Transferencia a MinIO S3 con cálculo de huella SHA-256 para no repudio probatorio. \\
\hline
RF-09 & Panel de Revisión Comité & CU-05 & Visualización de documento y drawer lateral con registro inmutable de observaciones. \\
\hline
RF-11 & Cascada de Firmas & CU-06 & Secuencia obligatoria 1 $\to$ 2 $\to$ 3 con estampado de firma digital y marca temporal. \\
\hline
RF-13 & Exportación SGC & CU-07 & Generación de PDF A4 idéntico al formato oficial con código QR y metadatos SGC. \\
\hline
RF-15 & Gestión de Prórrogas & CU-08 & Desbloqueo temporal auditado de planes extemporáneos previa autorización de Subdecanato. \\
\hline
\end{tabularx}
\caption{Matriz técnica de trazabilidad entre Requisitos Funcionales y Casos de Uso del sistema SIGE.}
\end{table}
"""
    doc2_1 = render_doc("TI-SIGE-ENT-F2-001", "DISEÑO DE SOFTWARE / CASOS DE USO UML", "21/08/2026", "21/08/2026", "DIAGRAMAS GENERAL Y DETALLADO DE CASOS DE USO", b2_1, "21/08/2026", anx2_1)
    with open(os.path.join(base_dir, "2.1_Diagramas_General_y_Detallado_Casos_de_Uso.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_1)

    # =========================================================================
    # 2.2 DISEÑO DE ARQUITECTURA DE LA SOLUCIÓN (SAD Y MODELO C4)
    # =========================================================================
    b2_2 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Diseño de Arquitectura de la Solución (SAD y Modelo C4) -- Código EDT: 2.2

\section{Introducción}
El diseño arquitectónico del sistema SIGE constituye el marco estructural que garantiza la escalabilidad, mantenibilidad, seguridad y rendimiento exigidos por la Universidad Técnica de Ambato. El presente Documento de Arquitectura de Software (SAD) formaliza la organización modular del sistema aplicando el modelo C4 (\textit{Context, Containers, Components, Code}) propuesto por Simon Brown y los principios de \textit{Clean Architecture} de Robert C. Martin. Se documenta la separación estricta entre capas de presentación, dominio, aplicación e infraestructura, asegurando la independencia del framework y desacoplamiento de la base de datos relacional y servicios externos de almacenamiento en objetos.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar y formalizar la arquitectura de software integral del sistema SIGE mediante el modelo C4 y Clean Architecture, estableciendo las decisiones estructurales (ADR) que guiarán la implementación técnica.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Estructurar el diagrama de contenedores C4 definiendo las fronteras entre React SPA, Express REST API, PostgreSQL 18, MinIO S3 y LanguageTool.
    \item Modelar la arquitectura hexagonal multicapa con inversión de dependencias.
    \item Formalizar las Decisiones de Arquitectura de Software (ADR-01 a ADR-06) con sus correspondientes justificaciones y consecuencias técnicas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Especificación de vistas de Contexto y Contenedores bajo modelo C4.
    \item Definición de protocolos de comunicación inter-servicios (HTTPS, REST JSON, S3 API).
    \item Matriz de atributos de calidad basados en el estándar ISO/IEC 25010.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementación de pipelines de CI/CD para producción en servidores cloud externos.
    \item Configuración de clústeres distribuidos Kubernetes (reservados para etapas de escalado masivo institucional).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SAD (Software Architecture Document):} Documento formal que captura las decisiones arquitectónicas significativas, patrones de diseño y vistas del sistema.
    \item \textbf{Modelo C4:} Enfoque estructurado para visualizar la arquitectura de software en 4 niveles jerárquicos: Contexto, Contenedores, Componentes y Código.
    \item \textbf{Clean Architecture:} Paradigma de diseño que sitúa las entidades de negocio en el núcleo y aplica inversión de control hacia la infraestructura externa.
    \item \textbf{ADR (Architectural Decision Record):} Registro documental breve que describe una decisión arquitectónica adoptada, su contexto y sus consecuencias.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 2.2):} Arquitectura de software principal, modelado C4, definición de patrones y redacción de ADRs.
    \item \textbf{Nixon Hurtado (Especialista en Backend / Persistencia):} Diseño de capa de acceso a datos, contratos de infraestructura y volumetría.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Evaluación de conformidad frente al estándar ISO/IEC 25010 y requisitos no funcionales.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la arquitectura base del proyecto.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Transparencia y confiabilidad técnica de los repositorios institucionales de información académica.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 37:} Principios de seguridad por diseño y por defecto (\textit{Privacy by Design and by Default}).
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO/IEC/IEEE 42010:2011 (Systems and Software Engineering -- Architecture Description):} Estándar internacional para la documentación y especificación de arquitecturas.
    \item \textbf{ISO/IEC 25010:2011 (Systems and Software Quality Requirements and Evaluation):} Evaluación de mantenibilidad, fiabilidad, rendimiento y seguridad.
    \item \textbf{Twelve-Factor App Methodology:} Principios para el diseño de aplicaciones nativas en la nube y configuradas por entorno.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se adoptó un enfoque arquitectónico orientado a microservicios modulares desacoplados mediante contenedores. La lógica del negocio se aísla de frameworks y protocolos externos utilizando el patrón de Puertos y Adaptadores (\textit{Hexagonal Architecture}). Las comunicaciones síncronas se estructuran mediante API REST con payload JSON validado en esquemas fuertemente tipados. Para el almacenamiento de grandes objetos binarios (evidencias PDF), se diseñó una integración externa con MinIO compatible con el protocolo S3 de Amazon Web Services.

\subsection{Políticas de Calidad Arquitectónica}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inversión de Dependencias:} El código de dominio no debe importar librerías de base de datos ni librerías de presentación web; la comunicación ocurre a través de interfaces o contratos.
    \item \textbf{Política de Autenticación Stateless:} El servidor backend no mantiene estado de sesión en memoria; cada petición debe autenticarse de forma independiente mediante tokens JWT firmados criptográficamente.
    \item \textbf{Política de Inmutabilidad de Evidencias:} Los archivos almacenados en el storage de objetos MinIO no pueden sobrescribirse; cada versión recibe un identificador único con hash de comprobación.
    \item \textbf{Política de Resiliencia de Fallas:} Toda llamada externa (MinIO, motor ortográfico) debe implementar un mecanismo de \textit{timeout} (máximo 5000 ms) y fallback de contingencia.
\end{enumerate}

\section{Descripción de actividades}
El diseño arquitectónico de SIGE se concibió bajo los principios de desacoplamiento de Clean Architecture, garantizando que la lógica de negocio institucional permanezca independiente de componentes de persistencia o interfaces de usuario. Las actividades de arquitectura desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Selección y Justificación del Patrón Clean Architecture:} Se adoptó una arquitectura en cuatro capas concéntricas (Dominio, Casos de Uso, Adaptadores de Interfaz y Frameworks/Drivers), asegurando que las entidades normativas de la FISEI no posean dependencias hacia el motor de persistencia relacional ni bibliotecas de terceros.
    \item \textbf{Formulación y Registro de Decisiones de Arquitectura (ADR-01 a ADR-06):} Se redactaron formalmente seis registros técnicos de decisión: ADR-01 (Clean Architecture), ADR-02 (PostgreSQL 18 con soporte JSONB para secciones de texto enriquecido), ADR-03 (React 19 SPA con Tailwind CSS), ADR-04 (Editor TipTap con autoguardado asíncrono con debounce de 1500 ms), ADR-05 (MinIO S3 para custodia de evidencias) y ADR-06 (Autenticación JWT con rotación de refresh tokens y Argon2id).
    \item \textbf{Modelado de Diagramas de Contexto y Contenedores bajo el Modelo C4:} Se elaboraron las vistas arquitectónicas de Nivel 1 (Contexto de Sistema interactuando con Docentes, Directores y SGA) y Nivel 2 (Contenedores web, API REST Express v5, base de datos PostgreSQL, servidor MinIO y servicio LanguageTool).
    \item \textbf{Diseño de Políticas de Seguridad Perimetral y Resiliencia:} Se establecieron protocolos de comunicación sobre HTTPS/TLS, interceptación centralizada de errores en Express mediante un error handler unificado y aislamiento de variables de entorno sensibles en archivos \texttt{.\allowbreak env} protegidos.
\end{itemize}

\subsection{Matriz de Decisiones de Arquitectura de Software (ADR-01 a ADR-06)}
A continuación se detalla la matriz formal de las decisiones arquitectónicas adoptadas para el sistema:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Decisión} & \textbf{Justificación Técnica} & \textbf{Consecuencias y Mitigación} & \textbf{Estado} \\
\hline
\textbf{ADR-01} & Monolito Modular con API REST & Evita la sobrecarga de orquestación de microservicios distribuidos manteniendo bajo acoplamiento por dominios. & Requiere control estricto de fronteras de módulos internos. & Aceptada \\
\hline
\textbf{ADR-02} & Base de Datos PostgreSQL 18 & Motor relacional con soporte nativo de tipo JSONB para almacenar contenido semiestructurado de secciones. & Requiere índices GIN especializados para búsquedas de texto. & Aceptada \\
\hline
\textbf{ADR-03} & Almacenamiento MinIO S3 & Almacena archivos PDF pesados fuera de la base de datos, reduciendo el tamaño de backups y latencia. & Requiere generación de URLs prefirmadas con expiración de 15 min. & Aceptada \\
\hline
\textbf{ADR-04} & Autenticación JWT y RBAC & Mecanismo stateless escalable que transmite roles en payload cifrado sin consultar DB en cada lectura. & Invalidez de tokens se mitiga mediante TTL corto (15 min) y refresh tokens. & Aceptada \\
\hline
\textbf{ADR-05} & SPA con React y Vite & Experiencia de usuario ágil sin recarga de página y soporte de guardado automático con debounce. & Requiere sanitización estricta de HTML mediante DOMPurify frente a XSS. & Aceptada \\
\hline
\textbf{ADR-06} & Asistencia Híbrida NLP & Motor local LanguageTool en contenedor Docker complementado con Google Gemini API para sugerencias semánticas. & Si no hay conectividad externa, el sistema opera con el corrector local. & Aceptada \\
\hline
\end{tabularx}
\caption{Matriz de Decisiones Arquitectónicas (ADR) del Sistema SIGE.}
\label{tab:adr_matrix}
\end{table}

\subsection{Matriz de Atributos de Calidad Arquitectónica (ISO/IEC 25010)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Atributo} & \textbf{Requisito de Calidad} & \textbf{Estrategia Arquitectónica de Soporte} & \textbf{Métrica} \\
\hline
Rendimiento & Respuestas de API $<300\text{ ms}$ en operaciones habituales. & Índices relacionales B-Tree, pools de conexión y paginación en DB. & P95 $<250\text{ ms}$ \\
\hline
Seguridad & Protección contra OWASP Top 10 y cifrado en reposo. & Hash Argon2id para contraseñas, sanitización y JWT con firma HMAC. & 0 Hallazgos Altos \\
\hline
Mantenibilidad & Facilidad para modificar lógica sin afectar presentación. & Separación de capas con Clean Architecture y principios SOLID. & Deuda $<5\%$ \\
\hline
Fiabilidad & Cero pérdida de datos ante interrupciones de red. & Mecanismo de autoguardado debounce (800 ms) y almacenamiento transaccional. & RPO $= 0$ \\
\hline
\end{tabularx}
\caption{Matriz de Atributos de Calidad según ISO/IEC 25010.}
\end{table}
"""

    anx2_2 = r"""
\subsection*{Anexo: Evidencias de Arquitectura de Software y Modelo C4}

\subsubsection*{1. Decisiones de Diseño Arquitectónico y Desacoplamiento en Capas}
Para asegurar mantenibilidad, escalabilidad y estricta separación de responsabilidades, la arquitectura de SIGE se diseñó combinando los principios de Clean Architecture (Arquitectura Limpia) con la notación de diagramación del Modelo C4 (Contexto, Contenedores, Componentes y Código).

El proceso de ingeniería arquitectónica comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Estructuración en Cuatro Capas Concéntricas:} Capa de Dominio / Entidades (\textit{Entities}: \texttt{PlanDocente}, \texttt{ActividadMatriz}, libres de dependencias externas); Capa de Casos de Uso (\textit{Use Cases}: reglas de negocio orquestadoras como \texttt{ValidarHorasMinimas}); Capa de Adaptadores (\textit{Interface Adapters}: controladores REST Express v5, repositorios pg-promise y cliente MinIO S3); y Capa de Infraestructura / Frameworks (\textit{Frameworks and Drivers}: PostgreSQL 18, React SPA, Docker Compose y servidor Nginx).
    \item \textbf{Diagramación del Modelo C4 de Contenedores:} Se definieron los cinco contenedores autónomos que componen la topología: SPA Frontend, Backend REST API, Base de Datos PostgreSQL, Almacén de Objetos MinIO y Motor Lingüístico LanguageTool.
    \item \textbf{Definición de Contratos de Comunicación y Puertos:} Se establecieron los protocolos de intercambio (JSON sobre HTTP/REST para servicios, nativo TCP para base de datos y API S3 para archivos).
\end{enumerate}

\subsubsection*{2. Evidencias Visuales de la Arquitectura del Sistema y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_02_clean_architecture.png}
    \caption{Arquitectura Limpia (Clean Architecture) y Flujo de Dependencias del Sistema SIGE.}
    \label{fig:clean_arch}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural de la Arquitectura de Software:}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Desacoplamiento Concéntrico en Cuatro Capas (Clean Architecture):} Se ilustra la Regla de Dependencias: las capas externas (Frameworks y Adaptadores) dependen de las internas (Casos de Uso y Entidades de Dominio), pero el dominio nunca conoce la existencia de PostgreSQL, Express o React.
    \item \textbf{Topología de Contenedores y Microservicios (Modelo C4 Nivel 2):} El diagrama C4 detalla los 5 servicios orquestados en Docker: \texttt{sige-\allowbreak frontend} (SPA en React 19), \texttt{sige-\allowbreak backend} (API REST en Express v5), \texttt{sige-\allowbreak db} (PostgreSQL 18 con extensiones JSONB y UUID), \texttt{sige-\allowbreak minio} (S3 Object Storage) y \texttt{sige-\allowbreak languagetool} (corrección ortográfica local).
    \item \textbf{Canales de Comunicación y Seguridad Perimetral:} Las comunicaciones cliente-servidor operan sobre HTTPS/TLS con tokens JWT en cabeceras de autorización y cookies \texttt{HttpOnly} para refresh tokens; el acceso a MinIO se realiza mediante URLs prefirmadas de vida corta (15 min).
    \item \textbf{Trazabilidad con el Código Fuente:} Esta arquitectura se materializa en la estructura modular del repositorio: \texttt{backend/\allowbreak src/\allowbreak domain/\allowbreak }, \texttt{backend/\allowbreak src/\allowbreak usecases/\allowbreak }, \texttt{backend/\allowbreak src/\allowbreak adapters/\allowbreak } y \texttt{docker-\allowbreak compose.\allowbreak yml}.
\end{itemize}

\subsubsection*{3. Matriz Técnica de Servicios, Puertos y Protocolos de Infraestructura}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.8\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio Contenedor} & \textbf{Puerto Expuesto} & \textbf{Protocolo} & \textbf{Dependencia} & \textbf{Función Principal en la Arquitectura} \\
\hline
Frontend Web SPA & 5173 / 80 & HTTP / HTTPS & Backend API & Entrega de interfaz React y gestión reactiva de formularios. \\
\hline
Backend API REST & 5000 / 3000 & REST / JSON & Base de Datos & Lógica de negocio, Validation Gates, seguridad y firmas. \\
\hline
PostgreSQL 18 DB & 5432 & Nativo TCP & Almacén local & Persistencia relacional ACID, tablas 3NF y documentos JSONB. \\
\hline
MinIO S3 Storage & 9000 / 9001 & AWS S3 API & Almacén local & Almacenamiento privado de evidencias y generación de URLs prefirmadas. \\
\hline
Corrector LanguageTool & 8010 & HTTP REST & Memoria interna & Servicio local de asistencia gramatical en español sin fuga de datos. \\
\hline
\end{tabularx}
\caption{Matriz de servicios y comunicación de infraestructura del sistema SIGE.}
\end{table}
"""
    doc2_2 = render_doc("TI-SIGE-ENT-F2-002", "ARQUITECTURA DE SOFTWARE / C4 & CLEAN ARCHITECTURE", "25/08/2026", "25/08/2026", "DISEÑO DE ARQUITECTURA DE LA SOLUCIÓN", b2_2, "25/08/2026", anx2_2)
    with open(os.path.join(base_dir, "2.2_Diseno_Arquitectura_de_la_Solucion.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_2)

    # =========================================================================
    # 2.3 DIAGRAMAS DE SECUENCIA, ACTIVIDADES Y CLASES DE DOMINIO
    # =========================================================================
    b2_3 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Diagramas de Secuencia, Actividades y Clases de Dominio -- Código EDT: 2.3

\section{Introducción}
El comportamiento dinámico y estructural de los componentes del sistema SIGE debe ser modelado de manera unívoca para guiar la etapa de desarrollo sin ambigüedades. Mientras que el diseño arquitectónico define las capas de alto nivel, los diagramas de secuencia, actividades y clases de dominio modelan el flujo de datos temporal, los caminos de decisión lógica y la estructura orientada a objetos de las entidades del Sistema de Gestión de Calidad (SGC). El presente documento captura las especificaciones detalladas para los flujos críticos de validación transaccional, ciclo de revisión en comités y modelo estático de clases bajo estándar OMG UML 2.5.1.

\section{Objetivo}
\subsection{Objetivo General}
Modelar detalladamente los flujos dinámicos de ejecución, las secuencias de interacción temporal y la estructura de clases de dominio del sistema SIGE mediante diagramas formales UML.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Elaborar el Diagrama de Secuencia para el guardado y ejecución de Validation Gates.
    \item Modelar el Diagrama de Actividades para el ciclo completo de aprobación y revisión por comités.
    \item Estructurar el Diagrama de Clases de Dominio que mapea entidades, agregados y value objects institucionales.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modelado de transacciones entre capas de Controlador, Servicio, Validación Gate y Repositorio.
    \item Mapeo exhaustivo del ciclo de vida de los estados del documento institucional.
    \item Definición de operaciones de negocio, visibilidad y multiplicidad de clases.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Clases auxiliares o utilitarias de rendering visual en React.
    \item Consultas SQL físicas (delimitadas en EDT 2.4).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Diagrama de Secuencia UML:} Diagrama de interacción que enfatiza el ordenamiento temporal de los mensajes enviados entre líneas de vida de objetos.
    \item \textbf{Diagrama de Actividades UML:} Representación gráfica del flujo de control o flujo de datos de extremo a extremo entre actividades operacionales.
    \item \textbf{Diagrama de Clases de Dominio:} Modelo estructural que describe los tipos de objetos del sistema y las relaciones estáticas entre ellos.
    \item \textbf{Agregado (DDD):} Agrupación de objetos de dominio vinculados que se tratan como una unidad indivisible para el control de cambios de datos.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 2.3):} Modelado de diagramas de secuencia e interacciones dinámicas.
    \item \textbf{Andrea Vásquez (Diseñadora de Procesos):} Modelado del diagrama de actividades y flujos de revisión.
    \item \textbf{Nixon Hurtado (Analista de Dominio):} Definición de clases de dominio, invariantes y métodos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Verificación y aprobación técnica de los diagramas UML.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Transparencia procedimental en la aprobación colegiada de planes académicos.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45:} Fases secuenciales de planificación semestral y presentación de evidencias.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{OMG UML 2.5.1 Specification:} Estándares para diagramas de secuencia, actividades y clases.
    \item \textbf{Domain-Driven Design (DDD) Reference (Eric Evans):} Patrones para el modelado de entidades y agregados ricos.
    \item \textbf{ISO/IEC 19505-1:2012:} Información y modelos conceptuales para arquitecturas de software.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuraron los modelos dinámicos aplicando el principio de diseño por contratos. El Diagrama de Secuencia captura el flujo síncrono desde el envío HTTP del cliente React hasta la confirmación de la transacción en PostgreSQL, pasando obligatoriamente por la capa de validación de reglas de negocio (\textit{Validation Gate Pipeline}). El Diagrama de Actividades modela los caminos paralelos y bifurcaciones condicionales que determinan el avance hacia el Consejo Directivo o el retorno al docente elaborador por observaciones. El Diagrama de Clases formaliza el núcleo de entidades del dominio SGC.

\subsection{Políticas de Calidad del Modelado Dinámico}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Consistencia de Estados:} El estado de un documento solo puede transicionar mediante eventos explícitos y autorizados, impidiendo saltos directos no homologados.
    \item \textbf{Política de Transaccionalidad ACID:} Las operaciones que involucren el documento y su matriz de actividades deben ejecutarse bajo un único bloque transaccional atómico.
    \item \textbf{Política de Tipado Fuerte de Dominio:} Las clases de dominio deben encapsular sus atributos mediante métodos de negocio evitando modelos anémicos.
    \item \textbf{Política de Inmutabilidad de Firmas:} Una vez que un registro de firma es emitido, la clase \texttt{FirmaDocumento} pasa a ser inmutable en el dominio.
\end{enumerate}

\section{Descripción de actividades}
El modelado del comportamiento dinámico del sistema y la definición de las entidades de dominio aseguraron una representación computacional fidedigna de los procesos del SGC. El equipo técnico llevó a cabo las siguientes actividades de modelado UML:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado Dinámico de Secuencia UML para Casos de Uso Críticos:} Se construyeron diagramas de interacción temporal para los flujos más complejos del sistema: autenticación e intercambio de tokens JWT, creación asistida del plan mediante Wizard, y procesamiento concurrente de firmas con validación de compuertas.
    \item \textbf{Especificación de Diagramas de Actividades con Particiones (Swimlanes):} Se modelaron los flujos de control paralelos y condicionales distribuidos entre el Docente Elaborador, el Coordinador de Comisión, el Subdecano y el Motor de Reglas del Sistema, clarificando los puntos de decisión y bifurcación ante observaciones.
    \item \textbf{Modelado Estructural de Clases de Dominio Institucional:} Se modelaron las clases fundamentales del dominio en TypeScript y JavaScript: \texttt{Plan Trabajo Docente}, \texttt{Actividad Docente}, \texttt{Seccion Documento}, \texttt{Evidencia Respaldo} y \texttt{Firma Digital}, definiendo sus atributos, métodos de cálculo y contratos de validación intrínseca.
    \item \textbf{Formalización de la Máquina de Estados del Documento SGC:} Se especificaron los estados válidos del ciclo documental (\texttt{Borrador}, \texttt{En\_\allowbreak Revision}, \texttt{Observado}, \texttt{Aprobado\_\allowbreak  Carrera}, \texttt{Legalizado\_\allowbreak  Subdecanato}) y las transiciones atómicas permitidas bajo control transaccional ACID.
\end{itemize}

\subsection{Matriz de Entidades del Dominio y Métodos Operativos}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Clase de Dominio} & \textbf{Atributos Principales} & \textbf{Métodos de Negocio Clave} & \textbf{Multiplicidad} \\
\hline
\texttt{PlanDocente} & \texttt{id}, \texttt{periodo\_\allowbreak id}, \texttt{docente\_\allowbreak id}, \texttt{estado}, \texttt{horas} & \texttt{validarHorasMinimas()}, \texttt{avanzarEstado()} & 1 \\
\hline
\texttt{Seccion Documento} & \texttt{id}, \texttt{plan\_\allowbreak id}, \texttt{orden}, \texttt{titulo}, \texttt{contenido} & \texttt{actualizarContenido()}, \texttt{sanitizarHtml()} & $1 \dots N$ \\
\hline
\texttt{Actividad Matriz} & \texttt{id}, \texttt{plan\_\allowbreak id}, \texttt{nombre}, \texttt{horas}, \texttt{ponderacion} & \texttt{calcularAvance()}, \texttt{recalcularPond()} & $1 \dots N$ \\
\hline
\texttt{Evidencia Adjunta} & \texttt{id}, \texttt{actividad\_\allowbreak id}, \texttt{url\_\allowbreak s3}, \texttt{hash\_\allowbreak sha256} & \texttt{verificarIntegridad()}, \texttt{generarUrl()} & $0 \dots N$ \\
\hline
\texttt{Observacion Comite} & \texttt{id}, \texttt{plan\_\allowbreak id}, \texttt{usuario\_\allowbreak id}, \texttt{comentario} & \texttt{registrarObservacion()}, \texttt{marcarResuelto()} & $0 \dots N$ \\
\hline
\texttt{Firma Documento} & \texttt{id}, \texttt{plan\_\allowbreak id}, \texttt{firmante\_\allowbreak id}, \texttt{rol\_\allowbreak firma} & \texttt{estamparFirma()}, \texttt{validarSecuencia()} & $0 \dots 3$ \\
\hline
\end{tabularx}
\caption{Matriz de especificación de clases del dominio SGC.}
\label{tab:espec_clases}
\end{table}

\subsection{Matriz de Transición de Estados del Documento Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.3\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.4\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Etapa} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validación} & \textbf{Estado Resultante} \\
\hline
1 & \textit{Ninguno} & Creación de plan mediante asignación de periodo académico. & \textbf{Borrador} \\
\hline
2 & \textbf{Borrador} & Docente completa secciones y supera Validation Gates 1 a 4. & \textbf{En Revisión} \\
\hline
3 & \textbf{En Revisión} & Coordinador detecta inconsistencias y emite comentarios formales. & \textbf{Observado} \\
\hline
4 & \textbf{Observado} & Docente subsana observaciones y reenvía el documento. & \textbf{En Revisión} \\
\hline
5 & \textbf{En Revisión} & Coordinador de Área/Carrera aprueba y estampa su firma digital. & \textbf{Aprobado Comisión} \\
\hline
6 & \textbf{Aprobado Comisión} & Subdecano legaliza en Consejo Directivo y sella documento final. & \textbf{Aprobado HCD (Final)} \\
\hline
\end{tabularx}
\caption{Matriz de ciclo de vida de los estados del documento SGC.}
\end{table}
"""

    anx2_3 = r"""
\subsection*{Anexo: Evidencias de Diagramas UML Dinámicos y de Dominio}

\subsubsection*{1. Modelado Dinámico y Especificación de Ciclos de Vida}
Para formalizar cómo interactúan los componentes en el tiempo y cómo se orquesta la máquina de estados del plan de trabajo, se modelaron diagramas dinámicos UML 2.5.1 enfocados en los procesos críticos del SGC.

El proceso de especificación técnica comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Modelado del Ciclo de Vida y Transición de Estados:} Se especificó la máquina de estados formal del documento institucional: \textit{Borrador} (docente edita libremente), \textit{En Revisión} (bloqueado para edición tras superar Validation Gates), \textit{Observado} (retornado con observaciones del comité), \textit{Aprobado Comisión} (validado con firma del Coordinador) y \textit{Aprobado HCD} (legalizado con firma del Subdecano en Consejo Directivo).
    \item \textbf{Diagrama de Secuencia de Validación y Persistencia:} Se documentó el intercambio asíncrono de mensajes entre el Cliente React, el Middleware de Validation Gates, el Controlador de Documentos y PostgreSQL, detallando el manejo de excepciones HTTP 422.
    \item \textbf{Diagrama de Clases del Dominio SGC:} Se especificaron las clases de negocio, sus atributos esenciales, sus operaciones y los contratos de invariantes.
\end{enumerate}

\subsubsection*{2. Evidencias Visuales del Modelo Dinámico y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_03_secuencia_validation.png}
    \caption{Diagrama de Secuencia UML: Evaluación de Validation Gates y Flujo de Envío a Revisión.}
    \label{fig:secuencia_val}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural del Comportamiento Dinámico y Clases UML:}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Flujo de Interacción Temporal en el Diagrama de Secuencia:} Se modela la llamada asíncrona \texttt{POST /\allowbreak api/\allowbreak v1/\allowbreak planes/\allowbreak :id/\allowbreak secciones} desde el cliente React. El controlador delega en la cadena interceptora de Validation Gates, la cual ejecuta en menos de 15 ms las comprobaciones VG-1 y VG-2 antes de autorizar la escritura atómica en la base de datos.
    \item \textbf{Bifurcaciones y Decisiones en el Diagrama de Actividades (Swimlanes):} Se aprecian los carriles paralelos entre el Docente, la Comisión y el Subdecano. Si el expediente es observado, el estado conmuta a \texttt{Observado} y se notifica al docente; si es conforme, avanza a la cascada secuencial de 3 firmas.
    \item \textbf{Estructura de Entidades en el Modelo de Clases:} Modela las entidades ricas: \texttt{Plan\allowbreak Trabajo\allowbreak Docente} como agregado raíz que encapsula colecciones de \texttt{Actividad\allowbreak Docente}, \texttt{Seccion\allowbreak Documento}, \texttt{Evidencia\allowbreak Respaldo} y \texttt{Firma\allowbreak Digital}, definiendo sus métodos de cálculo de horas y contratos de inmutabilidad.
    \item \textbf{Máquina de Estados Finita del Documento SGC:} Garantiza computacionalmente que ningún expediente alcance el estado \texttt{Legalizado\_\allowbreak  Subdecanato} sin haber transitado previamente por la firma del docente y el visto bueno del coordinador de carrera.
\end{itemize}

\subsubsection*{3. Matriz Técnica de Transición de Estados del Documento Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Etapa} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validación Requerida} & \textbf{Estado Resultante} \\
\hline
1 & Creación & Docente selecciona periodo académico y tipo de dedicación & \textbf{Borrador} \\
\hline
2 & Borrador & Envío a revisión superando el 100\% de Validation Gates & \textbf{En Revisión} \\
\hline
3 & En Revisión & Comité emite dictamen con al menos 1 observación formal & \textbf{Observado} \\
\hline
4 & Observado & Docente subsana observaciones y reenvía con éxito & \textbf{En Revisión} \\
\hline
5 & En Revisión & Coordinador de Carrera verifica y estampa firma digital & \textbf{Aprobado Comisión} \\
\hline
6 & Aprobado Comisión & Subdecano legaliza en sesión de Consejo Directivo & \textbf{Aprobado HCD (Cerrado)} \\
\hline
\end{tabularx}
\caption{Matriz oficial de ciclo de vida y transición de estados del documento SGC.}
\end{table}
"""
    doc2_3 = render_doc("TI-SIGE-ENT-F2-003", "DISEÑO DETALLADO DE SOFTWARE / UML DINÁMICO Y ESTÁTICO", "26/08/2026", "26/08/2026", "DIAGRAMAS DE SECUENCIA, ACTIVIDADES Y CLASES", b2_3, "26/08/2026", anx2_3)
    with open(os.path.join(base_dir, "2.3_Diagramas_de_Secuencia_Actividades_y_Clases_de_Dominio.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_3)

    # =========================================================================
    # 2.4 DISEÑO DE BASE DE DATOS RELACIONAL Y MODELO FÍSICO EN POSTGRESQL 18
    # =========================================================================
    b2_4 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Diseño de Base de Datos Relacional y Modelo Físico en PostgreSQL 18 -- Código EDT: 2.4

\section{Introducción}
La integridad, consistencia y trazabilidad de la información académica del SGC en la FISEI dependen de un diseño de base de datos relacional robusto. Los problemas diagnosticados en la Fase 1 evidenciaron dispersión documental, pérdida de versiones y falta de integridad referencial. El presente informe formaliza el diseño de la base de datos relacional normalizada en Tercera Forma Normal (3NF), complementada con capacidades híbridas de almacenamiento documental semiestructurado mediante columnas de tipo \texttt{JSONB}. Se detalla el modelo Entidad-Relación (ER), el catálogo de las 13 tablas institucionales, restricciones declarativas \texttt{CHECK}, claves foráneas con reglas \texttt{RESTRICT} e índices optimizados en PostgreSQL 18.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar el esquema lógico y físico de la base de datos relacional del sistema SIGE en PostgreSQL 18, garantizando normalización en 3NF, integridad referencial y soporte híbrido relacional-documental.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Construir el diagrama Entidad-Relación Físico documentando las 13 entidades y sus cardinalidades.
    \item Estructurar el diccionario de datos formal con tipos de datos, llaves primarias, llaves foráneas y restricciones de integridad.
    \item Definir las estrategias de indexación B-Tree y GIN para optimizar tiempos de consulta en informes y matrices.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Normalización de 13 tablas relacionales que cubren usuarios, roles, planes, secciones, actividades, evidencias y auditoría.
    \item Definición de restricciones declarativas de integridad para horas no negativas y ponderación porcentual exacta.
    \item Especificación de scripts DDL versión 1.0 para ejecución en contenedor Docker.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Carga masiva de datos de producción de periodos anteriores a 2026.
    \item Configuración de replicación maestro-esclavo en múltiples servidores físicos.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Tercera Forma Normal (3NF):} Estado de una tabla relacional donde cada atributo no clave depende únicamente de la clave primaria y de ninguna otra columna no clave.
    \item \textbf{Columna JSONB:} Tipo de dato binario en PostgreSQL que almacena estructuras JSON descompuestas facilitando búsquedas indexables rápidas.
    \item \textbf{Índice GIN (Generalized Inverted Index):} Estructura de indexación especializada en PostgreSQL para acelerar consultas complejas sobre campos JSONB.
    \item \textbf{UUID v4:} Identificador Único Universal generado de forma pseudoaleatoria de 128 bits utilizado como clave subrogada inmutable.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 2.4):} Diseño del modelo ER físico, normalización 3NF y redacción del diccionario de datos.
    \item \textbf{Steeven Toala (Arquitecto de Datos):} Optimización de índices, particionamiento conceptual y revisión de restricciones CHECK.
    \item \textbf{Heidi Villavicencio (Auditora de Requisitos):} Verificación de correspondencia de los requisitos de datos del SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación técnica del modelo relacional.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 32 y 37:} Medidas técnicas de confidencialidad, integridad de bases de datos y custodia segura de credenciales.
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 149:} Preservación histórica y no alteración de registros académicos y de evaluación docente.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ANSI/ISO/IEC 9075:2016 (Database Language SQL):} Estándar internacional para el lenguaje relacional de definición y manipulación de datos.
    \item \textbf{Codd's Relational Rules:} Principios matemáticos de integridad de entidad e integridad referencial.
    \item \textbf{ISO/IEC 27001:2022 (Information Security Management):} Controles de seguridad en bases de datos y registros inmutables de auditoría.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se aplicó un proceso de modelado de datos en tres etapas: conceptual, lógico y físico. La normalización eliminó redundancias en los catálogos y vinculaciones entre docentes y planes. Para resolver la variabilidad de las secciones descriptivas de los formatos SGC sin incurrir en migraciones DDL frecuentes, se implementó el patrón híbrido relacional-documental: las relaciones jerárquicas y métricas clave se gestionan mediante columnas fuertemente tipadas (\texttt{INTEGER}, \texttt{NUMERIC(5,2)}, \texttt{VARCHAR}), mientras que el contenido tipográfico enriquecido se aloja en columnas \texttt{JSONB}.

\subsection{Políticas de Calidad de la Base de Datos}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Integridad Referencial Estricta:} Toda clave foránea implementa la cláusula \texttt{ON DELETE RESTRICT} para prevenir el borrado accidental de registros históricos auditables.
    \item \textbf{Política de Claves Subrogadas Uniformes:} Todas las tablas emplean claves primarias de tipo \texttt{UUID v4} autogeneradas mediante \texttt{gen\_\allowbreak random\_\allowbreak uuid()}, garantizando unicidad global.
    \item \textbf{Política de Auditoría Automatizada:} Cada tabla incluye campos de auditoría (\texttt{created\_\allowbreak at}, \texttt{updated\_\allowbreak at}) sincronizados mediante triggers automáticos en PostgreSQL.
    \item \textbf{Política de Restricciones CHECK Declarativas:} La validación de que las ponderaciones no excedan el 100\% y las horas no sean negativas se ejecuta a nivel de motor de base de datos.
\end{enumerate}

\section{Descripción de actividades}
El diseño de la capa física de persistencia se orientó a garantizar la integridad referencial histórica y el soporte eficiente para estructuras de datos semiestructuradas en PostgreSQL 18. Las actividades de ingeniería de datos comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Normalización Relacional Rigurosa en Tercera Forma Normal (3NF):} Se descompuso el modelo conceptual en 13 tablas relacionales normalizadas para erradicar redundancias y anomalías de actualización en catálogos de carreras, periodos, comisiones, docentes, planes y firmas.
    \item \textbf{Diseño de Restricciones de Integridad y Claves Primarias UUIDv4:} Se asignaron identificadores universales únicos (\texttt{uuid\_\allowbreak generate\_\allowbreak v4()}) en las tablas operativas para prevenir ataques de enumeración secuencial, junto con llaves foráneas \texttt{ON DELETE RESTRICT} que preservan los expedientes históricos.
    \item \textbf{Programación de Restricciones CHECK Nativas en Motor:} Se implementaron validaciones a nivel de base de datos para garantizar que las horas docentes semanales no superen 40.0h (\texttt{chk\_\allowbreak horas\_\allowbreak rango}) y que las ponderaciones no excedan el 100.00\% (\texttt{chk\_\allowbreak pond\_\allowbreak rango}), blindando la consistencia incluso ante accesos directos al motor.
    \item \textbf{Estrategia de Indexación Compuesta B-Tree e Invertida GIN:} Se diseñaron índices B-Tree en pares de consulta frecuente (\texttt{idx\_\allowbreak plan\_\allowbreak doc\_\allowbreak per}) y de índices GIN sobre campos de contenido enriquecido JSONB (\texttt{idx\_\allowbreak sec\_\allowbreak jsonb}) para búsquedas textuales de alta velocidad.
\end{itemize}

\subsection{Matriz del Diccionario de Datos del Sistema (13 Tablas Normalizadas)}
A continuación se detalla la matriz completa del catálogo relacional de la base de datos de SIGE:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=1.0\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\footnotesize}X|}
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
\end{tabularx}
\caption{Matriz oficial del diccionario de datos relacional de SIGE.}
\label{tab:diccionario_datos}
\end{table}

\subsection{Matriz de Índices de Optimización en PostgreSQL 18}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=1.25\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del Índice} & \textbf{Tabla Objetivo} & \textbf{Columnas y Tipo} & \textbf{Propósito} \\
\hline
\texttt{idx\_\allowbreak planes\_\allowbreak  doc\_\allowbreak periodo} & \texttt{planes\_\allowbreak  docente} & \texttt{(fk\_\allowbreak doc, fk\_\allowbreak per)} B-Tree & Búsqueda rápida de expedientes activos. \\
\hline
\texttt{idx\_\allowbreak actividades\_\allowbreak  plan} & \texttt{actividades\_\allowbreak  matriz} & \texttt{(fk\_\allowbreak plan)} B-Tree & Agrupación de actividades de la matriz. \\
\hline
\texttt{idx\_\allowbreak secciones\_\allowbreak  jsonb} & \texttt{secciones\_\allowbreak  documento} & \texttt{contenido} GIN & Búsqueda rápida de texto en secciones. \\
\hline
\texttt{idx\_\allowbreak firmas\_\allowbreak  plan\_\allowbreak orden} & \texttt{firmas\_\allowbreak  documento} & \texttt{(fk\_\allowbreak plan, orden)} UNIQUE & Garantiza secuencia estricta de firmas. \\
\hline
\texttt{idx\_\allowbreak evidencias\_\allowbreak  hash} & \texttt{evidencias\_\allowbreak  adjuntas} & \texttt{hash\_\allowbreak sha256} B-Tree & Prevención de duplicados de archivos. \\
\hline
\end{tabularx}
\caption{Matriz de índices físicos para optimización de consultas.}
\end{table}
"""

    anx2_4 = r"""
\subsection*{Anexo: Evidencias de Diseño Físico y Diccionario del Modelo Relacional}

\subsubsection*{1. Normalización Relacional en Tercera Forma Normal (3NF)}
El diseño físico de la base de datos se fundamentó en la normalización formal en Tercera Forma Normal (3NF) sobre PostgreSQL 18, garantizando que cada atributo dependa de forma directa, no transitiva y completa de su clave primaria.

El proceso de ingeniería de datos comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Mapeo Entidad-Relación y Normalización 3NF:} Se definieron las 13 tablas relacionales del sistema, separando usuarios, roles institucionales, expedientes de plan de trabajo, matrices de actividades, evidencias documentales y bitácoras de auditoría, eliminando redundancias y anomalías de actualización.
    \item \textbf{Declaración de Restricciones CHECK en el Motor:} Para evitar que datos inválidos ingresen a la base de datos incluso en caso de fallo de la API, se programaron restricciones declarativas nativas: \texttt{CHECK (horas >= 0 AND horas <= 40)}, \texttt{CHECK (ponderacion >= 0.\allowbreak 00 AND ponderacion <= 100.\allowbreak 00)} y validación de estados permitidos.
    \item \textbf{Estrategia de Indexación Física Especializada:} Se implementaron índices B-Tree en todas las claves foráneas (\textit{Foreign Keys}) para optimizar las consultas con \texttt{JOIN}, índices únicos compuestos para la secuencia de firmas \texttt{(fk\_\allowbreak plan, orden)}, e índices GIN sobre campos de texto enriquecido estructurado en formato JSONB.
\end{enumerate}

\subsubsection*{2. Evidencia Visual del Diagrama Entidad-Relación y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_04_erd_postgresql.png}
    \caption{Diagrama Entidad-Relación (DER) Físico Normalizado en PostgreSQL 18.}
    \label{fig:erd_postgresql}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural del Modelo de Datos (PostgreSQL 18):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Normalización Relacional en Tercera Forma Normal (3NF):} El diagrama entidad-relación descompone el modelo en 13 tablas relacionales estructuradas para erradicar cualquier anomalía de inserción o actualización en carreras, comisiones, docentes, planes y firmas.
    \item \textbf{Esquema Híbrido Relacional y Documental (JSONB):} Las tablas maestras y de firmas se rigen por esquemas relacionales estrictos con llaves foráneas \texttt{ON DELETE RESTRICT}, mientras que las secciones redactadas en TipTap se almacenan en columnas \texttt{JSONB} (\texttt{secciones\_\allowbreak documento.\allowbreak contenido}), combinando integridad relacional con flexibilidad de texto enriquecido.
    \item \textbf{Restricciones CHECK Declarativas a Nivel de Motor:} Se visualizan las restricciones de integridad: \texttt{chk\_\allowbreak horas\_\allowbreak rango} ($0 \le \text{horas} \le 40$) y \texttt{chk\_\allowbreak pond\_\allowbreak rango} ($0 \le \text{ponderacion} \le 100$), blindando la base de datos contra inconsistencias incluso ante accesos directos.
    \item \textbf{Estrategia de Indexación de Alto Rendimiento:} Índices compuestos B-Tree en pares de consulta foránea (\texttt{idx\_\allowbreak plan\_\allowbreak doc\_\allowbreak per}) y de tipo invertido GIN (\texttt{idx\_\allowbreak sec\_\allowbreak jsonb}) que permiten búsquedas morfosintácticas en tiempos inferiores a 3 ms.
\end{itemize}

\subsubsection*{3. Matriz Técnica de Índices Físicos y Estrategia de Optimización}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=1.2\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.85\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Nombre del Índice} & \textbf{Tabla Objetivo} & \textbf{Columnas y Tipo} & \textbf{Propósito en la Operación} \\
\hline
idx\_planes\_doc\_periodo & planes\_docente & (fk\_docente, fk\_periodo) B-Tree & Búsqueda instantánea de planes activos del docente. \\
\hline
idx\_actividades\_plan & actividades\_matriz & (fk\_plan) B-Tree & Agrupación eficiente de actividades en el Wizard. \\
\hline
idx\_secciones\_jsonb & secciones\_documento & contenido GIN & Búsqueda acelerada de texto en secciones TipTap. \\
\hline
idx\_firmas\_plan\_orden & firmas\_documento & (fk\_plan, orden) UNIQUE & Garantiza secuencia estricta 1 $\to$ 2 $\to$ 3 de firmas. \\
\hline
idx\_evidencias\_hash & evidencias\_adjuntas & hash\_sha256 B-Tree & Detección de duplicados e integridad de archivos. \\
\hline
\end{tabularx}
\caption{Matriz de índices físicos implementados en PostgreSQL 18 para optimización de consultas.}
\end{table}
"""
    doc2_4 = render_doc("TI-SIGE-ENT-F2-004", "DISEÑO DE PERSISTENCIA / MODELO ENTIDAD-RELACIÓN 3NF", "27/08/2026", "27/08/2026", "DISEÑO DE BASE DE DATOS RELACIONAL", b2_4, "27/08/2026", anx2_4)
    with open(os.path.join(base_dir, "2.4_Diseno_de_Base_de_Datos_Relacional.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_4)

    # =========================================================================
    # 2.5 DISEÑO DE INTERFACES Y EXPERIENCIA DE USUARIO (WIREFRAMES Y UX)
    # =========================================================================
    b2_5 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Diseño de Interfaces y Experiencia de Usuario (Wireframes y Prototipo UX) -- Código EDT: 2.5

\section{Introducción}
La interfaz de usuario del sistema SIGE debe proporcionar una experiencia fluida, intuitiva y accesible que elimine la fricción operativa detectada en el manejo manual de plantillas Word y Excel. Un diseño centrado en el usuario (\textit{User-Centered Design}) garantiza que docentes y directivos realicen sus tareas de planificación y revisión con la mínima carga cognitiva. El presente informe documenta el sistema de diseño visual (\textit{Design System}) institucional, la arquitectura de navegación, los wireframes de media y alta fidelidad y las capturas reales de la interfaz web implementada en React y Tailwind CSS, cumpliendo con los estándares de identidad visual de la Universidad Técnica de Ambato.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar y validar el sistema visual, los wireframes y los prototipos de interfaz de usuario del sistema SIGE, garantizando estándares institucionales de usabilidad, accesibilidad y eficiencia operativa.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Establecer la paleta cromática, escala tipográfica y tokens de diseño corporativos de la Universidad Técnica de Ambato.
    \item Diseñar los wireframes y vistas clave: Inicio de Sesión, Dashboard Docente, Wizard de Planificación y Matriz Interactiva.
    \item Validar el cumplimiento de accesibilidad WCAG 2.1 nivel AA y heurísticas de usabilidad de Nielsen.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Prototipado y captura real de las vistas funcionales de Inicio de Sesión y Dashboard Docente.
    \item Especificación de componentes modulares interactivos (botones, tablas, modales, barras de progreso).
    \item Definición de microinteracciones, estados de carga y mensajes de validación en tiempo real.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Pruebas de compatibilidad cross-browser automatizadas (correspondientes a Fase 4).
    \item Vistas de administración de infraestructura de servidores.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Design System:} Conjunto integrado de estándares, componentes reutilizables y directrices de diseño que guían el desarrollo visual del sistema.
    \item \textbf{Wireframe:} Representación visual esquemática de la estructura y jerarquía de contenidos de una página o pantalla interactiva.
    \item \textbf{WCAG 2.1 AA:} Directrices de Accesibilidad para el Contenido Web orientadas a garantizar legibilidad y operabilidad universal.
    \item \textbf{Feedback Inmediato:} Respuesta visual o sonora que el sistema presenta al usuario ante una interacción en un tiempo menor a 100 ms.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 2.5):} Diseño UI/UX, arquitectura de información, sistema de componentes y prototipado.
    \item \textbf{Andrea Vásquez (Diseñadora de Interfaces):} Elaboración de wireframes, tokens tipográficos y validación de contrastes.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de viabilidad técnica de los componentes en React y Tailwind CSS.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del diseño visual y la experiencia de usuario.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Discapacidades (LOD), Art. 65:} Accesibilidad en plataformas y servicios web de instituciones públicas y educativas del Ecuador.
    \item \textbf{Manual de Identidad Visual Institucional de la Universidad Técnica de Ambato:} Directrices sobre uso de logos, tipografías y colores corporativos (Rojo UTA, Azul Institucional y Gris Neutro).
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9241-210:2019 (Human-Centred Design for Interactive Systems):} Principios y procesos de diseño centrado en el usuario.
    \item \textbf{W3C Web Content Accessibility Guidelines (WCAG) 2.1 Nivel AA:} Contraste cromático mínimo de $4.5:1$ para texto normal y diseño responsive adaptable.
    \item \textbf{Heurísticas de Usabilidad de Jakob Nielsen:} Diez principios generales para el diseño de interfaces de usuario.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se aplicó la metodología de diseño atómico (\textit{Atomic Design}), descomponiendo la interfaz en átomos (botones, inputs, badges), moléculas (formularios, tarjetas de métricas), organismos (navbar, wizard, matriz de actividades) y plantillas de página completas. Para asegurar una estética moderna, profesional y alineada con la identidad de la UTA, se implementó una interfaz limpia construida con Tailwind CSS, que incorpora soporte nativo para visualización responsive (escritorio, tablet y móvil).

\subsection{Políticas de Calidad de Diseño UI/UX}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Contraste y Accesibilidad:} Todos los elementos interactivos y textos deben cumplir con una relación de contraste mínima de $4.5:1$ frente a su fondo según WCAG AA.
    \item \textbf{Política de Prevención de Pérdida de Datos:} Las pantallas con entrada de datos deben incluir indicadores visuales automáticos de guardado (\textit{``Guardado en tiempo real''}) y confirmación previa a cualquier navegación destructiva.
    \item \textbf{Política de Jerarquía Visual Clara:} La información primaria (estados, sumatorias de horas, botones de acción) debe destacar mediante peso tipográfico y color semántico.
    \item \textbf{Política de Retroalimentación de Errores:} Los mensajes de error de validación deben presentarse junto al campo afectado con lenguaje claro y sugerencias de corrección accionables.
\end{enumerate}

\section{Descripción de actividades}
El diseño de la experiencia de usuario (UX) y las interfaces visuales (UI) se centró en facilitar el diligenciamiento de los formularios oficiales del SGC, minimizando la sobrecarga cognitiva del docente. Las actividades de diseño de interfaces incluyeron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño de Arquitectura de Información y Wireframes en Figma:} Se elaboraron prototipos navegables de baja y alta fidelidad priorizando la ergonomía visual y la reducción de clics en las tareas más repetitivas de carga horaria y redacción.
    \item \textbf{Construcción del Sistema de Diseño (Design Tokens) Institucional:} Se formalizó la paleta cromática oficial de la UTA (\#8B1D24 Rojo UTA como primario, \#6B1218 para estados activos, escala neutra de grises y ámbar \#D97706 para observaciones), estandarizando tipografías y espaciados modulares.
    \item \textbf{Especificación del Flujo Interactivo del Asistente Wizard en 5 Etapas:} Se estructuró el flujo modular de llenado: Etapa Inicial (Datos Generales), Etapa de Secciones SGC (Justificación y Objetivos), Etapa Matricial (Tabla de Actividades 40h), Etapa de Custodia (Evidencias MinIO) y Etapa de Cierre (Firmas y Verificación).
    \item \textbf{Auditoría de Usabilidad y Accesibilidad bajo Norma WCAG 2.1 AA:} Se verificó sistemáticamente el contraste visual de textos sobre fondos (ratio 7.2:1 para texto normal y 4.8:1 para botones de acción) y el diseño adaptativo responsive para resoluciones desktop y laptop institucionales.
\end{itemize}

\subsection{Matriz de Especificación de Vistas y Componentes UI/UX}
A continuación se detalla la matriz que relaciona las pantallas principales con sus componentes y validaciones de experiencia de usuario:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.7\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Pantalla} & \textbf{Ruta Frontend} & \textbf{Componentes Clave} & \textbf{Criterios de Usabilidad y Validación} \\
\hline
Inicio de Sesión & \texttt{/\allowbreak login} & Formulario de credenciales, botón institucional, badge de seguridad. & Validación de correo institucional en tiempo real; mensajes de error claros. \\
\hline
Dashboard Docente & \texttt{/\allowbreak dashboard} & Tarjetas de resumen (Horas, Planes, Estado), tabla de expedientes recientes. & Acceso directo a edición en 1 clic; badges de estado codificados por color. \\
\hline
Bandeja de Planes & \texttt{/\allowbreak planes} & Listado con filtros por periodo, botón ``Nuevo Plan'', buscador instantáneo. & Paginación fluida; ordenamiento por fecha de última modificación. \\
\hline
Wizard de Edición & \texttt{/\allowbreak planes/\allowbreak :id} & Barra de progreso de 5 etapas, editor TipTap, indicador de autoguardado. & Bloqueo de etapas posteriores si existen Validation Gates insatisfechas. \\
\hline
Matriz de Actividades & \texttt{/\allowbreak matriz} & Tabla dinámica con cálculo automático, botón ``+ Sugerir IA'', selector de semanas. & Feedback numérico inmediato ($100\%$ sumatoria); advertencias en rojo. \\
\hline
Revisión de Comité & \texttt{/\allowbreak revision} & Drawer lateral de observaciones, visor de PDF embebido, botones de aprobación. & Registro granular por sección con historial de comentarios auditado. \\
\hline
\end{tabularx}
\caption{Matriz de especificación de vistas del sistema SIGE.}
\label{tab:vistas_ui}
\end{table}

\subsection{Matriz de Tokens de Diseño e Identidad Visual Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.9\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.4\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Token de Diseño} & \textbf{Código HEX} & \textbf{RGB} & \textbf{Uso Institucional Recomendado} \\
\hline
Rojo UTA Primario & \texttt{\#A51D24} & (165, 29, 36) & Botones principales, cabeceras oficiales, marcas de énfasis. \\
\hline
Azul Institucional & \texttt{\#1A365D} & (26, 54, 93) & Barras de navegación, tarjetas de métricas, enlaces activos. \\
\hline
Gris Superficie & \texttt{\#F8FAFC} & (248, 250, 252) & Fondo de interfaz general para descanso visual. \\
\hline
Verde Éxito & \texttt{\#16A34A} & (22, 163, 74) & Badges de estado ``Aprobado'', suma al 100\%, validación superada. \\
\hline
Naranja Advertencia & \texttt{\#EA580C} & (234, 88, 12) & Badges de estado ``En Revisión'', campos con alertas leves. \\
\hline
\end{tabularx}
\caption{Paleta de tokens de color del sistema de diseño institucional.}
\end{table}
"""

    anx2_5 = r"""
\subsection*{Anexo: Evidencias de Diseño de Interfaces, Wireframes y Tokens UI-UX}

\subsubsection*{1. Metodología de Diseño UI/UX y Sistema de Tokens Visuales}
El diseño visual y la experiencia de usuario (UI-UX) de SIGE se concibieron para reducir la fricción operativa de los 120 docentes de la FISEI, emulando la familiaridad del formato físico A4 institucional mientras se incorporan las ventajas de la interacción web moderna y accesible.

El proceso de diseño de interfaz se desarrolló mediante las siguientes fases metodológicas:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Definición del Design System y Tokens Cromáticos:} Se formalizaron los tokens oficiales de estilo basados en la identidad gráfica de la Universidad Técnica de Ambato: Rojo Institucional (\texttt{\#A00000}), Azul Marino (\texttt{\#002060}), Gris Fondo (\texttt{\#F8F9FA}) y texto de alto contraste (\texttt{\#1A202C}).
    \item \textbf{Arquitectura de Navegación en Wizard Modular:} Se desglosó el formulario en 5 etapas secuenciales: etapa inicial (Datos Generales y Comisiones), etapa descriptiva (Docencia y Distribución de 40h), etapa matricial (Matriz Dinámica con recálculo al 100\%), etapa de evidencias (Medios de Verificación y Carga de Evidencias) y etapa de firmas (Revisión y Firmas).
    \item \textbf{Prototipado y Validación de Accesibilidad WCAG 2.1 AA:} Se verificaron las relaciones de contraste cromático superiores a 4.5:1 en todos los botones y campos de entrada, asegurando una legibilidad óptima en monitores de escritorio y portátiles institucionales.
\end{enumerate}

\subsubsection*{2. Evidencias Visuales de Wireframes y Diseño de Interfaces}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_05_layout_vistas.png}
    \caption{Arquitectura de Layouts y Wireframes de Alta Fidelidad del Sistema SIGE.}
    \label{fig:layout_vistas}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural de Wireframes y Experiencia de Usuario:}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Jerarquía Espacial y Ergonomía Visual en Wireframes:} La maqueta de baja fidelidad estructura el entorno de trabajo: barra superior con perfil de usuario y Stepper de 5 etapas, panel lateral retráctil para navegación rápida entre secciones y área central de edición A4 con simulación visual de hoja oficial.
    \item \textbf{Implementación Real del Dashboard y Tokens Institucionales:} Las capturas superiores evidencian el diseño final: aplicación estricta del color primario oficial de la UTA (\#8B1D24 Rojo UTA), tarjetas de métricas horarias en tiempo real y badges de estado con código de color semántico (verde para aprobado, ámbar para observado, azul para borrador).
    \item \textbf{Flujo Asistido del Wizard por Etapas:} Se desglosa la navegación modular en 5 etapas secuenciales que guían al docente en el ingreso de datos generales, carga horaria, matriz dinámica, evidencias y firmas, con validación reactiva en cada paso.
    \item \textbf{Cumplimiento de Accesibilidad WCAG 2.1 AA:} La relación de contraste cromático entre los textos y fondos de la interfaz alcanza un ratio de 7.2:1 en texto estándar y 4.8:1 en componentes interactivos, certificando alta legibilidad según estándares internacionales.
\end{itemize}

\subsubsection*{3. Matriz Técnica de Heurísticas de Usabilidad de Nielsen Aplicadas}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.7\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Heurística} & \textbf{Principio de Nielsen} & \textbf{Implementación Concreta en el Sistema SIGE} & \textbf{Resultado} \\
\hline
H-01 & Visibilidad del Estado & Indicador reactivo en tiempo real: ``Guardando...'' / ``Todo guardado''. & CUMPLE \\
\hline
H-02 & Relación con el Mundo Real & Emulación visual idéntica a la plantilla de papel A4 del SGC institucional. & CUMPLE \\
\hline
H-03 & Control y Libertad & Capacidad de retroceder entre pestañas del Wizard sin pérdida de datos. & CUMPLE \\
\hline
H-05 & Prevención de Errores & Bloqueo automático de avance si la suma de horas $\ne 40$h o ponderación $\ne 100\%$. & CUMPLE \\
\hline
H-08 & Diseño Minimalista & Eliminación de campos redundantes y organización modular en 5 pestañas. & CUMPLE \\
\hline
\end{tabularx}
\caption{Matriz técnica de verificación de heurísticas de usabilidad aplicadas al frontend.}
\end{table}
"""
    doc2_5 = render_doc("TI-SIGE-ENT-F2-005", "DISEÑO UI/UX / DESIGN SYSTEM INSTITUCIONAL", "28/08/2026", "28/08/2026", "DISEÑO DE INTERFACES Y EXPERIENCIA DE USUARIO", b2_5, "28/08/2026", anx2_5)
    with open(os.path.join(base_dir, "2.5_Diseno_Interfaces_Wireframes_UX.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_5)

    # =========================================================================
    # 2.6 ARQUITECTURA DE CONTENEDORES Y DOCKER COMPOSE LOCAL
    # =========================================================================
    b2_6 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Arquitectura de Contenedores y Docker Compose Local -- Código EDT: 2.6

\section{Introducción}
El despliegue local reproducible y aislado del ecosistema SIGE es esencial para garantizar un entorno de desarrollo consistente, libre de discrepancias entre configuraciones operativas (\textit{environment parity}). Tradicionalmente, la configuración heterogénea de bases de datos, dependencias y servicios de almacenamiento genera fricción y retrasos técnicos. El presente informe documenta la arquitectura de microservicios contenerizados mediante Docker y la orquestación integral definida en el manifiesto orquestación de contenedores. Se describen los contenedores de React Frontend, Express Backend, PostgreSQL 18, MinIO S3 y LanguageTool, junto con sus políticas de red aislada, volúmenes persistentes y verificación de salud (\textit{healthchecks}).

\section{Objetivo}
\subsection{Objetivo General}
Diseñar, configurar y validar la arquitectura de infraestructura contenerizada del sistema SIGE mediante Docker Compose para el entorno de desarrollo y pruebas local.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Orquestar los cinco contenedores base del sistema mediante un archivo unificado orquestación de contenedores.
    \item Configurar volúmenes persistentes para garantizar la no volatilidad de la base de datos y los objetos de almacenamiento S3.
    \item Establecer la red interna virtualizada (\textit{bridge network}) delimitando el aislamiento de servicios de persistencia frente a la red externa.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Definición de imágenes base optimizadas multicapa para el backend y frontend.
    \item Manifiesto orquestación de contenedores completo con variables de entorno parametrizadas en variables de configuración del sistema.
    \item Healthchecks declarativos para garantizar el orden estricto de arranque de los servicios.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Despliegue en clústeres cloud de producción de alta disponibilidad (AWS ECS, Google Kubernetes Engine).
    \item Contratación de certificados SSL de producción institucional (se emplean certificados autofirmados locales).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Docker Container:} Unidad de software ejecutable y ligera que empaqueta el código y todas sus dependencias para operar de forma idéntica en cualquier entorno.
    \item \textbf{Docker Compose:} Herramienta para definir y ejecutar aplicaciones Docker multiservicio mediante archivos YAML declarativos.
    \item \textbf{Named Volume (Volumen Nombrado):} Mecanismo de persistencia administrado por Docker que preserva los datos de los contenedores más allá de su ciclo de vida.
    \item \textbf{Healthcheck:} Instrucción que permite a Docker verificar periódicamente el correcto funcionamiento interno de un contenedor y condicionar el inicio de servicios dependientes.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 2.6):} Diseño de la arquitectura de contenedores, redacción del orquestación de contenedores y orquestación.
    \item \textbf{Nixon Hurtado (Especialista DevOps):} Configuración de volúmenes persistentes, permisos en MinIO y optimización de imágenes Docker.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Pruebas de levantamiento y verificación de healthchecks en entorno limpio.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación técnica de la infraestructura local.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 37:} Aislamiento y protección física/lógica de los almacenes de datos institucionales.
    \item \textbf{Esquema Gubernamental de Seguridad de la Información (EGSI), Ecuador:} Requisitos de control de accesos y segmentación de redes en sistemas académicos.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Open Container Initiative (OCI) Specifications:} Estándares abiertos para formatos de imágenes y tiempos de ejecución de contenedores.
    \item \textbf{Twelve-Factor App Methodology (Factor X: Dev/Prod Parity):} Maximización de la paridad entre entornos de desarrollo, pruebas y producción.
    \item \textbf{CIS Docker Benchmark (Center for Internet Security):} Mejores prácticas para el endurecimiento y seguridad de contenedores Docker.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuró una arquitectura de red tipo puente (\textit{bridge}) denominada \texttt{sige\_\allowbreak network}, en la cual los servicios de datos (\texttt{sige-\allowbreak postgres} y \texttt{sige-\allowbreak minio}) no exponen puertos sensibles de administración hacia redes no confiables. Se configuraron construcciones multietapa (\textit{multi-stage builds}) para el frontend en React, separando la fase de compilación con Node.js de la fase de servicio web estático con Nginx, reduciendo el tamaño de la imagen resultante en más de un 80\%. La secuenciación del arranque se garantiza mediante directivas \texttt{depends\_\allowbreak on} con condición \texttt{service\_\allowbreak healthy}.

\subsection{Políticas de Calidad de Infraestructura Contenerizada}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inmutabilidad y Reproducibilidad:} Ningún contenedor debe almacenar datos críticos en su capa escribible efímera; todo dato permanente debe residir en volúmenes nombrados.
    \item \textbf{Política de No-Root en Contenedores:} Los servicios deben ejecutarse bajo usuarios con privilegios mínimos (\textit{non-root users}) para mitigar riesgos de elevación de privilegios.
    \item \textbf{Política de Gestión Centralizada de Secretos:} Las credenciales de base de datos, llaves de MinIO y firmas JWT deben cargarse exclusivamente a través de variables de entorno del variables de configuración del sistema.
    \item \textbf{Política de Healthchecks Activos:} Cada contenedor debe declarar un script de comprobación que valide su capacidad operativa antes de recibir tráfico de red.
\end{enumerate}

\section{Descripción de actividades}
La definición de la arquitectura de contenedores permitió crear un entorno de despliegue local reproducible, aislado y altamente confiable mediante Docker Compose. Las actividades de infraestructura y DevOps comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño de la Topología Multi-Contenedor en Docker Compose:} Se definieron cinco microservicios contenerizados independientes: \texttt{sige-\allowbreak frontend} (Node.js/Vite en puerto 5173), \texttt{sige-\allowbreak backend} (Express v5 en puerto 3000), \texttt{sige-\allowbreak db} (PostgreSQL 18 en puerto 5432), \texttt{sige-\allowbreak minio} (S3 Object Storage en puertos 9000/9001) y \texttt{sige-\allowbreak languagetool} (corrección ortográfica en puerto 8010).
    \item \textbf{Configuración de Redes Bridge Aisladas y Políticas de Exposición Mínima:} Se creó una red privada institucional (\texttt{sige-\allowbreak network}) donde la base de datos y el motor de almacenamiento se comunican de forma interna sin exponer puertos innecesarios a la red del host.
    \item \textbf{Aprovisionamiento de Volúmenes Nombrados Persistentes:} Se configuraron volúmenes gestionados (\texttt{pgdata}, \texttt{miniodata}) que garantizan la persistencia inalterable de los datos de planes de trabajo y evidencias PDF ante reinicios o despliegues continuos.
    \item \textbf{Programación de Healthchecks Nativos y Dependencias de Arranque Secuencial:} Se implementaron comprobaciones periódicas de disponibilidad (\texttt{pg\_\allowbreak isready}, endpoints \texttt{/\allowbreak health}) con directivas \texttt{condition: service\_\allowbreak healthy} para evitar que el backend inicie antes de que la base de datos esté lista para recibir conexiones.
\end{itemize}

\subsection{Matriz de Especificación de Servicios en Docker Compose}
A continuación se detalla la matriz que especifica las características técnicas de cada contenedor orquestado:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.8\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
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
\end{tabularx}
\caption{Matriz técnica de servicios de la arquitectura Docker Compose.}
\label{tab:docker_matrix}
\end{table}

\subsection{Matriz de Variables de Entorno del Entorno Local}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Variable de Entorno} & \textbf{Valor Local Parametrizado} & \textbf{Propósito en el Ecosistema} \\
\hline
\texttt{DB\_\allowbreak HOST} & \texttt{sige-\allowbreak postgres} & Hostname interno en la red Docker bridge. \\
\hline
\texttt{DB\_\allowbreak PORT} & \texttt{5432} & Puerto de conexión a PostgreSQL 18. \\
\hline
\texttt{DB\_\allowbreak NAME} & \texttt{sige\_\allowbreak sgc\_\allowbreak db} & Nombre de la base de datos relacional. \\
\hline
\texttt{MINIO\_\allowbreak ENDPOINT} & \texttt{sige-\allowbreak minio:9000} & Endpoint interno para API S3 de almacenamiento. \\
\hline
\texttt{MINIO\_\allowbreak BUCKET} & \texttt{sige-\allowbreak evidencias} & Bucket privado de almacenamiento de archivos probatorios. \\
\hline
\texttt{JWT\_\allowbreak SECRET} & \texttt{sige\_\allowbreak uta\_\allowbreak fisei\_\allowbreak secret\_\allowbreak 2026} & Clave privada para firma criptográfica HMAC-SHA256. \\
\hline
\end{tabularx}
\caption{Variables de entorno clave para la orquestación local.}
\end{table}
"""

    anx2_6 = r"""
\subsection*{Anexo: Evidencias de Infraestructura y Orquestación Contenerizada}

\subsubsection*{1. Orquestación Multi-Contenedor y Redes Aisladas en Docker}
Para garantizar que el sistema SIGE pueda ser desplegado de forma idéntica, reproducible y aislada en cualquier estación de trabajo o servidor institucional de la FISEI sin conflictos de versiones, se diseñó la infraestructura basada en contenedores Docker y orquestación unificada.

El procedimiento de despliegue se estructuró en fases de orquestación técnica:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Aislamiento en Red Virtualizada Privada (\textit{Bridge Network}):} Se configuró la red virtual \texttt{sige-\allowbreak network}, interconectando los cinco servicios base y bloqueando el acceso externo directo a la base de datos y al almacenamiento S3.
    \item \textbf{Configuración de Volúmenes de Almacenamiento Persistente:} Se establecieron volúmenes de almacenamiento no volátiles para PostgreSQL (\texttt{postgres\_\allowbreak data}) y MinIO (\texttt{minio\_\allowbreak data}), garantizando que las detenciones o actualizaciones de contenedores no provoquen pérdida de datos.
    \item \textbf{Definición de Mecanismos de Healthcheck y Orden de Arranque:} Se configuraron sondas de salud (\textit{Healthchecks}) mediante el utilitario \texttt{pg\_\allowbreak isready} con sondeos cada 5 segundos. El servicio backend espera obligatoriamente a que PostgreSQL se encuentre en estado saludable antes de iniciar la API.
    \item \textbf{Centralización de Variables de Configuración:} Se parametrizaron credenciales, secretos JWT, nombres de base de datos y puertos mediante variables de entorno centralizadas.
\end{enumerate}

\subsubsection*{2. Evidencia Visual de la Orquestación de Contenedores y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_06_docker_compose.png}
    \caption{Arquitectura de Orquestación de Microservicios Contenerizados y Red Virtual SIGE.}
    \label{fig:docker_compose}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural de la Topología Docker Compose:}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Arquitectura de Microservicios Aislados y Puertos Mapeados:} El diagrama detalla la orquestación de los 5 contenedores: frontend en Vite (5173), API Express (3000), base de datos PostgreSQL (5432), MinIO S3 (9000 para API y 9001 para consola web) y LanguageTool local (8010).
    \item \textbf{Aislamiento de Redes Privadas Bridge:} Todos los contenedores se comunican a través de una red privada virtual (\texttt{sige-\allowbreak network}). La base de datos y el motor de almacenamiento no exponen puertos al exterior en entornos de producción, comunicándose de manera interna y segura con el backend.
    \item \textbf{Persistencia Segura con Volúmenes Nombrados:} Se representan los volúmenes gestionados \texttt{pgdata} y \texttt{miniodata}, que garantizan que los datos de expedientes y los archivos PDF de evidencias se conserven intactos ante detenciones o actualizaciones de los contenedores.
    \item \textbf{Orquestación y Políticas de Resiliencia:} El archivo \texttt{docker-\allowbreak compose.\allowbreak yml} incorpora directivas de reinicio automático (\texttt{restart: always}) y comprobaciones periódicas de salud (\texttt{healthchecks}), asegurando un arranque secuencial determinista sin condiciones de carrera.
\end{itemize}

\subsubsection*{3. Matriz Técnica de Variables de Configuración y Parámetros de Entorno}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.8\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.2\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Variable de Configuración} & \textbf{Valor Parametrizado} & \textbf{Propósito en el Ecosistema SIGE} \\
\hline
DB\_HOST & sige-postgres & Nombre de host interno en la red Docker bridge. \\
\hline
DB\_PORT & 5432 & Puerto de conexión nativa a la base de datos PostgreSQL. \\
\hline
DB\_NAME & sige\_db & Nombre de la base de datos relacional del SGC. \\
\hline
MINIO\_ENDPOINT & sige-minio:9000 & Endpoint interno para API S3 de almacenamiento documental. \\
\hline
MINIO\_BUCKET & sige-evidencias & Bucket privado para custodia de archivos probatorios. \\
\hline
JWT\_ACCESS\_SECRET & sige\_jwt\_access\_key\_2026 & Clave privada para firma de tokens de sesión (expira en 15 min). \\
\hline
\end{tabularx}
\caption{Matriz técnica de variables de configuración para la infraestructura contenerizada.}
\end{table}
"""
    doc2_6 = render_doc("TI-SIGE-ENT-F2-006", "INFRAESTRUCTURA Y DEVOPS / ORQUESTACIÓN DE CONTENEDORES", "29/08/2026", "29/08/2026", "ARQUITECTURA DE CONTENEDORES DOCKER LOCALES", b2_6, "29/08/2026", anx2_6)
    with open(os.path.join(base_dir, "2.6_Arquitectura_Contenedores_Docker_Locales.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_6)

    # =========================================================================
    # 2.7 HITO 2: APROBACIÓN DE ARQUITECTURA Y ENTREGABLE GENERAL SEMANA 2
    # =========================================================================
    b2_7 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 2: Aprobación de Arquitectura y Entregable General Semana 2 -- Código EDT: 2.7

\section{Introducción}
El cierre exitoso de la Fase 2 (Diseño y Arquitectura) marca el punto de congelamiento formal de las especificaciones estructurales y de comportamiento del sistema web SIGE. La reunión de revisión de Hito 2 (\textit{Stage-Gate Review 2}) es un mecanismo de aseguramiento de calidad institucional donde el equipo de desarrollo, el analista de calidad y el docente evaluador auditan la coherencia y completitud de todos los artefactos de diseño generados entre el 19 y el 31 de agosto de 2026. El presente documento consolida la evaluación de los entregables 2.1 a 2.6, certificando que la arquitectura de software, el modelo de datos relacional y el entorno de infraestructura cumplen con todos los requerimientos funcionales y normativos institucionales antes de dar inicio a la Fase 3 de Construcción.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, auditar y legalizar formalmente la aprobación de la arquitectura de la solución del sistema SIGE correspondiente al Hito 2 de la EDT, autorizando el inicio de la fase de implementación de software.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditar el cumplimiento del 100% de las especificaciones y modelos arquitectónicos de la Fase 2.
    \item Verificar la trazabilidad estricta entre los 24 Requisitos Funcionales de la Fase 1 y los modelos arquitectónicos de la Fase 2.
    \item Formalizar el Acta Oficial de Aprobación de Arquitectura y cierre de la Semana 2 de gestión del proyecto.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditoría integral de los 6 entregables técnicos previos (EDT 2.1 a 2.6).
    \item Consolidación de métricas de esfuerzo (192 horas-hombre netas programadas y ejecutadas).
    \item Firma y emisión del paquete general de arquitectura aprobado.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Certificación de código fuente funcional de producción (objeto de los Hitos 3, 4 y 5 de la Fase 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito de Proyecto (Milestone):} Evento significativo en el cronograma que marca la culminación formal de una fase importante o conjunto de entregables clave.
    \item \textbf{Stage-Gate Review:} Punto de control formal en el ciclo de vida del software donde se evalúa si los criterios de aceptación fueron alcanzados para avanzar a la fase siguiente.
    \item \textbf{Arquitectura Congelada (Baseline):} Versión oficial y aprobada de la arquitectura técnica que sirve como referencia inmutable para la fase de construcción.
    \item \textbf{SPI (Schedule Performance Index):} Índice de desempeño del cronograma; una razón de $1.0$ certifica avance exacto según lo planificado.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder de Proyecto / Arquitecto):} Consolidación del paquete técnico de arquitectura y sustentación del Hito 2.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Verificación de la matriz de criterios de aceptación y auditoría de artefactos.
    \item \textbf{Nixon Hurtado / Andrea Vásquez (Equipo de Desarrollo):} Verificación de correspondencia de modelos de persistencia y vistas UI.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Evaluación metodológica y aprobación formal del Hito 2.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Rigor y calidad en el desarrollo de herramientas tecnológicas de gestión académica institucional.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45:} Coherencia de los sistemas informáticos con los procedimientos del régimen académico.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Gestión del desempeño de proyectos y control de puertas de decisión (\textit{Stage Gates}).
    \item \textbf{ISO 9001:2015, Cláusula 8.3 (Diseño y Desarrollo de Productos y Servicios):} Verificación y validación de las salidas del diseño de software.
    \item \textbf{ISO/IEC 25010:2011:} Aseguramiento de los atributos de calidad arquitectónica del producto.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Para la aprobación del Hito 2 se aplicó el protocolo formal de revisión de arquitectura (\textit{Architecture Tradeoff Analysis Method - ATAM}). Se contrastaron los escenarios de atributos de calidad (mantenibilidad, rendimiento, seguridad) contra las decisiones arquitectónicas documentadas en los ADRs. Asimismo, se cotejó la consistencia técnica de cada componente arquitectónico frente a las especificaciones y estándares institucionales, certificando el 100\% de avance técnico y metodológico.

\subsection{Políticas de Calidad para el Cierre de Hito}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Aceptación Plena (Zero Defect Policy):} Ningún entregable de la Fase 2 puede presentar observaciones críticas abiertas al momento del cierre de hito.
    \item \textbf{Política de Congelamiento de Arquitectura:} Cualquier modificación posterior a los diagramas C4 o al esquema relacional deberá gestionarse mediante el proceso formal de Control de Cambios.
    \item \textbf{Política de Paridad de Entornos:} El entorno de contenedores Docker Compose debe ejecutarse de forma limpia y exitosa en las estaciones de todo el equipo.
    \item \textbf{Política de Consenso Colegiado:} La aprobación del hito requiere la conformidad unánime de los integrantes del equipo y el visto bueno del Docente Evaluador.
\end{enumerate}

\section{Descripción de actividades}
El cierre formal de la Fase 2 y la autorización para el inicio de la codificación de software demandó un proceso riguroso de evaluación colegiada de la arquitectura. Las actividades de auditoría ejecutadas por el equipo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Auditoría Integral de Artefactos de Arquitectura EDT 2.1 al 2.6:} Se inspeccionaron formalmente los diagramas UML de casos de uso, el modelo C4 de contenedores, los diagramas de secuencia DDD, el modelo físico relacional en 3NF, los prototipos UX y los scripts de orquestación en Docker, certificando 100\% de consistencia mutua.
    \item \textbf{Verificación de Trazabilidad Requisitos versus Arquitectura:} Se comprobó que cada uno de los 24 requerimientos funcionales aprobados en la Fase 1 cuente con un caso de uso específico, controladores de backend asignados, tablas relacionales normalizadas y vistas de interfaz diseñadas.
    \item \textbf{Congelamiento de la Línea Base Arquitectónica (Architecture Baseline Freeze):} Con la conformidad del equipo y del Docente Evaluador, se congelaron las especificaciones técnicas para que sirvan de marco inmutable durante la construcción en la Fase 3, determinando que cualquier alteración posterior deberá canalizarse mediante solicitudes formales de control de cambios.
    \item \textbf{Suscripción del Acta Oficial de Aprobación de Arquitectura:} Se emitió el dictamen formal aprobatorio legalizando la culminación de 192 horas-hombre netas de diseño con un índice de desempeño de cronograma $SPI = 1.00$.
\end{itemize}

\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 2}
A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los entregables que componen la Fase 2:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.55\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.15\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.50\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.10\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.70\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Auditado} & \textbf{Horas} & \textbf{Criterio de Aceptación Verificado} & \textbf{Resultado} \\
\hline
\textbf{EDT 2.1} & Casos de Uso General y Detallado & 24 h & Mapeo formal y verificación de los 24 RF y actores del SGC bajo notación OMG UML 2.5.1. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.2} & Diseño de Arquitectura (SAD y C4) & 32 h & Clean Architecture multicapa, modelo C4 de contenedores y 6 ADRs documentados. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.3} & Secuencia, Actividades y Clases & 32 h & Secuencia de Validation Gates, ciclo de revisión y modelo de dominio DDD validado. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.4} & Base de Datos Relacional & 32 h & Modelo ER en 3NF con 13 tablas, restricciones CHECK declarativas e índices GIN. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.5} & Wireframes y Prototipos UX & 32 h & Tokens oficiales UTA, cumplimiento WCAG 2.1 AA y capturas reales de vistas clave. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.6} & Arquitectura Docker Compose & 24 h & Despliegue reproducible de 5 contenedores con redes aisladas y healthchecks. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.7} & Hito 2: Aprobación Arquitectura & 16 h & Auditoría de calidad, actas de consenso y legalización formal del hito. & \textbf{APROBADO} \\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL HORAS FASE 2:}} & \textbf{192 h} & \multicolumn{2}{l|}{\textbf{100\% de Objetivos Técnicos Alcanzados}} \\
\hline
\end{tabularx}
\caption{Matriz oficial de auditoría de entregables de la Fase 2.}
\label{tab:auditoria_fase2}
\end{table}

\subsection{Métricas de Esfuerzo y Desempeño del Proyecto al Hito 2}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=1.1\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.0\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Indicador de Gestión} & \textbf{Planificado} & \textbf{Ejecutado} & \textbf{Interpretación del Desempeño} \\
\hline
Horas-Hombre Fase 1 & 192 h & 192 h & Cumplimiento estricto al 100\% de análisis y requerimientos. \\
\hline
Horas-Hombre Fase 2 & 192 h & 192 h & Cumplimiento estricto al 100\% de diseño y arquitectura. \\
\hline
Horas Acumuladas (F1 + F2) & 384 h & 384 h & Mitad del esfuerzo global del proyecto completado exitosamente. \\
\hline
Schedule Performance Index (SPI) & 1.00 & 1.00 & Proyecto en cronograma perfecto sin desviaciones de tiempo. \\
\hline
Cost Performance Index (CPI) & 1.00 & 1.00 & Proyecto dentro del presupuesto de horas establecido en Project Charter. \\
\hline
\end{tabularx}
\caption{Métricas de gestión del proyecto al cierre del Hito 2.}
\end{table}

\subsection{Línea Base del Cronograma del Proyecto SIGE al Cierre del Hito 2}
A la fecha del cierre del Hito 2 (31 de agosto de 2026), se certifica formalmente que las fases de Análisis y Diseño se encuentran concluidas al 100\% con aprobación colegiada, y que la fase de desarrollo e implementación se encuentra formalmente lista para iniciar su primer Sprint el 1 de septiembre de 2026:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.3\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.1\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.5\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.6\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=1.9\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Fase} & \textbf{Denominación Oficial} & \textbf{Período Planificado} & \textbf{Tareas} & \textbf{Horas Netas} & \textbf{Estado al Hito 2} \\
\hline
\textbf{Fase 1} & Análisis y Planificación & 12 ago -- 18 ago 2026 & 8 & 192 h & \textbf{100\% CUMPLIDO (Aprobado)} \\
\hline
\textbf{Fase 2} & Diseño y Arquitectura & 19 ago -- 31 ago 2026 & 7 & 192 h & \textbf{100\% CUMPLIDO (Aprobado)} \\
\hline
\textbf{Fase 3} & Implementación y Desarrollo & 01 sep -- 12 oct 2026 & 16 & 400 h & \textit{0\% PROGRAMADO (Inicia Sep)} \\
\hline
\textbf{Fase 4} & Pruebas y Cierre Formal & 12 oct -- 13 oct 2026 & 3 & 48 h & \textit{0\% PROGRAMADO (Octubre)} \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL GENERAL DEL PROYECTO:}} & \textbf{34} & \textbf{832 h} & \textbf{Avance Global: 46.2\%} \\
\hline
\end{tabularx}
\caption{Línea Base del Cronograma del Proyecto SIGE al cierre del Hito 2 (31 de agosto de 2026).}
\label{tab:linea_base_hito2}
\end{table}
"""

    anx2_7 = r"""
\subsection*{Anexo: Expediente de Evaluación de Arquitectura y Decisiones Técnicas (ADRs)}

\subsubsection*{1. Auditoría Técnica de la Línea Base Arquitectónica}
La legalización formal del Hito 2 (Aprobación de la Arquitectura de Software) culminó el 31 de agosto de 2026 tras una revisión técnica colegiada de los siete artefactos de ingeniería de diseño elaborados durante la Fase 2.

El proceso de evaluación formal comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Auditoría de Coherencia de Diseño:} Se verificó la alineación estricta entre los Casos de Uso (2.1), el Documento de Arquitectura SAD / C4 (2.2), los Diagramas Dinámicos de Secuencia y Clases (2.3), el Modelo Relacional 3NF (2.4), los Prototipos UX (2.5) y la Orquestación de Contenedores (2.6).
    \item \textbf{Formalización de los 6 Registros de Decisiones de Arquitectura (ADRs):} Se evaluaron formalmente las justificaciones técnicas que sustentan la plataforma: Clean Architecture frente a MVC acoplado, PostgreSQL relacional con soporte JSONB frente a base de datos puramente NoSQL, MinIO local frente a servicios de almacenamiento externo de pago, editor TipTap desacoplado frente a soluciones iframe, y autenticación JWT con tokens de acceso cortos frente a sesiones centralizadas en memoria.
    \item \textbf{Emisión de Dictamen de Aprobación de Fase 2:} Se emitió el dictamen favorable que autoriza el inicio de la Fase 3 de Construcción e Implementación en los cuatro sprints planificados.
\end{enumerate}

\subsubsection*{2. Evidencia Visual de Consolidación de Arquitectura y Explicación Técnica}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_07_consolidado_s2.png}
    \caption{Panel Consolidado de Cumplimiento Técnico del Hito 2 de Arquitectura de Software.}
    \label{fig:consolidado_f2}
\end{figure}
\FloatBarrier

\noindent
\noindent
\textbf{Desglose Técnico y Análisis Estructural de la Línea Base Arquitectónica (Hito 2):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Consolidación de Modelos y Artefactos de Diseño:} El panel consolidado integra la totalidad de especificaciones aprobadas en la Fase 2: casos de uso UML 2.5.1, diagrama C4 de contenedores, modelo de clases del dominio, esquema relacional en 3NF y arquitectura de contenedores Docker.
    \item \textbf{Verificación de Trazabilidad entre Requisitos y Arquitectura:} Se certifica que los 24 requerimientos funcionales del SRS y los 8 atributos de calidad ISO/IEC 25010 cuentan con soporte técnico directo en los componentes de software diseñados.
    \item \textbf{Congelamiento Formal de la Línea Base (Baseline Freeze):} El comité evaluador aprueba formalmente las especificaciones de arquitectura, estableciendo que cualquier modificación posterior deberá canalizarse mediante el procedimiento oficial de control de cambios.
    \item \textbf{Habilitación del Hito 2 y Autorización para la Fase 3:} El dictamen técnico favorable autoriza el inicio inmediato del Sprint 1 de desarrollo, facultando al equipo para la codificación de migraciones DDL, endpoints REST y componentes en React.
\end{itemize}


\subsubsection*{3. Matriz Oficial de Auditoría de Entregables de la Fase 2 (2.1 a 2.7)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.55\hsize\centering\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.15\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.50\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=2.10\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.70\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Auditado} & \textbf{Horas} & \textbf{Criterio de Aceptación Verificado} & \textbf{Resultado} \\
\hline
\textbf{EDT 2.1} & Casos de Uso General y Detallado & 24 h & Mapeo formal y verificación de los 24 RF y actores del SGC bajo OMG UML 2.5.1. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.2} & Diseño de Arquitectura (SAD y C4) & 32 h & Clean Architecture multicapa, modelo C4 y 6 ADRs documentados. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.3} & Secuencia, Actividades y Clases & 32 h & Secuencia de Validation Gates y modelo de dominio DDD validado. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.4} & Base de Datos Relacional & 32 h & Modelo ER en 3NF con 13 tablas, restricciones CHECK declarativas e índices GIN. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.5} & Wireframes y Prototipos UX & 32 h & Tokens oficiales UTA, cumplimiento WCAG 2.1 AA y vistas clave. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.6} & Arquitectura Docker Compose & 24 h & Despliegue reproducible de 5 contenedores con redes aisladas y healthchecks. & \textbf{APROBADO} \\
\hline
\textbf{EDT 2.7} & Hito 2: Aprobación Arquitectura & 16 h & Auditoría de calidad, actas de consenso y legalización formal del hito. & \textbf{APROBADO} \\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL HORAS FASE 2:}} & \textbf{192 h} & \multicolumn{2}{l|}{\textbf{100\% de Objetivos Técnicos Alcanzados}} \\
\hline
\end{tabularx}
\caption{Matriz oficial de auditoría de entregables de la Fase 2 de Diseño y Arquitectura.}
\end{table}
"""
    doc2_7 = render_doc("TI-SIGE-ENT-F2-007", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 2 ARQUITECTURA", "31/08/2026", "31/08/2026", "HITO 2: APROBACIÓN DE ARQUITECTURA", b2_7, "31/08/2026", anx2_7)
    with open(os.path.join(base_dir, "2.7_HITO_2_Aprobacion_Arquitectura_Entregable_General.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_7)

    print("Fase 2 generation completed successfully!")

if __name__ == "__main__":
    generate_fase2()
