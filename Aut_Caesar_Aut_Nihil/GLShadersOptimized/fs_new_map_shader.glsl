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
  vec4 tex_col_2;
  float height_3;
  vec2 parallaxcoords_4;
  vec4 tmpvar_5;
  vec2 tmpvar_6;
  tmpvar_6 = (0.95 * Tex0.xy);
  parallaxcoords_4.y = tmpvar_6.y;
  parallaxcoords_4.x = (tmpvar_6.x + (0.1 * sin(tmpvar_6.y)));
  vec3 tmpvar_7;
  tmpvar_7 = normalize(CameraDir);
  float tmpvar_8;
  tmpvar_8 = (0.01 * vSpecularColor.x);
  float tmpvar_9;
  tmpvar_9 = ((texture2D (env_texture, parallaxcoords_4).w * tmpvar_8) + (tmpvar_8 * -0.5));
  tmpvar_1.xy = (Tex0.xy + (tmpvar_9 * tmpvar_7.xy));
  parallaxcoords_4 = (parallaxcoords_4 + (tmpvar_9 * tmpvar_7.xy));
  vec4 tmpvar_10;
  tmpvar_10 = texture2D (diffuse_texture, tmpvar_1.xy);
  tex_col_2.w = tmpvar_10.w;
  tex_col_2.xyz = pow (tmpvar_10.xyz, vec3(2.2, 2.2, 2.2));
  height_3 = tmpvar_1.z;
  if ((vSeason > 2.5)) {
    height_3 = (Tex0.z * 2.0);
    height_3 += 1.65;
  };
  tex_col_2.xyz = (tex_col_2.xyz + clamp ((
    (height_3 * tmpvar_10.w)
   - 1.5), 0.0, 1.0));
  tex_col_2.w = 1.0;
  tex_col_2.xyz = mix ((tex_col_2.xyz * vec3(0.8, 0.75, 0.65)), (tex_col_2.xyz * 1.3), (1.0 - texture2D (env_texture, parallaxcoords_4).w));
  vec3 tmpvar_11;
  tmpvar_11 = ((2.0 * texture2D (normal_texture, (tmpvar_1.xy * 1.4)).xyz) - 1.0);
  vec4 tmpvar_12;
  tmpvar_12.w = 1.0;
  tmpvar_12.xyz = vSunColor.xyz;
  tmpvar_5.xyz = (tex_col_2 * (Color + (
    (clamp (dot (tmpvar_11, SunLightDir), 0.0, 1.0) * tmpvar_12)
   * vMaterialColor))).xyz;
  tmpvar_5.w = Color.w;
  vec3 tmpvar_13;
  tmpvar_13 = normalize(ViewDir);
  tmpvar_5.xyz = mix (tmpvar_5.xyz, (tmpvar_5.xyz * (
    (1.0 - clamp (dot (tmpvar_13, (
      (2.0 * texture2D (env_texture, parallaxcoords_4).xyz)
     - 1.0)), 0.0, 1.0))
   * 
    (1.0 - clamp (dot (tmpvar_13, tmpvar_11), 0.0, 1.0))
  )), 0.5);
  tmpvar_5.xyz = pow (tmpvar_5.xyz, output_gamma_inv.xyz);
  tmpvar_5.xyz = mix (vFogColor.xyz, tmpvar_5.xyz, Fog);
  gl_FragColor = tmpvar_5;
}

