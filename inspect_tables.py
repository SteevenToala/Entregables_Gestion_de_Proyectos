import glob
import re

tex_files = glob.glob('Fase_*/*.tex')

def extract_tables(txt):
    tables = []
    # find all \begin{tabularx}{...}{...} or \begin{tabular}{...}
    pos = 0
    while True:
        m = re.search(r'\\begin\{(tabularx|tabular)\}', txt[pos:])
        if not m:
            break
        env = m.group(1)
        start_idx = pos + m.start()
        
        # find matching \end{env}
        end_str = f"\\end{{{env}}}"
        end_idx = txt.find(end_str, start_idx)
        if end_idx == -1:
            break
            
        full_table = txt[start_idx:end_idx + len(end_str)]
        tables.append((env, full_table))
        pos = end_idx + len(end_str)
    return tables

all_tables = []
for tf in sorted(tex_files):
    txt = open(tf, encoding='utf-8').read()
    t_list = extract_tables(txt)
    all_tables.append((tf, t_list))

print(f"Audited {len(all_tables)} files, found total {sum(len(t) for _, t in all_tables)} tables.")

# Let's inspect each table: column spec and line overflows
for tf, t_list in all_tables:
    for env, t_str in t_list:
        first_line = t_str.split('\n')[0]
        # Check if tabularx has no X
        if env == 'tabularx':
            # extract column specification
            # after \begin{tabularx}{...}{...}
            m_spec = re.search(r'\\begin\{tabularx\}\s*\{([^}]+)\}\s*\{([\s\S]*?)\}', t_str)
            if m_spec:
                width = m_spec.group(1).strip()
                col_spec = m_spec.group(2).strip()
                if not any(k in col_spec for k in ['X', 'Y', 'L', 'C']):
                    print(f"NO X COLUMN in {tf}: {first_line[:80]}")
