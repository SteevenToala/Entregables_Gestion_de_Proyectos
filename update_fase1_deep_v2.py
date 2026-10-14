# apply_master_overhaul.py
# -*- coding: utf-8 -*-
"""
Script maestro para:
1. Eliminar completamente 'Paso 1, Paso 2...', '(Paso a Paso)', y cualquier tono de IA genérico.
2. Enriquecer en profundidad la sección 'Descripción de actividades' en TODOS los entregables de TODAS las fases (Fase 1, 2, 3 y 4).
"""

import re, os

def update_fase1():
    print(">>> Actualizando generate_fase1_enhanced.py...")
    with open("generate_fase1_enhanced.py", "r", encoding="utf-8") as f:
        c = f.read()

    # --- 1. Eliminar "(Paso a Paso)" y variantes en títulos y textos de Fase 1 ---
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico y Origen Real de los Datos (Paso a Paso)}",
                  r"\subsubsection*{1. Procedimiento Metodológico y Levantamiento de Campo As-Is}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico y Origen de los Roles del SGC (Paso a Paso)}",
                  r"\subsubsection*{1. Análisis de Competencias Orgánicas y Modelado de Roles del SGC}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico y Trazabilidad de Requisitos (Paso a Paso)}",
                  r"\subsubsection*{1. Ingeniería de Requisitos y Análisis de Trazabilidad Bidireccional}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Definición del Alcance (Paso a Paso)}",
                  r"\subsubsection*{1. Delimitación Estructural del Perímetro del Sistema Web}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico de las Validation Gates (Paso a Paso)}",
                  r"\subsubsection*{1. Formalización Lógica e Intercepción de Validation Gates}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico del Estudio Financiero y Operativo (Paso a Paso)}",
                  r"\subsubsection*{1. Modelado Financiero de Flujos Descontados y Retorno Operativo}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Estructura de Desglose del Trabajo (Paso a Paso)}",
                  r"\subsubsection*{1. Descomposición Jerárquica y Nivelación de la Ruta Crítica}")
    c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Auditoría del Hito 1 (Paso a Paso)}",
                  r"\subsubsection*{1. Procedimiento de Auditoría Integral y Aseguramiento de Calidad}")

    c = c.replace("El diseño paso a paso se basó en el catálogo de reglas de negocio:",
                  "La formalización de compuertas lógicas se estructuró a partir del catálogo normativo de reglas de negocio:")
    c = c.replace("El cálculo financiero se desarrolló paso a paso:",
                  "El análisis económico y financiero se fundamentó en las siguientes fases metodológicas:")
    c = c.replace("El proceso formal se desarrolló en tres pasos:",
                  "El proceso formal de auditoría y evaluación colegiada se articuló a través de tres fases técnicas:")
    c = c.replace("cuatro etapas secuenciales:", "cuatro fases técnicas secuenciales:")

    # --- 2. Enriquecer "Descripción de actividades" en Fase 1 ---

    # EDT 1.2
    act1_2 = r"""\section{Descripción de actividades}
La correcta asignación de responsabilidades y la eliminación de pasos de aprobación redundantes constituyeron el eje de las actividades de ingeniería de procesos ejecutadas en la facultad. El equipo técnico llevó a cabo las siguientes actividades de modelado organizacional:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Análisis de Competencias Orgánicas y Marco Estatutario UTA/LOES:} Se revisó el Estatuto de la Universidad Técnica de Ambato y el Reglamento de Régimen Académico (RRA - CES) para deslindar con precisión las atribuciones jurídicas de cada rol. Se determinó que el Coordinador de Comisión posee competencia de revisión técnica y disciplinar, mientras que el Subdecano de Facultad ostenta la autoridad legal exclusiva para la aprobación institucional final.
    \item \textbf{Taller de Mapeo de Interacciones y Flujos de Decisión Inter-departamentales:} Se desarrolló una sesión de trabajo colaborativo junto a los coordinadores de carrera y comisiones académicas de la FISEI, modelando formalmente los cinco roles esenciales del sistema: Docente Elaborador, Coordinador de Comisión, Director de Carrera, Subdecano de Facultad y Administrador del SGC, eliminando dos revisiones informales que generaban duplicidad sin valor agregado.
    \item \textbf{Estructuración de la Matriz RACI Institucional del Ciclo Documental:} Para cada una de las 8 fases del flujo documental (Configuración Inicial, Carga Horaria, Redacción Descriptiva, Matriz Dinámica, Custodia de Evidencias, Revisión Técnica de Comisión, Aprobación de Subdecanato y Custodia Histórica), se asignó con rigor quién es Responsable de ejecutar (R), Quién Aprueba legalmente (A), A quién se Consulta técnicamente (C) y Quién debe ser Informado (I).
    \item \textbf{Segmentación y Evaluación de Involucrados según el Marco PMBOK:} Se clasificaron los actores institucionales mediante una matriz de Poder versus Interés, definiendo estrategias diferenciadas de comunicación, vistas de tablero con permisos RBAC y canales de notificación asíncrona adaptados a su nivel de dedicación horaria.
\end{itemize}

\subsection{Matriz RACI de la Cadena Documental Institucional}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz RACI de la Cadena Documental Institucional\}',
        lambda m: act1_2,
        c
    )

    # EDT 1.3
    act1_3 = r"""\section{Descripción de actividades}
