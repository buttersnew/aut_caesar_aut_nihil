uniform sampler2D diffuse_texture;
uniform sampler2D diffuse_texture_2;
uniform sampler2D specular_texture;
uniform sampler2D normal_texture;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float vSeason;
varying float Fog;
varying vec4 Color;
varying vec2 Tex0;
varying vec4 SunLight;
void main ()
{
  vec4 tex_col_1;
  vec4 tmpvar_2;
  vec4 tmpvar_3;
  tmpvar_3 = texture2D (diffuse_texture, Tex0);
  tex_col_1 = tmpvar_3;
  if (((tmpvar_3.w - 0.5) < 0.0)) {
    discard;
  };
  if ((vSeason < 0.5)) {
    tex_col_1 = texture2D (diffuse_texture, Tex0);
  } else {
    if (((vSeason > 0.5) && (vSeason < 1.5))) {
      tex_col_1 = texture2D (diffuse_texture_2, Tex0);
    } else {
      if (((vSeason > 1.5) && (vSeason < 2.5))) {
        tex_col_1 = texture2D (normal_texture, Tex0);
      } else {
        if ((vSeason > 2.5)) {
          tex_col_1 = texture2D (specular_texture, Tex0);
        };
      };
    };
  };
  tex_col_1.xyz = pow (tex_col_1.xyz, vec3(2.2, 2.2, 2.2));
  tmpvar_2 = (tex_col_1 * (Color + SunLight));
  tmpvar_2.xyz = pow (tmpvar_2.xyz, output_gamma_inv.xyz);
  tmpvar_2.xyz = mix (vFogColor.xyz, tmpvar_2.xyz, Fog);
  gl_FragColor = tmpvar_2;
}

