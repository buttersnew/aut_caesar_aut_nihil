uniform sampler2D diffuse_texture;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform vec4 vLightDiffuse[4];
uniform vec4 vMaterialColor;
uniform vec4 vSpecularColor;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vGroundAmbientColor;
uniform vec4 vSkyLightColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float fMaterialPower;
uniform float spec_coef;
uniform int iLightIndices[4];
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
  vec4 tex_col_1;
  float fresnel_2;
  vec4 total_light_3;
  vec3 normal_4;
  vec4 tmpvar_5;
  normal_4 = ((2.0 * texture2D (normal_texture, Tex0).xyz) - 1.0);
  vec4 ambientTerm_6;
  ambientTerm_6 = mix (vGroundAmbientColor, vAmbientColor, ((
    dot (normal_4, SkyLightDir)
   + 1.0) * 0.5));
  total_light_3.w = ambientTerm_6.w;
  total_light_3.xyz = (ambientTerm_6.xyz + (vec3(clamp (
    dot (SunLightDir, normal_4)
  , 0.0, 1.0)) * vSunColor.xyz));
  total_light_3 = (total_light_3 + (clamp (
    dot (SkyLightDir, normal_4)
  , 0.0, 1.0) * vSkyLightColor));
  total_light_3.xyz = (total_light_3.xyz + VertexLighting);
  total_light_3 = (total_light_3 + clamp ((
    (dot (PointLightDir.xyz, normal_4) * vLightDiffuse[iLightIndices[0]])
   * PointLightDir.w), 0.0, 1.0));
  float tmpvar_7;
  tmpvar_7 = (1.0 - clamp (dot (
    normalize(ViewDir)
  , normal_4), 0.0, 1.0));
  fresnel_2 = (0.0204 + ((0.9796 * tmpvar_7) * (
    (tmpvar_7 * tmpvar_7)
   * tmpvar_7)));
  fresnel_2 = (fresnel_2 * 4.0);
  total_light_3.xyz = (total_light_3.xyz + (total_light_3.xyz * fresnel_2));
  float tmpvar_8;
  tmpvar_8 = (fresnel_2 * fresnel_2);
  fresnel_2 = tmpvar_8;
  total_light_3.xyz = (total_light_3.xyz + (0.02 * (total_light_3.xyz * tmpvar_8)));
  tmpvar_5.xyz = min (total_light_3.xyz, 2.0);
  tmpvar_5.xyz = (tmpvar_5.xyz * vMaterialColor.xyz);
  vec4 tmpvar_9;
  tmpvar_9 = texture2D (diffuse_texture, Tex0);
  tex_col_1.w = tmpvar_9.w;
  tex_col_1.xyz = pow (tmpvar_9.xyz, vec3(2.2, 2.2, 2.2));
  tmpvar_5.xyz = (tmpvar_5.xyz * tex_col_1.xyz);
  tmpvar_5.xyz = (tmpvar_5.xyz * VertexColor.xyz);
  vec4 specColor_10;
  vec4 fSpecular_11;
  specColor_10 = (((0.1 * spec_coef) * vSpecularColor) * dot (texture2D (specular_texture, Tex0).xyz, vec3(0.33, 0.33, 0.33)));
  fSpecular_11 = ((specColor_10 * vSunColor) * pow (clamp (
    dot (normalize((ViewDir + SunLightDir)), normal_4)
  , 0.0, 1.0), fMaterialPower));
  fSpecular_11 = (fSpecular_11 * VertexColor);
  fSpecular_11.xyz = (fSpecular_11.xyz + (specColor_10.xyz * ShadowTexCoord.xyz));
  fSpecular_11 = (fSpecular_11 + ((
    (specColor_10 * vLightDiffuse[iLightIndices[0]])
   * 
    (PointLightDir.w * 0.5)
  ) * pow (
    clamp (dot (normalize((ViewDir + PointLightDir.xyz)), normal_4), 0.0, 1.0)
  , fMaterialPower)));
  tmpvar_5 = (tmpvar_5 + fSpecular_11);
  tmpvar_5.xyz = pow (tmpvar_5.xyz, output_gamma_inv.xyz);
  tmpvar_5.w = (VertexColor.w * tmpvar_9.w);
  tmpvar_5.xyz = mix (vFogColor.xyz, tmpvar_5.xyz, Fog);
  gl_FragColor = tmpvar_5;
}

