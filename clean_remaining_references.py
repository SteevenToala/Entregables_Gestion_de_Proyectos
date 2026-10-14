import re

def clean_fase2():
    fname = "generate_fase2_enhanced.py"
    txt = open(fname, encoding="utf-8").read()

    txt = txt.replace(
        r"Entregable Oficial & \texttt{01\_Diagrama\_General\_Detallado\_Casos\_de\_Uso.pdf} \\",
        r"Entregable Oficial & Documento de Especificación y Modelado de Casos de Uso UML \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{02\_Diseno\_Arquitectura\_Solucion.pdf} (SAD \& C4 Model) \\",
        r"Entregable Oficial & Documento de Arquitectura de Software (SAD - Modelo C4) \\"
    )
    txt = txt.replace(
        r"Entregable Oficial & \texttt{03\_Diagramas\_Secuencia\_Actividades\_Clases.pdf} \\",
        r"Entregable Oficial & Especificación de Diagramas UML Dinámicos y de Dominio \\"
    )
    txt = txt.replace(
        r"parametrizadas en archivo \texttt{.env}.",
        r"parametrizadas en variables de configuración del sistema."
    )
    txt = txt.replace(
        r"archivo \texttt{.env}",
        r"variables de configuración del sistema"
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Cleaned remaining references in generate_fase2_enhanced.py")

def clean_fase3():
    fname = "generate_fase3_enhanced.py"
    txt = open(fname, encoding="utf-8").read()

    # Formal titles in Anexo 1
    anx1_replacements = [
        (r"Entregable Oficial & \texttt{DbInitializer} con usuarios y catálogos institucionales \\",
         r"Entregable Oficial & Módulo de Inicialización de Datos y Catálogos Maestros \\"),
        (r"Entregable Oficial & Auth Endpoints con JWT y decoradores \texttt{[Authorize(Roles=...)]} \\",
         r"Entregable Oficial & Servicio de Autenticación, Control de Acceso y Gestión de Roles \\"),
        (r"Entregable Oficial & SPA SIGE Frontend (React + Vite) funcional con navegación y rutas \\",
         r"Entregable Oficial & Arquitectura del Cliente Web y Sistema de Navegación Institucional \\"),
        (r"Entregable Oficial & \texttt{RichTextEditor} con autoguardado y formato HTML limpio \\",
         r"Entregable Oficial & Editor Enriquecido de Texto con Persistencia Automática Asíncrona \\"),
        (r"Entregable Oficial & Demostración funcional de Wizard con autoguardado en DB \\",
         r"Entregable Oficial & Expediente de Revisión del Incremento Sprint 2: Wizard y Persistencia \\"),
        (r"Entregable Oficial & Middlewares de validación y reglas de negocio (\texttt{validation.middleware.js}) \\",
         r"Entregable Oficial & Módulo de Validación Estricta y Compuertas Lógicas de Negocio \\"),
        (r"Entregable Oficial & \texttt{MinioStorageService.cs} y componente de upload de evidencias \\",
         r"Entregable Oficial & Servicio de Almacenamiento Seguro de Evidencias en MinIO S3 \\"),
        (r"Entregable Oficial & Demostración funcional de matriz con evidencias MinIO \\",
         r"Entregable Oficial & Expediente de Revisión del Incremento Sprint 3: Matriz y Evidencias S3 \\"),
        (r"Entregable Oficial & Panel de Comité y servicio de Firmas multinivel \\",
         r"Entregable Oficial & Módulo de Revisión Jerárquica y Cascada de Firmas Digitales \\"),
        (r"Entregable Oficial & \texttt{DocumentExportService.cs} con salidas idénticas al SGC \\",
         r"Entregable Oficial & Motor de Generación y Exportación Documental en Formato Institucional \\"),
        (r"Entregable Oficial & Versión funcional v0.9 con todas las funciones del SRS \\",
         r"Entregable Oficial & Expediente Integral de Cierre de Construcción del Sistema Core \\"),
    ]
    for old_s, new_s in anx1_replacements:
        txt = txt.replace(old_s, new_s)

    # In-text file references
    txt = txt.replace(
        r"\item Codificar los 6 Validation Gates del sistema (\texttt{validation.middleware.js}).",
        r"\item Codificar los 6 Validation Gates del sistema mediante la capa de validación de reglas de negocio."
    )
    txt = txt.replace(
        r"(\texttt{validation.middleware.js})",
        r"(Módulo de Validación de Reglas de Negocio)"
    )
    txt = txt.replace(
        r"\item Implementar el servicio \texttt{minio.service.js} con soporte para subida de archivos y generación de URLs prefirmadas.",
        r"\item Implementar el servicio de custodia documental con soporte para subida de archivos y generación de URLs prefirmadas."
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Cleaned remaining references in generate_fase3_enhanced.py")

if __name__ == "__main__":
    clean_fase2()
    clean_fase3()
    print("Done cleaning all remaining references!")
