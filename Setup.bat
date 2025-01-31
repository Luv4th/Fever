@echo off

echo Checking if Python is installed...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

echo Python is installed. Proceeding with the installation of dependencies...

pip install colorama==0.4.6
pip install requests==2.28.2

pip freeze > requirements.txt

echo requirements.txt has been created with the installed packages.
pause
