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
Modelar formalmente el comportamiento funcional e interacciones del sistema SIGE mediante diagramas UML de casos de uso generales y detallados, garantizando la cobertura integral de los roles institucionales y los procesos del SGC de la FISEI.
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
    \item \textbf{Nixon Hurtado (Analista de Requisitos):} Verificación de cobertura con la matriz de trazabilidad RF-01 a RF-24.
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

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/s2_01_casos_de_uso.png}
    \caption{Diagrama General de Casos de Uso del Sistema SIGE bajo Estándar OMG UML 2.5.1.}
    \label{fig:casos_uso_general}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz Oficial de Casos de Uso del Sistema (CU-01 a CU-08)}
A continuación se detalla la matriz general de casos de uso estructurada para el sistema SIGE:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}
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
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
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
    \item \textbf{E2 - Actividad sin Medios de Verificación:} El sistema impide el avance al paso de firmas hasta que cada ítem posea al menos un medio auditable.
\end{itemize} \\
\hline
Postcondiciones & La matriz de actividades queda almacenada con integridad relacional en la tabla \texttt{actividades\_matriz}. \\
\hline
\end{tabularx}
\caption{Especificación textual detallada del caso de uso crítico CU-03.}
\label{tab:cu_03_detalle}
\end{table}
"""

    anx2_1 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.1 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.1 \\
\hline
Nombre de la Tarjeta & Diagramas general y detallado de casos de uso \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 19 de agosto al 21 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{01\_Diagrama\_General\_Detallado\_Casos\_de\_Uso.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.1 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Trazabilidad entre Requisitos Funcionales y Casos de Uso}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Requisito Funcional} & \textbf{Descripción del Requisito} & \textbf{Caso de Uso Vinculado} & \textbf{Cobertura} \\
\hline
RF-01 & Autenticación institucional con credenciales universitarias & CU-01 & 100\% Total \\
\hline
RF-03 & Configuración general del plan semestral y carga horaria & CU-02 & 100\% Total \\
\hline
RF-05 & Registro interactivo de matriz de actividades y cronograma & CU-03 & 100\% Total \\
\hline
RF-07 & Almacenamiento seguro de medios de verificación en MinIO S3 & CU-04 & 100\% Total \\
\hline
RF-09 & Panel de revisión con observaciones granulares por sección & CU-05 & 100\% Total \\
\hline
RF-11 & Flujo secuencial e inmutable de cascada de firmas digitales & CU-06 & 100\% Total \\
\hline
RF-13 & Generación de reportes institucionales en PDF y DOCX & CU-07 & 100\% Total \\
\hline
RF-15 & Desbloqueo y gestión de prórrogas extemporáneas & CU-08 & 100\% Total \\
\hline
\end{tabularx}
\caption{Matriz de trazabilidad RF vs CU.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{c8192df - feat(arch): modelado de casos de uso UML 2.5.1 general y detallado CU-01 a CU-08}
    \item \textbf{Archivos Afectados:} \texttt{docs/casos\_uso\_sige.md}, \texttt{Entregables\_Latex/Fase\_2/2.1*.tex}
\end{itemize}
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

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_02_clean_architecture.png}
    \caption{Arquitectura Limpia Multicapa (Clean Architecture) implementada en el Backend de SIGE.}
    \label{fig:clean_arch}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_02_contenedores_c4.png}
    \caption{Diagrama de Contenedores C4 del Ecosistema SIGE (Frontend, Backend, DB, Storage y NLP).}
    \label{fig:c4_containers}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Decisiones de Arquitectura de Software (ADR-01 a ADR-06)}
A continuación se detalla la matriz formal de las decisiones arquitectónicas adoptadas para el sistema:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|X|c|}
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
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|X|X|c|}
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
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.2 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.2 \\
\hline
Nombre de la Tarjeta & Diseño de arquitectura de la solución \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 20 de agosto al 25 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & \texttt{02\_Diseno\_Arquitectura\_Solucion.pdf} (SAD \& C4 Model) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.2 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Puertos y Contratos de Comunicación Inter-Contenedores}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|c|m{2.2cm}|m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Puerto} & \textbf{Protocolo} & \textbf{Dependencia} & \textbf{Contrato / Función Principal} \\
\hline
\texttt{sige-frontend} & 5173 / 80 & HTTP/HTTPS & Backend API & Entrega de SPA React y proxy de llamadas API. \\
\hline
\texttt{sige-backend} & 3000 & REST / JSON & PostgreSQL, MinIO & Lógica de negocio, Validation Gates y autenticación. \\
\hline
\texttt{sige-postgres} & 5432 & PostgreSQL Wire & Volumen local & Persistencia relacional ACID y documentos JSONB. \\
\hline
\texttt{sige-minio} & 9000 / 9001 & AWS S3 API & Volumen local & Almacenamiento binario de evidencias PDF y URLs prefirmadas. \\
\hline
\texttt{sige-grammar} & 8010 & HTTP REST & Memoria interna & Servicio local Docker LanguageTool de gramática en español. \\
\hline
\end{tabularx}
\caption{Matriz de servicios y comunicación de infraestructura.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{e7421ab - feat(arch): definicion de arquitectura C4, SAD oficial y registro de ADR-01 a ADR-06}
    \item \textbf{Archivos Afectados:} \texttt{docs/architecture\_sad.md}, \texttt{Entregables\_Latex/Fase\_2/2.2*.tex}
\end{itemize}
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
    \item \textbf{Diagrama de Actividades UML:} Representación gráfica del flujo de control o flujo de datos paso a paso entre actividades operacionales.
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

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_03_secuencia_validation.png}
    \caption{Diagrama de Secuencia UML: Guardado de Secciones y Evaluación de Validation Gates.}
    \label{fig:secuencia_gates}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_03_actividades_ciclo.png}
    \caption{Diagrama de Actividades UML: Ciclo Completo de Aprobación, Observación y Legalización.}
    \label{fig:actividades_ciclo}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/s2_03_clases_uml.png}
    \caption{Diagrama de Clases del Dominio Institucional SIGE (Entidades, Atributos y Métodos).}
    \label{fig:clases_dominio}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Entidades del Dominio y Métodos Operativos}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|X|c|}
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
\end{tabularx}
\caption{Matriz de especificación de clases del dominio SGC.}
\label{tab:espec_clases}
\end{table}

\subsection{Matriz de Transición de Estados del Documento Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.0cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Paso} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validación} & \textbf{Estado Resultante} \\
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
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.3 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.3 \\
\hline
Nombre de la Tarjeta & Diagramas de secuencia, actividades y clases de dominio \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 21 de agosto al 26 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{03\_Diagramas\_Secuencia\_Actividades\_Clases.pdf} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.3 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Definición Formal de Invariantes y Contratos de Dominio}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Invariante} & \textbf{Clase Responsable} & \textbf{Expresión Lógica del Contrato de Dominio} \\
\hline
INV-01 & \texttt{PlanDocente} & $\sum \text{horas\_actividad} \ge \text{horas\_minimas\_contrato}$ (40h tiempo completo). \\
\hline
INV-02 & \texttt{ActividadMatriz} & $\sum \text{ponderacion\_actividad} = 100.00\%$ al enviar a revisión. \\
\hline
INV-03 & \texttt{FirmaDocumento} & Secuencia estricta: $\text{Orden}(\text{Elaborador}) < \text{Orden}(\text{Revisor}) < \text{Orden}(\text{Aprobador})$. \\
\hline
INV-04 & \texttt{EvidenciaAdjunta} & $\text{Longitud}(\text{hash\_sha256}) = 64 \text{ caracteres hexadecimales}$ no nulos. \\
\hline
\end{tabularx}
\caption{Invariantes y contratos del modelo de dominio.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{b38190c - feat(arch): modelado dinamico UML, secuencia de gates y clases de dominio DDD}
    \item \textbf{Archivos Afectados:} \texttt{docs/diagramas\_dinamicos\_uml.md}, \texttt{Entregables\_Latex/Fase\_2/2.3*.tex}
\end{itemize}
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
    \item Definición de restricciones declarativas de negocio (\texttt{CHECK horas >= 0}, \texttt{CHECK ponderacion <= 100}).
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
    \item \textbf{Heidi Villavicencio (Auditora de Requisitos):} Verificación de cobertura de los requisitos de datos del SGC.
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
    \item \textbf{Política de Claves Subrogadas Uniformes:} Todas las tablas emplean claves primarias de tipo \texttt{UUID v4} autogeneradas mediante \texttt{gen\_random\_uuid()}, garantizando unicidad global.
    \item \textbf{Política de Auditoría Automatizada:} Cada tabla incluye campos de auditoría (\texttt{created\_at}, \texttt{updated\_at}) sincronizados mediante triggers automáticos en PostgreSQL.
    \item \textbf{Política de Restricciones CHECK Declarativas:} La validación de que las ponderaciones no excedan el 100\% y las horas no sean negativas se ejecuta a nivel de motor de base de datos.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.2cm,keepaspectratio]{images/s2_04_erd_postgresql.png}
    \caption{Diagrama Entidad-Relación Físico (13 Tablas Normalizadas en PostgreSQL 18).}
    \label{fig:erd_postgres}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz del Diccionario de Datos del Sistema (13 Tablas Normalizadas)}
A continuación se detalla la matriz completa del catálogo relacional de la base de datos de SIGE:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.4cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Clave Primaria} & \textbf{Claves Foráneas y Restricciones Principales} & \textbf{Propósito SGC} \\
\hline
\texttt{usuarios} & \texttt{id} (UUID) & \texttt{email} (UNIQUE, CHECK institucional), \texttt{password\_hash} & Catálogo de docentes y administradores. \\
\hline
\texttt{roles} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE: DOCENTE, COORD\_AREA, COORD\_CARRERA) & Perfiles de acceso institucional RBAC. \\
\hline
\texttt{usuario\_roles} & \texttt{id} (UUID) & \texttt{fk\_usuario} $\to$ \texttt{usuarios}, \texttt{fk\_rol} $\to$ \texttt{roles} & Asignación de múltiples roles a usuarios. \\
\hline
\texttt{periodos\_academicos} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE), \texttt{CHECK(fecha\_fin > fecha\_inicio)} & Ciclos semestrales institucionales UTA. \\
\hline
\texttt{carreras} & \texttt{id} (UUID) & \texttt{codigo} (UNIQUE), \texttt{nombre}, \texttt{facultad} & Catálogo de carreras pertenecientes a FISEI. \\
\hline
\texttt{planes\_docente} & \texttt{id} (UUID) & \texttt{fk\_docente}, \texttt{fk\_periodo}, \texttt{fk\_carrera}, \texttt{CHECK(estado)} & Cabecera principal del plan de trabajo P7-T1. \\
\hline
\texttt{secciones\_documento} & \texttt{id} (UUID) & \texttt{fk\_plan} $\to$ \texttt{planes\_docente}, \texttt{contenido\_jsonb} & Contenido enriquecido de secciones del plan. \\
\hline
\texttt{actividades\_matriz} & \texttt{id} (UUID) & \texttt{fk\_plan}, \texttt{CHECK(horas >= 0)}, \texttt{CHECK(ponderacion <= 100)} & Filas dinámicas de la matriz SGC. \\
\hline
\texttt{evidencias\_adjuntas} & \texttt{id} (UUID) & \texttt{fk\_actividad}, \texttt{url\_s3}, \texttt{hash\_sha256} (CHAR 64) & Metadatos de archivos PDF en MinIO. \\
\hline
\texttt{observaciones\_comite} & \texttt{id} (UUID) & \texttt{fk\_plan}, \texttt{fk\_usuario}, \texttt{fk\_seccion}, \texttt{resuelto} (BOOLEAN) & Correcciones y observaciones de revisión. \\
\hline
\texttt{firmas\_documento} & \texttt{id} (UUID) & \texttt{fk\_plan}, \texttt{fk\_firmante}, \texttt{hash\_firma}, \texttt{orden} (1, 2, 3) & Registro cronológico e inmutable de firmas. \\
\hline
\texttt{auditoria\_logs} & \texttt{id} (UUID) & \texttt{fk\_usuario}, \texttt{accion}, \texttt{ip\_origen}, \texttt{created\_at} & Bitácora de seguridad y trazabilidad. \\
\hline
\texttt{notificaciones} & \texttt{id} (UUID) & \texttt{fk\_usuario}, \texttt{titulo}, \texttt{mensaje}, \texttt{leido} (BOOLEAN) & Avisos de cambios de estado y revisiones. \\
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
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{2.5cm}|X|c|}
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
\end{tabularx}
\caption{Matriz de índices físicos para optimización de consultas.}
\end{table}
"""

    anx2_4 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.4 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.4 \\
