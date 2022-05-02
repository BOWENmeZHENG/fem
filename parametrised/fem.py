import pygmsh


def meshing(pts_outer, pts_inner, ext_1, ext_2, ext_3, ext_4, mesh_size=0.008):
    with pygmsh.occ.Geometry() as geom:
        geom.characteristic_length_max = mesh_size
        outer = geom.add_polygon(pts_outer)
        parts = [outer,
                 geom.add_polygon(ext_1),
                 geom.add_polygon(ext_2),
                 geom.add_polygon(ext_3),
                 geom.add_polygon(ext_4)]
        # geom.boolean_union(parts)
        geom.boolean_difference(
            geom.boolean_union(parts),
            geom.add_polygon(pts_inner)
        )
        mesh = geom.generate_mesh()
    return mesh.points
