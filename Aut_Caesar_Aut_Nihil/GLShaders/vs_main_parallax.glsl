
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
attribute vec4 inColor0;
attribute vec4 inColor1;

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
	VSOut = vs_main_parallax(CURRENT_PCF_MODE, vec4(inPosition, 1.0), inNormal, inTexCoord, inTangent, inBinormal, inColor0, inColor1);

	gl_Position = VSOut.Pos;
	VertexColor = VSOut.VertexColor;
	Tex0 = VSOut.Tex0;
	SunLightDir = VSOut.SunLightDir;
	SkyLightDir = VSOut.SkyLightDir;
	PointLightDir = VSOut.PointLightDir;
	ShadowTexCoord = VSOut.ShadowTexCoord;
#ifdef USE_ShadowTexelPos_INTERPOLATOR
	ShadowTexelPos = VSOut.ShadowTexelPos;	
#endif
	ViewDir = VSOut.ViewDir;
	WorldNormal = VSOut.WorldNormal;
	Fog = VSOut.Fog;
}
