import subprocess
from pathlib import Path
import sys

gui_dir = Path("gui")
ui_dir = Path("ui")
ui_dir.mkdir(exist_ok=True)

# Chemin vers l'exécutable pyside6-uic dans le venv
venv_uic = Path(sys.executable).parent / "pyside6-uic.exe"

for ui_file in gui_dir.glob("*.ui"):
    output_file = ui_dir / f"ui_{ui_file.stem}.py"
    print(f"[INFO] Génération : {ui_file.name} -> {output_file.name}")
    subprocess.run([str(venv_uic), str(ui_file), "-o", str(output_file)], check=True)