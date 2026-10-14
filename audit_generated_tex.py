import os
import glob
import re

tex_files = glob.glob("Fase_*/*.tex")
print(f"Total .tex files found: {len(tex_files)}")

errors = []
total_figs_sec8 = 0
total_figs_anx2 = 0
ai_desc_count = 0
generic_resp_count = 0

for tf in sorted(tex_files):
    txt = open(tf, encoding='utf-8').read()
    
    # 1. Check Section 8 for figures
    sec8_m = re.search(r'\\section\{M[ée]todo, Políticas y Contenidos\}[\s\S]*?\\section\{Descripción de actividades\}', txt)
    if sec8_m:
        sec8_txt = sec8_m.group(0)
        figs_in_sec8 = re.findall(r'\\begin\{figure\}', sec8_txt)
        if figs_in_sec8:
            errors.append(f"{tf}: {len(figs_in_sec8)} figures still in Section 8!")
            total_figs_sec8 += len(figs_in_sec8)
    else:
        errors.append(f"{tf}: Could not find Section 8/9 boundary!")
        
    # 2. Check Anexo 2 for figures
    anx2_m = re.search(r'\\subsection\*\{Anexo 2:[\s\S]*?\\subsection\*\{Anexo 3:', txt)
    if anx2_m:
        anx2_txt = anx2_m.group(0)
        figs_in_anx2 = re.findall(r'\\begin\{figure\}', anx2_txt)
        total_figs_anx2 += len(figs_in_anx2)
    else:
        errors.append(f"{tf}: Could not find Anexo 2/3 boundary!")
        
    # 3. Check for robotic AI change description
    if "Emisión inicial del entregable según EDT del Tablero Trello" in txt:
        ai_desc_count += 1
        errors.append(f"{tf}: Still has robotic AI change description!")
        
    # 4. Check for generic Equipo de Proyecto SIGE in Control de Cambios
    # Specifically look at the table under \section{Control de Cambios}
    cc_m = re.search(r'\\section\{Control de Cambios\}[\s\S]*?\\end\{tabularx\}', txt)
    if cc_m:
        cc_txt = cc_m.group(0)
        if "Equipo de Proyecto SIGE" in cc_txt:
            generic_resp_count += 1
            errors.append(f"{tf}: Control de cambios has generic 'Equipo de Proyecto SIGE'!")

print(f"\nAUDIT RESULTS:")
print(f"Total files audited: {len(tex_files)}")
print(f"Figures remaining in Section 8: {total_figs_sec8}")
print(f"Figures placed in Anexo 2: {total_figs_anx2}")
print(f"Robotic AI change description occurrences: {ai_desc_count}")
print(f"Generic 'Equipo de Proyecto SIGE' in Control de Cambios: {generic_resp_count}")

if errors:
    print(f"\nERRORS DETECTED ({len(errors)}):")
    for e in errors:
        print("  -", e)
else:
    print("\nPERFECT AUDIT: ZERO errors across all 34 files!")
