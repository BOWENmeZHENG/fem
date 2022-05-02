import math
import numpy as np


def define_pts(theta=20 / 180 * 3.1416, size=0.2, thickness=0.02, extension=0.25):
    # Outer contour
    pts_outer = np.array([
        [size, size],
        [0, size * (1 - math.tan(theta))],
        [-size, size],
        [-size * (1 - math.tan(theta)), 0],
        [-size, -size],
        [0, -size * (1 - math.tan(theta))],
        [size, -size],
        [size * (1 - math.tan(theta)), 0],
    ])

    # Inner contour
    corner_shift = thickness / math.sin(3.1416 / 4 - theta) * math.sin(3.1416 / 4)
    pts_inner = np.array([
        [size - corner_shift, size - corner_shift],
        [0, size * (1 - math.tan(theta)) - thickness],
        [-size + corner_shift, size - corner_shift],
        [-size * (1 - math.tan(theta)) + thickness, 0],
        [-size + corner_shift, -size + corner_shift],
        [0, -size * (1 - math.tan(theta)) + thickness],
        [size - corner_shift, -size + corner_shift],
        [size * (1 - math.tan(theta)) - thickness, 0],
    ])

    # Extensions
    mid = size * (1 - math.tan(theta)) - thickness / 2
    ext_1 = np.array([
        [extension, -thickness / 2],
        [extension, thickness / 2],
        [mid, thickness / 2],
        [mid, -thickness / 2]
    ])
    ext_2 = np.array([
        [thickness / 2, mid],
        [thickness / 2, extension],
        [-thickness / 2, extension],
        [-thickness / 2, mid]
    ])
    ext_3 = np.array([
        [-extension, thickness / 2],
        [-extension, -thickness / 2],
        [-mid, -thickness / 2],
        [-mid, thickness / 2]
    ])
    ext_4 = np.array([
        [-thickness / 2, -mid],
        [-thickness / 2, -extension],
        [thickness / 2, -extension],
        [thickness / 2, -mid]
    ])

    return pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4