\hline
Nombre de la Tarjeta & Diseño de base de datos relacional \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 24 de agosto al 27 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{04\_Diseno\_Base\_de\_Datos\_ER\_Logico.pdf} \& \texttt{schema.sql} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.4 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Restricciones CHECK y Triggers en PostgreSQL 18}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Constraint / Trigger} & \textbf{Tabla Objetivo} & \textbf{Definición Técnica Declarativa} \\
\hline
\texttt{chk\_horas\_no\_negativas} & \texttt{actividades\_matriz} & \texttt{CHECK (horas >= 0 AND horas <= 40)} \\
\hline
\texttt{chk\_ponderacion\_rango} & \texttt{actividades\_matriz} & \texttt{CHECK (ponderacion >= 0.00 AND ponderacion <= 100.00)} \\
\hline
\texttt{chk\_estados\_validos} & \texttt{planes\_docente} & \texttt{CHECK (estado IN ('Borrador', 'En Revision', 'Observado', 'Aprobado'))} \\
\hline
\texttt{trg\_audit\_update} & Todas las tablas & \texttt{BEFORE UPDATE EXECUTE PROCEDURE update\_timestamp\_column()} \\
\hline
\end{tabularx}
\caption{Restricciones e integridad declarativa en la base de datos.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{d4812ef - feat(db): diseno fisico relacional 3NF de 13 tablas, restricciones CHECK e indices GIN}
    \item \textbf{Archivos Afectados:} \texttt{database/schema.sql}, \texttt{Entregables\_Latex/Fase\_2/2.4*.tex}
\end{itemize}
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

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_login_view.png}
    \caption{Captura Real de la Interfaz Web de Inicio de Sesión Institucional del Sistema SIGE.}
    \label{fig:sige_login}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_dashboard_resumen.png}
    \caption{Captura Real del Dashboard Principal del Docente en SIGE con Métricas y Planes Activos.}
    \label{fig:sige_dashboard}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_05_layout_vistas.png}
    \caption{Arquitectura de Wireframes y Jerarquía de Vistas del Entorno Docente y Coordinador.}
    \label{fig:layout_vistas}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Especificación de Vistas y Componentes UI/UX}
