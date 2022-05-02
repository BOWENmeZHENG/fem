from geometry import define_pts as pts
import graphing
import fem
from solidspy import solids_GUI
import matplotlib.pyplot as plt

pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4 = pts()
mesh = fem.meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4)
fem.write_files(mesh)

disp = solids_GUI(folder="")  # run the Finite Element Analysis
plt.show()    # plot contours


# graphing.scatter_nodes(mesh.points)
# graphing.plot_parts([pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4])
