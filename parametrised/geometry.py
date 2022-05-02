import math
import numpy as np
import matplotlib.pyplot as plt

SIZE = 0.2
THETA = 20 / 180 * 3.1416

pts = np.array([
    [SIZE, SIZE],
    [0, SIZE * (1 - math.tan(THETA))],
    [-SIZE, SIZE],
    [-SIZE * (1 - math.tan(THETA)), 0],
    [-SIZE, -SIZE],
    [0, -SIZE * (1 - math.tan(THETA))],
    [SIZE, -SIZE],
    [SIZE * (1 - math.tan(THETA)), 0],
])

plt.figure(figsize=(8, 8))
plt.plot(pts[:, 0], pts[:, 1])
plt.show()
