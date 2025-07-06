uniform vec4 vLightDiffuse[4];
uniform vec4 vMaterialColor;
uniform vec4 vSunDir;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightDir;
uniform vec4 vSkyLightColor;
uniform float fFogDensity;
uniform int iLightPointCount;
uniform int iLightIndices[4];
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vLightPosDir[4];
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec4 inColor1;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
varying vec4 Color;
varying vec4 Tex0;
varying vec3 CameraDir;
varying vec4 ShadowTexCoord;
varying vec2 ShadowTexelPos;
varying float Fog;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec3 ViewDir;
varying vec3 WorldNormal;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 diffuse_light_2;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  vec4 tmpvar_5;
  vec2 tmpvar_6;
  vec3 tmpvar_7;
  tmpvar_3 = (matWorldViewProj * tmpvar_1);
  vec4 tmpvar_8;
  tmpvar_8 = (matWorld * tmpvar_1);
  vec4 tmpvar_9;
  tmpvar_9.w = 0.0;
  tmpvar_9.xyz = inNormal;
  vec3 tmpvar_10;
  tmpvar_10 = normalize((matWorld * tmpvar_9).xyz);
  vec4 tmpvar_11;
  tmpvar_11.w = 0.0;
  tmpvar_11.xyz = inBinormal;
  vec4 tmpvar_12;
  tmpvar_12.w = 0.0;
  tmpvar_12.xyz = inTangent;
  mat3 tmpvar_13;
  tmpvar_13[0] = normalize((matWorld * tmpvar_12).xyz);
  tmpvar_13[1] = normalize((matWorld * tmpvar_11).xyz);
  tmpvar_13[2] = tmpvar_10;
  tmpvar_4.xy = inTexCoord;
  tmpvar_4.z = (0.7 * (tmpvar_8.z - 1.5));
  tmpvar_4.w = tmpvar_8.x;
  diffuse_light_2 = (vAmbientColor + inColor1.zyxw);
  diffuse_light_2.xyz = (diffuse_light_2.xyz + (clamp (
    dot (tmpvar_10, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor.xyz));
  vec4 vWorldPos_14;
  vWorldPos_14 = tmpvar_8;
  vec3 vWorldN_15;
  vWorldN_15 = tmpvar_10;
  vec4 total_17;
  total_17 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int j_16 = 0; j_16 < iLightPointCount; j_16++) {
    int tmpvar_18;
    tmpvar_18 = iLightIndices[j_16];
    vec3 tmpvar_19;
    tmpvar_19 = (vLightPosDir[tmpvar_18].xyz - vWorldPos_14.xyz);
    total_17 = (total_17 + ((
      clamp (dot (vWorldN_15, normalize(tmpvar_19)), 0.0, 1.0)
     * vLightDiffuse[tmpvar_18]) * (1.0/(
      dot (tmpvar_19, tmpvar_19)
    ))));
  };
  diffuse_light_2 = (diffuse_light_2 + total_17);
  vec4 tmpvar_20;
  tmpvar_20 = normalize((vCameraPos - tmpvar_8));
  vec3 tmpvar_21;
  tmpvar_21 = (matWorldView * tmpvar_1).xyz;
  gl_Position = tmpvar_3;
  Color = ((vMaterialColor * inColor0.zyxw) * diffuse_light_2);
  Tex0 = tmpvar_4;
  CameraDir = (tmpvar_13 * -(tmpvar_20.xyz));
  ShadowTexCoord = tmpvar_5;
  ShadowTexelPos = tmpvar_6;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_21, tmpvar_21))
   * fFogDensity))));
  SunLightDir = normalize((tmpvar_13 * -(vSunDir.xyz)));
  SkyLightDir = tmpvar_7;
  ViewDir = tmpvar_20.xyz;
  WorldNormal = tmpvar_10;
}

