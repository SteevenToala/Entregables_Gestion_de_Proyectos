import os, json, glob

with open('Entregables_Latex/full_deliverables_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print(f"Target deliverables count: {len(manifest)}")

# Check existing files
existing_files = glob.glob('Entregables_Latex/**/*.tex', recursive=True)
print(f"Current existing .tex files: {len(existing_files)}")

# Group manifest by folder
by_folder = {}
for item in manifest:
    folder = item['folder']
    if folder not in by_folder:
        by_folder[folder] = []
    by_folder[folder].append(item)

for folder, items in by_folder.items():
    print(f"\n--- {folder} ({len(items)} items) ---")
    for it in items:
        target_path = os.path.join('Entregables_Latex', folder, it['filename'])
        exists = os.path.exists(target_path)
        print(f"  [{it['code']}] {it['filename']} -> Exists: {exists}")
