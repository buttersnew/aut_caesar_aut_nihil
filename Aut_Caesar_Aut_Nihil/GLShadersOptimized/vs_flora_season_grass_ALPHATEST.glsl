uniform vec4 vMaterialColor;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform float fFogDensity;
uniform float vSeason;
uniform float vWindStrength;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
attribute vec3 inPosition;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
varying float Fog;
varying vec4 Color;
varying vec2 Tex0;
varying vec4 SunLight;
varying vec4 ShadowTexCoord;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2.yzw = tmpvar_1.yzw;
  vec2 coords_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vec4 tmpvar_6;
  vec4 tmpvar_7;
  tmpvar_7 = (matWorld * tmpvar_1);
  float tmpvar_8;
  tmpvar_8 = (0.333 * (max (1.5, vWindStrength) * clamp (
    ((inPosition.z * 0.03) - 0.01)
  , 0.0, 0.5)));
  float tmpvar_9;
  tmpvar_9 = (1.5 * time_var);
  vPosition_2.x = (inPosition.x + ((tmpvar_8 * 0.45) * sin(
    ((0.025 * tmpvar_7.z) + tmpvar_9)
  )));
  vPosition_2.x = (vPosition_2.x + ((tmpvar_8 * 0.45) * sin(
    ((0.0125 * tmpvar_7.z) + (0.2 * tmpvar_9))
  )));
  vPosition_2.y = (inPosition.y + ((tmpvar_8 * 0.45) * sin(
    ((0.019 * tmpvar_7.z) + (1.1 * tmpvar_9))
  )));
  vPosition_2.z = (inPosition.z - (0.3 * (inPosition.x - vPosition_2.x)));
  tmpvar_4 = (matWorldViewProj * vPosition_2);
  coords_3.y = inTexCoord.y;
  float tmpvar_10;
  tmpvar_10 = (1.0 - inTexCoord.y);
  coords_3.x = (inTexCoord.x + ((
    (tmpvar_8 * 1.5)
   * 
    (0.033 * (1.0 - tmpvar_10))
  ) * sin(
    ((5.0 * (1.0 - tmpvar_10)) + (1.75 * tmpvar_9))
  )));
  coords_3.x = (coords_3.x + ((
    (tmpvar_8 * 1.5)
   * 
    (0.1 * (1.0 - tmpvar_10))
  ) * sin(
    ((5.0 * (1.0 - tmpvar_10)) + (0.25 * tmpvar_9))
  )));
  float tmpvar_11;
  tmpvar_11 = sin((time_var + dot (vPosition_2.xy, vec2(6.5, 4.5))));
  float tmpvar_12;
  if ((vSeason > 2.5)) {
    tmpvar_12 = 0.25;
  } else {
    tmpvar_12 = 1.0;
  };
  coords_3.x = (coords_3.x + (0.015 * (tmpvar_11 * tmpvar_12)));
  coords_3.x = mix (coords_3.x, inTexCoord.x, clamp ((
    (tmpvar_10 * tmpvar_10)
   + 0.1), 0.0, 1.0));
  vec4 tmpvar_13;
  tmpvar_13.w = 1.0;
  tmpvar_13.xyz = vSunColor.xyz;
  tmpvar_5 = (inColor0.zyxw * (vAmbientColor + (tmpvar_13 * 0.06)));
  tmpvar_5.w = (tmpvar_5.w * vMaterialColor.w);
  vec3 tmpvar_14;
  tmpvar_14 = (matWorldView * vPosition_2).xyz;
  gl_Position = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_14, tmpvar_14))
   * fFogDensity))));
  Color = tmpvar_5;
  Tex0 = coords_3;
  SunLight = ((vSunColor * 0.34) * (vMaterialColor * inColor0.zyxw));
  ShadowTexCoord = tmpvar_6;
}

