import pygmsh


def meshing(pts_outer, ext_1, ext_2, ext_3, ext_4, mesh_size=0.01):
    with pygmsh.occ.Geometry() as geom:
        parts_1 = [geom.add_polygon(pts_outer, mesh_size=mesh_size),
                   geom.add_polygon(ext_1, mesh_size=mesh_size),
                   geom.add_polygon(ext_2, mesh_size=mesh_size),
                   geom.add_polygon(ext_3, mesh_size=mesh_size),
                   geom.add_polygon(ext_4, mesh_size=mesh_size)]
        geom.boolean_union(parts_1)
        mesh = geom.generate_mesh()
    return mesh.points
