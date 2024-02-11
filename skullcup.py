# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

from pathlib import Path
import pymesh
from scipy.spatial.transform import Rotation
from fix_mesh.fix_mesh import fix_mesh

# Load mesh files
#
# Mesh files to be place in same directory as this script

filenameCup = '/working/cup_fixed.stl'
filenameSkull = '/working/skull_fixed.stl'

print('Loading cup')

if (Path(filenameCup).exists()):
    cupMesh = pymesh.load_mesh(filenameCup)
else:
    # https://cults3d.com/en/3d-model/home/coffee-cup
    cupMesh = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
    print('Fixing cup')
    cupMesh = fix_mesh(cupMesh)
    pymesh.save_mesh(filenameCup, cupMesh)

print('Loading skull')

if (Path(filenameSkull).exists()):
    skullMesh = pymesh.load_mesh(filenameSkull)
else:
    # https://cults3d.com/en/3d-model/various/to-make-or-not-to-make
    skullMesh = pymesh.load_mesh('/working/Scull_geant_fix02.stl')
    print('Fixing skull')
    skullMesh = fix_mesh(skullMesh)
    pymesh.save_mesh(filenameSkull, skullMesh)

# Helper class


class MeshObj(object):

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


# Helper functions

def convex_hull(meshObj):
    name = 'convex_hull' + \
        meshObj.name if meshObj.name[0] == '(' else 'convex_hull(' + \
        meshObj.name + ')'

    print(name)
    return MeshObj(name, pymesh.convex_hull(meshObj.mesh()))


def transformMesh(mesh, fn):
    return pymesh.form_mesh([fn(v) for v in mesh.vertices], mesh.faces)


# Handle
#
# We use a convex hull to 'fill' the cup and thus exclude the skull from the cup's
# interior.  This means we have to exclude any other parts of the cup which are not
# convex, meaning the handle and the lip of the cup.
#
# We want a box containing the cup's handle, and a tiny sliver of the cup just so we can
# be certain we're not missing any of the handle.  Any amount of cup that doesn't
# cut through to the cup's interior will be fine.
print('Calculating handle')

handleBoxRotationMatrix = Rotation.from_euler('z', 5, degrees=True).as_matrix()

handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = MeshObj('handle', transformMesh(
    handle, lambda v: handleBoxRotationMatrix.dot(v)))

# Lip - a box containing the lip of the cup

print('Calculating lip')

lip = MeshObj('lip', pymesh.generate_box_mesh([-70, 35, -70], [70, 50, 70]))

# Cup

print('Orientating cup')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()

cupMesh = transformMesh(cupMesh, lambda v: cupRotationMatrix.dot(v))

cup = MeshObj('cup', cupMesh)

cupWithoutHandle = (cup - handle).mesh()

# Skull

print('Orientating skull')

# first scale skull appropriately with respect to cup, and align rotationally

scale = 0.6

skullRotationMatrix = Rotation.from_euler(
    'xy', [-90, 90], degrees=True).as_matrix()

skullMesh = transformMesh(skullMesh, lambda v: scale *
                          skullRotationMatrix.dot(v))

# now center the skull horizantally, and have its base aligned with the base of the cup

cupCenterX = (cupWithoutHandle.bbox[0][0] + cupWithoutHandle.bbox[1][0]) / 2
skullCenterX = (skullMesh.bbox[0][0] + skullMesh.bbox[1][0]) / 2
xAdjustment = cupCenterX - skullCenterX
yAdjustment = cupMesh.bbox[0][1] - skullMesh.bbox[0][1]

skull = MeshObj('skull', transformMesh(skullMesh, lambda v: v +
                [xAdjustment, yAdjustment, 20]))

# Skullcup

print('Combining to create skullcup')

skullcup = skull - lip - (convex_hull(cup - handle - lip) - cup) + cup

print('Scaling skullcup')

# Make it 100 units tall, which is great for interpreting as milimeters (mm)
scale = 100 / (skullcup.mesh().bbox[1][1] - skullcup.mesh().bbox[0][1])

skullcup = MeshObj('skull', transformMesh(
    skullcup.mesh(), lambda v: scale * v))

print('Fixing skullcup')

skullcup = fix_mesh(skullcup.mesh())

print('Saving skullcup')

pymesh.save_mesh('/working/skullcup.stl', skullcup)

print('Done')
