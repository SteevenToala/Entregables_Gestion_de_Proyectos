import glob
import re

log_files = sorted(glob.glob("Fase_*/*.log"))

for lf in log_files:
    txt = open(lf, encoding="latin1").read()
    tex_path = lf.replace(".log", ".tex")
    tex_lines = open(tex_path, encoding="utf-8").read().split("\n")
    
    # find lines with overfull > 5pt
    matches = re.finditer(r"Overfull \\hbox \(([0-9.]+)pt too wide\)[^\n]*?(?:at lines? (\d+)|in paragraph at lines? (\d+)--(\d+)|in alignment at lines? (\d+)--(\d+))", txt)
    
    deliv_printed = False
    for m in matches:
        pt = float(m.group(1))
        if pt > 3.0:
            line_str = m.group(2) or m.group(3) or m.group(5)
            if not deliv_printed:
                print(f"\n=== {lf} ===")
                deliv_printed = True
            line_no = int(line_str) if line_str else None
            snippet = tex_lines[line_no-1][:90] if (line_no and line_no <= len(tex_lines)) else "UNKNOWN"
            print(f"  Overfull {pt:.1f}pt at line {line_str}: {snippet}")
