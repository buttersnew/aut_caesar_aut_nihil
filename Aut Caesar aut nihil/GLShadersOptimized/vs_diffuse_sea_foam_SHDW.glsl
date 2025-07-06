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
uniform mat4 matSunViewProj;
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
  vec2 tmpvar_6;
  vec4 tmpvar_7;
  float tmpvar_8;
  tmpvar_8 = (vTimer * 10.0);
  vPosition_2.z = ((inPosition.z + (vWaveInfo.y * 
    sin(((vWaveInfo.w * inPosition.y) + tmpvar_8))
  )) + vWaveOrigin.y);
  vPosition_2.z = ((vPosition_2.z + (vWaveInfo.x * 
    sin(((vWaveInfo.z * inPosition.x) + tmpvar_8))
  )) + vWaveOrigin.x);
  vPosition_2.z = (vPosition_2.z + vWaveOrigin.z);
  tmpvar_4 = (matWorldViewProj * vPosition_2);
  vec4 tmpvar_9;
  tmpvar_9 = (matWorld * vPosition_2);
  vec4 tmpvar_10;
  tmpvar_10.w = 0.0;
  tmpvar_10.xyz = inNormal;
  vec3 tmpvar_11;
  tmpvar_11 = normalize((matWorld * tmpvar_10).xyz);
  tmpvar_5.xy = inTexCoord;
  tmpvar_5.z = (0.7 * (tmpvar_9.z - 1.5));
  tmpvar_5.w = tmpvar_9.x;
  diffuse_light_3 = (vAmbientColor + inColor1);
  diffuse_light_3 = (diffuse_light_3 + (clamp (
    dot (tmpvar_11, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor));
  vec4 vWorldPos_12;
  vWorldPos_12 = tmpvar_9;
  vec3 vWorldN_13;
  vWorldN_13 = tmpvar_11;
  vec4 total_15;
  total_15 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int j_14 = 0; j_14 < iLightPointCount; j_14++) {
    int tmpvar_16;
    tmpvar_16 = iLightIndices[j_14];
    vec3 tmpvar_17;
    tmpvar_17 = (vLightPosDir[tmpvar_16].xyz - vWorldPos_12.xyz);
    total_15 = (total_15 + ((
      clamp (dot (vWorldN_13, normalize(tmpvar_17)), 0.0, 1.0)
     * vLightDiffuse[tmpvar_16]) * (1.0/(
      dot (tmpvar_17, tmpvar_17)
    ))));
  };
  diffuse_light_3 = (diffuse_light_3 + total_15);
  vec3 tmpvar_18;
  tmpvar_18 = (matWorldView * vPosition_2).xyz;
  gl_Position = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_18, tmpvar_18))
   * fFogDensity))));
  Color = ((vMaterialColor * inColor0) * diffuse_light_3);
  Tex0 = tmpvar_5;
  SunLight = (((
    clamp (dot (tmpvar_11, -(vSunDir.xyz)), 0.0, 1.0)
   * vSunColor) * vMaterialColor) * inColor0);
  ShadowTexCoord = (matSunViewProj * tmpvar_9);
  ShadowTexelPos = tmpvar_6;
  WorldPos = tmpvar_7;
}

