uniform vec4 vSunDir;
uniform vec4 vSunColor;
uniform float fFogDensity;
uniform float far_clip_Inv;
uniform bool use_depth_effects;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform mat4 matWaterWorldViewProj;
uniform vec4 vCameraPos;
uniform vec4 vDepthRT_HalfPixel_ViewportSizeInv;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
varying vec2 Tex0;
varying vec4 LightDir_Alpha;
varying vec4 LightDif;
varying vec3 ViewDir;
varying vec3 CameraDir;
varying vec4 PosWater;
varying vec4 projCoord;
varying float Depth;
varying float Fog;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2.xyw = tmpvar_1.xyw;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vec3 tmpvar_6;
  vec3 tmpvar_7;
  vec4 tmpvar_8;
  vec4 tmpvar_9;
  float tmpvar_10;
  vPosition_2.z = (inPosition.z + 2.7);
  tmpvar_3 = (matWorldViewProj * vPosition_2);
  tmpvar_8 = (matWaterWorldViewProj * vPosition_2);
  vec3 tmpvar_11;
  tmpvar_11 = (matWorld * vPosition_2).xyz;
  vec4 tmpvar_12;
  tmpvar_12.w = 0.0;
  tmpvar_12.xyz = inNormal;
  vec4 tmpvar_13;
  tmpvar_13.w = 0.0;
  tmpvar_13.xyz = inBinormal;
  vec4 tmpvar_14;
  tmpvar_14.w = 0.0;
  tmpvar_14.xyz = inTangent;
  vec3 tmpvar_15;
  tmpvar_15 = (matWorldView * vPosition_2).xyz;
  mat3 tmpvar_16;
  tmpvar_16[0] = normalize((matWorld * tmpvar_14).xyz);
  tmpvar_16[1] = normalize((matWorld * tmpvar_13).xyz);
  tmpvar_16[2] = normalize((matWorld * tmpvar_12).xyz);
  tmpvar_7 = (tmpvar_16 * normalize((vCameraPos.xyz - tmpvar_11)));
  tmpvar_6.xy = normalize((tmpvar_16 * normalize(
    (vCameraPos.xyz - tmpvar_11)
  ))).xy;
  tmpvar_4.xyz = (tmpvar_16 * -(vSunDir.xyz));
  tmpvar_5 = (vSunColor * inColor0);
  tmpvar_4.w = inColor0.w;
  float tmpvar_17;
  tmpvar_17 = (1.0/(exp2((
    sqrt(dot (tmpvar_15, tmpvar_15))
   * fFogDensity))));
  if (use_depth_effects) {
    vec2 tmpvar_18;
    tmpvar_18.x = tmpvar_3.x;
    tmpvar_18.y = -(tmpvar_3.y);
    tmpvar_9.xy = ((tmpvar_18 + tmpvar_3.w) / 2.0);
    tmpvar_9.xy = (tmpvar_9.xy + (vDepthRT_HalfPixel_ViewportSizeInv.xy * tmpvar_3.w));
    tmpvar_9.zw = tmpvar_3.zw;
    tmpvar_10 = (((0.5 * tmpvar_3.z) + 0.5) * far_clip_Inv);
  };
  gl_Position = tmpvar_3;
  Tex0 = inTexCoord;
  LightDir_Alpha = tmpvar_4;
  LightDif = tmpvar_5;
  ViewDir = tmpvar_6;
  CameraDir = tmpvar_7;
  PosWater = tmpvar_8;
  projCoord = tmpvar_9;
  Depth = tmpvar_10;
  Fog = tmpvar_17;
}

