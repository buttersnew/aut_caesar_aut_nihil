uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
uniform float time_var;
varying float Fog;
varying vec4 Color;
varying vec4 Tex0;
varying vec4 SunLight;
void main ()
{
  float height_1;
  vec4 tex_col_2;
  vec4 wave_amp_3;
  vec2 TexCoord_4;
  vec4 tmpvar_5;
  TexCoord_4.y = Tex0.y;
  vec4 tmpvar_6;
  tmpvar_6 = texture2D (specular_texture, Tex0.xy);
  wave_amp_3.yzw = tmpvar_6.yzw;
  wave_amp_3.x = clamp ((tmpvar_6.x * 0.01), 0.0, 1.0);
  TexCoord_4.x = (Tex0.x + (wave_amp_3.x * sin(
    ((10.9 * Tex0.y) + (0.7 * time_var))
  )));
  vec4 tmpvar_7;
  tmpvar_7 = texture2D (diffuse_texture, TexCoord_4);
  tex_col_2.w = tmpvar_7.w;
  if (((tmpvar_7.w - 0.9) < 0.0)) {
    discard;
  };
  vec4 tmpvar_8;
  tmpvar_8 = texture2D (diffuse_texture_2, TexCoord_4);
  tex_col_2.xyz = pow (tmpvar_7.xyz, vec3(2.2, 2.2, 2.2));
  height_1 = Tex0.z;
  if ((vSeason > 2.5)) {
    height_1 = (Tex0.z * 2.0);
    height_1 = (height_1 - 0.7);
  } else {
    height_1 = (height_1 * 0.1);
  };
  vec4 tmpvar_9;
  tmpvar_9 = mix (tex_col_2, tmpvar_8, clamp ((height_1 - 1.5), 0.0, 1.0));
  tex_col_2 = tmpvar_9;
  tmpvar_5 = (tmpvar_9 * (Color + SunLight));
  tmpvar_5.xyz = pow (tmpvar_5.xyz, output_gamma_inv.xyz);
  tmpvar_5.xyz = mix (vFogColor.xyz, tmpvar_5.xyz, Fog);
  gl_FragColor = tmpvar_5;
}

