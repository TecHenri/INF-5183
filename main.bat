@echo off
REM =====================================================
REM Script pour lancer le projet Python et installer les dépendances
REM =====================================================

REM Vérifier si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Veuillez installer Python 3.11 ou plus.
    pause
    exit /b
)

REM Créer un environnement virtuel si non existant
IF NOT EXIST "venv" (
    echo Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer les dépendances
echo Installation des dépendances...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Lancer le programme principal
echo Lancement du programme...
python main.py

REM Pause pour voir les résultats
pause
