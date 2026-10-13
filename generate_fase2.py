import os
from template_engine import render_doc

def generate_fase2():
    base_dir = os.path.join("Entregables_Latex", "Fase_2")
    os.makedirs(base_dir, exist_ok=True)

    # 2.1
    b2_1 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Diagramas General y Detallado de Casos de Uso del Sistema SIGE -- Código EDT: 2.1

\section{Introducción}
El modelado de Casos de Uso bajo el estándar de la Object Management Group (OMG) en UML permite capturar con precisión las interacciones funcionales entre los actores institucionales y los límites del sistema SIGE. Tras el congelamiento de los 24 Requisitos Funcionales en la Fase 1, este informe detalla el comportamiento del sistema a través del Diagrama General de Casos de Uso y las especificaciones textuales detalladas de los escenarios primarios, alternos y de excepción, asegurando la trazabilidad directa con los procesos del Sistema de Gestión de Calidad (SGC) de la FISEI.

\section{Objetivo}
\subsection{Objetivo General}
Modelar formalmente el comportamiento funcional e interacciones del sistema SIGE mediante diagramas UML de casos de uso generales y detallados, garantizando la cobertura de los roles institucionales del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Elaborar el Diagrama General de Casos de Uso agrupando los 8 casos de uso centrales (CU-01 a CU-08).
    \item Especificar la plantilla formal de caso de uso para los flujos críticos: Elaboración, Carga de Evidencias y Cascada de Firmas.
    \item Definir los escenarios de excepción y manejo de errores para el envío extemporáneo y rechazo de documentos.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Casos de uso para Docente Elaborador, Coordinador de Área, Coordinador de Carrera y Administrador SGC.
    \item Relaciones de inclusión (\texttt{<<include>>}) y extensión (\texttt{<<extend>>}) formales.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementación de controladores o componentes visuales.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Caso de Uso (Use Case):} Descripción de una secuencia de acciones realizadas por el sistema que produce un resultado observable de valor para un actor.
    \item \textbf{Actor:} Entidad externa (humana o automatizada) que interactúa directamente con el sistema.
    \item \textbf{Extensión (\texttt{<<extend>>}):} Relación que especifica que el comportamiento de un caso de uso puede ser incrementado condicionalmente por otro.
    \item \textbf{Inclusión (\texttt{<<include>>}):} Relación que denota que el caso de uso base incorpora explícitamente el comportamiento de otro caso de uso.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 2.1):} Diagramación UML, redacción de especificaciones textuales y análisis de actores.
    \item \textbf{Steeven Toala (Arquitecto de Software):} Validación de relaciones de inclusión y arquitectura de negocio.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación metodológica de los casos de uso.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{OMG Unified Modeling Language (OMG UML) Superstructure Version 2.5.1.}
    \item \textbf{Norma ISO/IEC/IEEE 29148:2018:} Systems and software engineering -- Life cycle processes -- Requirements engineering.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó notación UML 2.5. En la Figura \ref{fig:s2_01_casos} se representa el diagrama general de interacción de los actores institucionales.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/s2_01_casos_de_uso.png}
    \caption{Diagrama General de Casos de Uso del Sistema SIGE (UML 2.5).}
    \label{fig:s2_01_casos}
\end{figure}

\section{Descripción de actividades}
\subsection{Catálogo de Casos de Uso del Sistema (CU-01 a CU-08)}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Caso de Uso} & \textbf{Actor Principal y Propósito Funcional} & \textbf{Criticidad} \\
\hline
\textbf{CU-01} & Iniciar Sesión en SIGE & Docente, Coordinadores y Admin: Autenticación JWT y carga de perfil. & Alta \\
\hline
\textbf{CU-02} & Elaborar Plan de Trabajo & Docente Elaborador: Llenado de secciones descriptivas y asignación horaria. & Crítica \\
\hline
\textbf{CU-03} & Gestionar Matriz Dinámica & Docente Elaborador: Registro de actividades, cálculo de $100\%$ y avance. & Crítica \\
\hline
\textbf{CU-04} & Cargar Evidencias en MinIO & Docente Elaborador: Subida de anexos PDF con cálculo de hash SHA-256. & Alta \\
\hline
\textbf{CU-05} & Revisar en Comité & Coordinador de Área/Carrera: Registro granular de observaciones por sección. & Alta \\
\hline
\textbf{CU-06} & Firmar Documento Cascada & Elaborador, Revisor, Aprobador: Estampado digital secuencial e irreversible. & Crítica \\
\hline
\textbf{CU-07} & Exportar Documento SGC & Todos los roles: Generación de salidas PDF oficiales y DOCX editables. & Alta \\
\hline
\textbf{CU-08} & Gestionar Extemporáneo & Docente / Administrador: Solicitud formal y desbloqueo auditado de plazos. & Media \\
\hline
\end{tabularx}
\caption{Catálogo de Casos de Uso Institucionales.}
\label{tab:casos_uso}
\end{table}