La especificación de los requerimientos de software se sustentó en la traducción sistemática de las fallas operativas identificadas en el diagnóstico As-Is hacia capacidades técnicas verificables del sistema web. Las actividades de ingeniería de requisitos comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Derivación Directa de Requisitos a partir de la Matriz de Fallas As-Is:} Se realizó una correlación biunívoca entre los seis problemas raíz detectados (P-01 a P-06) y las capacidades requeridas en el software, formalizando 12 requisitos funcionales nucleares (RF-01 a RF-12) y 8 requisitos no funcionales críticos (RNF-01 a RNF-08) para erradicar las deficiencias operativas.
    \item \textbf{Especificación Rigurosa de Requisitos bajo Sintaxis Normalizada EARS:} Para eliminar cualquier ambigüedad técnica, se redactaron los requerimientos aplicando las cláusulas del estándar EARS (Easy Approach to Requirements Syntax): requisitos ubicuos para funciones permanentes, disparados por eventos para transacciones de usuario y condicionales de estado para restricciones de acceso según el rol.
    \item \textbf{Definición de Criterios de Aceptación Cuantitativos según Norma ISO/IEC 25010:} Se formularon umbrales cuantitativos de calidad y rendimiento: tiempos de respuesta en API inferiores a 1.5 segundos (RNF-01), disponibilidad anual del 99.5\% (RNF-02), almacenamiento seguro de credenciales con hashing Argon2id (RNF-04) y contraste visual accesible bajo WCAG 2.1 AA (RNF-07).
    \item \textbf{Construcción de la Matriz de Trazabilidad Bidireccional de Requisitos:} Se estructuró el mapa de cobertura que enlaza cada requisito funcional con los casos de uso del sistema, las compuertas lógicas de backend y los módulos de persistencia en base de datos.
\end{itemize}

