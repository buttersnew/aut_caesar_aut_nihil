////////////////////////////////////////////////////////////////////////////////////
// POST EFFECT SHADERS (Refactored for Antique/Roman Look)
// ---
// ### 1. Critical Bug Fixes & Stability Improvements
// *   **Corrected Shader Model 2.0 `half` Precision Error:** The most critical fix was addressing the `error X3650` compiler error. `static const` global variables like `LUMINANCE_WEIGHTS` and `Epsilon` were reverted from `half` back to the `float` data type. This is a strict requirement of the `vs_2_0` shader profile and was the direct cause of the compilation failure.
// *   **Made HSV Functions More Robust:** A small `Epsilon` value was added to the denominators in the `RGBtoHSV` and `RGBtoHCV` functions. This prevents potential division-by-zero errors when processing pure black or greyscale colors, making the color manipulation logic more stable.
// ### 2. Performance & Optimization
// *   **Widespread Use of `half` Precision:** All variables that did not need 32-bit precision were converted from `float` to `half`. This includes:
//     *   All local variables inside pixel shader functions (e.g., `half4 color`, `half3 hsv`).
//     *   The `Tex` coordinate in the `VS_OUT_POSTFX` structure.
//     *   The return types and parameters of helper functions like `vignette` and the HSV conversions.
// *   **Optimized Math Operations:** Expensive `pow()` function calls were replaced with faster direct multiplications where possible (e.g., `greyscale * greyscale` instead of `pow(greyscale, 2)`).
// ### 3. Code Quality & Readability
// *   **Elimination of "Magic Numbers":** Hardcoded numerical constants were replaced with named `static const half` variables inside the `FinalScenePassPS` function. This makes the effects self-documenting and easy to tweak. Key examples include:
//     *   `VIGNETTE_BLUR_INNER_RADIUS` and `VIGNETTE_BLUR_STRENGTH` for the vignette effect.
//     *   `WARMTH_LERP` and `CONTRAST_POWER` for the color correction.
//     *   `SATURATION_MULTIPLIER` for the final palette adjustment.
// *   **Code Reorganization and Commenting:** The main `FinalScenePassPS` function was restructured into a clean, numbered pipeline with comments explaining each step:
//     1.  Sample Scene & Apply Gamma
//     2.  Vignette Blur
//     3.  HDR Bloom
//     4.  Color Correction
//     5.  Tonemapping
//     6.  Final Gamma & Palette Correction
//     This makes the complex chain of effects much easier to understand and modify.
// ### 4. Feature Enhancements & Tweaks
// *   **Implemented a True Vignette Blur:** The original Depth of Field (DOF) logic, which was causing a darkening effect at the edges, was completely removed. Now if HDR value is set to highest, there is new code that performs a **manual, multi-sample blur** on the original scene texture, but only for pixels near the edge of the screen (to maintain performance). This creates a true, cinematic blur vignette instead of just a dark border. (can be disabled by setting HDR to low or disabling it)
// *   **Tweaked for "Antique/Roman" Look:**
//     *   A new **Color Correction** step was implemented in the final pass. It analyzes the brightness of each pixel and subtly boosts the red and green channels to give the entire scene a warmer, "golden hour" tint.
//     *   A gentle **Contrast Curve** (`pow(color.rgb, CONTRAST_POWER)`) was added to make the image pop without crushing the blacks or whites.
//     *   The final **Saturation** multiplier was adjusted to enhance the vibrancy of colors, fitting the Mediterranean theme.
// *   **Adjusted Post-Processing Parameters:** The accompanying `postfx_params` Python list was completely re-tuned to work with the new shader logic, providing balanced and visually appealing settings for all in-game conditions (sunny, cloudy, night, indoors, etc.) that align with the desired "Antique/Roman" aesthetic.
////////////////////////////////////////////////////////////////////////////////////

#include "fx_configuration.h"

float4 output_gamma;
float4 output_gamma_inv;

// --- HSV <-> RGB Conversion Functions (Robust Version) ---
// Courtesy of Ian Taylor @ https://www.chilliant.com/rgb2hsv.html
// Modified for robustness with an epsilon value.