\subsection{Especificación Textual Detallada: CU-03 (Gestión de Matriz Dinámica)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Precondiciones:} El docente debe poseer sesión activa y un borrador de plan o informe abierto.
    \item \textbf{Flujo Principal:} El docente ingresa actividad, fecha inicio, fecha fin, horas asignadas y ponderación. El sistema actualiza en tiempo real la suma total ($\sum P_i$) y el avance ponderado global.
    \item \textbf{Flujo Alterno (Validation Gate):} Si la ponderación no suma exactamente el 100\%, el sistema deshabilita el botón de guardado definitivo y emite una alerta visual en la interfaz.
\end{itemize}
"""
    anx2_1 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Especificaciones Textuales Completas de CU-01 a CU-08.
\end{itemize}"""
    doc2_1 = render_doc("TI-SIGE-ENT-F2-001", "DISEÑO DE SOFTWARE / MODELADO FUNCIONAL", "27/08/2026", "27/08/2026", "DIAGRAMAS GENERAL Y DETALLADO DE CASOS DE USO", b2_1, "27/08/2026", anx2_1)
    with open(os.path.join(base_dir, "2.1_Diagramas_General_y_Detallado_Casos_de_Uso.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_1)

    # 2.2
    b2_2 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Documento de Arquitectura de Software (SAD \& C4 Model) -- Código EDT: 2.2

\section{Introducción}
La arquitectura de software constituye el esquema estructural y de organización técnica que determina la robustez, escalabilidad y mantenibilidad de la solución SIGE. En este documento se formaliza el \\textbf{Software Architecture Document (SAD)} fundamentado en los principios de Clean Architecture (Arquitectura Limpia) y el modelo C4 (Contexto, Contenedores, Componentes y Código). Se detalla la separación estricta de responsabilidades entre el Dominio institucional, los Casos de Uso de Aplicación, los Adaptadores de Infraestructura (PostgreSQL 18, MinIO S3, LanguageTool) y la capa de Presentación Web RESTful.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar la arquitectura técnica de la solución SIGE basada en principios de desacoplamiento, inmutabilidad y alta cohesión, documentada mediante el modelo C4 y vistas arquitectónicas estándar.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Estructurar las 4 capas de la Arquitectura Limpia: Dominio, Aplicación, Infraestructura y API.
    \item Elaborar los diagramas C4 de Nivel 1 (Contexto de Sistema) y Nivel 2 (Contenedores).
    \item Definir los patrones de diseño: Repository Pattern, Mediator, Middleware Pipeline y CQRS.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Diseño de arquitectura de microservicios contenerizados y tuberías de middlewares en Express v5.
    \item Estrategia de persistencia en PostgreSQL 18 y almacenamiento desacoplado de objetos en MinIO S3.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Arquitecturas de microservicios distribuidos en múltiples clústeres Kubernetes (excede el alcance del VPS local).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Clean Architecture:} Paradigma arquitectónico donde las reglas de negocio de la entidad no dependen de ningún framework externo.
    \item \textbf{C4 Model:} Jerarquía visual para la arquitectura de software (Contexto, Contenedores, Componentes y Código).
    \item \textbf{Repository Pattern:} Patrón que desacopla la lógica de negocio del acceso y persistencia en la base de datos.
    \item \textbf{Middleware Pipeline:} Cadena secuencial de interceptores de solicitudes HTTP para validación, autenticación y registro.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 2.2):} Definición de capas arquitectónicas, diagramación C4 y selección de patrones de diseño.
    \item \textbf{Nixon Hurtado (Backend):} Revisión de adaptadores de infraestructura y base de datos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del SAD institucional.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO/IEC/IEEE 42010:2011:} Systems and software engineering -- Architecture description.
    \item \textbf{The Open Group Architecture Framework (TOGAF 9.2).}
\end{itemize}

\section{Método, Políticas y Contenidos}
Se aplicó modelado C4. En las Figuras \ref{fig:s2_02_clean} y \ref{fig:s2_02_c4} se presentan el diagrama de capas de Arquitectura Limpia y el diagrama C4 de Contenedores.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/s2_02_clean_architecture.png}
    \caption{Arquitectura Limpia del Sistema SIGE (Capas y Regla de Dependencia).}
    \label{fig:s2_02_clean}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.5cm,keepaspectratio]{images/s2_02_contenedores_c4.png}
    \caption{Diagrama C4 de Nivel 2: Contenedores y Protocolos de Comunicación.}
    \label{fig:s2_02_c4}
\end{figure}

\section{Descripción de actividades}
\subsection{Organización de Capas de la Arquitectura Limpia}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Capa Arquitectónica} & \textbf{Responsabilidad Primaria} & \textbf{Componentes Clave} \\
\hline
1. Domain (Núcleo) & Entidades puras de negocio y reglas inmutables del SGC. Cero dependencias de librerías externas. & Entidad Documento, Actividad, Validación Ponderación ($100\%$), Firma Digital. \\
\hline
2. Application & Orquestación de casos de uso, transacciones y lógica de flujo documental. & Servicios de Documentos, Flujo de Firmas, Motor de Validation Gates. \\
\hline
3. Infrastructure & Adaptadores tecnológicos externos, bases de datos y servicios de red. & Repositorio PostgreSQL 18, MinIO Storage Client, LanguageTool REST Client, Google Gemini API Client. \\
\hline
4. Presentation / API & Interfaz gráfica SPA y endpoints HTTP RESTful con middlewares de seguridad. & Express v5 REST API, Auth JWT Middleware, SPA React + Vite + Tailwind CSS. \\
\hline
\end{tabularx}
\caption{Capas y Responsabilidades de la Arquitectura del Sistema SIGE.}
\label{tab:capas_arch}
\end{table}

