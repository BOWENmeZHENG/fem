import numpy as np
import pygmsh


def meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, inside_up, inside_down, mesh_size=0.01):
    with pygmsh.occ.Geometry() as geom:
        geom.characteristic_length_max = mesh_size
        outer = geom.add_polygon(pts_outer)
        inner = geom.add_polygon(pts_inner)
        shell = geom.boolean_difference(outer, inner)
        inside_up_struct = geom.add_polygon(inside_up)
        inside_down_struct = geom.add_polygon(inside_down)
        geom.boolean_union(
            [shell,
             inside_up_struct,
             inside_down_struct,
             geom.add_polygon(ext_1),
             geom.add_polygon(ext_2),
             geom.add_polygon(ext_3),
             geom.add_polygon(ext_4)
             ]
        )
        mesh = geom.generate_mesh()
    return mesh


def write_files(mesh, E=1.0e8, nu=0.3, load=-20.0e3):
    mesh_pts = mesh.points
    elements = mesh.cells_dict['triangle']

    # Write nodes.txt
    # fix bottom
    with open('nodes.txt', 'w') as f_nodes:
        for i, point in enumerate(mesh_pts):
            if point[1] == min(mesh_pts[:, 1]):
                bc_x, bc_y = -1, -1
            else:
                bc_x, bc_y = 0, 0
            f_nodes.write(f"{i:4} {point[0]:8.4f} {point[1]:8.4f}  {bc_x:4}  {bc_y:4} \n")

    # Write eles.txt
    with open('eles.txt', 'w') as f_eles:
        for i, element in enumerate(elements):
            f_eles.write(f"{i:4}   3   0  {element[0]:4} {element[1]:4}  {element[2]:4} \n")

    # Write mater.txt
    with open('mater.txt', 'w') as f_mater:
        f_mater.write(f"{E:8.4f} {nu:8.4f}")

    # Write mater.txt
    with open('loads.txt', 'w') as f_loads:
        for i, point in enumerate(mesh_pts):
            if point[1] == max(mesh_pts[:, 1]):
                f_loads.write(f"{i:4} {0.0:8.4f} {load:8.4f} \n")


def nodes_interested(mesh):
    mesh_pts = mesh.points
    id_up = np.argmax(mesh_pts[:, 1])
    id_right = np.argmax(mesh_pts[:, 0])
    id_left = np.argmin(mesh_pts[:, 0])

    return id_up, id_right, id_left