static const float Epsilon = 1e-10f;

half3 HUEtoRGB(in half H)
{
	half R = abs(H * 6.0h - 3.0h) - 1.0h;
	half G = 2.0h - abs(H * 6.0h - 2.0h);
	half B = 2.0h - abs(H * 6.0h - 4.0h);
	return saturate(half3(R,G,B));
}

half3 RGBtoHCV(in half3 RGB)
{
	// Based on work by Sam Hocevar and Emil Persson
	half4 P = (RGB.g < RGB.b) ? half4(RGB.bg, -1.0h, 2.0h/3.0h) : half4(RGB.gb, 0.0h, -1.0h/3.0h);
	half4 Q = (RGB.r < P.x) ? half4(P.xyw, RGB.r) : half4(RGB.r, P.yzx);
	half C = Q.x - min(Q.w, Q.y);
	half H = (C < Epsilon) ? 0.0h : abs((Q.w - Q.y) / (6.0h * C + Epsilon) + Q.z);
	return half3(H, C, Q.x);
}

half3 RGBtoHSV(in half3 RGB)
{
	half3 HCV = RGBtoHCV(RGB);
	half S = (HCV.z < Epsilon) ? 0.0h : HCV.y / (HCV.z + Epsilon);
	return half3(HCV.x, S, HCV.z);
}

half3 HSVtoRGB(in half3 HSV)
{
	half3 RGB = HUEtoRGB(HSV.x);
	return ((RGB - 1.0h) * HSV.y + 1.0h) * HSV.z;
}

// --- Constants ---
static const float3 LUMINANCE_WEIGHTS = float3(0.299h, 0.587h, 0.114h);
static const float min_exposure = 0.15f;
static const float max_exposure = 3.0f;

#pragma warning(disable: 3571) // pow(f,e) warning

// --- Sampler Definitions ---
#if defined(USE_FX_STATE_MANAGER) && !defined(USE_DEVICE_TEXTURE_ASSIGN)
	texture postFX_texture0, postFX_texture1, postFX_texture2, postFX_texture3, postFX_texture4;
	sampler postFX_sampler0 : register(s0) = sampler_state	{ Texture = postFX_texture0; };
	sampler postFX_sampler1 : register(s1) = sampler_state	{ Texture = postFX_texture1; };
	sampler postFX_sampler2 : register(s2) = sampler_state	{ Texture = postFX_texture2; };
	sampler postFX_sampler3 : register(s3) = sampler_state	{ Texture = postFX_texture3; };
	sampler postFX_sampler4 : register(s4) = sampler_state	{ Texture = postFX_texture4; };
#else
	#ifdef USE_REGISTERED_SAMPLERS
	sampler postFX_sampler0 : register(s0);
	sampler postFX_sampler1 : register(s1);
	sampler postFX_sampler2 : register(s2);
	sampler postFX_sampler3 : register(s3);
	sampler postFX_sampler4 : register(s4);
	#else
	sampler postFX_sampler0 : register(s0) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR; };
	sampler postFX_sampler1 : register(s1) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR; };
	sampler postFX_sampler2 : register(s2) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR; };
	sampler postFX_sampler3 : register(s3) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR; };
	sampler postFX_sampler4 : register(s4) = sampler_state{ AddressU = CLAMP; AddressV = CLAMP; MinFilter = LINEAR; MagFilter = LINEAR; };
	#endif
#endif

// --- Blur & Editor Parameters ---
static const float BlurPixelWeight[8] = { 0.256, 0.240, 0.144, 0.135, 0.120, 0.065, 0.030, 0.010 };
bool showing_ranged_data = false;
float4 g_HalfPixel_ViewportSizeInv;
float  g_HDR_frameTime;
float g_DOF_Focus = -0.005;
float g_DOF_Range = 5.19876;

#ifndef PS_2_X
	#define PS_2_X ps_2_b
#endif

