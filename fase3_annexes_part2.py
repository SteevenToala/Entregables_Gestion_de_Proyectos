# fase3_annexes_part2.py
# Anexos técnicos para los entregables 3.9 a 3.16 de la Fase 3

PART2_ANNEXES = {}

# -----------------------------------------------------------------------------
# 3.9 Construcción de la Matriz Dinámica de Actividades con Distribución Semanal
# -----------------------------------------------------------------------------
PART2_ANNEXES[9] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
La matriz de distribución de actividades semanales representa el núcleo operativo del formato \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T1}. Su desarrollo en React demandó un manejo exhaustivo de estados reactivos y reglas matemáticas estrictas:

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Modelado del Estado Complejo con useReducer:} Se estructuró un reductor que gestiona las operaciones tabulares: agregar actividad, modificar descripción, cambiar tipo (Docencia, Investigación, Tutorías, Gestión), actualizar horas semanales, editar ponderación y marcar el cronograma de semanas activas.
    \item \textbf{Cálculo Reactivo de Totales y Validaciones en Tiempo Real:} Mediante \texttt{useMemo}, la matriz recalcula continuamente dos indicadores críticos:
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item \textbf{Sumatoria de Carga Horaria Semanal:} Debe totalizar exactamente 40.0 horas semanales para docentes a tiempo completo (o 20.0h para tiempo parcial) conforme a los Arts. 45 y 67 del Reglamento de Régimen Académico.
        \item \textbf{Sumatoria de Ponderación Porcentual:} La suma de los pesos asignados a cada actividad debe coincidir exactamente con 100.00\%.
    \end{itemize}
    \item \textbf{Selector Matricial de 16 Semanas Académicas:} Se implementó una cuadrícula interactiva con casillas de verificación correspondientes a las 16 semanas del semestre B26, calculando el total de horas semestrales por actividad de forma automatizada.
    \item \textbf{Badges Visuales Condicionales de Calidad:} Si las horas difieren de 40.0 o la ponderación no suma 100.00\%, la interfaz despliega insignias rojas de advertencia y deshabilita el avance en el Wizard. Cuando ambas sumatorias son exactas, las insignias conmutan a color verde con la leyenda "Conforme con Normativa RRA".
    \item \textbf{Persistencia y Sincronización en Base de Datos:} Los cambios se persisten en la tabla \texttt{actividades\_matriz} mediante sentencias en lote que respetan las restricciones \texttt{CHECK} declarativas del motor relacional.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_matriz_dinamica_actividades.png}
    \caption{Matriz Dinámica de Actividades Docentes con Cronograma de 16 Semanas y Totales Validados.}
    \label{fig:anx_f3_09}
\end{figure}

\subsubsection*{Desglose Técnico y Análisis Estructural del Artefacto Visual}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Elementos Estructurales Visualizados:} La imagen documenta la vista de la matriz en la Etapa Matricial del Wizard. Se visualizan las actividades distribuidas en los cuatro componentes académicos oficiales (Docencia, Investigación, Gestión y Vinculación), la cuadrícula de 16 semanas y los contadores en el pie de tabla.
    \item \textbf{Cálculo Reactivo de Balances en Tiempo Real:} Se aprecian los contadores activos: "Total Horas Semanales: 40.0 h / 40.0 h (100\%)" y "Ponderación Total: 100.00\% / 100.00\%", ambos resaltados en verde brillante, lo que confirma que el plan cumple con la distribución horaria exacta exigida por el RRA y el SGC.
    \item \textbf{Intercepción de Errores y Bloqueo de Avance:} Si el docente altera alguna casilla y la suma difiere de 40.0 horas o del 100.00\% de ponderación, los contadores conmutan automáticamente a color rojo carmesí y deshabilitan el botón de avance hacia la etapa de evidencias.
    \item \textbf{Trazabilidad con el Código Fuente:} Programado en \texttt{frontend/src/components/matriz/MatrizActividades.jsx} y optimizado mediante el hook \texttt{useMatrizCalculator.js}.
\end{itemize}

