# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from scipy.spatial.transform import Rotation


def transformMesh(mesh, fn):
    return pymesh.form_mesh([fn(v) for v in mesh.vertices], mesh.faces)


class MeshObj(object):

    def __init__(self, mesh):
        self._mesh = mesh

    def mesh(self):
        return self._mesh

    def __add__(self, other):
        return MeshObj(pymesh.boolean(self._mesh, other._mesh, 'union', 'cork'))

    def __sub__(self, other):
        return MeshObj(pymesh.boolean(self._mesh, other._mesh, 'difference', 'cork'))
    
    def convex_hull(self):
        return MeshObj(pymesh.convex_hull(self.mesh()))


scale = 0.6

# TO DO URL
cupMesh = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')

# TO DO URL
skullMesh = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()
handleBoxRotationMatrix = Rotation.from_euler('z', 5, degrees=True).as_matrix()

skullRotationMatrix = Rotation.from_euler(
    'xy', [-90, 90], degrees=True).as_matrix()

# We want a box containing the handle, and a tiny sliver of cup just so we can
# be certain we're not missing any of the handle.  Any amount of cup that doesn't
# cut through to the cup's interior will be fine.
handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = MeshObj(transformMesh(handle, lambda v: handleBoxRotationMatrix.dot(v)))

cupMesh = transformMesh(cupMesh, lambda v: cupRotationMatrix.dot(v))

cup = MeshObj(cupMesh)

cupWithoutHandle = (cup - handle).mesh()

skullMesh = transformMesh(skullMesh, lambda v: scale *
                      skullRotationMatrix.dot(v))

cupCenterX = (cupWithoutHandle.bbox[0][0] + cupWithoutHandle.bbox[1][0]) / 2
skullCenterX = (skullMesh.bbox[0][0] + skullMesh.bbox[1][0]) / 2
xAdjustment = cupCenterX - skullCenterX
yAdjustment = cupMesh.bbox[0][1] - skullMesh.bbox[0][1]

skull = MeshObj(transformMesh(skullMesh, lambda v: v + [xAdjustment, yAdjustment, 20]))

skullcup = skull - (cup - handle).convex_hull() + cup

pymesh.save_mesh('/working/skullcup.stl', skullcup.mesh())