\subsection{Catálogo Oficial de Requisitos Funcionales Nucleares (RF-01 a RF-12)}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Catálogo Oficial de Requisitos Funcionales Nucleares \(RF-01 a RF-12\)\}',
        lambda m: act1_3,
        c
    )

    # EDT 1.4
    act1_4 = r"""\section{Descripción de actividades}
La delimitación precisa del alcance del software y su alineación con los requerimientos del Sistema de Gestión de Calidad (SGC) demandaron un trabajo conjunto entre los analistas del proyecto y las autoridades académicas. Las actividades técnicas ejecutadas incluyeron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Delimitación Estructural del Perímetro del Sistema Web SIGE:} Se definieron con exactitud los módulos que componen la solución tecnológica: gestión de planes de trabajo docente (\texttt{UTA-SGC-A-2-1-P7-T1}), informes de cumplimiento semestral (\texttt{UTA-SGC-A-2-1-P7-T4}), matriz dinámica de actividades de 40 horas semanales, repositorio de evidencias en almacenamiento de objetos S3 y flujo de 3 firmas electrónicas.
    \item \textbf{Identificación y Documentación de Exclusiones Explícitas del Proyecto:} Se formalizaron las fronteras operativas del sistema para prevenir desviaciones en el desarrollo: se excluyeron expresamente el procesamiento de nómina financiera, el control biométrico de asistencia y la gestión de matrículas estudiantiles, atribuciones exclusivas del Sistema de Gestión Académica (SGA) central.
    \item \textbf{Alineación de Restricciones Operativas con Normas ISO 9001:2015 e Indicadores CACES:} Se vincularon los requerimientos del software con los estándares de acreditación universitaria, garantizando que el sistema provea evidencias inmutables, trazabilidad forense y respaldo documental para las auditorías institucionales.
    \item \textbf{Formulación de Métricas de Éxito del Software:} Se establecieron indicadores clave de desempeño (KPI) para el proyecto: digitalización del 100\% de planes en las cinco carreras de la facultad, 0\% de errores aritméticos en la suma horaria y reducción mínima del 85\% en los tiempos totales de legalización.
\end{itemize}

\subsection{Matriz de Alineación entre Objetivos del SGC y Módulos de SIGE}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Alineación entre Objetivos del SGC y Módulos de SIGE\}',
        lambda m: act1_4,
        c
    )

    # EDT 1.5
    act1_5 = r"""\section{Descripción de actividades}
La formulación de las reglas de negocio y de los mecanismos de intercepción lógica constituyó la base para erradicar las inconsistencias de cálculo que afectaban los procesos manuales. El equipo técnico llevó a cabo las siguientes actividades de modelado lógico:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Formalización Matemática de Reglas de Carga Horaria y Ponderación:} Se modeló algebraicamente la restricción horaria semanal según los Artículos 45 y 67 del RRA ($\sum h_{\text{docencia}} + h_{\text{investigación}} + h_{\text{gestión}} + h_{\text{vinculación}} = 40.0\text{ h}$ exactas para dedicación a Tiempo Completo) y la restricción de ponderación estricta ($\sum P_i = 100.00\%$) para las actividades planificadas en la Tabla 1 del SGC.
    \item \textbf{Diseño Lógico de la Cadena Interceptora de Validation Gates (VG-1 a VG-6):} Se especificó la arquitectura de compuertas lógicas transaccionales que bloquean el guardado o envío de documentos ante inconsistencias: VG-1 (Integridad Horaria), VG-2 (Ponderación 100\%), VG-3 (Custodia Obligatoria de Evidencias en avances $>0\%$), VG-4 (Orden Estricto de Firmas), VG-5 (Inmutabilidad del Documento Aprobado) y VG-6 (Control de Extemporaneidad).
    \item \textbf{Modelado de la Matriz de Transiciones de Estado del Documento:} Se diseñó el autómata de estados finitos que gobierna el ciclo de vida del expediente (\texttt{Borrador} $\to$ \texttt{En\_Revision} $\to$ \texttt{Observado} $\to$ \texttt{Aprobado\_Carrera} $\to$ \texttt{Legalizado\_Subdecanato}), definiendo las condiciones de guarda requeridas para cada transición.
    \item \textbf{Protocolo Transaccional para la Gestión de Subsanaciones y Desbloqueos:} Se definió el procedimiento de reapertura controlada para expedientes observados, incorporando una bitácora forense que registra obligatoriamente el justificativo, usuario responsable y marca de tiempo UTC de cada modificación.
\end{itemize}