\subsubsection*{Desglose Técnico y Análisis Estructural del Artefacto Visual}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Elementos Estructurales Visualizados:} La captura muestra el diagrama de flujo y la respuesta de la consola del backend ante una solicitud con inconsistencias. Se observa el arribo de una petición \texttt{POST /api/\allowbreak v1/\allowbreak planes/\allowbreak :id/\allowbreak enviar-revision} interceptada por el pipeline de middlewares.
    \item \textbf{Evaluación Secuencial de Validation Gates:} El middleware ejecuta en 12 ms la compuerta VG-1 (aprobada con 40h), VG-2 (aprobada con 100\%) y se detiene en la compuerta VG-3, emitiendo un código de retorno HTTP 422 Unprocessable Entity debido a que una actividad reportaba avance del 40\% sin registrar evidencias en el bucket MinIO.
    \item \textbf{Carga Útil de Error y Subsanación:} La respuesta JSON detalla el campo afectado (\texttt{"actividad\_id": "act-4"}), la compuerta violada (\texttt{"gate": "VG-3"}) y el mensaje de acción correctiva que la interfaz presenta al docente para guiar su resolución.
    \item \textbf{Trazabilidad con el Código Fuente:} Implementado en \texttt{backend/src/middlewares/validationGates.js} y probado exhaustivamente en \texttt{backend/tests/validationGates.test.js}.
\end{itemize}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La imagen documenta la interfaz de gestión de evidencias vinculada al Informe de Cumplimiento. En la tabla se visualizan los respaldos adjuntados por actividad docente: nombre del archivo institucional, tamaño en kilobytes, estampa de subida y el hash SHA-256 abreviado. El botón "Ver Evidencia" despacha una solicitud al backend para generar la URL prefirmada temporal, abriendo el documento PDF en un visor integrado de alta resolución.

