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


class MeshObj:

    def __init__(self, name, mesh):
        self.name = name
        self._mesh = mesh

    def mesh(self):
        return self._mesh

    def __add__(self, other):
        name = self.name + ' + ' + other.name
        print(name)
        return MeshObj('(' + name + ')', pymesh.boolean(self._mesh, other._mesh, 'union'))

    def __sub__(self, other):
        name = self.name + ' - ' + other.name
        print(name)
        return MeshObj('(' + name + ')', pymesh.boolean(self._mesh, other._mesh, 'difference'))


def convex_hull(meshObj):
    name = 'convex_hull' + \
        meshObj.name if meshObj.name[0] == '(' else 'convex_hull(' + \
        meshObj.name + ')'

    print(name)
    return MeshObj(name, pymesh.convex_hull(meshObj.mesh()))


def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))


def biggest_piece(mesh):
    def reducer(acc, piece): return acc if len(
        acc.faces) > len(piece.faces) else piece

    emptyMesh = pymesh.form_mesh(np.empty(0), np.empty([0, 0]))

    sep = pymesh.separate_mesh(mesh)

    return reduce(reducer, sep, emptyMesh)
