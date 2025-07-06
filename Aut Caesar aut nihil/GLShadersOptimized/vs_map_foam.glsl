uniform vec4 vMaterialColor;
uniform vec4 vSunDir;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightDir;
uniform vec4 vSkyLightColor;
uniform float fFogDensity;
uniform float time_var;
uniform mat4 matWorldViewProj;
uniform mat4 matWorldView;
uniform mat4 matWorld;
uniform vec4 vCameraPos;
attribute vec3 inPosition;
attribute vec3 inNormal;
attribute vec2 inTexCoord;
attribute vec4 inColor0;
attribute vec4 inColor1;
varying vec4 Color;
varying vec2 Tex0;
varying vec3 LightDir;
varying vec3 CameraDir;
varying vec4 PosWater;
varying float Fog;
void main ()
{
  vec4 tmpvar_1;
  tmpvar_1.w = 1.0;
  tmpvar_1.xyz = inPosition;
  vec4 vPosition_2;
  vPosition_2 = tmpvar_1;
  vec4 diffuse_light_3;
  if ((inPosition.z < 0.7)) {
    vPosition_2.z = (inPosition.z + (0.2 * sin(
      ((20.0 * inTexCoord.x) + time_var)
    )));
    vPosition_2.z = (vPosition_2.z + sin((
      (10.0 * inTexCoord.y)
     + time_var)));
  };
  vec4 tmpvar_4;
  tmpvar_4 = (matWorld * vPosition_2);
  vec4 tmpvar_5;
  tmpvar_5.w = 0.0;
  tmpvar_5.xyz = inNormal;
  vec3 tmpvar_6;
  tmpvar_6 = normalize((matWorld * tmpvar_5).xyz);
  vec3 tmpvar_7;
  tmpvar_7 = (matWorldView * vPosition_2).xyz;
  vec4 tmpvar_8;
  tmpvar_8 = (vAmbientColor + inColor1.zyxw);
  diffuse_light_3.w = tmpvar_8.w;
  diffuse_light_3.xyz = (tmpvar_8.xyz + (clamp (
    dot (tmpvar_6, -(vSkyLightDir.xyz))
  , 0.0, 1.0) * vSkyLightColor.xyz));
  vec3 tmpvar_9;
  tmpvar_9 = -(vSunDir.xyz);
  diffuse_light_3.xyz = (diffuse_light_3.xyz + (max (-0.0001, 
    dot (tmpvar_6, tmpvar_9)
  ) * vSunColor.xyz));
  mat3 tmpvar_10;
  tmpvar_10[0] = vec3(1.0, 0.0, 0.0);
  tmpvar_10[1] = vec3(0.0, 1.0, 0.0);
  tmpvar_10[2] = vec3(0.0, 0.0, 1.0);
  gl_Position = (matWorldViewProj * vPosition_2);
  Color = ((vMaterialColor * inColor0.zyxw) * diffuse_light_3);
  Tex0 = inTexCoord;
  LightDir = (tmpvar_10 * tmpvar_9);
  CameraDir = (tmpvar_10 * -(normalize(
    (vCameraPos.xyz - tmpvar_4.xyz)
  )));
  PosWater = tmpvar_4;
  Fog = (1.0/(exp2((
    sqrt(dot (tmpvar_7, tmpvar_7))
   * fFogDensity))));
}

