@echo off
set TID=_A2A
@REM for %%a in ("%CD%") do set TID=%%~nxa
set SID=23301077
set LNG=py
c++ %TID%.cpp
.\a.exe %TID% %SID% %LNG%
for %%a in (*) do if %%~za==0 del "%%a"
del /f /s /q /a .\out.txt >nul
del /f /s /q /a .\in.txt >nul
del /f /s /q /a .\*.exe >nul
rd /s /q __pycache__ >nul
pause
