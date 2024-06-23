import pymesh
from numpy.linalg import norm

def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))

def fix_mesh(mesh, tolerance=0.01):
    mesh_info(mesh)

    print('remove_duplicated_vertices')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh, tolerance)
    mesh_info(mesh)

    # print('remove_degenerated_triangles')
    # mesh, __ = pymesh.remove_degenerated_triangles(mesh, 100)
    # mesh_info(mesh)

    print('remove_duplicated_faces')
    mesh, __ = pymesh.remove_duplicated_faces(mesh, tolerance)
    mesh_info(mesh)

    print('resolve_self_intersection')
    mesh = pymesh.resolve_self_intersection(mesh)
    mesh_info(mesh)

    return mesh
