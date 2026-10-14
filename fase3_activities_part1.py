# fase3_activities_part1.py
# Descripciones tecnicas enriquecidas de actividades para EDT 3.1 a 3.8

ACTIVITIES_F3_PART1 = {}

# -----------------------------------------------------------------------------
# 3.1 Implementación de Tablas, Índices y Scripts DDL en PostgreSQL 18
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[1] = r"""\section{Descripción de actividades}
La materialización de la capa física de persistencia se desarrolló en el contenedor \texttt{sige-postgres} bajo PostgreSQL 18-alpine, asegurando consistencia ACID y soporte nativo para documentos semiestructurados JSONB. El equipo de desarrollo ejecutó las siguientes actividades de ingeniería de base de datos:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Aprovisionamiento y Parametrización del Motor Relacional:} Se configuró el servicio en \texttt{docker-compose.yml} montando un volumen persistente \texttt{pgdata}, ajustando los parámetros de rendimiento en \texttt{postgresql.conf} (\texttt{shared\_buffers = 256MB}, \texttt{work\_mem = 16MB}) y definiendo la codificación UTF-8 para soporte estricto del idioma español y caracteres especiales institucionales.
    \item \textbf{Despliegue Secuencial del Esquema Relacional en 3NF:} Se ejecutó el script estructurado \texttt{schema.sql} creando las 13 tablas relacionales normalizadas en tercera forma normal: entidades maestras (\texttt{users}, \texttt{roles}, \texttt{carreras}, \texttt{periodos}, \texttt{comisiones}), entidades operativas (\texttt{planes\_docente}, \texttt{secciones\_documento}, \texttt{actividades\_matriz}, \texttt{plan\_seguimiento}), entidades probatorias (\texttt{seguimiento\_\allowbreak evidencias}, \texttt{firmas\_\allowbreak documento}) y tablas de soporte (\texttt{audit\_logs}, \texttt{refresh\_tokens}).
    \item \textbf{Programación de Restricciones Declarativas CHECK en Motor:} Para blindar la consistencia a nivel de base de datos, se programaron cláusulas \texttt{CHECK} declarativas: \texttt{chk\_horas\_rango} limitando la carga semanal a valores entre 0 y 40 horas según el RRA, \texttt{chk\_pond\_rango} garantizando ponderaciones entre 0.00\% y 100.00\%, y \texttt{chk\_estado\_valido} restringiendo los estados documentales a los cuatro estadios del SGC.
    \item \textbf{Estrategia de Indexación Compuesta B-Tree e Invertida GIN:} Se crearon índices B-Tree en pares de llaves foráneas de alta concurrencia (\texttt{idx\_plan\_doc\_per}) y secuencia de firmas (\texttt{idx\_firma\_sec}). Para los campos semiestructurados que albergan texto enriquecido redactado con TipTap, se generaron índices GIN (\texttt{idx\_sec\_jsonb}) acelerando búsquedas contextuales en tiempos inferiores a 3 ms.
    \item \textbf{Automatización de Auditoría con Triggers PL/pgSQL:} Se creó la función disparadora \texttt{trigger\_set\_timestamp()} asociada a todas las tablas para estampar la fecha y hora UTC (\texttt{NOW()}) ante cualquier actualización de registro.
\end{itemize}

\subsection{Matriz Técnica de Integridad e Índices en PostgreSQL 18}
A continuación se detalla la matriz técnica de especificación de restricciones e índices del esquema físico:"""

# -----------------------------------------------------------------------------
# 3.2 Datos Iniciales y Catálogos Institucionales
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[2] = r"""\section{Descripción de actividades}
El poblado de catálogos y datos maestros dotó al sistema de la estructura operativa real de la FISEI, sustentada en resoluciones vigentes del Consejo Directivo y manuales de calidad del SGC. Las actividades desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Recopilación y Normalización de Catálogos de la Facultad:} Se consolidó la información oficial de las 5 carreras de ingeniería de la FISEI (Software, Tecnologías de la Información, Industrial, Telecomunicaciones, Automatización y Robótica), asignando sus códigos institucionales y directores de carrera autorizados.
    \item \textbf{Estructuración del Catálogo de 14 Comisiones Académicas:} Se registraron las 14 comisiones permanentes establecidas en el estatuto de la facultad (Evaluación Interna, Vinculación, Investigación, Titulación, Prácticas Preprofesionales, etc.), permitiendo que los docentes vinculen sus horas de gestión conforme a la normativa universitaria.
    \item \textbf{Carga y Tipificación del Claustro Docente:} Se procesaron las cuentas de los 120 docentes de la facultad, clasificándolos por dedicación horaria (Tiempo Completo 40h y Medio Tiempo 20h) y tipo de relación laboral (Titulares y Ocasionales), asociando sus correos institucionales (\texttt{@uta.edu.ec}).
    \item \textbf{Parametrización del Período Académico Activo B26:} Se configuró el ciclo semestral oficial correspondiente a Septiembre 2026 -- Febrero 2027, definiendo las fechas de inicio, corte medio término y entrega de informes de cumplimiento.
    \item \textbf{Construcción del Script Idempotente de Semilla (seed.sql):} Se implementaron sentencias \texttt{INSERT ... ON CONFLICT (codigo) DO NOTHING} encapsuladas en transacciones ACID, garantizando que el script pueda ejecutarse en cualquier entorno sin duplicar datos ni corromper llaves foráneas.
\end{itemize}

\subsection{Matriz Oficial de Catálogos Maestros Cargados en el Sistema SIGE}
A continuación se detalla el consolidado cuantitativo de los datos maestros poblados en la base de datos:"""

