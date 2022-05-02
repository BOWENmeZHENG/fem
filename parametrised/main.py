from geometry import define_pts as pts
import graphing
import fem

pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4 = pts()
mesh_points = fem.meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4)
graphing.scatter_nodes(mesh_points)
# graphing.plot_parts([pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4])
