import glob
import re

log_files = sorted(glob.glob("Fase_*/*.log"))
print(f"Analyzing {len(log_files)} log files...")

for lf in log_files:
    tex_path = lf.replace(".log", ".tex")
    txt = open(lf, encoding="latin1").read()
    tex_txt = open(tex_path, encoding="utf-8").read().split("\n") if glob.glob(tex_path) else []
    
    overfulls = re.findall(r"Overfull \\hbox \(([0-9.]+pt too wide\)[^\n]*)", txt)
    if overfulls:
        # filter out the minor 2.28pt footer ones to see table-specific big ones
        big_overfulls = [o for o in overfulls if not o.startswith("2.28")]
        if big_overfulls:
            print(f"\n=== {lf} ({len(big_overfulls)} significant overfulls) ===")
            for bo in big_overfulls:
                print(" ", bo)
                m_line = re.search(r"lines? (\d+)", bo)
                if m_line and tex_txt:
                    line_no = int(m_line.group(1)) - 1
                    if 0 <= line_no < len(tex_txt):
                        print(f"    Line {line_no+1}: {tex_txt[line_no][:100]}")
