# update_fase2_deep_v2.py
# -*- coding: utf-8 -*-
"""
Script para:
1. Eliminar 'Paso X', '(Paso a Paso)', y clichés de IA en Fase 2.
2. Enriquecer en profundidad la sección 'Descripción de actividades' en EDT 2.2, 2.3, 2.4, 2.5, 2.6.
"""

import re

print(">>> Actualizando generate_fase2_enhanced.py...")
with open("generate_fase2_enhanced.py", "r", encoding="utf-8") as f:
    c = f.read()

# --- 1. Reemplazos de títulos de anexos y expresiones en Fase 2 ---
c = c.replace(r"\subsubsection*{1. Desglose Metodológico y Origen Real de los Casos de Uso (Paso a Paso)}",
              r"\subsubsection*{1. Especificación Formal y Trazabilidad de Casos de Uso}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Arquitectura de Software (Paso a Paso)}",
              r"\subsubsection*{1. Decisiones de Diseño Arquitectónico y Desacoplamiento en Capas}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico de los Diagramas Dinámicos (Paso a Paso)}",
              r"\subsubsection*{1. Modelado Dinámico y Especificación de Ciclos de Vida}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico del Diseño Relacional (Paso a Paso)}",
              r"\subsubsection*{1. Normalización Relacional en Tercera Forma Normal (3NF)}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Experiencia de Usuario (Paso a Paso)}",
              r"\subsubsection*{1. Metodología de Diseño UI/UX y Sistema de Tokens Visuales}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Contenerización (Paso a Paso)}",
              r"\subsubsection*{1. Orquestación Multi-Contenedor y Redes Aisladas en Docker}")
c = c.replace(r"\subsubsection*{1. Desglose Metodológico de la Auditoría del Hito 2 (Paso a Paso)}",
              r"\subsubsection*{1. Auditoría Técnica de la Línea Base Arquitectónica}")

# Reemplazos textuales de "paso"
c = c.replace("El sistema impide el avance al paso de firmas", "El sistema impide el avance a la etapa de firmas")
c = c.replace("flujo de datos paso a paso", "flujo de datos de extremo a extremo")
c = c.replace(r"\textbf{Paso} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validaci",
              r"\textbf{Etapa} & \textbf{Estado Inicial} & \textbf{Evento Disparador y Validaci")
c = c.replace("Barra de progreso de 5 pasos", "Barra de progreso de 5 etapas")
c = c.replace("El proceso de diseño se desarrolló paso a paso:",
              "El proceso de diseño de interfaz se desarrolló mediante las siguientes fases metodológicas:")
c = c.replace("Se desglosó el formulario en 5 pasos secuenciales",
              "Se desglosó el formulario en 5 etapas secuenciales")
c = c.replace("El procedimiento de despliegue se estructuró paso a paso:",
              "El procedimiento de despliegue se estructuró en fases de orquestación técnica:")

# --- 2. Enriquecer "Descripción de actividades" en Fase 2 ---

