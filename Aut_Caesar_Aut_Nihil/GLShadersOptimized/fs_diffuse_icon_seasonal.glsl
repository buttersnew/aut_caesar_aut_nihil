uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying float Fog;
varying vec4 Color;
varying vec4 Tex0;
varying vec4 SunLight;
void main ()
{
  float height_1;
  float snow_amount_2;
  vec4 tex_col_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  tmpvar_5 = texture2D (diffuse_texture_2, Tex0.xy);
  tex_col_3.w = tmpvar_5.w;
  if (((tmpvar_5.w - 0.5) < 0.0)) {
    discard;
  };
  tex_col_3.xyz = pow (tmpvar_5.xyz, vec3(2.2, 2.2, 2.2));
  vec4 tmpvar_6;
  tmpvar_6 = texture2D (diffuse_texture, Tex0.xy);
  vec4 tmpvar_7;
  tmpvar_7 = texture2D (specular_texture, Tex0.xy);
  snow_amount_2 = tmpvar_7.w;
  height_1 = Tex0.z;
  if ((vSeason > 2.5)) {
    height_1 = (Tex0.z * 2.0);
    height_1 += 1.0;
  };
  snow_amount_2 = (clamp ((
    (height_1 * tmpvar_7.w)
   - 1.5), 0.0, 1.0) * texture2D (normal_texture, Tex0.xy).x);
  vec4 tmpvar_8;
  tmpvar_8 = mix (tex_col_3, tmpvar_6, snow_amount_2);
  tex_col_3 = tmpvar_8;
  tmpvar_4 = (tmpvar_8 * (Color + SunLight));
  tmpvar_4.xyz = pow (tmpvar_4.xyz, output_gamma_inv.xyz);
  tmpvar_4.xyz = mix (vFogColor.xyz, tmpvar_4.xyz, Fog);
  gl_FragColor = tmpvar_4;
}

