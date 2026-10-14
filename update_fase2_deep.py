# update_fase2_deep.py
import re

fname = "generate_fase2_enhanced.py"
txt = open(fname, encoding="utf-8").read()

anx2_1_new = r"""
\subsection*{Anexo: Evidencias de Modelado y Especificación de Casos de Uso}

\subsubsection*{1. Desglose Metodológico y Origen Real de los Casos de Uso (Paso a Paso)}
Para garantizar que el modelado funcional responda estrictamente a la operativa institucional y no a conjeturas aisladas, los Casos de Uso se derivaron directamente del formato oficial \texttt{UTA-SGC-A-2-1-P7-T1} (Plan de Trabajo Docente) y de los 24 Requisitos Funcionales aprobados en la Fase 1.

El desarrollo del modelado se ejecutó en cuatro etapas secuenciales:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Identificación de Actores Primarios y Secundarios:} A partir del estatuto orgánico de la UTA y la matriz de actores de la FISEI, se formalizaron los roles del sistema: Docente Elaborador (usuario primario de planificación y carga de evidencias), Coordinador de Comisión (revisor de actividades específicas), Coordinador de Carrera (auditor de carga horaria y primer validador), Subdecano (aprobador de facultad) y Administrador SGC (gestor de catálogos y prórrogas).
    \item \textbf{Paso 2: Estructuración del Catálogo de 8 Casos de Uso (CU-01 a CU-08):} Se definieron los límites del sistema agrupando las interacciones en CU-01 (Iniciar Sesión JWT), CU-02 (Elaborar Plan en Wizard), CU-03 (Gestionar Matriz Dinámica 100\%), CU-04 (Custodiar Evidencias en MinIO S3), CU-05 (Revisar Expediente en Comité), CU-06 (Cascada Secuencial de Firmas), CU-07 (Exportar Documento Oficial SGC) y CU-08 (Gestionar Prórrogas Extemporáneas).
    \item \textbf{Paso 3: Definición de Relaciones de Inclusión y Extensión:} Se identificaron las dependencias funcionales: todos los casos de uso incluyen obligatoriamente la resolución de identidad (\texttt{<<include>> CU-01}); la elaboración de plan incluye el cálculo automático de 40 horas; y la gestión de extemporaneidad extiende condicionalmente (\texttt{<<extend>> CU-08}) la edición cuando la fecha actual sobrepasa el cronograma lectivo.
    \item \textbf{Paso 4: Redacción de Especificaciones Textuales Normalizadas:} Se redactaron fichas detalladas para cada caso de uso declarando precondiciones, flujo principal (\textit{happy path}), flujos alternos de asistencia y flujos de excepción transaccionales.
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
\textbf{Explicación Técnica del Diagrama de Casos de Uso:}
La figura ilustra las fronteras del sistema web SIGE y las interacciones de los actores institucionales con los módulos funcionales. El Docente Elaborador interactúa principalmente con el subsistema de elaboración (CU-02, CU-03, CU-04), donde el Wizard por pasos valida progresivamente los datos antes de habilitar el envío a revisión. El Coordinador de Carrera y el Subdecano operan sobre el subsistema de fiscalización y firmas (CU-05, CU-06), el cual implementa una compuerta estricta que impide que una autoridad firme un expediente si el docente o revisor previo no han estampado su firma digital. Finalmente, todos los actores tienen acceso a la exportación documental oficial (CU-07) para obtener copias impresas o digitales certificadas con código QR.

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

anx2_2_new = r"""
\subsection*{Anexo: Evidencias de Arquitectura de Software y Modelo C4}

\subsubsection*{1. Desglose Metodológico de la Arquitectura de Software (Paso a Paso)}
Para asegurar mantenibilidad, escalabilidad y estricta separación de responsabilidades, la arquitectura de SIGE se diseñó combinando los principios de Clean Architecture (Arquitectura Limpia) con la notación de diagramación del Modelo C4 (Contexto, Contenedores, Componentes y Código).