# EDT 2.2
act2_2 = r"""\section{Descripción de actividades}
El diseño arquitectónico de SIGE se concibió bajo los principios de desacoplamiento de Clean Architecture, garantizando que la lógica de negocio institucional permanezca independiente de componentes de persistencia o interfaces de usuario. Las actividades de arquitectura desarrolladas abarcaron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Selección y Justificación del Patrón Clean Architecture:} Se adoptó una arquitectura en cuatro capas concéntricas (Dominio, Casos de Uso, Adaptadores de Interfaz y Frameworks/Drivers), asegurando que las entidades normativas de la FISEI no posean dependencias hacia el motor de persistencia relacional ni bibliotecas de terceros.
    \item \textbf{Formulación y Registro de Decisiones de Arquitectura (ADR-01 a ADR-06):} Se redactaron formalmente seis registros técnicos de decisión: ADR-01 (Clean Architecture), ADR-02 (PostgreSQL 18 con soporte JSONB para secciones de texto enriquecido), ADR-03 (React 19 SPA con Tailwind CSS), ADR-04 (Editor TipTap con autoguardado asíncrono con debounce de 1500 ms), ADR-05 (MinIO S3 para custodia de evidencias) y ADR-06 (Autenticación JWT con rotación de refresh tokens y Argon2id).
    \item \textbf{Modelado de Diagramas de Contexto y Contenedores bajo el Modelo C4:} Se elaboraron las vistas arquitectónicas de Nivel 1 (Contexto de Sistema interactuando con Docentes, Directores y SGA) y Nivel 2 (Contenedores web, API REST Express v5, base de datos PostgreSQL, servidor MinIO y servicio LanguageTool).
    \item \textbf{Diseño de Políticas de Seguridad Perimetral y Resiliencia:} Se establecieron protocolos de comunicación sobre HTTPS/TLS, interceptación centralizada de errores en Express mediante un error handler unificado y aislamiento de variables de entorno sensibles en archivos \texttt{.env} protegidos.
\end{itemize}

\subsection{Matriz de Decisiones de Arquitectura de Software (ADR-01 a ADR-06)}"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Decisiones de Arquitectura de Software \(ADR-01 a ADR-06\)\}',
    lambda m: act2_2,
    c
)

# EDT 2.3
act2_3 = r"""\section{Descripción de actividades}
El modelado del comportamiento dinámico del sistema y la definición de las entidades de dominio aseguraron una representación computacional fidedigna de los procesos del SGC. El equipo técnico llevó a cabo las siguientes actividades de modelado UML:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Modelado Dinámico de Secuencia UML para Casos de Uso Críticos:} Se construyeron diagramas de interacción temporal para los flujos más complejos del sistema: autenticación e intercambio de tokens JWT, creación asistida del plan mediante Wizard, y procesamiento concurrente de firmas con validación de compuertas.
    \item \textbf{Especificación de Diagramas de Actividades con Particiones (Swimlanes):} Se modelaron los flujos de control paralelos y condicionales distribuidos entre el Docente Elaborador, el Coordinador de Comisión, el Subdecano y el Motor de Reglas del Sistema, clarificando los puntos de decisión y bifurcación ante observaciones.
    \item \textbf{Modelado Estructural de Clases de Dominio Institucional:} Se diseñaron las entidades fundamentales del sistema en TypeScript/JavaScript: \texttt{PlanTrabajoDocente}, \texttt{ActividadDocente}, \texttt{SeccionDocumento}, \texttt{EvidenciaRespaldo} y \texttt{FirmaDigital}, definiendo sus atributos, métodos de cálculo y contratos de validación intrínseca.
    \item \textbf{Formalización de la Máquina de Estados del Documento SGC:} Se especificaron los estados válidos del ciclo documental (\texttt{Borrador}, \texttt{En\_Revision}, \texttt{Observado}, \texttt{Aprobado\_Carrera}, \texttt{Legalizado\_Subdecanato}) y las transiciones atómicas permitidas bajo control transaccional ACID.
\end{itemize}

\subsection{Matriz de Entidades del Dominio y Métodos Operativos}"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Entidades del Dominio y Métodos Operativos\}',
    lambda m: act2_3,
    c
)