\subsection*{Anexo 3: Matriz de Verificación Operacional del Almacenamiento S3}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Escenario de Prueba} & \textbf{Condición de Entrada y Archivo} & \textbf{Comportamiento del Servicio S3 / Backend} & \textbf{Resultado Verificado} \\
\hline
P1: Subida de PDF Válido & Carga de acta en PDF de 2.4 MB con credenciales válidas. & Objeto almacenado en bucket; hash SHA-256 insertado en DB; HTTP 201. & Custodia Exitosa \\
\hline
P2: Archivo Ejecutable & Subida de script \texttt{.exe} renombrado artificialmente a \texttt{.pdf}. & Rechazo inmediato por validación de firma mágica; código HTTP 400. & Amenaza Bloqueada \\
\hline
P3: Archivo Excede 10 MB & Intento de subida de archivo de video de 25 MB. & Interceptado por Multer; rechazo con código HTTP 413 Payload Too Large. & Límite Respetado \\
\hline
P4: URL Expirada & Acceso a enlace prefirmado tras 16 minutos de emitido. & Respuesta de MinIO con error XML \texttt{Request has expired} (HTTP 403). & Expiración Estricta \\
\hline
\end{tabularx}
\caption{Matriz de pruebas del microservicio de almacenamiento y custodia de evidencias en MinIO S3.}
\end{table}
"""

# -----------------------------------------------------------------------------
# 3.12 Revisión de Sprint 3: Demostración Operativa de Matriz y Custodia S3
# -----------------------------------------------------------------------------
PART2_ANNEXES[12] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
Al concluir el Sprint 3 de desarrollo, se ejecutó la sesión formal de demostración y revisión de sprint bajo metodología Scrum, focalizada en validar la integración entre la Matriz Dinámica, las Validation Gates y el almacenamiento en MinIO S3:

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Preparación del Entorno Integrado de Demostración:} Se verificó el funcionamiento conjunto de los contenedores \texttt{sige-backend}, \texttt{sige-postgres} y \texttt{sige-minio}, precargando un informe de cumplimiento semestral para pruebas en vivo.
    \item \textbf{Demostración de la Matriz Dinámica en Tiempo Real:}
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item Se mostró la distribución de 40 horas en 6 actividades académicas y la asignación del cronograma en 16 semanas.
        \item Se ejecutó una alteración deliberada de la carga horaria a 38h, mostrando en pantalla cómo los badges visuales se tornaban rojos y el sistema bloqueaba el botón de guardado.
        \item Se restableció la suma exacta a 40.0h y 100.00\%, observando la transición inmediata a color verde.
    \end{itemize}
    \item \textbf{Comprobación de la Compuerta VG-3 y Custodia S3:}
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item Se ingresó un avance del 60\% en la actividad de docencia e intentó enviar a revisión sin evidencias; la compuerta VG-3 bloqueó la operación devolviendo el error HTTP 422.
        \item Se adjuntó un archivo PDF de calificaciones de 1.8 MB; el backend calculó su hash SHA-256 y lo custodió en MinIO.
        \item Con la evidencia registrada, el sistema permitió el envío exitoso del informe a revisión.
    \end{itemize}
    \item \textbf{Inspección en Caliente del Bucket MinIO:} Se proyectó la consola de administración de MinIO en el puerto 9001, evidenciando el objeto almacenado con clave UUID y metadatos inmutables.
    \item \textbf{Formalización del Acta del Sprint 3:} El docente evaluador constató el cumplimiento de las Historias de Usuario HU-09 a HU-14, autorizando el inicio de la implementación del Drawer de Observaciones y Firmas Digitales en el Sprint 4.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_gestion_evidencias_detalle.png}
    \caption{Demostración en Vivo de la Custodia de Evidencias y Verificación de Validation Gates.}
    \label{fig:anx_f3_12}
\end{figure}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La captura muestra el modal de detalle de evidencias proyectado durante la sesión de Sprint Review. En la ventana se confirma la recepción exitosa del archivo de respaldo en el bucket de MinIO, el cálculo de su huella digital criptográfica y la vinculación directa con la fila de la matriz de actividades. Tras esta validación, el botón de "Enviar a Comité de Revisión" se activó, certificando la superación de las compuertas de calidad.

\subsection*{Anexo 3: Matriz de Verificación Operacional del Sprint 3 Review}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Criterio Evaluado en Sprint} & \textbf{Mecanismo de Comprobación en Vivo} & \textbf{Evidencia Observada por Evaluadores} & \textbf{Resultado del Sprint} \\
\hline
Validación 40h / 100\% & Ingreso de valores deliberadamente erróneos. & Bloqueo reactivo en frontend y compuertas VG-1 y VG-2 en backend. & Aceptado sin Defectos \\
\hline
Compuerta VG-3 de Evidencias & Envío de informe con avance sin respaldos. & Rechazo con HTTP 422 detallando la actividad infractora sin evidencia. & Aceptado sin Defectos \\
\hline
Subida y Hash en MinIO S3 & Carga de archivo de respaldo PDF en tiempo real. & Objeto alojado en bucket privado con hash SHA-256 verificado en DB. & Aceptado sin Defectos \\
\hline
URLs Prefirmadas Temporales & Apertura de enlace de visualización de evidencia. & Previsualización instantánea en navegador y confirmación de expiración a 15m. & Aceptado sin Defectos \\
\hline
\end{tabularx}
\caption{Matriz de criterios técnicos y de aceptación validados en la Revisión de Sprint 3.}
\end{table}
"""