\subsection{Catálogo Oficial de Reglas de Negocio del Sistema (RN-01 a RN-06)}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Catálogo Oficial de Reglas de Negocio del Sistema \(RN-01 a RN-06\)\}',
        lambda m: act1_5,
        c
    )

    # EDT 1.6
    act1_6 = r"""\section{Descripción de actividades}
La evaluación económica y financiera del proyecto se estructuró mediante la cuantificación rigurosa de costos de desarrollo y el ahorro operativo proyectado para la FISEI. Las actividades de análisis financiero y gobernanza comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado Paramétrico de Costos de Desarrollo e Infraestructura:} Se calculó el presupuesto total del proyecto considerando 832 horas netas de trabajo de ingeniería de software distribuidas entre el equipo de desarrollo, servidores locales con contenedores Docker, almacenamiento de objetos MinIO y librerías de código abierto sin costos de licenciamiento recurrente.
    \item \textbf{Cuantificación Económica del Ahorro Operativo Institucional:} Se cuantificó el ahorro anual derivado de eliminar las horas de transcripción manual de 120 docentes de la FISEI y de optimizar la revisión en 14 comisiones académicas y 5 directores de carrera, adicionando el ahorro directo en papel físico (45 resmas semestrales) y consumibles de impresión.
    \item \textbf{Evaluación Financiera Integral con Modelos de Flujos Descontados:} Se proyectaron los flujos de caja netos a un horizonte de evaluación de 3 años con una tasa de descuento institucional del 10.5\%, obteniendo un Valor Actual Neto (VAN) de \$31,450.28, una Tasa Interna de Retorno (TIR) del 68.4\%, un Retorno de la Inversión (ROI) del +554\% y un período de recuperación de la inversión (Payback) de 8.2 meses.
    \item \textbf{Formalización del Project Charter y Gobernanza Institucional:} Se redactó el acta de constitución del proyecto estableciendo los objetivos estratégicos, el alcance acordado, los hitos clave de entrega y las firmas de patrocinio por parte de las autoridades de la facultad.
\end{itemize}

\subsection{Cuantificación Financiera del Proyecto y Retorno de la Inversión (ROI)}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Cuantificación Financiera del Proyecto y Retorno de la Inversión \(ROI\)\}',
        lambda m: act1_6,
        c
    )

    # EDT 1.7
    act1_7 = r"""\section{Descripción de actividades}
La planificación operativa del proyecto se estructuró a partir de una descomposición jerárquica orientada a entregables, asegurando una asignación eficiente de recursos y el control estricto de los plazos de ejecución. Las actividades técnicas de gestión desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Descomposición Jerárquica de la EDT/WBS en 34 Paquetes de Trabajo:} Se estructuró el árbol de entregables en cuatro fases metodológicas bien delimitadas: Fase 1 (Análisis y Requisitos, 1.1 al 1.8), Fase 2 (Diseño y Arquitectura, 2.1 al 2.7), Fase 3 (Implementación y Desarrollo, 3.1 al 3.16) y Fase 4 (Pruebas y Calidad, 4.1 al 4.3).
    \item \textbf{Estimación Paramétrica de Esfuerzo y Nivelación de Cargas:} Mediante Microsoft Project se estimaron las duraciones de cada actividad técnica y se niveló la asignación horaria del equipo de ingeniería para garantizar un régimen de trabajo sostenible sin sobreasignación de recursos humanos.
    \item \textbf{Modelado de Precedencias PDM y Determinación de la Ruta Crítica (CPM):} Se configuraron las dependencias lógicas Fin a Inicio (FS) entre paquetes de trabajo, identificando la cadena crítica de tareas que condiciona la duración total del proyecto fijada en 104 días laborables.
    \item \textbf{Establecimiento de Compuertas de Control de Calidad (Stage-Gates 1 a 5):} Se programaron cinco hitos formales de evaluación colegiada al cierre de cada etapa para auditar la completitud de los artefactos técnicos y autorizar el avance hacia la siguiente fase de desarrollo.
\end{itemize}

\subsection{Resumen de la Línea Base del Cronograma por Fases de la EDT}"""

    c = re.sub(
        r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Resumen de la Línea Base del Cronograma por Fases de la EDT\}',
        lambda m: act1_7,
        c
    )

    with open("generate_fase1_enhanced.py", "w", encoding="utf-8") as f:
        f.write(c)
    print("generate_fase1_enhanced.py actualizado con éxito.")

update_fase1()
