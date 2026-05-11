@echo off
REM ---------------------------------------------
REM  Set up environment for Robot Framework tests
REM ---------------------------------------------

REM Get the directory of the script
SET SCRIPT_DIR=%~dp0

REM Set PYTHONPATH to the project root so Python can find 'libraries'
SET PYTHONPATH=%SCRIPT_DIR%

REM Activate virtual environment
CALL "%SCRIPT_DIR%\.venv\Scripts\activate.bat"

REM Run Robot Framework tests
robot --outputdir "%SCRIPT_DIR%reports" "%SCRIPT_DIR%tests"

REM Pause at the end so you can see output
PAUSE