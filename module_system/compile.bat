:repeat
@echo off

python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9
@echo Script processing has ended as of %TIME%
@pause
goto:repeat
pause