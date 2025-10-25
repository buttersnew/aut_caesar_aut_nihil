uniform sampler2D diffuse_texture;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform sampler2D env_texture;
uniform sampler2D shadowmap_texture;
uniform vec4 vMaterialColor;
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
varying vec3 ViewDir;
varying float Fog;
void main ()
{
  vec2 tmpvar_1;
  vec4 tex_col_2;
  float fresnel_3;
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
  total_light_5 = (vAmbientColor + ((
    clamp (dot (SunLightDir, normal_4), 0.0, 1.0)
   * 
    (sun_amount_9 * sun_amount_9)
  ) * vSunColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (SkyLightDir, normal_4)
  , 0.0, 1.0) * vSkyLightColor));
  total_light_5 = (total_light_5 + (clamp (
    dot (PointLightDir.xyz, normal_4)
  , 0.0, 1.0) * vPointLightColor));
  float tmpvar_21;
  tmpvar_21 = (1.0 - clamp (dot (
    normalize(ViewDir)
  , normal_4), 0.0, 1.0));
  fresnel_3 = (0.0204 + ((
    (0.9796 * tmpvar_21)
   * 
    (tmpvar_21 * tmpvar_21)
  ) * (tmpvar_21 * tmpvar_21)));
  total_light_5.xyz = (total_light_5.xyz + (0.5 * (total_light_5.xyz * fresnel_3)));
  vec4 tmpvar_22;
  tmpvar_22 = clamp (total_light_5, 0.0, 1.0);
  total_light_5 = tmpvar_22;
  tmpvar_6.xyz = tmpvar_22.xyz;
  tmpvar_6.w = 1.0;
  tmpvar_6 = (tmpvar_6 * vMaterialColor);
  vec4 tmpvar_23;
  tmpvar_23 = texture2D (diffuse_texture, tmpvar_1);
  tex_col_2 = tmpvar_23;
  if ((vSeason < 0.5)) {
    tex_col_2.xyz = (tmpvar_23.xyz * vec3(0.9, 1.1, 0.9));
  } else {
    if (((vSeason > 0.5) && (vSeason < 1.5))) {
      tex_col_2.xyz = tex_col_2.xyz;
    } else {
      if (((vSeason > 1.5) && (vSeason < 2.5))) {
        tex_col_2.xyz = (tex_col_2.xyz * vec3(1.1, 0.9, 0.9));
      } else {
        if ((vSeason > 2.5)) {
          tex_col_2.xyz = texture2D (env_texture, tmpvar_1).xyz;
        };
      };
    };
  };
  tex_col_2.xyz = pow (tex_col_2.xyz, vec3(2.2, 2.2, 2.2));
  tmpvar_6 = (tmpvar_6 * tex_col_2);
  tmpvar_6 = (tmpvar_6 * VertexColor);
  if ((vSeason < 2.5)) {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * (0.35 + fresnel_3)), dot (tmpvar_22.xyz, vec3(0.3, 0.59, 0.11)));
    tmpvar_6.xyz = mix ((tmpvar_6.xyz * 0.75), (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  } else {
    tmpvar_6.xyz = mix (tmpvar_6.xyz, mix (tmpvar_6.xyz, (tmpvar_6.xyz * 
      (0.35 + fresnel_3)
    ), dot (tmpvar_22.xyz, vec3(0.3, 0.59, 0.11))), 0.5);
    tmpvar_6.xyz = mix (tmpvar_6.xyz, (tmpvar_6.xyz * 1.2), texture2D (specular_texture, tmpvar_1).w);
  };
  tmpvar_6.xyz = pow (tmpvar_6.xyz, output_gamma_inv.xyz);
  tmpvar_6.xyz = mix (vFogColor.xyz, tmpvar_6.xyz, Fog);
  gl_FragColor = tmpvar_6;
}

