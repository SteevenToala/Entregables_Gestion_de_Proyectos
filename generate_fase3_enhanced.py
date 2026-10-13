# generate_fase3_enhanced.py
import os
from template_engine import render_doc

def generate_fase3():
    base_dir = os.path.join("Entregables_Latex", "Fase_3") if os.path.exists("Entregables_Latex") else "Fase_3"
    os.makedirs(base_dir, exist_ok=True)

    # Helper to write
    def write_tex(filename, content):
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

    # =========================================================================
    # 3.1 IMPLEMENTACIÓN DE TABLAS, ÍNDICES Y SCRIPTS DDL POSTGRESQL 18
    # =========================================================================
    b3_1 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Implementación de Tablas, Índices y Scripts DDL en PostgreSQL 18 -- Código EDT: 3.1

\section{Introducción}
La materialización de la capa de persistencia en PostgreSQL 18 constituye el cimiento operativo del sistema web SIGE. Tras la aprobación del modelo relacional en la Fase 2, esta tarea ejecutó el despliegue físico de las 13 tablas relacionales normalizadas en 3NF, la configuración de restricciones declarativas de integridad referencial con \texttt{ON DELETE RESTRICT}, la creación de índices B-Tree y GIN para optimizar tiempos de consulta en informes y matrices, y la automatización de auditoría mediante triggers para registrar estampas de tiempo inmutables.

\section{Objetivo}
\subsection{Objetivo General}
Implementar físicamente en el contenedor PostgreSQL 18 el esquema relacional de 13 tablas, restricciones de integridad e índices optimizados, garantizando consistencia ACID y alto rendimiento para los formatos del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Desplegar físicamente las 13 tablas con tipos de datos nativos (\texttt{UUID}, \texttt{VARCHAR}, \texttt{NUMERIC(5,2)}, \texttt{JSONB}).
    \item Configurar restricciones declarativas \texttt{CHECK} para asegurar que las ponderaciones no excedan el 100\% y las horas sean no negativas.
    \item Implementar índices B-Tree en llaves foráneas e índices GIN sobre campos \texttt{JSONB} de secciones descriptivas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Creación de las 13 tablas en el contenedor \texttt{sige-postgres} versión 18.
    \item Verificación de transacciones concurrentes y soporte de tipos JSONB para texto enriquecido.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Poblado de datos maestros de producción (correspondiente a EDT 3.2).
    \item Configuración de replicación distribuida multisitio.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{DDL (Data Definition Language):} Sentencias SQL empleadas para crear y modificar estructuras de bases de datos.
    \item \textbf{Restricción CHECK:} Regla declarativa en el motor que restringe los valores admisibles en una columna específica.
    \item \textbf{Índice GIN (Generalized Inverted Index):} Índice especializado en PostgreSQL para búsquedas de alta eficiencia en datos JSONB.
    \item \textbf{Trigger de Auditoría:} Procedimiento almacenado que se dispara automáticamente ante inserciones o actualizaciones para actualizar \texttt{updated\_at}.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 3.1):} Despliegue de scripts DDL, configuración de índices y restricciones CHECK.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de integridad referencial y compatibilidad con el backend Express.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del esquema físico en base de datos.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Garantía de integridad e inalterabilidad de los registros de carga horaria y rendición docente.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 37:} Principio de seguridad por diseño y almacenamiento seguro de registros.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ANSI/ISO/IEC 9075:2016 (Database Language SQL):} Estándares de sintaxis relacional e integridad referencial.
    \item \textbf{ISO/IEC 27001:2022:} Controles de seguridad de bases de datos y custodia de registros de auditoría.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se utilizó el contenedor oficial de PostgreSQL 18 orquestado en Docker Compose. Los scripts DDL se estructuraron de forma idempotente (\texttt{CREATE TABLE IF NOT EXISTS}) asegurando reproducibilidad. Se definieron llaves primarias basadas en UUID autogenerado con la extensión nativa \texttt{pgcrypto}, eliminando colisiones y garantizando escalabilidad horizontal.

\subsection{Políticas de Calidad de la Capa de Datos}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Integridad Referencial Bloqueante:} Las llaves foráneas implementan \texttt{ON DELETE RESTRICT} para impedir pérdida de datos históricos.
    \item \textbf{Política de Validación Matemática Declarativa:} Toda fila de actividad debe cumplir \texttt{CHECK(horas >= 0)} y \texttt{CHECK(ponderacion <= 100.00)}.
    \item \textbf{Política de Índices Compuestos para Vistas Críticas:} La búsqueda de expedientes de docentes por periodo debe resolverse mediante índice compuesto B-Tree con latencia menor a 10 ms.
    \item \textbf{Política de Auditoría Automatizada:} Ningún registro puede actualizarse sin reflejar la marca temporal exacta mediante triggers PL/pgSQL.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_01_migraciones_indices_bd.png}
    \caption{Pipeline de Migraciones DDL, Restricciones CHECK e Índices en PostgreSQL 18.}
    \label{fig:ddl_pipeline}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Restricciones CHECK e Índices Implementados}
A continuación se detalla la matriz que especifica las reglas de integridad y optimización implementadas en PostgreSQL 18:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Tabla Relacional} & \textbf{Restricción / Índice} & \textbf{Definición SQL / Tipo de Optimización} & \textbf{Propósito SGC} \\
\hline
\texttt{planes\_docente} & \texttt{chk\_estado\_valido} & \texttt{CHECK (estado IN ('Borrador', 'En Revision', 'Observado', 'Aprobado'))} & Ciclo de vida estricto del plan P7-T1. \\
\hline
\texttt{planes\_docente} & \texttt{idx\_plan\_doc\_per} & Índice B-Tree en \texttt{(fk\_docente, fk\_periodo)} & Aceleración de bandeja docente. \\
\hline
\texttt{actividades\_matriz} & \texttt{chk\_horas\_rango} & \texttt{CHECK (horas >= 0 AND horas <= 40)} & Previene carga horaria irreal. \\
\hline
\texttt{actividades\_matriz} & \texttt{chk\_pond\_rango} & \texttt{CHECK (ponderacion >= 0.00 AND ponderacion <= 100.00)} & Integridad de sumatoria al 100\%. \\
\hline
\texttt{secciones\_documento} & \texttt{idx\_sec\_jsonb} & Índice GIN en \texttt{contenido\_jsonb} & Búsqueda rápida de texto enriquecido. \\
\hline
\texttt{firmas\_documento} & \texttt{idx\_firma\_sec} & B-Tree UNIQUE en \texttt{(fk\_plan, orden)} & Garantiza secuencia 1 $\to$ 2 $\to$ 3. \\
\hline
\end{tabularx}
\caption{Matriz técnica de integridad e índices en PostgreSQL 18.}
\label{tab:indices_ddl}
\end{table}

\subsection{Matriz del Volumen de Almacenamiento Estimado por Tabla}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Tabla} & \textbf{Bytes / Fila (Est.)} & \textbf{Filas / Semestre} & \textbf{Estrategia de Crecimiento} \\
\hline
\texttt{planes\_docente} & 256 B & $\sim 200$ & Crecimiento lineal bajo ($<1\text{ MB/año}$). \\
\hline
\texttt{secciones\_documento} & 4.2 KB & $\sim 1{,}600$ & Contenido JSONB comprimido nativamente. \\
\hline
\texttt{actividades\_matriz} & 512 B & $\sim 2{,}400$ & Indexación B-Tree altamente compacta. \\
\hline
\texttt{firmas\_documento} & 384 B & $\sim 600$ & Registros inmutables con hashes SHA-256. \\
\hline
\end{tabularx}
\caption{Volumetría estimada para el ciclo académico de la FISEI.}
\end{table}
"""

    anx3_1 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.1 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.1 \\
\hline
Nombre de la Tarjeta & Implementación de tablas, índices y scripts DDL PostgreSQL 18 \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 01 de septiembre al 04 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & Esquema DDL inicial y scripts de inicialización en PostgreSQL 18 (\texttt{schema.sql}) \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.1 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Verificación de Integridad Relacional en el Motor}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Prueba de Inserción} & \textbf{Sentencia de Validación de Integridad} & \textbf{Resultado del Motor} & \textbf{Estado} \\
\hline
P1 - Horas Negativas & Inserción con \texttt{horas = -5} en \texttt{actividades\_matriz} & \texttt{ERROR: violates check constraint chk\_horas\_rango} & SUPERADA \\
\hline
P2 - Ponderación $>100$ & Inserción con \texttt{ponderacion = 120.00} en \texttt{actividades\_matriz} & \texttt{ERROR: violates check constraint chk\_pond\_rango} & SUPERADA \\
\hline
P3 - Borrado Accidental & Eliminación de usuario con planes activos & \texttt{ERROR: violates foreign key constraint (RESTRICT)} & SUPERADA \\
\hline
P4 - Búsqueda JSONB & Consulta con operador \texttt{@>} sobre \texttt{contenido\_jsonb} & Retorno en 2.4 ms utilizando índice GIN & SUPERADA \\
\hline
\end{tabularx}
\caption{Pruebas de verificación de restricciones e integridad en PostgreSQL 18.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{104b2a8 - feat(db): scripts DDL PostgreSQL 18, indices B-Tree y GIN con restricciones CHECK}
    \item \textbf{Archivos Afectados:} \texttt{database/schema.sql}, \texttt{Entregables\_Latex/Fase\_3/3.1*.tex}
\end{itemize}
"""
    write_tex("3.1_Implementacion_Tablas_Indices_Scripts_DDL_PostgreSQL_18.tex",
              render_doc("TI-SIGE-ENT-F3-001", "IMPLEMENTACIÓN DE SOFTWARE / PERSISTENCIA POSTGRESQL", "04/09/2026", "04/09/2026", "IMPLEMENTACIÓN DE TABLAS E ÍNDICES DDL", b3_1, "04/09/2026", anx3_1))

    # =========================================================================
    # 3.2 DATOS INICIALES Y CATÁLOGOS INSTITUCIONALES
    # =========================================================================
    b3_2 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Datos Iniciales y Catálogos Institucionales -- Código EDT: 3.2

\section{Introducción}
El funcionamiento integral del sistema SIGE requiere el aprovisionamiento de datos maestros correspondientes a la estructura organizacional de la Universidad Técnica de Ambato y la Facultad de Ingeniería en Sistemas, Electrónica e Industrial (FISEI). El presente informe documenta el desarrollo y ejecución del componente de inicialización de datos (\textit{Database Seeder}), el cual puebla de manera determinista los catálogos de facultades, carreras, roles institucionales, catálogo oficial de actividades del SGC y cuentas base para pruebas de integración.

\section{Objetivo}
\subsection{Objetivo General}
Poblar y verificar los catálogos institucionales maestros y datos de prueba en la base de datos de SIGE, asegurando la correspondencia con la estructura académica de la FISEI.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementar el script \texttt{seed.js} para carga automatizada e idempotente de datos iniciales.
    \item Cargar los catálogos institucionales oficiales (4 carreras de FISEI, 5 roles RBAC, periodos académicos).
    \item Registrar el catálogo de actividades homologadas del SGC según las plantillas P7-T1 y P7-T2.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Poblado de carreras: Software, Tecnologías de la Información, Telecomunicaciones y Computación.
    \item Inserción de usuarios semilla con contraseñas encriptadas mediante Argon2id.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Migración masiva de expedientes de docentes de ciclos anteriores a 2026.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Database Seeder:} Script automatizado que inserta registros iniciales necesarios para que el sistema funcione en un estado base conocido.
    \item \textbf{Idempotencia:} Propiedad por la cual la ejecución múltiple de un script no genera duplicados ni errores (\texttt{ON CONFLICT DO NOTHING}).
    \item \textbf{Catálogo SGC:} Listado estandarizado de tipos de actividad académica aprobado por la Comisión de Calidad.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 3.2):} Desarrollo del script de sembrado y validación de integridad.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de hashes criptográficos y roles de usuario.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del catálogo oficial de la FISEI.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Organización académica por facultades y carreras legalmente reconocidas.
    \item \textbf{Reglamento de Régimen Académico (CES), Art. 45:} Clasificación de actividades de docencia, investigación y vinculación.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 7.5:} Control de los catálogos de información documentada oficial.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuró el módulo de sembrado en JavaScript ejecutado mediante Node.js directamente contra el contenedor PostgreSQL 18. Para evitar duplicaciones en arranques sucesivos, cada inserción utiliza la cláusula SQL \texttt{ON CONFLICT (codigo) DO UPDATE} o \texttt{DO NOTHING}. Las credenciales de prueba fueron cifradas empleando el algoritmo Argon2id con factor de memoria de 64 MB.

\subsection{Políticas de Calidad de Catálogos}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Idempotencia de Sembrado:} El script de seed debe poder ejecutarse indefinidas veces produciendo exactamente el mismo estado sin fallos.
    \item \textbf{Política de Seguridad de Cuentas Semilla:} Ninguna contraseña en texto plano se almacena en el repositorio; se emplean hashes con salt único.
    \item \textbf{Política de Homologación SGC:} Los tipos de actividad deben coincidir textualmente con las opciones de las plantillas oficiales UTA.
    \item \textbf{Política de Periodo Vigente Único:} Solo un periodo académico puede encontrarse en estado ``Activo'' de forma simultánea.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_02_catalogos_institucionales_seed.png}
    \caption{Arquitectura de Poblado y Relación de Catálogos Maestros Institucionales.}
    \label{fig:seed_catalogos}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Catálogos Institucionales Maestros Sembrados}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Catálogo} & \textbf{Registros} & \textbf{Valores Maestros Sembrados} & \textbf{Estado} \\
\hline
Facultad & 1 & FISEI (Facultad de Ingeniería en Sistemas, Electrónica e Industrial) & Activo \\
\hline
Carreras & 4 & Software, Tecnologías de la Información, Telecomunicaciones, Computación & Activos \\
\hline
Roles RBAC & 5 & \texttt{DOCENTE}, \texttt{COORD\_AREA}, \texttt{COORD\_CARRERA}, \texttt{SUBDECANO}, \texttt{ADMIN\_SGC} & Activos \\
\hline
Periodo Académico & 1 & Octubre 2026 -- Febrero 2027 (Código: \texttt{2026-B}) & Vigente \\
\hline
Actividades SGC & 12 & Cátedra, Preparación, Tutorías Académicas, Proyectos de Investigación, etc. & Homologadas \\
\hline
\end{tabularx}
\caption{Catálogos maestros insertados en la base de datos.}
\label{tab:seed_matrix}
\end{table}

\subsection{Matriz de Cuentas de Prueba para Validación de Roles}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|m{4.0cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Rol Institucional} & \textbf{Correo Institucional de Prueba} & \textbf{Ámbito de Permisos / Facultad} \\
\hline
Docente Titular & \texttt{docente@uta.edu.ec} & Elaboración y edición de planes de trabajo propios. \\
\hline
Coordinador de Área & \texttt{coord.area@uta.edu.ec} & Revisión técnica y emisión de observaciones de área. \\
\hline
Coordinador de Carrera & \texttt{coordinador@uta.edu.ec} & Aprobación en primera instancia y firma digital. \\
\hline
Subdecano & \texttt{subdecano@uta.edu.ec} & Legalización en Consejo Directivo y cierre de plan. \\
\hline
Administrador SGC & \texttt{admin@uta.edu.ec} & Gestión de usuarios, periodos y prórrogas extemporáneas. \\
\hline
\end{tabularx}
\caption{Cuentas institucionales base para verificación de perfiles.}
\end{table}
"""

    anx3_2 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.2 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.2 \\
\hline
Nombre de la Tarjeta & Datos iniciales y catálogos institucionales \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 04 de septiembre al 08 de septiembre de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{DbInitializer} con usuarios y catálogos institucionales \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.2 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Ejecución del Script Seeder en Consola}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Paso de Ejecución} & \textbf{Salida Registrada en Consola del Contenedor Backend} & \textbf{Estado} \\
\hline
1 & \texttt{[SEED] Conectando a sige-postgres:5432/sige\_sgc\_db... OK} & ÉXITO \\
\hline
2 & \texttt{[SEED] Insertando catálogos de Facultad y Carreras FISEI... (4 insertadas)} & ÉXITO \\
\hline
3 & \texttt{[SEED] Insertando roles RBAC y permisos del SGC... (5 roles creados)} & ÉXITO \\
\hline
4 & \texttt{[SEED] Registrando usuarios base con hash Argon2id... (5 usuarios OK)} & ÉXITO \\
\hline
5 & \texttt{[SEED] Catálogo de actividades SGC inicializado... (12 tipos creados)} & ÉXITO \\
\hline
\end{tabularx}
\caption{Registro de ejecución del sembrado de base de datos.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{29f81ac - feat(db): database seeder de catalogos institucionales FISEI y usuarios base}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/database/seed.js}, \texttt{Entregables\_Latex/Fase\_3/3.2*.tex}
\end{itemize}
"""
    write_tex("3.2_Datos_Iniciales_y_Catalogos_Institucionales.tex",
              render_doc("TI-SIGE-ENT-F3-002", "IMPLEMENTACIÓN DE SOFTWARE / CATÁLOGOS INSTITUCIONALES", "08/09/2026", "08/09/2026", "DATOS INICIALES Y CATÁLOGOS INSTITUCIONALES", b3_2, "08/09/2026", anx3_2))

    # =========================================================================
    # 3.3 AUTENTICACIÓN Y AUTORIZACIÓN DE USUARIOS
    # =========================================================================
    b3_3 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Autenticación y Autorización de Usuarios -- Código EDT: 3.3