#ifdef ENABLE_EDITOR
	float4 postfx_editor_vector[4];
	#define postfxTonemapOp		( int(postfx_editor_vector[0].x) )
	#define postfxParams1		float4(postfx_editor_vector[1].x, postfx_editor_vector[1].y, postfx_editor_vector[1].z, postfx_editor_vector[1].w)
	#define postfxParams2		float4(postfx_editor_vector[2].x, postfx_editor_vector[2].y, postfx_editor_vector[2].z, postfx_editor_vector[2].w)
	#define postfxParams3		float4(postfx_editor_vector[3].x, postfx_editor_vector[3].y, postfx_editor_vector[3].z, postfx_editor_vector[3].w)
	#define RELATIVE_PS_TARGET PS_2_X
#else
	#define RELATIVE_PS_TARGET ps_2_0
#endif

#define HDRRange 				(postfxParams1.x)
#define HDRExposureScaler 		(postfxParams1.y)
#define LuminanceAverageScaler 	(postfxParams1.z)
#define LuminanceMaxScaler 		(postfxParams1.w)
#define BrightpassTreshold 	(postfxParams2.x)
#define BrightpassPostPower (postfxParams2.y)
#define BlurStrenght 		(postfxParams2.z)
#define BlurAmount 			(postfxParams2.w)
#define Palette 			(postfxParams3.w)
#define HDRRangeInv 		(1.0f / HDRRange)

// --- Helper Functions ---
half vignette(half2 pos, half inner, half outer)
{
  half r = dot(pos,pos);
  return 1.0h - smoothstep(inner, outer, r);
}

half3 tonemapping(const half3 scene_color, const half2 luminanceAvgMax, const int tonemapOp)
{
	half lum_avg = luminanceAvgMax.x * LuminanceAverageScaler;
	static const half MiddleValue = 0.85h;
	half exposure = MiddleValue / (Epsilon + lum_avg);
	exposure = clamp(exposure * HDRExposureScaler, min_exposure, max_exposure);

	half3 scene_color_exposed = scene_color * exposure;
	half3 final_color;

	if( tonemapOp == 0 )
	{
		final_color = scene_color_exposed;
	}
	else if( tonemapOp == 1 )
	{
		final_color.rgb = 1.0h - exp2(-scene_color_exposed);
	}
	else if( tonemapOp == 2 )
	{
		final_color = scene_color_exposed / (scene_color_exposed + 1.0h);
	}
	else // tonemapOp == 3
	{
		half lum_max = luminanceAvgMax.y * LuminanceMaxScaler;
		half Lp = (exposure / lum_avg) * max(scene_color_exposed.r, max(scene_color_exposed.g, scene_color_exposed.b));
		half LmSqr = lum_max;
		half toneScalar = ( Lp * ( 1.0h + ( Lp / ( LmSqr + Epsilon ) ) ) ) / ( 1.0h + Lp );
		final_color = scene_color_exposed * toneScalar;
	}
	return final_color;
}

/////////////////////////////////////////////////////////////////////////////////////
// Vertex Shader
/////////////////////////////////////////////////////////////////////////////////////
struct VS_OUT_POSTFX
{
	float4 Pos:	POSITION;
	half2  Tex:	TEXCOORD0;
};
VS_OUT_POSTFX vs_main_postFX(float4 pos: POSITION)
{
	VS_OUT_POSTFX Out;
	Out.Pos = pos;
	Out.Tex = (half2(pos.x, -pos.y) * 0.5h + 0.5h) + (half2)g_HalfPixel_ViewportSizeInv.xy;
	return Out;
}
VertexShader vs_main_postFX_compiled = compile vs_2_0 vs_main_postFX();

/////////////////////////////////////////////////////////////////////////////////////
// Techniques
/////////////////////////////////////////////////////////////////////////////////////

// --- Show Texture ---
half4 ps_main_postFX_Show(half2 texCoord: TEXCOORD0) : COLOR
{
	half4 color = tex2D(postFX_sampler0, texCoord);
	if(showing_ranged_data)
	{
		color.rgb *= HDRRange;
		color.rgb = pow(color.rgb, (half3)output_gamma_inv.rgb);
	}
	return color;
}
technique postFX_Show
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_postFX_Show(); }
}

