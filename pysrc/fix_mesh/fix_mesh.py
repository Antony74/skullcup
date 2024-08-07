#!/usr/bin/env python

"""
Remesh the input mesh to remove degeneracies and improve triangle quality.
"""

import argparse
import numpy as np
from numpy.linalg import norm
import pymesh
from fix_mesh.mesh_info import mesh_info


def fix_mesh(mesh, detail="normal", max_repeat=10):
    bbox_min, bbox_max = mesh.bbox
    diag_len = norm(bbox_max - bbox_min)
    if detail == "normal":
        target_len = diag_len * 5e-3
    elif detail == "high":
        target_len = diag_len * 2.5e-3
    elif detail == "low":
        target_len = diag_len * 1e-2
    print("Target resolution: {} mm".format(target_len))

    count = 0

    print('remove_duplicated_vertices')
    mesh, __ = pymesh.remove_duplicated_vertices(mesh)
    mesh_info(mesh)

    print('remove_degenerated_triangles')
    mesh, __ = pymesh.remove_degenerated_triangles(mesh, 100)
    mesh_info(mesh)

    # print('split_long_edges')
    # mesh, __ = pymesh.split_long_edges(mesh, target_len)
    # mesh_info(mesh)

    num_vertices = mesh.num_vertices
    while True:

        print(
            'collapse_short_edges ' +
            str(count + 1) + ' of ' + str(max_repeat + 1)
        )

        mesh, __ = pymesh.collapse_short_edges(mesh, 1e-6)
        mesh_info(mesh)

        print('collapse_short_edges')
        mesh, __ = pymesh.collapse_short_edges(mesh, target_len,
                                               preserve_feature=True)
        mesh_info(mesh)

        print('remove_obtuse_triangles')
        mesh, __ = pymesh.remove_obtuse_triangles(mesh, 150.0, 100)
        mesh_info(mesh)

        if mesh.num_vertices == num_vertices:
            break

        num_vertices = mesh.num_vertices
        count += 1
        if count > max_repeat:
            break

    print('resolve_self_intersection')
    mesh = pymesh.resolve_self_intersection(mesh)
    mesh_info(mesh)

    print('remove_duplicated_faces')
    mesh, __ = pymesh.remove_duplicated_faces(mesh)
    mesh_info(mesh)

    print('compute_outer_hull')
    mesh = pymesh.compute_outer_hull(mesh)
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


def old_fix_mesh(vertices, faces, detail="normal"):
    bbox_min = np.amin(vertices, axis=0)
    bbox_max = np.amax(vertices, axis=0)
    diag_len = norm(bbox_max - bbox_min)
    if detail == "normal":
        target_len = diag_len * 5e-3
    elif detail == "high":
        target_len = diag_len * 2.5e-3
    elif detail == "low":
        target_len = diag_len * 1e-2
    print("Target resolution: {} mm".format(target_len))

    count = 0
    vertices, faces = pymesh.split_long_edges(vertices, faces, target_len)
    num_vertices = len(vertices)
    while True:
        vertices, faces = pymesh.collapse_short_edges(vertices, faces, 1e-6)
        vertices, faces = pymesh.collapse_short_edges(vertices, faces,
                                                      target_len, preserve_feature=True)
        vertices, faces = pymesh.remove_obtuse_triangles(
            vertices, faces, 150.0, 100)
        if num_vertices == len(vertices):
            break
        num_vertices = len(vertices)
        print("#v: {}".format(num_vertices))
        count += 1
        if count > 10:
            break

    vertices, faces = pymesh.resolve_self_intersection(vertices, faces)
    vertices, faces = pymesh.remove_duplicated_faces(vertices, faces)
    vertices, faces, _ = pymesh.compute_outer_hull(vertices, faces, False)
    vertices, faces = pymesh.remove_duplicated_faces(vertices, faces)
    vertices, faces = pymesh.remove_obtuse_triangles(vertices, faces, 179.0, 5)
    vertices, faces, voxels = pymesh.remove_isolated_vertices(vertices, faces)
    return vertices, faces


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__)
    parser.add_argument("--timing", help="print timing info",
                        action="store_true")
    parser.add_argument("--detail", help="level of detail to preserve",
                        choices=["low", "normal", "high"], default="normal")
    parser.add_argument("in_mesh", help="input mesh")
    parser.add_argument("out_mesh", help="output mesh")
    return parser.parse_args()


def main():
    args = parse_args()
    mesh = pymesh.meshio.load_mesh(args.in_mesh)

    mesh = fix_mesh(mesh, detail=args.detail)

    pymesh.meshio.save_mesh(args.out_mesh, mesh)

    if args.timing:
        pymesh.timethis.summarize()


if __name__ == "__main__":
    main()