\subsection{Estrategia de Seguridad e Inmutabilidad}
Toda mutación de estado que legalice un documento genera un sellado digital con el cálculo del hash criptográfico del contenido consolidado, imposibilitando la alteración retroactiva de datos en base de datos.
"""
    anx2_2 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Ficha Técnica de Decisión Arquitectónica (ADR-01 a ADR-05).
\end{itemize}"""
    doc2_2 = render_doc("TI-SIGE-ENT-F2-002", "ARQUITECTURA DE SOFTWARE / SAD Y C4", "28/08/2026", "28/08/2026", "DISEÑO DE ARQUITECTURA DE LA SOLUCIÓN", b2_2, "28/08/2026", anx2_2)
    with open(os.path.join(base_dir, "2.2_Diseno_Arquitectura_de_la_Solucion.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_2)

    # 2.3
    b2_3 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Diagramas de Secuencia, Actividades y Clases de Dominio -- Código EDT: 2.3

\section{Introducción}
El comportamiento dinámico y la estructura estática de las entidades de software requieren una especificación formal y no ambigua que oriente a los desarrolladores durante la construcción. El presente entregable documenta tres perspectivas esenciales del modelado UML: la secuencia temporal de intercambio de mensajes en la Cascada de Firmas, el flujo de control y toma de decisiones en el ciclo de vida del informe mediante Diagramas de Actividades, y la estructura de clases del dominio SGC que sustentará los modelos de datos y objetos de negocio.

\section{Objetivo}
\subsection{Objetivo General}
Especificar formalmente el comportamiento dinámico y las estructuras de clases del sistema SIGE mediante diagramas UML de secuencia, actividades y clases de dominio.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modelar la interacción temporal y validaciones en la Cascada de Firmas multinivel (Secuencia).
    \item Representar el ciclo de vida completo de elaboración, revisión y aprobación del informe (Actividades).
    \item Diseñar el diagrama de clases de dominio con relaciones de agregación, composición y multiplicidades.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Secuencia de firmas con validación criptográfica y bloqueo de edición.
    \item Máquina de estados documental: Borrador $\to$ En Revisión $\to$ Observado $\to$ Firmado $\to$ Legalizado.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Interfaces de usuario finales y controladores frontend.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Diagrama de Secuencia:} Diagrama que muestra las interacciones entre objetos ordenadas en secuencia temporal.
    \item \textbf{Diagrama de Actividades:} Diagrama que describe el flujo de control procedimental entre actividades concurrentes y secuenciales.
    \item \textbf{Clase de Dominio:} Representación de un concepto del negocio institucional con atributos y responsabilidades.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Heidi Villavicencio (Responsables EDT 2.3):} Modelado de diagramas de secuencia, actividades y clases UML.
    \item \textbf{Nixon Hurtado (DBA):} Revisión de correspondencia entre clases de dominio y el modelo de datos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación técnica de los modelos dinámicos.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{OMG UML 2.5 Specification (Behavioral \& Structural Diagrams).}
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó Enterprise Architect y Mermaid. En las Figuras \ref{fig:s2_03_sec}, \ref{fig:s2_03_act} y \ref{fig:s2_03_cla} se aprecian los tres diagramas formalizados.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/s2_03_secuencia_validation.png}
    \caption{Diagrama de Secuencia: Validación y Flujo de Firmas en Cascada.}
    \label{fig:s2_03_sec}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/s2_03_actividades_ciclo.png}
    \caption{Diagrama de Actividades: Ciclo de Vida del Informe Institucional SGC.}
    \label{fig:s2_03_act}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/s2_03_clases_uml.png}
    \caption{Diagrama de Clases de Dominio del Sistema SIGE.}
    \label{fig:s2_03_cla}
\end{figure}

\section{Descripción de actividades}
\subsection{Especificación del Circuito de Firmas en Cascada}
El diagrama de secuencia estipula el siguiente intercambio ordenado:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item El Docente invoca \texttt{POST /firmar} con su certificado digital.
    \item El \texttt{ValidationGateService} verifica que $\sum P_i = 100\%$ y que todas las actividades posean evidencias en MinIO.
    \item Si es válido, se estampa la Firma 1 (Elaborador), se calcula el hash SHA-256 inmutable y el documento se bloquea para edición.
    \item El Coordinador de Área revisa y estampa la Firma 2 (Revisor).
    \item El Coordinador de Carrera verifica y estampa la Firma 3 (Aprobador), legalizando el documento para Consejo Directivo.
