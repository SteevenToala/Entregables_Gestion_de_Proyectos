# -*- coding: utf-8 -*-
with open("generate_fase3_enhanced.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("|}m{3.5cm}|c|c|X|}", "|}")
text = text.replace("|}m{3.2cm}|m{3.0cm}|X|c|}", "|}")
text = text.replace("|}m{3.2cm}|X|c|}", "|}")
text = text.replace("|}m{3.2cm}|m{2.8cm}|X|c|}", "|}")
text = text.replace("|}m{3.2cm}|c|X|c|}", "|}")

with open("generate_fase3_enhanced.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Cleaned trailing specs in generate_fase3_enhanced.py")

with open("compile_folder.py", "r", encoding="utf-8") as f:
    cf = f.read()
cf = cf.replace("text=True", "text=True, encoding='latin-1', errors='replace'")
with open("compile_folder.py", "w", encoding="utf-8") as f:
    f.write(cf)
print("Updated compile_folder.py with safe encoding")
