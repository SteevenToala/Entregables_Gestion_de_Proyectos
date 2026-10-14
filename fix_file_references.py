import re

# Comprehensive dictionary of formal artifact titles for Anexo 1
ENTREGABLES_MAP = {
    # Fase 1
    "1.1": "Informe Técnico de Diagnóstico y Mapeo del Proceso As-Is",
    "1.2": "Matriz de Identificación de Actores y Mapa de Procesos SGC",
    "1.3": "Especificación de Requisitos de Software (SRS - IEEE 29148)",
    "1.4": "Documento de Línea Base del Alcance y Restricciones SGC",
    "1.5": "Catálogo de Reglas de Negocio y Validación Gates Lógicas",
    "1.6": "Caso de Negocio, Estudio de Retorno de Inversión y Project Charter",
    "1.7": "Cronograma Oficial del Proyecto y Estructura de Desglose del Trabajo",
    "1.8": "Expediente Técnico de Aprobación de Fase 1 e Hito Institucional",
    # Fase 2
    "2.1": "Documento de Especificación y Modelado de Casos de Uso UML",
    "2.2": "Documento de Arquitectura de Software (SAD - Modelo C4)",
    "2.3": "Especificación de Diagramas UML Dinámicos y de Dominio",
    "2.4": "Diseño Físico y Diccionario del Modelo Relacional",
    "2.5": "Especificación de Interfaces de Usuario y Design System",
    "2.6": "Infraestructura y Orquestación de Microservicios Contenerizados",
    "2.7": "Expediente Integral de Aprobación de Arquitectura de Software",
    # Fase 3
    "3.1": "Definición de Esquema e Índices Relacionales en PostgreSQL 18",
    "3.2": "Módulo de Inicialización de Datos y Catálogos Maestros",
    "3.3": "Servicio de Autenticación, Control de Acceso y Gestión de Roles",
    "3.4": "Arquitectura del Cliente Web y Sistema de Navegación Institucional",
    "3.5": "Componente Asistente Guiado Modular (Wizard) para Planes de Trabajo",
    "3.6": "Editor Enriquecido de Texto con Persistencia Automática Asíncrona",
    "3.7": "Controladores de Persistencia y Transacciones ACID de Secciones",
    "3.8": "Expediente de Revisión del Incremento Sprint 2: Wizard y Persistencia",
    "3.9": "Componente Interactivo de la Matriz Dinámica de Actividades",
    "3.10": "Módulo de Validación Estricta y Compuertas Lógicas de Negocio",
    "3.11": "Servicio de Almacenamiento Seguro de Evidencias en MinIO S3",
    "3.12": "Expediente de Revisión del Incremento Sprint 3: Matriz y Evidencias S3",
    "3.13": "Módulo de Revisión Jerárquica y Cascada de Firmas Digitales",
    "3.14": "Capa de Asistencia Lingüística y Corrección de Redacción",
    "3.15": "Motor de Generación y Exportación Documental en Formato Institucional",
    "3.16": "Expediente Integral de Cierre de Construcción del Sistema Core",
    # Fase 4
    "4.1": "Suite Automatizada de Pruebas Unitarias de Backend",
    "4.2": "Informe de Auditoría de Seguridad y Pruebas de Integración OWASP",
    "4.3": "Informe de Pruebas de Interfaz, Accesibilidad WCAG y Diseño Adaptable",
}

for phase_num, fname in [(1, 'generate_fase1_enhanced.py'), (2, 'generate_fase2_enhanced.py'), (3, 'generate_fase3_enhanced.py'), (4, 'generate_fase4_enhanced.py')]:
    txt = open(fname, encoding='utf-8').read()
    
    # Replace in each anx block
    for idx_num in range(1, 17):
        key = f"{phase_num}.{idx_num}"
        if key not in ENTREGABLES_MAP:
            continue
        title = ENTREGABLES_MAP[key]
        anx_var = f"anx{phase_num}_{idx_num}"
        
        # Match anx block
        anx_pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?)Entregable Oficial & [^\n]*?\\\\([\s\S]*?""")'
        m = re.search(anx_pat, txt)
        if m:
            txt = txt[:m.start()] + m.group(1) + f"Entregable Oficial & {title} \\\\" + m.group(2) + txt[m.end():]
            print(f"[{fname}] Replaced Entregable Oficial for {key}")
            
    # Also replace any stray file names in text or tables
    replacements = [
        # Fase 2 specific
        (r"(\texttt{docker-compose.yml})", "la especificación de orquestación de contenedores"),
        (r"\texttt{docker-compose.yml}", "la especificación de orquestación de contenedores"),
        (r"docker-compose.yml", "orquestación de contenedores Docker"),
        (r"(\texttt{schema.sql})", "los scripts de definición DDL"),
        (r"\texttt{schema.sql}", "los scripts DDL"),
        (r"schema.sql", "scripts DDL"),
        # Fase 3 specific
        (r"\texttt{PlanEditorWizard.tsx}", "Componente Wizard del Plan"),
        (r"\texttt{MatrizActividadesTable.tsx}", "Componente de la Matriz Dinámica"),
        (r"PlanEditorWizard.tsx", "Componente Wizard del Plan"),
        (r"MatrizActividadesTable.tsx", "Componente de la Matriz Dinámica"),
        # Fase 4 specific
        (r"\texttt{tests/auth-jwt.test.js}", "Suite de pruebas de autenticación y tokens JWT"),
        (r"\texttt{tests/validation-gates.test.js}", "Suite de pruebas de compuertas lógicas"),
        (r"\texttt{tests/matriz-calc.test.js}", "Suite de pruebas de cálculo matricial"),
        (r"\texttt{tests/firmas-cascade.test.js}", "Suite de pruebas de flujo y cascada de firmas"),
        (r"tests/auth-jwt.test.js", "Módulo de pruebas de autenticación"),
        (r"tests/validation-gates.test.js", "Módulo de pruebas de compuertas de validación"),
        (r"tests/matriz-calc.test.js", "Módulo de pruebas de cálculo matricial"),
        (r"tests/firmas-cascade.test.js", "Módulo de pruebas de cascada de firmas"),
        # General file mentions
        (r"(\texttt{0[0-9]\_[^\}]+?\.(?:pdf|md)\})", ""),
        (r"\texttt{0[0-9]\_[^\}]+?\.(?:pdf|md)\}", ""),
    ]
    for old_s, new_s in replacements:
        txt = txt.replace(old_s, new_s)
        
    # Write back
    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"Updated {fname} successfully.\n")

print("All generator files cleaned of file references!")
