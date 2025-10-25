
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;

varying float4 Color;
varying float2 Tex0;
varying float3 CameraDir;
varying float4 PosWater;
varying float Fog;
varying float4 projCoord;
varying float2  Depth;
varying float4 LightDir_Alpha;
varying float4 LightDif;

void main()
{
	VS_OUTPUT_MAP_WATER_NEW VSOut;
	VSOut = vs_map_water_new(true, vec4(inPosition, 1.0), inNormal, inTangent, inBinormal, inTexCoord, inColor0, inColor1);

	gl_Position = VSOut.Pos;
	Color = VSOut.Color;
	Tex0 = VSOut.Tex0;
	CameraDir = VSOut.CameraDir;
	PosWater = VSOut.PosWater;
	Fog = VSOut.Fog;
	projCoord = VSOut.projCoord;
	Depth = VSOut.Depth;
	LightDir_Alpha = VSOut.LightDir_Alpha;
	LightDif = VSOut.LightDif;
}