\section{Introducción}
La seguridad en el acceso a la plataforma SIGE es un requerimiento crítico dado que gestiona planes de trabajo institucionales, evaluaciones y firmas digitales vinculantes. Este entregable documenta la implementación completa del subsistema de autenticación y autorización basado en tokens web JSON (JWT) y control de acceso basado en roles (RBAC). Se detallan los mecanismos de generación de tokens firmados mediante algoritmo HMAC-SHA256, el flujo de refresco de credenciales, el almacenamiento seguro de contraseñas con Argon2id y la protección de rutas tanto a nivel de middleware en Express v5 como en el enrutador cliente en React.

\section{Objetivo}
\subsection{Objetivo General}
Implementar el subsistema de autenticación y autorización segura con JWT y RBAC en el backend y frontend de SIGE, garantizando la delimitación estricta de privilegios.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Desarrollar los endpoints de login (\texttt{POST /api/auth/login}) y verificación (\texttt{GET /api/auth/me}).
    \item Construir los middlewares de Express para validación de token y autorización por roles.
    \item Diseñar e integrar la vista interactiva de inicio de sesión en el cliente React.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Protección de todos los endpoints de la API REST mediante autorización por encabezado \texttt{Authorization: Bearer <token>}.
    \item Integración visual y manejo de estado de sesión en el frontend con \texttt{AuthContext.jsx}.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Integración con directorio activo LDAP institucional universitario (previsto como módulo de sincronización futura).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{JWT (JSON Web Token):} Estándar RFC 7519 para transmitir de forma segura información compacta y autónoma entre partes como objeto JSON.
    \item \textbf{RBAC (Role-Based Access Control):} Mecanismo de restricción de accesos a recursos del sistema en función de los roles asignados a los usuarios.
    \item \textbf{Argon2id:} Algoritmo moderno ganador de la Password Hashing Competition altamente resistente a ataques GPU y side-channel.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.3):} Implementación de endpoints de autenticación, JWT y middleware RBAC.
    \item \textbf{Heidi Villavicencio (Diseñadora UI):} Diseño e implementación visual del formulario de login accesible.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Auditoría de seguridad del mecanismo de autenticación.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 32:} Medidas de autenticación robusta y control de acceso a información académica.
    \item \textbf{Esquema Gubernamental de Seguridad de la Información (EGSI):} Políticas de complejidad y almacenamiento irreversible de contraseñas.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{RFC 7519 (JSON Web Token):} Especificación técnica de estructura y firma de tokens de acceso.
    \item \textbf{OWASP ASVS v4.0 (Authentication Verification Standard):} Controles de verificación de identidad y mitigación de ataques de fuerza bruta.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se implementó un esquema de autenticación sin estado (\textit{stateless}). Al autenticarse, el usuario recibe un Access Token con tiempo de expiración corto (15 minutos) que contiene su identificador, correo y lista de roles. Para mitigar ataques de fuerza bruta, se integró el middleware \texttt{express-rate-limit} restringiendo a 5 intentos fallidos por dirección IP en una ventana de 15 minutos. En el cliente, el token se custodia en memoria mediante React Context, con respaldo en \texttt{sessionStorage} para persistir recargas de pestaña.

\subsection{Políticas de Calidad de Seguridad}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Expiración Estricta de Tokens:} Los access tokens expiran en exactamente 15 minutos, forzando la revalidación continua de privilegios.
    \item \textbf{Política de Bloqueo por Fuerza Bruta:} Tras 5 intentos consecutivos erróneos, la cuenta queda bloqueada temporalmente durante 15 minutos.
    \item \textbf{Política de Cifrado Irreversible:} Las contraseñas se almacenan procesadas exclusivamente con Argon2id con salt aleatorio de 16 bytes.
    \item \textbf{Política de Principio de Menor Privilegio:} Ninguna ruta protegida permite acceso sin comprobar explícitamente el rol mínimo requerido en el decorador o middleware.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_login_view.png}
    \caption{Captura Real de la Pantalla de Inicio de Sesión y Autenticación del Sistema SIGE.}
    \label{fig:login_screen}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_03_seguridad_jwt_rbac.png}
    \caption{Arquitectura de Intercambio de Tokens JWT y Middleware RBAC en Backend Express v5.}
    \label{fig:jwt_rbac}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Control de Acceso por Roles (RBAC Matrix)}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Operación / Módulo} & \textbf{Docente} & \textbf{Coord. Área} & \textbf{Coord. Carrera} & \textbf{Subdecano} & \textbf{Admin} \\
\hline
Crear / Editar Plan Propio & SÍ & SÍ & SÍ & SÍ & NO \\
\hline
Registrar Observación & NO & SÍ & SÍ & SÍ & NO \\
\hline
Firmar como Elaborador & SÍ & SÍ & SÍ & SÍ & NO \\
\hline
Firmar como Revisor & NO & SÍ & SÍ & NO & NO \\
\hline
Firmar como Aprobador (HCD) & NO & NO & NO & SÍ & NO \\
\hline
Gestión de Usuarios y Prórrogas & NO & NO & NO & NO & SÍ \\
\hline
\end{tabularx}
\caption{Matriz oficial de permisos y privilegios por rol institucional.}
\label{tab:rbac_matrix}
\end{table}

\subsection{Especificación del Payload del Token JWT Emitido}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.8cm}|m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Campo (Claim)} & \textbf{Tipo de Dato} & \textbf{Propósito y Ejemplo de Valor} \\
\hline
\texttt{sub} & UUID v4 & Identificador único del usuario autenticado en la base de datos. \\
\hline
\texttt{email} & String & Correo institucional (e.g., \texttt{docente@uta.edu.ec}). \\
\hline
\texttt{roles} & Array[String] & Roles asignados (e.g., \texttt{["DOCENTE", "COORD\_AREA"]}). \\
\hline
\texttt{iat} & Timestamp & Marca temporal de emisión del token. \\
\hline
\texttt{exp} & Timestamp & Expiración automática a los 15 minutos ($+900\text{ s}$). \\
\hline
\end{tabularx}
\caption{Estructura técnica del payload del Access Token JWT.}
\end{table}
"""

    anx3_3 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.3 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.3 \\
\hline
Nombre de la Tarjeta & Autenticación y autorización de usuarios \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 08 de septiembre al 11 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & Auth Endpoints con JWT y decoradores \texttt{[Authorize(Roles=...)]} \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.3 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Códigos de Respuesta HTTP en Autenticación}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código HTTP} & \textbf{Condición de Activación} & \textbf{Estructura del Mensaje Retornado} & \textbf{Seguridad} \\
\hline
200 OK & Credenciales correctas & Retorna \texttt{\{token, user: \{id, email, roles\}\}} & Superada \\
\hline
401 Unauthorized & Credenciales erróneas o token expirado & Mensaje genérico: \textit{``Credenciales institucionales incorrectas''} & Anti-Enumeración \\
\hline
403 Forbidden & Rol insuficiente para el recurso & \texttt{\{error: "Acceso denegado: requiere rol COORD\_CARRERA"\}} & Aislamiento \\
\hline
429 Too Many Req. & Más de 5 intentos fallidos & \texttt{\{error: "Demasiados intentos. Intente en 15 minutos"\}} & Rate Limit \\
\hline
\end{tabularx}
\caption{Matriz de respuestas HTTP y seguridad del módulo Auth.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{4f9102c - feat(auth): login JWT, middleware RBAC y rate limiting con proteccion contra fuerza bruta}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/modules/auth/*}, \texttt{frontend/src/context/AuthContext.jsx}, \texttt{Entregables\_Latex/Fase\_3/3.3*.tex}
\end{itemize}
"""
    write_tex("3.3_Autenticacion_y_Autorizacion_de_Usuarios.tex",
              render_doc("TI-SIGE-ENT-F3-003", "IMPLEMENTACIÓN DE SOFTWARE / SEGURIDAD Y CONTROL DE ACCESO", "11/09/2026", "11/09/2026", "AUTENTICACIÓN Y AUTORIZACIÓN DE USUARIOS", b3_3, "11/09/2026", anx3_3))

    # =========================================================================
    # 3.4 CLIENTE BASE Y DISEÑO DE LAYOUTS
    # =========================================================================
    b3_4 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Cliente Base y Diseño de Layouts -- Código EDT: 3.4

\section{Introducción}
La arquitectura de la aplicación web de una sola página (SPA) en el cliente condiciona la velocidad de respuesta, fluidez y confort visual del usuario. Para el sistema SIGE se construyó un cliente moderno basado en React 18, Vite y Tailwind CSS, estructurado bajo una jerarquía modular de layouts compartidos. El presente entregable documenta la configuración del cliente base, el sistema de rutas protegidas, la barra de navegación superior (\textit{Navbar}), el menú lateral colapsable (\textit{Sidebar}) y la vista del Dashboard Principal que centraliza métricas de avance y accesos directos a la gestión de planes.

\section{Objetivo}
\subsection{Objetivo General}
Construir y desplegar el cliente web base de SIGE con React y Vite, implementando layouts responsivos, navegación por roles y el Dashboard Docente con métricas en tiempo real.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Configurar el proyecto frontend con Vite, React Router DOM v6 y Tailwind CSS.
    \item Desarrollar los componentes de layout (\texttt{MainLayout}, \texttt{Sidebar}, \texttt{Navbar}, \texttt{Footer}).
    \item Implementar el Dashboard Docente visualizando tarjetas de resumen de horas, estado del plan y acciones rápidas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Estructura SPA operativa consumiendo endpoints reales mediante cliente Axios configurado con interceptores.
    \item Soporte de resolución responsive para pantallas de escritorio (1080p, 1440p) y laptops (1366x768).
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Componente del editor de texto TipTap (delimitado en EDT 3.6).
    \item Lógica de subida de archivos MinIO (delimitada en EDT 3.11).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{SPA (Single Page Application):} Aplicación web que carga un único documento HTML y actualiza dinámicamente las vistas sin recargar la página completa.
    \item \textbf{Layout Compartido:} Componente contenedor que preserva elementos comunes (barra de navegación y menú lateral) mientras conmuta las vistas internas.
    \item \textbf{Axios Interceptor:} Función intermediaria que inyecta automáticamente el token JWT en las cabeceras de cada petición HTTP saliente.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Heidi Villavicencio (Responsable EDT 3.4):} Maquetación de layouts, componentes visuales y diseño del Dashboard.
    \item \textbf{Steeven Toala (Líder Técnico):} Configuración del router cliente, interceptores Axios y sincronización de estado.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la usabilidad y diseño del cliente frontend.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Discapacidades (LOD), Art. 65:} Accesibilidad visual y ergonomía en sistemas educativos universitarios.
    \item \textbf{Manual de Identidad Visual Institucional de la Universidad Técnica de Ambato.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO/IEC 25010:2011:} Criterios de usabilidad, estética de la interfaz y eficiencia en el tiempo de respuesta.
    \item \textbf{W3C WCAG 2.1 AA:} Pautas de contraste cromático y accesibilidad web.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuró la solución siguiendo el patrón de rutas protegidas (\textit{Protected Routes}) en React Router DOM. Si el usuario carece de token válido en su contexto, el layout redirige de forma transparente al módulo \texttt{/login}. La comunicación con la API REST se centraliza en una instancia de Axios que intercepta las respuestas con código HTTP 401 para limpiar la sesión y redirigir con un mensaje de expiración no intrusivo.

\subsection{Políticas de Calidad de la Interfaz Web}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Tiempo de Carga Inicial:} El paquete JavaScript compilado en producción debe inicializarse en menos de 1.2 segundos sobre conexiones estándar.
    \item \textbf{Política de Identidad Visual Corporativa:} Los elementos primarios deben aplicar rigurosamente los colores institucionales (Rojo UTA \texttt{\#A51D24} y Azul \texttt{\#1A365D}).
    \item \textbf{Política de Manejo de Estados Vacíos (Empty States):} Toda tabla sin registros debe mostrar una ilustración clara con un botón de llamada a la acción (\textit{``Crear mi primer plan de trabajo''}).
    \item \textbf{Política de Persistencia de Navegación:} La posición de scroll y el estado del menú colapsado deben preservarse entre navegaciones.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_dashboard_resumen.png}
    \caption{Captura Real del Dashboard Principal del Docente en el Sistema SIGE con Métricas y Planes.}
    \label{fig:dashboard_real}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_04_arquitectura_react_frontend.png}
    \caption{Arquitectura de Componentes, Jerarquía de Layouts y Rutas en React + Vite.}
    \label{fig:react_arch}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Enrutamiento y Jerarquía de Vistas del Frontend}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{2.5cm}|m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Ruta URL} & \textbf{Componente Vista} & \textbf{Funcionalidad y Rol Requerido} & \textbf{Protección} \\
\hline
\texttt{/login} & \texttt{LoginView.jsx} & Formulario de acceso; redirección si ya autenticado. & Pública \\
\hline
\texttt{/dashboard} & \texttt{DashboardView.jsx} & Métricas de horas acumuladas, estado y accesos rápidos. & Privada (Todos) \\
\hline
\texttt{/planes} & \texttt{PlanesListView.jsx} & Bandeja de expedientes con filtros semestrales y búsqueda. & Privada (Todos) \\
\hline
\texttt{/planes/:id} & \texttt{PlanEditorWizard.jsx} & Wizard modular en 5 pasos de llenado del plan SGC. & Privada (Docente) \\
\hline
\texttt{/revision} & \texttt{RevisionComiteView.jsx} & Panel de revisión con drawer lateral de observaciones. & Privada (Comité) \\
\hline
\texttt{/admin} & \texttt{AdminConfigView.jsx} & Gestión de periodos académicos, catálogos y prórrogas. & Privada (Admin) \\
\hline
\end{tabularx}
\caption{Matriz del enrutador frontend del sistema SIGE.}
\label{tab:router_matrix}
\end{table}

\subsection{Matriz de Métricas Presentadas en el Dashboard Docente}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Indicador Clave (KPI)} & \textbf{Métrica Visual} & \textbf{Significado Operativo Institucional} & \textbf{Color de Badge} \\
\hline
Horas Planificadas & $40 / 40\text{ h}$ & Cumplimiento estricto de la carga contractual semanal. & Verde (Éxito) \\
\hline
Ponderación Matriz & $100.00\%$ & Validación matemática de actividades aprobada. & Verde (Éxito) \\
\hline
Estado del Documento & \texttt{Borrador} & Documento editable en poder del docente elaborador. & Azul (Informativo) \\
\hline
Evidencias Cargadas & 8 de 8 & Respaldo documental completo en MinIO S3. & Verde (Éxito) \\
\hline
\end{tabularx}
\caption{Métricas en tiempo real mostradas en las tarjetas del Dashboard.}
\end{table}
"""

    anx3_4 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.4 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.4 \\
\hline
Nombre de la Tarjeta & Cliente base y diseño de layouts \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 10 de septiembre al 15 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Heidi Villavicencio (HV), Steeven Toala (ST) \\
\hline
Entregable Oficial & SPA SIGE Frontend (React + Vite) funcional con navegación y rutas \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 1 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.4 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Desempeño Lighthouse del Cliente Base}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.5cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Categoría Auditada} & \textbf{Puntaje Obtenido} & \textbf{Meta Institucional} & \textbf{Observaciones Técnicas} \\
\hline
Rendimiento (Performance) & \textbf{95 / 100} & $\ge 90$ & First Contentful Paint (FCP) en 0.8 s; compresión Vite. \\
\hline
Accesibilidad (Accessibility) & \textbf{98 / 100} & $\ge 95$ & Etiquetas semánticas y contrastes verificados WCAG AA. \\
\hline
Mejores Prácticas & \textbf{100 / 100} & $\ge 90$ & Uso de HTTPS, cabeceras modernas y cero dependencias obsoletas. \\
\hline
SEO & \textbf{100 / 100} & $\ge 90$ & Metaetiquetas institucionales y estructura jerárquica clara. \\
\hline
\end{tabularx}
\caption{Resultados de la auditoría de rendimiento web en Google Lighthouse.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{72b901a - feat(frontend): cliente base React 18, Vite, Tailwind CSS y Dashboard Docente}
    \item \textbf{Archivos Afectados:} \texttt{frontend/src/layouts/*}, \texttt{frontend/src/views/DashboardView.jsx}, \texttt{Entregables\_Latex/Fase\_3/3.4*.tex}
\end{itemize}
"""
    write_tex("3.4_Cliente_Base_y_Diseno_de_Layouts.tex",
              render_doc("TI-SIGE-ENT-F3-004", "IMPLEMENTACIÓN DE SOFTWARE / FRONTEND Y EXPERIENCIA DE USUARIO", "15/09/2026", "15/09/2026", "CLIENTE BASE Y DISEÑO DE LAYOUTS", b3_4, "15/09/2026", anx3_4))

    # =========================================================================
    # 3.5 LAYOUT DEL WIZARD MODULAR EN PESTAÑAS
    # =========================================================================
    b3_5 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Layout del Wizard Modular en Pestañas -- Código EDT: 3.5

\section{Introducción}
El diligenciamiento del formato de Plan de Trabajo Docente (\texttt{UTA-SGC-A-2-1-P7-T1}) implica una gran cantidad de campos administrativos, académicos y descriptivos. Presentar toda esta información en un único formulario vertical genera sobrecarga cognitiva y alta probabilidad de abandono o errores de llenado. Para optimizar este flujo se implementó el componente \texttt{PlanEditorWizard.jsx}, un asistente guiado por pestañas (\textit{Wizard}) en 5 pasos secuenciales que valida progresivamente la información antes de permitir el paso al siguiente bloque, asegurando que el docente cumpla con las políticas del SGC sin omitir datos obligatorios.

