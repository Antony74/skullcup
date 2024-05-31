import json
import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import save_mesh_verbose
from common.linearMap import linearMap

radiusAdjust = -0.5

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')
unitPrism = pymesh.load_mesh('working/prism.stl')

with open('working/profile.json') as f:
    profile = json.load(f)

bands = profile['bands']
yMin = profile['yMin']
yMax = profile['yMax']
profile = profile['profile']

getBand = createBandedMap(bands, yMin, yMax)

patchRadius = 0.15
patchXMid = -0.5
patchXMin = patchXMid - patchRadius
patchXMax = patchXMid + patchRadius
patchYMin = linearMap(0.3, 0, 1, yMin, yMax)
patchYMax = linearMap(0.8, 0, 1, yMin, yMax)


def cupMap(theta, y):
    band = getBand(y)
    radius = profile[band] + radiusAdjust
    return AffineMatrix().translate(radius * math.cos(0), y, radius * math.sin(0)).rotateY(theta)


# 'patch' refers to the patch of the cup where we want the design,
# and the patchMap function maps to it from the unit square.
def patchMap(pt):
    x = pt[0]
    y = pt[1]
    return cupMap(linearMap(x, 0, 1, patchXMin * math.pi, patchXMax * math.pi), linearMap(y, 0, 1, patchYMin, patchYMax))


meshes = []

points = list(map(lambda pt: patchMap(pt).dot([1, 0, 0]),
                  [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]))

for index in range(0, len(points)):
    point = points[index]
    x = point[0]
    y = point[1]
    z = point[2]
    meshes.append(AffineMatrix().translate(x, y, z).dot(unitPrism))

patch = pymesh.merge_meshes(meshes)
backPatch = AffineMatrix().rotateY(math.pi).dot(patch)

out = pymesh.merge_meshes([cup, patch, backPatch])

save_mesh_verbose('working/m.stl', out)
