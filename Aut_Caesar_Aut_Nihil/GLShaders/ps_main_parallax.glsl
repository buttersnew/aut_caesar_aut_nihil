
varying float4 VertexColor;
varying float2 Tex0;
varying float3 SunLightDir;
varying float3 SkyLightDir;
varying float4 PointLightDir;
varying float4 ShadowTexCoord;
#ifdef USE_ShadowTexelPos_INTERPOLATOR
	varying float2 ShadowTexelPos;
#endif
varying float3 ViewDir;
varying float4 WorldNormal;
varying float  Fog;

void main()
{ 
	VS_OUTPUT_PARALLAX VSOut;
	VSOut.VertexColor = VertexColor;
	VSOut.Tex0 = Tex0;
	VSOut.SunLightDir = SunLightDir;
	VSOut.SkyLightDir = SkyLightDir;
	VSOut.PointLightDir = PointLightDir;
	VSOut.ShadowTexCoord = ShadowTexCoord;
#ifdef USE_ShadowTexelPos_INTERPOLATOR
	VSOut.ShadowTexelPos = ShadowTexelPos;
#endif
	VSOut.ViewDir = ViewDir;
	VSOut.WorldNormal = WorldNormal;
	VSOut.Fog = Fog;
	
	gl_FragColor = ps_main_parallax(VSOut, CURRENT_PCF_MODE).RGBColor;
}