\end{enumerate}
"""
    anx2_3 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Diccionario de Mensajes y Parámetros del Flujo de Secuencia.
\end{itemize}"""
    doc2_3 = render_doc("TI-SIGE-ENT-F2-003", "DISEÑO DE SOFTWARE / COMPORTAMIENTO DINÁMICO", "02/09/2026", "02/09/2026", "DIAGRAMAS DE SECUENCIA, ACTIVIDADES Y CLASES DE DOMINIO", b2_3, "02/09/2026", anx2_3)
    with open(os.path.join(base_dir, "2.3_Diagramas_de_Secuencia_Actividades_y_Clases_de_Dominio.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_3)

    # 2.4
    b2_4 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Diseño de Base de Datos Relacional (Modelo ER, Lógico y DDL) -- Código EDT: 2.4

\section{Introducción}
La integridad referencial y la durabilidad de los datos institucionales son requisitos indispensables en un sistema de gestión de calidad académica. En este entregable se formaliza el diseño integral de la base de datos relacional para el motor PostgreSQL 18. Se presentan el Modelo Entidad-Relación bajo notación Crow's Foot, el esquema lógico normalizado en Tercera Forma Normal (3NF) y el diccionario exhaustivo de las 13 tablas relacionales con sus tipos de datos, llaves primarias, foráneas, restricciones de chequeo y políticas de indexación.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar y estructurar la base de datos relacional institucional del sistema SIGE en PostgreSQL 18, garantizando la consistencia, normalización 3NF y trazabilidad de los datos del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Modelar el Diagrama Entidad-Relación conceptual y lógico con las 13 tablas relacionales.
    \item Elaborar el Diccionario de Datos exhaustivo con tipos nativos de PostgreSQL 18 y restricciones de integridad.
    \item Diseñar la estrategia de indexación B-Tree y GIN para acelerar las consultas frecuentes.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item 13 tablas relacionales: usuarios, roles, facultades, carreras, periodos, documentos, secciones, actividades, evidencias, observaciones, firmas, catalogos, auditoria.
    \item Restricciones de integridad referencial con borrado lógico y cascada controlada.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Ejecución física de scripts DDL en el servidor (actividad cubierta en EDT 3.1).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PostgreSQL 18:} Sistema de gestión de bases de datos relacional y orientado a objetos open source.
    \item \textbf{Tercera Forma Normal (3NF):} Estado de normalización donde no existen dependencias funcionales transitivas entre atributos no clave.
    \item \textbf{Crow's Foot (Pata de Cuervo):} Notación gráfica estándar para representar cardinalidades en modelos Entidad-Relación.
    \item \textbf{Diccionario de Datos:} Repositorio detallado que describe la estructura, significado y restricciones de cada columna de la base.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado / Steeven Toala (Responsables EDT 2.4):} Diseño del modelo ER, diccionario de datos y definición de constraints.
    \item \textbf{Heidi Villavicencio (Analista):} Verificación de campos obligatorios según formatos SGC.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del esquema de base de datos.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ANSI/ISO/IEC 9075:2016 (SQL Standard).}
    \item \textbf{Norma ISO/IEC 25012:2008:} Software engineering -- Data quality model.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó modelado en 3NF. En la Figura \ref{fig:s2_04_erd} se presenta el Diagrama Entidad-Relación consolidado en notación Crow's Foot.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s2_04_erd_postgresql.png}
    \caption{Diagrama Entidad-Relación Crow's Foot del Sistema SIGE (13 Tablas).}
    \label{fig:s2_04_erd}
\end{figure}

\section{Descripción de actividades}
\subsection{Estructura General de las 13 Tablas Relacionales}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{No.} & \textbf{Tabla} & \textbf{Descripción y Propósito Institucional} & \textbf{Registros Est.} \\
\hline
1 & \texttt{roles} & Catálogo de roles de seguridad (Docente, Coordinador, Subdecano, Admin). & 4 \\
\hline
2 & \texttt{facultades} & Unidad académica mayor (FISEI). & 1 \\
\hline
3 & \texttt{carreras} & Programas académicos de pregrado de la facultad. & 5 \\
\hline
4 & \texttt{usuarios} & Credenciales institucionales, nombres, email y rol asignado. & 120 \\
\hline
5 & \texttt{periodos\_academicos} & Ciclos semestrales oficiales con fechas límite y fechas extemporáneas. & 10 \\
\hline
6 & \texttt{documentos} & Cabecera de Plan de Trabajo e Informe con estado SGC y código único. & 1,500 \\
\hline
7 & \texttt{secciones} & Contenido de texto enriquecido HTML de cada sección descriptiva del SGC. & 7,500 \\
\hline
8 & \texttt{actividades} & Registro detallado de la Matriz Dinámica con horas, ponderación y avance. & 15,000 \\
\hline
9 & \texttt{evidencias} & Metadatos de anexos en MinIO S3 con URL, tamaño y hash SHA-256. & 25,000 \\
\hline
10 & \texttt{observaciones} & Registro de comentarios de coordinadores a nivel de sección o actividad. & 3,000 \\
\hline
11 & \texttt{firmas\_documento} & Registro del circuito de firmas con cargo, estampa de tiempo y hash. & 4,500 \\
\hline
12 & \texttt{catalogos\_sgc} & Tipologías estandarizadas de actividades de docencia, vinculación e investigación. & 50 \\
\hline
13 & \texttt{auditoria\_logs} & Bitácora inmutable de eventos del sistema para trazabilidad forense. & 100,000 \\
\hline
\end{tabularx}
\caption{Catálogo de Tablas del Esquema Relacional PostgreSQL 18.}
\label{tab:tablas_bd}
\end{table}

\subsection{Diccionario de Datos: Tabla Central \texttt{documentos}}
\begin{table}[htbp]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Campo (Columna)} & \textbf{Tipo de Dato} & \textbf{Nulo} & \textbf{Restricciones y Claves} \\
\hline
\texttt{id} & \texttt{UUID} & NO & Primary Key (\texttt{gen\_random\_uuid()}) \\
\hline
\texttt{codigo\_documento} & \texttt{VARCHAR(50)} & NO & Unique Key (\texttt{TI-SIGE-PLA-2026-001}) \\
\hline
\texttt{tipo\_documento} & \texttt{VARCHAR(20)} & NO & Check: in ('PLAN\_TRABAJO', 'INFORME\_CUMPLIMIENTO') \\
\hline
\texttt{usuario\_id} & \texttt{UUID} & NO & Foreign Key $\to$ \texttt{usuarios(id)} \\
\hline
\texttt{periodo\_id} & \texttt{UUID} & NO & Foreign Key $\to$ \texttt{periodos\_academicos(id)} \\
\hline
\texttt{estado} & \texttt{VARCHAR(30)} & NO & Check: in ('BORRADOR', 'EN\_REVISION', 'OBSERVADO', 'FIRMADO', 'LEGALIZADO') \\
\hline
\texttt{porcentaje\_avance} & \texttt{NUMERIC(5,2)} & NO & Default: 0.00, Check: entre 0.00 y 100.00 \\
\hline
\texttt{fecha\_creacion} & \texttt{TIMESTAMPTZ} & NO & Default: \texttt{CURRENT\_TIMESTAMP} \\
\hline
\texttt{hash\_inmutable} & \texttt{VARCHAR(64)} & SÍ & Hash SHA-256 generado al firmar \\
\hline
\end{tabularx}
\caption{Diccionario de Datos de la Tabla \texttt{documentos}.}
\label{tab:diccionario_documentos}
\end{table}
"""
    anx2_4 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Diccionario de Datos Completo de las 13 Tablas en Formato Tabular.
\end{itemize}"""
    doc2_4 = render_doc("TI-SIGE-ENT-F2-004", "BASE DE DATOS / MODELADO RELACIONAL", "03/09/2026", "03/09/2026", "DISEÑO DE BASE DE DATOS RELACIONAL", b2_4, "03/09/2026", anx2_4)
    with open(os.path.join(base_dir, "2.4_Diseno_de_Base_de_Datos_Relacional.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_4)

    # 2.5
    b2_5 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Diseño de Interfaces y Experiencia de Usuario (Wireframes y UX) -- Código EDT: 2.5

\section{Introducción}
La usabilidad y la experiencia de usuario (UX) son determinantes para la adopción exitosa del software en entornos universitarios. El cuerpo docente requiere una interfaz moderna, limpia y predecible que minimice la fatiga visual y agilice el registro de sus labores. Este informe consolida el diseño de alta fidelidad, la arquitectura de interfaces, el flujo del Wizard modular de 4 pasos para el elaborador, los componentes de la matriz interactiva y el panel de revisión colegiada, acompañados de una guía de estilos y tokens cromáticos institucionales accesibles bajo el estándar WCAG 2.1 nivel AA.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar la arquitectura de interfaces y experiencia de usuario (UI/UX) del sistema SIGE, elaborando wireframes de alta fidelidad, flujos interactivos y el sistema de diseño accesible.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Diseñar el Wizard modular de 4 pasos para la elaboración secuencial de documentos.
    \item Maquetar la Matriz Dinámica responsive que replica la Tabla 1 del formato SGC.
    \item Diseñar el panel de revisión del Comité con bandeja de observaciones contextuales.
    \item Establecer la paleta de colores institucional, tipografía y tokens accesibles WCAG AA.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Vistas de Dashboard Docente, Editor Wizard, Tabla de Matriz, Subida de Archivos y Panel de Revisión.
    \item Prototipo interactivo en Figma y especificación de tokens para Tailwind CSS.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Código JavaScript de componentes React (cubierto en Fase 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Wireframe de Alta Fidelidad:} Representación visual interactiva y detallada de la interfaz con colores y tipografías reales.
    \item \textbf{Design Tokens:} Variables de diseño centralizadas (colores, espaciados, fuentes) que garantizan consistencia visual.
    \item \textbf{WCAG 2.1 (Nivel AA):} Pautas de Accesibilidad para el Contenido Web con ratios mínimos de contraste cromático (4.5:1).
    \item \textbf{Wizard de Navegación:} Patrón de diseño UI que guía al usuario paso a paso a través de un flujo complejo.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio / Andrea Vásquez (Responsables EDT 2.5):} Diseño UI en Figma, investigación de usuarios y diseño del sistema visual.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de factibilidad de maquetación en Tailwind CSS.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del prototipo de interfaces.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{W3C Web Content Accessibility Guidelines (WCAG) 2.1.}
    \item \textbf{ISO 9241-210:2019:} Ergonomics of human-system interaction -- Human-centred design for interactive systems.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se utilizó diseño centrado en el usuario (HCD). En las Figuras \ref{fig:s2_05_views} y \ref{fig:s2_05_palette} se aprecian las vistas principales del sistema y la paleta de colores institucional.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/s2_05_layout_vistas.png}
    \caption{Diseño de Layouts y Vistas del Sistema SIGE.}
    \label{fig:s2_05_views}
