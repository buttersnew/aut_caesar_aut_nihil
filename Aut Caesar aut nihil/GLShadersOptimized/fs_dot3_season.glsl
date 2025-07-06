uniform sampler2D diffuse_texture;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform vec4 vMaterialColor;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightColor;
uniform vec4 vPointLightColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying vec4 VertexColor;
varying vec2 Tex0;
varying vec3 SunLightDir;
varying vec3 SkyLightDir;
varying vec4 PointLightDir;
varying float Fog;
varying vec3 ViewDir;
varying vec3 WorldNormal;
void main ()
{
  vec4 tex_col_1;
  vec4 total_light_2;
  vec4 tmpvar_3;
  vec3 tmpvar_4;
  tmpvar_4 = ((2.0 * texture2D (normal_texture, Tex0).xyz) - 1.0);
  total_light_2 = (vAmbientColor + (clamp (
    dot (SunLightDir, tmpvar_4)
  , 0.0, 1.0) * vSunColor));
  total_light_2 = (total_light_2 + (clamp (
    dot (SkyLightDir, tmpvar_4)
  , 0.0, 1.0) * vSkyLightColor));
  total_light_2 = (total_light_2 + (clamp (
    dot (PointLightDir.xyz, tmpvar_4)
  , 0.0, 1.0) * vPointLightColor));
  tmpvar_3.xyz = total_light_2.xyz;
  tmpvar_3.w = 1.0;
  tmpvar_3 = (tmpvar_3 * vMaterialColor);
  vec4 tmpvar_5;
  tmpvar_5 = texture2D (diffuse_texture, Tex0);
  tex_col_1 = tmpvar_5;
  if ((vSeason < 0.5)) {
    tex_col_1.xyz = (tmpvar_5.xyz * vec3(0.9, 1.1, 0.9));
  } else {
    if (((vSeason > 0.5) && (vSeason < 1.5))) {
      tex_col_1.xyz = tex_col_1.xyz;
    } else {
      if (((vSeason > 1.5) && (vSeason < 2.5))) {
        tex_col_1.xyz = (tex_col_1.xyz * vec3(1.1, 0.9, 0.9));
      } else {
        if ((vSeason > 2.5)) {
          tex_col_1 = texture2D (specular_texture, Tex0);
        };
      };
    };
  };
  tex_col_1.xyz = pow (tex_col_1.xyz, vec3(2.2, 2.2, 2.2));
  tmpvar_3 = (tmpvar_3 * tex_col_1);
  tmpvar_3 = (tmpvar_3 * VertexColor);
  float tmpvar_6;
  tmpvar_6 = (1.0 - clamp (dot (ViewDir, WorldNormal), 0.0, 1.0));
  tmpvar_3.xyz = (tmpvar_3.xyz * max (0.6, (
    (tmpvar_6 * tmpvar_6)
   + 0.1)));
  tmpvar_3.xyz = pow (tmpvar_3.xyz, output_gamma_inv.xyz);
  tmpvar_3.xyz = mix (vFogColor.xyz, tmpvar_3.xyz, Fog);
  gl_FragColor = tmpvar_3;
}

