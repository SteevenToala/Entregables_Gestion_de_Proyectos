# fix_wrap_overfulls.py
# -*- coding: utf-8 -*-
import glob, re

def wrap_texttt_contents(text):
    def repl(m):
        inner = m.group(1)
        # Avoid double allowbreaks
        inner_clean = inner.replace(r'\allowbreak', '')
        # Wrap slashes
        inner_clean = re.sub(r'(/+)', r'\1\\allowbreak ', inner_clean)
        # Wrap underscores
        inner_clean = re.sub(r'(\\_)', r'\1\\allowbreak ', inner_clean)
        # Wrap dots that are followed by alphanumeric
        inner_clean = re.sub(r'(\.)(?=[a-zA-Z0-9])', r'\1\\allowbreak ', inner_clean)
        # Wrap hyphens in long codes
        inner_clean = re.sub(r'(-)(?=[a-zA-Z0-9])', r'\1\\allowbreak ', inner_clean)
        return r'\texttt{' + inner_clean + '}'
    return re.sub(r'\\texttt\{([^}]+)\}', repl, text)

def fix_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    c = wrap_texttt_contents(c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Patched line wraps in {fpath}")

# Patch generators
for p in ['generate_fase1_enhanced.py', 'generate_fase2_enhanced.py', 'generate_fase3_enhanced.py', 'generate_fase4_enhanced.py']:
    fix_file(p)

# Patch current tex files
for tf in glob.glob('Fase_*/*.tex'):
    fix_file(tf)

print("Done comprehensive wrapping on all texttt paths!")
