# inspect_activities.py
import re

phases = {
    'Fase 1': 'generate_fase1_enhanced.py',
    'Fase 2': 'generate_fase2_enhanced.py',
    'Fase 3': 'generate_fase3_enhanced.py',
    'Fase 4': 'generate_fase4_enhanced.py'
}

for phase_name, filename in phases.items():
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Check "Paso 1" occurrences
    paso_matches = re.findall(r'paso\s*\d+', text, re.I)
    print(f'=== {phase_name} ({filename}) ===')
    print(f'  Occurrences of "Paso X": {len(paso_matches)}')
    
    # Find all bodies
    bodies = re.findall(r'(b\d+_\d+)\s*=\s*r"""(.*?)"""', text, re.DOTALL)
    print(f'  Bodies found: {len(bodies)}')
    for bname, bcontent in bodies:
        m = re.search(r'\\section\{Descripci[oó]n de actividades\}(.*?)(?=\\section\{Firmas|\\section\{Control|\Z)', bcontent, re.DOTALL)
        if m:
            desc = m.group(1).strip()
            # Count paragraphs / subsections
            subsecs = len(re.findall(r'\\subsection', desc))
            tables = len(re.findall(r'\\begin\{table\}', desc))
            chars = len(desc)
            print(f'    {bname}: {chars} chars, {subsecs} subsections, {tables} tables')
        else:
            print(f'    {bname}: NO Descripcion de actividades found!')

    # Check annexes files if any
    if phase_name == 'Fase 3':
        for anx_file in ['fase3_annexes_part1.py', 'fase3_annexes_part2.py']:
            with open(anx_file, 'r', encoding='utf-8') as af:
                atext = af.read()
            af_pasos = len(re.findall(r'paso\s*\d+', atext, re.I))
            print(f'  {anx_file}: {af_pasos} occurrences of "Paso X"')
