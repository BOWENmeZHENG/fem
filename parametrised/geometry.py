import math
import numpy as np
import matplotlib.pyplot as plt

SIZE = 0.2
THETA = 20 / 180 * 3.1416
THICKNESS = 0.02
EXT = 0.25


# Outer contour
pts_outer = np.array([
    [SIZE, SIZE],
    [0, SIZE * (1 - math.tan(THETA))],
    [-SIZE, SIZE],
    [-SIZE * (1 - math.tan(THETA)), 0],
    [-SIZE, -SIZE],
    [0, -SIZE * (1 - math.tan(THETA))],
    [SIZE, -SIZE],
    [SIZE * (1 - math.tan(THETA)), 0],
])

# Inner contour
corner_shift = THICKNESS / math.sin(3.1416 / 4 - THETA) * math.sin(3.1416 / 4)
pts_inner = np.array([
    [SIZE - corner_shift, SIZE - corner_shift],
    [0, SIZE * (1 - math.tan(THETA)) - THICKNESS],
    [-SIZE + corner_shift, SIZE - corner_shift],
    [-SIZE * (1 - math.tan(THETA)) + THICKNESS, 0],
    [-SIZE + corner_shift, -SIZE + corner_shift],
    [0, -SIZE * (1 - math.tan(THETA)) + THICKNESS],
    [SIZE - corner_shift, -SIZE + corner_shift],
    [SIZE * (1 - math.tan(THETA)) - THICKNESS, 0],
])

# Extensions
mid = SIZE * (1 - math.tan(THETA)) - THICKNESS / 2
ext_1 = np.array([
    [EXT, -THICKNESS / 2],
    [EXT, THICKNESS / 2],
    [mid, THICKNESS / 2],
    [mid, -THICKNESS / 2]
])
ext_2 = np.array([
    [THICKNESS / 2, mid],
    [THICKNESS / 2, EXT],
    [-THICKNESS / 2, EXT],
    [-THICKNESS / 2, mid]
])
ext_3 = np.array([
    [-EXT, THICKNESS / 2],
    [-EXT, -THICKNESS / 2],
    [-mid, -THICKNESS / 2],
    [-mid, THICKNESS / 2]
])
ext_4 = np.array([
    [-THICKNESS / 2, -mid],
    [-THICKNESS / 2, -EXT],
    [THICKNESS / 2, -EXT],
    [THICKNESS / 2, -mid]
])


plt.figure(figsize=(8, 8))
plt.plot(pts_outer[:, 0], pts_outer[:, 1])
plt.plot(pts_inner[:, 0], pts_inner[:, 1])
plt.plot(ext_1[:, 0], ext_1[:, 1])
plt.plot(ext_2[:, 0], ext_2[:, 1])
plt.plot(ext_3[:, 0], ext_3[:, 1])
plt.plot(ext_4[:, 0], ext_4[:, 1])
plt.show()
