
varying float Fog;	
varying float4 Color;
varying float4 Tex0;
varying float4 SunLight;
varying float4 ShadowTexCoord;
#ifdef USE_ShadowTexelPos_INTERPOLATOR
	varying float2 ShadowTexelPos;
#endif
varying float4 WorldPos;

void main()
{ 
	VS_OUTPUT_ICON_SEASONAL VSOut;
	VSOut.Fog = Fog;
	VSOut.Color = Color;
	VSOut.Tex0 = Tex0;
	VSOut.SunLight = SunLight;
	VSOut.ShadowTexCoord = ShadowTexCoord;
	#ifdef USE_ShadowTexelPos_INTERPOLATOR
		VSOut.ShadowTexelPos = ShadowTexelPos;
	#endif
	VSOut.WorldPos = WorldPos;
	
	gl_FragColor = ps_main_icon_seasonal(VSOut, CURRENT_PCF_MODE).RGBColor;
}
