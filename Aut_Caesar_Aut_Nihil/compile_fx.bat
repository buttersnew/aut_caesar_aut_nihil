:start

@echo off && title compiling the hlsl shaders thing-- && echo ^[working hard...^] ^[started at %time%^] && echo. 
start /b /wait /i /high /realtime fxc /D /nologo /D PS_2_X=ps_2_b /Tfx_2_0 /Fomb.fx mb_src.fx

echo. && echo Shader processing has ended at %time%.
echo Press any key to recompile. . .
echo ___________________________________
goto :start
