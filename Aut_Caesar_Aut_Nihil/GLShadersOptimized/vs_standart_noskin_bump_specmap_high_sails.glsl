uniform vec4 vLightDiffuse[4];
uniform vec4 vMaterialColor;
uniform vec4 vSunDir;
uniform float fMaterialPower;
uniform float fFogDensity;
uniform int iLightPointCount;
uniform int iLightIndices[4];
uniform bool bUseMotionBlur;
uniform float vWindStrength;
uniform float vWindDirection;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform mat4 matMotionBlur;
uniform mat4 matViewProj;
uniform vec4 vLightPosDir[4];
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec4 inColor0;
attribute vec2 inTexCoord;
attribute vec3 inTangent;
attribute vec3 inBinormal;
varying float Fog;
varying vec4 VertexColor;
varying vec3 VertexLighting;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying vec4 ShadowTexCoord;
varying vec3 ViewDir;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2 = tmpvar_1;
  vec4 vVertexColor_3;
  vVertexColor_3 = inColor0;
  vec4 vWorldPos_4;
  vec2 UV_5;
  vec4 tmpvar_6;
  vec4 tmpvar_7;
  vec3 tmpvar_8;
  vec3 tmpvar_9;
  vec3 tmpvar_10;
  vec4 tmpvar_11;
  vec3 tmpvar_12;
  float tmpvar_13;
  tmpvar_13 = max (1.5, vWindStrength);
  UV_5.x = inTexCoord.x;
  UV_5.y = (1.0 - inTexCoord.y);
  if ((((
    (UV_5.y < 0.05)
   && 
    (inTexCoord.x < 0.05)
  ) || (
    (inTexCoord.x > 0.95)
   && 
    (UV_5.y < 0.05)
  )) || (UV_5.y > 0.95))) {
    vPosition_2.x = tmpvar_1.x;
  } else {
    float inflate_14;
    vec4 WindDirection_15;
    vec4 WindDir_16;
    vec4 tmpvar_17;
    tmpvar_17.w = 0.0;
    tmpvar_17.xyz = inNormal;
    vec4 tmpvar_18;
    tmpvar_18.w = 0.0;
    tmpvar_18.xyz = inBinormal;
    vec4 tmpvar_19;
    tmpvar_19.w = 0.0;
    tmpvar_19.xyz = inTangent;
    mat3 tmpvar_20;
    tmpvar_20[0] = normalize((matWorld * tmpvar_19).xyz);
    tmpvar_20[1] = normalize((matWorld * tmpvar_18).xyz);
    tmpvar_20[2] = normalize((matWorld * tmpvar_17).xyz);
    WindDir_16.w = 1.0;
    WindDir_16.z = 0.001;
    float tmpvar_21;
    tmpvar_21 = (vWindDirection * 0.01745329);
    WindDir_16.x = ((cos(tmpvar_21) * 0.001) - (sin(tmpvar_21) * 0.99));
    WindDir_16.y = ((sin(tmpvar_21) * 0.001) + (cos(tmpvar_21) * 0.99));
    WindDirection_15.w = 1.0;
    WindDirection_15.xyz = (tmpvar_20 * WindDir_16.xyz);
    float tmpvar_22;
    tmpvar_22 = dot (inNormal.xy, WindDirection_15.xy);
    inflate_14 = tmpvar_22;
    if ((tmpvar_22 < 0.0)) {
      inflate_14 = -(tmpvar_22);
    };
    inflate_14 = (inflate_14 * tmpvar_13);
    vPosition_2.x = (vPosition_2.x + ((inflate_14 / 6.0) * sin(
      ((1.5 * inPosition.y) + ((1.6 * tmpvar_13) * time_var))
    )));
    vPosition_2.x = (vPosition_2.x + ((inflate_14 / 4.0) * sin(
      ((0.6 * inPosition.y) + (tmpvar_13 * time_var))
    )));
    inflate_14 = (1.0 - inflate_14);
    vPosition_2.x = (vPosition_2.x + ((inflate_14 / 4.0) * sin(
      ((0.6 * inPosition.z) + (tmpvar_13 * time_var))
    )));
  };
  vec4 tmpvar_23;
  tmpvar_23 = (matWorld * vPosition_2);
  vWorldPos_4 = tmpvar_23;
  vec4 tmpvar_24;
  tmpvar_24.w = 0.0;
  tmpvar_24.xyz = inNormal;
  vec3 tmpvar_25;
  tmpvar_25 = normalize((matWorld * tmpvar_24).xyz);
  if (bUseMotionBlur) {
    vec4 tmpvar_26;
    tmpvar_26 = (matMotionBlur * vPosition_2);
    vec3 tmpvar_27;
    tmpvar_27 = normalize((tmpvar_26.xyz - tmpvar_23.xyz));
    float tmpvar_28;
    tmpvar_28 = dot (tmpvar_25, tmpvar_27);
    float tmpvar_29;
    if ((tmpvar_28 > 0.1)) {
      tmpvar_29 = 1.0;
    } else {
      tmpvar_29 = 0.0;
    };
    vWorldPos_4 = mix (tmpvar_23, tmpvar_26, (tmpvar_29 * clamp (
      (inPosition.y + 0.15)
    , 0.0, 1.0)));
    vVertexColor_3.w = ((clamp (
      (0.5 - inPosition.y)
    , 0.0, 1.0) + clamp (
      mix (1.1, -0.6999999, clamp ((dot (tmpvar_25, tmpvar_27) + 0.5), 0.0, 1.0))
    , 0.0, 1.0)) + 0.25);
  };
  if (bUseMotionBlur) {
    tmpvar_6 = (matViewProj * vWorldPos_4);
  } else {
    tmpvar_6 = (matWorldViewProj * vPosition_2);
  };
  vec4 tmpvar_30;
  tmpvar_30.w = 0.0;
  tmpvar_30.xyz = inBinormal;
  vec4 tmpvar_31;
  tmpvar_31.w = 0.0;
  tmpvar_31.xyz = inTangent;
  mat3 tmpvar_32;
  tmpvar_32[0] = normalize((matWorld * tmpvar_31).xyz);
  tmpvar_32[1] = normalize((matWorld * tmpvar_30).xyz);
  tmpvar_32[2] = tmpvar_25;
  tmpvar_9 = normalize((tmpvar_32 * -(vSunDir.xyz)));
  tmpvar_10 = (tmpvar_32 * vec3(0.0, 0.0, 1.0));
  tmpvar_7 = vVertexColor_3.zyxw;
  vec4 vWorldPos_33;
  vWorldPos_33 = vWorldPos_4;
  vec3 vWorldN_34;
  vWorldN_34 = tmpvar_25;
  vec4 total_36;
  total_36 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int j_35 = 0; j_35 < iLightPointCount; j_35++) {
    if ((j_35 != 0)) {
      int tmpvar_37;
      tmpvar_37 = iLightIndices[j_35];
      vec3 tmpvar_38;
      tmpvar_38 = (vLightPosDir[tmpvar_37].xyz - vWorldPos_33.xyz);
      total_36 = (total_36 + ((
        clamp (dot (vWorldN_34, normalize(tmpvar_38)), 0.0, 1.0)
       * vLightDiffuse[tmpvar_37]) * (1.0/(
        dot (tmpvar_38, tmpvar_38)
      ))));
    };
  };
  tmpvar_8 = total_36.xyz;
  vec3 tmpvar_39;
  tmpvar_39 = (vLightPosDir[iLightIndices[0]].xyz - vWorldPos_4.xyz);
  tmpvar_11.xyz = (tmpvar_32 * normalize(tmpvar_39));
  tmpvar_11.w = clamp ((1.0/(dot (tmpvar_39, tmpvar_39))), 0.0, 1.0);
  vec3 tmpvar_40;
  tmpvar_40 = normalize((vCameraPos.xyz - vWorldPos_4.xyz));
  tmpvar_12 = (tmpvar_32 * tmpvar_40);
  vec3 vWorldPos_41;
  vWorldPos_41 = vWorldPos_4.xyz;
  vec3 vWorldN_42;
  vWorldN_42 = tmpvar_25;
  vec3 vWorldView_43;
  vWorldView_43 = tmpvar_40;
  vec4 total_45;
  total_45 = vec4(0.0, 0.0, 0.0, 0.0);
  for (int i_44 = 0; i_44 < iLightPointCount; i_44++) {
    vec3 tmpvar_46;
    tmpvar_46 = (vLightPosDir[i_44].xyz - vWorldPos_41);
    total_45 = (total_45 + ((
      (1.0/(dot (tmpvar_46, tmpvar_46)))
     * vLightDiffuse[i_44]) * pow (
      clamp (dot (normalize((vWorldView_43 + 
        normalize(tmpvar_46)
      )), vWorldN_42), 0.0, 1.0)
    , fMaterialPower)));
  };
  tmpvar_7.w = (vVertexColor_3.w * vMaterialColor.w);
  vec3 tmpvar_47;
  tmpvar_47 = (matWorldView * vPosition_2).xyz;
  gl_Position = tmpvar_6;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_47, tmpvar_47))
   * fFogDensity))));
  VertexColor = tmpvar_7;
  VertexLighting = tmpvar_8;
  Tex0 = inTexCoord;
  SunLightDir = tmpvar_9;
  SkyLightDir = tmpvar_10;
  PointLightDir = tmpvar_11;
  ShadowTexCoord = total_45;
  ViewDir = tmpvar_12;
}