\end{figure}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.80\textwidth,height=5.0cm,keepaspectratio]{images/s2_05_paleta_colores.png}
    \caption{Paleta Cromática y Tokens de Diseño Accesible del Sistema SIGE.}
    \label{fig:s2_05_palette}
\end{figure}

\section{Descripción de actividades}
\subsection{Arquitectura del Wizard Modular de 4 Pasos}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Paso} & \textbf{Denominación} & \textbf{Componentes de Interfaz} & \textbf{Validación de Avance} \\
\hline
Paso 1 & Datos Generales & Selección de Período, Dedicación Horaria, Carrera y Asignaturas. & Período activo y datos obligatorios completos. \\
\hline
Paso 2 & Secciones SGC & Editor TipTap con barra de herramientas enriquecida y autoguardado. & Mínimo 50 caracteres por sección requerida. \\
\hline
Paso 3 & Matriz Dinámica & Tabla interactiva de actividades con adición/edición de filas y avance. & Suma estricta de ponderaciones igual a $100.00\%$. \\
\hline
Paso 4 & Resumen y Envío & Visor general de cumplimiento, gestor de evidencias y botón de firma. & Validación de evidencias y ausencia de observaciones. \\
\hline
\end{tabularx}
\caption{Estructura de Pasos del Wizard de Edición.}
\label{tab:wizard_steps}
\end{table}