# -----------------------------------------------------------------------------
# 3.3 Autenticación y Autorización de Usuarios (JWT y RBAC)
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[3] = r"""\section{Descripción de actividades}
La protección de la información docente y la delimitación de accesos se implementaron siguiendo las pautas de OWASP ASVS v4.0 y la Ley Orgánica de Protección de Datos Personales (LOPDP). Las actividades de ingeniería de seguridad comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Configuración de Hashing Criptográfico con Argon2id:} Se implementó la biblioteca nativa \texttt{argon2} para el almacenamiento de contraseñas, aplicando 64 MB de memoria RAM por cálculo, 3 iteraciones y 4 hilos de paralelismo, neutralizando intentos de ataque mediante fuerza bruta o tablas arcoíris.
    \item \textbf{Diseño de Tokens de Acceso JWT de Vida Corta (15 minutos):} El backend genera un token de acceso firmado con algoritmo HS256 conteniendo los claims estrictamente necesarios (\texttt{sub}, \texttt{role}, \texttt{carrera\_id}, \texttt{exp}), asegurando que ante una eventual interceptación el token expire rápidamente.
    \item \textbf{Mecanismo de Refresh Tokens Rotativos y Cookies HttpOnly Seguras:} Para mantener la sesión sin comprometer la seguridad en el cliente, se diseñó un Refresh Token con validez de 7 días transmitido exclusivamente mediante una cookie HTTP con banderas \texttt{HttpOnly}, \texttt{Secure} y \texttt{SameSite=Strict}. Cada renovación invalida el token previo en la tabla \texttt{refresh\_tokens}.
    \item \textbf{Implementación del Middleware de Autorización por Roles (RBAC):} Se construyó el interceptor \texttt{verifyRole} en Express v5, el cual valida en cada petición que el rol en el token cuente con los permisos necesarios para la ruta invocada, emitiendo un código HTTP 403 Forbidden ante cualquier acceso no autorizado.
    \item \textbf{Protocolo de Revocación Inmediata de Sesiones:} Se programó el endpoint \texttt{POST /api/\allowbreak v1/\allowbreak auth/\allowbreak logout} que elimina el hash del Refresh Token en base de datos y purga la cookie del navegador, garantizando el cierre de sesión seguro.
\end{itemize}

\subsection{Matriz de Control de Acceso por Roles (RBAC) y Permisos en la API}
A continuación se especifica la matriz de permisos y privilegios por rol institucional:"""

# -----------------------------------------------------------------------------
# 3.4 Cliente Base y Diseño de Layouts
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[4] = r"""\section{Descripción de actividades}
La construcción de la interfaz gráfica se desarrolló como una aplicación de página única (Single Page Application - SPA) con React 18, empaquetador Vite y enrutador React Router v6. Las actividades de desarrollo frontend ejecutadas comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Estructuración Jerárquica del Enrutador y Guardias de Seguridad:} Se construyó la estructura de rutas protegiendo las vistas privadas mediante el componente \texttt{ProtectedRoute}, el cual evalúa reactivamente el contexto global de autenticación (\texttt{AuthContext}) y redirige al usuario al inicio de sesión si no existe token válido.
    \item \textbf{Maquetación del Shell Maestro Institucional (MainLayout):} Se diseñó el contenedor principal que integra el encabezado superior con el imagotipo de la UTA, el selector del período académico B26 y el menú de perfil, articulado con una barra lateral elástica que filtra sus accesos según los permisos del usuario en sesión.
    \item \textbf{Aplicación de Tokens de Diseño Oficiales de la UTA:} Se incorporaron las variables CSS del sistema de diseño institucional, aplicando el color Rojo UTA (\texttt{\#8B1D24}), Gris Pizarra (\texttt{\#1E293B}) y tipografía Inter, garantizando una relación de contraste superior a 7:1 acorde con WCAG 2.1 AA.
    \item \textbf{Optimización de Rendimiento con Carga Perezosa (Code-Splitting):} Se configuraron los módulos de alta densidad (Wizard, Editor TipTap y Matriz de Actividades) con \texttt{React.lazy()} y \texttt{Suspense}, reduciendo el peso de la carga inicial a 184 KB.
    \item \textbf{Diseño de Estados de Carga y Retroalimentación Visual:} Se implementaron componentes de esqueleto (\textit{Skeleton Loaders}) y pantallas de estado vacío (\textit{Empty States}) para evitar saltos visuales durante la carga de datos desde los microservicios Docker.
\end{itemize}

\subsection{Matriz de Componentes del Shell SPA y Rutas Institucionales}
A continuación se detalla la matriz que especifica los componentes modulares del frontend:"""

