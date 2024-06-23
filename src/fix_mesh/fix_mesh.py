import pymesh
from numpy.linalg import norm

def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))

def fix_mesh(mesh, detail="normal"):
    bbox_min, bbox_max = mesh.bbox
    diag_len = norm(bbox_max - bbox_min)
    if detail == "normal":
        target_len = diag_len * 5e-3
    elif detail == "high":
        target_len = diag_len * 2.5e-3
    elif detail == "low":
        target_len = diag_len * 1e-2

    mesh_info(mesh)

    print('remove_duplicated_vertices')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh)
    mesh_info(mesh)

    print('remove_degenerated_triangles')
    mesh, __ = pymesh.remove_degenerated_triangles(mesh, 100)
    mesh_info(mesh)

    print('split_long_edges')
    mesh, __ = pymesh.split_long_edges(mesh, target_len)
    mesh_info(mesh)

    print('resolve_self_intersection')
    mesh = pymesh.resolve_self_intersection(mesh)
    mesh_info(mesh)

    print('remove_duplicated_faces')
    mesh, __ = pymesh.remove_duplicated_faces(mesh)
    mesh_info(mesh)

    print('remove_obtuse_triangles')
    mesh, __ = pymesh.remove_obtuse_triangles(mesh, 179.0, 5)
    mesh_info(mesh)

    print('remove_isolated_vertices')
    mesh, __ = pymesh.remove_isolated_vertices(mesh)
    mesh_info(mesh)

    return mesh