El proceso de ingeniería arquitectónica comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Estructuración en Cuatro Capas Concéntricas:} Capa de Dominio / Entidades (\textit{Entities}: \texttt{PlanDocente}, \texttt{ActividadMatriz}, libres de dependencias externas); Capa de Casos de Uso (\textit{Use Cases}: reglas de negocio orquestadoras como \texttt{ValidarHorasMinimas}); Capa de Adaptadores (\textit{Interface Adapters}: controladores REST Express v5, repositorios pg-promise y cliente MinIO S3); y Capa de Infraestructura / Frameworks (\textit{Frameworks and Drivers}: PostgreSQL 18, React SPA, Docker Compose y servidor Nginx).
    \item \textbf{Paso 2: Diagramación del Modelo C4 de Contenedores:} Se definieron los cinco contenedores autónomos que componen la topología: SPA Frontend, Backend REST API, Base de Datos PostgreSQL, Almacén de Objetos MinIO y Motor Lingüístico LanguageTool.
    \item \textbf{Paso 3: Definición de Contratos de Comunicación y Puertos:} Se establecieron los protocolos de intercambio (JSON sobre HTTP/REST para servicios, nativo TCP para base de datos y API S3 para archivos).
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
\textbf{Explicación Técnica de Clean Architecture:}
La figura ilustra la regla de dependencias fundamental: las capas exteriores conocen y dependen de las interiores, pero el núcleo de dominio nunca conoce los detalles de persistencia ni la interfaz de usuario. Si la facultad decide en el futuro cambiar el motor de base de datos de PostgreSQL a otra tecnología, las entidades y reglas de negocio del SGC permanecen intactas, protegiendo la inversión institucional de software.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_02_contenedores_c4.png}
    \caption{Diagrama de Contenedores del Modelo C4: Servicios, Puertos y Topología de Red.}
    \label{fig:contenedores_c4}
\end{figure}
\FloatBarrier

\noindent
\textbf{Explicación Técnica del Diagrama C4 de Contenedores:}
El diagrama describe la topología de servicios que interactúan en el ecosistema SIGE. El usuario accede a través del navegador web comunicándose por HTTPS con la aplicación de página única (SPA) en React montada sobre Nginx. La SPA se conecta exclusivamente con la API REST Backend (puerto 5000/3000), la cual autentica cada solicitud mediante tokens JWT. La base de datos PostgreSQL 18 y el almacén MinIO S3 residen en la red interna privada (\textit{bridge}), impidiendo que clientes externos accedan directamente a los puertos de datos sin pasar por la validación de negocio.

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

anx2_3_new = r"""
\subsection*{Anexo: Evidencias de Diagramas UML Dinámicos y de Dominio}

\subsubsection*{1. Desglose Metodológico de los Diagramas Dinámicos (Paso a Paso)}
Para formalizar cómo interactúan los componentes en el tiempo y cómo se orquesta la máquina de estados del plan de trabajo, se modelaron diagramas dinámicos UML 2.5.1 enfocados en los procesos críticos del SGC.

El proceso de especificación técnica comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Modelado del Ciclo de Vida y Transición de Estados:} Se especificó la máquina de estados formal del documento institucional: \textit{Borrador} (docente edita libremente), \textit{En Revisión} (bloqueado para edición tras superar Validation Gates), \textit{Observado} (retornado con observaciones del comité), \textit{Aprobado Comisión} (validado con firma del Coordinador) y \textit{Aprobado HCD} (legalizado con firma del Subdecano en Consejo Directivo).
    \item \textbf{Paso 2: Diagrama de Secuencia de Validación y Persistencia:} Se documentó el intercambio asíncrono de mensajes entre el Cliente React, el Middleware de Validation Gates, el Controlador de Documentos y PostgreSQL, detallando el manejo de excepciones HTTP 422.
    \item \textbf{Paso 3: Diagrama de Clases del Dominio SGC:} Se especificaron las clases de negocio, sus atributos esenciales, sus operaciones y los contratos de invariantes.
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
\textbf{Explicación Técnica del Diagrama de Secuencia:}
El diagrama ilustra el flujo de ejecución cuando el docente pulsa el botón ``Enviar a Revisión''. La petición arriba al servidor donde el middleware intercepta los datos y ejecuta en secuencia estricta los 6 comprobadores lógicos. Si alguna compuerta falla (por ejemplo, si faltan horas para completar las 40h), se interrumpe la ejecución (\textit{fail-fast}), se registra el intento en la bitácora y se retorna un código HTTP 422 con el detalle estructurado. El cliente interpreta el JSON de error y marca visualmente la pestaña observada. Si todas las compuertas devuelven conformidad, se abre una transacción en PostgreSQL, se cambia el estado a ``En Revisión'', se estampa la firma del docente y se notifica al coordinador.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/s2_03_clases_uml.png}
    \caption{Diagrama de Clases del Dominio SGC: Entidades, Relaciones y Contratos de Negocio.}
    \label{fig:clases_uml}
\end{figure}
\FloatBarrier

\noindent
\textbf{Explicación Técnica del Diagrama de Clases:}
La figura modela las entidades del núcleo de negocio. La clase principal \texttt{PlanDocente} actúa como la raíz del agregado (\textit{Aggregate Root}), manteniendo relaciones de composición con \texttt{SeccionDocumento} ($1 \dots N$) y \texttt{ActividadMatriz} ($1 \dots N$). Cada actividad posee una relación opcional con \texttt{EvidenciaAdjunta} ($0 \dots N$), la cual custodia la URL prefirmada y el hash SHA-256. La entidad \texttt{FirmaDocumento} gestiona la cascada secuencial inmutable con multiplicidad de $0 \dots 3$ firmas por expediente.

\subsubsection*{3. Matriz Técnica de Transición de Estados del Documento Institucional}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\hsize=0.45\hsize\centering\arraybackslash\footnotesize}X|>{\hsize=0.95\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.6\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.0\hsize\raggedright\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Paso} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validación Requerida} & \textbf{Estado Resultante} \\
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

anx2_4_new = r"""
\subsection*{Anexo: Evidencias de Diseño Físico y Diccionario del Modelo Relacional}

