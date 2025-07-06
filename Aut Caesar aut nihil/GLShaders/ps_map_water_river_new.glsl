
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
	VSOut.Color = Color;
	VSOut.Tex0 = Tex0;
	VSOut.CameraDir = CameraDir;
	VSOut.PosWater = PosWater;
	VSOut.Fog = Fog;
	VSOut.projCoord = projCoord;
	VSOut.Depth = Depth;
	VSOut.LightDir_Alpha = LightDir_Alpha;
	VSOut.LightDif = LightDif;

	gl_FragColor = ps_map_water_river_new(true, VSOut).RGBColor;
}
