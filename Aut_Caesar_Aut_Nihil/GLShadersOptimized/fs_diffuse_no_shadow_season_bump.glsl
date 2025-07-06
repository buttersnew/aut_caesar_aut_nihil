uniform sampler2D diffuse_texture;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform vec4 vMaterialColor;
uniform vec4 vSunColor;
uniform vec4 vAmbientColor;
uniform vec4 vSkyLightColor;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying vec2 Tex0;
varying vec3 SkyDir;
varying vec3 SunDir;
varying vec4 vColor;
varying float Fog;
void main ()
{
  vec4 diffuse_light_1;
  vec4 tex_col_2;
  vec4 tmpvar_3;
  vec4 tmpvar_4;
  tmpvar_4 = texture2D (diffuse_texture, Tex0);
  tex_col_2.w = tmpvar_4.w;
  if (((tmpvar_4.w - 0.5) < 0.0)) {
    discard;
  };
  tex_col_2.xyz = pow (tmpvar_4.xyz, vec3(2.2, 2.2, 2.2));
  vec3 tmpvar_5;
  tmpvar_5 = ((2.0 * texture2D (normal_texture, Tex0).xyz) - 1.0);
  diffuse_light_1 = (vAmbientColor + (clamp (
    dot (tmpvar_5, SkyDir)
  , 0.0, 1.0) * vSkyLightColor));
  diffuse_light_1 = (diffuse_light_1 + (clamp (
    dot (tmpvar_5, SunDir)
  , 0.0, 1.0) * vSunColor));
  vec4 tmpvar_6;
  tmpvar_6 = clamp (((vMaterialColor * vColor) * diffuse_light_1), 0.0, 1.0);
  if ((vSeason < 0.5)) {
    tex_col_2.xyz = (tex_col_2.xyz * vec3(0.9, 1.1, 0.9));
  } else {
    if (((vSeason > 0.5) && (vSeason < 1.5))) {
      tex_col_2.xyz = tex_col_2.xyz;
    } else {
      if (((vSeason > 1.5) && (vSeason < 2.5))) {
        tex_col_2.xyz = (tex_col_2.xyz * vec3(1.1, 0.9, 0.9));
      } else {
        if ((vSeason > 2.5)) {
          tex_col_2 = texture2D (specular_texture, Tex0);
        };
      };
    };
  };
  tmpvar_3 = (tmpvar_6 * tex_col_2);
  tmpvar_3.xyz = pow (tmpvar_3.xyz, output_gamma_inv.xyz);
  tmpvar_3.xyz = mix (vFogColor.xyz, tmpvar_3.xyz, Fog);
  gl_FragColor = tmpvar_3;
}

