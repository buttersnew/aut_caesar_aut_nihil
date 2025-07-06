uniform vec4 vLightDiffuse[4];
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightDir;
uniform vec4 vSkyLightColor;
uniform float fFogDensity;
uniform int iLightPointCount;
uniform int iLightIndices[4];
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vLightPosDir[4];
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec3 inTangent;
attribute vec2 inTexCoord;
attribute vec4 inColor0;
varying vec2 Tex0;
varying vec4 VertexLighting;
varying vec3 viewVec;
varying vec3 normal;
varying vec3 tangent;
varying vec4 VertexColor;
varying vec4 ShadowTexCoord;
varying float Fog;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 diffuse_light_2;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  tmpvar_3 = (matWorldViewProj * tmpvar_1);
  vec4 tmpvar_5;
  tmpvar_5 = (matWorld * tmpvar_1);
  vec4 tmpvar_6;
  tmpvar_6.w = 0.0;
  tmpvar_6.xyz = inNormal;
  vec3 tmpvar_7;
  tmpvar_7 = normalize((matWorld * tmpvar_6).xyz);
  vec3 tmpvar_8;
  tmpvar_8 = (matWorldView * tmpvar_1).xyz;
  vec2 tmpvar_9;
  tmpvar_9.y = 0.0;
  tmpvar_9.x = sin(((25.0 * inTexCoord.y) + (1.5 * time_var)));
  vec2 tmpvar_10;
  tmpvar_10 = (inTexCoord + (0.01 * tmpvar_9));
  diffuse_light_2 = (vAmbientColor + (clamp (
    dot (tmpvar_7, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor));
  vec4 vWorldPos_11;
  vWorldPos_11 = tmpvar_5;
  vec3 vWorldN_12;
  vWorldN_12 = tmpvar_7;
  vec4 total_14;
  total_14 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int j_13 = 0; j_13 < iLightPointCount; j_13++) {
    int tmpvar_15;
    tmpvar_15 = iLightIndices[j_13];
    vec3 tmpvar_16;
    tmpvar_16 = (vLightPosDir[tmpvar_15].xyz - vWorldPos_11.xyz);
    float tmpvar_17;
    tmpvar_17 = dot (vWorldN_12, normalize(tmpvar_16));
    total_14 = (total_14 + ((
      max ((0.2 * (tmpvar_17 + 0.9)), tmpvar_17)
     * vLightDiffuse[tmpvar_15]) * (1.0/(
      dot (tmpvar_16, tmpvar_16)
    ))));
  };
  diffuse_light_2 = (diffuse_light_2 + total_14);
  vec4 tmpvar_18;
  tmpvar_18.w = 0.0;
  tmpvar_18.xyz = inNormal;
  vec4 tmpvar_19;
  tmpvar_19.w = 0.0;
  tmpvar_19.xyz = inTangent;
  gl_Position = tmpvar_3;
  Tex0 = tmpvar_10;
  VertexLighting = clamp ((inColor0 * diffuse_light_2), 0.0, 1.0);
  viewVec = normalize((vCameraPos - tmpvar_5).xyz);
  normal = normalize((matWorld * tmpvar_18).xyz);
  tangent = normalize((matWorld * tmpvar_19).xyz);
  VertexColor = inColor0;
  ShadowTexCoord = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_8, tmpvar_8))
   * fFogDensity))));
}

