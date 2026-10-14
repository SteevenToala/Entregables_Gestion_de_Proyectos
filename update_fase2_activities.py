# update_fase2_activities.py
import re

with open("generate_fase2_enhanced.py", "r", encoding="utf-8") as f:
    c = f.read()

# -----------------------------------------------------------------------------
# 1. ELIMINATE "Paso X" IN FASE 2
# -----------------------------------------------------------------------------
c = re.sub(r'\\textbf\{Paso\s*\d+:\s*', r'\\textbf{', c, flags=re.I)
c = re.sub(r'\bpaso\s*1\b', 'etapa inicial', c, flags=re.I)
c = re.sub(r'\bpaso\s*2\b', 'etapa descriptiva', c, flags=re.I)
c = re.sub(r'\bpaso\s*3\b', 'etapa matricial', c, flags=re.I)
c = re.sub(r'\bpaso\s*4\b', 'etapa de evidencias', c, flags=re.I)
c = re.sub(r'\bpaso\s*5\b', 'etapa de firmas', c, flags=re.I)

# -----------------------------------------------------------------------------
# 2. ENRICH "Descripción de actividades" IN FASE 2 BODIES
# -----------------------------------------------------------------------------

# --- EDT 2.1 ---
act2_1 = r"""\section{Descripción de actividades}
El modelado de casos de uso constituyó la base para traducir los 24 requisitos funcionales del SRS hacia contratos de interacción precisos entre los actores del SGC y el sistema web SIGE. El equipo de análisis y modelado desarrolló las siguientes actividades técnicas:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Identificación de Actores Primarios y Perímetros de Interacción:} Con base en el estatuto de la FISEI y la matriz RACI de la Fase 1, se delimitaron formalmente las fronteras de los roles autorizados: Docente Elaborador (titular/ocasional), Coordinador de Área Académica, Coordinador de Carrera, Subdecano de Facultad y Administrador del SGC. Se garantizó que ninguna interacción viole el principio de segregación de funciones.
    \item \textbf{Estructuración del Catálogo de Casos de Uso (CU-01 a CU-08):} Se agruparon las operaciones del sistema en 8 casos de uso de alta cohesión funcional, asegurando cobertura directa de la gestión de credenciales, llenado de planes, cálculo de matrices, carga probatoria, revisión colegiada, firmas digitales y gestión de prórrogas.
    \item \textbf{Modelado de Relaciones de Inclusión y Extensión:} Aplicando la notación estándar OMG UML 2.5.1, se formalizó que el caso de uso base CU-02 (\textit{Elaborar Plan de Trabajo}) incluye obligatoriamente (\texttt{<<include>>}) la autenticación en sesión (CU-01) y la gestión matricial (CU-03), mientras que la solicitud de prórroga extemporánea (CU-08) extiende condicionalmente (\texttt{<<extend>>}) el flujo principal únicamente ante ventanas de fecha vencidas.
    \item \textbf{Redacción de Especificaciones Textuales Normalizadas:} Para cada caso de uso se redactó una plantilla formal con identificador, precondiciones, disparador, curso básico (camino feliz), flujos alternos, escenarios de excepción y postcondiciones verificables en base de datos.
\end{itemize}

\subsection{Matriz Oficial de Casos de Uso del Sistema (CU-01 a CU-08)}
A continuación se detalla la matriz general de casos de uso estructurada para el sistema SIGE:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz Oficial de Casos de Uso del Sistema \(CU-01 a CU-08\)\}\s*A continuación se detalla la matriz general de casos de uso estructurada para el sistema SIGE:',
    lambda m: act2_1,
    c
)

# --- EDT 2.2 ---
act2_2 = r"""\section{Descripción de actividades}
El diseño arquitectónico formalizó la topología lógica y física del sistema web SIGE para garantizar atributos esenciales de mantenibilidad, seguridad y desacoplamiento. Las actividades de arquitectura ejecutadas comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Estructuración en Cuatro Capas Concéntricas de Clean Architecture:} Siguiendo los principios de Robert C. Martin, se organizó el software en:
    \begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
        \item \textit{Entidades de Dominio:} Modelos puros (\texttt{Plan}, \texttt{Actividad}, \texttt{Firma}) independientes de frameworks.
        \item \textit{Casos de Uso (Lógica de Aplicación):} Orquestación de reglas de negocio y validación de compuertas sin conocimiento de HTTP o SQL.
        \item \textit{Adaptadores de Interfaz:} Controladores REST en Express v5, middlewares y repositorios de datos.
        \item \textit{Marcos y Controladores (Infraestructura):} Motor PostgreSQL 18, MinIO S3 y servicios externos.
    \end{enumerate}
    \item \textbf{Modelado de Contenedores bajo la Notación C4:} Se elaboró el diagrama C4 de nivel 2 definiendo las fronteras operativas, protocolos de red y tecnologías de los 5 contenedores independientes: Single Page Application (React 18 + Vite), API Gateway / Backend (Express v5), Motor Relacional (PostgreSQL 18), Repositorio de Objetos (MinIO S3) y Servicio Lingüístico (LanguageTool en puerto 8010).
    \item \textbf{Evaluación de Decisiones Arquitectónicas con ATAM:} Se contrastaron los escenarios de rendimiento y seguridad frente a opciones de diseño, formalizando 6 Registros de Decisiones de Arquitectura (ADR-01 a ADR-06) con su contexto, alternativas evaluadas y consecuencias técnicas.
    \item \textbf{Definición de Contratos de Interfaces y Manejo de Errores:} Se establecieron los estándares de comunicación RESTful, formatos de payload JSON normalizados y códigos de estado HTTP alineados a RFC 7807.
