uniform vec4 vMaterialColor;
uniform vec4 vSunDir;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightDir;
uniform vec4 vSkyLightColor;
uniform float fFogDensity;
uniform float far_clip_Inv;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform mat4 matWaterWorldViewProj;
uniform vec4 vCameraPos;
uniform vec4 vDepthRT_HalfPixel_ViewportSizeInv;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
varying vec4 Color;
varying vec2 Tex0;
varying vec3 CameraDir;
varying vec4 PosWater;
varying float Fog;
varying vec4 projCoord;
varying vec2 Depth;
varying vec4 LightDir_Alpha;
varying vec4 LightDif;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2 = tmpvar_1;
  vec4 diffuse_light_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vec2 tmpvar_6;
  vec4 tmpvar_7;
  vec2 tmpvar_8;
  vec4 tmpvar_9;
  vec4 tmpvar_10;
  vec4 tmpvar_11;
  tmpvar_11 = (matWorld * tmpvar_1);
  if ((inPosition.z < 0.7)) {
    vPosition_2.z = (inPosition.z + (0.07 * sin(
      ((20.0 * inTexCoord.x) + time_var)
    )));
    vPosition_2.z = (vPosition_2.z + (0.08 * sin(
      ((13.0 * inTexCoord.y) + time_var)
    )));
  };
  tmpvar_4 = (matWorldViewProj * vPosition_2);
  vec4 tmpvar_12;
  tmpvar_12 = (matWorld * vPosition_2);
  vec4 tmpvar_13;
  tmpvar_13.w = 0.0;
  tmpvar_13.xyz = inNormal;
  vec3 tmpvar_14;
  tmpvar_14 = normalize((matWorld * tmpvar_13).xyz);
  vec4 tmpvar_15;
  tmpvar_15.w = 0.0;
  tmpvar_15.xyz = inBinormal;
  vec4 tmpvar_16;
  tmpvar_16.w = 0.0;
  tmpvar_16.xyz = inTangent;
  mat3 tmpvar_17;
  tmpvar_17[0] = normalize((matWorld * tmpvar_16).xyz);
  tmpvar_17[1] = normalize((matWorld * tmpvar_15).xyz);
  tmpvar_17[2] = tmpvar_14;
  vec3 tmpvar_18;
  tmpvar_18 = (matWorldView * vPosition_2).xyz;
  tmpvar_6 = (0.065 * tmpvar_12.xy);
  tmpvar_6.y = (tmpvar_6.y * 0.75);
  vec4 tmpvar_19;
  tmpvar_19 = (vAmbientColor + inColor1.zyxw);
  diffuse_light_3.w = tmpvar_19.w;
  diffuse_light_3.xyz = (tmpvar_19.xyz + (clamp (
    dot (tmpvar_14, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor.xyz));
  vec3 tmpvar_20;
  tmpvar_20 = -(vSunDir.xyz);
  diffuse_light_3.xyz = (diffuse_light_3.xyz + (max (-0.0001, 
    dot (tmpvar_14, tmpvar_20)
  ) * vSunColor.xyz));
  tmpvar_5.xyz = ((vMaterialColor * inColor0.zyxw) * diffuse_light_3).xyz;
  tmpvar_5.w = tmpvar_11.z;
  vec2 tmpvar_21;
  tmpvar_21.x = tmpvar_4.x;
  tmpvar_21.y = -(tmpvar_4.y);
  tmpvar_7.xy = ((tmpvar_21 + tmpvar_4.ww) / 2.0);
  tmpvar_7.xy = (tmpvar_7.xy + (vDepthRT_HalfPixel_ViewportSizeInv.xy * tmpvar_4.w));
  tmpvar_7.zw = tmpvar_4.zw;
  tmpvar_8.x = (((0.5 * tmpvar_4.z) + 0.5) * far_clip_Inv);
  tmpvar_10.w = 0.0;
  tmpvar_9.xyz = (tmpvar_17 * tmpvar_20);
  tmpvar_10.xyz = (vSunColor.xyz * inColor0.zyx);
  tmpvar_9.w = inColor0.w;
  vec3 tmpvar_22;
  tmpvar_22 = (vCameraPos.xyz - tmpvar_12.xyz);
  tmpvar_8.y = sqrt(dot (tmpvar_22, tmpvar_22));
  gl_Position = tmpvar_4;
  Color = tmpvar_5;
  Tex0 = tmpvar_6;
  CameraDir = (tmpvar_17 * normalize((vCameraPos.xyz - tmpvar_12.xyz)));
  PosWater = (matWaterWorldViewProj * vPosition_2);
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_18, tmpvar_18))
   * fFogDensity))));
  projCoord = tmpvar_7;
  Depth = tmpvar_8;
  LightDir_Alpha = tmpvar_9;
  LightDif = tmpvar_10;
}

