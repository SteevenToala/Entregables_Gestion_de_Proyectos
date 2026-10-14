# fase3_activities_part2.py
# Descripciones tecnicas enriquecidas de actividades para EDT 3.9 a 3.16

ACTIVITIES_F3_PART2 = {}

# -----------------------------------------------------------------------------
# 3.9 Desarrollo de la Matriz Dinámica de Actividades
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[9] = r"""\section{Descripción de actividades}
La matriz de distribución de actividades semanales constituye el núcleo operativo del formato \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T1}. Su construcción en React demandó un manejo exhaustivo de estados reactivos y reglas de balance matemático estrictas. Las actividades técnicas comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado del Estado Complejo con useReducer:} Se estructuró un reductor que gestiona las operaciones tabulares: adición de actividades, edición de descripciones, clasificación por componentes (Docencia, Investigación, Tutorías y Gestión), asignación de horas semanales y cálculo de ponderaciones porcentuales.
    \item \textbf{Cálculo Reactivo de Balances Matemáticos en Tiempo Real:} Mediante hooks optimizados con \texttt{useMemo}, la matriz recalcula continuamente dos indicadores críticos:
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item \textbf{Balance de Carga Horaria Semanal:} Debe sumar exactamente 40.0 horas semanales para docentes de dedicación a tiempo completo (o 20.0h para tiempo parcial) conforme a los Arts. 45 y 67 del Reglamento de Régimen Académico.
        \item \textbf{Balance de Ponderación Porcentual:} La suma acumulada de los pesos asignados a cada actividad debe totalizar exactamente 100.00\%.
    \end{itemize}
    \item \textbf{Construcción del Selector Matricial de 16 Semanas:} Se desarrolló una cuadrícula interactiva con casillas de verificación para las 16 semanas del ciclo semestral B26, calculando el total de horas semestrales por actividad de forma automatizada.
    \item \textbf{Insignias Visuales Condicionales de Control de Calidad:} Si las horas difieren de 40.0 o la ponderación no suma 100.00\%, la interfaz despliega badges rojos de advertencia y bloquea el avance en el Wizard. Cuando ambas sumatorias son exactas, las insignias conmutan a color verde con la leyenda "Conforme con Normativa RRA".
    \item \textbf{Persistencia Lote y Validación de Restricciones CHECK:} Los cambios se persisten en la tabla \texttt{actividades\_matriz} mediante sentencias en lote que respetan las restricciones declarativas del motor relacional.
\end{itemize}

\subsection{Matriz de Parámetros y Reglas de la Matriz Dinámica de Actividades}
A continuación se detalla la matriz que especifica los componentes, pesos y validaciones del cálculo matricial:"""

# -----------------------------------------------------------------------------
# 3.10 Reglas de Negocio, Validation Gates y Middlewares en Express v5
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[10] = r"""\section{Descripción de actividades}
Para blindar al sistema contra datos anómalos y garantizar que ningún expediente avance al comité de revisión sin cumplir los requisitos del SGC, se implementó la cadena de Validation Gates en el backend Express v5. Las actividades de desarrollo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Arquitectura de la Cadena de Responsabilidad (Middleware Chain):} Se diseñó una serie de interceptores que evalúan de forma temprana (\textit{fail-fast}) las condiciones antes de procesar cambios de estado o persistencia definitiva en base de datos.
    \item \textbf{Implementación de la Compuerta VG-1 (Integridad Horaria RRA):} Extrae las actividades del plan y ejecuta \texttt{SUM(horas)}. Si el resultado no coincide con la dedicación contractual del docente (40h tiempo completo o 20h medio tiempo), interrumpe el flujo y responde inmediatamente con código HTTP 422.
    \item \textbf{Implementación de la Compuerta VG-2 (Ponderación Absoluta al 100\%):} Verifica mediante precisión decimal (\texttt{Math.abs(sum - 100.0) < 0.001}) que el porcentaje total sea exactamente 100.00\%, evitando desbalances en la evaluación de fin de ciclo.
    \item \textbf{Implementación de la Compuerta VG-3 (Custodia Obligatoria de Evidencias):} Al procesar un Informe de Cumplimiento (\texttt{P7-T4}), si una actividad reporta un porcentaje de avance mayor a cero (\texttt{avance > 0}), exige la existencia de al menos un registro vinculado en la tabla \texttt{seguimiento\_\allowbreak evidencias} con archivo verificado en MinIO S3.
    \item \textbf{Implementación de la Compuerta VG-4 (Justificación Obligatoria ante Desvíos):} Si el avance real alcanzado presenta un desvío negativo mayor al 15\% respecto a lo planificado, la compuerta rechaza la solicitud si el campo de justificación cualitativa contiene menos de 30 caracteres.
    \item \textbf{Estandarización de Respuestas de Error bajo RFC 7807:} Todos los rechazos retornan un objeto JSON con estructura estandarizada: código de error, compuerta infractora, detalle del desvío numérico y recomendación de remediación para el usuario.
\end{itemize}

\subsection{Matriz Técnica de Especificación de las Validation Gates (VG-1 a VG-6)}
A continuación se detalla la matriz que consolida las reglas, compuertas y códigos de retorno del middleware:"""