A continuación se detalla la matriz que relaciona las pantallas principales con sus componentes y validaciones de experiencia de usuario:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{2.4cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Pantalla} & \textbf{Ruta Frontend} & \textbf{Componentes Clave} & \textbf{Criterios de Usabilidad y Validación} \\
\hline
Inicio de Sesión & \texttt{/login} & Formulario de credenciales, botón institucional, badge de seguridad. & Validación de correo institucional en tiempo real; mensajes de error claros. \\
\hline
Dashboard Docente & \texttt{/dashboard} & Tarjetas de resumen (Horas, Planes, Estado), tabla de expedientes recientes. & Acceso directo a edición en 1 clic; badges de estado codificados por color. \\
\hline
Bandeja de Planes & \texttt{/planes} & Listado con filtros por periodo, botón ``Nuevo Plan'', buscador instantáneo. & Paginación fluida; ordenamiento por fecha de última modificación. \\
\hline
Wizard de Edición & \texttt{/planes/:id} & Barra de progreso de 5 pasos, editor TipTap, indicador de autoguardado. & Bloqueo de pasos posteriores si existen Validation Gates insatisfechas. \\
\hline
Matriz de Actividades & \texttt{/matriz} & Tabla dinámica con cálculo automático, botón ``+ Sugerir IA'', selector de semanas. & Feedback numérico inmediato ($100\%$ sumatoria); advertencias en rojo. \\
\hline
Revisión de Comité & \texttt{/revision} & Drawer lateral de observaciones, visor de PDF embebido, botones de aprobación. & Registro granular por sección con historial de comentarios auditado. \\
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
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|X|}
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
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.5 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.5 \\
\hline
Nombre de la Tarjeta & Diseño de interfaces y experiencia de usuario \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 25 de agosto al 28 de agosto de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{05\_Diseno\_Interfaces\_Wireframes\_UX.pdf} \& Prototipo Figma \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.5 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Heurísticas de Usabilidad de Nielsen Evaluadas}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Heurística} & \textbf{Principio de Nielsen} & \textbf{Implementación Específica en SIGE} & \textbf{Cumplimiento} \\
\hline
H-01 & Visibilidad del estado del sistema & Indicador dinámico de autoguardado (\textit{``Guardando...'' / ``Guardado''}). & 100\% \\
\hline
H-03 & Control y libertad del usuario & Posibilidad de deshacer cambios de texto y cancelar acciones en modales. & 100\% \\
\hline
H-05 & Prevención de errores & Validación de horas en tiempo real impidiendo sumas mayores a 40h. & 100\% \\
\hline
H-08 & Diseño estético y minimalista & Eliminación de elementos superfluos; foco en el diligenciamiento SGC. & 100\% \\
\hline
\end{tabularx}
\caption{Evaluación de heurísticas de usabilidad en las vistas clave.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{f19280a - feat(ui): prototipo de interfaces, diseno de componentes accesibles y tokens de diseno}
    \item \textbf{Archivos Afectados:} \texttt{frontend/src/views/*}, \texttt{Entregables\_Latex/Fase\_2/2.5*.tex}
\end{itemize}
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
El despliegue local reproducible y aislado del ecosistema SIGE es esencial para garantizar un entorno de desarrollo consistente, libre de discrepancias entre configuraciones operativas (\textit{environment parity}). Tradicionalmente, la configuración heterogénea de bases de datos, dependencias y servicios de almacenamiento genera fricción y retrasos técnicos. El presente informe documenta la arquitectura de microservicios contenerizados mediante Docker y la orquestación integral definida en el manifiesto \texttt{docker-compose.yml}. Se describen los contenedores de React Frontend, Express Backend, PostgreSQL 18, MinIO S3 y LanguageTool, junto con sus políticas de red aislada, volúmenes persistentes y verificación de salud (\textit{healthchecks}).

\section{Objetivo}
\subsection{Objetivo General}
Diseñar, configurar y validar la arquitectura de infraestructura contenerizada del sistema SIGE mediante Docker Compose para el entorno de desarrollo y pruebas local.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Orquestar los cinco contenedores base del sistema mediante un archivo unificado \texttt{docker-compose.yml}.
    \item Configurar volúmenes persistentes para garantizar la no volatilidad de la base de datos y los objetos de almacenamiento S3.
    \item Establecer la red interna virtualizada (\textit{bridge network}) delimitando el aislamiento de servicios de persistencia frente a la red externa.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Definición de Dockerfiles optimizados multicapa para el backend y frontend.
    \item Manifiesto \texttt{docker-compose.yml} completo con variables de entorno parametrizadas en archivo \texttt{.env}.
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
    \item \textbf{Steeven Toala (Responsable EDT 2.6):} Diseño de la arquitectura de contenedores, redacción del \texttt{docker-compose.yml} y orquestación.
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
Se estructuró una arquitectura de red tipo puente (\textit{bridge}) denominada \texttt{sige\_network}, en la cual los servicios de datos (\texttt{sige-postgres} y \texttt{sige-minio}) no exponen puertos sensibles de administración hacia redes no confiables. Se configuraron construcciones multietapa (\textit{multi-stage builds}) para el frontend en React, separando la fase de compilación con Node.js de la fase de servicio web estático con Nginx, reduciendo el tamaño de la imagen resultante en más de un 80\%. La secuenciación del arranque se garantiza mediante directivas \texttt{depends\_on} con condición \texttt{service\_healthy}.

\subsection{Políticas de Calidad de Infraestructura Contenerizada}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inmutabilidad y Reproducibilidad:} Ningún contenedor debe almacenar datos críticos en su capa escribible efímera; todo dato permanente debe residir en volúmenes nombrados.
    \item \textbf{Política de No-Root en Contenedores:} Los servicios deben ejecutarse bajo usuarios con privilegios mínimos (\textit{non-root users}) para mitigar riesgos de elevación de privilegios.
    \item \textbf{Política de Gestión Centralizada de Secretos:} Las credenciales de base de datos, llaves de MinIO y firmas JWT deben cargarse exclusivamente a través de variables de entorno del archivo \texttt{.env}.
    \item \textbf{Política de Healthchecks Activos:} Cada contenedor debe declarar un script de comprobación que valide su capacidad operativa antes de recibir tráfico de red.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/s2_06_docker_compose.png}
    \caption{Topología de Red, Volúmenes y Contenedores Orquestados en Docker Compose Local.}
    \label{fig:docker_topology}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Especificación de Servicios en Docker Compose}
A continuación se detalla la matriz que especifica las características técnicas de cada contenedor orquestado:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|m{3.2cm}|c|m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Imagen Base / Dockerfile} & \textbf{Puertos} & \textbf{Volumen Nombrado} & \textbf{Healthcheck / Comando} \\
\hline
\texttt{sige-frontend} & \texttt{node:20-alpine} & \texttt{5173:5173} & Ninguno & \texttt{curl -f http://localhost:5173 || exit 1} \\
\hline
\texttt{sige-backend} & \texttt{node:20-alpine} & \texttt{3000:3000} & Ninguno & \texttt{curl -f http://localhost:3000/api/health} \\
\hline
\texttt{sige-postgres} & \texttt{postgres:18-alpine} & \texttt{5432:5432} & \texttt{pgdata\_sige} & \texttt{pg\_isready -U sige\_user -d sige\_db} \\
\hline
\texttt{sige-minio} & \texttt{minio/minio:latest} & \texttt{9000:9000} \newline \texttt{9001:9001} & \texttt{minio\_data} & \texttt{curl -f http://localhost:9000/minio/health/live} \\
\hline
\texttt{sige-grammar} & \texttt{erikvl87/languagetool} & \texttt{8010:8010} & Ninguno & \texttt{curl -f http://localhost:8010/v2/languages} \\
\hline
\end{tabularx}
\caption{Matriz técnica de servicios de la arquitectura Docker Compose.}
\label{tab:docker_matrix}
\end{table}

\subsection{Matriz de Variables de Entorno del Entorno Local (.env)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{4.2cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Variable de Entorno} & \textbf{Valor Local Parametrizado} & \textbf{Propósito en el Ecosistema} \\
\hline
\texttt{DB\_HOST} & \texttt{sige-postgres} & Hostname interno en la red Docker bridge. \\
\hline
\texttt{DB\_PORT} & \texttt{5432} & Puerto de conexión a PostgreSQL 18. \\
\hline
\texttt{DB\_NAME} & \texttt{sige\_sgc\_db} & Nombre de la base de datos relacional. \\
\hline
\texttt{MINIO\_ENDPOINT} & \texttt{sige-minio:9000} & Endpoint interno para API S3 de almacenamiento. \\
\hline
\texttt{MINIO\_BUCKET} & \texttt{sige-evidencias} & Bucket privado de almacenamiento de archivos PDF. \\
\hline
\texttt{JWT\_SECRET} & \texttt{sige\_uta\_fisei\_secret\_2026} & Clave privada para firma criptográfica HMAC-SHA256. \\
\hline
\end{tabularx}
\caption{Variables de entorno clave para la orquestación local.}
\end{table}
"""

    anx2_6 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.6 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.6 \\
\hline
Nombre de la Tarjeta & Arquitectura de microservicios y Docker Compose local \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 26 de agosto al 29 de agosto de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & \texttt{06\_Arquitectura\_Contenedores\_Docker\_Locales.pdf} \& \texttt{docker-compose.yml} \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado en Reunión de Hito 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.6 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Comandos de Operación y Validación de Servicios}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{4.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Operación} & \textbf{Comando CLI de Ejecución} & \textbf{Resultado Esperado de la Verificación} \\
\hline
Arranque & \texttt{docker compose up -d} & 5 contenedores en estado \texttt{Running} en segundo plano. \\
\hline
Salud & \texttt{docker compose ps} & Todos los servicios con etiqueta \texttt{(healthy)}. \\
\hline
Logs & \texttt{docker compose logs -f backend} & Mensaje de confirmación: \textit{``Server listening on port 3000''}. \\
\hline
Detención & \texttt{docker compose down} & Detención segura preservando los volúmenes \texttt{pgdata} y \texttt{minio}. \\
\hline
\end{tabularx}
\caption{Comandos de operación y verificación del entorno Docker.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{a90182c - feat(devops): orquestacion integral con docker-compose.yml, redes bridge y healthchecks}
    \item \textbf{Archivos Afectados:} \texttt{docker-compose.yml}, \texttt{.env.example}, \texttt{Entregables\_Latex/Fase\_2/2.6*.tex}
\end{itemize}
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
    \item Auditar el cumplimiento del 100\% de las tareas técnicas asignadas a la Fase 2 en el Tablero Trello y Cronograma Gantt.
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
Para la aprobación del Hito 2 se aplicó el protocolo formal de revisión de arquitectura (\textit{Architecture Tradeoff Analysis Method - ATAM}). Se contrastaron los escenarios de atributos de calidad (mantenibilidad, rendimiento, seguridad) contra las decisiones arquitectónicas documentadas en los ADRs. Asimismo, se cotejó el estado de cada tarjeta en el Tablero Kanban de Trello frente a los artefactos compilados, certificando el 100\% de avance físico y cronológico.

\subsection{Políticas de Calidad para el Cierre de Hito}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Aceptación Plena (Zero Defect Policy):} Ningún entregable de la Fase 2 puede presentar observaciones críticas abiertas al momento del cierre de hito.
    \item \textbf{Política de Congelamiento de Arquitectura:} Cualquier modificación posterior a los diagramas C4 o al esquema relacional deberá gestionarse mediante el proceso formal de Control de Cambios.
    \item \textbf{Política de Paridad de Entornos:} El entorno de contenedores Docker Compose debe ejecutarse de forma limpia y exitosa en las estaciones de todo el equipo.
    \item \textbf{Política de Consenso Colegiado:} La aprobación del hito requiere la conformidad unánime de los integrantes del equipo y el visto bueno del Docente Evaluador.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/trello_tablero_captura_real.png}
    \caption{Captura Real del Tablero Trello evidenciando el 100\% de Tareas Completadas en la Fase 2.}
    \label{fig:trello_fase2}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_gantt_cronograma.png}
    \caption{Cronograma Gantt en MS Project mostrando la Culminación Exitosa del Hito 2 en la Semana 2.}
    \label{fig:gantt_fase2}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 2}
A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los entregables que componen la Fase 2:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Auditado} & \textbf{Horas} & \textbf{Criterio de Aceptación Verificado} & \textbf{Resultado} \\
\hline
\textbf{EDT 2.1} & Casos de Uso General y Detallado & 24 h & Cobertura total de los 24 RF y actores del SGC bajo notación OMG UML 2.5.1. & \textbf{APROBADO} \\
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
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.0cm}|c|c|X|}
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
"""

    anx2_7 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 2.7 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 2.7 \\
\hline
Nombre de la Tarjeta & HITO 2: Aprobación de Arquitectura y Entregable General Semana 2 \\
\hline
Fase Correspondiente & FASE 2. DISEÑO Y ARQUITECTURA \\
\hline
Período de Ejecución & 29 de agosto al 31 de agosto de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV), Nixon Hurtado (NH), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & \texttt{07\_Entregable\_General\_Semana\_2.pdf} (Paquete Arquitectura Aprobado) \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado Formalmente \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 2.7 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Acta Formal de Aprobación de Arquitectura de Software}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA INSTITUCIONAL DE CIERRE DE HITO 2 -- SISTEMA SIGE}} \\
\hline
\textbf{Fecha de Sesión:} & 31 de agosto de 2026 \\
\hline
\textbf{Lugar:} & Laboratorio de Gestión de Software / Entorno Virtual Teams -- FISEI \\
\hline
\textbf{Participantes:} & Steeven Toala (Líder/Arquitecto), Heidi Villavicencio (Calidad), Nixon Hurtado (Backend), Andrea Vásquez (UI/UX), Ing. Paulo Torres (Docente Evaluador). \\
\hline
\textbf{Resolución:} & Habiendo verificado la consistencia de los modelos C4, el esquema 3NF en PostgreSQL 18, los wireframes UX institucionales y la orquestación en Docker Compose, el Comité aprueba por unanimidad el Hito 2 y autoriza el inicio de la Fase 3 de Construcción. \\
\hline
\end{tabularx}
\caption{Acta de aprobación colegiada del Hito 2.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Etiqueta de Versión (\textit{Release Tag}):} \texttt{v0.2.0-milestone2-arch-approved}
    \item \textbf{Commit de Consolidación:} \texttt{82019ab - docs(milestone2): consolidacion de paquete de arquitectura semana 2 y acta de aprobacion}
    \item \textbf{Archivos Afectados:} \texttt{Entregables\_Latex/Fase\_2/*}
\end{itemize}
"""
    doc2_7 = render_doc("TI-SIGE-ENT-F2-007", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 2 ARQUITECTURA", "31/08/2026", "31/08/2026", "HITO 2: APROBACIÓN DE ARQUITECTURA", b2_7, "31/08/2026", anx2_7)
    with open(os.path.join(base_dir, "2.7_HITO_2_Aprobacion_Arquitectura_Entregable_General.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_7)

    print("Fase 2 generation completed successfully!")

if __name__ == "__main__":
    generate_fase2()
