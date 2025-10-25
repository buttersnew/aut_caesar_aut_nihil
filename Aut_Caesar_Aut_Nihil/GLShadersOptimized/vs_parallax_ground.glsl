uniform vec4 vSunDir;
uniform vec4 vSkyLightDir;
uniform float fFogDensity;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
varying vec4 VertexColor;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying vec4 ShadowTexCoord;
varying vec3 ViewDir;
varying vec4 WorldNormal;
varying float Fog;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 tmpvar_2;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  tmpvar_5.w = 0.0;
  tmpvar_5.xyz = inNormal;
  vec3 tmpvar_6;
  tmpvar_6 = normalize((matWorld * tmpvar_5).xyz);
  vec4 tmpvar_7;
  tmpvar_7.w = 0.0;
  tmpvar_7.xyz = inBinormal;
  vec4 tmpvar_8;
  tmpvar_8.w = 0.0;
  tmpvar_8.xyz = inTangent;
  vec3 tmpvar_9;
  tmpvar_9 = (matWorldView * tmpvar_1).xyz;
  mat3 tmpvar_10;
  tmpvar_10[0] = normalize((matWorld * tmpvar_8).xyz);
  tmpvar_10[1] = normalize((matWorld * tmpvar_7).xyz);
  tmpvar_10[2] = tmpvar_6;
  tmpvar_2.xyz = ((2.0 * inColor1.xyz) - 1.0);
  tmpvar_2.w = inColor1.w;
  vec3 tmpvar_11;
  tmpvar_11 = normalize((tmpvar_10 * normalize(
    (vCameraPos.xyz - (matWorld * tmpvar_1).xyz)
  )));
  tmpvar_4.xyz = tmpvar_6;
  tmpvar_4.w = (1.0 - clamp (dot (tmpvar_11, tmpvar_6), 0.0, 1.0));
  gl_Position = (matWorldViewProj * tmpvar_1);
  VertexColor = inColor0.zyxw;
  Tex0 = inTexCoord;
  SunLightDir = (tmpvar_10 * -(vSunDir.xyz));
  SkyLightDir = (tmpvar_10 * -(vSkyLightDir.xyz));
  PointLightDir = tmpvar_2;
  ShadowTexCoord = tmpvar_3;
  ViewDir = tmpvar_11;
  WorldNormal = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_9, tmpvar_9))
   * fFogDensity))));
}

