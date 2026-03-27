@echo off

echo ==========================
echo   Running GUI Mode
echo ==========================
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing base requirements...
pip install -r requirements.txt

echo.
echo Checking PySide6...

pip show PySide6 >nul 2>&1
if errorlevel 1 (
    echo Installing PySide6...
    pip install PySide6
) else (
    echo PySide6 already installed.
)

echo.
echo Launching GUI app...
python main_gui.py

pause