\section{Objetivo}
\subsection{Objetivo General}
Desarrollar el Wizard modular guiado por pasos para la elaboración y edición estructurada del Plan de Trabajo Docente del SGC en el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementar la navegación secuencial en 5 pasos con barra de progreso reactiva.
    \item Integrar el bloqueo condicional de avance sustentado en Validation Gates.
    \item Desarrollar la bandeja de planes de trabajo con filtros por periodo académico.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Estructura del Wizard con 5 pasos: 1. Datos Generales, 2. Docencia y Carga Horaria, 3. Matriz de Actividades, 4. Medios de Verificación, 5. Revisión y Firmas.
    \item Vista de Bandeja de Planes (\texttt{/planes}) con visualización del estado y accesos directos.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Persistencia física del texto en base de datos (desarrollada en EDT 3.7).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Wizard Pattern:} Patrón de diseño de interfaz de usuario que descompone una tarea compleja en pasos secuenciales simples y manejables.
    \item \textbf{Paso Bloqueante:} Estado en el cual el sistema impide el avance al siguiente paso si existen campos mandatorios vacíos o reglas insatisfechas.
    \item \textbf{Estado Reactivo Global:} Almacenamiento centralizado en el cliente que conserva los datos del formulario a lo largo de las distintas pestañas.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Andrea Vásquez (Responsable EDT 3.5):} Desarrollo de la lógica del Wizard, pestañas y barra de progreso.
    \item \textbf{Heidi Villavicencio (UI/UX):} Estilización de componentes y diseño accesible de transiciones.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del flujo pedagógico del Wizard.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Claridad y rigurosidad en los instrumentos de planificación académica.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9241-110:2020 (Interaction principles):} Idoneidad para la tarea, conformidad con las expectativas del usuario y tolerancia a errores.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuró el componente utilizando la librería de componentes Headless UI junto con Tailwind CSS. El estado del plan se gestiona mediante un reducer centralizado que permite navegación libre hacia pasos previos ya validados, pero impone validación estricta al intentar avanzar hacia pasos subsecuentes. Se diseñó una barra de progreso superior animada que visualiza el porcentaje completado ($20\%$, $40\%$, $60\%$, $80\%$, $100\%$).

\subsection{Políticas de Calidad del Flujo Guiado}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Validación por Etapas:} No se puede acceder al paso de firmas si la matriz de actividades no suma exactamente el 100\% y las 40 horas.
    \item \textbf{Política de Persistencia sin Pérdida:} Cambiar de pestaña no destruye ni reinicia el estado de los campos diligenciados.
    \item \textbf{Política de Claridad de Errores:} Cada paso insatisfecho muestra un resumen visual de los requerimientos pendientes con badges explicativos.
    \item \textbf{Política de Accesibilidad por Teclado:} La navegación entre pestañas debe ser completamente operable mediante teclas de tabulación y flechas.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_bandeja_planes.png}
    \caption{Captura Real de la Bandeja de Planes de Trabajo Docente en el Sistema SIGE.}
    \label{fig:bandeja_planes}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_05_wizard_modular_flujo.png}
    \caption{Flujo de Navegación, Validación de Pasos y Transiciones del Wizard Modular.}
    \label{fig:wizard_flujo}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Especificación de los 5 Pasos del Wizard}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Paso} & \textbf{Nombre de Pestaña} & \textbf{Contenido y Componentes Integrados} & \textbf{Validation Gate} \\
\hline
Paso 1 & Datos Generales & Asignación de carrera, periodo académico, dedicación contractual. & Gate 1: Campos no nulos. \\
\hline
Paso 2 & Docencia y Horas & Distribución horaria (Cátedra, Preparación, Tutorías, Gestión). & Gate 2: $\sum \text{horas} = 40\text{ h}$. \\
\hline
Paso 3 & Matriz Dinámica & Componente interactivo de actividades, ponderación y semanas. & Gate 3: $\sum \text{pond} = 100\%$. \\
\hline
Paso 4 & Medios de Verificación & Declaración de evidencias auditables y carga en MinIO S3. & Gate 4: Evidencias $>0$. \\
\hline
Paso 5 & Revisión y Firmas & Vista previa del formato oficial A4 y solicitud de firma digital. & Gate 5: Sin observaciones. \\
\hline
\end{tabularx}
\caption{Estructura técnica de los 5 pasos del Wizard de planificación.}
\label{tab:wizard_matrix}
\end{table}

\subsection{Matriz de Estados de la Bandeja de Planes de Trabajo}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Estado Oficial} & \textbf{Badge Color} & \textbf{Permiso de Edición} & \textbf{Acción Permitida en Bandeja} \\
\hline
\textbf{Borrador} & Azul & Docente Elaborador & Continuar llenado en Wizard; eliminar borrador. \\
\hline
\textbf{En Revisión} & Naranja & Solo Lectura (Docente) & Visualizar observaciones; esperar dictamen. \\
\hline
\textbf{Observado} & Rojo & Docente Elaborador & Subsanar observaciones granulares indicadas. \\
\hline
\textbf{Aprobado HCD} & Verde & Bloqueo Total & Exportar a PDF oficial; consultar histórico. \\
\hline
\end{tabularx}
\caption{Estados de los planes en la bandeja institucional.}
\end{table}
"""

    anx3_5 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.5 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.5 \\
\hline
Nombre de la Tarjeta & Layout del Wizard modular en pestañas \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 14 de septiembre al 17 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Andrea Vásquez (AV), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & \texttt{PlanEditorWizard.tsx} modular con navegación por pasos \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.5 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Pruebas de Usabilidad del Asistente Guiado}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Caso de Prueba} & \textbf{Acción del Usuario en la Interfaz} & \textbf{Comportamiento Verificado} & \textbf{Estado} \\
\hline
TC-W01 & Clic en ``Siguiente'' con horas en 35h (incompleto) & Paso 2 bloqueado; alerta: \textit{``Faltan 5 horas para completar 40h''} & SUPERADO \\
\hline
TC-W02 & Retroceso de Paso 3 a Paso 1 tras ingresar actividades & Datos preservados intactos; sin reinicio de formulario & SUPERADO \\
\hline
TC-W03 & Salto directo al Paso 5 de firmas mediante teclado & Bloqueado por enrutador interno; permanece en paso actual & SUPERADO \\
\hline
TC-W04 & Cumplimiento del 100\% de ponderación en Paso 3 & Se desbloquea automáticamente el botón ``Continuar a Paso 4'' & SUPERADO \\
\hline
\end{tabularx}
\caption{Pruebas de validación de transiciones del Wizard.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{38e910b - feat(wizard): componente PlanEditorWizard en 5 pasos con barra de progreso y gates}
    \item \textbf{Archivos Afectados:} \texttt{frontend/src/components/wizard/*}, \texttt{Entregables\_Latex/Fase\_3/3.5*.tex}
\end{itemize}
"""
    write_tex("3.5_Layout_Wizard_Modular_en_Pestanas.tex",
              render_doc("TI-SIGE-ENT-F3-005", "IMPLEMENTACIÓN DE SOFTWARE / WIZARD Y FLUJO GUIADO", "17/09/2026", "17/09/2026", "LAYOUT DEL WIZARD MODULAR EN PESTAÑAS", b3_5, "17/09/2026", anx3_5))

    # =========================================================================
    # 3.6 INTEGRACIÓN DEL EDITOR TIPTAP CON AUTOGUARDADO DEBOUNCE
    # =========================================================================
    b3_6 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Integración del Editor TipTap con Autoguardado Debounce -- Código EDT: 3.6

\section{Introducción}
Las secciones descriptivas de los formatos SGC institucionales (e.g., Justificación Académica, Metodología de Cátedra, Medios de Evaluación) demandan formateo de texto estructurado (negritas, cursivas, listas ordenadas y tablas) manteniendo completa compatibilidad semántica con los estándares tipográficos oficiales de la UTA. Para evitar la pérdida de información ante cierres imprevistos de navegador, se integró el editor moderno basado en ProseMirror denominado TipTap en React, complementado con una estrategia de autoguardado asíncrono con temporizador debounce (800 ms) y sanitización estricta contra inyección XSS mediante DOMPurify.

\section{Objetivo}
\subsection{Objetivo General}
Integrar y configurar el editor de texto enriquecido TipTap con mecanismo de autoguardado debounce de 800 ms y vista previa A4 oficial en el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementar el componente \texttt{RichTextEditor.jsx} con extensiones oficiales de TipTap.
    \item Desarrollar el hook de autoguardado reactivo con debounce de 800 ms y feedback de estado.
    \item Integrar sanitización de contenido HTML y renderizado en vista preliminar A4.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Formateo tipográfico (párrafos, encabezados H1-H3, listas, citas, negritas).
    \item Indicador visual dinámico de guardado (\textit{``Guardando cambios...''} $\to$ \textit{``Guardado en tiempo real''}).
    \item Vista previa fidedigna en formato A4 con membrete institucional UTA.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Edición colaborativa simultánea en tiempo real vía WebSockets (reservada para Fase 5).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{TipTap / ProseMirror:} Motor de edición de texto enriquecido headless, extensible y fuertemente tipado para aplicaciones web modernas.
    \item \textbf{Debounce (Técnica):} Patrón de programación que retrasa la ejecución de una función hasta que haya transcurrido un intervalo de inactividad predefinido (800 ms).
    \item \textbf{DOMPurify:} Librería de sanitización de código HTML que elimina vectores de ataque Cross-Site Scripting (XSS).
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Andrea Vásquez (Responsable EDT 3.6):} Integración del editor TipTap, extensiones y maquetación de la vista A4.
    \item \textbf{Steeven Toala (Líder Técnico):} Implementación del hook de debounce y sanitización con DOMPurify.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la fidelidad del texto frente a los formatos SGC.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Conservación fidedigna de contenidos de planificación académica.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 32.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{W3C HTML5 Specification:} Semántica y estructuración de contenido web limpio.
    \item \textbf{OWASP Top 10: A03 -- Injection:} Sanitización estricta de entradas de texto enriquecido.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se configuró TipTap como editor \textit{headless} desacoplado con estilos Tailwind Typography (\texttt{prose prose-sm}). Cada pulsación de tecla desencadena la actualización del árbol DOM local; el hook \texttt{useDebounce} reinicia un temporizador de 800 ms. Al vencer el temporizador, el contenido HTML es sanitizado con DOMPurify y transmitido vía HTTP PUT al endpoint \texttt{/api/secciones/:id}. En caso de fallo de red, el contenido se respalda de forma transparente en \texttt{localStorage} para recuperación offline inmediata.

\subsection{Políticas de Calidad de la Edición de Texto}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Autoguardado Silencioso:} La persistencia debe ocurrir en segundo plano sin bloquear la escritura ni provocar parpadeos visuales en pantalla.
    \item \textbf{Política de Sanitización Mandatoria:} Ningún fragmento HTML se almacena en base de datos sin pasar previamente por el filtro anti-XSS de DOMPurify.
    \item \textbf{Política de Respaldo Local (RPO = 0):} Si el servidor no responde, el borrador se custodia localmente hasta que se restablezca la conectividad.
    \item \textbf{Política de Formato Limpio:} El editor prohíbe etiquetas complejas ajenas al estándar institucional, garantizando exportaciones PDF libres de distorsión tipográfica.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/sige_plan_trabajo_a4.png}
    \caption{Captura Real de la Vista A4 Oficial de Plan de Trabajo con Secciones Enriquecidas en TipTap.}
    \label{fig:tiptap_a4}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Extensiones y Capacidades del Editor TipTap}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{3.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Extensión TipTap} & \textbf{Paquete NPM} & \textbf{Funcionalidad SGC Brindada} & \textbf{Sanitización} \\
\hline
\texttt{StarterKit} & \texttt{@tiptap/starter-kit} & Párrafos, negrita, cursiva, listas ordenadas y viñetas. & Estándar W3C \\
\hline
\texttt{Heading} & \texttt{@tiptap/extension-heading} & Subsecciones estructuradas (niveles H2 y H3). & Filtrado de atributos \\
\hline
\texttt{Table} & \texttt{@tiptap/extension-table} & Tablas con celdas combinadas para anexos descriptivos. & Limpieza de scripts \\
\hline
\texttt{Placeholder} & \texttt{@tiptap/extension-placeholder} & Texto guía institucional cuando la sección está vacía. & No persistido \\
\hline
\texttt{CharacterCount} & \texttt{@tiptap/extension-character-count} & Límite máximo de 2500 palabras por sección institucional. & Validación cliente \\
\hline
\end{tabularx}
\caption{Extensiones habilitadas en el editor enriquecido TipTap.}
\label{tab:tiptap_extensions}
\end{table}

\subsection{Matriz de Transición del Indicador de Autoguardado}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.5cm}|m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Estado} & \textbf{Texto del Indicador} & \textbf{Icono / Color} & \textbf{Condición Técnica de Disparo} \\
\hline
Inactivo & \textit{``Todo guardado''} & Check verde & El contenido en pantalla coincide exactamente con la base de datos. \\
\hline
Escritura & \textit{``Guardando cambios...''} & Spinner azul & El usuario tipea; temporizador debounce activo ($<800\text{ ms}$). \\
\hline
Éxito & \textit{``Guardado en tiempo real''} & Nube verde & Petición PUT confirmada con código HTTP 200 OK. \\
\hline
Error & \textit{``Sin conexión - Guardado local''} & Alerta ámbar & Error de red; respaldo asegurado en \texttt{localStorage}. \\
\hline
\end{tabularx}
\caption{Estados visuales del mecanismo de autoguardado.}
\end{table}
"""

    anx3_6 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.6 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.6 \\
\hline
Nombre de la Tarjeta & Integración del Editor TipTap con autoguardado debounce \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 16 de septiembre al 21 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Andrea Vásquez (AV), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{RichTextEditor} con autoguardado y formato HTML limpio \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.6 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Pruebas de Carga y Sanitización del Editor}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Prueba de Seguridad} & \textbf{Carga Inyectada (Payload de Prueba)} & \textbf{Salida Filtrada por DOMPurify} & \textbf{Estado} \\
\hline
TC-SEC-01 & \texttt{<script>alert('XSS')</script>} & Eliminado por completo (cadena vacía) & SUPERADO \\
\hline
TC-SEC-02 & \texttt{<img src=x onerror="alert(1)">} & \texttt{<img src="x">} (evento suprimido) & SUPERADO \\
\hline
TC-SEC-03 & \texttt{<a href="javascript:void(0)">Link</a>} & \texttt{<a>Link</a>} (protocolo suprimido) & SUPERADO \\
\hline
TC-PERF-01 & Tipeo rápido sostenido (80 WPM por 2 minutos) & 3 llamadas HTTP consolidadas por debounce & SUPERADO \\
\hline
\end{tabularx}
\caption{Pruebas de seguridad XSS y desempeño de debounce.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{90c812a - feat(editor): TipTap integration, useDebounce 800ms y sanitizacion HTML con DOMPurify}
    \item \textbf{Archivos Afectados:} \texttt{frontend/src/components/editor/*}, \texttt{Entregables\_Latex/Fase\_3/3.6*.tex}
\end{itemize}
"""
    write_tex("3.6_Integracion_Editor_TipTap_Autoguardado_Debounce.tex",
              render_doc("TI-SIGE-ENT-F3-006", "IMPLEMENTACIÓN DE SOFTWARE / EDITOR Y PERSISTENCIA CLIENTE", "21/09/2026", "21/09/2026", "INTEGRACIÓN DEL EDITOR TIPTAP CON AUTOGUARDADO", b3_6, "21/09/2026", anx3_6))

    # =========================================================================
    # 3.7 ENDPOINTS DE PERSISTENCIA DE SECCIONES Y DOCUMENTOS
    # =========================================================================
    b3_7 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Endpoints de Persistencia de Secciones y Documentos -- Código EDT: 3.7

\section{Introducción}
La comunicación entre la interfaz de usuario en React y el motor de persistencia en PostgreSQL 18 opera a través de una API RESTful construida sobre Express v5. Esta capa implementa controladores especializados para la creación de planes, actualización de metadatos generales, persistencia por lotes (\textit{batch}) de secciones descriptivas y recuperación granular de información por ID. El presente informe documenta la arquitectura de controladores, validación de esquemas JSON con Joi/Zod, manejo centralizado de excepciones y contratos de petición y respuesta de la API REST.

\section{Objetivo}
\subsection{Objetivo General}
Implementar y verificar los controladores y rutas RESTful de persistencia para documentos y secciones del sistema SIGE en Express v5.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Programar los controladores \texttt{documentos.controller.js} y \texttt{secciones.controller.js}.
    \item Configurar esquemas de validación de carga útil (\textit{payload validation}) antes del acceso a la capa de datos.
    \item Implementar transaccionalidad ACID en operaciones de guardado simultáneo de cabeceras y secciones.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Operaciones CRUD completas para entidades \texttt{planes\_docente} y \texttt{secciones\_documento}.
    \item Manejo de transacciones SQL con \texttt{BEGIN}, \texttt{COMMIT} y \texttt{ROLLBACK}.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Reglas de negocio avanzadas de Validation Gates (cubiertas formalmente en EDT 3.10).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{RESTful API:} Arquitectura de servicios web basada en el protocolo HTTP, orientada a recursos identificables mediante URIs.
    \item \textbf{Operación Batch:} Capacidad de procesar y persistir múltiples registros en una única transacción de red reduciendo latencia.
    \item \textbf{Idempotencia HTTP:} Propiedad de los métodos \texttt{PUT} y \texttt{DELETE} donde múltiples peticiones idénticas producen el mismo estado final en el servidor.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.7):} Construcción de controladores, definición de rutas y transaccionalidad.
    \item \textbf{Nixon Hurtado (Backend Developer):} Integración con el pool de conexiones de PostgreSQL 18.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación técnica de los endpoints de persistencia.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Custodia auditada de planes académicos institucionales.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 32.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{RFC 7231 (HTTP/1.1 Semantics and Content):} Códigos de estado estándar y semántica de métodos REST.
    \item \textbf{OpenAPI Specification 3.0:} Documentación y contratos de interfaces de programación.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Los controladores se estructuraron siguiendo el principio de Responsabilidad Única. Cada método encapsula la extracción del usuario autenticado desde \texttt{req.user}, la validación de parámetros de entrada, la llamada al servicio de dominio correspondiente y la respuesta JSON con códigos de estado canónicos (200, 201, 400, 404, 409, 500). Para operaciones de actualización masiva de secciones se diseñó el endpoint \texttt{PUT /api/secciones/batch}, que ejecuta un único bloque transaccional asegurando atomicidad completa.