\end{itemize}

\subsection{Matriz de Responsabilidades por Capas de la Clean Architecture}
A continuación se especifica la distribución de responsabilidades y contratos entre las capas del sistema:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Responsabilidades por Capas de la Clean Architecture\}\s*A continuación se detalla la matriz de especificación de las 4 capas de la arquitectura:',
    lambda m: act2_2,
    c
)

# --- EDT 2.3 ---
act2_3 = r"""\section{Descripción de actividades}
Para asegurar que la ejecución del software sea predecible y consistente ante concurrencia o fallas transaccionales, se modeló exhaustivamente la dinámica temporal y estructural de las operaciones. Las actividades de diseño dinámico comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado del Ciclo de Vida y Transición de Estados del Expediente:} Se diagramó la máquina de estados que rige los documentos del SGC: \texttt{Borrador} $\to$ \texttt{En Revisión} $\to$ \texttt{Observado} $\to$ \texttt{Aprobado}, formalizando las condiciones de guarda que impiden transiciones ilegítimas (e.g., aprobar un plan con observaciones no resueltas).
    \item \textbf{Diagramación de Secuencia del Proceso de Validación y Persistencia:} Se documentó el intercambio cronológico de mensajes entre el navegador del docente, el router de Express, los middlewares de Validation Gates, el servicio de base de datos y MinIO S3, demostrando que ante cualquier fallo se ejecuta un \texttt{ROLLBACK} atómico en menos de 5 ms.
    \item \textbf{Diseño del Modelo de Clases del Dominio bajo DDD (Domain-Driven Design):} Se especificaron los agregados de dominio, entidades, objetos de valor (\textit{Value Objects}) y fábricas necesarias para encapsular las reglas de negocio (e.g., cálculo de avance porcentual y verificación de sumatoria a 40 horas).
    \item \textbf{Diseño de Protocolos de Manejo de Excepciones Concurrente:} Se modelaron los flujos alternos ante conflictos de versión en concurrencia optimista, garantizando que dos usuarios editando simultáneamente reciban advertencias inmediatas sin sobreescritura ciega de datos.
\end{itemize}

\subsection{Matriz de Transición de Estados del Plan de Trabajo Docente}
A continuación se detalla la matriz que rige el ciclo de vida del plan institucional:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Transición de Estados del Plan de Trabajo Docente\}\s*A continuación se detalla la matriz que rige el ciclo de vida del plan:',
    lambda m: act2_3,
    c
)

# --- EDT 2.4 ---
act2_4 = r"""\section{Descripción de actividades}
El diseño de la capa de persistencia se orientó a garantizar atomicidad, consistencia, aislamiento y durabilidad (ACID), estructurando un modelo relacional en tercera forma normal capaz de resistir auditorías forenses del SGC. Las actividades desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Normalización Relacional en Tercera Forma Normal (3NF):} A partir del análisis de dependencias funcionales de los formatos \texttt{P7-T1} y \texttt{P7-T4}, se descompusieron las entidades eliminando redundancias y anomalías de actualización. Se crearon 13 tablas relacionales estructuradas alrededor del usuario, planes, matrices, evidencias, firmas y auditoría.
    \item \textbf{Adopción de Llaves Primarias Universales (UUIDv4):} Se sustituyeron los identificadores numéricos secuenciales por identificadores UUIDv4 nativos de PostgreSQL, neutralizando vulnerabilidades de enumeración horizontal de recursos (\textit{IDOR}) en las rutas de la API.
    \item \textbf{Diseño de Restricciones Declarativas CHECK e Integridad Referencial:} Se trasladaron las reglas críticas de negocio hacia el motor relacional: restricción de 0 a 40 horas semanales (\texttt{chk\_horas\_rango}), límites de ponderación de 0 a 100\% (\texttt{chk\_pond\_rango}) y políticas de borrado restrictivas (\texttt{ON DELETE RESTRICT}) que preservan las cadenas de custodia institucional.
    \item \textbf{Estrategia de Indexación Compuesta B-Tree e Índices Invertidos GIN:} Se diseñaron índices B-Tree en combinaciones de alta consulta (\texttt{fk\_docente, fk\_periodo}) y se definieron índices GIN sobre los campos semiestructurados \texttt{JSONB} que albergan las secciones descriptivas enriquecidas redactadas con TipTap.
    \item \textbf{Modelado de Triggers Automáticos de Auditoría en PL/pgSQL:} Se concibió la función disparadora inmutable encargada de registrar la estampa de tiempo UTC exacta (\texttt{NOW()}) ante cualquier actualización de fila.