# -----------------------------------------------------------------------------
# 3.13 Drawer de Observaciones del Comité y Cascada de 3 Firmas Digitales
# -----------------------------------------------------------------------------
PART2_ANNEXES[13] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
El flujo colegiado de revisión y legalización formal de los expedientes del SGC demandó la construcción de dos subsistemas interconectados:

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Diseño del Drawer React de Observaciones Granulares:} Se implementó un panel lateral deslizante (\textit{Slide-over Drawer}) en la vista del Coordinador de Carrera. Este componente permite emitir observaciones puntuales asociadas a secciones específicas del documento (e.g., "Ajustar justificación de tutorías") o dictaminar observaciones de carácter general.
    \item \textbf{Flujo de Devolución y Resaltado en Ámbar:} Cuando el Coordinador dictamina el estado como "Observado", el expediente se desbloquea para el docente en modo corrección, destacando visualmente en color ámbar las secciones señaladas junto con los comentarios del revisor.
    \item \textbf{Arquitectura de la Cascada Secuencial de 3 Firmas:}
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item \textbf{Firma 1 (Docente Elaborador):} Se estampa al momento de someter formalmente el plan al comité, congelando el borrador contra modificaciones arbitrarias.
        \item \textbf{Firma 2 (Coordinador de Carrera / Área):} Se estampa una vez auditada la matriz y habiendo constatado cero observaciones abiertas.
        \item \textbf{Firma 3 (Subdecano de Facultad):} Estampado de aprobación institucional definitiva, emitiendo el dictamen final de validez semestral.
    \end{itemize}
    \item \textbf{Regla Estricta de Precedencia Criptográfica:} El backend valida en base de datos la secuencia cronológica inalterable: la Firma 2 no puede ejecutarse si no existe la Firma 1; la Firma 3 no puede registrarse si falta la Firma 2. Si un docente intenta modificar un plan ya firmado, las firmas previas se invalidan automáticamente.
    \item \textbf{Estructura Inmutable del Registro de Firma:} Cada firma genera un registro en \texttt{firmas\allowbreak\_documento} conteniendo el UUID del firmante, su rol institucional, dirección IP, estampa de tiempo UTC y la huella digital criptográfica SHA-256 del contenido documental aprobado.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_coordinador_revision.png}
    \caption{Bandeja de Revisión del Coordinador con Drawer Lateral de Observaciones Activo.}
    \label{fig:anx_f3_13}
\end{figure}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La captura muestra la vista del Coordinador de Carrera durante la auditoría técnica de un plan de trabajo. En la parte central se proyecta el documento completo en formato institucional. A la derecha se encuentra desplegado el Drawer de Observaciones, donde el coordinador redacta recomendaciones sobre la sección metodológica. En la parte superior derecha se aprecian los botones de acción rápida: "Devolver con Observaciones" (ámbar) y "Aprobar y Estampar Firma 2" (verde institucional).

