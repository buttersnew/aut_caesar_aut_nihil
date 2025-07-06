
varying float4 Color;
varying float4 Tex0;
varying float3 CameraDir;
varying float4 ShadowTexCoord;
#ifdef USE_ShadowTexelPos_INTERPOLATOR
	varying float2 ShadowTexelPos;
#endif
varying float  Fog;
varying float3 SunLightDir;
varying float3 SkyLightDir;
varying float3 ViewDir;
varying float3 WorldNormal;

void main()
{
	VS_OUTPUT_NEW_MAP VSOut;
	VSOut.Color = Color;
	VSOut.Tex0 = Tex0;
	VSOut.CameraDir = CameraDir;
	VSOut.ShadowTexCoord = ShadowTexCoord;
	#ifdef USE_ShadowTexelPos_INTERPOLATOR
		VSOut.ShadowTexelPos = ShadowTexelPos;
	#endif
	VSOut.Fog = Fog;
	VSOut.SunLightDir = SunLightDir;
	VSOut.SkyLightDir = SkyLightDir;
	VSOut.ViewDir = ViewDir;
	VSOut.WorldNormal = WorldNormal;

	gl_FragColor = ps_new_map(VSOut, CURRENT_PCF_MODE).RGBColor;
}