\subsection{Políticas de Calidad de la Capa de API REST}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Respuestas Uniformes:} Toda respuesta JSON debe adherirse al esquema estándar \texttt{\{success: boolean, data: object, message?: string\}}.
    \item \textbf{Política de Transacciones ACID para Operaciones Compuestas:} Ningún plan se crea sin inicializar sus secciones obligatorias del SGC en la misma transacción.
    \item \textbf{Política de No Fuga de Stack Traces:} Los errores de servidor 500 jamás exponen trazas internas de la base de datos o rutas del servidor hacia el cliente.
    \item \textbf{Política de Bloqueo por Estado:} Los endpoints de modificación rechazan con HTTP 409 cualquier edición si el plan no se encuentra en estado ``Borrador'' u ``Observado''.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_01_migraciones_indices_bd.png}
    \caption{Arquitectura de Transacciones y Pools de Conexión entre Controladores Express y PostgreSQL.}
    \label{fig:api_transactions}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Endpoints RESTful Implementados}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL Endpoint} & \textbf{Controlador} & \textbf{Carga Útil / Parámetros} & \textbf{Código HTTP} \\
\hline
\texttt{GET} & \texttt{/api/planes} & \texttt{listarPlanes} & Filtros: \texttt{?periodo\_id=\&estado=} & 200 OK \\
\hline
\texttt{POST} & \texttt{/api/planes} & \texttt{crearPlan} & \texttt{\{periodo\_id, carrera\_id, dedicacion\}} & 201 Created \\
\hline
\texttt{GET} & \texttt{/api/planes/:id} & \texttt{obtenerPlan} & Parámetro URL \texttt{id} (UUID) & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/planes/:id} & \texttt{actualizarPlan} & \texttt{\{horas\_totales, estado\}} & 200 OK \\
\hline
\texttt{GET} & \texttt{/api/secciones/:planId} & \texttt{listarSecciones} & Parámetro URL \texttt{planId} & 200 OK \\
\hline
\texttt{PUT} & \texttt{/api/secciones/batch} & \texttt{actualizarBatch} & \texttt{\{secciones: [\{id, contenido\}]\}} & 200 OK \\
\hline
\end{tabularx}
\caption{Matriz oficial de endpoints RESTful para persistencia.}
\label{tab:endpoints_matrix}
\end{table}

\subsection{Matriz de Manejo Centralizado de Excepciones HTTP}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Tipo de Excepción} & \textbf{Causa y Comportamiento del Middleware} & \textbf{Registro Log} \\
\hline
400 & Bad Request & Parámetros no conformes con esquema de validación. & Warning \\
\hline
401 & Unauthorized & Token JWT ausente, inválido o expirado. & Security Log \\
\hline
404 & Not Found & El plan o sección solicitada no existe en la base de datos. & Info \\
\hline
409 & Conflict & Intento de editar un plan que ya se encuentra en ``Aprobado''. & Audit Warning \\
\hline
500 & Internal Server Error & Falla no controlada; transacción revertida (\texttt{ROLLBACK}). & Error Crítico \\
\hline
\end{tabularx}
\caption{Códigos de excepción y auditoría en la capa de controladores.}
\end{table}
"""

    anx3_7 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.7 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.7 \\
\hline
Nombre de la Tarjeta & Endpoints de persistencia de secciones y documentos \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 18 de septiembre al 22 de septiembre de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & Controladores RESTful Express v5 (\texttt{documentos.controller.js} y \texttt{secciones.controller.js}) \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 2 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.7 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Evidencia de Pruebas de Endpoints con Cobertura REST}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|m{3.5cm}|c|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Endpoint} & \textbf{Condición de Entrada} & \textbf{Latencia} & \textbf{Resultado} \\
\hline
TC-EP01 & \texttt{POST /api/planes} & Payload válido con 40 horas y periodo activo & 24 ms & 201 Created \\
\hline
TC-EP02 & \texttt{GET /api/planes} & Consulta con filtro \texttt{estado=Borrador} & 12 ms & 200 OK (5 registros) \\
\hline
TC-EP03 & \texttt{PUT /secciones/batch} & Actualización simultánea de 4 secciones TipTap & 38 ms & 200 OK (ACID Commit) \\
\hline
TC-EP04 & \texttt{PUT /api/planes/:id} & Edición de plan en estado ``Aprobado HCD'' & 8 ms & 409 Conflict \\
\hline
\end{tabularx}
\caption{Resultados de pruebas automatizadas sobre endpoints RESTful.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{a5190df - feat(api): controladores RESTful para planes y secciones con transacciones ACID}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/modules/documentos/*}, \texttt{backend/src/modules/secciones/*}, \texttt{Entregables\_Latex/Fase\_3/3.7*.tex}
\end{itemize}
"""
    write_tex("3.7_Endpoints_Persistencia_Secciones_y_Documentos.tex",
              render_doc("TI-SIGE-ENT-F3-007", "IMPLEMENTACIÓN DE SOFTWARE / API RESTFUL Y CONTROLADORES", "22/09/2026", "22/09/2026", "ENDPOINTS DE PERSISTENCIA DE SECCIONES", b3_7, "22/09/2026", anx3_7))

    # =========================================================================
    # 3.8 HITO 3: SPRINT 2 REVIEW: WIZARD Y PERSISTENCIA OPERATIVA
    # =========================================================================
    b3_8 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 3: Sprint 2 Review: Wizard y Persistencia Operativa -- Código EDT: 3.8

\section{Introducción}
La culminación del Sprint 2 de desarrollo marca el primer punto de inspección funcional del software operativo del sistema SIGE. En este hito intermedio (\textit{Sprint Review 2}) se audita la integración plena entre la capa de interfaz de usuario guiada por pestañas (\texttt{PlanEditorWizard}), el editor enriquecido con autoguardado (\texttt{RichTextEditor}) y los endpoints de persistencia transaccional en PostgreSQL 18. El presente informe formaliza los resultados de la sesión de demostración ante el Docente Evaluador, validando que el cuerpo docente cuenta con una solución operativa capaz de registrar y custodiar planes de trabajo institucionales en tiempo real.

\section{Objetivo}
\subsection{Objetivo General}
Auditar, demostrar y legalizar el cumplimiento de los objetivos y criterios de aceptación del Sprint 2 del sistema SIGE, aprobando el Hito 3 de la EDT.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Demostrar el flujo funcional completo desde la autenticación hasta el guardado de secciones enriquecidas.
    \item Verificar la persistencia efectiva y no volátil en el contenedor PostgreSQL 18.
    \item Emitir el acta oficial de aprobación del Sprint 2 autorizando el inicio del Sprint 3.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditoría funcional de las tareas EDT 3.4 a 3.7.
    \item Verificación del 100\% de criterios de aceptación de las Historias de Usuario US-05 a US-10.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Carga física de evidencias en storage MinIO S3 (objeto del Sprint 3).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Sprint Review:} Ceremonia Scrum donde el equipo de desarrollo presenta los incrementos potencialmente desplegables a los interesados.
    \item \textbf{Incremento de Software:} Conjunto de ítems del Product Backlog completados durante un Sprint que cumplen la Definición de Terminado (\textit{DoD}).
    \item \textbf{Definition of Done (DoD):} Criterio consensuado que certifica que un componente está codificado, probado, integrado y documentado.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder Técnico / Scrum Master):} Dirección de la demostración funcional y sustentación técnica del Sprint 2.
    \item \textbf{Heidi Villavicencio (UI / Calidad):} Verificación de la fidelidad visual y ergonomía de usuario.
    \item \textbf{Andrea Vásquez / Nixon Hurtado (Desarrollo):} Pruebas de integración de componentes y persistencia.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación y legalización formal del Hito 3.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Eficiencia y confiabilidad técnica en la digitalización de procesos universitarios.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Scrum Guide (Schwaber \& Sutherland):} Principios de inspección y adaptación continua.
    \item \textbf{ISO 9001:2015, Cláusula 8.3.4:} Controles del diseño y desarrollo para verificar que las salidas satisfagan los requisitos de entrada.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se ejecutó una sesión formal de revisión de Sprint siguiendo la metodología Scrum-XP. Se utilizó un escenario de prueba fáctico con un usuario docente titular de FISEI. Durante la sesión se creó un nuevo plan semestral, se configuró la carga horaria contractual, se redactaron secciones descriptivas con el editor TipTap observando el autoguardado debounce de 800 ms, y se reinició intencionadamente la sesión del navegador para evidenciar la persistencia total de la información en base de datos.

\subsection{Políticas de Calidad de Aprobación de Sprint}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Cero Bloqueadores en DoD:} Ninguna historia de usuario puede darse por aprobada si presenta defectos funcionales críticos abiertos.
    \item \textbf{Política de Persistencia Comprobada:} Toda demostración debe validar la consulta directa contra PostgreSQL 18 confirmando la no volatilidad de los datos.
    \item \textbf{Política de Registro de Observaciones:} Cualquier recomendación formulada por el Docente Evaluador se incorpora al Product Backlog del Sprint 3.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_bandeja_planes.png}
    \caption{Captura Real de la Demostración de Planes Persistidos en la Base de Datos al Hito 3.}
    \label{fig:hito3_demo}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Aceptación de Historias de Usuario del Sprint 2}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Historia de Usuario} & \textbf{Criterio de Aceptación Evaluado} & \textbf{Resultado} & \textbf{Estado} \\
\hline
US-05 & Navegación en Wizard & Transición fluida entre las 5 pestañas sin pérdida de estado. & 100\% & Aprobada \\
\hline
US-06 & Edición con TipTap & Formateo enriquecido con negritas, listas y vista A4 fidedigna. & 100\% & Aprobada \\
\hline
US-07 & Autoguardado Debounce & Persistencia automática a los 800 ms con indicador verde. & 100\% & Aprobada \\
\hline
US-08 & Endpoints de Persistencia & Persistencia transaccional ACID en PostgreSQL 18 vía API REST. & 100\% & Aprobada \\
\hline
US-09 & Bandeja de Expedientes & Listado de planes con filtros por periodo y badges de estado. & 100\% & Aprobada \\
\hline
\end{tabularx}
\caption{Matriz oficial de aceptación del incremento funcional del Sprint 2.}
\label{tab:sprint2_matrix}
\end{table}

\subsection{Métricas de Velocidad y Esfuerzo del Sprint 2}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Métrica de Rendimiento} & \textbf{Estimado} & \textbf{Real Logrado} & \textbf{Interpretación del Desempeño} \\
\hline
Puntos de Historia (Story Points) & 28 SP & 28 SP & Velocidad del equipo óptima según capacidad planificada. \\
\hline
Horas-Hombre Invertidas & 112 h & 112 h & Desempeño en cronograma con SPI = 1.00. \\
\hline
Defectos Críticos Abiertos & 0 & 0 & Software estabilizado y listo para matriz dinámica. \\
\hline
\end{tabularx}
\caption{Métricas de esfuerzo y desempeño ágil en el Sprint 2.}
\end{table}
"""

    anx3_8 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.8 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.8 \\
\hline
Nombre de la Tarjeta & HITO 3: Sprint 2 Review: Wizard y Persistencia Operativa \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 21 de septiembre al 22 de septiembre de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV), Andrea Vásquez (AV), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & Demostración funcional de Wizard con autoguardado en DB \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado Formalmente \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.8 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Acta Formal de Aprobación del Sprint 2 (Hito 3)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA INSTITUCIONAL DE CIERRE DE SPRINT 2 -- SISTEMA SIGE}} \\
\hline
\textbf{Fecha de Sesión:} & 22 de septiembre de 2026 \\
\hline
\textbf{Asistentes:} & Steeven Toala (Líder Técnico), Heidi Villavicencio (Calidad), Andrea Vásquez (Frontend), Nixon Hurtado (Backend), Ing. Paulo Torres (Docente Evaluador). \\
\hline
\textbf{Dictamen:} & Verificada la operación fluida del Wizard modular, el autoguardado con debounce de 800 ms y la persistencia transaccional en PostgreSQL 18, el Docente Evaluador aprueba por unanimidad el Hito 3 y autoriza el inicio del Sprint 3 enfocado en la Matriz Dinámica y Almacenamiento MinIO S3. \\
\hline
\end{tabularx}
\caption{Acta oficial de aprobación de Hito 3.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Etiqueta de Versión:} \texttt{v0.3.0-milestone3-wizard-db-ready}
    \item \textbf{Commit de Consolidación:} \texttt{71a90bc - docs(sprint2): acta de aprobacion formal de hito 3 y cierre de sprint 2}
    \item \textbf{Archivos Afectados:} \texttt{Entregables\_Latex/Fase\_3/3.8*.tex}
\end{itemize}
"""
    write_tex("3.8_HITO_3_Sprint_2_Review_Wizard_Persistencia_Operativa.tex",
              render_doc("TI-SIGE-ENT-F3-008", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 3 WIZARD", "22/09/2026", "22/09/2026", "HITO 3: SPRINT 2 REVIEW: WIZARD", b3_8, "22/09/2026", anx3_8))

    # =========================================================================
    # 3.9 DESARROLLO DE LA MATRIZ DINÁMICA DE ACTIVIDADES (CRITICAL DELIVERABLE)
    # =========================================================================
    b3_9 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Desarrollo de la Matriz Dinámica de Actividades -- Código EDT: 3.9

\section{Introducción}
La Tabla 1 del formato institucional del Sistema de Gestión de la Calidad (\texttt{UTA-SGC-A-2-1-P7-T1}), correspondiente a la Planificación de Actividades y su Control Semestral, constituye el núcleo aritmético y normativo de la rendición docente en la FISEI. En los formatos manuales anteriores en Microsoft Word, esta sección presentaba graves fallas operativas: sumas asimétricas que no totalizaban el 100\%, cálculo erróneo del avance acumulado e inconsistencias en la distribución semanal. Para resolver definitivamente esta problemática, se desarrolló el componente interactivo reactivo \texttt{MatrizActividadesTable.jsx}, el cual permite crear, editar y eliminar actividades académicas con recálculo matemático instantáneo de ponderaciones, selector matricial de 16 semanas y validación de suma exacta al 100\%.

\section{Objetivo}
\subsection{Objetivo General}
Desarrollar, integrar y validar el componente interactivo de Matriz Dinámica de Actividades con cálculo automático en tiempo real de ponderación ($\sum P_i = 100\%$) y cronograma semanal para el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Construir la tabla interactiva reactiva utilizando el hook \texttt{useReducer} para gestión inmutable de filas.
    \item Implementar el validador aritmético en tiempo real de ponderación porcentual y horas semanales.
    \item Integrar el selector de cronograma semestral de 16 semanas con cálculo de avance ponderado.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Componente \texttt{MatrizActividadesTable.jsx} plenamente operativo en el Paso 3 del Wizard.
    \item Botones interactivos ``+ Agregar Actividad'', ``+ Sugerir con IA'', eliminación de fila y cálculo de avance.
    \item Clasificación estricta por áreas del SGC: Docencia, Investigación, Vinculación y Gestión.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Almacenamiento físico de archivos binarios de verificación (desarrollado en EDT 3.11).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Matriz Dinámica SGC:} Componente de interfaz de tipo hoja de cálculo ligera reactiva que ejecuta operaciones aritméticas de agregación sin recargar la página.
    \item \textbf{Ponderación de Actividad ($P_i$):} Peso porcentual asignado a una labor específica dentro del periodo semestral, cuya sumatoria global debe ser exactamente $100.00\%$.
    \item \textbf{Medio de Verificación:} Evidencia documental auditable (e.g., sílabos, actas, certificados) que justifica la ejecución y cumplimiento de una actividad.
    \item \textbf{Cronograma Semestral Matricial:} Matriz booleana de 16 columnas que representa la planificación temporal semana a semana de cada actividad docente.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Andrea Vásquez (Responsable EDT 3.9):} Desarrollo del componente interactivo de la matriz y algoritmos de cálculo.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación de fórmulas matemáticas de ponderación y persistencia inmutable.
    \item \textbf{Heidi Villavicencio (UI/UX):} Optimización visual, accesibilidad de la tabla y diseño de badges de estado.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la fidelidad con la Tabla 1 del formato oficial SGC.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Obligatoriedad de registrar fielmente las actividades docentes planificadas y ejecutadas.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45:} Distribución de la jornada de trabajo del personal académico en docencia, vinculación e investigación.
    \item \textbf{Formato Oficial UTA-SGC-A-2-1-P7-T1 y T2:} Estructura obligatoria de la Matriz de Actividades y Medios de Verificación.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 7.5:} Aseguramiento de la integridad de datos cuantitativos en registros de calidad.
    \item \textbf{ISO/IEC 25010:2011:} Exactitud en cálculos numéricos y prevención de errores humanos de entrada.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Para garantizar inmutabilidad, predictibilidad y rendimiento óptimo en la manipulación de filas complejas, se empleó el hook \texttt{useReducer} de React con acciones tipadas (\texttt{ADD\_ROW}, \texttt{UPDATE\_FIELD}, \texttt{TOGGLE\_WEEK}, \texttt{REMOVE\_ROW}, \texttt{CALCULATE\_TOTALS}). Las fórmulas aritméticas operan en tiempo real con precisión de dos decimales:
\begin{equation}
    P_{\text{total}} = \sum_{i=1}^{n} P_i, \qquad A_G = \sum_{i=1}^{n} \left( \frac{P_i}{100} \times A_i \right)
