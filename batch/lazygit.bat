@ECHO OFF
set /p id=""
git add .
git commit -m "%id%"
git push