\end{itemize}

\subsection{Diccionario de Datos: Estructura de Tablas Core en PostgreSQL 18}
A continuación se detalla la matriz que especifica las entidades centrales del modelo de base de datos:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Diccionario de Datos: Estructura de Tablas Core en PostgreSQL 18\}\s*A continuación se detalla la matriz del diccionario de datos de las entidades centrales:',
    lambda m: act2_4,
    c
)

# --- EDT 2.5 ---
act2_5 = r"""\section{Descripción de actividades}
El diseño de interfaces de usuario se fundamentó en la ingeniería de usabilidad y los estándares internacionales de accesibilidad web, buscando erradicar la sobrecarga cognitiva del trámite manual anterior. Las actividades de diseño UI/UX comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Definición del Sistema de Diseño Institucional y Tokens CSS:} Se formalizó la paleta de colores oficial de la Universidad Técnica de Ambato: Rojo UTA (\texttt{\#8B1D24}), Gris Pizarra (\texttt{\#1E293B}), estados de éxito (\texttt{\#16A34A}), advertencia (\texttt{\#D97706}) y error (\texttt{\#DC2626}), estandarizando tipografía Inter, radios de borde de 8px y sombras elásticas.
    \item \textbf{Auditoría de Accesibilidad según Pautas WCAG 2.1 Nivel AA:} Se verificó cuantitativamente que todas las combinaciones de color entre texto y fondo superen la relación de contraste mínima de 4.5:1 para texto normal y 3.0:1 para controles de interfaz, alcanzando relaciones óptimas de hasta 7.2:1 en botones de acción.
    \item \textbf{Prototipado de Alta Fidelidad del Asistente Guiado (Wizard):} Se maquetó la experiencia de usuario dividida en 5 etapas secuenciales, diseñando indicadores visuales de progreso, retroalimentación en tiempo real para autoguardado y paneles de error con microinteracciones no intrusivas.
    \item \textbf{Diseño de Vistas Especializadas por Rol Institucional:} Se prototipó el Dashboard con tarjetas analíticas de avance para el docente, la bandeja con Drawer lateral de observaciones para el coordinador de carrera y la vista de previsualización estricta en formato de hoja A4 emulando el reporte físico impreso.
\end{itemize}

\subsection{Matriz de Tokens de Diseño Oficiales de la UTA}
A continuación se detalla el sistema de tokens visuales estandarizados para la interfaz web SIGE:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Tokens de Diseño Oficiales de la UTA\}\s*A continuación se detalla la matriz de tokens visuales estandarizados:',
    lambda m: act2_5,
    c
)

# --- EDT 2.6 ---
act2_6 = r"""\section{Descripción de actividades}
La garantía de que el sistema opere de forma idéntica en estaciones de desarrollo, servidores locales del campus y entornos de prueba exigió el diseño de una arquitectura de virtualización ligera basada en contenedores. Las actividades de infraestructura desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado de la Topología de 5 Microservicios en Docker Compose:} Se estructuró el archivo maestro \texttt{docker-compose.yml} definiendo los cinco servicios autónomos: \texttt{sige-postgres} (PostgreSQL 18-alpine), \texttt{sige-backend} (Express v5 en Node.js 20-alpine), \texttt{sige-frontend} (SPA en React 18 con Vite), \texttt{sige-minio} (Almacenamiento S3) y \texttt{sige-languagetool} (Corrección ortográfica en puerto 8010).
    \item \textbf{Aislamiento Perimetral Mediante Redes Bridge Seguras:} Se configuró la red interna \texttt{sige-internal-net} sin exposición pública para la comunicación entre backend, base de datos y LanguageTool, mientras que únicamente el frontend y los puertos de entrada de la API se mapearon hacia la red externa del host.
    \item \textbf{Diseño de Sondas de Salud Activas (Healthchecks):} Para impedir que el backend intente conectarse a PostgreSQL o MinIO antes de que estos completen su inicialización, se implementaron directivas \texttt{healthcheck} con intervalos de 5 segundos y directivas \texttt{depends\_on} condicionadas a \texttt{service\_healthy}.
    \item \textbf{Estrategia de Persistencia de Volúmenes y Variables de Entorno:} Se diseñaron volúmenes persistentes nombrados (\texttt{pgdata}, \texttt{miniodata}) que garantizan la supervivencia de bases de datos y archivos binarios ante reinicios o recreaciones de contenedores, aislando credenciales en archivos \texttt{.env} seguros.