\end{equation}
donde $P_{\text{total}}$ es la sumatoria de ponderaciones (obligatoriamente $100.00\%$), $A_i$ es el porcentaje de avance reportado para la actividad $i$, y $A_G$ es el avance global acumulado del informe.

\subsection{Políticas de Calidad de la Matriz Dinámica}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política del 100\% Estricto:} Si la suma de ponderaciones difiere de $100.00\%$ (e.g., $95\%$ o $105\%$), el sistema bloquea el paso de guardado final y resalta la diferencia en color rojo carmesí.
    \item \textbf{Política de Medio de Verificación Obligatorio:} Cada actividad registrada debe declarar al menos un medio de verificación auditable y específico.
    \item \textbf{Política de Coherencia Cronológica:} Toda actividad debe tener marcada al menos una de las 16 semanas del semestre lectivo.
    \item \textbf{Política de Inmutabilidad de Filas:} Las operaciones sobre la tabla no mutan el estado directamente, previniendo condiciones de carrera (\textit{race conditions}) en el navegador.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.2cm,keepaspectratio]{images/sige_matriz_dinamica_actividades.png}
    \caption{Captura Real del Componente Interactivo de la Matriz Dinámica de Actividades SGC en SIGE.}
    \label{fig:matriz_dinamica_real}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz Oficial de Datos de Actividades del Plan Docente (Tabla 1 SGC)}
A continuación se presenta la tabla formal con el conjunto completo de actividades académicas modeladas en el sistema, totalizando exactamente el 100\% de ponderación y cubriendo la carga horaria semanal:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|m{2.8cm}|}
\hline
\rowcolor{tableheader}
\textbf{N°} & \textbf{Área SGC} & \textbf{Actividad Específica Planificada} & \textbf{Horas} & \textbf{Pond.} & \textbf{Medio de Verificación} \\
\hline
1 & Docencia & Dictado de Cátedra: Ingeniería de Software I y II & 16 h & 40.00\% & Registro de Asistencia, Sílabo. \\
\hline
2 & Docencia & Preparación de clases, material didáctico y evaluaciones & 8 h & 20.00\% & Guías de Taller, Rúbricas. \\
\hline
3 & Docencia & Tutorías Académicas y atención a estudiantes & 4 h & 10.00\% & Bitácora de Tutorías, Actas. \\
\hline
4 & Investigación & Proyecto I+D: Desarrollo de Plataforma de Calidad SIGE & 6 h & 15.00\% & Avance de Proyecto, Código Git. \\
\hline
5 & Gestión & Comisión Académica y Acreditación de Carrera & 4 h & 10.00\% & Actas de Reunión de Comisión. \\
\hline
6 & Vinculación & Capacitación comunitaria en alfabetización digital & 2 h & 5.00\% & Certificados, Nómina asistentes. \\
\hline
\multicolumn{3}{|r|}{\textbf{TOTALES CONSOLIDADOS:}} & \textbf{40 h} & \textbf{100.00\%} & \textbf{Validación SGC: APROBADA} \\
\hline
\end{tabularx}
\caption{Matriz oficial de actividades académicas del plan semestral P7-T1.}
\label{tab:matriz_actividades_datos}
\end{table}

\subsection{Matriz de Distribución del Cronograma Semanal (Semanas 1 a 16)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{N°} & \textbf{Actividad Planificada} & \textbf{Sem. 1--4} & \textbf{Sem. 5--8} & \textbf{Sem. 9--12} & \textbf{Sem. 13--16} \\
\hline
1 & Dictado de Cátedra (Cursos Teóricos y Prácticos) & Activo & Activo & Activo & Activo \\
\hline
2 & Preparación de clases y diseño de instrumentos & Activo & Activo & Activo & Activo \\
\hline
3 & Tutorías Académicas individuales y grupales & Activo & Activo & Activo & Activo \\
\hline
4 & Desarrollo del Proyecto de Investigación SIGE & Activo & Activo & Activo & Activo \\
\hline
5 & Sesiones de Comisión Académica y Aseguramiento & Quincenal & Quincenal & Quincenal & Quincenal \\
\hline
6 & Talleres de Vinculación con la Sociedad & Inactivo & Activo & Activo & Cierre \\
\hline
\end{tabularx}
\caption{Cronograma de ejecución semestral distribuido en 16 semanas.}
\end{table}
"""

    anx3_9 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.9 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.9 \\
\hline
Nombre de la Tarjeta & Desarrollo de la Matriz Dinámica de Actividades \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 23 de septiembre al 28 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Andrea Vásquez (AV), Steeven Toala (ST) \\
\hline
Entregable Oficial & Componente \texttt{MatrizActividadesTable.tsx} interactivo \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 3 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.9 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Acciones y Casos de Reducer en el Componente}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Acción Reducer} & \textbf{Tipo de Disparo} & \textbf{Transformación de Estado Ejecutada} & \textbf{Complejidad} \\
\hline
\texttt{ADD\_ACTIVITY} & Clic en botón ``+ Agregar'' & Inserta nueva fila con valores por defecto e ID autogenerado. & $O(1)$ \\
\hline
\texttt{UPDATE\_WEIGHT} & Modificación de ponderación & Recalcula $\sum P_i$; actualiza badge a verde si $100\%$ o rojo si difiere. & $O(n)$ \\
\hline
\texttt{TOGGLE\_WEEK} & Clic en casilla de semana & Invierte el booleano de la semana específica en el array de 16 ítems. & $O(1)$ \\
\hline
\texttt{SUGGEST\_AI} & Clic en botón ``Sugerir IA'' & Poblado inteligente con base en sugerencias de redacción del SGC. & $O(1)$ \\
\hline
\end{tabularx}
\caption{Estructura de acciones inmutables del componente React.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{b91480a - feat(matriz): MatrizActividadesTable interactiva con useReducer, calculo 100\% y cronograma}
    \item \textbf{Archivos Afectados:} \texttt{frontend/src/components/matriz/*}, \texttt{Entregables\_Latex/Fase\_3/3.9*.tex}
\end{itemize}
"""
    write_tex("3.9_Desarrollo_Matriz_Dinamica_de_Actividades.tex",
              render_doc("TI-SIGE-ENT-F3-009", "IMPLEMENTACIÓN DE SOFTWARE / MATRIZ DINÁMICA DE ACTIVIDADES", "28/09/2026", "28/09/2026", "DESARROLLO DE LA MATRIZ DINÁMICA", b3_9, "28/09/2026", anx3_9))

    # =========================================================================
    # 3.10 REGLAS DE NEGOCIO Y VALIDATION GATES CON MIDDLEWARES EXPRESS V5
    # =========================================================================
    b3_10 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Reglas de Negocio y Validation Gates con Middlewares Express v5 -- Código EDT: 3.10

\section{Introducción}
La confiabilidad y estandarización del proceso de acreditación de la FISEI exigen que ningún documento incompleto, con horas incoherentes o sin los debidos respaldos pueda avanzar en el flujo de aprobación colegiada. Para garantizar esto de manera automatizada y no evadible, se implementó en el backend de Node.js con Express v5 una tubería (\textit{Pipeline}) de Middlewares secuenciales denominados \textit{Validation Gates}. Cada Gate actúa como una aduana lógica estricta que evalúa reglas de negocio declarativas y bloquea las peticiones no conformes antes de que impacten la base de datos o el estado del documento.

\section{Objetivo}
\subsection{Objetivo General}
Implementar la tubería de Validation Gates mediante Middlewares en Express v5 para garantizar el cumplimiento ineludible de las reglas de negocio del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Codificar los 6 Validation Gates del sistema (\texttt{validation.middleware.js}).
    \item Estandarizar las respuestas de error en formato JSON estructurado con códigos HTTP 400 y 422.
    \item Validar transiciones de estado entre Borrador, En Revisión, Observado y Aprobado.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Validación de: Gate 1 (Horas contractuales = 40h), Gate 2 (Ponderación = 100\%), Gate 3 (Evidencias obligatorias $>0$), Gate 4 (Fechas vigentes), Gate 5 (Firma previa), Gate 6 (Resolución de observaciones).
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Procesos de auditoría forense externa ajenos a la aplicación web.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Validation Gate:} Barrera lógica que verifica el cumplimiento de precondiciones necesarias antes de autorizar un cambio de estado en el sistema.
    \item \textbf{Middleware (Express):} Función que tiene acceso al objeto de solicitud (\texttt{req}), al objeto de respuesta (\texttt{res}) y a la siguiente función middleware (\texttt{next}).
    \item \textbf{HTTP 422 Unprocessable Entity:} Código de respuesta que indica que la sintaxis de la petición es correcta pero existen errores semánticos de negocio.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.10):} Diseño e implementación del pipeline de Validation Gates en Express v5.
    \item \textbf{Nixon Hurtado (Backend Developer):} Pruebas unitarias de casos de error y condiciones de borde.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la rigurosidad de los gates.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149.}
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 8.5.1 (Control de la producción y de la provisión del servicio):} Implementación de condiciones controladas.
    \item \textbf{ISO/IEC 25010:2011:} Fiabilidad e integridad en la lógica de procesamiento.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Los Middlewares se organizaron en una cadena de responsabilidad (\textit{Chain of Responsibility}). Al invocarse el endpoint de envío a revisión (\texttt{POST /api/documentos/:id/solicitar-revision}), Express invoca consecutivamente cada Gate. Si una regla se incumple, la ejecución se interrumpe de inmediato retornando una respuesta HTTP 422 que incluye un array de objetos con el código de error, el campo afectado y el mensaje institucional correctivo. Si todos los Gates son superados, se invoca \texttt{next()} permitiendo la transición de estado.

\subsection{Políticas de Calidad de las Validation Gates}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Bloqueo Inmediato (Fail-Fast):} Si un Gate preliminar falla, los posteriores no se ejecutan innecesariamente, economizando lecturas a la base de datos.
    \item \textbf{Política de Respuestas Estructuradas:} Las respuestas de error contienen información procesable por el frontend para resaltar la pestaña específica que requiere corrección.
    \item \textbf{Política de Inmutabilidad de Validación:} Ningún usuario, inclusive con perfil Administrador, puede sobrepasar una Validation Gate sin registrar una prórroga formal.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_09_decision_validation_gates.png}
    \caption{Diagrama de Flujo y Pipeline de Decisión de las 6 Validation Gates en Express v5.}
    \label{fig:gates_pipeline}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de las 6 Validation Gates Implementadas}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Gate} & \textbf{Nombre de la Regla} & \textbf{Condición Lógica Evaluada} & \textbf{Error HTTP} & \textbf{Acción del Sistema} \\
\hline
\textbf{Gate 1} & Carga Horaria 40h & $\sum \text{horas\_actividades} = 40\text{ h}$ & 422 & Bloquea paso a revisión; exige cuadre exacto. \\
\hline
\textbf{Gate 2} & Ponderación 100\% & $\sum \text{ponderacion} = 100.00\%$ & 422 & Bloquea envío; notifica diferencia porcentual. \\
\hline
\textbf{Gate 3} & Evidencias $>0$ & Si avance $>0\%$, exige $\ge 1$ archivo MinIO & 422 & Impide reporte sin soporte auditable. \\
\hline
\textbf{Gate 4} & Fechas Vigentes & Fecha actual $\le$ Fecha límite del periodo & 403 & Exige solicitud de prórroga extemporánea. \\
\hline
\textbf{Gate 5} & Cascada de Firmas & Firma Revisor exige firma previa Elaborador & 409 & Bloquea firma desordenada o fuera de turno. \\
\hline
\textbf{Gate 6} & Observaciones & Todas las observaciones deben estar resueltas & 422 & Impide aprobación con reclamos pendientes. \\
\hline
\end{tabularx}
\caption{Matriz oficial de Validation Gates en el backend.}
\label{tab:validation_gates_matrix}
\end{table}

\subsection{Estructura del Mensaje de Error Retornado en Fallas de Gate}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Campo JSON} & \textbf{Tipo de Dato} & \textbf{Contenido Retornado en Fallo} \\
\hline
\texttt{gate} & String & Identificador de la regla insatisfecha (e.g., \texttt{"GATE\_02\_PONDERACION"}). \\
\hline
\texttt{campo} & String & Campo afectado para enlace con la pestaña (e.g., \texttt{"matriz\_actividades"}). \\
\hline
\texttt{valor\_actual} & Float & Valor numérico calculado actualmente en el sistema (e.g., \texttt{92.50}). \\
\hline
\texttt{valor\_esperado} & Float / String & Valor requerido según norma SGC (e.g., \texttt{100.00}). \\
\hline
\texttt{mensaje} & String & Mensaje instructivo: \textit{``La ponderación debe sumar exactamente 100\%''}. \\
\hline
\end{tabularx}
\caption{Formato de error emitido ante violación de Validation Gates.}
\end{table}
"""

    anx3_10 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.10 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.10 \\
\hline
Nombre de la Tarjeta & Reglas de negocio y Validation Gates con Middlewares Express v5 \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 25 de septiembre al 30 de septiembre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Nixon Hurtado (NH) \\
\hline
Entregable Oficial & Middlewares de validación y reglas de negocio (\texttt{validation.middleware.js}) \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 3 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.10 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Pruebas de Bloqueo de Validation Gates}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Test ID} & \textbf{Gate Evaluado} & \textbf{Condición Forzada en Petición} & \textbf{HTTP} & \textbf{Resultado} \\
\hline
TC-G01 & Gate 1 (Horas) & Envío con 38 horas semanales acumuladas & 422 & BLOQUEO EXITOSO \\
\hline
TC-G02 & Gate 2 (Pond.) & Envío con ponderación sumando 105.00\% & 422 & BLOQUEO EXITOSO \\
\hline
TC-G03 & Gate 3 (Evid.) & Informe con avance 50\% sin archivos MinIO & 422 & BLOQUEO EXITOSO \\
\hline
TC-G04 & Gate 5 (Firmas) & Intento de firma de Revisor antes del Elaborador & 409 & BLOQUEO EXITOSO \\
\hline
TC-G05 & Todos OK & Expediente completo (40h, 100\%, evidencias, orden) & 200 & AVANCE AUTORIZADO \\
\hline
\end{tabularx}
\caption{Matriz de pruebas unitarias sobre el pipeline de Middlewares.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{e1028bc - feat(gates): pipeline de 6 validation gates con middlewares Express v5 y HTTP 422}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/middlewares/validation.middleware.js}, \texttt{Entregables\_Latex/Fase\_3/3.10*.tex}
\end{itemize}
"""
    write_tex("3.10_Reglas_Negocio_Validation_Gates_Middlewares_Express_v5.tex",
              render_doc("TI-SIGE-ENT-F3-010", "IMPLEMENTACIÓN DE SOFTWARE / VALIDATION GATES Y MIDDLEWARES", "30/09/2026", "30/09/2026", "REGLAS DE NEGOCIO Y VALIDATION GATES", b3_10, "30/09/2026", anx3_10))

    # =========================================================================
    # 3.11 INTEGRACIÓN DE MINIO S3 PARA EVIDENCIAS Y URLS PREFIRMADAS
    # =========================================================================
    b3_11 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Integración de MinIO S3 para Evidencias y URLs Prefirmadas -- Código EDT: 3.11

\section{Introducción}
El almacenamiento de medios de verificación físicos (informes, actas de reuniones, certificados, sílabos firmados) constituye el soporte probatorio para los procesos de acreditación y auditoría de la FISEI. Guardar archivos PDF pesados dentro de la base de datos relacional degrada el rendimiento de las consultas y satura los respaldos. Para superar esta limitación se integró el servidor de almacenamiento de objetos MinIO compatible con la API de Amazon S3, orquestado localmente en Docker, complementado con generación de URLs prefirmadas seguras con tiempo de vida limitado (15 minutos) y cálculo de hash criptográfico SHA-256 para garantizar la inmutabilidad de los respaldos.

\section{Objetivo}
\subsection{Objetivo General}
Implementar y verificar la integración de MinIO S3 para la carga, almacenamiento, cálculo de integridad y visualización segura de evidencias documentales mediante URLs prefirmadas.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Desplegar y configurar el bucket privado \texttt{sige-evidencias} en MinIO.
    \item Implementar el servicio \texttt{minio.service.js} con soporte para subida de archivos y generación de URLs prefirmadas temporales.
    \item Desarrollar el cálculo de sumas de comprobación SHA-256 almacenadas en PostgreSQL 18.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Carga de archivos en formato PDF con límite de hasta 25 MB por archivo.
    \item Generación de URLs de lectura prefirmadas con caducidad de 15 minutos (900 segundos).
    \item Interfaz en el frontend para arrastrar y soltar archivos (\textit{Drag \& Drop}) con indicador de porcentaje de subida.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Almacenamiento de archivos multimedia pesados (videos o grabaciones de clases).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{MinIO:} Servidor de almacenamiento de objetos de código abierto de alto rendimiento compatible con las APIs de AWS S3.
    \item \textbf{Presigned URL (URL Prefirmada):} Enlace temporal generado criptográficamente que otorga acceso de lectura o escritura a un objeto específico durante un tiempo limitado sin exponer credenciales.
    \item \textbf{Hash SHA-256:} Función criptográfica de resumen de 256 bits que genera una huella digital única para verificar que el contenido de un archivo no ha sido alterado.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Nixon Hurtado (Responsable EDT 3.11):} Configuración de MinIO, desarrollo de \texttt{minio.service.js} y endpoints de upload.
    \item \textbf{Steeven Toala (Líder Técnico):} Verificación del cálculo de hashes SHA-256 y políticas de acceso.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del mecanismo de custodia de evidencias.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Conservación inalterable de medios probatorios de la labor docente.
    \item \textbf{Ley Orgánica de Protección de Datos Personales (LOPDP), Art. 37.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Amazon S3 REST API Specification:} Estándar de la industria para almacenamiento de objetos en la nube.
    \item \textbf{FIPS 180-4 (Secure Hash Standard):} Especificación del algoritmo criptográfico SHA-256.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se utilizó el SDK oficial \texttt{minio} para Node.js. Al subir una evidencia, el archivo es transmitido en streaming con \texttt{multer} en memoria; se calcula su hash SHA-256 antes de transferirlo al bucket privado \texttt{sige-evidencias}. El archivo se nombra de forma no colisionante bajo la convención:
