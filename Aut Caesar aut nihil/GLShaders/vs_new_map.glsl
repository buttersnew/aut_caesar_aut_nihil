
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;

varying float4 Pos;
varying float4 Color;
varying float4 Tex0;
varying float3 CameraDir;
varying float4 ShadowTexCoord;
varying float2 ShadowTexelPos;
varying float Fog;	
varying float3 SunLightDir;
varying float3 SkyLightDir;	
varying float3 ViewDir;
varying float3 WorldNormal;

void main()
{
	VS_OUTPUT_NEW_MAP VSOut;
	VSOut = vs_new_map(CURRENT_PCF_MODE, vec4(inPosition, 1.0), inNormal, inTangent, inBinormal, inTexCoord, inColor0, inColor1);

	gl_Position = VSOut.Pos;
	Color = VSOut.Color;
	Tex0 = VSOut.Tex0;
	CameraDir = VSOut.CameraDir;
	ShadowTexCoord = VSOut.ShadowTexCoord;
	ShadowTexelPos = VSOut.ShadowTexelPos;
	Fog = VSOut.Fog;	
	SunLightDir = VSOut.SunLightDir;
	SkyLightDir = VSOut.SkyLightDir;	
	ViewDir = VSOut.ViewDir;
	WorldNormal = VSOut.WorldNormal;
}