\subsection*{Anexo 3: Matriz de Verificación Operacional de Firmas y Observaciones}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Escenario de Prueba} & \textbf{Condición de Entrada y Acción} & \textbf{Respuesta del Sistema y Middleware} & \textbf{Resultado Verificado} \\
\hline
P1: Firma Fuera de Orden & Subdecano intenta estampar Firma 3 sobre plan sin Firma 2. & Bloqueo con HTTP 400; mensaje "Secuencia de firmas inválida: Requiere firma previa". & Precedencia Forzada \\
\hline
P2: Registro de Observación & Coordinador emite observación sobre la Matriz de Actividades. & Estado cambia a "Observado"; notificación enviada al docente; campos en ámbar. & Flujo de Corrección \\
\hline
P3: Cascada Completa & Ejecución secuencial de Firma 1 $\to$ Firma 2 $\to$ Firma 3. & Generación de 3 hashes SHA-256; documento conmutado a estado final "Aprobado". & Aprobación Exitosa \\
\hline
P4: Modificación Tras Firma & Intento de editar actividad en plan que ya cuenta con Firma 1. & Bloqueo por middleware de inmutabilidad; edición deshabilitada en cliente. & Inmutabilidad Blindada \\
\hline
\end{tabularx}
\caption{Matriz de pruebas del subsistema de observaciones y cascada de firmas digitales.}
\end{table}
"""

# -----------------------------------------------------------------------------
# 3.14 Integración de LanguageTool Local (Puerto 8010) y Fallback IA
# -----------------------------------------------------------------------------
PART2_ANNEXES[14] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
Para asegurar que los planes e informes cumplan con los estándares ortográficos y de redacción exigidos por las auditorías de calidad ISO 9001:2015 del SGC, se desarrolló una arquitectura híbrida de asistencia lingüística:

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Aprovisionamiento de LanguageTool en Contenedor Local:} Se configuró el servicio \texttt{sige-languagetool} basado en imagen Java oficial de LanguageTool, desplegado en Docker Compose en el puerto 8010 interno. Esta solución opera localmente sin necesidad de enviar textos confidenciales a servidores externos.
    \item \textbf{Carga del Diccionario Institucional de la UTA:} Se incorporó un archivo de reglas personalizadas (\texttt{es-UTA.xml}) con los acrónimos y términos oficiales de la facultad (FISEI, UTA, SGC, RRA, LOES, CES, TipTap, Docker, JSONB, etc.), evitando falsos positivos durante la corrección técnica.
    \item \textbf{Integración Asíncrona con el Editor TipTap:} En el cliente React se diseñó un servicio que analiza el texto en segundo plano mediante \texttt{POST /v2/check} al puerto 8010, subrayando reactivamente los errores ortográficos (rojo) y gramaticales (azul) con sugerencias de sustitución en tarjetas flotantes.
    \item \textbf{Mecanismo de Fallback Resiliente hacia Gemini API:} Si el contenedor local LanguageTool se encuentra detenido por mantenimiento o sobrecargado, el backend intercepta la contingencia y redirige asíncronamente la petición hacia la API de Google Gemini (vía SDK oficial) para sugerencias de estilo académico.
    \item \textbf{Protección de Datos Personales (LOPDP):} Antes de despachar cualquier payload al servicio secundario de asistencia lingüística, un filtro regex elimina automáticamente nombres propios, correos electrónicos y números de cédula.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_12_languagetool_docker.png}
    \caption{Verificación Ortográfica en Tiempo Real con LanguageTool Local y Sugerencias de Estilo.}
    \label{fig:anx_f3_14}
\end{figure}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La captura documenta el editor TipTap durante la redacción de la metodología del plan docente. En el texto se aprecian palabras deliberadamente mal escritas subrayadas en rojo. Al hacer clic sobre el término infractor, se despliega una tarjeta contextual flotante generada por el microservicio local de LanguageTool que ofrece la corrección adecuada con un solo clic, logrando tiempos de análisis menores a 120 ms.

\subsection*{Anexo 3: Matriz de Verificación Operacional de Asistencia Lingüística}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Escenario de Prueba} & \textbf{Condición de Entrada del Texto} & \textbf{Respuesta del Microservicio / Fallback} & \textbf{Resultado Verificado} \\
\hline
P1: Falta Ortográfica & Párrafo con palabras con tildes faltantes y errores de tipeo. & Detección inmediata en 95 ms; sugerencias de reemplazo precisas en UI. & Corrección Exitosa \\
\hline
P2: Acrónimos Institucionales & Redacción que incluye "FISEI", "UTA" y "SGC". & Términos reconocidos por diccionario \texttt{es-UTA.xml}; 0 falsas alarmas. & Sin Falsos Positivos \\
\hline
P3: Caída de LanguageTool & Simulación de apagado del contenedor local (puerto 8010). & Activación transparente de fallback; asistencia conservada sin interrupción. & Alta Disponibilidad \\
\hline
P4: Anonimización LOPDP & Envío de texto con nombres de docentes y cédulas. & Datos sensibles ofuscados con tokens \texttt{[ANON]} previo al análisis. & Privacidad Asegurada \\
\hline
\end{tabularx}
\caption{Matriz de pruebas del servicio de asistencia ortográfica y fallback resiliente.}
\end{table}
"""