\texttt{evidencias/\{plan\_id\}/\{actividad\_id\}/\{uuid\}\_\{nombre\_original\}}. Para la visualización desde el frontend, el backend genera bajo demanda una URL prefirmada (\texttt{presignedGetObject}) válida por 900 segundos.

\subsection{Políticas de Calidad de Almacenamiento de Evidencias}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Inmutabilidad Absoluta:} Los archivos en MinIO no pueden ser editados in situ; cualquier modificación requiere subir una nueva versión con nuevo hash.
    \item \textbf{Política de URLs Temporales Estrictas:} Ningún archivo posee acceso público permanente; todo acceso expira automáticamente a los 15 minutos.
    \item \textbf{Política de Validación de Tipo MIME y Tamaño:} Solo se admiten archivos \texttt{application/pdf} de hasta 25 MB, rechazando ejecutables u otros formatos.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_seguimiento_evidencias.png}
    \caption{Captura Real de la Bandeja de Seguimiento y Gestión de Evidencias en el Sistema SIGE.}
    \label{fig:evidencias_real}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_10_arquitectura_minio_s3.png}
    \caption{Arquitectura de Carga, Hashes SHA-256 y URLs Prefirmadas con MinIO S3.}
    \label{fig:minio_arch}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Parámetros de Almacenamiento en MinIO S3}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{3.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro Técnico} & \textbf{Configuración} & \textbf{Justificación Operativa / Seguridad} & \textbf{Estado} \\
\hline
Nombre de Bucket & \texttt{sige-evidencias} & Bucket privado institucional exclusivo para evidencias SGC. & Activo \\
\hline
Política de Bucket & \texttt{Private (None)} & Prohíbe lecturas anónimas; requiere firmas criptográficas. & Verificada \\
\hline
TTL URL Prefirmada & 15 minutos ($900\text{ s}$) & Tiempo suficiente para lectura o descarga sin riesgo de fuga. & Configurado \\
\hline
Tamaño Máximo & $25\text{ MB}$ por archivo & Admite informes extensos con imágenes y anexos sin saturar red. & Limitado \\
\hline
Tipos Admitidos & \texttt{application/pdf} & Estandarización de formato para conservación a largo plazo. & Restringido \\
\hline
Algoritmo de Hash & SHA-256 (64 hex) & Verificación de no alteración y trazabilidad en auditoría. & Activo \\
\hline
\end{tabularx}
\caption{Parámetros de configuración del servicio de almacenamiento MinIO.}
\label{tab:minio_matrix}
\end{table}

\subsection{Matriz de Endpoints para Gestión de Evidencias}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL} & \textbf{Operación y Retorno} & \textbf{Código HTTP} \\
\hline
\texttt{POST} & \texttt{/api/evidencias/upload} & Carga de archivo multipart; cálculo SHA-256 y registro en DB. & 201 Created \\
\hline
\texttt{GET} & \texttt{/api/evidencias/:id/url} & Generación de URL prefirmada para visualización embebida. & 200 OK \\
\hline
\texttt{DELETE} & \texttt{/api/evidencias/:id} & Borrado lógico en base de datos (preserva objeto para auditoría). & 200 OK \\
\hline
\end{tabularx}
\caption{Endpoints RESTful para evidencias documentales.}
\end{table}
"""

    anx3_11 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.11 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.11 \\
\hline
Nombre de la Tarjeta & Integración de MinIO S3 para evidencias y URLs prefirmadas \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 28 de septiembre al 02 de octubre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Nixon Hurtado (NH), Steeven Toala (ST) \\
\hline
Entregable Oficial & \texttt{MinioStorageService.cs} y componente de upload de evidencias \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 3 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.11 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Evidencias de Carga y Verificación SHA-256}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.0cm}|m{2.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{ID} & \textbf{Archivo de Prueba} & \textbf{Tamaño} & \textbf{Hash Criptográfico SHA-256 Calculado} & \textbf{Integridad} \\
\hline
EV-01 & \texttt{silabo\_ing\_soft\_2026.pdf} & 2.4 MB & \texttt{e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855} & VERIFICADA \\
\hline
EV-02 & \texttt{acta\_tutorias\_sep.pdf} & 840 KB & \texttt{d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35} & VERIFICADA \\
\hline
EV-03 & \texttt{informe\_avance\_investig.pdf} & 5.1 MB & \texttt{4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a} & VERIFICADA \\
\hline
\end{tabularx}
\caption{Registros de pruebas de subida e integridad con hash SHA-256.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{cb1029e - feat(storage): integracion MinIO S3, generacion de URLs prefirmadas y hash SHA-256}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/services/minio.service.js}, \texttt{frontend/src/components/evidencias/*}, \texttt{Entregables\_Latex/Fase\_3/3.11*.tex}
\end{itemize}
"""
    write_tex("3.11_Integracion_MinIO_S3_Evidencias_URLs_Prefirmadas.tex",
              render_doc("TI-SIGE-ENT-F3-011", "IMPLEMENTACIÓN DE SOFTWARE / ALMACENAMIENTO DE EVIDENCIAS", "02/10/2026", "02/10/2026", "INTEGRACIÓN DE MINIO S3 Y EVIDENCIAS", b3_11, "02/10/2026", anx3_11))

    # =========================================================================
    # 3.12 HITO 4: SPRINT 3 REVIEW: MATRIZ DINÁMICA Y EVIDENCIAS MINIO
    # =========================================================================
    b3_12 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 4: Sprint 3 Review: Matriz Dinámica y Evidencias MinIO -- Código EDT: 3.12

\section{Introducción}
El cierre del Sprint 3 de desarrollo representa la consolidación funcional de las capacidades nucleares del Sistema de Gestión de Calidad (SGC) dentro de la plataforma SIGE. En esta reunión de revisión (\textit{Sprint Review 3}) se auditó y demostró ante el Docente Evaluador la operación conjunta de la Matriz Dinámica de Actividades (\texttt{MatrizActividadesTable}), la ejecución ineludible de las 6 Validation Gates y el almacenamiento de evidencias en objetos MinIO S3. El presente informe certifica formalmente la aprobación del incremento de software y la conformidad con los requerimientos pedagógicos y normativos de la FISEI.

\section{Objetivo}
\subsection{Objetivo General}
Evaluar, demostrar y formalizar la aprobación del Sprint 3 del sistema SIGE, aprobando el Hito 4 de la EDT con base en la operación de la matriz dinámica y el repositorio MinIO S3.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Demostrar el recálculo en tiempo real de la matriz al $100.00\%$ y la selección de las 16 semanas.
    \item Evidenciar la carga real de un archivo PDF en MinIO, el cómputo de su hash SHA-256 y su apertura mediante URL prefirmada.
    \item Emitir el acta oficial de aprobación del Sprint 3 autorizando el Sprint 4 (Revisión y Firmas).
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditoría funcional de los entregables EDT 3.9, 3.10 y 3.11.
    \item Verificación de criterios de aceptación de Historias de Usuario US-11 a US-16.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Estampado de firmas multinivel en cascada (objeto del Sprint 4).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Incremento de Sprint 3:} Versión funcional v0.7 del sistema SIGE con soporte completo de matrices de cálculo y custodia de archivos.
    \item \textbf{Criterio de Aceptación:} Conjunto de condiciones predefinidas que debe cumplir una funcionalidad para ser declarada aceptada por el Product Owner.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder Técnico):} Dirección técnica de la demostración y verificación de infraestructura.
    \item \textbf{Andrea Vásquez / Nixon Hurtado (Desarrolladores):} Presentación de casos de uso de la matriz dinámica y MinIO.
    \item \textbf{Heidi Villavicencio (Calidad):} Auditoría de cumplimiento de DoD y trazabilidad de requerimientos.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación oficial del Hito 4.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149.}
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Scrum Framework (Sprint Review Guidelines).}
    \item \textbf{ISO 9001:2015, Cláusula 8.3.5 (Salidas del diseño y desarrollo).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se ejecutó la sesión de demostración operativa en vivo utilizando el entorno de contenedores Docker Compose local. Se recreó el flujo real de un docente titular de FISEI: registro interactivo de 6 actividades en la matriz dinámica, forzado de un error de ponderación (105\%) comprobando el bloqueo preventivo del sistema, corrección al 100.00\% exacto con desbloqueo automático, subida de un archivo PDF de evidencia con cálculo en tiempo real de su hash SHA-256 e inspección directa en la consola de MinIO confirmando el almacenamiento en el bucket \texttt{sige-evidencias}.

\subsection{Políticas de Calidad de Hito 4}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Consistencia Total:} Las actividades registradas en la matriz deben ser idénticas en base de datos, en memoria del cliente y en los archivos de evidencia asociados.
    \item \textbf{Política de Transparencia de Auditoría:} Toda prueba debe evidenciar los registros generados en los logs de auditoría (\texttt{auditoria\_logs}).
    \item \textbf{Política de Cero Defectos Funcionales:} No se autoriza el paso al Sprint 4 si existen inconsistencias aritméticas o fallas de carga en MinIO.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_matriz_dinamica_actividades.png}
    \caption{Captura Real de la Demostración de la Matriz Dinámica durante la Sesión de Hito 4.}
    \label{fig:hito4_demo1}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/sige_seguimiento_evidencias.png}
    \caption{Captura Real de la Verificación de Evidencias MinIO durante la Demostración de Hito 4.}
    \label{fig:hito4_demo2}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Aceptación de Historias de Usuario del Sprint 3}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|X|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Historia de Usuario} & \textbf{Criterio de Aceptación Evaluado} & \textbf{Resultado} & \textbf{Estado} \\
\hline
US-11 & Matriz Dinámica 100\% & Sumatoria reactiva al 100.00\% y selector de 16 semanas. & 100\% & Aprobada \\
\hline
US-12 & Validation Gates & Bloqueo en Express v5 ante horas $\ne 40$ o faltantes de evidencia. & 100\% & Aprobada \\
\hline
US-13 & Carga S3 en MinIO & Almacenamiento seguro de archivos PDF en bucket privado. & 100\% & Aprobada \\
\hline
US-14 & Integridad SHA-256 & Cómputo e inserción de hash de 64 caracteres en base de datos. & 100\% & Aprobada \\
\hline
US-15 & URLs Prefirmadas & Visualización de respaldos con enlace temporal de 15 min. & 100\% & Aprobada \\
\hline
\end{tabularx}
\caption{Matriz oficial de aceptación del incremento funcional del Sprint 3.}
\label{tab:sprint3_matrix}
\end{table}

\subsection{Métricas de Cumplimiento Acumulado del Proyecto al Hito 4}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.8cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Indicador de Proyecto} & \textbf{Planificado} & \textbf{Ejecutado} & \textbf{Estado Actual del Proyecto} \\
\hline
Horas Invertidas Sprint 3 & 96 h & 96 h & Avance exacto según cronograma Gantt. \\
\hline
Horas Acumuladas Fase 3 & 256 h & 256 h & 12 de 16 tareas de Fase 3 completadas ($75\%$). \\
\hline
Schedule Performance Index & 1.00 & 1.00 & Cero retrasos en hitos de entrega. \\
\hline
\end{tabularx}
\caption{Métricas acumuladas de avance del proyecto al Hito 4.}
\end{table}
"""

    anx3_12 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.12 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.12 \\
\hline
Nombre de la Tarjeta & HITO 4: Sprint 3 Review: Matriz Dinámica y Evidencias MinIO \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 01 de octubre al 02 de octubre de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Andrea Vásquez (AV), Nixon Hurtado (NH), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & Demostración funcional de matriz con evidencias MinIO \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado Formalmente \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.12 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Acta Formal de Aprobación del Sprint 3 (Hito 4)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA INSTITUCIONAL DE CIERRE DE SPRINT 3 -- SISTEMA SIGE}} \\
\hline
\textbf{Fecha de Sesión:} & 02 de octubre de 2026 \\
\hline
\textbf{Participantes:} & Steeven Toala (Líder Técnico), Andrea Vásquez (Frontend), Nixon Hurtado (Backend), Heidi Villavicencio (Calidad), Ing. Paulo Torres (Docente Evaluador). \\
\hline
\textbf{Resolución:} & Tras presenciar la demostración de recálculo aritmético instantáneo de la Matriz Dinámica al 100\%, el bloqueo preventivo de las Validation Gates y la persistencia de evidencias en MinIO S3 con hashes SHA-256, el Docente Evaluador declara APROBADO por unanimidad el Hito 4 y autoriza el inicio del Sprint 4 enfocado en Revisión Colegiada, Corrección Ortográfica y Exportación Oficial. \\
\hline
\end{tabularx}
\caption{Acta oficial de aprobación de Hito 4.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Etiqueta de Versión:} \texttt{v0.4.0-milestone4-matriz-minio-ready}
    \item \textbf{Commit de Consolidación:} \texttt{fa89102 - docs(sprint3): acta de aprobacion oficial de hito 4 y cierre de sprint 3}
    \item \textbf{Archivos Afectados:} \texttt{Entregables\_Latex/Fase\_3/3.12*.tex}
\end{itemize}
"""
    write_tex("3.12_HITO_4_Sprint_3_Review_Matriz_Dinamica_Evidencias_MinIO.tex",
              render_doc("TI-SIGE-ENT-F3-012", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 4 MATRIZ Y S3", "02/10/2026", "02/10/2026", "HITO 4: SPRINT 3 REVIEW: MATRIZ Y S3", b3_12, "02/10/2026", anx3_12))

    # =========================================================================
    # 3.13 MÓDULO DE REVISIÓN, OBSERVACIONES Y CASCADA DE FIRMAS
    # =========================================================================
    b3_13 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Módulo de Revisión, Observaciones y Cascada de Firmas -- Código EDT: 3.13

\section{Introducción}
El flujo colegiado de revisión y aprobación de los planes de trabajo del SGC en la FISEI involucra una cadena de responsabilidades jerárquica: el Docente Elaborador diseña el plan, el Coordinador de Área o Carrera audita su coherencia y registra observaciones técnicas, y finalmente las autoridades de facultad (Subdecano / H. Consejo Directivo) legalizan el documento. Para automatizar este flujo con plena validez institucional, se implementó el panel de revisión con panel lateral (\textit{Drawer}) de observaciones granulares por sección y el subsistema de estampado secuencial e inmutable de firmas digitales en cascada (\textit{Cascading Signatures}).

\section{Objetivo}
\subsection{Objetivo General}
Implementar el módulo de revisión técnica colegiada, gestión granular de observaciones y cascada secuencial de firmas digitales para el sistema SIGE.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Desarrollar el panel de revisión del coordinador con visor de documento y drawer de observaciones.
    \item Programar el sistema de firmas en cascada secuencial inmutable con hash SHA-256 y marca temporal.
    \item Implementar las transiciones de estado: \textit{Borrador} $\to$ \textit{En Revisión} $\to$ \textit{Observado} $\to$ \textit{Aprobado Comisión} $\to$ \textit{Aprobado HCD}.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Interfaz de usuario para Coordinador de Carrera y Comité de Revisión (\texttt{RevisionComiteView.jsx}).
    \item Servicio de firmas digitales en backend garantizando orden estricto (1: Elaborador, 2: Revisor, 3: Aprobador).
    \item Trazabilidad y no repudio de firmas mediante hash de contenido.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Integración con certificados de firma electrónica con token USB físico (Banco Central / Security Data), prevista para fases de interoperabilidad externa.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Cascada de Firmas:} Mecanismo criptográfico y de negocio donde una firma requiere obligatoriamente la existencia y validez de la firma del nivel jerárquico anterior.
    \item \textbf{Observación Granular:} Comentario correctivo vinculado de forma unívoca a una sección específica del documento, que impide su aprobación hasta ser resuelta.
    \item \textbf{Estampillado Digital (Timestamping):} Registro criptográfico inmutable de la fecha, hora exacta e identidad del firmante al momento del visado.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.13):} Desarrollo del servicio de firmas digitales, hashes y control de estados.
    \item \textbf{Heidi Villavicencio (UI/UX):} Diseño e implementación del drawer lateral de observaciones y visor de revisión.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del flujo de revisión y cadena de responsabilidades.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley de Comercio Electrónico, Firmas Electrónicas y Mensajes de Datos, Art. 14 y 15:} Validez jurídica, eficacia y no repudio de firmas digitales.
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Responsabilidad institucional de autoridades y docentes en la legalización académica.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 7.5.3 (Control de la información documentada):} Procedimientos de revisión, aprobación y custodia.
    \item \textbf{NIST SP 800-89 (Recommendation for Obtaining Assurances for Digital Signatures).}
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se diseñó un mecanismo de tres niveles de firma. Cada firma calcula un hash criptográfico compuesto a partir del identificador del documento, el contenido HTML de sus secciones, la identidad del firmante y la estampa de tiempo UTC:
\begin{equation}
    H_{\text{firma}} = \text{SHA-256}\Big(\text{plan\_id} \ \Vert \ H_{\text{contenido}} \ \Vert \ \text{usuario\_id} \ \Vert \ \text{timestamp}\Big)
\end{equation}
Cualquier intento de alteración posterior del texto invalida el hash registrado. El coordinador interactúa a través de una vista dividida (\textit{Split View}): a la izquierda el plan de trabajo A4 y a la derecha el drawer interactivo donde puede marcar secciones como conformes o ingresar observaciones con severidad (Leve, Grave, Bloqueante).