\subsection{Tokens de Color y Accesibilidad}
La paleta se fundamenta en el azul corporativo institucional:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Primary Navy:} \texttt{\#1A365D} (Contraste 11.2:1 con fondo blanco, cumple WCAG AAA).
    \item \textbf{Accent Blue:} \texttt{\#2B6CB0} (Para botones primarios e indicadores de navegación).
    \item \textbf{Success Green:} \texttt{\#2F855A} (Para estado 100\% de ponderación y firmas válidas).
    \item \textbf{Warning Amber:} \texttt{\#C05621} (Para estados de observación pendiente).
    \item \textbf{Danger Red:} \texttt{\#C53030} (Para bloqueos de Validation Gate y sumatorias incorrectas).
\end{itemize}
"""
    anx2_5 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Enlace y Especificación del Prototipo Interactivo Figma.
\end{itemize}"""
    doc2_5 = render_doc("TI-SIGE-ENT-F2-005", "EXPERIENCIA DE USUARIO / WIREFRAMES UI-UX", "03/09/2026", "03/09/2026", "DISEÑO DE INTERFACES Y EXPERIENCIA DE USUARIO", b2_5, "03/09/2026", anx2_5)
    with open(os.path.join(base_dir, "2.5_Diseno_Interfaces_Wireframes_UX.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_5)

    # 2.6
    b2_6 = r"""
\section{Título}
\textbf{Denominación del Entregable:} Arquitectura de Microservicios y Docker Compose Local -- Código EDT: 2.6

\section{Introducción}
El aseguramiento de la portabilidad y la reproducibilidad del entorno de ejecución constituye una buena práctica fundamental en la ingeniería de software actual. Para evitar las típicas fallas de configuración cruzada entre los entornos de desarrollo, pruebas y producción, el sistema SIGE adopta un modelo contenerizado integral orquestado mediante Docker Compose. En este informe se formaliza la topología de red aislada, la asignación de volúmenes persistentes y las especificaciones de los contenedores que conforman el ecosistema SIGE: la base de datos relacional PostgreSQL 18, el almacenamiento de objetos MinIO S3 y el motor de asistencia lingüística LanguageTool.

\section{Objetivo}
\subsection{Objetivo General}
Diseñar y formalizar la arquitectura de contenedores y el entorno de orquestación local con Docker Compose para el stack tecnológico completo del sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Diseñar el archivo de orquestación \texttt{docker-compose.yml} con redes bridge privadas y volúmenes persistentes.
    \item Configurar el contenedor de base de datos relacional PostgreSQL 18 con inicialización automática de tablas.
    \item Integrar el contenedor MinIO Object Storage con creación del bucket institucional \texttt{sige-evidencias}.
    \item Configurar el microservicio LanguageTool local para corrección gramatical y ortográfica sin dependencias externas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Orquestación de 5 servicios: \texttt{db} (PostgreSQL 18), \texttt{minio} (S3), \texttt{languagetool} (Gramática), \texttt{api} (Backend Express) y \texttt{client} (Frontend React).
    \item Políticas de reinicio automático (\texttt{restart: unless-stopped}) y Health Checks.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Clústeres Kubernetes distribuidos de alta disponibilidad (diseñados para VPS standalone).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Docker Compose:} Herramienta para definir y ejecutar aplicaciones Docker multicontenedor mediante archivos YAML.
    \item \textbf{MinIO S3:} Servidor de almacenamiento de objetos de alto rendimiento compatible con las APIs de Amazon S3.
    \item \textbf{LanguageTool:} Software open source de corrección gramatical, de estilo y ortográfica para más de 30 idiomas.
    \item \textbf{Health Check:} Instrucción algorítmica para determinar periódicamente si un contenedor se encuentra en estado saludable y operativo.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala / Nixon Hurtado (Responsables EDT 2.6):} Definición de especificaciones de contenedores, mapeo de puertos y volúmenes.
    \item \textbf{Andrea Vásquez (Frontend):} Validación de puertos de enlace con el cliente web.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la arquitectura de contenedores.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Open Container Initiative (OCI) Image Specification.}
    \item \textbf{Docker Compose File Format Specification v3.8.}
\end{itemize}

\section{Método, Políticas y Contenidos}
Se diseñaron redes bridge privadas. En la Figura \ref{fig:s2_06_docker} se presenta el esquema topológico de los contenedores Docker orquestados.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.2cm,keepaspectratio]{images/s2_06_docker_compose.png}
    \caption{Arquitectura de Contenedores y Redes Aisladas en Docker Compose.}
    \label{fig:s2_06_docker}
\end{figure}

\section{Descripción de actividades}
\subsection{Especificación Técnica de Contenedores Orquestados}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|m{2.8cm}|c|X|X|}
\hline
\rowcolor{tableheader}
\textbf{Servicio} & \textbf{Imagen Base} & \textbf{Puertos} & \textbf{Volumen Persistente} & \textbf{Propósito / Función} \\
\hline
\texttt{db} & \texttt{postgres:18-alpine} & 5432:5432 & \texttt{postgres\_data:/var/lib/postgresql/data} & Persistencia relacional de 13 tablas, índices y transacciones. \\
\hline
\texttt{minio} & \texttt{minio/minio:RELEASE} & 9000, 9001 & \texttt{minio\_data:/data} & Almacenamiento seguro S3 de evidencias en PDF con hash SHA-256. \\
\hline
\texttt{languagetool} & \texttt{erikvl87/languagetool} & 8010:8010 & N/A (Stateless) & Motor local de revisión ortográfica consumido en tiempo real por el editor. \\
\hline
\texttt{api} & \texttt{node:22-alpine} & 4000:4000 & \texttt{api\_logs:/app/logs} & Backend Express v5, API RESTful y Validation Gates. \\
\hline
\texttt{client} & \texttt{nginx:alpine} & 80:80, 443 & N/A (Build estático) & Servidor web del cliente SPA React + Vite + Tailwind CSS. \\
\hline
\end{tabularx}
\caption{Matriz de Contenedores y Configuración del Stack Tecnológico.}
\label{tab:contenedores}
\end{table}

\subsection{Políticas de Red y Aislamiento de Seguridad}
Se configuró la red privada \texttt{sige\_internal\_net} de tipo \texttt{bridge}, asegurando que la base de datos PostgreSQL y MinIO no expongan puertos innecesarios a redes públicas no autorizadas.
"""
    anx2_6 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Especificación Completa del Archivo \texttt{docker-compose.yml}.
\end{itemize}"""
    doc2_6 = render_doc("TI-SIGE-ENT-F2-006", "INFRAESTRUCTURA / CONTENEDORES DOCKER", "04/09/2026", "04/09/2026", "ARQUITECTURA DE MICROSERVICIOS Y DOCKER COMPOSE LOCAL", b2_6, "04/09/2026", anx2_6)
    with open(os.path.join(base_dir, "2.6_Arquitectura_Contenedores_Docker_Locales.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_6)

    # 2.7
    b2_7 = r"""
\section{Título}
\textbf{Denominación del Entregable:} HITO 2: Aprobación de Arquitectura y Entregable General Semana 2 -- Código EDT: 2.7

\section{Introducción}
El cierre formal de la Fase 2: Diseño y Arquitectura representa el hito más crítico previo al inicio de la codificación y desarrollo del núcleo del sistema SIGE. En este documento se consolida la revisión exhaustiva de todos los artefactos de diseño construidos entre el 25 de agosto y el 04 de septiembre de 2026: Casos de Uso, Documento de Arquitectura de Software (SAD), Modelos Dinámicos UML, Base de Datos PostgreSQL 18, Wireframes y Prototipo Figma, y la Orquestación de Contenedores con Docker Compose. Se documenta la sustentación ante el docente evaluador Ing. Paulo Torres y la certificación formal para dar inicio al desarrollo Core en la Fase 3.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, evaluar y aprobar formalmente el paquete de entregables de la Fase 2: Diseño y Arquitectura (Hito 2), certificando la conformidad técnica y autorizando el inicio de la Fase 3 de Desarrollo Core.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Verificar el cumplimiento y calidad técnica de los entregables EDT 2.1 al 2.6.
    \item Comprobar la trazabilidad del 100\% entre los Requerimientos SRS IEEE 830 y los artefactos de diseño arquitectónico.
    \item Realizar la demostración del prototipo interactivo en Figma y la puesta en marcha del stack Docker local.
    \item Suscribir el acta formal de aprobación de Hito 2 por parte del docente evaluador.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Consolidado de los 7 entregables de Fase 2 ejecutados entre el 25 de agosto y el 04 de septiembre de 2026.
    \item Validación de arquitectura de datos, interfaces y contenedores.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Cambios estructurales en el modelo relacional o arquitectura tras la firma de este hito.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Hito 2 (Milestone Semana 2):} Punto de control que certifica que los cimientos arquitectónicos del software están terminados y validados.
    \item \textbf{Línea Base de Arquitectura:} Conjunto congelado de especificaciones técnicas que guiarán la implementación del código fuente.
    \item \textbf{Trazabilidad Arquitectónica:} Capacidad de vincular cada requisito funcional con un componente o módulo específico del diseño.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Equipo de Proyecto SIGE (Responsables EDT 2.7):} Consolidación del paquete técnico, demostración de prototipos y sustentación.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador / Patrocinador):} Revisión de conformidad, retroalimentación y suscripción formal de aprobación.
\end{itemize}

\section{Normativa Legal y Técnica}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{IEEE Std 1016-2009:} Standard for Information Technology -- Systems Design -- Software Design Descriptions.
    \item \textbf{Guía PMBOK (7ma Edición):} Gestión de la Calidad y Cierre de Fase Técnica.
\end{itemize}

\section{Método, Políticas y Contenidos}
Se llevó a cabo una sesión de sustentación técnica de 2 horas el viernes 04 de septiembre de 2026. En la Figura \ref{fig:s2_07_cons} se presenta el mapa consolidado de la Fase 2 de Arquitectura.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth,height=5.2cm,keepaspectratio]{images/s2_07_consolidado_s2.png}
    \caption{Mapa Consolidado de la Fase 2: Diseño y Arquitectura de la Solución.}
    \label{fig:s2_07_cons}
\end{figure}

\section{Descripción de actividades}
\subsection{Matriz de Verificación y Conformidad de Entregables de Fase 2}
\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{4.0cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{EDT} & \\textbf{Entregable Oficial} & \textbf{Artefacto Verificado} & \textbf{Horas} & \textbf{Estado} \\
\hline
2.1 & Casos de Uso UML & Diagrama general y especificación CU-01 a CU-08 & 24 h & Aprobado \\
\hline
2.2 & Arquitectura SAD & Clean Architecture, C4 Model Nivel 1 y 2 & 32 h & Aprobado \\
\hline
2.3 & Modelado Dinámico & Diagramas Secuencia, Actividades y Clases & 40 h & Aprobado \\
\hline
2.4 & Base de Datos & ER Crow's Foot, normalización 3NF y 13 tablas & 40 h & Aprobado \\
\hline
2.5 & Interfaces y UX & Wireframes alta fidelidad, Wizard y Figma & 40 h & Aprobado \\
\hline
2.6 & Contenedores Docker & \texttt{docker-compose.yml}, PostgreSQL, MinIO, LT & 32 h & Aprobado \\
\hline
2.7 & Hito 2: Aprobación Arquitectura & Paquete Arquitectura Aprobado y Sustentación & 0 h & Aprobado \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL HORAS INVERTIDAS EN FASE 2:}} & \textbf{208 h} & \textbf{100\%} \\
\hline
\end{tabularx}
\caption{Matriz de Conformidad y Cierre de Entregables de Fase 2.}
\label{tab:cierre_fase2}
\end{table}

\subsection{Dictamen Técnico y Autorización de Desarrollo}
El docente evaluador Ing. Paulo Torres emite el dictamen de APROBADO sin observaciones impeditivas, autorizando formalmente al equipo para iniciar la Fase 3: Desarrollo Core a partir del lunes 07 de septiembre de 2026.
"""
    anx2_7 = r"""\begin{itemize}[leftmargin=1.5em]
\item \textbf{Anexo 1:} Acta de Aprobación de Hito 2 (Semana 2).
\item \textbf{Anexo 2:} Matriz de Trazabilidad Arquitectura vs. Requerimientos SRS.
\end{itemize}"""
    doc2_7 = render_doc("TI-SIGE-ENT-F2-007", "HITO DE CONTROL / APROBACIÓN DE FASE 2", "04/09/2026", "04/09/2026", "HITO 2: APROBACIÓN DE ARQUITECTURA Y ENTREGABLE GENERAL", b2_7, "04/09/2026", anx2_7)
    with open(os.path.join(base_dir, "2.7_HITO_2_Aprobacion_Arquitectura_Entregable_General.tex"), "w", encoding="utf-8") as f:
        f.write(doc2_7)

    print("Fase 2 generated successfully via template_engine!")

if __name__ == "__main__":
    generate_fase2()
