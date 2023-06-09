@echo off
setlocal enabledelayedexpansion

set /a percentage=%random% %% 101
chcp 65001 >nul
echo Your gay is: %percentage%%%
pause >nul
