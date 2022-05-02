from geometry import define_pts as pts
import matplotlib.pyplot as plt

pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4 = pts()

plt.figure(figsize=(8, 8))
plt.plot(pts_outer[:, 0], pts_outer[:, 1])
plt.plot(pts_inner[:, 0], pts_inner[:, 1])
plt.plot(ext_1[:, 0], ext_1[:, 1])
plt.plot(ext_2[:, 0], ext_2[:, 1])
plt.plot(ext_3[:, 0], ext_3[:, 1])
plt.plot(ext_4[:, 0], ext_4[:, 1])
plt.show()
