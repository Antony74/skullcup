import json
import math
from common.coordinates import cartesianToSpherical
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import createEmptyMesh, save_mesh_verbose
from common.linearMap import linearMap

radiusAdjust = -2
prismThickness = 7
prismHeight = 25

unitPrism = pymesh.load_mesh('working/prism.stl')
unitCone = pymesh.load_mesh('working/cone.stl')

with open('working/profile.json') as f:
    profile = json.load(f)

bands = profile['bands']
yMin = profile['yMin']
yMax = profile['yMax']
profile = profile['profile']

getBand = createBandedMap(bands, yMin, yMax)

patchRadius = 0.12
patchXMid = -0.5
patchXMin = patchXMid - patchRadius
patchXMax = patchXMid + patchRadius
patchYMin = linearMap(0.35, 0, 1, yMin, yMax)
patchYMax = linearMap(0.75, 0, 1, yMin, yMax)


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

def getVectorMappingMatrix(r, theta, phi, start):
    return (AffineMatrix()
              .scale(r, prismHeight, prismThickness)
              .rotateX(cupCorrection[index] * math.pi)
              .rotateY(theta)
              .rotateZ(phi + math.pi)
              .translate(start[0], start[1], start[2]))

meshes = []

points = list(map(lambda pt: patchMap(pt).dot([1, 0, 0]),
                  [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]))

cupCorrection = [0.35, 0.5, 0.5, 0.35]

for index in range(0, len(points) - 1):
    start = points[index]
    end = points[index + 1]
    vector = start - end

    r, theta, phi = cartesianToSpherical(
        vector[0],
        vector[1],
        vector[2])

    mesh = getVectorMappingMatrix(r, theta, phi, start).dot(unitPrism)

    cone = getVectorMappingMatrix(prismThickness, theta, phi, start).dot(unitCone)
    mesh = pymesh.boolean(mesh, cone, 'union')

    endCone = AffineMatrix().translate(-vector[0], -vector[1], -vector[2]).dot(cone)
    mesh = pymesh.boolean(mesh, endCone, 'union')

    meshes.append(mesh)

out = createEmptyMesh()

for index in range(len(meshes)):
    mesh = meshes[index]
    out = pymesh.boolean(out, mesh, 'union')

save_mesh_verbose('working/m.stl', out)