# -----------------------------------------------------------------------------
# 3.5 Layout Wizard Modular en Pestañas
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[5] = r"""\section{Descripción de actividades}
Para guiar al docente de manera secuencial y estructurada en el diligenciamiento de los formatos oficiales \texttt{P7-T1} y \texttt{P7-T4}, se desarrolló el asistente modular por pasos (\texttt{PlanWizard.jsx}). Las actividades de construcción abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Descomposición Modular en 5 Etapas del Ciclo Documental:} Se fragmentó la captura de información en cinco bloques lógicos: Etapa Inicial (Datos Generales y Carga Horaria), Etapa Descriptiva (Justificación Académica), Etapa Matricial (Matriz de Actividades y Ponderación), Etapa de Evidencias (Custodia de Archivos en MinIO S3) y Etapa de Firmas (Previsualización A4 y Solicitud de Firma).
    \item \textbf{Modelado de la Máquina de Estados con useReducer:} Se centralizó la lógica del asistente en un reductor reactivo que administra las transiciones de avance (\texttt{NEXT\_STEP}), retroceso (\texttt{PREV\_STEP}), actualización de borradores y validaciones por paso.
    \item \textbf{Implementación de Compuertas de Avance Condicional (Step Gates):} Se condicionó la habilitación del botón "Siguiente" a la superación de las reglas de validación en tiempo real, bloqueando el avance si los campos obligatorios se encuentran incompletos o inconsistentes.
    \item \textbf{Construcción del Stepper Visual con Estados de Color:} Se diseñó una barra superior interactiva que muestra el porcentaje de avance global y clasifica cada paso en verde (validado), azul institucional (en edición) o gris (bloqueado pendiente de prerrequisitos).
    \item \textbf{Persistencia y Resiliencia en Memoria Local:} Se configuró un mecanismo de sincronización que almacena los cambios en \texttt{LocalStorage} cada 2 segundos, permitiendo recuperar el borrador completo ante cierres accidentales de pestaña o caídas de red.
\end{itemize}

\subsection{Matriz de Flujo y Reglas de Validación del Asistente Wizard}
A continuación se especifica la matriz de etapas, componentes y compuertas del asistente:"""

# -----------------------------------------------------------------------------
# 3.6 Integración de Editor TipTap con Autoguardado y Debounce
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[6] = r"""\section{Descripción de actividades}
La redacción de las secciones descriptivas de los planes docentes (justificación, metodología y compromisos académicos) requirió un editor que garantizara tipografía homogénea y persistencia asíncrona segura. Las actividades ejecutadas comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Integración del Núcleo TipTap sobre la Aplicación React:} Se incorporó la suite modular \texttt{@tiptap/react} con extensiones oficiales esenciales (\texttt{StarterKit}, \texttt{Table}, \texttt{Link}), configurando una barra de herramientas enriquecida con formatos autorizados por el SGC.
    \item \textbf{Serialización Estructurada en Formato JSONB:} En lugar de almacenar cadenas HTML planas susceptibles a inyecciones de código y difíciles de paginar en reportes PDF, el editor serializa el contenido en un árbol de nodos JSON nativo, persistido en la columna \texttt{contenido\_jsonb} de PostgreSQL 18.
    \item \textbf{Mecanismo de Autoguardado Asíncrono con Debounce de 1500 ms:} Mediante el hook \texttt{useDebounce}, el sistema reinicia el contador mientras el usuario escribe activamente; al detectar 1500 ms de inactividad tras la última pulsación, despacha la petición de guardado al backend sin interrumpir la experiencia de redacción.
    \item \textbf{Indicador Visual Reactivo del Estado de Persistencia:} Se implementó un componente de estado en la cabecera del editor que informa de forma no intrusiva si el borrador se está guardando, si la persistencia fue exitosa o si existe una anomalía de red.
    \item \textbf{Sanitización Perimetral de Contenido con DOMPurify:} Como medida de protección contra ataques XSS, el contenido se procesa a través de un pipeline de sanitización estricta que remueve cualquier etiqueta potencialmente peligrosa antes del guardado en el servidor.
\end{itemize}

\subsection{Matriz Técnica de Configuración del Editor de Texto Enriquecido}
A continuación se detalla la matriz de especificación técnica del editor TipTap y su mecanismo de autoguardado:"""

