import pymesh
from numpy.linalg import norm
import numpy as np

def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))

def fix_mesh_lite(mesh, tolerance=0.01):
    bbox_min, bbox_max = mesh.bbox
    diag_len = norm(bbox_max - bbox_min)
    target_len = diag_len * 5e-3

    print('remove_duplicated_vertices')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh, tolerance)
    mesh_info(mesh)

    print('remove_degenerated_triangles')
    mesh, __ = pymesh.remove_degenerated_triangles(mesh, 100)
    mesh_info(mesh)

    print('remove_duplicated_faces')
    mesh, __ = pymesh.remove_duplicated_faces(mesh, tolerance)
    mesh_info(mesh)

    print('split_long_edges')
    mesh, __ = pymesh.split_long_edges(mesh, target_len)
    mesh_info(mesh)

    print('resolve_self_intersection')
    mesh = pymesh.resolve_self_intersection(mesh)
    mesh_info(mesh)

    print('remove_duplicated_vertices 2')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh, tolerance)
    mesh_info(mesh)

    return mesh

