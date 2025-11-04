from __future__ import absolute_import
from header_postfx import *

####################################################################################################################
#  PostFX Parameters - Tweaked for a vibrant, warm "Antique/Roman" look.
#
#  - "default" and "sunny" are now warmer and more saturated.
#  - "sunset" has a richer, more golden bloom.
#  - "night" and "indoors" are warmer, simulating torch/firelight.
#  - "cloudy" and "overcast" are less desaturated to retain some color.
#
#  Parameter Fields:
#  1) id (string)
#  2) flags (int)
#  3) tonemap operator (0-3)
#  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
#  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
#  6) shader parameters3 [ Not used by this shader, but kept for compatibility ]
####################################################################################################################

postfx_params = [
    # Default/Sunny: Increased contrast and warmth, subtle bloom.
    ("default", 0, 0, [128.0, 1.0, 1.35, 10.0], [0.90, 1.40, 1.20, 0.15], [1.0, 1.0, 2.0, 1.0]),
    ("sunny",   0, 0, [128.0, 0.9, 1.25, 10.0], [0.85, 1.50, 1.10, 0.18], [1.0, 1.0, 2.8, 1.0]),

    # Map: Brighter and more saturated to make details clear.
    ("map_params", 0, 0, [128.0, 1.0, 1.25, 10.0], [0.70, 2.5, 1.20, 0.05], [1.0, 1.0, 2.4, 1.0]),

    # Indoors: Warmer and darker, with a soft bloom to simulate firelight.
    ("indoors", 0, 0, [128.0, 1.0, 1.25, 10.0], [0.60, 2.0, 1.5, 0.10], [0.48, 1.0, 1.6, 5.0]),

    # Sunset: Rich golden/orange bloom.
    ("sunset", 0, 0, [128.0, 0.8, 1.1, 1.0], [0.50, 1.8, 1.4, 0.25], [1.0, 1.0, 2.0, 1.0]),

    # Night: Darker, but retains some warmth and color. Less blue/grey.
    ("night", 0, 0, [128.0, 1.0, 1.25, 10.0], [0.70, 2.0, 1.2, 0.05], [1.0, 1.0, 2.4, 4.0]),

    # Cloudy/Overcast: Less desaturated than before to keep the world from looking too dull.
    ("cloudy", 0, 0, [128.0, 1.0, 1.1, 0.0], [0.40, 2.0, 1.8, 0.20], [1.0, 1.0, 1.2, 2.0]),
    ("overcast", 0, 0, [128.0, 1.0, 1.0, 0.0], [0.35, 2.5, 2.0, 0.10], [1.0, 1.0, 0.8, 3.0]),

    # High Contrast: Kept for artistic effect.
    ("high_contrast",  0, 3, [128.0, 1.0, 1.29, 10.0], [0.43, 2.0, 1.05, 0.05], [1.0, 1.0, 4.8, 1.0]),
]