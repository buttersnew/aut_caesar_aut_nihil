
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec2 inTexCoord;
attribute vec4 inColor0;
attribute vec4 inColor1;

varying float  Fog;	
varying float4 Color;
varying float4 Tex0;
varying float4 SunLight;
varying float4 ShadowTexCoord;
varying float2 ShadowTexelPos;
varying float4 WorldPos;

void main()
{
	VS_OUTPUT_SEA_FOAM VSOut;
	VSOut = vs_main_sea_foam(CURRENT_PCF_MODE, true, vec4(inPosition, 1.0), inNormal, inTexCoord, inColor0, inColor1);

	gl_Position = VSOut.Pos;
	Fog = VSOut.Fog;	
	Color = VSOut.Color;
	Tex0 = VSOut.Tex0;
	SunLight = VSOut.SunLight;
	ShadowTexCoord = VSOut.ShadowTexCoord;
	ShadowTexelPos = VSOut.ShadowTexelPos;
	WorldPos = VSOut.WorldPos;
}