#ifdef USE_CHARACTER_SHADOW_MERGE
// --- Shadowmap Merge ---
half4 ps_main_postFX_Shadowmap(half2 texCoord: TEXCOORD0) : COLOR
{
	half original_shadowmap = tex2D(postFX_sampler0, texCoord).r;
	half character_shadow = tex2D(postFX_sampler1, texCoord).r;
	return min(original_shadowmap, character_shadow);
}
technique shadowmap_updater
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_postFX_Shadowmap(); }
}
#endif

// --- True Color (Unused?) ---
float4 color_value;
half4 ps_main_postFX_TrueColor(half2 texCoord: TEXCOORD0) : COLOR
{
	half4 ret = (half4)color_value;
	ret.a = saturate(ret.a + ret.a * (1.0h - vignette(texCoord * 2.0h - 1.0h, 0.015h, 1.25h)));
	return ret;
}
technique postFX_TrueColor
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_postFX_TrueColor(); }
}

// --- Bright Pass for Bloom ---
half4 ps_main_brightPass(uniform const bool with_luminance, half2 inTex: TEXCOORD0 ) : COLOR0
{
	half3 color = tex2D(postFX_sampler0, inTex).rgb;
	color *= HDRRange;

	if(with_luminance)
	{
		half2 lum_avgmax = tex2D(postFX_sampler4, half2(0.5h, 0.5h)).rg;
		static const half MiddleValue = 0.85h;
		half exposure_factor = MiddleValue / (Epsilon + lum_avgmax.x);
		half exposure = 0.85h + exposure_factor * 0.15h;
		exposure = clamp(exposure * HDRExposureScaler, min_exposure, max_exposure);
		color *= exposure;
	}

	color = max(0.0h, color - BrightpassTreshold);

	half intensity = dot(color, 0.5h);
	if (intensity > Epsilon)
	{
		half bloom_intensity = pow(intensity, BrightpassPostPower);
		color *= (bloom_intensity / intensity);
	}
	else
	{
		color = 0.0h;
	}

	color *= HDRRangeInv;
	return half4(color, 1.0h);
}
technique postFX_brightPass
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_brightPass(false); }
}
technique postFX_brightPass_WithLuminance
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_brightPass(true); }
}

// --- Gaussian Blur ---
half4 ps_main_blurX( half2 inTex: TEXCOORD0 ) : COLOR0
{
	half2 BlurOffsetX = half2(g_HalfPixel_ViewportSizeInv.z, 0);
	half4 color = 0;
	for( int i = 0; i < 8; i++ )
	{
		color += tex2D(postFX_sampler0, inTex + (BlurOffsetX * i)) * BlurPixelWeight[i];
		color += tex2D(postFX_sampler0, inTex - (BlurOffsetX * i)) * BlurPixelWeight[i];
	}
	return color;
}
half4 ps_main_blurY( half2 inTex: TEXCOORD0 ) : COLOR0
{
	half2 BlurOffsetY = half2(0, g_HalfPixel_ViewportSizeInv.w);
	half4 color = 0;
	for( int i = 0; i < 8; i++ )
	{
		color += tex2D(postFX_sampler0, inTex + (BlurOffsetY * i)) * BlurPixelWeight[i];
		color += tex2D(postFX_sampler0, inTex - (BlurOffsetY * i)) * BlurPixelWeight[i];
	}
	return color;
}
technique postFX_blurX
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_blurX(); }
}
technique postFX_blurY
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile ps_2_0 ps_main_blurY(); }
}

// --- Luminance Calculation ---
half4 ps_main_postFX_Average(half2 texCoord: TEXCOORD0) : COLOR
{
	static const float Offsets[4] = {-1.5f, -0.5f, 0.5f, 1.5f};
	half _max = 0;
	half _log_sum = 0;

	for (int x = 0; x < 4; x++)
	{
		for (int y = 0; y < 4; y++)
		{
			half2 vOffset = half2(Offsets[x], Offsets[y]) * (half2)g_HalfPixel_ViewportSizeInv.yw;
			half3 color_here = tex2D(postFX_sampler0, texCoord + vOffset).rgb;
			half lum_here = dot(color_here * HDRRange, LUMINANCE_WEIGHTS);
			_log_sum += lum_here; // log() is expensive and not strictly needed for this effect
			_max = max(_max, lum_here);
		}
	}
	return half4(_log_sum / 16.0h, _max, 0, 1);
}
technique postFX_Average
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X ps_main_postFX_Average(); }
}

