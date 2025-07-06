uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform sampler2D env_texture;
uniform vec4 vSpecularColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma;
uniform vec4 output_gamma_inv;
uniform float time_var;
varying vec4 Color;
varying vec2 Tex0;
varying vec3 CameraDir;
varying vec4 PosWater;
varying float Fog;
varying vec2 Depth;
varying vec4 LightDir_Alpha;
varying vec4 LightDif;
void main ()
{
  vec2 tmpvar_1;
  vec2 oceanfloorcord_2;
  vec3 cWaterColor_3;
  vec4 tex_4;
  vec3 normal2_5;
  vec3 normal_6;
  float offset_7;
  float height_8;
  float bias_9;
  float volume_10;
  float factor_11;
  vec4 tmpvar_12;
  tmpvar_1 = (Tex0 * 1.5);
  float tmpvar_13;
  tmpvar_13 = (0.2 * time_var);
  vec3 tmpvar_14;
  tmpvar_14 = normalize(CameraDir);
  float tmpvar_15;
  tmpvar_15 = (0.01 * vSpecularColor.x);
  factor_11 = tmpvar_15;
  float tmpvar_16;
  tmpvar_16 = (tmpvar_15 * 1.4);
  volume_10 = tmpvar_16;
  float tmpvar_17;
  tmpvar_17 = (tmpvar_15 * -0.7);
  bias_9 = tmpvar_17;
  vec2 tmpvar_18;
  tmpvar_18.x = (tmpvar_1.x + (0.25 * tmpvar_13));
  tmpvar_18.y = tmpvar_1.y;
  vec4 tmpvar_19;
  tmpvar_19 = texture2D (diffuse_texture_2, tmpvar_18);
  height_8 = tmpvar_19.w;
  float tmpvar_20;
  tmpvar_20 = ((tmpvar_19.w * tmpvar_16) + tmpvar_17);
  offset_7 = tmpvar_20;
  vec2 tmpvar_21;
  tmpvar_21.x = tmpvar_1.x;
  tmpvar_21.y = (tmpvar_1.y + (0.15 * tmpvar_13));
  tmpvar_1 = (tmpvar_1 + (tmpvar_20 * tmpvar_14.xy));
  tmpvar_1 = (tmpvar_1 + ((
    (texture2D (diffuse_texture_2, tmpvar_21).w * tmpvar_16)
   + tmpvar_17) * tmpvar_14.xy));
  vec2 tmpvar_22;
  tmpvar_22.x = (tmpvar_1.x + (0.25 * tmpvar_13));
  tmpvar_22.y = tmpvar_1.y;
  normal_6.xy = ((2.0 * texture2D (normal_texture, tmpvar_22).wy) - 1.0);
  normal_6.z = sqrt((1.0 - dot (normal_6.xy, normal_6.xy)));
  vec2 tmpvar_23;
  tmpvar_23.x = tmpvar_1.x;
  tmpvar_23.y = (tmpvar_1.y + (0.15 * tmpvar_13));
  normal2_5.xy = ((2.0 * texture2D (normal_texture, tmpvar_23).wy) - 1.0);
  normal2_5.z = sqrt((1.0 - dot (normal2_5.xy, normal2_5.xy)));
  vec3 tmpvar_24;
  tmpvar_24 = mix (normal_6, normal2_5, 0.5);
  normal_6 = tmpvar_24;
  float tmpvar_25;
  tmpvar_25 = clamp ((Depth.y * 0.0075), 0.0, 1.0);
  tmpvar_12.xyz = ((0.01 * clamp (
    dot (tmpvar_24, LightDir_Alpha.xyz)
  , 0.0, 1.0)) * LightDif).xyz;
  vec2 tmpvar_26;
  tmpvar_26.x = (0.5 + (0.5 * (PosWater.x / PosWater.w)));
  tmpvar_26.y = (0.5 - (0.5 * (PosWater.y / PosWater.w)));
  vec2 tmpvar_27;
  tmpvar_27 = ((0.25 * tmpvar_24.xy) + tmpvar_26);
  vec2 tmpvar_28;
  tmpvar_28.x = tmpvar_27.x;
  tmpvar_28.y = (1.0 - tmpvar_27.y);
  vec4 tmpvar_29;
  tmpvar_29 = texture2D (env_texture, tmpvar_28);
  tex_4.w = tmpvar_29.w;
  tex_4.xyz = pow (tmpvar_29.xyz, output_gamma.xyz);
  float tmpvar_30;
  tmpvar_30 = (1.0 - clamp (dot (tmpvar_14, tmpvar_24), 0.0, 1.0));
  vec3 tmpvar_31;
  tmpvar_31 = clamp ((tex_4.xyz * (0.0204 + 
    (((0.9796 * tmpvar_30) * (tmpvar_30 * tmpvar_30)) * (tmpvar_30 * tmpvar_30))
  )), 0.0, 1.0);
  float tmpvar_32;
  tmpvar_32 = clamp (((Color.w - 0.361) * 2.0), 0.0, 1.0);
  tmpvar_12.w = (1.0 - (0.3 * CameraDir.z));
  tmpvar_12.w = (tmpvar_12.w * LightDir_Alpha.w);
  cWaterColor_3 = (mix (mix (vec3(0.009803922, 0.04901961, 0.09803922), vec3(0.02352941, 0.1176471, 0.2352941), 
    (1.0 - texture2D (diffuse_texture_2, tmpvar_22).w)
  ), vec3(0.01960784, 0.09803922, 0.1960784), tmpvar_25) * ((1.0 - 
    clamp (dot (CameraDir, tmpvar_24), 0.0, 1.0)
  ) * max (0.25, Color.x)));
  if ((CameraDir.z > 0.5)) {
    tmpvar_12.xyz = (tmpvar_12.xyz + mix ((cWaterColor_3 + tmpvar_31), (
      (12.0 * cWaterColor_3)
     + 
      (5.0 * tmpvar_31)
    ), (CameraDir.z - 0.5)));
  } else {
    tmpvar_12.xyz = (tmpvar_12.xyz + (cWaterColor_3 + tmpvar_31));
  };
  vec2 tmpvar_33;
  tmpvar_33.x = (2.0 * tmpvar_1.x);
  tmpvar_33.y = ((2.0 * tmpvar_1.y) - (0.1 * tmpvar_13));
  factor_11 = (0.01 * vSpecularColor.x);
  volume_10 = (factor_11 * 20.0);
  bias_9 = (factor_11 * -10.0);
  height_8 = (1.0 - (0.5 * tmpvar_32));
  offset_7 = ((height_8 * volume_10) + bias_9);
  tmpvar_1.y = (tmpvar_1.y * 1.333);
  oceanfloorcord_2 = (tmpvar_1 - (offset_7 * normalize(CameraDir).xy));
  oceanfloorcord_2 = (oceanfloorcord_2 * 2.0);
  if ((tmpvar_32 > 0.08)) {
    vec3 FoamColor_34;
    vec3 caustics_35;
    vec3 tmpvar_36;
    tmpvar_36 = max (vec3(0.25, 0.25, 0.25), Color.xyz);
    tmpvar_12.xyz = mix ((tmpvar_12.xyz + (
      ((0.5 * (tmpvar_32 - 0.08)) * texture2D (specular_texture, oceanfloorcord_2).xyz)
     * tmpvar_36)), (tmpvar_12.xyz + (
      ((0.17 * (tmpvar_32 - 0.08)) * texture2D (specular_texture, oceanfloorcord_2).xyz)
     * tmpvar_36)), clamp ((tmpvar_25 * 1.8), 0.0, 1.0));
    vec2 tmpvar_37;
    tmpvar_37.x = ((0.4 * oceanfloorcord_2.x) - (0.08 * time_var));
    tmpvar_37.y = ((0.4 * oceanfloorcord_2.x) - (0.089 * time_var));
    caustics_35 = ((0.5 * clamp (
      ((tmpvar_32 - 0.08) * texture2D (specular_texture, ((0.4 * oceanfloorcord_2) + (0.075 * time_var))).www)
    , 0.0, 1.0)) + (0.5 * clamp (
      ((tmpvar_32 - 0.08) * texture2D (specular_texture, tmpvar_37).www)
    , 0.0, 1.0)));
    caustics_35 = (caustics_35 * 0.5);
    caustics_35 = (caustics_35 * vec3(0.2, 0.2, 1.0));
    caustics_35 = (caustics_35 * tmpvar_36);
    tmpvar_12.xyz = mix ((tmpvar_12.xyz + (0.95 * caustics_35)), (tmpvar_12.xyz + (0.25 * caustics_35)), clamp ((tmpvar_25 * 1.5), 0.0, 1.0));
    float tmpvar_38;
    tmpvar_38 = texture2D (diffuse_texture, tmpvar_33).w;
    FoamColor_34 = (clamp (vec3((0.4 * 
      ((tmpvar_32 - 0.08) * (tmpvar_38 * tmpvar_38))
    )), 0.0, 1.0) * tmpvar_36);
    tmpvar_12.xyz = mix ((tmpvar_12.xyz + (0.95 * FoamColor_34)), (tmpvar_12.xyz + (0.1 * FoamColor_34)), clamp ((tmpvar_25 * 2.0), 0.0, 1.0));
  };
  tmpvar_12.w = 1.0;
  tmpvar_12.xyz = pow (tmpvar_12.xyz, output_gamma_inv.xyz);
  tmpvar_12.w = clamp (1.0, 0.0, 1.0);
  tmpvar_12.xyz = mix (vFogColor.xyz, tmpvar_12.xyz, Fog);
  gl_FragColor = tmpvar_12;
}

