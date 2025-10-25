:start
@echo off
title Compiling HLSL Shaders...

cls
echo [Working hard...] [Started at %time%]
echo.

REM Run the compiler and wait for it to finish.
start /b /wait /i /high /realtime fxc /D /nologo /D PS_2_X=ps_2_b /Tfx_2_0 /Fomb.fx mb_src.fx

echo.
echo Shader processing has ended at %time%.
echo ___________________________________
echo Press any key to recompile...

REM This is the crucial fix: Pause and wait for a key press.
pause > nul

REM Now, loop back to the start.
goto :start