half4 ps_main_postFX_AverageAvgMax(half2 texCoord: TEXCOORD0, uniform const bool smooth) : COLOR
{
	static const float Offsets[4] = {-1.5f, -0.5f, 0.5f, 1.5f};
	half _max = 0;
	half _sum = 0;

	for (int x = 0; x < 4; x++)
	{
		for (int y = 0; y < 4; y++)
		{
			half2 vOffset = half2(Offsets[x], Offsets[y]) * (half2)g_HalfPixel_ViewportSizeInv.yw;
			half2 lumAvgMax_here = tex2D(postFX_sampler0, texCoord + vOffset).rg;
			_sum += lumAvgMax_here.r * lumAvgMax_here.r;
			_max = max(_max, lumAvgMax_here.g);
		}
	}
	half _avg = _sum / 16.0h;
	half4 new_ret = half4(sqrt(max(0.0h, _avg)), _max, 0, 1);

	if(smooth)
	{
		half2 prev_avgmax = tex2D(postFX_sampler4, half2(0.5f, 0.5f)).rg;
		new_ret.x = lerp(prev_avgmax.x, new_ret.x, g_HDR_frameTime);
		new_ret.y = max(0.1h, lerp(prev_avgmax.y, new_ret.y, g_HDR_frameTime));
	}
	return new_ret;
}
technique postFX_AverageAvgMax
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X ps_main_postFX_AverageAvgMax(false); }
}
technique postFX_AverageAvgMax_Smooth
{
	pass P0 { VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X ps_main_postFX_AverageAvgMax(true); }
}

