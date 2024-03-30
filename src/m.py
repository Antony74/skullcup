import json
import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.bandedMap import createBandedMap
from common.helpers import save_mesh_verbose
from common.linearMap import linearMap

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')
nib = pymesh.load_mesh('working/nib.stl')

with open('working/profile.json') as f:
    profile = json.load(f)

bands = profile['bands']
yMin = profile['yMin']
yMax = profile['yMax']

getBand, fromBand = createBandedMap(bands, yMin, yMax)


def cupMap(theta, y):
    radius = getBand(y)
    return [radius * math.cos(theta), y, radius * math.sin(theta)]


yMid = 0.5 * (yMin + yMax)

x, y, z = cupMap(0, yMid)
nib1 = AffineMatrix().translate(x, y, z).dot(nib)

x, y, z = cupMap(0.5 * math.pi, yMid)
nib2 = AffineMatrix().translate(x, y, z).dot(nib)

x, y, z = cupMap(math.pi, yMid)
nib3 = AffineMatrix().translate(x, y, z).dot(nib)

x, y, z = cupMap(1.5 * math.pi, yMid)
nib4 = AffineMatrix().translate(x, y, z).dot(nib)

out = pymesh.merge_meshes([cup, nib1, nib2, nib3, nib4])

save_mesh_verbose('working/m.stl', out)
