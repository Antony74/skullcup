from pathlib import Path
from functools import reduce
import numpy as np
import pymesh
from fix_mesh.fix_mesh import fix_mesh


def load_fixed_mesh(originalFilename, fixedFilename, pinMesh=None):
    if (Path(fixedFilename).exists()):
        print('Loading ' + fixedFilename)
        mesh = pymesh.load_mesh(fixedFilename)
    else:
        print('Loading ' + originalFilename)
        mesh = pymesh.load_mesh(originalFilename)
        mesh_info(mesh)
        print('Fixing ' + originalFilename)
        mesh = fix_mesh(mesh)
        pymesh.save_mesh(fixedFilename, mesh)

    mesh_info(mesh)
    return mesh


def convex_hull(meshObj):
    name = 'convex_hull' + \
        meshObj.name if meshObj.name[0] == '(' else 'convex_hull(' + \
        meshObj.name + ')'

    print(name)
    result = meshObj.create(name, pymesh.convex_hull(meshObj.mesh()))
    pymesh.save_mesh('/skullcup/working/' + name + '.stl', result.mesh())
    return result


def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))


def biggest_piece(mesh):
    print('biggest_piece')

    def reducer(acc, piece): return acc if len(
        acc.faces) > len(piece.faces) else piece

    emptyMesh = pymesh.form_mesh(np.empty(0), np.empty([0, 0]))

    sep = pymesh.separate_mesh(mesh)

    result = reduce(reducer, sep, emptyMesh)
    mesh_info(result)

    return result
