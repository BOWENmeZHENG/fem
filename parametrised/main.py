from geometry import define_pts as pts
import graphing
import fem
from solidspy import solids_GUI
import matplotlib.pyplot as plt

PI = 3.1416

pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down \
    = pts(theta=20 / 180 * PI, alpha=15 / 180 * PI, size=0.2, thickness=0.02, extension=0.25)
mesh = fem.meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down)
fem.write_files(mesh)

disp = solids_GUI(folder="")  # run the Finite Element Analysis
plt.show()    # plot contours


# graphing.scatter_nodes(mesh.points)
# graphing.plot_parts([pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down])
