@echo off
echo ========================================
echo Starting Backend Server with SSL Fix
echo ========================================
cd /d D:\yt-shorts-automation\backend
call venv\Scripts\activate.bat
echo.
echo Setting SSL environment variables...
set PYTHONHTTPSVERIFY=0
set CURL_CA_BUNDLE=
set REQUESTS_CA_BUNDLE=
echo.
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop
echo.
python main.py
