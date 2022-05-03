import math

from geometry import define_pts as pts
import graphing
import fem
from solidspy import solids_GUI
import matplotlib.pyplot as plt

PI = 3.1416


def run(theta, alpha, plot_contours=True, size=0.2, thickness=0.02, extension=0.25):
    pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down \
        = pts(theta=theta / 180 * PI, alpha=alpha / 180 * PI, size=size, thickness=thickness, extension=extension)
    mesh = fem.meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down)
    fem.write_files(mesh)

    disp = solids_GUI(plot_contours=plot_contours, folder="")  # run the Finite Element Analysis
    plt.show()  # plot contours
    return disp, mesh


def calc_pr(disp, mesh, theta, size=0.2, thickness=0.02):
    mid = size * (1 - math.tan(theta)) - thickness / 2
    id_up, id_right, id_left = fem.nodes_interested(mesh)
    disp_axial = disp[id_up, 1]
    disp_lateral = disp[id_right, 0] - disp[id_left, 0]
    strain_axial = disp_axial / (mid * 2)
    strain_lateral = disp_lateral / (mid * 2)
    pr = -strain_lateral / strain_axial
    return pr
# graphing.scatter_nodes(mesh.points)
# graphing.plot_parts([pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down])