# -----------------------------------------------------------------------------
# 3.11 Integración de MinIO S3 y Evidencias Digitales
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[11] = r"""\section{Descripción de actividades}
La custodia digital de respaldos docentes (actas de notas, registros de asistencia, fotos y sílabos) se implementó bajo una arquitectura de almacenamiento compatible con Amazon S3 utilizando MinIO en contenedor Docker local. Las actividades de desarrollo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Aprovisionamiento de MinIO en Docker Compose:} Se configuró el servicio \texttt{sige-minio} escuchando en el puerto 9000 (API S3) y puerto 9001 (Consola de Administración), montando un volumen persistente \texttt{miniodata} para resguardo de objetos.
    \item \textbf{Creación Automática del Bucket Institucional:} Mediante un script de inicialización con el cliente \texttt{mc} (MinIO Client), se automatizó la creación del bucket privado \texttt{sige-evidencias}, aplicando una política de acceso que prohíbe terminantemente la lectura pública sin token.
    \item \textbf{Controlador de Carga Segura con Multer y Magic Bytes:} El backend procesa las subidas filtrando extensiones autorizadas (\texttt{.pdf}, \texttt{.png}, \texttt{.jpg}) y validando los primeros bytes del archivo (\textit{magic bytes}) para neutralizar archivos ejecutables camuflados. Se estableció un límite estricto de 10 MB por archivo.
    \item \textbf{Generación de Huella Criptográfica SHA-256:} Al recibir el flujo de bytes, el backend calcula la suma de verificación SHA-256 del archivo y la almacena en la tabla \texttt{seguimiento\_\allowbreak evidencias}, garantizando la inmutabilidad y la no alteración del documento en auditorías posteriores.
    \item \textbf{Emisión de URLs Prefirmadas con Expiración a 900 Segundos (15 min):} Para la descarga y previsualización de evidencias por parte de coordinadores y evaluadores, el backend genera enlaces temporales firmados criptográficamente mediante la función \texttt{presigned\allowbreak GetObject()}. Una vez transcurridos 15 minutos, el enlace expira automáticamente en MinIO.
\end{itemize}

\subsection{Matriz de Especificación del Repositorio de Evidencias en MinIO S3}
A continuación se detalla la matriz técnica de configuración del almacenamiento de objetos:"""

# -----------------------------------------------------------------------------
# 3.12 Hito 4: Sprint 3 Review (Matriz Dinámica y Evidencias MinIO)
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[12] = r"""\section{Descripción de actividades}
Al culminar el Sprint 3 de desarrollo, se ejecutó la sesión formal de demostración y revisión de sprint bajo metodología Scrum, focalizada en validar la integración entre la Matriz Dinámica, las Validation Gates y el almacenamiento en MinIO S3. Las actividades de demostración comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Preparación del Entorno Integrado de Demostración:} Se verificó el funcionamiento conjunto de los contenedores \texttt{sige-backend}, \texttt{sige-postgres} y \texttt{sige-minio}, precargando un informe de cumplimiento semestral para pruebas en vivo.
    \item \textbf{Demostración de la Matriz Dinámica en Tiempo Real:} Se mostró la distribución de 40 horas en 6 actividades académicas y la asignación del cronograma en 16 semanas. Se ejecutó una alteración deliberada de la carga horaria a 38h, mostrando en pantalla cómo los badges visuales se tornaban rojos y el sistema bloqueaba el botón de guardado. Se restableció la suma exacta a 40.0h y 100.00\%, observando la transición inmediata a color verde.
    \item \textbf{Comprobación de la Compuerta VG-3 y Custodia S3:} Se ingresó un avance del 60\% en la actividad de docencia e intentó enviar a revisión sin evidencias; la compuerta VG-3 bloqueó la operación devolviendo el error HTTP 422. Se adjuntó un archivo PDF de calificaciones de 1.8 MB; el backend calculó su hash SHA-256 y lo custodió en MinIO, permitiendo el envío exitoso tras la adjunción del respaldo.
    \item \textbf{Inspección en Caliente del Bucket MinIO:} Se proyectó la consola de administración de MinIO en el puerto 9001, evidenciando el objeto almacenado con clave UUID y metadatos inmutables.
    \item \textbf{Suscripción del Acta del Sprint 3:} El Docente Evaluador constató el cumplimiento de las Historias de Usuario HU-09 a HU-14, autorizando el inicio de la implementación del Drawer de Observaciones y Firmas Digitales en el Sprint 4.
\end{itemize}

\subsection{Matriz de Criterios y Funcionalidades Aprobadas en el Sprint 3 Review}
A continuación se detalla la matriz que consolida los incrementos aprobados por el comité:"""

