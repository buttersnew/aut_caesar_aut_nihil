uniform vec4 vSunDir;
uniform vec4 vSkyLightDir;
uniform float fFogDensity;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec3 inTangent;
attribute vec3 inBinormal;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
varying vec2 Tex0;
varying vec3 SkyDir;
varying vec3 SunDir;
varying vec4 vColor;
varying float Fog;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 tmpvar_2;
  tmpvar_2.w = 0.0;
  tmpvar_2.xyz = inNormal;
  vec4 tmpvar_3;
  tmpvar_3.w = 0.0;
  tmpvar_3.xyz = inBinormal;
  vec4 tmpvar_4;
  tmpvar_4.w = 0.0;
  tmpvar_4.xyz = inTangent;
  mat3 tmpvar_5;
  tmpvar_5[0] = normalize((matWorld * tmpvar_4).xyz);
  tmpvar_5[1] = normalize((matWorld * tmpvar_3).xyz);
  tmpvar_5[2] = normalize((matWorld * tmpvar_2).xyz);
  vec3 tmpvar_6;
  tmpvar_6 = (matWorldView * tmpvar_1).xyz;
  gl_Position = (matWorldViewProj * tmpvar_1);
  Tex0 = inTexCoord;
  SkyDir = (tmpvar_5 * -(vSkyLightDir.xyz));
  SunDir = (tmpvar_5 * -(vSunDir.xyz));
  vColor = inColor0;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_6, tmpvar_6))
   * fFogDensity))));
}

