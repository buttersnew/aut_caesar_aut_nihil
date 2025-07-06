uniform vec4 vSunDir;
uniform vec4 vSkyLightDir;
uniform float fFogDensity;
uniform float vWindStrength;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
varying vec4 VertexColor;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying vec4 ShadowTexCoord;
varying float Fog;
varying vec3 ViewDir;
varying vec3 WorldNormal;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2 = tmpvar_1;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  tmpvar_5 = (matWorld * tmpvar_1);
  float tmpvar_6;
  tmpvar_6 = (0.333 * (max (1.5, vWindStrength) * clamp (
    ((inPosition.z * 0.03) - 0.01)
  , 0.0, 0.5)));
  float tmpvar_7;
  tmpvar_7 = (1.0 - inTexCoord.y);
  if ((tmpvar_7 < 0.9)) {
    float treeamp_8;
    float tmpvar_9;
    tmpvar_9 = (1.5 * time_var);
    float tmpvar_10;
    tmpvar_10 = ((1.0 - tmpvar_7) + 0.2);
    treeamp_8 = ((clamp (
      (tmpvar_10 * tmpvar_10)
    , 0.0, 1.0) * 0.9) * tmpvar_6);
    vPosition_2.x = (inPosition.x + (treeamp_8 * sin(
      ((0.025 * tmpvar_5.z) + tmpvar_9)
    )));
    vPosition_2.x = (vPosition_2.x + (treeamp_8 * sin(
      ((0.0125 * tmpvar_5.z) + (0.2 * tmpvar_9))
    )));
    vPosition_2.y = (inPosition.y + (treeamp_8 * sin(
      ((0.019 * tmpvar_5.z) + (1.1 * tmpvar_9))
    )));
    vPosition_2.z = (inPosition.z - (0.3 * (inPosition.x - vPosition_2.x)));
  };
  vec4 tmpvar_11;
  tmpvar_11.w = 0.0;
  tmpvar_11.xyz = inNormal;
  vec3 tmpvar_12;
  tmpvar_12 = normalize((matWorld * tmpvar_11).xyz);
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
  tmpvar_16[2] = tmpvar_12;
  tmpvar_3.xyz = ((2.0 * inColor1.xyz) - 1.0);
  tmpvar_3.w = inColor1.w;
  gl_Position = (matWorldViewProj * vPosition_2);
  VertexColor = inColor0.zyxw;
  Tex0 = inTexCoord;
  SunLightDir = (tmpvar_16 * -(vSunDir.xyz));
  SkyLightDir = (tmpvar_16 * -(vSkyLightDir.xyz));
  PointLightDir = tmpvar_3;
  ShadowTexCoord = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_15, tmpvar_15))
   * fFogDensity))));
  ViewDir = normalize((vCameraPos.xyz - (matWorld * vPosition_2).xyz));
  WorldNormal = tmpvar_12;
}