# EDT 2.4
act2_4 = r"""\section{Descripción de actividades}
El diseño de la capa física de persistencia se orientó a garantizar la integridad referencial histórica y el soporte eficiente para estructuras de datos semiestructuradas en PostgreSQL 18. Las actividades de ingeniería de datos comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Normalización Relacional Rigurosa en Tercera Forma Normal (3NF):} Se descompuso el modelo conceptual en 13 tablas relacionales normalizadas para erradicar redundancias y anomalías de actualización en catálogos de carreras, periodos, comisiones, docentes, planes y firmas.
    \item \textbf{Diseño de Restricciones de Integridad y Claves Primarias UUIDv4:} Se asignaron identificadores universales únicos (\texttt{uuid\_generate\_v4()}) en las tablas operativas para prevenir ataques de enumeración secuencial, junto con llaves foráneas \texttt{ON DELETE RESTRICT} que preservan los expedientes históricos.
    \item \textbf{Programación de Restricciones CHECK Nativas en Motor:} Se implementaron validaciones a nivel de base de datos para garantizar que las horas docentes semanales no superen 40.0h (\texttt{chk\_horas\_rango}) y que las ponderaciones no excedan el 100.00\% (\texttt{chk\_pond\_rango}), blindando la consistencia incluso ante accesos directos al motor.
    \item \textbf{Estrategia de Indexación Compuesta B-Tree e Invertida GIN:} Se diseñaron índices B-Tree en pares de consulta frecuente (\texttt{idx\_plan\_doc\_per}) y de índices GIN sobre campos de contenido enriquecido JSONB (\texttt{idx\_sec\_jsonb}) para búsquedas textuales de alta velocidad.
\end{itemize}

\subsection{Matriz del Diccionario de Datos del Sistema (13 Tablas Normalizadas)}"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz del Diccionario de Datos del Sistema \(13 Tablas Normalizadas\)\}',
    lambda m: act2_4,
    c
)

# EDT 2.5
act2_5 = r"""\section{Descripción de actividades}
El diseño de la experiencia de usuario (UX) y las interfaces visuales (UI) se centró en facilitar el diligenciamiento de los formularios oficiales del SGC, minimizando la sobrecarga cognitiva del docente. Las actividades de diseño de interfaces incluyeron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño de Arquitectura de Información y Wireframes en Figma:} Se elaboraron prototipos navegables de baja y alta fidelidad priorizando la ergonomía visual y la reducción de clics en las tareas más repetitivas de carga horaria y redacción.
    \item \textbf{Construcción del Sistema de Diseño (Design Tokens) Institucional:} Se formalizó la paleta cromática oficial de la UTA (#8B1D24 Rojo UTA como primario, #6B1218 para estados activos, escala neutra de grises y ámbar #D97706 para observaciones), estandarizando tipografías y espaciados modulares.
    \item \textbf{Especificación del Flujo Interactivo del Asistente Wizard en 5 Etapas:} Se estructuró el flujo modular de llenado: Etapa Inicial (Datos Generales), Etapa de Secciones SGC (Justificación y Objetivos), Etapa Matricial (Tabla de Actividades 40h), Etapa de Custodia (Evidencias MinIO) y Etapa de Cierre (Firmas y Verificación).
    \item \textbf{Auditoría de Usabilidad y Accesibilidad bajo Norma WCAG 2.1 AA:} Se verificó sistemáticamente el contraste visual de textos sobre fondos (ratio 7.2:1 para texto normal y 4.8:1 para botones de acción) y el diseño adaptativo responsive para resoluciones desktop y laptop institucionales.
\end{itemize}

\subsection{Matriz de Especificación de Vistas y Componentes UI/UX}"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Especificación de Vistas y Componentes UI/UX\}',
    lambda m: act2_5,
    c
)

# EDT 2.6
act2_6 = r"""\section{Descripción de actividades}
La definición de la arquitectura de contenedores permitió crear un entorno de despliegue local reproducible, aislado y altamente confiable mediante Docker Compose. Las actividades de infraestructura y DevOps comprendieron:

\begin{itemize}[leftmargin=1.5em, itemsep=4pt]
    \item \textbf{Diseño de la Topología Multi-Contenedor en Docker Compose:} Se definieron cinco microservicios contenerizados independientes: \texttt{sige-frontend} (Node.js/Vite en puerto 5173), \texttt{sige-backend} (Express v5 en puerto 3000), \texttt{sige-db} (PostgreSQL 18 en puerto 5432), \texttt{sige-minio} (S3 Object Storage en puertos 9000/9001) y \texttt{sige-languagetool} (corrección ortográfica en puerto 8010).
    \item \textbf{Configuración de Redes Bridge Aisladas y Políticas de Exposición Mínima:} Se creó una red privada institucional (\texttt{sige-network}) donde la base de datos y el motor de almacenamiento se comunican de forma interna sin exponer puertos innecesarios a la red del host.
    \item \textbf{Aprovisionamiento de Volúmenes Nombrados Persistentes:} Se configuraron volúmenes gestionados (\texttt{pgdata}, \texttt{miniodata}) que garantizan la persistencia inalterable de los datos de planes de trabajo y evidencias PDF ante reinicios o despliegues continuos.
    \item \textbf{Programación de Healthchecks Nativos y Dependencias de Arranque Secuencial:} Se implementaron comprobaciones periódicas de disponibilidad (\texttt{pg\_isready}, endpoints \texttt{/health}) con directivas \texttt{condition: service\_healthy} para evitar que el backend inicie antes de que la base de datos esté lista para recibir conexiones.
\end{itemize}

\subsection{Matriz de Especificación de Servicios en Docker Compose}"""

c = re.sub(
    r'\\section\{Descripci[oó]n de actividades\}\s*\\subsection\{Matriz de Especificación de Servicios en Docker Compose\}',
    lambda m: act2_6,
    c
)

with open("generate_fase2_enhanced.py", "w", encoding="utf-8") as f:
    f.write(c)

print("generate_fase2_enhanced.py actualizado con éxito.")
