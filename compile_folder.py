import os, sys, subprocess, glob

def compile_folder(folder_name):
    target_dir = os.path.join("Entregables_Latex", folder_name)
    tex_files = sorted(glob.glob(os.path.join(target_dir, "*.tex")))
    print(f"\n=======================================================")
    print(f"Compiling {len(tex_files)} documents in {folder_name}...")
    print(f"=======================================================")
    success_count = 0
    fail_count = 0
    for tf in tex_files:
        base_name = os.path.basename(tf)
        print(f"-> Compiling {base_name}...", end=" ", flush=True)
        # Run pdflatex inside the target directory
        res = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", base_name],
            cwd=target_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if res.returncode == 0:
            # Second pass for references
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", base_name],
                cwd=target_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            pdf_name = base_name.replace(".tex", ".pdf")
            pdf_path = os.path.join(target_dir, pdf_name)
            if os.path.exists(pdf_path):
                size = os.path.getsize(pdf_path)
                print(f"OK ({size} bytes)")
                success_count += 1
            else:
                print("FAIL (PDF not created)")
                fail_count += 1
        else:
            print("FAIL (Error in LaTeX)")
            print("\n--- LaTeX Log snippet ---")
            for line in res.stdout.splitlines()[-25:]:
                print(line)
            print("-------------------------\n")
            fail_count += 1

    print(f"\nFinished {folder_name}: {success_count} succeeded, {fail_count} failed.\n")
    return fail_count == 0

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "Fase_1"
    compile_folder(folder)
