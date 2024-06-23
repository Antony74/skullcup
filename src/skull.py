import pymesh
from common.helpers import save_mesh_verbose
from common.AffineMatrix import AffineMatrix

# https://cults3d.com/en/3d-model/various/to-make-or-not-to-make
skullMesh = pymesh.load_mesh('Scull_geant_fix02.stl')

cupWithoutHandle = pymesh.load_mesh('working/cupWithoutHandle.stl')

scale = 0.6

skullMesh = AffineMatrix().scale(
    scale).rotateX(-90, degrees=True).rotateY(90, degrees=True).dot(skullMesh)

# now center the skull horizontally, and have its base aligned with the base of the cup

cupCenterX = (cupWithoutHandle.bbox[0][0] + cupWithoutHandle.bbox[1][0]) / 2
skullCenterX = (skullMesh.bbox[0][0] + skullMesh.bbox[1][0]) / 2
xAdjustment = cupCenterX - skullCenterX
yAdjustment = cupWithoutHandle.bbox[0][1] - skullMesh.bbox[0][1]

skull = AffineMatrix().translate(xAdjustment, yAdjustment, 20).dot(skullMesh)

save_mesh_verbose('working/skull.stl', skull)