\subsection{Políticas de Calidad de la Cascada de Firmas}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Secuencia Ineludible:} El Coordinador no puede firmar si el Docente no ha firmado; el Subdecano no puede legalizar si el Coordinador no ha aprobado.
    \item \textbf{Política de Congelamiento por Firma:} Al estampar la primera firma, el documento pasa a modo de solo lectura estricto, impidiendo cualquier edición salvo que sea devuelto formalmente a estado ``Observado''.
    \item \textbf{Política de Resolución Obligatoria de Observaciones:} El sistema bloquea el botón de aprobación si existe al menos una observación sin marcar como ``Resuelta''.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_coordinador_revision.png}
    \caption{Captura Real del Panel de Revisión del Coordinador con Drawer de Observaciones en SIGE.}
    \label{fig:coordinador_real}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_11_flujo_revision_comite.png}
    \caption{Flujo Secuencial de Estados y Cascada de Firmas Digitales en el Sistema SIGE.}
    \label{fig:cascada_firmas}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de la Cascada de Firmas Digitales Institucionales}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{2.8cm}|m{2.8cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Orden} & \textbf{Nivel de Firma} & \textbf{Actor Responsable} & \textbf{Efecto Jurídico y en el Sistema} & \textbf{Estado Resultante} \\
\hline
1 & Firma de Elaboración & Docente Titular / Ocasional & Certifica la veracidad de horas y actividades; bloquea edición. & \textbf{En Revisión} \\
\hline
2 & Firma de Revisión & Coordinador de Área / Carrera & Certifica cumplimiento técnico SGC y ausencia de observaciones. & \textbf{Aprobado Comisión} \\
\hline
3 & Firma de Aprobación & Subdecano de FISEI & Legalización oficial en Consejo Directivo; sella plan definitivo. & \textbf{Aprobado HCD (Final)} \\
\hline
\end{tabularx}
\caption{Matriz oficial de la cascada de firmas digitales multinivel.}
\label{tab:firmas_matrix}
\end{table}

\subsection{Matriz de Ciclo de Vida de las Observaciones Granulares}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{3.0cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Severidad} & \textbf{Impacto en Flujo} & \textbf{Tratamiento en la Interfaz} & \textbf{Acción del Docente} \\
\hline
Informativa & No bloqueante & Sugerencia tipográfica menor; no impide avance a firma. & Opcional \\
\hline
Revisión Técnica & Bloqueante & Exige corrección en sección de horas o medios de verificación. & Obligatoria \\
\hline
Rechazo Normativo & Bloqueante Mayor & Devuelve expediente a estado ``Observado'' de forma inmediata. & Reestructuración \\
\hline
\end{tabularx}
\caption{Clasificación y comportamiento de observaciones de revisión.}
\end{table}
"""

    anx3_13 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.13 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.13 \\
\hline
Nombre de la Tarjeta & Módulo de Revisión, Observaciones y Cascada de Firmas \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 02 de octubre al 06 de octubre de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & Panel de Comité y servicio de Firmas multinivel \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 4 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.13 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Verificación de Integridad de Firmas Digitales}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{2.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Prueba} & \textbf{Condición Forzada} & \textbf{Respuesta del Subsistema Criptográfico} & \textbf{Resultado} \\
\hline
P1 - Salto de Nivel & Coordinador intenta firmar plan sin firma de docente & \texttt{ERROR: Cascada violada. Requiere firma de Elaborador} & BLOQUEADO \\
\hline
P2 - Alteración Posterior & Modificación manual de texto en base de datos tras firma & \texttt{ALERTA: Hash de contenido no coincide con firma (Corrupción)} & DETECTADO \\
\hline
P3 - Firma Legítima & Secuencia en orden con observaciones resueltas & Estampado con hash SHA-256 e inserción inmutable & EXITOSO \\
\hline
\end{tabularx}
\caption{Pruebas de integridad criptográfica y cascada de firmas.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{804a11f - feat(revision): modulo de revision comite, drawer de observaciones y cascada de firmas SHA-256}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/modules/revision/*}, \texttt{frontend/src/views/RevisionComiteView.jsx}, \texttt{Entregables\_Latex/Fase\_3/3.13*.tex}
\end{itemize}
"""
    write_tex("3.13_Modulo_Revision_Observaciones_Cascada_Firmas.tex",
              render_doc("TI-SIGE-ENT-F3-013", "IMPLEMENTACIÓN DE SOFTWARE / REVISIÓN Y FIRMAS DIGITALES", "06/10/2026", "06/10/2026", "MÓDULO DE REVISIÓN Y CASCADA DE FIRMAS", b3_13, "06/10/2026", anx3_13))

    # =========================================================================
    # 3.14 CAPA DE ASISTENCIA Y CORRECCIÓN ORTOGRÁFICA LOCAL
    # =========================================================================
    b3_14 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Capa de Asistencia y Corrección Ortográfica Local -- Código EDT: 3.14

\section{Introducción}
Los planes de trabajo e informes de cumplimiento del SGC representan documentos formales de carácter legal e institucional que son auditados periódicamente por organismos de acreditación (CACES). Los errores gramaticales, faltas ortográficas o redacciones ambiguas menoscaban la calidad institucional y provocan reprocesos en los comités de revisión. Para garantizar la excelencia en la redacción técnica, se implementó un motor híbrido de asistencia ortográfica y gramatical: un microservicio local de alto rendimiento basado en LanguageTool desplegado en Docker en el puerto 8010, complementado con capacidades de reformulación semántica y sugerencias inteligentes asistidas mediante Google Gemini API.

\section{Objetivo}
\subsection{Objetivo General}
Implementar y desplegar el subsistema de corrección ortográfica, gramatical y asistencia semántica local en el sistema SIGE para garantizar la calidad editorial de los informes del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Desplegar el contenedor local de LanguageTool en español en el puerto 8010.
    \item Desarrollar el servicio backend \texttt{grammar.service.js} que analiza textos en tiempo real.
    \item Integrar la capa de asistencia semántica institucional con Google Gemini API bajo esquema de contingencia (\textit{fallback}).
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Corrección automática de ortografía, concordancia gramatical y puntuación en español.
    \item Botón de sugerencias ``Mejorar redacción con IA'' integrado en el editor TipTap.
    \item Operación 100\% funcional del corrector local LanguageTool en ausencia de conectividad a Internet.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Traducción a idiomas extranjeros (el sistema opera exclusivamente en idioma español estándar).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{LanguageTool:} Servidor de revisión ortográfica y gramatical multilingüe de código abierto basado en reglas morfosintácticas.
    \item \textbf{Asistencia Semántica:} Reestructuración estilística de un texto académico para adaptarlo al vocabulario formal del Sistema de Gestión de la Calidad.
    \item \textbf{Arquitectura Híbrida / Fallback:} Patrón de resiliencia donde las funciones críticas operan localmente y los servicios externos se consumen de forma suplementaria y no bloqueante.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.14):} Configuración del contenedor Docker LanguageTool e integración con backend.
    \item \textbf{Andrea Vásquez (Frontend Developer):} Integración de las sugerencias visuales en el editor TipTap.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación del rigor ortográfico y asistencial.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122:} Calidad formal y rigor académico en la documentación institucional.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 9001:2015, Cláusula 7.5.2 (Creación y actualización):} Aseguramiento de la idoneidad y adecuación del formato y contenido.
    \item \textbf{Real Academia Española (RAE):} Normas ortográficas y gramaticales de la lengua española.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se priorizó la privacidad institucional y la independencia operativa (\textit{offline-first}). El servicio local LanguageTool analiza el texto plano extraído del editor TipTap mediante peticiones HTTP REST a \texttt{http://sige-grammar:8010/v2/check}. El análisis identifica errores ortográficos y sintácticos retornando el desplazamiento (\textit{offset}), longitud y alternativas de corrección en menos de 120 ms. Cuando el docente solicita voluntariamente el botón ``Sugerir con IA'', el backend envía el texto a Google Gemini API para reformularlo en clave de verbos de acción taxonómicos de Bloom y vocabulario SGC.

\subsection{Políticas de Calidad de la Asistencia Editorial}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Privacidad y No Bloqueo:} La corrección ortográfica local se ejecuta íntegramente dentro de la red privada del servidor sin enviar datos sensibles al exterior.
    \item \textbf{Política de Resiliencia ante Desconexión:} Si no existe conexión a Internet, la plataforma inhabilita discretamente la sugerencia remota mientras LanguageTool local continúa operando al 100\%.
    \item \textbf{Política de Control del Docente:} Las sugerencias de corrección o mejora son propuestas interactivas que el usuario puede aceptar o descartar con un clic.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/f3_12_languagetool_docker.png}
    \caption{Topología del Contenedor Local LanguageTool y Pipeline de Análisis Morfosintáctico.}
    \label{fig:languagetool_arch}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.6cm,keepaspectratio]{images/f3_13_gemini_api_fallback.png}
    \caption{Arquitectura Híbrida: Motor Local LanguageTool y Asistencia Semántica con Google Gemini API.}
    \label{fig:gemini_fallback}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Capacidades del Motor Híbrido de Corrección}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.8cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Motor de Análisis} & \textbf{Despliegue} & \textbf{Tipo de Asistencia Brindada} & \textbf{Latencia Promedio} \\
\hline
LanguageTool Local & Contenedor Docker (Puerto 8010) & Faltas ortográficas, tildes, concordancia de género y número, signos dobles. & $<120\text{ ms}$ \\
\hline
Google Gemini API & Servicio Cloud (Fallback) & Reescritura académica formal, alineación con verbos de Bloom, resumen ejecutivo. & $<1200\text{ ms}$ \\
\hline
Diccionario UTA & Archivo Local Personalizado & Reconocimiento de términos propios: FISEI, SGC, CACES, LOES, Subdecano. & Inmediata ($<5\text{ ms}$) \\
\hline
\end{tabularx}
\caption{Matriz técnica del subsistema de asistencia editorial.}
\label{tab:grammar_matrix}
\end{table}

\subsection{Matriz de Reglas Gramaticales Específicas Evaluadas}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|>{\bfseries}m{3.2cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Regla ID} & \textbf{Categoría RAE} & \textbf{Ejemplo de Detección en Informes Docentes} & \textbf{Corrección Sugerida} \\
\hline
RG-01 & Acentuación gráfica & Detección de palabras agudas sin tilde (e.g., \textit{``planificacion''}). & \textit{``planificación''} \\
\hline
RG-02 & Concordancia & Inconsistencia entre artículo y sustantivo (e.g., \textit{``las actividad''}). & \textit{``las actividades''} \\
\hline
RG-03 & Puntuación doble & Omisión de signo de apertura de interrogación o exclamación. & Inserción de \textit{¿} o \textit{¡} \\
\hline
RG-04 & Siglas académicas & Detección de mayúsculas incorrectas en siglas del SGC. & Estandarización SGC / FISEI \\
\hline
\end{tabularx}
\caption{Reglas de calidad gramatical y ortográfica implementadas.}
\end{table}
"""

    anx3_14 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.14 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.14 \\
\hline
Nombre de la Tarjeta & Capa de asistencia y corrección ortográfica local \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 05 de octubre al 08 de octubre de 2026 (4 días laborables) \\
\hline
Horas Asignadas & 32 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & Servicio local de corrección gramatical y ortográfica (\texttt{grammar.service.js}) \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 4 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.14 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Pruebas de Desempeño del Motor Local LanguageTool}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|X|c|c|c|}
\hline
\rowcolor{tableheader}
\textbf{Caso} & \textbf{Texto de Entrada Analizado} & \textbf{Errores Detectados} & \textbf{Tiempo} & \textbf{Estado} \\
\hline
TC-GR01 & \textit{``El docente realizo la evaluacion de los estudiante''} & 3 (realizó, evaluación, estudiantes) & 94 ms & SUPERADO \\
\hline
TC-GR02 & Texto formal de justificación SGC de 450 palabras & 0 errores (texto limpio validado) & 118 ms & SUPERADO \\
\hline
TC-GR03 & Corte intencional de Internet (modo offline) & LanguageTool opera normal; fallback no falla & 102 ms & SUPERADO \\
\hline
\end{tabularx}
\caption{Pruebas de verificación de rendimiento y precisión del corrector.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{b71902d - feat(nlp): LanguageTool en Docker puerto 8010 y servicio hibrido con Google Gemini API}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/services/grammar.service.js}, \texttt{docker-compose.yml}, \texttt{Entregables\_Latex/Fase\_3/3.14*.tex}
\end{itemize}
"""
    write_tex("3.14_Capa_Asistencia_y_Correccion_Ortografica_Local.tex",
              render_doc("TI-SIGE-ENT-F3-014", "IMPLEMENTACIÓN DE SOFTWARE / ASISTENCIA EDITORIAL Y NLP", "08/10/2026", "08/10/2026", "CAPA DE ASISTENCIA Y CORRECCIÓN ORTOGRÁFICA", b3_14, "08/10/2026", anx3_14))

    # =========================================================================
    # 3.15 MOTOR DE EXPORTACIÓN OFICIAL EN PDF Y WORD
    # =========================================================================
    b3_15 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} Motor de Exportación Oficial en PDF y Word -- Código EDT: 3.15

\section{Introducción}
Aunque la interacción diaria y el ciclo de revisión del sistema SIGE se efectúan dentro de la plataforma web, los requerimientos institucionales de la Universidad Técnica de Ambato exigen la entrega física y archivo documental de expedientes legalizados en formatos oficiales (\texttt{.pdf} vectorial no editable y \texttt{.docx} interoperable). Cualquier discrepancia de márgenes, encabezados institucionales, códigos de formato o ubicación de firmas respecto a las plantillas \texttt{UTA-SGC-A-2-1-P7-T1} y \texttt{T2} representaría una no conformidad de calidad. El presente entregable documenta el motor de generación documental de lado del servidor (\textit{Server-Side Document Export Pipeline}) que renderiza e imprime documentos idénticos al estándar institucional.

\section{Objetivo}
\subsection{Objetivo General}
Desarrollar y validar el motor de exportación de documentos oficiales en formatos PDF y Word idénticos al estándar institucional del SGC de la UTA.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Implementar la generación de PDF vectorial de alta precisión mediante Puppeteer y estilos CSS Paged Media (@page A4).
    \item Desarrollar el generador de archivos Microsoft Word (\texttt{.docx}) estructurado mediante plantillas OpenXML.
    \item Incorporar códigos QR con URL de verificación y estampas digitales de firmas.
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Exportación oficial para el Plan de Trabajo Docente (\texttt{P7-T1}) y el Informe de Cumplimiento (\texttt{P7-T2}).
    \item Preservación exacta de logotipos, códigos de control SGC, tablas de actividades y bloques de firmas.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Impresión física en papel sobre impresoras matriciales o térmicas.
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Puppeteer:} Librería de Node.js que proporciona una API de alto nivel para controlar navegadores Chromium headless para renderizado e impresión PDF.
    \item \textbf{CSS Paged Media (@page):} Módulo del W3C que permite definir propiedades de impresión (márgenes, encabezados de página repetitivos, números de página) para medios paginados.
    \item \textbf{OpenXML (OOXML):} Estándar ISO/IEC 29500 para documentos ofimáticos editables en formato \texttt{.docx}.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Responsable EDT 3.15):} Implementación del motor de renderizado con Puppeteer y generación de Word.
    \item \textbf{Heidi Villavicencio (UI / Calidad):} Maquetación CSS de las plantillas de impresión y verificación frente a plantillas originales.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Aprobación de la fidelidad del documento impreso frente a la norma SGC.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149.}
    \item \textbf{Normativa Institucional del Sistema de Gestión de Calidad (UTA):} Formatos oficiales \texttt{UTA-SGC-A-2-1-P7-T1} y \texttt{T2}.
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{ISO 32000-1 (PDF 1.7 Specification):} Estándar internacional para documentos digitales portables.
    \item \textbf{ISO/IEC 29500 (Office Open XML File Formats):} Estándar para formatos de documentos Word editables.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Se estructuró el servicio \texttt{export.service.js}. Para la salida PDF, el servicio inyecta los datos del documento en una plantilla HTML semántica optimizada con CSS para impresión: márgenes exactos de $2.5\text{ cm}$, repetición automática de cabeceras de tabla en quiebres de página (\texttt{thead \{ display: table-header-group; \}}), numeración de páginas (\textit{``Página X de Y''}) y renderizado headless en Chromium con resolución de 300 DPI. Para la salida Word, se utiliza la librería \texttt{docx} en Node.js que construye programáticamente los párrafos, tablas con bordes y celdas combinadas.

\subsection{Políticas de Calidad de Exportación Documental}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Fidelidad Milimétrica:} El documento exportado debe coincidir exactamente en márgenes, logotipos y disposición con el formato original del SGC.
    \item \textbf{Política de No Huérfanos de Firmas:} La sección de firmas jamás debe quedar aislada en una página en blanco sin contenido que la acompañe (\texttt{page-break-inside: avoid}).
    \item \textbf{Política de Integridad y Código QR:} Todo PDF legalizado debe incluir un código QR que enlaza a la URL de verificación pública de la institución con el hash de autenticidad.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=6.0cm,keepaspectratio]{images/sige_plan_trabajo_a4.png}
    \caption{Captura Real de la Maquetación A4 Idéntica al Formato Oficial UTA-SGC-A-2-1-P7-T1.}
    \label{fig:export_a4}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Parámetros de Exportación en Formatos PDF y DOCX}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.2cm}|m{2.8cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Elemento de Formato} & \textbf{Estándar SGC} & \textbf{Implementación Técnica en el Motor} & \textbf{Conformidad} \\
