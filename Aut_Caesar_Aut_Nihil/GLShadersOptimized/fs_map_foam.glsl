uniform sampler2D diffuse_texture;
uniform sampler2D normal_texture;
uniform vec4 vFogColor;
uniform vec4 output_gamma_inv;
uniform float time_var;
varying vec4 Color;
varying vec2 Tex0;
varying vec3 CameraDir;
varying vec4 PosWater;
varying float Fog;
void main ()
{
  vec2 tmpvar_1;
  tmpvar_1 = Tex0;
  vec3 normal_2;
  vec4 tex_col_3;
  vec4 tmpvar_4;
  tmpvar_4 = Color;
  if ((PosWater.x < -125.0)) {
    tmpvar_1 = (Tex0 * 0.75);
    vec2 newvector_5;
    newvector_5.x = ((-0.7071068 * tmpvar_1.x) - (-0.7071067 * tmpvar_1.y));
    newvector_5.y = ((-0.7071067 * tmpvar_1.x) + (-0.7071068 * tmpvar_1.y));
    tmpvar_1.x = newvector_5.x;
    tmpvar_1.y = (newvector_5.y - (0.05 * time_var));
  } else {
    if (((PosWater.y > 273.0) && (PosWater.x < -75.0))) {
      tmpvar_1 = (tmpvar_1 * 0.75);
      tmpvar_1 = (1.0 - tmpvar_1);
      tmpvar_1.y = (tmpvar_1.y - (0.05 * time_var));
    } else {
      if (((PosWater.y > 213.0) && (PosWater.x > -75.0))) {
        tmpvar_1 = (tmpvar_1 * 0.75);
        tmpvar_1.y = (tmpvar_1.y - (0.05 * time_var));
      } else {
        if (((PosWater.x > -125.0) && (PosWater.x < -50.0))) {
          tmpvar_1 = (tmpvar_1 * 0.75);
          vec2 newvector_6;
          newvector_6.x = ((-4.371139e-08 * tmpvar_1.x) - tmpvar_1.y);
          newvector_6.y = (tmpvar_1.x + (-4.371139e-08 * tmpvar_1.y));
          tmpvar_1.x = newvector_6.x;
          tmpvar_1.y = (newvector_6.y - (0.05 * time_var));
        } else {
          if (((PosWater.y < 213.0) && (PosWater.x > -50.0))) {
            tmpvar_1 = (tmpvar_1 * 0.75);
            vec2 newvector_7;
            newvector_7.x = ((1.192488e-08 * tmpvar_1.x) - -(tmpvar_1.y));
            newvector_7.y = (-(tmpvar_1.x) + (1.192488e-08 * tmpvar_1.y));
            tmpvar_1.x = newvector_7.x;
            tmpvar_1.y = (newvector_7.y - (0.05 * time_var));
          } else {
            tmpvar_1.y = (tmpvar_1.y - (0.05 * time_var));
          };
        };
      };
    };
  };
  vec4 tmpvar_8;
  tmpvar_8 = texture2D (diffuse_texture, tmpvar_1);
  tex_col_3.w = tmpvar_8.w;
  tex_col_3.xyz = pow (tmpvar_8.xyz, vec3(2.2, 2.2, 2.2));
  normal_2.xy = ((2.0 * texture2D (normal_texture, (tmpvar_1 * 8.0)).wy) - 1.0);
  normal_2.z = sqrt((1.0 - dot (normal_2.xy, normal_2.xy)));
  float tmpvar_9;
  tmpvar_9 = (1.0 - clamp (dot (
    normalize(CameraDir)
  , normal_2), 0.0, 1.0));
  tmpvar_4.xyz = (Color.xyz + ((0.0204 + 
    (((0.9796 * tmpvar_9) * (tmpvar_9 * tmpvar_9)) * (tmpvar_9 * tmpvar_9))
  ) * Color.xyz));
  tmpvar_4.xyz = (tmpvar_4.xyz * tex_col_3.xyz);
  tmpvar_4.xyz = (tmpvar_4.xyz * 0.8);
  tmpvar_4.xyz = pow (tmpvar_4.xyz, output_gamma_inv.xyz);
  tmpvar_4.w = (Color.w * tmpvar_8.w);
  tmpvar_4.xyz = mix (vFogColor.xyz, tmpvar_4.xyz, Fog);
  gl_FragColor = tmpvar_4;
}

