@echo off
set c1=%CD%
%~d0
cd %~d0%~p0
python -u "./GUI/dmp.py"
cd %c1%