# -----------------------------------------------------------------------------
# 3.13 Módulo de Revisión del Comité y Cascada de 3 Firmas Digitales
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[13] = r"""\section{Descripción de actividades}
El flujo colegiado de revisión y legalización formal de los expedientes del SGC demandó la construcción de dos subsistemas interconectados: el panel de revisión granular y la cascada criptográfica de firmas. Las actividades desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño del Drawer React de Observaciones Granulares:} Se implementó un panel lateral deslizante (\textit{Slide-over Drawer}) en la vista del Coordinador de Carrera. Este componente permite emitir observaciones puntuales asociadas a secciones específicas del documento (e.g., "Ajustar justificación de tutorías") o dictaminar observaciones de carácter general.
    \item \textbf{Flujo de Devolución y Resaltado en Ámbar:} Cuando el Coordinador dictamina el estado como "Observado", el expediente se desbloquea para el docente en modo corrección, destacando visualmente en color ámbar las secciones señaladas junto con los comentarios del revisor.
    \item \textbf{Arquitectura de la Cascada Secuencial de 3 Firmas:} Se estructuró la secuencia institucional obligatoria: Firma 1 estampada por el Docente Elaborador (congelando el borrador), Firma 2 estampada por el Coordinador de Carrera (tras constatar cero observaciones abiertas) y Firma 3 estampada por el Subdecano de Facultad (aprobación definitiva y cierre institucional).
    \item \textbf{Regla Estricta de Precedencia Criptográfica:} El backend valida en base de datos la secuencia cronológica inalterable: la Firma 2 no puede ejecutarse si no existe la Firma 1; la Firma 3 no puede registrarse si falta la Firma 2. Si un docente intenta modificar un plan ya firmado, las firmas previas se invalidan automáticamente.
    \item \textbf{Estructura Inmutable del Registro de Firma:} Cada firma genera un registro en \texttt{firmas\_\allowbreak documento} conteniendo el UUID del firmante, su rol institucional, dirección IP, estampa de tiempo UTC y la huella digital criptográfica SHA-256 del contenido documental aprobado.
\end{itemize}

\subsection{Matriz de Estados de Revisión y Secuencia de Firmas Digitales}
A continuación se detalla la matriz técnica de estados y precedencias de firma:"""

# -----------------------------------------------------------------------------
# 3.14 Capa de Asistencia y Corrección Ortográfica Local con LanguageTool
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[14] = r"""\section{Descripción de actividades}
Para asegurar que los planes e informes cumplan con los estándares ortográficos y de redacción exigidos por las auditorías de calidad ISO 9001:2015 del SGC, se desarrolló una arquitectura híbrida de asistencia lingüística. Las actividades ejecutadas comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Aprovisionamiento de LanguageTool en Contenedor Local:} Se configuró el servicio \texttt{sige-languagetool} basado en imagen Java oficial de LanguageTool, desplegado en Docker Compose en el puerto 8010 interno. Esta solución opera localmente sin necesidad de enviar textos confidenciales a servidores externos.
    \item \textbf{Carga del Diccionario Institucional de la UTA:} Se incorporó un archivo de reglas personalizadas (\texttt{es-UTA.xml}) con los acrónimos y términos oficiales de la facultad (FISEI, UTA, SGC, RRA, LOES, CES, TipTap, Docker, JSONB, etc.), evitando falsos positivos durante la corrección técnica.
    \item \textbf{Integración Asíncrona con el Editor TipTap:} En el cliente React se diseñó un servicio que analiza el texto en segundo plano mediante \texttt{POST /v2/check} al puerto 8010, subrayando reactivamente los errores ortográficos (rojo) y gramaticales (azul) con sugerencias de sustitución en tarjetas flotantes.
    \item \textbf{Mecanismo de Fallback Resiliente hacia Gemini API:} Si el contenedor local LanguageTool se encuentra detenido por mantenimiento o sobrecargado, el backend intercepta la contingencia y redirige asíncronamente la petición hacia la API de Google Gemini (vía SDK oficial) para sugerencias de estilo académico.
    \item \textbf{Protección de Datos Personales (LOPDP):} Antes de despachar cualquier payload al servicio secundario de asistencia lingüística, un filtro regex elimina automáticamente nombres propios, correos electrónicos y números de cédula.
\end{itemize}

\subsection{Matriz de Reglas y Categorías de Corrección Ortográfica}
A continuación se especifica la matriz de categorías lingüísticas y diccionarios cargados:"""

