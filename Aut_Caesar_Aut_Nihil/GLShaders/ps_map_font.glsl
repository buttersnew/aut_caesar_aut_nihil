
varying float Fog;
varying float4 Color;
varying float2 Tex0;
varying float Map;

void main()
{
	VS_OUTPUT_MAP_FONT VSOut;
	VSOut.Fog = Fog;
	VSOut.Color = Color;
	VSOut.Tex0 = Tex0;
	VSOut.Map = Map;

	gl_FragColor = ps_map_font(VSOut).RGBColor;
}