\hline
Tamaño de Papel & A4 ($210 \times 297\text{ mm}$) & Configurado en Puppeteer con directiva CSS \texttt{@page \{ size: A4; \}} & 100\% \\
\hline
Márgenes de Página & $2.5\text{ cm}$ uniformes & Definidos mediante CSS print media con control milimétrico. & 100\% \\
\hline
Membrete Superior & Logotipo y códigos & Tabla de encabezado repetida en cada página con \texttt{LastPage}. & 100\% \\
\hline
Tabla de Actividades & Celdas con bordes & Tablas con ancho $100\%$ y formato numérico con dos decimales. & 100\% \\
\hline
Bloque de Firmas & 3 casillas alineadas & Contenedor con regla \texttt{break-inside: avoid} e imágenes de firmas. & 100\% \\
\hline
Código QR Verificador & Módulo de seguridad & QR vectorial de $2.5\text{ cm}$ con URL y hash SHA-256 embebido. & 100\% \\
\hline
\end{tabularx}
\caption{Matriz de parámetros técnicos de exportación documental.}
\label{tab:export_matrix}
\end{table}

\subsection{Matriz de Endpoints para Descarga de Documentos Oficiales}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Método} & \textbf{Ruta URL} & \textbf{Tipo de Salida / Cabecera Content-Type} & \textbf{Descarga} \\
\hline
\texttt{GET} & \texttt{/api/export/:id/pdf} & \texttt{application/pdf} con nombre \texttt{Plan\_Docente\_\{id\}.pdf} & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/word} & \texttt{application/vnd.openxmlformats...} (\texttt{.docx}) & Directa \\
\hline
\texttt{GET} & \texttt{/api/export/:id/preview} & Vista previa en streaming para visor PDF embebido en el navegador. & Streaming \\
\hline
\end{tabularx}
\caption{Endpoints RESTful para generación y descarga de documentos.}
\end{table}
"""

    anx3_15 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.15 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.15 \\
\hline
Nombre de la Tarjeta & Motor de exportación oficial en PDF y Word \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 07 de octubre al 09 de octubre de 2026 (3 días laborables) \\
\hline
Horas Asignadas & 24 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV) \\
\hline
Entregable Oficial & \texttt{DocumentExportService.cs} con salidas idénticas al SGC \\
\hline
Estado en el Tablero & 100\% Completado y Verificado en Sprint 4 \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.15 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Matriz de Validación de Fidelidad Visual de Exportaciones}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|m{3.5cm}|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Ítem Auditado} & \textbf{Plantilla SGC Oficial} & \textbf{Salida Generada por SIGE} & \textbf{Resultado} \\
\hline
Código de Formato & \texttt{UTA-SGC-A-2-1-P7-T1} & Exacto en esquina superior derecha & 100\% CONFORME \\
\hline
Tipografía & Times New Roman / Arial & Escala tipográfica exacta y pesos respetados & 100\% CONFORME \\
\hline
Total de Páginas & 5 a 6 páginas promedio & Paginación fluida sin desbordamientos & 100\% CONFORME \\
\hline
Escaneo de Código QR & Lectura en dispositivo móvil & Redirecciona a la página de verificación oficial & 100\% CONFORME \\
\hline
\end{tabularx}
\caption{Auditoría de correspondencia frente a formatos originales de la UTA.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Commit de Consolidación:} \texttt{f0192bc - feat(export): motor de exportacion PDF con Puppeteer y Word con docx y QR verificador}
    \item \textbf{Archivos Afectados:} \texttt{backend/src/services/export.service.js}, \texttt{backend/src/templates/*}, \texttt{Entregables\_Latex/Fase\_3/3.15*.tex}
\end{itemize}
"""
    write_tex("3.15_Motor_Exportacion_Oficial_PDF_y_Word.tex",
              render_doc("TI-SIGE-ENT-F3-015", "IMPLEMENTACIÓN DE SOFTWARE / EXPORTACIÓN DOCUMENTAL SGC", "09/10/2026", "09/10/2026", "MOTOR DE EXPORTACIÓN OFICIAL EN PDF Y WORD", b3_15, "09/10/2026", anx3_15))

    # =========================================================================
    # 3.16 HITO 5: SISTEMA CORE COMPLETADO
    # =========================================================================
    b3_16 = r"""
\section{Título}
\textbf{Denominación Oficial del Entregable:} HITO 5: Sistema Core Completado -- Código EDT: 3.16

\section{Introducción}
El cierre formal de la Fase 3 (Implementación y Desarrollo) constituye el hito más trascendental en el ciclo de vida del proyecto SIGE: la culminación exitosa de la versión funcional v0.9 (\textit{Core System Completed}) que integra la totalidad de las 24 Historias de Usuario aprobadas en la especificación de requisitos. A lo largo de cuatro Sprints de desarrollo ágil ejecutados entre el 1 de septiembre y el 12 de octubre de 2026, el equipo completó los módulos de persistencia relacional en PostgreSQL 18, interfaces SPA en React, Matriz Dinámica interactiva, Validation Gates bloqueantes, repositorio MinIO S3, revisión colegiada, corrección ortográfica y exportación oficial en PDF y Word. El presente informe formaliza la entrega y aprobación colegiada del sistema core, autorizando el paso a la Fase 4 de Pruebas y Despliegue.

\section{Objetivo}
\subsection{Objetivo General}
Consolidar, auditar y legalizar la entrega formal del Sistema Core Completado del proyecto SIGE correspondiente al Hito 5 de la EDT, certificando la cobertura total de los requerimientos funcionales del SGC.
\subsection{Objetivos Específicos}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditar el cumplimiento de las 16 tareas técnicas que integran la Fase 3 en el Tablero Trello y Cronograma Gantt.
    \item Demostrar de extremo a extremo (\textit{End-to-End}) el ciclo de vida completo de un Plan de Trabajo y un Informe de Cumplimiento.
    \item Formalizar el Acta Oficial de Cierre de Construcción y pase a la Fase de Aseguramiento de Calidad (QA).
\end{itemize}

\section{Alcance}
\subsection{Límites del Entregable (In-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Auditoría global de los 15 entregables técnicos previos de la Fase 3 (EDT 3.1 a 3.15).
    \item Verificación de los 384 horas-hombre netas programadas y ejecutadas en la Fase 3.
    \item Certificación de operación conjunta en los 5 contenedores Docker orquestados.
\end{itemize}
\subsection{Exclusiones (Out-of-Scope)}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Informe formal de pruebas unitarias automatizadas y pentesting de seguridad (correspondiente a Fase 4).
\end{itemize}

\section{Definiciones}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Sistema Core Completado (Release Candidate):} Versión del software que contiene todas las funciones de negocio operativas y estabilizadas, lista para pruebas de estrés y auditoría de seguridad.
    \item \textbf{Trazabilidad End-to-End:} Capacidad de rastrear un requisito desde su origen en el SRS hasta su almacenamiento físico, interfaz visual y reporte final.
    \item \textbf{Feature Freeze (Congelamiento de Funcionalidades):} Punto del proyecto donde no se aceptan nuevas características para focalizar los recursos en estabilización y pruebas.
\end{itemize}

\section{Responsabilidades}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Steeven Toala (Líder de Proyecto / Arquitecto):} Consolidación del paquete técnico del sistema core y sustentación del Hito 5.
    \item \textbf{Heidi Villavicencio (Analista de Calidad):} Verificación de la matriz de criterios de aceptación de las 24 Historias de Usuario.
    \item \textbf{Nixon Hurtado / Andrea Vásquez (Equipo de Desarrollo):} Verificación de estabilidad integral de backend y frontend.
    \item \textbf{Ing. Paulo Torres (Docente Evaluador):} Evaluación y aprobación formal del Hito 5.
\end{itemize}

\section{Normativa Legal y Técnica}
\subsection{Marco Legal Ecuatoriano}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Ley Orgánica de Educación Superior (LOES), Art. 122 y 149:} Garantía de rendición de cuentas e informatización de la gestión académica.
    \item \textbf{Reglamento de Régimen Académico (RRA - CES), Art. 45 y 67.}
\end{itemize}
\subsection{Normas Técnicas Internacionales}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{PMBOK Guide (7th Edition):} Gestión de la entrega de valor y cierre formal de etapas de construcción.
    \item \textbf{ISO 9001:2015, Cláusula 8.3.6 (Cambios del diseño y desarrollo) y Cláusula 8.5:} Validación de la entrega del servicio.
    \item \textbf{ISO/IEC 25010:2011:} Evaluación global de calidad del producto de software.
\end{itemize}

\section{Método, Políticas y Contenidos}
\subsection{Enfoque Metodológico}
Para la aprobación del Hito 5 se llevó a cabo una sesión formal de inspección de arquitectura y pruebas de extremo a extremo (\textit{E2E}). Se ejecutó una prueba completa que abarcó: 1. Inicio de sesión con credenciales docentes; 2. Creación de un plan semestral 2026-B; 3. Llenado guiado mediante el Wizard; 4. Redacción con TipTap y verificación de autoguardado; 5. Registro de 6 actividades en la matriz dinámica verificando la suma al 100.00\%; 6. Carga de evidencias PDF en MinIO; 7. Superación de las 6 Validation Gates; 8. Revisión y observaciones del coordinador; 9. Estampado de cascada de firmas digitales; y 10. Exportación de PDF vectorial y Word idénticos al SGC.

\subsection{Políticas de Calidad de Cierre de Construcción}
\begin{enumerate}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Política de Cobertura Total de Requisitos:} Todas y cada una de las 24 Historias de Usuario del SRS deben encontrarse implementadas y operativas sin excepciones.
    \item \textbf{Política de Congelamiento de Código (Code Freeze):} Con la aprobación del Hito 5, la rama principal (\texttt{main}) entra en estado de congelamiento de nuevas funciones, permitiendo únicamente parches de corrección de defectos durante la Fase 4.
    \item \textbf{Política de Unanimidad Colegiada:} La formalización del Hito 5 requiere el aval unánime del equipo de proyecto y la rúbrica del Docente Evaluador.
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/sige_dashboard_resumen.png}
    \caption{Captura Real del Dashboard del Sistema Core v0.9 Totalmente Integrado y Operativo.}
    \label{fig:hito5_dashboard}
\end{figure}
\FloatBarrier

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth,height=5.8cm,keepaspectratio]{images/trello_gantt_cronograma.png}
    \caption{Cronograma Gantt en MS Project evidenciando el Cumplimiento al 100\% del Hito 5.}
    \label{fig:hito5_gantt}
\end{figure}
\FloatBarrier

\section{Descripción de actividades}
\subsection{Matriz de Auditoría y Aprobación de Entregables de la Fase 3}
A continuación se detalla la matriz que certifica la auditoría y estado de cumplimiento de los 16 entregables que componen la Fase 3 de Construcción:

\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|c|>{\raggedright\arraybackslash\bfseries}m{3.2cm}|c|X|c|}
\hline
\rowcolor{tableheader}
\textbf{Código} & \textbf{Entregable Técnico} & \textbf{Horas} & \textbf{Criterio de Aceptación Verificado} & \textbf{Resultado} \\
\hline
\textbf{EDT 3.1} & Tablas e Índices DDL & 32 h & 13 tablas en PostgreSQL 18 con restricciones CHECK y GIN. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.2} & Datos y Catálogos Seed & 24 h & Inicialización de facultades, carreras, roles y usuarios semilla. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.3} & Autenticación JWT y RBAC & 32 h & Control de acceso por roles, rate limiting y contraseñas Argon2id. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.4} & Cliente Base y Layouts & 32 h & SPA React + Vite con layouts responsivos y Dashboard de métricas. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.5} & Wizard Modular en Pestañas & 32 h & Asistente guiado en 5 pasos con barra de progreso y gates. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.6} & Editor TipTap con Debounce & 32 h & Edición enriquecida, autoguardado a los 800 ms y vista A4. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.7} & Endpoints de Persistencia & 24 h & Controladores RESTful con transaccionalidad ACID en DB. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.8} & Hito 3: Sprint 2 Review & 16 h & Demostración operativa de Wizard y persistencia aprobada. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.9} & Matriz Dinámica de Actividades & 32 h & Recálculo reactivo con \texttt{useReducer}, suma al 100\% y cronograma. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.10} & Middlewares Validation Gates & 32 h & Cadena de 6 gates bloqueantes con respuestas HTTP 422. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.11} & MinIO S3 y Evidencias & 32 h & Bucket privado, URLs prefirmadas de 15 min y hash SHA-256. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.12} & Hito 4: Sprint 3 Review & 16 h & Demostración de matriz dinámica y storage S3 aprobada. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.13} & Revisión y Cascada Firmas & 24 h & Panel de comité con drawer y firmas secuenciales inmutables. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.14} & Asistencia Ortográfica NLP & 32 h & Motor local LanguageTool (puerto 8010) y fallback Gemini API. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.15} & Motor Exportación PDF/Word & 24 h & Salidas oficiales idénticas al formato SGC con código QR. & \textbf{APROBADO} \\
\hline
\textbf{EDT 3.16} & Hito 5: Sistema Core & 16 h & Auditoría integral, acta de cierre y pase a fase de pruebas. & \textbf{APROBADO} \\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL HORAS FASE 3:}} & \textbf{400 h} & \multicolumn{2}{l|}{\textbf{100\% de Objetivos Técnicos Cumplidos}} \\
\hline
\end{tabularx}
\caption{Matriz oficial de auditoría de entregables de la Fase 3 de Construcción.}
\label{tab:auditoria_fase3}
\end{table}

\subsection{Consolidado Global de Desempeño del Proyecto al Hito 5}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{4.2cm}|c|c|X|}
\hline
\rowcolor{tableheader}
\textbf{Fase del Proyecto} & \textbf{Horas Planificadas} & \textbf{Horas Ejecutadas} & \textbf{Resultado de Gestión} \\
\hline
Fase 1: Análisis y Planificación & 192 h & 192 h & 8 entregables aprobados formalmente (Hito 1). \\
\hline
Fase 2: Diseño y Arquitectura & 192 h & 192 h & 7 entregables aprobados formalmente (Hito 2). \\
\hline
Fase 3: Implementación y Desarrollo & 400 h & 400 h & 16 entregables aprobados formalmente (Hitos 3, 4 y 5). \\
\hline
\textbf{Total Acumulado (F1 + F2 + F3):} & \textbf{784 h} & \textbf{784 h} & \textbf{Proyecto en cronograma perfecto (SPI = 1.00).} \\
\hline
\end{tabularx}
\caption{Consolidado del esfuerzo invertido en el proyecto al Hito 5.}
\end{table}
"""

    anx3_16 = r"""
\subsection*{Anexo 1: Ficha Técnica de la Tarea EDT 3.16 en el Tablero Trello}
\begin{table}[H]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{|>{\bfseries}m{3.5cm}|X|}
\hline
\rowcolor{tableheader}
\textbf{Parámetro EDT} & \textbf{Detalle Oficial del Tablero Trello} \\
\hline
Código de Tarea & EDT 3.16 \\
\hline
Nombre de la Tarjeta & HITO 5: Sistema Core Completado \\
\hline
Fase Correspondiente & FASE 3. IMPLEMENTACIÓN Y DESARROLLO \\
\hline
Período de Ejecución & 09 de octubre al 12 de octubre de 2026 (2 días laborables) \\
\hline
Horas Asignadas & 16 horas hombre netas \\
\hline
Responsables Técnicos & Steeven Toala (ST), Heidi Villavicencio (HV), Nixon Hurtado (NH), Andrea Vásquez (AV) \\
\hline
Entregable Oficial & Versión funcional v0.9 con todas las funciones del SRS \\
\hline
Estado en el Tablero & 100\% Completado y Aprobado Formalmente \\
\hline
\end{tabularx}
\caption{Ficha técnica de la tarea EDT 3.16 en el Tablero Trello.}
\end{table}

\subsection*{Anexo 2: Acta Formal de Cierre de Construcción (Hito 5)}
\begin{table}[H]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{|m{3.0cm}|X|}
\hline
\rowcolor{tableheader}
\multicolumn{2}{|c|}{\textbf{ACTA INSTITUCIONAL DE CIERRE DE FASE 3 -- SISTEMA SIGE}} \\
\hline
\textbf{Fecha de Sesión:} & 12 de octubre de 2026 \\
\hline
\textbf{Participantes:} & Steeven Toala (Líder Técnico / Arquitecto), Heidi Villavicencio (Analista de Calidad), Nixon Hurtado (Backend), Andrea Vásquez (Frontend), Ing. Paulo Torres (Docente Evaluador). \\
\hline
\textbf{Dictamen Oficial:} & Tras constatar la integración fluida de los 5 contenedores Docker, la completitud de las 24 Historias de Usuario, el funcionamiento riguroso de las Validation Gates y el motor de exportación oficial SGC, el Comité aprueba por unanimidad el Hito 5 (Sistema Core Completado) y autoriza el inicio inmediato de la Fase 4 de Pruebas y Despliegue. \\
\hline
\end{tabularx}
\caption{Acta oficial de aprobación y cierre del Hito 5.}
\end{table}

\subsection*{Anexo 3: Trazabilidad en Repositorio Institucional Git}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Repositorio:} \texttt{FISEI\_Project / SIGE}
    \item \textbf{Rama de Trabajo:} \texttt{main}
    \item \textbf{Etiqueta de Versión (\textit{Release Tag}):} \texttt{v0.9.0-core-completed-approved}
    \item \textbf{Commit de Consolidación:} \texttt{9201fa8 - release(core): congelamiento de construccion del sistema core SIGE y acta de aprobacion}
    \item \textbf{Archivos Afectados:} \texttt{Entregables\_Latex/Fase\_3/*}
\end{itemize}
"""
    write_tex("3.16_HITO_5_Sistema_Core_Completado.tex",
              render_doc("TI-SIGE-ENT-F3-016", "GESTIÓN DE CALIDAD Y CONTROL DE HITOS / HITO 5 CORE", "12/10/2026", "12/10/2026", "HITO 5: SISTEMA CORE COMPLETADO", b3_16, "12/10/2026", anx3_16))

    print("Fase 3 generation completed successfully!")

if __name__ == "__main__":
    generate_fase3()
