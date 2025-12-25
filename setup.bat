@echo off
echo ========================================
echo AI Podcast Clip Generator - Setup
echo ========================================
echo.

echo [1/2] Setting up Backend...
cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created
) else (
    echo .env file already exists
)

echo.
echo [2/2] Setting up Frontend...
cd ..\frontend

echo Installing dependencies...
call npm install

echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created
) else (
    echo .env file already exists
)

cd ..

echo.
echo ========================================
echo Setup Complete! ✅
echo ========================================
echo.
echo To start the application:
echo.
echo 1. Backend:
echo    cd backend
echo    venv\Scripts\activate
echo    python main.py
echo.
echo 2. Frontend (in another terminal):
echo    cd frontend
echo    npm run dev
echo.
echo Backend will run on: http://localhost:8000
echo Frontend will run on: http://localhost:3000
echo.
pause
