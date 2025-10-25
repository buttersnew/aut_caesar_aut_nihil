uniform vec4 vMaterialColor;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform float fFogDensity;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
attribute vec3 inPosition;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
varying float Fog;
varying vec4 Color;
varying vec4 Tex0;
varying vec4 SunLight;
varying vec4 ShadowTexCoord;
varying vec2 WorldPos;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2.yw = tmpvar_1.yw;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vPosition_2.z = (inPosition.z + (0.01 * sin(
    ((0.7 * inPosition.y) + (0.5 * time_var))
  )));
  vPosition_2.x = (inPosition.x + (0.015 * sin(
    ((0.9 * inPosition.y) + (0.4 * time_var))
  )));
  vec4 tmpvar_6;
  tmpvar_6 = (matWorld * vPosition_2);
  tmpvar_4.xy = inTexCoord;
  tmpvar_4.z = (0.7 * (tmpvar_6.z - 1.5));
  tmpvar_4.w = tmpvar_6.x;
  vec4 tmpvar_7;
  tmpvar_7.w = 1.0;
  tmpvar_7.xyz = vSunColor.xyz;
  tmpvar_3 = (inColor0.zyxw * (vAmbientColor + (tmpvar_7 * 0.06)));
  tmpvar_3.w = (tmpvar_3.w * vMaterialColor.w);
  vec3 tmpvar_8;
  tmpvar_8 = (matWorldView * vPosition_2).xyz;
  gl_Position = (matWorldViewProj * vPosition_2);
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_8, tmpvar_8))
   * fFogDensity))));
  Color = tmpvar_3;
  Tex0 = tmpvar_4;
  SunLight = ((vSunColor * 0.34) * (vMaterialColor * inColor0.zyxw));
  ShadowTexCoord = tmpvar_5;
  WorldPos = tmpvar_6.xy;
}