\subsubsection*{1. Desglose Metodológico del Diseño Relacional (Paso a Paso)}
El diseño físico de la base de datos se fundamentó en la normalización formal en Tercera Forma Normal (3NF) sobre PostgreSQL 18, garantizando que cada atributo dependa de forma directa, no transitiva y completa de su clave primaria.

El proceso de ingeniería de datos comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Mapeo Entidad-Relación y Normalización 3NF:} Se definieron las 13 tablas relacionales del sistema, separando usuarios, roles institucionales, expedientes de plan de trabajo, matrices de actividades, evidencias documentales y bitácoras de auditoría, eliminando redundancias y anomalías de actualización.
    \item \textbf{Paso 2: Declaración de Restricciones CHECK en el Motor:} Para evitar que datos inválidos ingresen a la base de datos incluso en caso de fallo de la API, se programaron restricciones declarativas nativas: \texttt{CHECK (horas >= 0 AND horas <= 40)}, \texttt{CHECK (ponderacion >= 0.00 AND ponderacion <= 100.00)} y validación de estados permitidos.
    \item \textbf{Paso 3: Estrategia de Indexación Física Especializada:} Se implementaron índices B-Tree en todas las claves foráneas (\textit{Foreign Keys}) para optimizar las consultas con \texttt{JOIN}, índices únicos compuestos para la secuencia de firmas \texttt{(fk\_plan, orden)}, e índices GIN sobre campos de texto enriquecido estructurado en formato JSONB.
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
\textbf{Explicación Técnica del Esquema Físico Relacional:}
El diagrama evidencia la estructura normalizada de la base de datos. La tabla central \texttt{plan\_seguimiento} se vincula con la tabla \texttt{users} para identificar al docente responsable y con \texttt{roles} para determinar sus privilegios. La tabla \texttt{seguimiento\_evidencias} mantiene una clave foránea hacia la actividad correspondiente con política de borrado restrictivo (\texttt{ON DELETE RESTRICT}), garantizando que un expediente con evidencias legalizadas nunca pueda ser eliminado accidentalmente, cumpliendo con la exigencia de no repudio de la LOES.

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