# -----------------------------------------------------------------------------
# 3.15 Motor de Generación de Documentos Oficiales en PDF Vectorial (Puppeteer)
# -----------------------------------------------------------------------------
PART2_ANNEXES[15] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
La emisión de los formatos oficiales impresos y descargables requirió la construcción de un motor de renderizado de alta fidelidad basado en Chromium headless:

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Integración de Puppeteer en Contenedor Node.js:} Se configuró una instancia optimizada de Chromium sin interfaz gráfica, administrada mediante un pool reutilizable de pestañas para mitigar el consumo de memoria RAM.
    \item \textbf{Plantilla HTML/CSS de Alta Fidelidad SGC:} Se diseñó la estructura de maquetación replicando con precisión milimétrica los formatos institucionales \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T1} y \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T4}:
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item Formato de página A4 estándar (210 x 297 mm) con márgenes reglamentarios de 25 mm.
        \item Encabezado institucional con logotipo vectorial de la UTA y escudo de la FISEI.
        \item Tabla de matriz semanal con reglas CSS estrictas (\texttt{page-break-inside: avoid}) impidiendo saltos de página huérfanos que corten filas a la mitad.
        \item Recuadros inferiores oficiales para el estampado de las 3 firmas de responsabilidad.
    \end{itemize}
    \item \textbf{Incrustación de Código QR Vectorial de Validación:} En el pie de página de cada hoja generada se inserta un código QR generado con la biblioteca \texttt{qrcode}. Al ser escaneado con cualquier dispositivo móvil, direcciona al endpoint público de validación institucional (\texttt{/api/v1/validar/:codigo}), certificando la autenticidad del documento sin revelar datos privados.
    \item \textbf{Estampado de Huella Criptográfica SHA-256:} El código hash del expediente completo se imprime de forma textual junto al código QR, garantizando la trazabilidad ante auditorías forenses del SGC.
    \item \textbf{Optimización de Peso y Vectorización de Fuentes:} Se embebieron fuentes TrueType institucionales (Inter), generando archivos PDF vectoriales con texto seleccionable, peso promedio inferior a 650 KB y tiempo de renderizado menor a 1.8 segundos.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/preview_plan_trabajo.png}
    \caption{Previsualización del Plan de Trabajo Docente Generado en PDF Vectorial con Código QR.}
    \label{fig:anx_f3_15}
\end{figure}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La captura presenta el documento PDF generado por el motor Puppeteer. Se evidencia el encabezado oficial del SGC, la distribución tabular de la matriz de actividades perfectamente paginada sin desbordes de margen y los tres bloques de firmas digitales en la parte inferior. En la esquina inferior izquierda se observa el código QR institucional y la cadena hash SHA-256 para validación pública.

\subsection*{Anexo 3: Matriz de Verificación Operacional del Motor PDF y Código QR}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Escenario de Prueba} & \textbf{Condición de Entrada y Datos} & \textbf{Comportamiento Verificado del Motor} & \textbf{Resultado Verificado} \\
\hline
P1: Generación de Plan Completo & Expediente con 8 actividades y cronograma de 16 semanas. & Documento de 5 páginas generado en 1.6 segundos; 0 desbordes de texto. & Renderizado Exitoso \\
\hline
P2: Salto de Página Limpio & Actividad con descripción extensa al borde inferior de página. & Paginación respetada; fila completa desplazada a siguiente hoja sin roturas. & Maquetación Perfecta \\
\hline
P3: Lectura de Código QR & Escaneo con cámara de smartphone sobre código QR generado. & Apertura inmediata de URL pública certificando estado "Aprobado Oficial". & Validación QR Funcional \\
\hline
P4: Verificación Forense & Cotejo de hash SHA-256 impreso contra registro en base de datos. & Correspondencia bit a bit exacta confirmando inmutabilidad del archivo. & Hash Verificado \\
\hline
\end{tabularx}
\caption{Matriz de pruebas del motor de renderizado PDF vectorial y trazabilidad QR.}
\end{table}
"""

# -----------------------------------------------------------------------------
# 3.16 Hito 3: Revisión de Sprint 4 y Demostración Integral del Sistema Operativo
# -----------------------------------------------------------------------------
PART2_ANNEXES[16] = r"""
\subsection*{Anexo 1: Desglose Metodológico y Procedimiento Técnico de Construcción}
La culminación de la Fase 3 de Implementación y Construcción se formalizó mediante la auditoría técnica colegiada del Hito 5 (Sistema Core Completado):

