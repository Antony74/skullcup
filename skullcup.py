# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from fix_mesh.fix_mesh import fix_mesh
from helpers import load_fixed_mesh, MeshObj, convex_hull
from AffineMatrix import AffineMatrix

# Load mesh files
#
# Mesh files to be place in same directory as this script

# https://cults3d.com/en/3d-model/home/coffee-cup
cupMesh = load_fixed_mesh(
    '/working/Coffee_Cup.A.1.stl', '/working/cup_fixed.stl')

# https://cults3d.com/en/3d-model/various/to-make-or-not-to-make
skullMesh = load_fixed_mesh(
    '/working/Scull_geant_fix02.stl', '/working/skull_fixed.stl')


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

handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = MeshObj('handle', AffineMatrix().rotateZ(5, degrees=True).dot(handle))

# Lip - a box containing the lip of the cup

print('Calculating lip')

lip = MeshObj('lip', pymesh.generate_box_mesh([-70, 35, -70], [70, 50, 70]))

# Cup

print('Orientating cup')

cupMesh = AffineMatrix().rotateY(180, degrees=True).dot(cupMesh)

cup = MeshObj('cup', cupMesh)

cupWithoutHandle = (cup - handle).mesh()

# Skull

print('Orientating skull')

# first scale skull appropriately with respect to cup, and align rotationally

scale = 0.6

skullMesh = AffineMatrix().scale(
    scale).rotateX(-90, degrees=True).rotateY(90, degrees=True).dot(skullMesh)

# now center the skull horizontally, and have its base aligned with the base of the cup

cupCenterX = (cupWithoutHandle.bbox[0][0] + cupWithoutHandle.bbox[1][0]) / 2
skullCenterX = (skullMesh.bbox[0][0] + skullMesh.bbox[1][0]) / 2
xAdjustment = cupCenterX - skullCenterX
yAdjustment = cupMesh.bbox[0][1] - skullMesh.bbox[0][1]

skull = MeshObj('skull', AffineMatrix().translate(xAdjustment, yAdjustment, 20).dot(skullMesh))

# Skullcup

print('Combining to create skullcup')

skullcup = skull - lip - (convex_hull(cup - handle - lip) - cup) + cup

print('Scaling skullcup')

# Make it 100 units tall, which is great for interpreting as millimeters (mm)
scale = 100 / (skullcup.mesh().bbox[1][1] - skullcup.mesh().bbox[0][1])

skullcup = MeshObj('skull', AffineMatrix().scale(scale).dot(skullcup.mesh()))

print('Fixing skullcup')

skullcup = fix_mesh(skullcup.mesh())

print('Saving skullcup')

pymesh.save_mesh('/working/skullcup.stl', skullcup)

print('Done')
