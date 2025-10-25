uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform sampler2D shadowmap_texture;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
uniform float fShadowMapNextPixel;
uniform float fShadowMapSize;
varying float Fog;
varying vec4 Color;
varying vec4 Tex0;
varying vec4 SunLight;
varying vec4 ShadowTexCoord;
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
  float sun_amount_9;
  sun_amount_9 = 0.0;
  vec2 tmpvar_10;
  tmpvar_10 = fract((ShadowTexCoord.xy * fShadowMapSize));
  vec4 tmpvar_11;
  tmpvar_11 = texture2D (shadowmap_texture, ShadowTexCoord.xy);
  float tmpvar_12;
  if ((tmpvar_11.x < ShadowTexCoord.z)) {
    tmpvar_12 = 0.0;
  } else {
    tmpvar_12 = 1.0;
  };
  vec2 tmpvar_13;
  tmpvar_13.y = 0.0;
  tmpvar_13.x = fShadowMapNextPixel;
  vec4 tmpvar_14;
  tmpvar_14 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + tmpvar_13));
  float tmpvar_15;
  if ((tmpvar_14.x < ShadowTexCoord.z)) {
    tmpvar_15 = 0.0;
  } else {
    tmpvar_15 = 1.0;
  };
  vec2 tmpvar_16;
  tmpvar_16.x = 0.0;
  tmpvar_16.y = fShadowMapNextPixel;
  vec4 tmpvar_17;
  tmpvar_17 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + tmpvar_16));
  float tmpvar_18;
  if ((tmpvar_17.x < ShadowTexCoord.z)) {
    tmpvar_18 = 0.0;
  } else {
    tmpvar_18 = 1.0;
  };
  vec4 tmpvar_19;
  tmpvar_19 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + vec2(fShadowMapNextPixel)));
  float tmpvar_20;
  if ((tmpvar_19.x < ShadowTexCoord.z)) {
    tmpvar_20 = 0.0;
  } else {
    tmpvar_20 = 1.0;
  };
  sun_amount_9 = clamp (mix (mix (tmpvar_12, tmpvar_15, tmpvar_10.x), mix (tmpvar_18, tmpvar_20, tmpvar_10.x), tmpvar_10.y), 0.0, 1.0);
  tmpvar_4 = (tmpvar_8 * (Color + (SunLight * sun_amount_9)));
  tmpvar_4.xyz = pow (tmpvar_4.xyz, output_gamma_inv.xyz);
  tmpvar_4.xyz = mix (vFogColor.xyz, tmpvar_4.xyz, Fog);
  gl_FragColor = tmpvar_4;
}