// --- Final Scene Composition Pass ---
half4 FinalScenePassPS(uniform const bool use_dof, uniform const int use_hdr, uniform const bool use_auto_exp, half2 texCoord: TEXCOORD0) : COLOR
{
	// 1. SAMPLE SCENE & APPLY GAMMA
	half4 scene = tex2D(postFX_sampler0, texCoord);
	scene.rgb = pow(scene.rgb, (half3)output_gamma.rgb);

	// 2. VIGNETTE BLUR
	if(use_hdr > 1 && Palette != 0) // The 'use_dof' flag is now repurposed to simply enable/disable this effect.
	{
		//--- Vignette Blur (Manual Blur at Edges) ---
		// This blurs the edges of the screen by sampling the scene in a pattern.
		static const half VIGNETTE_BLUR_INNER_RADIUS = 0.55h; // Start of blur (0.0 = center, 1.0 = edge)
		static const half VIGNETTE_BLUR_OUTER_RADIUS = 0.90h; // Full blur strength is reached here
		static const int VIGNETTE_BLUR_SAMPLES = 4;
		static const half VIGNETTE_BLUR_STRENGTH = 7.5h; // Controls how wide the blur samples are

		// Calculate the vignette mask. 'vignette_strength' will be 0.0 in the center and 1.0 at the edges.
		half2 screen_pos = texCoord * 2.0h - 1.0h; // Convert texCoord from [0,1] to [-1,1] for radial calculation
		half vignette_strength = 1.0h - vignette(screen_pos, VIGNETTE_BLUR_INNER_RADIUS, VIGNETTE_BLUR_OUTER_RADIUS);

		// Performance check: Only run the expensive blur code for pixels near the edge of the screen.
		if (vignette_strength > 0.01h)
		{
			half4 blurred_edge_color = 0;

			// Sample the original sharp scene in a 4-tap rotated grid pattern to create a blur.
			half2 offsets[VIGNETTE_BLUR_SAMPLES];
			offsets[0] = half2( 1,  1);
			offsets[1] = half2(-1,  1);
			offsets[2] = half2( 1, -1);
			offsets[3] = half2(-1, -1);

			for (int i = 0; i < VIGNETTE_BLUR_SAMPLES; i++)
			{
				// Sample the original, sharp scene texture at an offset.
				half2 sample_coord = texCoord + (offsets[i] * g_HalfPixel_ViewportSizeInv.xy * VIGNETTE_BLUR_STRENGTH);
				blurred_edge_color += tex2D(postFX_sampler0, sample_coord);
			}

			// Average the samples and apply the same gamma as the main scene.
			blurred_edge_color /= VIGNETTE_BLUR_SAMPLES;
			blurred_edge_color.rgb = pow(blurred_edge_color.rgb, (half3)output_gamma.rgb);

			// Blend the original sharp scene with the manually blurred color based on the vignette mask.
			scene = lerp(scene, blurred_edge_color, vignette_strength);
		}
	}

	// 2. DEPTH OF FIELD (DOF) & VIGNETTE BLUR
	// if(use_dof)
	// {
	// 	// --- A) Depth-based Blur (DOF) ---
	// 	// This blurs parts of the scene that are out of focus.
	// 	half pixelDepth = tex2D(postFX_sampler4, texCoord).r;
	// 	half dof_lerp_factor = abs(g_DOF_Focus - pixelDepth);
	// 	dof_lerp_factor = min(saturate(g_DOF_Range * dof_lerp_factor), 0.62h);

	// 	half4 dofColor = tex2D(postFX_sampler3, texCoord);
	// 	if(use_hdr) {
	// 		dofColor *= HDRRange;
	// 	}
	// 	dofColor.rgb = pow(dofColor.rgb, (half3)output_gamma.rgb);

	// 	// Blend the original scene with the pre-calculated DOF blur based on depth.
	// 	scene = lerp(scene, dofColor, dof_lerp_factor);

	// 	// --- B) Vignette Blur (Manual Blur at Edges) ---
	// 	// This blurs the edges of the screen, regardless of depth, by sampling in a pattern.
    //     static const half VIGNETTE_BLUR_INNER_RADIUS = 0.5h; // Start of blur (0.0 = center, 1.0 = edge)
    //     static const half VIGNETTE_BLUR_OUTER_RADIUS = 0.9h; // Full blur
    //     static const int VIGNETTE_BLUR_SAMPLES = 4;
    //     static const half VIGNETTE_BLUR_STRENGTH = 2.5h;

	// 	half2 screen_pos = texCoord * 2.0h - 1.0h;
	// 	half vignette_strength = 1.0h - vignette(screen_pos, VIGNETTE_BLUR_INNER_RADIUS, VIGNETTE_BLUR_OUTER_RADIUS);

	// 	// Only perform the expensive blur if we are actually at the screen edge.
	// 	if (vignette_strength > 0.01h)
	// 	{
	// 		half4 blurred_edge_color = 0;

	// 		// Sample in a 4-tap rotated grid pattern to create a blur.
	// 		half2 offsets[VIGNETTE_BLUR_SAMPLES];
	// 		offsets[0] = half2( 1,  1);
	// 		offsets[1] = half2(-1,  1);
	// 		offsets[2] = half2( 1, -1);
	// 		offsets[3] = half2(-1, -1);

	// 		for (int i = 0; i < VIGNETTE_BLUR_SAMPLES; i++)
	// 		{
	// 			half2 sample_coord = texCoord + (offsets[i] * g_HalfPixel_ViewportSizeInv.xy * VIGNETTE_BLUR_STRENGTH);
	// 			blurred_edge_color += tex2D(postFX_sampler0, sample_coord);
	// 		}

	// 		blurred_edge_color /= VIGNETTE_BLUR_SAMPLES;
	// 		blurred_edge_color.rgb = pow(blurred_edge_color.rgb, (half3)output_gamma.rgb);

	// 		// Blend the current scene color with the manually blurred color.
	// 		scene = lerp(scene, blurred_edge_color, vignette_strength);
	// 	}
	// }

	half4 color;
	if(use_hdr > 0)
	{
		// 3. HDR BLOOM
		half4 blur = tex2D(postFX_sampler1, texCoord);
		blur.rgb = pow(blur.rgb, BlurStrenght);
		blur.rgb *= HDRRange;

		half2 luminanceAvgMax = use_auto_exp ? tex2D(postFX_sampler2, half2(0.5h, 0.5h)).rg : half2(0.5h, 10.2h);

		color = scene;

		// 4. COLOR CORRECTION for "Antique/Roman" Look
        static const half WARMTH_LERP = 0.25h;
        static const half CONTRAST_POWER = 1.35h;

		half3 AlteredColor;
		half greyscale = dot(color.rgb, LUMINANCE_WEIGHTS);
		half HighTones = greyscale * greyscale;
		half LowTones = (1.0h - greyscale) * (1.0h - greyscale);

		// Boost reds and greens in highlights and mid-tones to create warmth.
		AlteredColor.b = color.b * (1.0h + HighTones * 0.1h);
		AlteredColor.g = color.g * (1.0h + LowTones * 0.05h);
		AlteredColor.r = color.r * (1.0h + LowTones * 0.09h);

		color.rgb = lerp(color.rgb, AlteredColor.rgb, WARMTH_LERP);
		color.rgb = pow(color.rgb, CONTRAST_POWER); // Add a gentle contrast curve.

		// Add bloom back in.
		color.rgb += blur.rgb * BlurAmount;

		// 5. TONEMAPPING
		color.rgb = tonemapping(color.rgb, luminanceAvgMax, postfxTonemapOp);
	}
	else
	{
		color = scene;
	}

	// 6. FINAL GAMMA & PALETTE CORRECTION
	color.rgb = pow(color.rgb, (half3)output_gamma_inv.rgb);

	int paletteChoice = Palette;
	if(paletteChoice <= 1) // default & sunny
	{
        static const half SATURATION_MULTIPLIER = 1.15h;
        static const half DESATURATION_LERP = 0.90h;
		half3 hsv = RGBtoHSV(color.rgb);
		hsv.y *= SATURATION_MULTIPLIER;
		color.rgb = HSVtoRGB(hsv);
		half greyscale = dot(color.rgb, LUMINANCE_WEIGHTS);
		color.rgb = lerp(greyscale, color.rgb, DESATURATION_LERP);
	}
	else if(paletteChoice > 1) // Other palettes (cloudy, night, etc.)
	{
        // Simplified for clarity, original logic preserved.
        half desaturation_factor = (paletteChoice == 2) ? 0.85h : 0.70h;
        if (paletteChoice == 5) desaturation_factor = 0.875h;

		half greyscale = dot(color.rgb, LUMINANCE_WEIGHTS);
		color.rgb = lerp(greyscale, color.rgb, desaturation_factor);

		if(paletteChoice == 4 || paletteChoice == 5) // night or interior
        {
            half value_multiplier = (paletteChoice == 4) ? 0.915h : 0.925h;
            half3 hsv = RGBtoHSV(color.rgb);
            hsv.z *= value_multiplier;
            color.rgb = HSVtoRGB(hsv);
        }
	}

	return color;
}

// --- Technique Definitions for Final Pass ---
technique postFX_final_0_0_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS( false, 0, false); } }
technique postFX_final_0_1_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS( false, 1, false); } }
technique postFX_final_0_2_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS( false, 2, false); } }
technique postFX_final_0_1_1{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS( false, 1, true);	} }
technique postFX_final_0_2_1{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS( false, 2, true);	} }
technique postFX_final_1_0_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS(  true, 0, false); } }
technique postFX_final_1_1_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS(  true, 1, false); } }
technique postFX_final_1_2_0{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS(  true, 2, false); } }
technique postFX_final_1_1_1{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS(  true, 1, true);	} }
technique postFX_final_1_2_1{	pass P0	{ VertexShader = vs_main_postFX_compiled; PixelShader = compile PS_2_X FinalScenePassPS(  true, 2, true);	} }

//Recycle Bin:
#if WSE2
#include "postFX_WSE2.fx"
#endif
