import json
import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import save_mesh_verbose
from common.linearMap import linearMap

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


def cupMap(theta, y):
    band = getBand(y)
    radius = profile[band] + radiusAdjust
    return [radius * math.cos(theta), y, radius * math.sin(theta)]


yMid = 0.5 * (yMin + yMax)

meshes = [cup]

for n in range(10):

    yy = linearMap(n, 0, 10, yMin, yMax)

    x, y, z = cupMap(0, yy)
    newNib = AffineMatrix().translate(x, y, z).dot(nib)
    meshes.append(newNib)

    x, y, z = cupMap(0.5 * math.pi, yy)
    newNib = AffineMatrix().translate(x, y, z).dot(nib)
    meshes.append(newNib)

    x, y, z = cupMap(math.pi, yy)
    newNib = AffineMatrix().translate(x, y, z).dot(nib)
    meshes.append(newNib)

    x, y, z = cupMap(1.5 * math.pi, yy)
    newNib = AffineMatrix().translate(x, y, z).dot(nib)
    meshes.append(newNib)

out = pymesh.merge_meshes(meshes)

save_mesh_verbose('working/m.stl', out)
