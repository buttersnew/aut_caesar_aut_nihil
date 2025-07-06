
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
	VSOut.Tex0 = Tex0;
	VSOut.LightDir_Alpha = LightDir_Alpha;
	VSOut.LightDif = LightDif;
	VSOut.ViewDir = ViewDir;
	VSOut.Fog = Fog;
	VSOut.CameraDir = CameraDir;
	VSOut.PosWater = PosWater;
	VSOut.projCoord = projCoord;
	VSOut.Depth = Depth;
	VSOut.Fog = Fog;

	gl_FragColor = ps_parallax_water(VSOut, true, true, false).RGBColor;
}
