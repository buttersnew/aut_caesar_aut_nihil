
varying vec4 outColor0;
varying vec2 outTexCoord;
varying float outFog;

void main()
{ 
	VS_OUTPUT_FONT VSOut;
	VSOut.Color = outColor0;
	VSOut.Tex0 = outTexCoord;
	VSOut.Fog = outFog;
	
	gl_FragColor = ps_main_no_shadow_season(VSOut).RGBColor;
}