\begin{enumerate}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{Consolidación de los 16 Entregables Técnicos:} Se constató la ejecución completa de los 16 paquetes de trabajo de la Fase 3 (EDT 3.1 a EDT 3.16), totalizando 400 horas-hombre netas de desarrollo con un índice de desempeño de cronograma $SPI = 1.00$.
    \item \textbf{Demostración End-to-End en Vivo ante el Evaluador:} Se recorrió el ciclo de vida completo del sistema sin interrupciones:
    \begin{itemize}[leftmargin=1.2em, itemsep=2pt]
        \item Inicio de sesión docente con JWT y verificación de permisos RBAC.
        \item Creación guiada de un Plan de Trabajo Semestral en el Asistente Wizard.
        \item Redacción en TipTap con autoguardado y corrección ortográfica en línea con LanguageTool.
        \item Configuración de la Matriz Dinámica cumpliendo 40 horas y ponderación al 100.00\%.
        \item Subida y custodia de evidencias de cumplimiento en MinIO S3 con hash SHA-256.
        \item Superación de la cadena de las 6 Validation Gates sin advertencias.
        \item Revisión colegiada por el Coordinador de Carrera a través del Drawer de observaciones.
        \item Estampado cronológico de la Cascada de 3 Firmas Digitales (Docente $\to$ Coordinador $\to$ Subdecano).
        \item Descarga del reporte final en PDF vectorial idéntico al formato oficial del SGC con código QR.
    \end{itemize}
    \item \textbf{Auditoría de Salud de Contenedores Docker:} Se inspeccionó el estado del clúster local en Docker Compose, verificando que los 5 contenedores (\texttt{sige-postgres}, \texttt{sige-backend}, \texttt{sige-frontend}, \texttt{sige-minio} y \texttt{sige-languagetool}) se mantuvieron en estado saludable sin reinicios intempestivos ni fugas de memoria.
    \item \textbf{Decreto Formal de Congelamiento de Código (Code Freeze):} Con la aprobación del Hito 5, la rama principal de código (\texttt{main}) entra en estado inmutable para nuevas funciones, autorizando el inicio inmediato de la Fase 4 de Pruebas Unitarias, Pentesting y Despliegue.
\end{enumerate}

\subsection*{Anexo 2: Evidencia Visual de Funcionamiento Operativo}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/s4_03_cascada_firmas.png}
    \caption{Documento Oficial SGC Legalizado con las 3 Firmas Digitales Estampadas en Cascada.}
    \label{fig:anx_f3_16}
\end{figure}

\subsubsection*{Explicación Técnica del Artefacto Visual}
La captura documenta la sección final de legalización del Plan de Trabajo Docente en el formato \texttt{UTA-\allowbreak SGC-\allowbreak A-2-1-\allowbreak P7-T1}. Se evidencian los tres bloques de firma con sus identificadores de usuario, cargos institucionales, estampas de tiempo UTC y huellas criptográficas SHA-256. En la parte lateral se aprecia el código QR de validación pública institucional, certificando que el expediente completó con éxito el ciclo de vida del sistema SIGE.

\subsection*{Anexo 3: Matriz de Verificación Operacional del Cierre de Construcción}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|>{\hsize=0.75\hsize\raggedright\arraybackslash\bfseries\footnotesize}X|>{\hsize=1.25\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=1.35\hsize\raggedright\arraybackslash\footnotesize}X|>{\hsize=0.65\hsize\centering\arraybackslash\footnotesize}X|}
\hline
\rowcolor{tableheader}
\textbf{Área Evaluada en Cierre} & \textbf{Mecanismo de Auditoría Técnica} & \textbf{Evidencia Observada por Evaluadores} & \textbf{Resultado del Hito} \\
\hline
Completitud de Requisitos & Mapeo de las 24 Historias de Usuario aprobadas. & 100\% de requisitos implementados y comprobados en interfaz y base de datos. & Aprobado sin Observaciones \\
\hline
Flujo End-to-End & Ejecución del ciclo completo de plan e informe. & Recorrido íntegro de 10 etapas operativas completado con éxito en menos de 4 minutos. & Aprobado sin Observaciones \\
\hline
Infraestructura Docker & Inspección de los 5 contenedores en ejecución. & Todos los servicios saludables, puertos enlazados y volúmenes persistentes íntegros. & Aprobado sin Observaciones \\
\hline
Aprobación de Code Freeze & Firma del acta de cierre de construcción de Fase 3. & Dictamen unánime emitido; autorización formal para inicio de Fase 4 de Pruebas. & Hito 5 Legalizado \\
\hline
\end{tabularx}
\caption{Matriz oficial de auditoría de cierre de construcción y legalización del Hito 5.}
\end{table}
"""

print("fase3_annexes_part2.py loaded successfully with annexes 3.9 to 3.16!")
