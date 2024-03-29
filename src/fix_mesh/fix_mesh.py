import pymesh
from numpy.linalg import norm

def fix_mesh(mesh, detail="normal"):
    bbox_min, bbox_max = mesh.bbox
    diag_len = norm(bbox_max - bbox_min)
    if detail == "normal":
        target_len = diag_len * 5e-3
    elif detail == "high":
        target_len = diag_len * 2.5e-3
    elif detail == "low":
        target_len = diag_len * 1e-2
    # print("Target resolution: {} mm".format(target_len))

    # count = 0
    print('remove_duplicated_vertices')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh)
    print('remove_degenerated_triangles')
    mesh, __ = pymesh.remove_degenerated_triangles(mesh, 100)
    print('split_long_edges')
    mesh, __ = pymesh.split_long_edges(mesh, target_len)
    # num_vertices = mesh.num_vertices
    # while True:
    #     mesh, __ = pymesh.collapse_short_edges(mesh, 1e-6)
    #     mesh, __ = pymesh.collapse_short_edges(mesh, target_len,
    #                                            preserve_feature=True)
    #     mesh, __ = pymesh.remove_obtuse_triangles(mesh, 150.0, 100)
    #     if mesh.num_vertices == num_vertices:
    #         break

    #     num_vertices = mesh.num_vertices
    #     print("#v: {}".format(num_vertices))
    #     count += 1
    #     if count > 10:
    #         break
    print('resolve_self_intersection')
    mesh = pymesh.resolve_self_intersection(mesh)
    print('remove_duplicated_faces')
    mesh, __ = pymesh.remove_duplicated_faces(mesh)
    # mesh = pymesh.compute_outer_hull(mesh)
    # mesh, __ = pymesh.remove_duplicated_faces(mesh)
    print('remove_obtuse_triangles')
    mesh, __ = pymesh.remove_obtuse_triangles(mesh, 179.0, 5)
    print('remove_isolated_vertices')
    mesh, __ = pymesh.remove_isolated_vertices(mesh)

    return mesh
