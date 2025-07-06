
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;

varying float2 Tex0;
varying float4 LightDir_Alpha;
varying float4 LightDif;
varying float3 ViewDir;
varying float3 CameraDir;
varying float4 PosWater;
varying float4 projCoord;
varying float Depth;
varying float Fog;

void main()
{
	VS_OUTPUT_PARALLAX_WATER VSOut;
	VSOut = vs_parallax_water(vec4(inPosition, 1.0), inNormal, inColor0, inTexCoord, inTangent, inBinormal);

	gl_Position = VSOut.Pos;
	Tex0 = VSOut.Tex0;
	LightDir_Alpha = VSOut.LightDir_Alpha;
	LightDif = VSOut.LightDif;
	ViewDir = VSOut.ViewDir;
	CameraDir = VSOut.CameraDir;
	PosWater = VSOut.PosWater;
	projCoord = VSOut.projCoord;
	Depth = VSOut.Depth;
	Fog = VSOut.Fog;
}
