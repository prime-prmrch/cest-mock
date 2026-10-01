@echo off
echo ====================================================
echo Starting Cambridge English Skills Test Portal...
echo ====================================================
echo Open your browser at http://localhost:8080
echo To access from iPhone/tablet on local Wi-Fi, use your PC's IP address:8080
echo ====================================================
python -m http.server 8080
pause