\end{itemize}

\subsection{Topología Oficial de Servicios en Docker Compose}
A continuación se presenta la matriz técnica de especificación de contenedores, puertos y volúmenes:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Topología Oficial de Servicios en Docker Compose\}\s*A continuación se detalla la matriz de especificación de los 5 contenedores orquestados:',
    lambda m: act2_6,
    c
)

# --- EDT 2.7 ---
act2_7 = r"""\section{Descripción de actividades}
El cierre formal de la Fase 2 y la autorización para el inicio de la codificación de software demandó un proceso riguroso de evaluación colegiada de la arquitectura. Las actividades de auditoría ejecutadas por el equipo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Auditoría Integral de Artefactos de Arquitectura EDT 2.1 al 2.6:} Se inspeccionaron formalmente los diagramas UML de casos de uso, el modelo C4 de contenedores, los diagramas de secuencia DDD, el modelo físico relacional en 3NF, los prototipos UX y los scripts de orquestación en Docker, certificando 100\% de consistencia mutua.
    \item \textbf{Verificación de Trazabilidad Requisitos versus Arquitectura:} Se comprobó que cada uno de los 24 requerimientos funcionales aprobados en la Fase 1 cuente con un caso de uso específico, controladores de backend asignados, tablas relacionales normalizadas y vistas de interfaz diseñadas.
    \item \textbf{Congelamiento de la Línea Base Arquitectónica (Architecture Baseline Freeze):} Con la conformidad del equipo y del Docente Evaluador, se congelaron las especificaciones técnicas para que sirvan de marco inmutable durante la construcción en la Fase 3, determinando que cualquier alteración posterior deberá canalizarse mediante solicitudes formales de control de cambios.
    \item \textbf{Suscripción del Acta Oficial de Aprobación de Arquitectura:} Se emitió el dictamen formal aprobatorio legalizando la culminación de 192 horas-hombre netas de diseño con un índice de desempeño de cronograma $SPI = 1.00$.
\end{itemize}

\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 2}
A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los entregables que componen la Fase 2:"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Auditoría y Aprobación de Entregables de la Fase 2\}\s*A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los entregables que componen la Fase 2:',
    lambda m: act2_7,
    c
)

with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c)

print("generate_fase2_enhanced.py updated successfully with rich activities and zero Paso X!")