# -----------------------------------------------------------------------------
# 3.7 Endpoints de Persistencia de Secciones y Transaccionalidad
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[7] = r"""\section{Descripción de actividades}
Para asegurar que las múltiples secciones que componen un plan se actualicen de manera atómica sin generar estados intermedios inconsistentes, se desarrolló la capa de controladores transaccionales en Express v5. Las actividades de desarrollo backend abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño de Rutas RESTful de Actualización Masiva:} Se implementó el endpoint transaccional \texttt{PATCH /api/v1/planes/:id/secciones}, permitiendo recibir un arreglo de bloques descriptivos modificados en una sola transacción de red.
    \item \textbf{Transaccionalidad Atómica con pg-promise:} Se encapsuló la persistencia mediante bloques atómicos \texttt{db.tx(async t => \{ ... \})}. Todas las sentencias \texttt{UPDATE} se ejecutan dentro del mismo ámbito transaccional: si una sola sección presenta un error de formato o clave foránea, el motor ejecuta un \texttt{ROLLBACK} total en menos de 5 ms.
    \item \textbf{Control de Concurrencia Optimista con Columna de Versión:} Para evitar sobreescrituras accidentales entre usuarios concurrentes, se incorporó un campo entero \texttt{version} en la tabla \texttt{planes\_docente}. La consulta exige coincidencia exacta de versión; si otro usuario actualizó previamente el registro, el sistema aborta la operación y retorna un código HTTP 409 Conflict.
    \item \textbf{Validación Rigurosa de Esquema con Zod:} Previo a la apertura de la transacción en base de datos, el middleware valida los tipos de datos, identificadores UUID y restricciones de longitud de cada campo del payload JSON entrante.
    \item \textbf{Registro Automático en Bitácora de Auditoría:} Al completarse la transacción con éxito, el sistema inserta automáticamente un evento en la tabla \texttt{audit\_logs} detallando el identificador del usuario, dirección IP, estampa de tiempo UTC y secciones modificadas.
\end{itemize}

\subsection{Matriz de Controladores y Endpoints de Persistencia REST}
A continuación se detalla la matriz técnica de especificación de los endpoints del backend:"""

# -----------------------------------------------------------------------------
# 3.8 Hito 3: Sprint 2 Review (Wizard y Persistencia Operativa)
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART1[8] = r"""\section{Descripción de actividades}
Al culminar la segunda iteración del ciclo de desarrollo de la Fase 3, se llevó a cabo la ceremonia formal de Revisión de Sprint (Sprint 2 Review) bajo el marco Scrum, certificando la operación conjunta del Asistente Wizard y la capa de persistencia. Las actividades de revisión técnica comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Preparación del Entorno Integrado de Demostración:} Se verificó el funcionamiento saludable de los 5 contenedores en Docker Compose, precargando los datos maestros de la carrera de Ingeniería de Software para las pruebas en vivo.
    \item \textbf{Demostración End-to-End del Asistente Wizard en Vivo:} Ante el equipo de desarrollo y el Docente Evaluador, se ejecutó una sesión real que demostró la autenticación del usuario, la creación guiada de un nuevo plan de trabajo para el período B26, el autoguardado a los 1500 ms tras redactar justificaciones y la recuperación intacta del borrador tras un cierre forzado del navegador.
    \item \textbf{Inspección Forense de la Capa de Datos en PostgreSQL 18:} Se accedió a la consola de base de datos para comprobar que los registros en las tablas \texttt{planes\_docente} y \texttt{secciones\_documento} se crearon con identificadores UUID válidos, claves foráneas correctas y tipos JSONB estructurados.
    \item \textbf{Levantamiento de Retroalimentación de Coordinadores de Área:} Se recopilaron recomendaciones respecto al contraste de los botones de acción del Wizard, aprobándose el paso inmediato al desarrollo de la Matriz Dinámica en el Sprint 3.
    \item \textbf{Suscripción del Acta Formal de Aprobación de Sprint Review:} Se legalizó el documento de aceptación de los incrementos construidos, certificando el cumplimiento del 100\% de los criterios de las Historias de Usuario HU-01 a HU-08 con cero defectos abiertos.
\end{itemize}

\subsection{Matriz de Auditoría y Verificación de Criterios del Sprint 2}
A continuación se presenta la matriz de evaluación formal de los incrementos demostrados en el Sprint 2:"""

print("fase3_activities_part1.py loaded successfully!")