anx2_5_new = r"""
\subsection*{Anexo: Evidencias de Diseño de Interfaces, Wireframes y Tokens UI-UX}

\subsubsection*{1. Desglose Metodológico de la Experiencia de Usuario (Paso a Paso)}
El diseño visual y la experiencia de usuario (UI-UX) de SIGE se concibieron para reducir la fricción operativa de los 120 docentes de la FISEI, emulando la familiaridad del formato físico A4 institucional mientras se incorporan las ventajas de la interacción web moderna y accesible.

El proceso de diseño se desarrolló paso a paso:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Definición del Design System y Tokens Cromáticos:} Se formalizaron los tokens oficiales de estilo basados en la identidad gráfica de la Universidad Técnica de Ambato: Rojo Institucional (\texttt{\#A00000}), Azul Marino (\texttt{\#002060}), Gris Fondo (\texttt{\#F8F9FA}) y texto de alto contraste (\texttt{\#1A202C}).
    \item \textbf{Paso 2: Arquitectura de Navegación en Wizard Modular:} Se desglosó el formulario en 5 pasos secuenciales: Paso 1 (Datos Generales y Comisiones), Paso 2 (Docencia y Distribución de 40h), Paso 3 (Matriz Dinámica con recálculo al 100\%), Paso 4 (Medios de Verificación y Carga de Evidencias) y Paso 5 (Revisión y Firmas).
    \item \textbf{Paso 3: Prototipado y Validación de Accesibilidad WCAG 2.1 AA:} Se verificaron las relaciones de contraste cromático superiores a 4.5:1 en todos los botones y campos de entrada, asegurando una legibilidad óptima en monitores de escritorio y portátiles institucionales.
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
\textbf{Explicación Técnica de los Wireframes:}
El diagrama presenta la disposición espacial del sistema web. A la izquierda se sitúa la barra de navegación lateral colapsable institucional, permitiendo transitar entre el Dashboard, la Bandeja de Planes, el Seguimiento y la Administración. El área principal alberga el encabezado institucional con logo oficial y el contenedor de trabajo. En la vista de revisión colegiada, se aprecia el drawer lateral deslizable que permite al coordinador registrar observaciones sin perder la visualización del texto completo del plan docente.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,keepaspectratio]{images/sige_dashboard_resumen.png}
    \caption{Diseño Final Implementado del Tablero de Control (Dashboard Docente).}
    \label{fig:dashboard_ui}
\end{figure}
\FloatBarrier

\noindent
\textbf{Explicación Técnica del Dashboard Implementado:}
La captura superior muestra la implementación final del Dashboard en React. El docente visualiza tres tarjetas métricas directas: total de horas asignadas (40h), horas distribuidas en docencia y tutoría, y porcentaje de avance acumulado. La interfaz incorpora una paleta de colores sobria y accesible con tipografía sans-serif de alta legibilidad, facilitando la identificación inmediata de documentos pendientes de subsanar o aprobados por la comisión.

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

anx2_6_new = r"""
\subsection*{Anexo: Evidencias de Infraestructura y Orquestación Contenerizada}

\subsubsection*{1. Desglose Metodológico de la Contenerización (Paso a Paso)}
Para garantizar que el sistema SIGE pueda ser desplegado de forma idéntica, reproducible y aislada en cualquier estación de trabajo o servidor institucional de la FISEI sin conflictos de versiones, se diseñó la infraestructura basada en contenedores Docker y orquestación unificada.

El procedimiento de despliegue se estructuró paso a paso:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Aislamiento en Red Virtualizada Privada (\textit{Bridge Network}):} Se configuró la red virtual \texttt{sige-network}, interconectando los cinco servicios base y bloqueando el acceso externo directo a la base de datos y al almacenamiento S3.
    \item \textbf{Paso 2: Configuración de Volúmenes de Almacenamiento Persistente:} Se establecieron volúmenes de almacenamiento no volátiles para PostgreSQL (\texttt{postgres\_data}) y MinIO (\texttt{minio\_data}), garantizando que las detenciones o actualizaciones de contenedores no provoquen pérdida de datos.
    \item \textbf{Paso 3: Definición de Mecanismos de Healthcheck y Orden de Arranque:} Se configuraron sondas de salud (\textit{Healthchecks}) mediante el utilitario \texttt{pg\_isready} con sondeos cada 5 segundos. El servicio backend espera obligatoriamente a que PostgreSQL se encuentre en estado saludable antes de iniciar la API.
    \item \textbf{Paso 4: Centralización de Variables de Configuración:} Se parametrizaron credenciales, secretos JWT, nombres de base de datos y puertos mediante variables de entorno centralizadas.
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
\textbf{Explicación Técnica de la Topología de Contenedores:}
El diagrama detalla los cinco contenedores orquestados. El contenedor de frontend expone los puertos 5173 y 80 para la entrega de la aplicación web. El contenedor de backend opera en el puerto 5000/3000 procesando la lógica de negocio. Ambos se comunican internamente con PostgreSQL (puerto 5432) y MinIO (puertos 9000 para API S3 y 9001 para consola de administración). El contenedor de LanguageTool opera de forma autónoma en el puerto 8010 ofreciendo corrección ortográfica local en español, manteniendo todo el tráfico de datos estrictamente confinado dentro del host institucional.

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

