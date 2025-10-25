uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform sampler2D env_texture;
uniform sampler2D shadowmap_texture;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightColor;
uniform vec4 vPointLightColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
uniform float fShadowMapNextPixel;
uniform float fShadowMapSize;
varying vec4 VertexColor;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying vec4 ShadowTexCoord;
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
  float sun_amount_10;
  sun_amount_10 = 0.0;
  vec2 tmpvar_11;
  tmpvar_11 = fract((ShadowTexCoord.xy * fShadowMapSize));
  vec4 tmpvar_12;
  tmpvar_12 = texture2D (shadowmap_texture, ShadowTexCoord.xy);
  float tmpvar_13;
  if ((tmpvar_12.x < ShadowTexCoord.z)) {
    tmpvar_13 = 0.0;
  } else {
    tmpvar_13 = 1.0;
  };
  vec2 tmpvar_14;
  tmpvar_14.y = 0.0;
  tmpvar_14.x = fShadowMapNextPixel;
  vec4 tmpvar_15;
  tmpvar_15 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + tmpvar_14));
  float tmpvar_16;
  if ((tmpvar_15.x < ShadowTexCoord.z)) {
    tmpvar_16 = 0.0;
  } else {
    tmpvar_16 = 1.0;
  };
  vec2 tmpvar_17;
  tmpvar_17.x = 0.0;
  tmpvar_17.y = fShadowMapNextPixel;
  vec4 tmpvar_18;
  tmpvar_18 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + tmpvar_17));
  float tmpvar_19;
  if ((tmpvar_18.x < ShadowTexCoord.z)) {
    tmpvar_19 = 0.0;
  } else {
    tmpvar_19 = 1.0;
  };
  vec4 tmpvar_20;
  tmpvar_20 = texture2D (shadowmap_texture, (ShadowTexCoord.xy + vec2(fShadowMapNextPixel)));
  float tmpvar_21;
  if ((tmpvar_20.x < ShadowTexCoord.z)) {
    tmpvar_21 = 0.0;
  } else {
    tmpvar_21 = 1.0;
  };
  sun_amount_10 = clamp (mix (mix (tmpvar_13, tmpvar_16, tmpvar_11.x), mix (tmpvar_19, tmpvar_21, tmpvar_11.x), tmpvar_11.y), 0.0, 1.0);
  total_light_5 = (vAmbientColor + ((
    clamp (dot (SunLightDir, normal_4), 0.0, 1.0)
   * sun_amount_10) * vSunColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (SkyLightDir, normal_4)
  , 0.0, 1.0) * vSkyLightColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (PointLightDir.xyz, normal_4)
  , 0.0, 1.0) * vPointLightColor));
  float tmpvar_22;
  tmpvar_22 = (1.0 - clamp (dot (
    normalize(ViewDir)
  , normal_4), 0.0, 1.0));
  fresnel_2 = (0.0204 + ((
    (0.9796 * tmpvar_22)
   * 
    (tmpvar_22 * tmpvar_22)
  ) * (tmpvar_22 * tmpvar_22)));
  total_light_5.xyz = (total_light_5.xyz + (0.5 * (total_light_5.xyz * fresnel_2)));
  vec4 tmpvar_23;
  tmpvar_23 = clamp (total_light_5, 0.0, 1.0);
  total_light_5 = tmpvar_23;
  tmpvar_6.xyz = tmpvar_23.xyz;
  tmpvar_6.w = 1.0;
  tmpvar_6 = (tmpvar_6 * multi_tex_col_3);
  tmpvar_6.xyz = (tmpvar_6.xyz * VertexColor.xyz);
  tmpvar_6.w = (tmpvar_6.w * PointLightDir.w);
  if ((vSeason < 2.5)) {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * (0.35 + fresnel_2)), dot (tmpvar_23.xyz, vec3(0.3, 0.59, 0.11)));
    tmpvar_6.xyz = mix ((tmpvar_6.xyz * 0.75), (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  } else {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, mix (tmpvar_6.xyz, (tmpvar_6.xyz * 
      (0.35 + fresnel_2)
    ), dot (tmpvar_23.xyz, vec3(0.3, 0.59, 0.11))), 0.5);
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  };
  tmpvar_6.xyz = pow (tmpvar_6.xyz, output_gamma_inv.xyz);
  tmpvar_6.xyz = mix (vFogColor.xyz, tmpvar_6.xyz, Fog);
  gl_FragColor = tmpvar_6;
}

