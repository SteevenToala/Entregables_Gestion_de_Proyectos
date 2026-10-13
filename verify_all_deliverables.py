import os, glob, re, json

def verify_all():
    print("================================================================")
    print("VERIFICACIÓN INTEGRAL DE ENTREGABLES SIGE SEGÚN TABLERO TRELLO")
    print("================================================================\n")

    phases = {
        "Fase_1": 8,
        "Fase_2": 7,
        "Fase_3": 16,
        "Fase_4": 3
    }

    total_expected = sum(phases.values())
    total_tex = 0
    total_pdf = 0
    all_passed = True

    for phase, expected_count in phases.items():
        tex_files = sorted(glob.glob(os.path.join("Entregables_Latex", phase, "*.tex")))
        pdf_files = sorted(glob.glob(os.path.join("Entregables_Latex", phase, "*.pdf")))
        print(f"[{phase}]")
        print(f"  Archivos .tex encontrados: {len(tex_files)} (Esperados: {expected_count})")
        print(f"  Archivos .pdf generados:   {len(pdf_files)} (Esperados: {expected_count})")
        
        if len(tex_files) != expected_count or len(pdf_files) != expected_count:
            print(f"  ERROR: Discrepancia en cantidad en {phase}")
            all_passed = False
        else:
            print(f"  OK: Cantidad exacta.")

        total_tex += len(tex_files)
        total_pdf += len(pdf_files)

        # Audit content of each file
        for tf in tex_files:
            fname = os.path.basename(tf)
            with open(tf, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # 1. No lstlisting
            if r"\begin{lstlisting}" in content:
                print(f"  ERROR en {fname}: Contiene bloques de código lstlisting!")
                all_passed = False

            # 2. No DATOS GENERALES
            if "DATOS GENERALES" in content:
                print(f"  ERROR en {fname}: Contiene sección DATOS GENERALES!")
                all_passed = False

            # 3. No Gemini versions
            if re.search(r"Gemini\s*(1\.5|2\.0|2\.5|Flash|Pro)", content, re.IGNORECASE):
                print(f"  ERROR en {fname}: Contiene versiones numéricas de Gemini!")
                all_passed = False

            # 4. Check 4 integrantes line
            if "Heidi Villavicencio" not in content or "Steeven Toala" not in content or "Nixon Hurtado" not in content or "Andrea Vásquez" not in content:
                print(f"  ERROR en {fname}: No contiene los 4 integrantes en la cabecera!")
                all_passed = False

            # 5. Check exactly 3 signers
            if "firma_heidi.png" not in content or "firma_steveen.png" not in content or "Ing. Paulo Torres" not in content:
                print(f"  ERROR en {fname}: Faltan firmas de responsabilidad obligatorias!")
                all_passed = False

    print("\n----------------------------------------------------------------")
    print(f"Total .tex auditados: {total_tex} / {total_expected}")
    print(f"Total .pdf generados: {total_pdf} / {total_expected}")
    print("----------------------------------------------------------------")

    if all_passed and total_pdf == total_expected:
        print("\n>>> AUDITORÍA 100% EXITOSA: TODOS LOS ENTREGABLES COINCIDEN CON TRELLO <<<\n")
        return True
    else:
        print("\n>>> AUDITORÍA CON ADVERTENCIAS O ERRORES <<<\n")
        return False

if __name__ == "__main__":
    verify_all()
