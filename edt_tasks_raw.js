const tasks = [
        // Retrocompatibilidad con scripts
        // EDT_TASKS contiene las 49 tareas estructuradas con código EDT

            {
                        "id": "edt-1-0",
                        "rowId": 1,
                        "code": "1",
                        "edtCode": "EDT 1.0",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": true,
                        "title": "FASE 1. ANÁLISIS Y PLANIFICACIÓN",
                        "dates": "12 ago - 24 ago",
                        "dateStart": "2026-08-12",
                        "dateEnd": "2026-08-24",
                        "durationDays": 9,
                        "durationHours": 72,
                        "durationLabel": "9 d (72h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo de Proyecto SIGE",
                        "avatarColor": "bg-red-600",
                        "tag": "Fase Resumen",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "",
                        "predecessorCodes": "-",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Aprobación de Fase 1 y Paquete Entregables Semana 1",
                        "description": "Fase inicial de levantamiento institucional, especificación formal SRS IEEE 830, reglas de negocio y caso de negocio del proyecto SIGE. Calendario laboral: lunes a viernes 8h/día.",
                        "subtasks": [
                                    {
                                                "text": "Levantamiento y entrevistas con docentes",
                                                "done": true
                                    },
                                    {
                                                "text": "Formalización de SRS y reglas SGC",
                                                "done": true
                                    },
                                    {
                                                "text": "Elaboración de Caso de Negocio y Charter",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-1",
                        "rowId": 2,
                        "code": "1.1",
                        "edtCode": "EDT 1.1",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Levantamiento de información del proceso actual",
                        "dates": "12 ago - 14 ago",
                        "dateStart": "2026-08-12",
                        "dateEnd": "2026-08-14",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "SGC / Diagnóstico",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "",
                        "predecessorCodes": "-",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "01_Levantamiento_Informacion_Proceso_Actual.md (Mapeo As-Is)",
                        "description": "Diagnóstico exhaustivo del flujo actual de elaboración de planes de trabajo e informes institucionales del Sistema de Gestión de Calidad (SGC). Mapeo de formatos UTA-SGC-A-2-1-P7-T1 y T2.",
                        "subtasks": [
                                    {
                                                "text": "Mapeo de pasos manuales en Word y Excel de planes de trabajo",
                                                "done": true
                                    },
                                    {
                                                "text": "Identificación de inconsistencias en versiones y pérdidas de firmas",
                                                "done": true
                                    },
                                    {
                                                "text": "Entrevistas con docentes elaboradores y coordinadores de área",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-2",
                        "rowId": 3,
                        "code": "1.2",
                        "edtCode": "EDT 1.2",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Identificación de actores y procesos",
                        "dates": "13 ago - 18 ago",
                        "dateStart": "2026-08-13",
                        "dateEnd": "2026-08-18",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "HV",
                        "assigneeName": "Heidy Villavicencio (Analista)",
                        "avatarColor": "bg-blue-600",
                        "tag": "Stakeholders",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "2",
                        "predecessorCodes": "EDT 1.1 (SS+1d)",
                        "isParallel": true,
                        "parallelWith": "EDT 1.1",
                        "parallelReason": "Inicia el jueves 13 en paralelo con el cierre de EDT 1.1, pausando el fin de semana del 15-16 y culminando el martes 18.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "02_Identificacion_Actores_Procesos.md (Matriz de Stakeholders)",
                        "description": "Mapeo riguroso de interesados, niveles de poder e interés, roles institucionales (Docente Elaborador, Coordinador de Área, Coordinador de Carrera, Subdecano y Administrador SGC).",
                        "subtasks": [
                                    {
                                                "text": "Matriz de poder vs impacto de cada rol",
                                                "done": true
                                    },
                                    {
                                                "text": "Definición de expectativas y requerimientos de información",
                                                "done": true
                                    },
                                    {
                                                "text": "Formalización de la cascada de 3 firmas de responsabilidad",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-3",
                        "rowId": 4,
                        "code": "1.3",
                        "edtCode": "EDT 1.3",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Definición de requisitos funcionales y no funcionales",
                        "dates": "17 ago - 21 ago",
                        "dateStart": "2026-08-17",
                        "dateEnd": "2026-08-21",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "HV, AV",
                        "assigneeName": "Heidy Villavicencio / Andrea Vasquez",
                        "avatarColor": "bg-blue-600",
                        "tag": "Requerimientos",
                        "tagColor": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
                        "predecessors": "2, 3",
                        "predecessorCodes": "EDT 1.1, EDT 1.2",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "03_Definicion_Requisitos_Funcionales_No_Funcionales.md (SRS)",
                        "description": "Especificación formal de lunes a viernes bajo estándar IEEE 830 con 24 requisitos funcionales (RF-01 a RF-24) y 10 no funcionales (RNF-01 a RNF-10).",
                        "subtasks": [
                                    {
                                                "text": "Redacción de 24 Requerimientos Funcionales clasificados",
                                                "done": true
                                    },
                                    {
                                                "text": "Especificación de Requerimientos No Funcionales (ISO 25010)",
                                                "done": true
                                    },
                                    {
                                                "text": "Matriz de trazabilidad inicial de requisitos",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-4",
                        "rowId": 5,
                        "code": "1.4",
                        "edtCode": "EDT 1.4",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Definición del alcance, restricciones y objetivos SGC",
                        "dates": "18 ago - 21 ago",
                        "dateStart": "2026-08-18",
                        "dateEnd": "2026-08-21",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST, HV",
                        "assigneeName": "Steeven Toala / Heidy Villavicencio",
                        "avatarColor": "bg-amber-600",
                        "tag": "Alcance SGC",
                        "tagColor": "bg-amber-500/20 text-amber-300 border-amber-500/30",
                        "predecessors": "4",
                        "predecessorCodes": "EDT 1.3",
                        "isParallel": true,
                        "parallelWith": "EDT 1.5",
                        "parallelReason": "Se ejecuta de martes a viernes en paralelo con la definición de Validation Gates lógicas.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "04_Definicion_Alcance_Restricciones_Objetivos.md",
                        "description": "Delimitación del alcance incluido y exclusiones del sistema, objetivos SMART del proyecto, hitos de control de calidad institucional y cumplimiento del SGC UTA.",
                        "subtasks": [
                                    {
                                                "text": "Definición de fronteras del sistema e integraciones SI UTA",
                                                "done": true
                                    },
                                    {
                                                "text": "Establecimiento de límites, supuestos y restricciones técnicas",
                                                "done": true
                                    },
                                    {
                                                "text": "Objetivo general y objetivos específicos del software SIGE",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-5",
                        "rowId": 6,
                        "code": "1.5",
                        "edtCode": "EDT 1.5",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Reglas de negocio y Validation Gates lógicas",
                        "dates": "19 ago - 24 ago",
                        "dateStart": "2026-08-19",
                        "dateEnd": "2026-08-24",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST, NH",
                        "assigneeName": "Steeven Toala / Nixon Hurtado",
                        "avatarColor": "bg-amber-600",
                        "tag": "Validation Gates",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "4",
                        "predecessorCodes": "EDT 1.3",
                        "isParallel": true,
                        "parallelWith": "EDT 1.4",
                        "parallelReason": "Inicia el miércoles 19, pausa el fin de semana del 22-23 y culmina el lunes 24.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "05_Reglas_Negocio_Validation_Gates.md",
                        "description": "Formalización matemática de los Validation Gates: bloqueo de avance si evidencia < 100% sin justificación, cálculo de ponderaciones de actividades y bloqueo extemporáneo.",
                        "subtasks": [
                                    {
                                                "text": "Fórmula matemática de porcentaje de avance consolidado",
                                                "done": true
                                    },
                                    {
                                                "text": "Regla de bloqueo por evidencias no subidas a MinIO",
                                                "done": true
                                    },
                                    {
                                                "text": "Especificación del circuito de firmas obligatorias",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-6",
                        "rowId": 7,
                        "code": "1.6",
                        "edtCode": "EDT 1.6",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Elaboración de Caso de Negocio, ROI y Project Charter",
                        "dates": "20 ago - 24 ago",
                        "dateStart": "2026-08-20",
                        "dateEnd": "2026-08-24",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "Equipo",
                        "assigneeName": "ST, HV, NH, AV (Equipo Completo)",
                        "avatarColor": "bg-red-600",
                        "tag": "Caso de Negocio",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "5, 6",
                        "predecessorCodes": "EDT 1.4, EDT 1.5",
                        "isParallel": true,
                        "parallelWith": "EDT 1.7",
                        "parallelReason": "Jueves 20, Viernes 21 y Lunes 24 de agosto (3 días hábiles). Corre en paralelo con el setup de Git.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "06_Caso_de_Negocio.md & Project Charter Oficial",
                        "description": "Evaluación financiera y técnica: Presupuesto total ($630.30), Ahorro anual estimado ($23,700), Retorno de Inversión ROI (+3,660%), VAN ($84,212) y período de recuperación de 1.8 meses.",
                        "subtasks": [
                                    {
                                                "text": "Cálculo de costos directos de equipo y licencias Open Source",
                                                "done": true
                                    },
                                    {
                                                "text": "Análisis de ahorro de horas-docente por automatización",
                                                "done": true
                                    },
                                    {
                                                "text": "Redacción del Acta de Constitución del Proyecto (Charter)",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-7",
                        "rowId": 8,
                        "code": "1.7",
                        "edtCode": "EDT 1.7",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "Planificación del proyecto y cronograma de trabajo",
                        "dates": "20 ago - 24 ago",
                        "dateStart": "2026-08-20",
                        "dateEnd": "2026-08-24",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "ST",
                        "assigneeName": "Steeven Toala (Líder / Arquitecto)",
                        "avatarColor": "bg-amber-600",
                        "tag": "Planificación / EDT",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "5",
                        "predecessorCodes": "EDT 1.4",
                        "isParallel": true,
                        "parallelWith": "EDT 1.6",
                        "parallelReason": "Se elabora la EDT y el cronograma maestro durante los 3 días hábiles en paralelo con el Caso de Negocio.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "07_Planificacion_Proyecto_Cronograma_EDT.md & Cronograma MS Project",
                        "description": "Estructuración formal del plan de gestión del proyecto, descomposición EDT de 49 tareas, cronograma maestro en Microsoft Project con calendario laboral de Ambato (57 días laborables, 456 horas), dependencias y asignación de recursos.",
                        "subtasks": [
                                    {
                                                "text": "Elaboración de la Estructura de Desglose del Trabajo (EDT) de 49 tareas",
                                                "done": true
                                    },
                                    {
                                                "text": "Configuración del cronograma maestro en Microsoft Project con calendario de Ecuador",
                                                "done": true
                                    },
                                    {
                                                "text": "Asignación de recursos del equipo y estimación de esfuerzo en horas",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-1-8",
                        "rowId": 9,
                        "code": "1.8",
                        "edtCode": "EDT 1.8",
                        "phase": "fase1",
                        "phaseName": "FASE 1: ANÁLISIS Y PLANIFICACIÓN",
                        "isSummary": false,
                        "title": "HITO 1: Aprobación de Fase 1 y Entregable General Semana 1",
                        "dates": "24 ago",
                        "dateStart": "2026-08-24",
                        "dateEnd": "2026-08-24",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito de Fase",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "7, 8",
                        "predecessorCodes": "EDT 1.6, EDT 1.7",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "08_Entregable_General_Semana_1.md (Paquete Completo Aprobado)",
                        "description": "Hito formal de revisión y aprobación de la Fase 1 por el docente asesor Ing. Paulo Torres el lunes 24 de agosto de 2026.",
                        "subtasks": [
                                    {
                                                "text": "Consolidación del informe semanal 1 en LaTeX",
                                                "done": true
                                    },
                                    {
                                                "text": "Validación de conformidad de requerimientos",
                                                "done": true
                                    },
                                    {
                                                "text": "Firma de aprobación de avance de Fase 1",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-0",
                        "rowId": 10,
                        "code": "2",
                        "edtCode": "EDT 2.0",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": true,
                        "title": "FASE 2. DISEÑO RÁPIDO Y ARQUITECTURA",
                        "dates": "25 ago - 04 sep",
                        "dateStart": "2026-08-25",
                        "dateEnd": "2026-09-04",
                        "durationDays": 9,
                        "durationHours": 72,
                        "durationLabel": "9 d (72h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo de Proyecto SIGE",
                        "avatarColor": "bg-blue-600",
                        "tag": "Fase Resumen",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "9",
                        "predecessorCodes": "EDT 1.8",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Aprobación de Arquitectura y Paquete Entregables Semana 2",
                        "description": "Fase de especificación de arquitectura modular en Node.js + Express (v5), modelado de base de datos relacional PostgreSQL 18, prototipos Figma y contenedores locales Docker (9 días hábiles).",
                        "subtasks": [
                                    {
                                                "text": "Diseño de Casos de Uso y Arquitectura Clean",
                                                "done": true
                                    },
                                    {
                                                "text": "Modelo ER y Base de datos normalizada",
                                                "done": true
                                    },
                                    {
                                                "text": "Prototipos UX en Figma y contenedores Docker Compose",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-1",
                        "rowId": 11,
                        "code": "2.1",
                        "edtCode": "EDT 2.1",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Diagramas general y detallado de casos de uso",
                        "dates": "25 ago - 27 ago",
                        "dateStart": "2026-08-25",
                        "dateEnd": "2026-08-27",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "HV",
                        "assigneeName": "Heidy Villavicencio (Analista / UI-UX)",
                        "avatarColor": "bg-blue-600",
                        "tag": "Casos de Uso",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "9",
                        "predecessorCodes": "EDT 1.8",
                        "isParallel": true,
                        "parallelWith": "EDT 2.2",
                        "parallelReason": "Martes 25 a Jueves 27 de agosto en paralelo con el diseño de arquitectura técnica.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "01_Diagrama_General_Detallado_Casos_de_Uso.md",
                        "description": "Modelado UML de todas las interacciones de los actores institucionales: Elaborar Plan, Validar Matriz, Cargar Evidencia, Revisar en Comité, Firmar Digitalmente y Generar Informe.",
                        "subtasks": [
                                    {
                                                "text": "Diagrama de Casos de Uso General del Sistema SIGE",
                                                "done": true
                                    },
                                    {
                                                "text": "Especificación textual de escenarios primarios y alternos",
                                                "done": true
                                    },
                                    {
                                                "text": "Modelado de casos de uso de gestión extemporánea",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-2",
                        "rowId": 12,
                        "code": "2.2",
                        "edtCode": "EDT 2.2",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Diseño de arquitectura de la solución",
                        "dates": "25 ago - 28 ago",
                        "dateStart": "2026-08-25",
                        "dateEnd": "2026-08-28",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST",
                        "assigneeName": "Steeven Toala (Líder / Arquitecto)",
                        "avatarColor": "bg-amber-600",
                        "tag": "Arquitectura",
                        "tagColor": "bg-indigo-500/20 text-indigo-300 border-indigo-500/30",
                        "predecessors": "9",
                        "predecessorCodes": "EDT 1.8",
                        "isParallel": true,
                        "parallelWith": "EDT 2.1",
                        "parallelReason": "Martes 25 a Viernes 28 de agosto en paralelo con los casos de uso.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "02_Diseno_Arquitectura_Solucion.md (SAD & C4 Model)",
                        "description": "Definición de capas Domain, Application, Infrastructure y WebAPI. Patrones Mediator, Repository y CQRS. Integración desacoplada para MinIO y LanguageTool.",
                        "subtasks": [
                                    {
                                                "text": "Definir capas, controladores, middlewares y rutas en Express v5",
                                                "done": true
                                    },
                                    {
                                                "text": "Elaborar diagramas C4 (Contexto, Contenedores, Componentes)",
                                                "done": true
                                    },
                                    {
                                                "text": "Estrategia de inmutabilidad y firmas digitales",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-3",
                        "rowId": 13,
                        "code": "2.3",
                        "edtCode": "EDT 2.3",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Diagramas de secuencia, actividades y clases de dominio",
                        "dates": "27 ago - 02 sep",
                        "dateStart": "2026-08-27",
                        "dateEnd": "2026-09-02",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "ST, HV",
                        "assigneeName": "Steeven Toala / Heidy Villavicencio",
                        "avatarColor": "bg-amber-600",
                        "tag": "Diseño UML",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "11, 12",
                        "predecessorCodes": "EDT 2.1, EDT 2.2",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "03_Diagramas_Secuencia_Actividades_Clases.md",
                        "description": "Jueves 27 y Viernes 28 de agosto, pausa sábado 29 y domingo 30, continúa Lunes 31 de agosto al Miércoles 02 de septiembre (5 días hábiles netos).",
                        "subtasks": [
                                    {
                                                "text": "Diagrama de secuencia del flujo de firmas multinivel",
                                                "done": true
                                    },
                                    {
                                                "text": "Diagrama de actividades del ciclo de vida del informe",
                                                "done": true
                                    },
                                    {
                                                "text": "Diagrama de clases de entidades del SGC",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-4",
                        "rowId": 14,
                        "code": "2.4",
                        "edtCode": "EDT 2.4",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Diseño de base de datos relacional",
                        "dates": "28 ago - 03 sep",
                        "dateStart": "2026-08-28",
                        "dateEnd": "2026-09-03",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Base de Datos",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "12",
                        "predecessorCodes": "EDT 2.2",
                        "isParallel": true,
                        "parallelWith": "EDT 2.5",
                        "parallelReason": "Viernes 28 ago al Jueves 03 sep (5 días hábiles). El DBA diseña la BD mientras las diseñadoras construyen los wireframes en Figma.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "04_Diseno_Base_de_Datos_ER_Logico.md & schema.sql",
                        "architecture": "PostgreSQL 18 relacional ACID con tablas de usuarios, roles, tokens y auditoría",
                        "description": "Estructuración de las 13 tablas relacionales con índices, constraints y DDL oficial.",
                        "subtasks": [
                                    {
                                                "text": "Diagrama Entidad-Relación en Notación Crow's Foot",
                                                "done": true
                                    },
                                    {
                                                "text": "Diccionario de datos completo con tipos y constraints",
                                                "done": true
                                    },
                                    {
                                                "text": "Generación de scripts DDL PostgreSQL 18 (schema.sql, seed.sql, init.js)",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-5",
                        "rowId": 15,
                        "code": "2.5",
                        "edtCode": "EDT 2.5",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Diseño de interfaces y experiencia de usuario",
                        "dates": "28 ago - 03 sep",
                        "dateStart": "2026-08-28",
                        "dateEnd": "2026-09-03",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "HV, AV",
                        "assigneeName": "Heidy Villavicencio / Andrea Vasquez",
                        "avatarColor": "bg-blue-600",
                        "tag": "UI / UX Figma",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "11",
                        "predecessorCodes": "EDT 2.1",
                        "isParallel": true,
                        "parallelWith": "EDT 2.4",
                        "parallelReason": "Se diseña la experiencia visual en Figma en paralelo con el modelado de datos.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "05_Diseno_Interfaces_Wireframes_UX.md & Prototipo Figma",
                        "description": "Diseño de alta fidelidad: Wizard paso a paso para el elaborador, tabla dinámica de actividades y visor de observaciones.",
                        "subtasks": [
                                    {
                                                "text": "Wireframes de Wizard modular de secciones",
                                                "done": true
                                    },
                                    {
                                                "text": "Diseño de componentes de tabla de actividades responsive",
                                                "done": true
                                    },
                                    {
                                                "text": "Flujo interactivo de comité y cambio de estados",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-6",
                        "rowId": 16,
                        "code": "2.6",
                        "edtCode": "EDT 2.6",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "Arquitectura de microservicios y Docker Compose local",
                        "dates": "01 sep - 04 sep",
                        "dateStart": "2026-09-01",
                        "dateEnd": "2026-09-04",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST, NH",
                        "assigneeName": "Steeven Toala / Nixon Hurtado",
                        "avatarColor": "bg-amber-600",
                        "tag": "Docker Local",
                        "tagColor": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
                        "predecessors": "14",
                        "predecessorCodes": "EDT 2.4",
                        "isParallel": true,
                        "parallelWith": "EDT 2.5",
                        "parallelReason": "Martes 01 a Viernes 04 de septiembre en paralelo con los últimos wireframes de Figma.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "06_Arquitectura_Contenedores_Docker_Locales.md & docker-compose.yml",
                        "description": "Orquestación con Docker Compose de PostgreSQL 18 con volúmenes persistentes, MinIO Object Storage y servicio LanguageTool local.",
                        "subtasks": [
                                    {
                                                "text": "Crear docker-compose.yml con redes aisladas",
                                                "done": true
                                    },
                                    {
                                                "text": "Configurar bucket privado 'sige-evidencias' en MinIO",
                                                "done": true
                                    },
                                    {
                                                "text": "Verificar arranque saludable (Health Checks) de servicios",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-2-7",
                        "rowId": 17,
                        "code": "2.7",
                        "edtCode": "EDT 2.7",
                        "phase": "fase2",
                        "phaseName": "FASE 2: DISEÑO Y ARQUITECTURA",
                        "isSummary": false,
                        "title": "HITO 2: Aprobación de Arquitectura y Entregable General Semana 2",
                        "dates": "04 sep",
                        "dateStart": "2026-09-04",
                        "dateEnd": "2026-09-04",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito de Fase",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "13, 15, 16",
                        "predecessorCodes": "EDT 2.3, EDT 2.5, EDT 2.6",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "07_Entregable_General_Semana_2.md (Paquete Arquitectura Aprobado)",
                        "description": "Hito formal de aprobación de diseño y arquitectura técnica el viernes 04 de septiembre de 2026.",
                        "subtasks": [
                                    {
                                                "text": "Consolidación del informe técnico semanal 2 en LaTeX",
                                                "done": true
                                    },
                                    {
                                                "text": "Demostración del prototipo interactivo Figma",
                                                "done": true
                                    },
                                    {
                                                "text": "Revisión y firma de inicio de desarrollo Core",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-0",
                        "rowId": 18,
                        "code": "3",
                        "edtCode": "EDT 3.0",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": true,
                        "title": "FASE 3. DESARROLLO ITERATIVO CORE",
                        "dates": "07 sep - 08 oct",
                        "dateStart": "2026-09-07",
                        "dateEnd": "2026-10-08",
                        "durationDays": 24,
                        "durationHours": 192,
                        "durationLabel": "24 d (192h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo de Proyecto SIGE",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Fase Resumen",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "17",
                        "predecessorCodes": "EDT 2.7",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Código Fuente del Sistema SIGE Completo (Node.js + Express v5 + React + Vite)",
                        "description": "Construcción iterativa de los 4 Sprints en 24 días laborables netos (192 horas hábiles), culminando el jueves 08 de octubre previo al feriado nacional del 9 de octubre.",
                        "subtasks": [
                                    {
                                                "text": "Sprint 1: Infraestructura y Auth JWT",
                                                "done": true
                                    },
                                    {
                                                "text": "Sprint 2: Wizard y Editor TipTap",
                                                "done": true
                                    },
                                    {
                                                "text": "Sprint 3: Matriz de actividades y MinIO S3",
                                                "done": true
                                    },
                                    {
                                                "text": "Sprint 4: Comité, IA local y Exportación PDF/Word",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-1",
                        "rowId": 19,
                        "code": "3.1",
                        "edtCode": "EDT 3.1",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Implementación de tablas, índices y scripts DDL PostgreSQL 18",
                        "dates": "07 sep - 10 sep",
                        "dateStart": "2026-09-07",
                        "dateEnd": "2026-09-10",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH",
                        "assigneeName": "Nixon Hurtado (Backend / DBA)",
                        "avatarColor": "bg-indigo-600",
                        "tag": "PostgreSQL 18 / DB",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "17",
                        "predecessorCodes": "EDT 2.7",
                        "isParallel": true,
                        "parallelWith": "EDT 3.4",
                        "parallelReason": "Lunes 07 a Jueves 10 de septiembre. El Backend modela el esquema PostgreSQL 18 mientras el Frontend levanta el cliente base React + Vite.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Esquema DDL inicial y scripts de inicialización en PostgreSQL 18 (schema.sql, init.js)",
                        "description": "Definición de tablas, índices relacionales y pool de conexiones pg en PostgreSQL 18 con restricciones de integridad.",
                        "subtasks": [
                                    {
                                                "text": "Mapeo de DbContext con 13 entidades del dominio",
                                                "done": true
                                    },
                                    {
                                                "text": "Ejecución de Add-Migration e índices de optimización",
                                                "done": true
                                    },
                                    {
                                                "text": "Prueba de integridad referencial en PostgreSQL",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-2",
                        "rowId": 20,
                        "code": "3.2",
                        "edtCode": "EDT 3.2",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Datos iniciales y catálogos institucionales",
                        "dates": "10 sep - 14 sep",
                        "dateStart": "2026-09-10",
                        "dateEnd": "2026-09-14",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "NH",
                        "assigneeName": "Nixon Hurtado (Backend / DBA)",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Seeders",
                        "tagColor": "bg-indigo-500/20 text-indigo-300 border-indigo-500/30",
                        "predecessors": "19",
                        "predecessorCodes": "EDT 3.1",
                        "isParallel": true,
                        "parallelWith": "EDT 3.4",
                        "parallelReason": "Jueves 10, Viernes 11 y Lunes 14 de septiembre (3 días laborables). Carga de datos mientras avanza el frontend.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "DbInitializer con usuarios y catálogos institucionales",
                        "description": "Inyección de carreras FISEI, roles institucionales, catálogo de actividades típicas y usuario administrador inicial.",
                        "subtasks": [
                                    {
                                                "text": "Poblado de carreras y unidades académicas FISEI",
                                                "done": true
                                    },
                                    {
                                                "text": "Inserción de roles y permisos del SGC",
                                                "done": true
                                    },
                                    {
                                                "text": "Carga de catálogo estándar de actividades de docencia y APE",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-3",
                        "rowId": 21,
                        "code": "3.3",
                        "edtCode": "EDT 3.3",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Autenticación y autorización de usuarios",
                        "dates": "09 sep - 14 sep",
                        "dateStart": "2026-09-09",
                        "dateEnd": "2026-09-14",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Auth JWT",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "19",
                        "predecessorCodes": "EDT 3.1",
                        "isParallel": true,
                        "parallelWith": "EDT 3.4",
                        "parallelReason": "Miércoles 09 a Lunes 14 de septiembre (4 días hábiles netos). Desarrollo de seguridad en paralelo con el frontend.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Auth Endpoints con JWT y decoradores [Authorize(Roles=...)]",
                        "description": "Servicio de emisión de tokens JWT firmados con HMAC-SHA256, Refresh Tokens, caducidad y políticas de acceso por rol.",
                        "subtasks": [
                                    {
                                                "text": "Controlador AuthController (Login, Refresh, Me)",
                                                "done": true
                                    },
                                    {
                                                "text": "Middleware de manejo global de excepciones y claims",
                                                "done": true
                                    },
                                    {
                                                "text": "Políticas de autorización por rol institucional",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-4",
                        "rowId": 22,
                        "code": "3.4",
                        "edtCode": "EDT 3.4",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Cliente base y diseño de layouts",
                        "dates": "08 sep - 14 sep",
                        "dateStart": "2026-09-08",
                        "dateEnd": "2026-09-14",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "AV",
                        "assigneeName": "Andrea Vasquez (Frontend / QA)",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Frontend Base",
                        "tagColor": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
                        "predecessors": "17",
                        "predecessorCodes": "EDT 2.7",
                        "isParallel": true,
                        "parallelWith": "EDT 3.1, 3.2, 3.3",
                        "parallelReason": "Martes 08 a Lunes 14 de septiembre (5 días hábiles netos). Desarrollo frontend base en paralelo con la infraestructura backend del Sprint 1.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "SPA SIGE Frontend (React + Vite) funcional con navegación y rutas",
                        "description": "Inicialización de Vite, Tailwind CSS, sistema de tokens de color UTA, componentes de navegación y consumo de API con Axios.",
                        "subtasks": [
                                    {
                                                "text": "Configuración de TypeScript, ESLint y Tailwind CSS",
                                                "done": true
                                    },
                                    {
                                                "text": "Rutas protegidas con React Router DOM",
                                                "done": true
                                    },
                                    {
                                                "text": "Componentes de Header, Sidebar y Login institucional",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-5",
                        "rowId": 23,
                        "code": "3.5",
                        "edtCode": "EDT 3.5",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Layout del Wizard modular en pestañas",
                        "dates": "15 sep - 18 sep",
                        "dateStart": "2026-09-15",
                        "dateEnd": "2026-09-18",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "AV",
                        "assigneeName": "Andrea Vasquez (Frontend / QA)",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Wizard UI",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "22",
                        "predecessorCodes": "EDT 3.4",
                        "isParallel": true,
                        "parallelWith": "EDT 3.7",
                        "parallelReason": "Martes 15 a Viernes 18 de septiembre en paralelo con los endpoints de persistencia.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "PlanEditorWizard.tsx modular con navegación por pasos",
                        "description": "Componente asistente paso a paso: Datos Informativos, Justificación, Matriz, Anexos y Cascada de Firmas.",
                        "subtasks": [
                                    {
                                                "text": "Estructura de pestañas con estado local en React",
                                                "done": true
                                    },
                                    {
                                                "text": "Validación de avance entre pasos obligatorios",
                                                "done": true
                                    },
                                    {
                                                "text": "Indicador de completitud porcentual del documento",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-6",
                        "rowId": 24,
                        "code": "3.6",
                        "edtCode": "EDT 3.6",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Integración del Editor TipTap con autoguardado debounce",
                        "dates": "17 sep - 22 sep",
                        "dateStart": "2026-09-17",
                        "dateEnd": "2026-09-22",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "AV",
                        "assigneeName": "Andrea Vasquez (Frontend / QA)",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Editor TipTap",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "23",
                        "predecessorCodes": "EDT 3.5",
                        "isParallel": true,
                        "parallelWith": "EDT 3.7",
                        "parallelReason": "Jueves 17, Viernes 18, Lunes 21 y Martes 22 de septiembre (4 días hábiles netos).",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "RichTextEditor con autoguardado y formato HTML limpio",
                        "description": "Editor de texto enriquecido con extensiones de formato y guardado asíncrono con debounce de 1.5s.",
                        "subtasks": [
                                    {
                                                "text": "Configurar TipTap con extensiones requeridas",
                                                "done": true
                                    },
                                    {
                                                "text": "Implementar hook useDebounce para autoguardado",
                                                "done": true
                                    },
                                    {
                                                "text": "Manejo de estado 'Guardando...' y 'Guardado' en tiempo real",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-7",
                        "rowId": 25,
                        "code": "3.7",
                        "edtCode": "EDT 3.7",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Endpoints de persistencia de secciones y documentos",
                        "dates": "15 sep - 22 sep",
                        "dateStart": "2026-09-15",
                        "dateEnd": "2026-09-22",
                        "durationDays": 6,
                        "durationHours": 48,
                        "durationLabel": "6 d (48h)",
                        "assignee": "NH",
                        "assigneeName": "Nixon Hurtado (Backend / DBA)",
                        "avatarColor": "bg-indigo-600",
                        "tag": "WebAPI REST",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "21",
                        "predecessorCodes": "EDT 3.3",
                        "isParallel": true,
                        "parallelWith": "EDT 3.5, 3.6",
                        "parallelReason": "Martes 15 a Martes 22 de septiembre (6 días hábiles netos). El backend crea los controladores mientras el frontend diseña las vistas.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Controladores RESTful Express v5 (documentos.controller.js y secciones.controller.js)",
                        "description": "Controladores RESTful en Node.js + Express (v5) para CRUD de planes e informes, versionamiento y guardado atómico con transacciones PostgreSQL.",
                        "subtasks": [
                                    {
                                                "text": "POST /api/documentos (Creación de borrador)",
                                                "done": true
                                    },
                                    {
                                                "text": "PUT /api/documentos/{id}/secciones (Persistencia de contenido)",
                                                "done": true
                                    },
                                    {
                                                "text": "GET /api/documentos/mis-documentos con filtros",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-8",
                        "rowId": 26,
                        "code": "3.8",
                        "edtCode": "EDT 3.8",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "HITO 3: Sprint 2 Review: Wizard y Persistencia Operativa",
                        "dates": "22 sep",
                        "dateStart": "2026-09-22",
                        "dateEnd": "2026-09-22",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito Sprint",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "24, 25",
                        "predecessorCodes": "EDT 3.6, EDT 3.7",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "Demostración funcional de Wizard con autoguardado en DB",
                        "description": "Hito de cierre de Sprint 2 el martes 22 de septiembre de 2026.",
                        "subtasks": [
                                    {
                                                "text": "Demostración de autoguardado sin recargar página",
                                                "done": true
                                    },
                                    {
                                                "text": "Verificación de datos en base de datos PostgreSQL",
                                                "done": true
                                    },
                                    {
                                                "text": "Aprobación de Sprint 2 por el equipo",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-9",
                        "rowId": 27,
                        "code": "3.9",
                        "edtCode": "EDT 3.9",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Desarrollo de la Matriz Dinámica de Actividades",
                        "dates": "23 sep - 29 sep",
                        "dateStart": "2026-09-23",
                        "dateEnd": "2026-09-29",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "AV",
                        "assigneeName": "Andrea Vasquez (Frontend / QA)",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Matriz UI",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "26",
                        "predecessorCodes": "EDT 3.8",
                        "isParallel": true,
                        "parallelWith": "EDT 3.10",
                        "parallelReason": "Miércoles 23 a Martes 29 de septiembre (5 días hábiles netos). En paralelo con las reglas en backend.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Componente MatrizActividadesTable.tsx interactivo",
                        "description": "Tabla interactiva que reproduce la Tabla 1 del formato SGC con cálculo automático de avance.",
                        "subtasks": [
                                    {
                                                "text": "Agregar, editar y eliminar actividades dinámicamente",
                                                "done": true
                                    },
                                    {
                                                "text": "Suma automática de ponderaciones para validar 100%",
                                                "done": true
                                    },
                                    {
                                                "text": "Cálculo ponderado del avance global del documento",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-10",
                        "rowId": 28,
                        "code": "3.10",
                        "edtCode": "EDT 3.10",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Reglas de negocio y Validation Gates con Middlewares Express v5",
                        "dates": "23 sep - 29 sep",
                        "dateStart": "2026-09-23",
                        "dateEnd": "2026-09-29",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Validation Gates",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "26",
                        "predecessorCodes": "EDT 3.8",
                        "isParallel": true,
                        "parallelWith": "EDT 3.9",
                        "parallelReason": "Miércoles 23 a Martes 29 de septiembre (5 días hábiles netos) en paralelo con la interfaz de la matriz.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Middlewares de validación y reglas de negocio para documentos y actividades (validation.middleware.js)",
                        "description": "Implementación estricta de Validation Gates en Express v5 para bloqueo preventivo si falta evidencia o justificación.",
                        "subtasks": [
                                    {
                                                "text": "Validador DocumentoValidator con reglas SGC",
                                                "done": true
                                    },
                                    {
                                                "text": "Validador ActividadMatrizValidator con chequeo de fechas",
                                                "done": true
                                    },
                                    {
                                                "text": "Mensajes de error semánticos devueltos al frontend",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-11",
                        "rowId": 29,
                        "code": "3.11",
                        "edtCode": "EDT 3.11",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Integración de MinIO S3 para evidencias y URLs prefirmadas",
                        "dates": "25 sep - 30 sep",
                        "dateStart": "2026-09-25",
                        "dateEnd": "2026-09-30",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH, AV",
                        "assigneeName": "Nixon Hurtado / Andrea Vasquez",
                        "avatarColor": "bg-indigo-600",
                        "tag": "MinIO S3",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "28",
                        "predecessorCodes": "EDT 3.10",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "MinioStorageService.cs y componente de upload de evidencias",
                        "description": "Viernes 25, Lunes 28, Martes 29 y Miércoles 30 de septiembre (4 días hábiles netos). Servicio seguro de almacenamiento.",
                        "subtasks": [
                                    {
                                                "text": "Subida en streaming con comprobación de tamaño máximo",
                                                "done": true
                                    },
                                    {
                                                "text": "Cálculo y guardado de hash SHA-256 inmutable",
                                                "done": true
                                    },
                                    {
                                                "text": "Generación de URLs de descarga segura con expiración de 60 min",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-12",
                        "rowId": 30,
                        "code": "3.12",
                        "edtCode": "EDT 3.12",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "HITO 4: Sprint 3 Review: Matriz Dinámica y Evidencias MinIO",
                        "dates": "30 sep",
                        "dateStart": "2026-09-30",
                        "dateEnd": "2026-09-30",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito Sprint",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "27, 29",
                        "predecessorCodes": "EDT 3.9, EDT 3.11",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "Demostración funcional de matriz con evidencias MinIO",
                        "description": "Hito de cierre de Sprint 3 el miércoles 30 de septiembre de 2026.",
                        "subtasks": [
                                    {
                                                "text": "Prueba de subida de PDF con hash SHA-256",
                                                "done": true
                                    },
                                    {
                                                "text": "Intento de envío sin evidencia para verificar bloqueo",
                                                "done": true
                                    },
                                    {
                                                "text": "Aprobación de Sprint 3 por el equipo",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-13",
                        "rowId": 31,
                        "code": "3.13",
                        "edtCode": "EDT 3.13",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Módulo de Revisión, Observaciones y Cascada de Firmas",
                        "dates": "01 oct - 07 oct",
                        "dateStart": "2026-10-01",
                        "dateEnd": "2026-10-07",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "AV, NH",
                        "assigneeName": "Andrea Vasquez / Nixon Hurtado",
                        "avatarColor": "bg-emerald-600",
                        "tag": "Firmas Cascada",
                        "tagColor": "bg-indigo-500/20 text-indigo-300 border-indigo-500/30",
                        "predecessors": "30",
                        "predecessorCodes": "EDT 3.12",
                        "isParallel": true,
                        "parallelWith": "EDT 3.14",
                        "parallelReason": "Jueves 01 al Miércoles 07 de octubre (5 días hábiles netos). En paralelo con el módulo ortográfico de IA.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Panel de Comité y servicio de Firmas multinivel",
                        "description": "Panel para Coordinadores de Área y de Carrera: observaciones granulares y legalización de firmas en cascada.",
                        "subtasks": [
                                    {
                                                "text": "Panel de revisión con estado 'En Revisión'",
                                                "done": true
                                    },
                                    {
                                                "text": "Marcado y solución de observaciones por sección",
                                                "done": true
                                    },
                                    {
                                                "text": "Circuito de 3 firmas consecutivas con sellado criptográfico",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-14",
                        "rowId": 32,
                        "code": "3.14",
                        "edtCode": "EDT 3.14",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Capa de asistencia y corrección ortográfica local",
                        "dates": "02 oct - 07 oct",
                        "dateStart": "2026-10-02",
                        "dateEnd": "2026-10-07",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST, AV",
                        "assigneeName": "Steeven Toala / Andrea Vasquez",
                        "avatarColor": "bg-amber-600",
                        "tag": "IA LanguageTool",
                        "tagColor": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
                        "predecessors": "30",
                        "predecessorCodes": "EDT 3.12",
                        "isParallel": true,
                        "parallelWith": "EDT 3.13",
                        "parallelReason": "Viernes 02 al Miércoles 07 de octubre (4 días hábiles netos) en paralelo con el módulo de comité.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Servicio local de corrección gramatical y ortográfica",
                        "description": "Conexión desde el frontend con el microservicio LanguageTool en Docker para sugerir correcciones en tiempo real.",
                        "subtasks": [
                                    {
                                                "text": "Consumo de API /v2/check de LanguageTool",
                                                "done": true
                                    },
                                    {
                                                "text": "Resaltado visual de errores en el editor TipTap",
                                                "done": true
                                    },
                                    {
                                                "text": "Pop-up de reemplazo de palabra con un clic",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-15",
                        "rowId": 33,
                        "code": "3.15",
                        "edtCode": "EDT 3.15",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "Motor de exportación oficial en PDF y Word",
                        "dates": "05 oct - 08 oct",
                        "dateStart": "2026-10-05",
                        "dateEnd": "2026-10-08",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Exportación SGC",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "31",
                        "predecessorCodes": "EDT 3.13",
                        "isParallel": true,
                        "parallelWith": "EDT 3.14",
                        "parallelReason": "Lunes 05 a Jueves 08 de octubre (4 días hábiles netos). Concluye justo antes del feriado nacional del viernes 09 de octubre.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "DocumentExportService.cs con salidas idénticas al SGC",
                        "description": "Generación de archivos PDF y Word idénticos al formato oficial UTA-SGC-A-2-1-P7-T1 y T2.",
                        "subtasks": [
                                    {
                                                "text": "Plantilla de cabeceras, logos oficiales y numeración SGC",
                                                "done": true
                                    },
                                    {
                                                "text": "Renderizado de matriz de actividades con anchos de celda fijos",
                                                "done": true
                                    },
                                    {
                                                "text": "Incrustación de códigos QR de verificación digital",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-3-16",
                        "rowId": 34,
                        "code": "3.16",
                        "edtCode": "EDT 3.16",
                        "phase": "fase3",
                        "phaseName": "FASE 3: DESARROLLO ITERATIVO CORE",
                        "isSummary": false,
                        "title": "HITO 5: Sistema Core Completado",
                        "dates": "08 oct",
                        "dateStart": "2026-10-08",
                        "dateEnd": "2026-10-08",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito de Fase",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "31, 32, 33",
                        "predecessorCodes": "EDT 3.13, EDT 3.14, EDT 3.15",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "Versión funcional v0.9 con todas las funciones del SRS",
                        "description": "Hito de congelamiento de código (Code Freeze) el jueves 08 de octubre de 2026, previo al feriado nacional del viernes 9 de octubre (Independencia de Guayaquil).",
                        "subtasks": [
                                    {
                                                "text": "Cierre de Pull Requests de funcionalidades principales",
                                                "done": true
                                    },
                                    {
                                                "text": "Generación de tag Git 'v0.9-beta-freeze'",
                                                "done": true
                                    },
                                    {
                                                "text": "Revisión general de cobertura con Ing. Paulo Torres",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-0",
                        "rowId": 35,
                        "code": "4",
                        "edtCode": "EDT 4.0",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": true,
                        "title": "FASE 4. PRUEBAS QA, SEGURIDAD E INTEGRACIÓN",
                        "dates": "12 oct - 23 oct",
                        "dateStart": "2026-10-12",
                        "dateEnd": "2026-10-23",
                        "durationDays": 10,
                        "durationHours": 80,
                        "durationLabel": "10 d (80h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo de Proyecto SIGE",
                        "avatarColor": "bg-amber-600",
                        "tag": "Fase Resumen",
                        "tagColor": "bg-amber-500/20 text-amber-300 border-amber-500/30",
                        "predecessors": "34",
                        "predecessorCodes": "EDT 3.16",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Informe de QA, Casos de Prueba y Release Candidate v1.0-RC",
                        "description": "Fase exhaustiva de QA en exactamente 10 días hábiles netos (80 horas), iniciando el lunes 12 de octubre tras el feriado nacional del 9 de octubre.",
                        "subtasks": [
                                    {
                                                "text": "Pruebas unitarias con cobertura > 80%",
                                                "done": true
                                    },
                                    {
                                                "text": "Pruebas de seguridad e inyección SQL/XSS",
                                                "done": true
                                    },
                                    {
                                                "text": "Pruebas de extremo a extremo y versión Release Candidate",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-1",
                        "rowId": 36,
                        "code": "4.1",
                        "edtCode": "EDT 4.1",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Pruebas unitarias en backend",
                        "dates": "12 oct - 15 oct",
                        "dateStart": "2026-10-12",
                        "dateEnd": "2026-10-15",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH, ST",
                        "assigneeName": "Nixon Hurtado / Steeven Toala",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Unit Tests",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "34",
                        "predecessorCodes": "EDT 3.16",
                        "isParallel": true,
                        "parallelWith": "EDT 4.3",
                        "parallelReason": "Lunes 12 a Jueves 15 de octubre. Backend corre pruebas unitarias mientras Frontend realiza pruebas de UI/UX.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Proyecto SIGE.Tests con 45 pruebas unitarias automatizadas",
                        "description": "Automatización de pruebas unitarias para controladores, servicios de ponderación y Validation Gates.",
                        "subtasks": [
                                    {
                                                "text": "Pruebas unitarias de cálculo matemático de ponderaciones",
                                                "done": true
                                    },
                                    {
                                                "text": "Mocks de repositorio y MinIO con la librería Moq",
                                                "done": true
                                    },
                                    {
                                                "text": "Reporte de cobertura de código con Coverlet",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-2",
                        "rowId": 37,
                        "code": "4.2",
                        "edtCode": "EDT 4.2",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Pruebas de integración y seguridad",
                        "dates": "13 oct - 16 oct",
                        "dateStart": "2026-10-13",
                        "dateEnd": "2026-10-16",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "ST, NH",
                        "assigneeName": "Steeven Toala / Nixon Hurtado",
                        "avatarColor": "bg-amber-600",
                        "tag": "Seguridad",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "34",
                        "predecessorCodes": "EDT 3.16",
                        "isParallel": true,
                        "parallelWith": "EDT 4.1, 4.3",
                        "parallelReason": "Martes 13 a Viernes 16 de octubre (4 días hábiles netos). Pruebas de seguridad simultáneas.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Informe de Auditoría de Seguridad y Pentesting OWASP",
                        "description": "Validación de expiración de tokens, sanitización de inputs contra XSS y prevención de SQL Injection.",
                        "subtasks": [
                                    {
                                                "text": "Escaneo de vulnerabilidades con herramientas de análisis estático",
                                                "done": true
                                    },
                                    {
                                                "text": "Pruebas de escalación de privilegios cambiando claims de rol",
                                                "done": true
                                    },
                                    {
                                                "text": "Verificación de encabezados de seguridad HTTP",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-3",
                        "rowId": 38,
                        "code": "4.3",
                        "edtCode": "EDT 4.3",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Pruebas de interfaz UI/UX, responsive y accesibilidad",
                        "dates": "12 oct - 19 oct",
                        "dateStart": "2026-10-12",
                        "dateEnd": "2026-10-19",
                        "durationDays": 6,
                        "durationHours": 48,
                        "durationLabel": "6 d (48h)",
                        "assignee": "AV, HV",
                        "assigneeName": "Andrea Vasquez / Heidy Villavicencio",
                        "avatarColor": "bg-emerald-600",
                        "tag": "QA Frontend",
                        "tagColor": "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
                        "predecessors": "34",
                        "predecessorCodes": "EDT 3.16",
                        "isParallel": true,
                        "parallelWith": "EDT 4.1, 4.2",
                        "parallelReason": "Lunes 12 a Lunes 19 de octubre (6 días hábiles netos, pausando el fin de semana del 17-18 oct).",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Matriz de Compatibilidad Cross-Browser y Accesibilidad",
                        "description": "Verificación en Chrome, Firefox, Edge y pantallas móviles. Cumplimiento de estándares WCAG 2.1.",
                        "subtasks": [
                                    {
                                                "text": "Pruebas de diseño responsivo en resoluciones de 375px a 1920px",
                                                "done": true
                                    },
                                    {
                                                "text": "Validación de contraste y lectura accesible en modo oscuro",
                                                "done": true
                                    },
                                    {
                                                "text": "Pruebas de rendimiento Lighthouse (score > 90 en Performance)",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-4",
                        "rowId": 39,
                        "code": "4.4",
                        "edtCode": "EDT 4.4",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Pruebas de flujo extremo a extremo",
                        "dates": "16 oct - 22 oct",
                        "dateStart": "2026-10-16",
                        "dateEnd": "2026-10-22",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "AV, ST",
                        "assigneeName": "Andrea Vasquez / Steeven Toala",
                        "avatarColor": "bg-emerald-600",
                        "tag": "E2E Testing",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "36, 37",
                        "predecessorCodes": "EDT 4.1, EDT 4.2",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Casos de Prueba E2E Ejecutados y Certificado de Calidad",
                        "description": "Viernes 16, Lunes 19, Martes 20, Miércoles 21 y Jueves 22 de octubre (5 días hábiles netos).",
                        "subtasks": [
                                    {
                                                "text": "Caso de prueba de flujo feliz (Aprobación sin observaciones)",
                                                "done": true
                                    },
                                    {
                                                "text": "Caso de prueba de rechazo y corrección de observaciones",
                                                "done": true
                                    },
                                    {
                                                "text": "Caso de prueba de habilitación extemporánea por el Administrador",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-5",
                        "rowId": 40,
                        "code": "4.5",
                        "edtCode": "EDT 4.5",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Pruebas de carga y estrés concurrente en MinIO y PDF",
                        "dates": "19 oct - 22 oct",
                        "dateStart": "2026-10-19",
                        "dateEnd": "2026-10-22",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH",
                        "assigneeName": "Nixon Hurtado (Backend / DBA)",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Estrés / Carga",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "37",
                        "predecessorCodes": "EDT 4.2",
                        "isParallel": true,
                        "parallelWith": "EDT 4.4",
                        "parallelReason": "Lunes 19 a Jueves 22 de octubre (4 días hábiles netos) en paralelo con las pruebas E2E.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Reporte de Pruebas de Carga y Tiempos de Respuesta",
                        "description": "Simulación de accesos concurrentes de 50 docentes subiendo evidencias pesadas simultáneamente.",
                        "subtasks": [
                                    {
                                                "text": "Pruebas de carga con 50 peticiones simultáneas a MinIO",
                                                "done": true
                                    },
                                    {
                                                "text": "Medición de uso de memoria RAM y CPU en el contenedor PostgreSQL 18",
                                                "done": true
                                    },
                                    {
                                                "text": "Validación de estabilidad sin caídas del servicio",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-6",
                        "rowId": 41,
                        "code": "4.6",
                        "edtCode": "EDT 4.6",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "Corrección de bugs y versión Release Candidate",
                        "dates": "21 oct - 23 oct",
                        "dateStart": "2026-10-21",
                        "dateEnd": "2026-10-23",
                        "durationDays": 3,
                        "durationHours": 24,
                        "durationLabel": "3 d (24h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE (Completo)",
                        "avatarColor": "bg-red-600",
                        "tag": "Estabilización",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "39, 40",
                        "predecessorCodes": "EDT 4.4, EDT 4.5",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Versión candidata a producción v1.0-RC lista para despliegue",
                        "description": "Miércoles 21 a Viernes 23 de octubre (3 días hábiles netos). Resolución de incidencias y congelamiento de versión Release Candidate.",
                        "subtasks": [
                                    {
                                                "text": "Resolución de tickets de ajuste visual y validación",
                                                "done": true
                                    },
                                    {
                                                "text": "Generación de tag Git 'v1.0-RC'",
                                                "done": true
                                    },
                                    {
                                                "text": "Verificación de suite de tests en verde al 100%",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-4-7",
                        "rowId": 42,
                        "code": "4.7",
                        "edtCode": "EDT 4.7",
                        "phase": "fase4",
                        "phaseName": "FASE 4: PRUEBAS QA Y SEGURIDAD",
                        "isSummary": false,
                        "title": "HITO 6: Aceptación de QA y Release Candidate v1.0-RC",
                        "dates": "23 oct",
                        "dateStart": "2026-10-23",
                        "dateEnd": "2026-10-23",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito de Fase",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "41",
                        "predecessorCodes": "EDT 4.6",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "Acta de Certificación de Pruebas y Aprobación de QA",
                        "description": "Hito formal de aprobación de calidad y auditoría el viernes 23 de octubre de 2026.",
                        "subtasks": [
                                    {
                                                "text": "Revisión del informe de pruebas con Ing. Paulo Torres",
                                                "done": true
                                    },
                                    {
                                                "text": "Firma de aprobación de criterios de aceptación de QA",
                                                "done": true
                                    },
                                    {
                                                "text": "Autorización formal de despliegue en servidor",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-0",
                        "rowId": 43,
                        "code": "5",
                        "edtCode": "EDT 5.0",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": true,
                        "title": "FASE 5. DESPLIEGUE FINAL, CAPACITACIÓN Y CIERRE",
                        "dates": "26 oct - 30 oct",
                        "dateStart": "2026-10-26",
                        "dateEnd": "2026-10-30",
                        "durationDays": 5,
                        "durationHours": 40,
                        "durationLabel": "5 d (40h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo de Proyecto SIGE",
                        "avatarColor": "bg-purple-600",
                        "tag": "Fase Resumen",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "42",
                        "predecessorCodes": "EDT 4.7",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Sistema en Producción, Manuales y Acta de Cierre Firmada",
                        "description": "Semana final de 5 días hábiles exactos (Lunes 26 a Viernes 30 de octubre de 2026 | 40 horas). Cierre formal previo a los asuetos de noviembre en Ambato.",
                        "subtasks": [
                                    {
                                                "text": "Despliegue de producción con Docker y SSL",
                                                "done": true
                                    },
                                    {
                                                "text": "Elaboración de manuales técnicos y de usuario",
                                                "done": true
                                    },
                                    {
                                                "text": "Capacitación institucional y Acta de Cierre",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-1",
                        "rowId": 44,
                        "code": "5.1",
                        "edtCode": "EDT 5.1",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "Configuración de entorno de producción VPS Linux y Docker",
                        "dates": "26 oct - 27 oct",
                        "dateStart": "2026-10-26",
                        "dateEnd": "2026-10-27",
                        "durationDays": 2,
                        "durationHours": 16,
                        "durationLabel": "2 d (16h)",
                        "assignee": "ST",
                        "assigneeName": "Steeven Toala (Líder / Arquitecto)",
                        "avatarColor": "bg-amber-600",
                        "tag": "Producción",
                        "tagColor": "bg-purple-500/20 text-purple-300 border-purple-500/30",
                        "predecessors": "42",
                        "predecessorCodes": "EDT 4.7",
                        "isParallel": true,
                        "parallelWith": "EDT 5.3",
                        "parallelReason": "Lunes 26 y Martes 27 de octubre en paralelo con la redacción de manuales de usuario.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Servidor VPS Linux en línea con stack Docker de producción",
                        "description": "Aprovisionamiento de servidor Linux con Docker Compose, Nginx Proxy Inverso y políticas UFW.",
                        "subtasks": [
                                    {
                                                "text": "Configurar cortafuegos y puertos seguros (80, 443)",
                                                "done": true
                                    },
                                    {
                                                "text": "Despliegue de contenedores PostgreSQL 18 y MinIO productivos",
                                                "done": true
                                    },
                                    {
                                                "text": "Configuración de reinicio automático 'always' en Docker",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-2",
                        "rowId": 45,
                        "code": "5.2",
                        "edtCode": "EDT 5.2",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "Aseguramiento de dominio, SSL HTTPS Let's Encrypt y SMTP",
                        "dates": "27 oct - 28 oct",
                        "dateStart": "2026-10-27",
                        "dateEnd": "2026-10-28",
                        "durationDays": 2,
                        "durationHours": 16,
                        "durationLabel": "2 d (16h)",
                        "assignee": "ST",
                        "assigneeName": "Steeven Toala (Líder / Arquitecto)",
                        "avatarColor": "bg-amber-600",
                        "tag": "Dominio & SSL",
                        "tagColor": "bg-indigo-500/20 text-indigo-300 border-indigo-500/30",
                        "predecessors": "44",
                        "predecessorCodes": "EDT 5.1",
                        "isParallel": true,
                        "parallelWith": "EDT 5.3, 5.4",
                        "parallelReason": "Martes 27 y Miércoles 28 de octubre en paralelo con los manuales técnicos.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Dominio institucional con candado verde HTTPS y correo SMTP",
                        "description": "Emisión e instalación de certificado SSL Let's Encrypt y servicio SMTP para notificaciones.",
                        "subtasks": [
                                    {
                                                "text": "Configurar DNS y certificado SSL con Certbot",
                                                "done": true
                                    },
                                    {
                                                "text": "Prueba de envío de correos transaccionales de notificación",
                                                "done": true
                                    },
                                    {
                                                "text": "Verificación de redirección forzosa de HTTP a HTTPS",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-3",
                        "rowId": 46,
                        "code": "5.3",
                        "edtCode": "EDT 5.3",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "Elaboración de manuales de usuario por rol",
                        "dates": "26 oct - 29 oct",
                        "dateStart": "2026-10-26",
                        "dateEnd": "2026-10-29",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "HV",
                        "assigneeName": "Heidy Villavicencio (Analista / UI-UX)",
                        "avatarColor": "bg-blue-600",
                        "tag": "Manual Usuario",
                        "tagColor": "bg-blue-500/20 text-blue-300 border-blue-500/30",
                        "predecessors": "42",
                        "predecessorCodes": "EDT 4.7",
                        "isParallel": true,
                        "parallelWith": "EDT 5.1, 5.2",
                        "parallelReason": "Lunes 26 a Jueves 29 de octubre (4 días hábiles netos) en paralelo con el despliegue en servidor.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Manual de Usuario Oficial del Sistema SIGE (PDF / Web)",
                        "description": "Guía pedagógica paso a paso con capturas de pantalla para Docente Elaborador, Coordinadores de Área y Administrador SGC.",
                        "subtasks": [
                                    {
                                                "text": "Módulo 1: Elaboración y carga de evidencias para docentes",
                                                "done": true
                                    },
                                    {
                                                "text": "Módulo 2: Panel de revisión y firmas para comités",
                                                "done": true
                                    },
                                    {
                                                "text": "Módulo 3: Administración y desbloqueo extemporáneo",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-4",
                        "rowId": 47,
                        "code": "5.4",
                        "edtCode": "EDT 5.4",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "Elaboración de Manual Técnico, API y BD y Plan de Contingencias",
                        "dates": "27 oct - 30 oct",
                        "dateStart": "2026-10-27",
                        "dateEnd": "2026-10-30",
                        "durationDays": 4,
                        "durationHours": 32,
                        "durationLabel": "4 d (32h)",
                        "assignee": "NH",
                        "assigneeName": "Nixon Hurtado (Backend / DBA)",
                        "avatarColor": "bg-indigo-600",
                        "tag": "Manual Técnico",
                        "tagColor": "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
                        "predecessors": "42",
                        "predecessorCodes": "EDT 4.7",
                        "isParallel": true,
                        "parallelWith": "EDT 5.2, 5.3",
                        "parallelReason": "Martes 27 a Viernes 30 de octubre (4 días hábiles netos). Documentación técnica y backups en paralelo.",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Manual Técnico de Despliegue, Mantenimiento y Backups",
                        "description": "Documentación de arquitectura, endpoints Swagger, scripts de backups y plan de contingencia.",
                        "subtasks": [
                                    {
                                                "text": "Documentar endpoints REST y esquema Swagger OpenAPI",
                                                "done": true
                                    },
                                    {
                                                "text": "Script automatizado de copias de seguridad de PostgreSQL 18 y MinIO",
                                                "done": true
                                    },
                                    {
                                                "text": "Plan de recuperación ante desastres (Disaster Recovery Plan)",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-5",
                        "rowId": 48,
                        "code": "5.5",
                        "edtCode": "EDT 5.5",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "Capacitación a usuarios, sustentación y firma de Acta de Cierre",
                        "dates": "29 oct - 30 oct",
                        "dateStart": "2026-10-29",
                        "dateEnd": "2026-10-30",
                        "durationDays": 2,
                        "durationHours": 16,
                        "durationLabel": "2 d (16h)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE (Completo)",
                        "avatarColor": "bg-red-600",
                        "tag": "Cierre Proyecto",
                        "tagColor": "bg-red-500/20 text-red-300 border-red-500/30",
                        "predecessors": "45, 46, 47",
                        "predecessorCodes": "EDT 5.2, EDT 5.3, EDT 5.4",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": false,
                        "percentDone": 100,
                        "deliverable": "Acta de Entrega-Recepción y Capacitación Docente",
                        "description": "Jueves 29 y Viernes 30 de octubre (2 días hábiles netos). Taller de capacitación y firma formal del Acta de Cierre.",
                        "subtasks": [
                                    {
                                                "text": "Taller de socialización con docentes de la carrera",
                                                "done": true
                                    },
                                    {
                                                "text": "Presentación de resultados e informe final de alcance",
                                                "done": true
                                    },
                                    {
                                                "text": "Firma formal del Acta de Cierre con autoridades",
                                                "done": true
                                    }
                        ]
            },
            {
                        "id": "edt-5-6",
                        "rowId": 49,
                        "code": "5.6",
                        "edtCode": "EDT 5.6",
                        "phase": "fase5",
                        "phaseName": "FASE 5: DESPLIEGUE FINAL Y CIERRE",
                        "isSummary": false,
                        "title": "HITO 7: Cierre Formal del Proyecto y Sistema en Producción",
                        "dates": "30 oct",
                        "dateStart": "2026-10-30",
                        "dateEnd": "2026-10-30",
                        "durationDays": 0,
                        "durationHours": 0,
                        "durationLabel": "0 d (Hito)",
                        "assignee": "Equipo",
                        "assigneeName": "Equipo SIGE / Ing. Paulo Torres",
                        "avatarColor": "bg-slate-900",
                        "tag": "Hito Final",
                        "tagColor": "bg-yellow-500/20 text-yellow-300 border-yellow-500/30",
                        "predecessors": "48",
                        "predecessorCodes": "EDT 5.5",
                        "isParallel": false,
                        "parallelWith": "",
                        "parallelReason": "",
                        "isMilestone": true,
                        "percentDone": 100,
                        "deliverable": "Sistema SIGE Oficialmente Operativo en Producción",
                        "description": "Cierre formal el viernes 30 de octubre de 2026 (57 días laborables netos / 456 horas hábiles). Sistema 100% operativo en la FISEI UTA.",
                        "subtasks": [
                                    {
                                                "text": "Entrega final del repositorio con tag 'v1.0-release'",
                                                "done": true
                                    },
                                    {
                                                "text": "Publicación del sistema en el dominio institucional",
                                                "done": true
                                    },
                                    {
                                                "text": "Calificación y cierre académico del proyecto SIGE",
                                                "done": true
                                    }
                        ]
            }
];
console.log(JSON.stringify(tasks));