# -----------------------------------------------------------------------------
# 3.15 Motor de Exportación Oficial PDF y Validación QR
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[15] = r"""\section{Descripción de actividades}
La emisión de los formatos oficiales impresos y descargables requirió la construcción de un motor de renderizado de alta fidelidad basado en Chromium headless. Las actividades de desarrollo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Integración de Puppeteer en Contenedor Node.js:} Se configuró una instancia optimizada de Chromium sin interfaz gráfica, administrada mediante un pool reutilizable de pestañas para mitigar el consumo de memoria RAM.
    \item \textbf{Plantilla HTML/CSS de Alta Fidelidad SGC:} Se diseñó la estructura de maquetación replicando con precisión milimétrica los formatos institucionales \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T1} y \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T4}: formato A4 estándar con márgenes de 25 mm, encabezado institucional con imagotipo de la UTA, matriz de actividades con reglas CSS estrictas (\texttt{page-break-inside: avoid}) impidiendo cortes huérfanos de filas y recuadros de firmas inferiores.
    \item \textbf{Incrustación de Código QR Vectorial de Validación:} En el pie de página de cada hoja generada se inserta un código QR vectorial. Al ser escaneado con cualquier dispositivo móvil, direcciona al endpoint público de validación institucional (\texttt{/api/v1/validar/:codigo}), certificando la autenticidad del documento sin revelar datos privados.
    \item \textbf{Estampado de Huella Criptográfica SHA-256:} El código hash del expediente completo se imprime de forma textual junto al código QR, garantizando la trazabilidad ante auditorías forenses del SGC.
    \item \textbf{Optimización de Peso y Vectorización de Fuentes:} Se embebieron fuentes TrueType institucionales (Inter), generando archivos PDF vectoriales con texto seleccionable, peso promedio inferior a 650 KB y tiempo de renderizado menor a 1.8 segundos.
\end{itemize}

\subsection{Matriz de Parámetros y Renderizado de Documentos Oficiales en PDF}
A continuación se detalla la matriz técnica de especificación del motor de generación PDF:"""

# -----------------------------------------------------------------------------
# 3.16 Hito 5: Sistema Core Completado y Demostración Integral
# -----------------------------------------------------------------------------
ACTIVITIES_F3_PART2[16] = r"""\section{Descripción de actividades}
La culminación de la Fase 3 de Implementación y Construcción se formalizó mediante la auditoría técnica colegiada del Hito 5 (Sistema Core Completado). Las actividades de cierre ejecutadas por el equipo comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Consolidación de los 16 Entregables Técnicos:} Se constató la ejecución completa de los 16 paquetes de trabajo de la Fase 3 (EDT 3.1 a EDT 3.16), totalizando 400 horas-hombre netas de desarrollo con un índice de desempeño de cronograma $SPI = 1.00$.
    \item \textbf{Demostración End-to-End en Vivo ante el Evaluador:} Se recorrió el ciclo de vida completo del sistema sin interrupciones: inicio de sesión con JWT y RBAC, llenado del plan en el Asistente Wizard, redacción con TipTap y LanguageTool, matriz dinámica validada al 100\% y 40 horas, custodia de evidencias en MinIO S3, superación de las 6 Validation Gates, revisión del coordinador en Drawer, estampado de la cascada de 3 firmas digitales y exportación a PDF vectorial con código QR.
    \item \textbf{Auditoría de Salud de Contenedores Docker:} Se inspeccionó el estado del clúster local en Docker Compose, verificando que los 5 contenedores (\texttt{sige-postgres}, \texttt{sige-backend}, \texttt{sige-frontend}, \texttt{sige-minio} y \texttt{sige-languagetool}) se mantuvieron en estado saludable sin reinicios intempestivos ni fugas de memoria.
    \item \textbf{Decreto Formal de Congelamiento de Código (Code Freeze):} Con la aprobación del Hito 5, la rama principal de código entra en estado inmutable para nuevas funciones, autorizando el inicio inmediato de la Fase 4 de Pruebas Unitarias, Pentesting y Despliegue.
\end{itemize}

\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 3}
A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los 16 entregables que componen la Fase 3 de Construcción:"""

print("fase3_activities_part2.py loaded successfully!")