anx2_7_new = r"""
\subsection*{Anexo: Expediente de Evaluación de Arquitectura y Decisiones Técnicas (ADRs)}

\subsubsection*{1. Desglose Metodológico de la Auditoría del Hito 2 (Paso a Paso)}
La legalización formal del Hito 2 (Aprobación de la Arquitectura de Software) culminó el 31 de agosto de 2026 tras una revisión técnica colegiada de los siete artefactos de ingeniería de diseño elaborados durante la Fase 2.

El proceso de evaluación formal comprendió:
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Paso 1: Auditoría de Coherencia de Diseño:} Se verificó la alineación estricta entre los Casos de Uso (2.1), el Documento de Arquitectura SAD / C4 (2.2), los Diagramas Dinámicos de Secuencia y Clases (2.3), el Modelo Relacional 3NF (2.4), los Prototipos UX (2.5) y la Orquestación de Contenedores (2.6).
    \item \textbf{Paso 2: Formalización de los 6 Registros de Decisiones de Arquitectura (ADRs):} Se evaluaron formalmente las justificaciones técnicas que sustentan la plataforma: Clean Architecture frente a MVC acoplado, PostgreSQL relacional con soporte JSONB frente a base de datos puramente NoSQL, MinIO local frente a servicios de almacenamiento externo de pago, editor TipTap desacoplado frente a soluciones iframe, y autenticación JWT con tokens de acceso cortos frente a sesiones centralizadas en memoria.
    \item \textbf{Paso 3: Emisión de Dictamen de Aprobación de Fase 2:} Se emitió el dictamen favorable que autoriza el inicio de la Fase 3 de Construcción e Implementación en los cuatro sprints planificados.
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
\textbf{Explicación Técnica del Panel de Cierre de Arquitectura:}
La ilustración evidencia la conclusión satisfactoria de los 7 entregables de la Fase 2, alcanzando un progreso acumulado del 46.2\% del esfuerzo total del proyecto (384 de 832 horas hombre netas). El panel resume los artefactos de ingeniería completados: 8 casos de uso especificados, 13 tablas relacionales en 3NF con restricciones declarativas, tokens de accesibilidad WCAG 2.1 AA validados y la orquestación reproducible en Docker lista para soportar los sprints de desarrollo de la Fase 3.

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
\textbf{EDT 2.1} & Casos de Uso General y Detallado & 24 h & Cobertura total de los 24 RF y actores del SGC bajo OMG UML 2.5.1. & \textbf{APROBADO} \\
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

def safe_replace_anx(pattern, new_val, target_str):
    return re.sub(pattern, lambda m: f'{m.group(1)} = r"""{new_val}"""', target_str, flags=re.DOTALL)

txt = safe_replace_anx(r'(anx2_1)\s*=\s*r?""".*?"""', anx2_1_new, txt)
txt = safe_replace_anx(r'(anx2_2)\s*=\s*r?""".*?"""', anx2_2_new, txt)
txt = safe_replace_anx(r'(anx2_3)\s*=\s*r?""".*?"""', anx2_3_new, txt)
txt = safe_replace_anx(r'(anx2_4)\s*=\s*r?""".*?"""', anx2_4_new, txt)
txt = safe_replace_anx(r'(anx2_5)\s*=\s*r?""".*?"""', anx2_5_new, txt)
txt = safe_replace_anx(r'(anx2_6)\s*=\s*r?""".*?"""', anx2_6_new, txt)
txt = safe_replace_anx(r'(anx2_7)\s*=\s*r?""".*?"""', anx2_7_new, txt)

with open(fname, "w", encoding="utf-8") as f:
    f.write(txt)

print("Updated generate_fase2_enhanced.py with deep step-by-step content, rich visual explanations, and zero Trello/checklist cards!")
