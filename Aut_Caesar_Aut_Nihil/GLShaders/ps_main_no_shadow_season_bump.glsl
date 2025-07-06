
varying float2 Tex0;
varying float3 SkyDir;
varying float3 SunDir;
varying float4 vColor;
varying float Fog;

void main()
{ 
	VS_OUTPUT_FONT_X_BUMP VSOut;
	VSOut.Tex0 = Tex0;
	VSOut.SkyDir = SkyDir;
	VSOut.SunDir = SunDir;
	VSOut.vColor = vColor;
	VSOut.Fog = Fog;
	
	gl_FragColor = ps_main_no_shadow_season_bump(VSOut).RGBColor;
}
