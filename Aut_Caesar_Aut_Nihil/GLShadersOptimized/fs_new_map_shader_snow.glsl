uniform sampler2D diffuse_texture;
uniform sampler2D normal_texture;
uniform sampler2D env_texture;
uniform vec4 vMaterialColor;
uniform vec4 vSpecularColor;
uniform vec4 vSunColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying vec4 Color;
varying vec4 Tex0;
varying vec3 CameraDir;
varying float Fog;
varying vec3 SunLightDir;
varying vec3 ViewDir;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.zw = Tex0.zw;
  float latitude_2;
  vec4 tex_col_3;
  float height_4;
  vec2 parallaxcoords_5;
  vec4 tmpvar_6;
  vec2 tmpvar_7;
  tmpvar_7 = (0.95 * Tex0.xy);
  parallaxcoords_5.y = tmpvar_7.y;
  parallaxcoords_5.x = (tmpvar_7.x + (0.1 * sin(tmpvar_7.y)));
  vec3 tmpvar_8;
  tmpvar_8 = normalize(CameraDir);
  float tmpvar_9;
  tmpvar_9 = (0.01 * vSpecularColor.x);
  float tmpvar_10;
  tmpvar_10 = ((texture2D (env_texture, parallaxcoords_5).w * tmpvar_9) + (tmpvar_9 * -0.5));
  tmpvar_1.xy = (Tex0.xy + (tmpvar_10 * tmpvar_8.xy));
  parallaxcoords_5 = (parallaxcoords_5 + (tmpvar_10 * tmpvar_8.xy));
  vec4 tmpvar_11;
  tmpvar_11 = texture2D (diffuse_texture, tmpvar_1.xy);
  tex_col_3.w = tmpvar_11.w;
  tex_col_3.xyz = pow (tmpvar_11.xyz, vec3(2.2, 2.2, 2.2));
  height_4 = tmpvar_1.z;
  float tmpvar_12;
  tmpvar_12 = (Tex0.w + 155.0);
  latitude_2 = tmpvar_12;
  if ((vSeason > 2.5)) {
    height_4 = (Tex0.z * 2.0);
    height_4 += 1.0;
    height_4 = (height_4 * 1.5);
  } else {
    height_4 = (height_4 * 2.0);
    height_4 += 1.0;
    latitude_2 = (1.0 - clamp (tmpvar_12, 0.0, 1.0));
    latitude_2 += 0.5;
    height_4 = (height_4 * latitude_2);
  };
  tex_col_3.xyz = (tex_col_3.xyz + clamp ((
    (height_4 * tmpvar_11.w)
   - 1.5), 0.0, 1.0));
  tex_col_3.w = 1.0;
  tex_col_3.xyz = mix ((tex_col_3.xyz * vec3(0.8, 0.75, 0.65)), (tex_col_3.xyz * 1.3), (1.0 - texture2D (env_texture, parallaxcoords_5).w));
  vec3 tmpvar_13;
  tmpvar_13 = ((2.0 * texture2D (normal_texture, (tmpvar_1.xy * 1.4)).xyz) - 1.0);
  tmpvar_6.xyz = (tex_col_3 * (Color + (
    (clamp (dot (tmpvar_13, SunLightDir), 0.0, 1.0) * vSunColor)
   * vMaterialColor))).xyz;
  tmpvar_6.w = Color.w;
  vec3 tmpvar_14;
  tmpvar_14 = normalize(ViewDir);
  tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * (
    (1.0 - clamp (dot (tmpvar_14, (
      (2.0 * texture2D (env_texture, parallaxcoords_5).xyz)
     - 1.0)), 0.0, 1.0))
   * 
    (1.0 - clamp (dot (tmpvar_14, tmpvar_13), 0.0, 1.0))
  )), 0.5);
  tmpvar_6.xyz = pow (tmpvar_6.xyz, output_gamma_inv.xyz);
  tmpvar_6.xyz = mix (vFogColor.xyz, tmpvar_6.xyz, Fog);
  gl_FragColor = tmpvar_6;
}

