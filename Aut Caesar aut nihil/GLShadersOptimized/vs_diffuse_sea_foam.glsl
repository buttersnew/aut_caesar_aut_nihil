uniform vec4 vLightDiffuse[4];
uniform vec4 vMaterialColor;
uniform vec4 vSunDir;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightDir;
uniform vec4 vSkyLightColor;
uniform float fFogDensity;
uniform int iLightPointCount;
uniform int iLightIndices[4];
uniform float vTimer;
uniform vec4 vWaveInfo;
uniform vec4 vWaveOrigin;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vLightPosDir[4];
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec2 inTexCoord;
attribute vec4 inColor0;
attribute vec4 inColor1;
varying float Fog;
varying vec4 Color;
varying vec4 Tex0;
varying vec4 SunLight;
varying vec4 ShadowTexCoord;
varying vec2 ShadowTexelPos;
varying vec4 WorldPos;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2.xyw = tmpvar_1.xyw;
  vec4 diffuse_light_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vec4 tmpvar_6;
  vec2 tmpvar_7;
  vec4 tmpvar_8;
  float tmpvar_9;
  tmpvar_9 = (vTimer * 10.0);
  vPosition_2.z = ((inPosition.z + (vWaveInfo.y * 
    sin(((vWaveInfo.w * inPosition.y) + tmpvar_9))
  )) + vWaveOrigin.y);
  vPosition_2.z = ((vPosition_2.z + (vWaveInfo.x * 
    sin(((vWaveInfo.z * inPosition.x) + tmpvar_9))
  )) + vWaveOrigin.x);
  vPosition_2.z = (vPosition_2.z + vWaveOrigin.z);
  tmpvar_4 = (matWorldViewProj * vPosition_2);
  vec4 tmpvar_10;
  tmpvar_10 = (matWorld * vPosition_2);
  vec4 tmpvar_11;
  tmpvar_11.w = 0.0;
  tmpvar_11.xyz = inNormal;
  vec3 tmpvar_12;
  tmpvar_12 = normalize((matWorld * tmpvar_11).xyz);
  tmpvar_5.xy = inTexCoord;
  tmpvar_5.z = (0.7 * (tmpvar_10.z - 1.5));
  tmpvar_5.w = tmpvar_10.x;
  diffuse_light_3 = (vAmbientColor + inColor1);
  diffuse_light_3 = (diffuse_light_3 + (clamp (
    dot (tmpvar_12, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor));
  vec4 vWorldPos_13;
  vWorldPos_13 = tmpvar_10;
  vec3 vWorldN_14;
  vWorldN_14 = tmpvar_12;
  vec4 total_16;
  total_16 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int j_15 = 0; j_15 < iLightPointCount; j_15++) {
    int tmpvar_17;
    tmpvar_17 = iLightIndices[j_15];
    vec3 tmpvar_18;
    tmpvar_18 = (vLightPosDir[tmpvar_17].xyz - vWorldPos_13.xyz);
    total_16 = (total_16 + ((
      clamp (dot (vWorldN_14, normalize(tmpvar_18)), 0.0, 1.0)
     * vLightDiffuse[tmpvar_17]) * (1.0/(
      dot (tmpvar_18, tmpvar_18)
    ))));
  };
  diffuse_light_3 = (diffuse_light_3 + total_16);
  vec3 tmpvar_19;
  tmpvar_19 = (matWorldView * vPosition_2).xyz;
  gl_Position = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_19, tmpvar_19))
   * fFogDensity))));
  Color = ((vMaterialColor * inColor0) * diffuse_light_3);
  Tex0 = tmpvar_5;
  SunLight = (((
    clamp (dot (tmpvar_12, -(vSunDir.xyz)), 0.0, 1.0)
   * vSunColor) * vMaterialColor) * inColor0);
  ShadowTexCoord = tmpvar_6;
  ShadowTexelPos = tmpvar_7;
  WorldPos = tmpvar_8;
}

