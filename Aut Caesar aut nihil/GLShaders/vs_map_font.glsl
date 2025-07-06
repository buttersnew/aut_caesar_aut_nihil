
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;

varying float4 Pos;
varying float Fog;
varying float4 Color;
varying float2 Tex0;
varying float Map;

void main()
{
	VS_OUTPUT_MAP_FONT VSOut;
	VSOut = vs_map_font(float4(inPosition, 1.0), inNormal, inTexCoord, inColor0, inColor1);

	gl_Position = VSOut.Pos;
	Fog = VSOut.Fog;	
	Color = VSOut.Color;
	Tex0 = VSOut.Tex0;
	Map = VSOut.Map;
}
