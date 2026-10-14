import re

for phase_num, fname in [(1, 'generate_fase1_enhanced.py'), (2, 'generate_fase2_enhanced.py'), (3, 'generate_fase3_enhanced.py'), (4, 'generate_fase4_enhanced.py')]:
    txt = open(fname, encoding='utf-8').read()
    b_matches = list(re.finditer(rf'b{phase_num}_(\d+)', txt))
    indices = sorted(list(set([m.group(1) for m in b_matches])), key=int)
    print(f"=== {fname} ===")
    for idx in indices:
        anx_var = f"anx{phase_num}_{idx}"
        m = re.search(rf'{anx_var}\s*=\s*r?"""([\s\S]*?)"""', txt)
        if m:
            anx_content = m.group(1)
            imgs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', anx_content)
            caps = re.findall(r'\\caption\{([^}]+)\}', anx_content)
            img_list = ", ".join(imgs) if imgs else "NO IMAGES"
            print(f"  {phase_num}.{idx}: {img_list}")
        else:
            print(f"  {phase_num}.{idx}: FAILED TO FIND ANX")
