import re
import os
import subprocess

METADATA = {
    # ==========================
    # FASE 1
    # ==========================
    "1.1": {
        "desc_cambio": "Diagnóstico del flujo operativo As-Is, relevamiento de plantillas SGC y matriz de fallas operativas P-01 a P-06.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "1.2": {
        "desc_cambio": "Elaboración de la matriz de partes interesadas (Stakeholders), asignación de niveles RACI y perfiles de usuario.",
        "resp_cambio": "Heidi Villavicencio / Nixon Hurtado",
    },
    "1.3": {
        "desc_cambio": "Especificación formal de requisitos bajo estándar IEEE 29148: 14 funcionales (RF-01 a RF-14) y 8 no funcionales (RNF-01 a RNF-08).",
        "resp_cambio": "Heidi Villavicencio / Andrea Vásquez",
    },
    "1.4": {
        "desc_cambio": "Definición de fronteras del sistema, matriz de exclusiones operativas y alineación con objetivos SGC ISO 9001:2015.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },
    "1.5": {
        "desc_cambio": "Modelado de reglas de negocio institucionales (RN-01 a RN-08) y especificación de compuertas lógicas de validación.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },
    "1.6": {
        "desc_cambio": "Evaluación financiera, cuantificación de ahorros operativos, estimación de ROI institucional y formalización del Project Charter.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },
    "1.7": {
        "desc_cambio": "Estructuración de la EDT institucional, asignación de cargas de trabajo, dependencias lógicas y línea base del cronograma.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },
    "1.8": {
        "desc_cambio": "Consolidación del expediente de análisis, auditoría de calidad SGC y formalización de cierre de Fase 1.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },

    # ==========================
    # FASE 2
    # ==========================
    "2.1": {
        "desc_cambio": "Modelado formal de casos de uso UML, especificación de flujos principales, alternos y excepciones según estándar IEEE 1362.",
        "resp_cambio": "Heidi Villavicencio / Andrea Vásquez",
    },
    "2.2": {
        "desc_cambio": "Documento de Arquitectura de Software (SAD) bajo modelo C4 y principios de Clean Architecture multicapa.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },
    "2.3": {
        "desc_cambio": "Modelado dinámico y estructural UML: flujos de validación, ciclo de aprobación de documentos y clases de dominio.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },
    "2.4": {
        "desc_cambio": "Diseño entidad-relación relacional en tercera forma normal (3FN), diccionario de datos y esquema físico para PostgreSQL 18.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "2.5": {
        "desc_cambio": "Diseño de wireframes, arquitectura de información UI/UX institucional y especificación de flujos de interacción del usuario.",
        "resp_cambio": "Heidi Villavicencio / Andrea Vásquez",
    },
    "2.6": {
        "desc_cambio": "Definición de microservicios contenerizados, redes aisladas, volúmenes de persistencia y archivo docker-compose.yml de desarrollo.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },
    "2.7": {
        "desc_cambio": "Inspección técnica de especificaciones arquitectónicas, validación de diseño estructural y aprobación de Fase 2.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },

    # ==========================
    # FASE 3
    # ==========================
    "3.1": {
        "desc_cambio": "Desarrollo y ejecución de scripts DDL con restricciones de integridad, claves foráneas e índices B-tree optimizados.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.2": {
        "desc_cambio": "Implementación de migraciones de seeders y carga controlada de catálogos institucionales FISEI con llaves idempotentes.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.3": {
        "desc_cambio": "Implementación del servicio de autenticación JWT HMAC-SHA256, hash de contraseñas bcrypt y middleware RBAC por roles.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.4": {
        "desc_cambio": "Construcción del shell React, barra de navegación institucional, manejo de sesión en Zustand y rutas protegidas.",
        "resp_cambio": "Andrea Vásquez / Heidi Villavicencio",
    },
    "3.5": {
        "desc_cambio": "Desarrollo del componente Wizard por pestañas temáticas, sincronización de estado de guardado y validación de avance.",
        "resp_cambio": "Andrea Vásquez / Heidi Villavicencio",
    },
    "3.6": {
        "desc_cambio": "Integración del editor WYSIWYG TipTap con sanitización HTML DOMPurify y autoguardado reactivo con debounce de 1500 ms.",
        "resp_cambio": "Andrea Vásquez / Steeven Toala",
    },
    "3.7": {
        "desc_cambio": "Implementación de endpoints RESTful para guardado incremental, transacciones ACID y control de versiones de documentos.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.8": {
        "desc_cambio": "Demostración operativa del incremento Sprint 2, verificación de persistencia reactiva y validación con el Product Owner.",
        "resp_cambio": "Steeven Toala / Andrea Vásquez",
    },
    "3.9": {
        "desc_cambio": "Construcción de la tabla editable interactiva con cálculo reactivo de horas por eje sustantivo y compuertas de balance horario.",
        "resp_cambio": "Andrea Vásquez / Steeven Toala",
    },
    "3.10": {
        "desc_cambio": "Implementación del middleware de validación estricta de sumatorias horarias, duplicidad de tareas y control de estados de documento.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.11": {
        "desc_cambio": "Integración del servicio de almacenamiento S3 MinIO, cálculo de checksum SHA-256 de archivos y generación de URLs prefirmadas.",
        "resp_cambio": "Nixon Hurtado / Andrea Vásquez",
    },
    "3.12": {
        "desc_cambio": "Evaluación técnica del incremento Sprint 3: matriz dinámica de actividades, repositorio de evidencias y auditoría de horas.",
        "resp_cambio": "Steeven Toala / Heidi Villavicencio",
    },
    "3.13": {
        "desc_cambio": "Implementación del workflow de aprobación jerárquica con transiciones de estado, bandeja de revisión y registro de observaciones.",
        "resp_cambio": "Andrea Vásquez / Nixon Hurtado",
    },
    "3.14": {
        "desc_cambio": "Desarrollo del servicio de corrección lingüística híbrida mediante LanguageTool Docker local y fallback a Google Gemini API.",
        "resp_cambio": "Steeven Toala / Andrea Vásquez",
    },
    "3.15": {
        "desc_cambio": "Implementación del microservicio de generación documental en PDF y DOCX estructurados según formatos UTA-SGC-A-2-1-P7.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "3.16": {
        "desc_cambio": "Consolidación y cierre de la Fase 3, verificación de cobertura funcional de los módulos core e inspección del entregable general.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },

    # ==========================
    # FASE 4
    # ==========================
    "4.1": {
        "desc_cambio": "Diseño y ejecución de suite de pruebas unitarias automatizadas con Jest y Supertest sobre modelos, controladores y validadores.",
        "resp_cambio": "Nixon Hurtado / Steeven Toala",
    },
    "4.2": {
        "desc_cambio": "Ejecución de auditoría de seguridad OWASP Top 10, pruebas de inyección, mitigación de vulnerabilidades y verificación de cabeceras Helmet.",
        "resp_cambio": "Steeven Toala / Nixon Hurtado",
    },
    "4.3": {
        "desc_cambio": "Evaluación de cumplimiento de accesibilidad WCAG 2.1 nivel AA, pruebas de usabilidad y adaptabilidad multidispositivo responsive.",
        "resp_cambio": "Andrea Vásquez / Heidi Villavicencio",
    },
}

def clean_anx2_title(raw_sub):
    sub = raw_sub.strip()
    # Remove leading Evidencias Técnicas... if already present
    sub = re.sub(r'^Evidencias Técnicas de Ejecución y Validación\s*(--|:|-)?\s*', '', sub, flags=re.I).strip()
    # Remove leading Evidencia(s) de (la|del|los|las)
    sub = re.sub(r'^Evidencias?\s+de(\s+(la|del|los|las))?\s+', '', sub, flags=re.I).strip()
    # Remove leading Evidencia (e.g. "Evidencia del Proceso...")
    sub = re.sub(r'^Evidencia\s+(del?\s+|de\s+la\s+)?', '', sub, flags=re.I).strip()
    return sub

def process_phase_file(phase_num, fname):
    print(f"\n==========================================")
    print(f"Processing {fname} (Phase {phase_num})...")
    print(f"==========================================")
    content = open(fname, encoding='utf-8').read()
    
    # Pattern to match bodies: b{phase}_{idx} = r""" ... """
    b_pattern = rf'(b{phase_num}_(\d+)\s*=\s*r?""")([\s\S]*?)(""")'
    body_matches = list(re.finditer(b_pattern, content))
    print(f"Found {len(body_matches)} body blocks.")
    
    new_content = content
    
    for bm in body_matches:
        idx = bm.group(2)
        deliv_code = f"{phase_num}.{idx}"
        b_var = f"b{phase_num}_{idx}"
        anx_var = f"anx{phase_num}_{idx}"
        
        # 1. Locate body string
        b_find_pat = rf'({b_var}\s*=\s*r?""")([\s\S]*?)(""")'
        b_m = re.search(b_find_pat, new_content)
        if not b_m:
            print(f"  [ERROR] Could not find {b_var} in content!")
            continue
            
        b_prefix = b_m.group(1)
        b_body = b_m.group(2)
        b_suffix = b_m.group(3)
        
        # Check Section 8 and Section 9
        sec8_regex = r'(\\section\{M[ée]todo, Políticas y Contenidos\}[\s\S]*?)(\\section\{Descripción de actividades\})'
        sec_m = re.search(sec8_regex, b_body)
        if not sec_m:
            print(f"  [WARNING] Could not find Sec8/Sec9 in {b_var}")
            extracted_figs = ""
        else:
            sec8_text = sec_m.group(1)
            sec9_heading = sec_m.group(2)
            
            # Find all figure blocks in sec8_text
            fig_blocks = re.findall(r'(\\begin\{figure\}[\s\S]*?\\end\{figure\}(?:\s*\\FloatBarrier)?)', sec8_text)
            if not fig_blocks:
                print(f"  [{deliv_code}] No figures in Section 8.")
                extracted_figs = ""
            else:
                print(f"  [{deliv_code}] Found {len(fig_blocks)} figures in Section 8.")
                extracted_figs = "\n\n".join([fb.strip() for fb in fig_blocks])
                
                # Remove figures from Section 8
                cleaned_sec8 = sec8_text
                for fb in fig_blocks:
                    cleaned_sec8 = cleaned_sec8.replace(fb, "")
                cleaned_sec8 = cleaned_sec8.rstrip() + "\n\n"
                
                # Rebuild body
                new_body = b_body[:sec_m.start()] + cleaned_sec8 + sec9_heading + b_body[sec_m.end():]
                old_b_str = b_prefix + b_body + b_suffix
                new_b_str = b_prefix + new_body + b_suffix
                new_content = new_content.replace(old_b_str, new_b_str)
                print(f"  [{deliv_code}] Successfully purged figures from Section 8.")
                
        # 2. Relocate extracted figures into anx
        if extracted_figs:
            anx_find_pat = rf'({anx_var}\s*=\s*r?"""[\s\S]*?)(\\subsection\*\{{Anexo 2:([^\n]*?)\}})([\s\S]*?""")'
            anx_m = re.search(anx_find_pat, new_content)
            if not anx_m:
                print(f"  [WARNING] Could not find Anexo 2 in {anx_var}!")
            else:
                anx_pre = anx_m.group(1)
                anx2_old_heading = anx_m.group(2)
                raw_sub = anx_m.group(3)
                anx_post = anx_m.group(4)
                
                sub_title = clean_anx2_title(raw_sub)
                new_heading = f"\\subsection*{{Anexo 2: Evidencias Técnicas de Ejecución y Validación -- {sub_title}}}"
                
                # Clean up extracted_figs to ensure \FloatBarrier is on each
                # Insert heading + figures
                figs_block = extracted_figs + "\n"
                anx_replacement = f"{anx_pre}{new_heading}\n\n{figs_block}\n{anx_post}"
                old_anx_str = anx_m.group(0)
                new_content = new_content.replace(old_anx_str, anx_replacement)
                print(f"  [{deliv_code}] Successfully relocated figures to Anexo 2.")
                
        # 3. Update render_doc call with desc_cambio and resp_cambio
        meta = METADATA.get(deliv_code)
        if meta:
            desc_c = meta["desc_cambio"].replace('"', '\\"')
            resp_c = meta["resp_cambio"].replace('"', '\\"')
            
            # Match render_doc call
            # render_doc(..., b{phase}_{idx}, ..., anx{phase}_{idx}[, optional args])
            r_pat = rf'render_doc\(([\s\S]*?b{phase_num}_{idx}[\s\S]*?anx{phase_num}_{idx})(\s*,[\s\S]*?)?\)'
            r_m = re.search(r_pat, new_content)
            if not r_m:
                print(f"  [WARNING] Could not find render_doc call for {deliv_code}!")
            else:
                base_args = r_m.group(1).strip()
                new_render_call = f'render_doc({base_args}, desc_cambio="{desc_c}", resp_cambio="{resp_c}")'
                old_render_str = r_m.group(0)
                new_content = new_content.replace(old_render_str, new_render_call)
                print(f"  [{deliv_code}] Updated render_doc parameters (desc_cambio & resp_cambio).")
                
    # Save modified file
    with open(fname, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Saved changes to {fname}.")

if __name__ == "__main__":
    for phase_num, fname in [(1, 'generate_fase1_enhanced.py'), (2, 'generate_fase2_enhanced.py'), (3, 'generate_fase3_enhanced.py'), (4, 'generate_fase4_enhanced.py')]:
        process_phase_file(phase_num, fname)
