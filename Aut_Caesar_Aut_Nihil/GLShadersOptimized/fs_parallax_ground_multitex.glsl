uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform sampler2D env_texture;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightColor;
uniform vec4 vPointLightColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying vec4 VertexColor;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying float Fog;
varying vec3 ViewDir;
void main ()
{
  vec2 tmpvar_1;
  float fresnel_2;
  vec4 multi_tex_col_3;
  vec3 normal_4;
  vec4 total_light_5;
  vec4 tmpvar_6;
  total_light_5 = vAmbientColor;
  vec4 tmpvar_7;
  tmpvar_7 = texture2D (specular_texture, Tex0);
  tmpvar_1 = (Tex0 + ((
    ((tmpvar_7.w * 0.063) + -0.0315)
   * tmpvar_7.z) * ViewDir.xy));
  vec4 tmpvar_8;
  tmpvar_8 = texture2D (normal_texture, vec2(0.5, 0.5));
  if ((tmpvar_8.x > 0.005)) {
    normal_4 = ((2.0 * texture2D (normal_texture, tmpvar_1).xyz) - 1.0);
  } else {
    normal_4.xy = ((2.0 * texture2D (normal_texture, tmpvar_1).wy) - 1.0);
    normal_4.z = sqrt((1.0 - dot (normal_4.xy, normal_4.xy)));
  };
  vec4 tmpvar_9;
  tmpvar_9 = texture2D (diffuse_texture, tmpvar_1);
  multi_tex_col_3.w = tmpvar_9.w;
  multi_tex_col_3.xyz = (tmpvar_9.xyz * (1.0 - VertexColor.w));
  multi_tex_col_3.xyz = (multi_tex_col_3.xyz + (texture2D (diffuse_texture_2, (tmpvar_1 * 1.237)).xyz * VertexColor.w));
  multi_tex_col_3.xyz = pow (multi_tex_col_3.xyz, vec3(2.2, 2.2, 2.2));
  if ((vSeason < 0.5)) {
    multi_tex_col_3.xyz = (multi_tex_col_3.xyz * vec3(0.9, 1.1, 0.9));
  } else {
    if (((vSeason > 0.5) && (vSeason < 1.5))) {
      multi_tex_col_3.xyz = multi_tex_col_3.xyz;
    } else {
      if (((vSeason > 1.5) && (vSeason < 2.5))) {
        multi_tex_col_3.xyz = (multi_tex_col_3.xyz * vec3(1.1, 0.9, 0.9));
      } else {
        if ((vSeason > 2.5)) {
          multi_tex_col_3.xyz = mix (vec3(dot (multi_tex_col_3.xyz, vec3(0.3, 0.59, 0.11))), multi_tex_col_3.xyz, 0.75);
          multi_tex_col_3.xyz = mix (multi_tex_col_3.xyz, texture2D (env_texture, tmpvar_1).xyz, clamp (1.0, 0.0, 1.0));
        };
      };
    };
  };
  total_light_5 = (vAmbientColor + (clamp (
    dot (SunLightDir, normal_4)
  , 0.0, 1.0) * vSunColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (SkyLightDir, normal_4)
  , 0.0, 1.0) * vSkyLightColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (PointLightDir.xyz, normal_4)
  , 0.0, 1.0) * vPointLightColor));
  float tmpvar_10;
  tmpvar_10 = (1.0 - clamp (dot (
    normalize(ViewDir)
  , normal_4), 0.0, 1.0));
  fresnel_2 = (0.0204 + ((
    (0.9796 * tmpvar_10)
   * 
    (tmpvar_10 * tmpvar_10)
  ) * (tmpvar_10 * tmpvar_10)));
  total_light_5.xyz = (total_light_5.xyz + (0.5 * (total_light_5.xyz * fresnel_2)));
  vec4 tmpvar_11;
  tmpvar_11 = clamp (total_light_5, 0.0, 1.0);
  total_light_5 = tmpvar_11;
  tmpvar_6.xyz = tmpvar_11.xyz;
  tmpvar_6.w = 1.0;
  tmpvar_6 = (tmpvar_6 * multi_tex_col_3);
  tmpvar_6.xyz = (tmpvar_6.xyz * VertexColor.xyz);
  tmpvar_6.w = (tmpvar_6.w * PointLightDir.w);
  if ((vSeason < 2.5)) {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * (0.35 + fresnel_2)), dot (tmpvar_11.xyz, vec3(0.3, 0.59, 0.11)));
    tmpvar_6.xyz = mix ((tmpvar_6.xyz * 0.75), (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  } else {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, mix (tmpvar_6.xyz, (tmpvar_6.xyz * 
      (0.35 + fresnel_2)
    ), dot (tmpvar_11.xyz, vec3(0.3, 0.59, 0.11))), 0.5);
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  };
  tmpvar_6.xyz = pow (tmpvar_6.xyz, output_gamma_inv.xyz);
  tmpvar_6.xyz = mix (vFogColor.xyz, tmpvar_6.xyz, Fog);
  gl_FragColor = tmpvar_6;
}

