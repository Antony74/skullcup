import json
import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import save_mesh_verbose
from common.linearMap import linearMap

radiusAdjust = 5
prismThickness = 5

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


def cartesianToSpherical(x, y, z):
    XsqPlusYsq = x**2 + y**2
    r = math.sqrt(XsqPlusYsq + z**2)                  # r
    elevation = math.acos(z / r)                      # theta
    azimuth = math.atan2(y, x)                        # phi
    return r, elevation, azimuth


meshes = []

points = list(map(lambda pt: patchMap(pt).dot([1, 0, 0]),
                  [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]))

elevationCorrection = [1, -1, 1, -1]

for index in range(0, len(points) - 1):
    start = points[index]
    end = points[index + 1]
    vector = start - end

    r, elevation, azimuth = cartesianToSpherical(
        vector[0],
        vector[1],
        vector[2])

    elevation -= 0.5 * math.pi

    meshes.append(AffineMatrix()
                  .scale(r, prismThickness, prismThickness)
                  .rotateX(0.5 * math.pi)
                  .rotateZ(azimuth + math.pi)
                  .rotateX(elevation * elevationCorrection[index])
                  .translate(start[0], start[1], start[2])
                  .dot(unitPrism))

patch = pymesh.merge_meshes(meshes)
backPatch = AffineMatrix().rotateY(math.pi).dot(patch)

out = pymesh.merge_meshes([cup, patch, backPatch])

save_mesh_verbose('working/m.stl', out)
