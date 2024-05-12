import json
import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import save_mesh_verbose
from common.linearMap import linearMap, linearMap2D, segmentedMap

radiusAdjust = 2

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')
nib = pymesh.load_mesh('working/nib.stl')

with open('working/profile.json') as f:
    profile = json.load(f)

bands = profile['bands']
yMin = profile['yMin']
yMax = profile['yMax']
profile = profile['profile']

getBand, fromBand = createBandedMap(bands, yMin, yMax)

patchMin = linearMap(0.25, 0, 1, yMin, yMax)
patchMax = linearMap(0.75, 0, 1, yMin, yMax)


def cupMap(theta, y):
    band = getBand(y)
    radius = profile[band] + radiusAdjust
    return AffineMatrix().translate(radius * math.cos(0), y, radius * math.sin(0)).rotateY(theta)

# 'patch' refers to the patch of the cup where we want the design,
# and the patchMap function maps to it from the unit square.


def patchMap(x, y):
    return cupMap(linearMap(x, 0, 1, -0.25 * math.pi, 0.25 * math.pi), linearMap(y, 0, 1, patchMin, patchMax))


meshes = [cup]

steps = 40

for step in range(0, steps + 1):
    step = linearMap(step, 0, steps, 0, 4)
    position = segmentedMap(
        step,
        [0, 1, 2, 3, 4],
        [[0, 0], [0, 1], [0.5, 0], [1, 1], [1, 0]],
        [linearMap2D] * 5,
    )

    newNib = patchMap(position[0], position[1]).dot(nib)
    meshes.append(newNib)

out = pymesh.merge_meshes(meshes)

save_mesh_verbose('working/m.stl', out)
