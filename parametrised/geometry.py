import math
import numpy as np

PI = 3.1416


def define_pts(theta=20 / 180 * PI, alpha=15 / 180 * PI, size=0.2, thickness=0.02, extension=0.25):
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
        [0, size * (1 - math.tan(theta)) - thickness / math.cos(theta)],
        [-size + corner_shift, size - corner_shift],
        [-size * (1 - math.tan(theta)) + thickness / math.cos(theta), 0],
        [-size + corner_shift, -size + corner_shift],
        [0, -size * (1 - math.tan(theta)) + thickness / math.cos(theta)],
        [size - corner_shift, -size + corner_shift],
        [size * (1 - math.tan(theta)) - thickness / math.cos(theta), 0],
    ])

    # inside structure
    in_mid = (size - corner_shift) * (1 - math.tan(theta + alpha))
    in_close = in_mid + thickness / 2 / math.cos(theta + alpha)
    in_far = in_mid - thickness / 2 / math.cos(theta + alpha)
    corner_x_close = (size - corner_shift) - thickness / 2 * math.sin(theta + alpha)
    corner_y_close = (size - corner_shift) + thickness / 2 * math.cos(theta + alpha)
    corner_x_far = (size - corner_shift) + thickness / 2 * math.sin(theta + alpha)
    corner_y_far = (size - corner_shift) - thickness / 2 * math.cos(theta + alpha)
    inside_up = np.array([
        [-corner_x_close, corner_y_close],
        [-corner_x_far, corner_y_far],
        [0, in_far],
        [corner_x_far, corner_y_far],
        [corner_x_close, corner_y_close],
        [0, in_close]
    ])

    inside_down = np.array([
        [-corner_x_far, -corner_y_far],
        [-corner_x_close, -corner_y_close],
        [0, -in_close],
        [corner_x_close, -corner_y_close],
        [corner_x_far, -corner_y_far],
        [0, -in_far]
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
        [thickness / 2, in_mid],
        [thickness / 2, extension],
        [-thickness / 2, extension],
        [-thickness / 2, in_mid]
    ])
    ext_3 = np.array([
        [-extension, thickness / 2],
        [-extension, -thickness / 2],
        [-mid, -thickness / 2],
        [-mid, thickness / 2]
    ])
    ext_4 = np.array([
        [-thickness / 2, -in_mid],
        [-thickness / 2, -extension],
        [thickness / 2, -extension],
        [thickness / 2, -in_mid]
    ])

    return pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down
