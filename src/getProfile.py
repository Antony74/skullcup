import sys
import json
import pymesh
from common.linearMap import linearMap

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')

bands = 100

yMin = cup.bbox[0][1]
yMax = cup.bbox[1][1]

profile = [-sys.maxsize] * (bands + 1)


def getBand(y):
    return int(round(linearMap(y, yMin, yMax, -0.5, bands + 0.5)))


def getY(band):
    return linearMap(band, -0.5, bands + 0.5, yMin, yMax)


for [x, y, z] in cup.vertices:
    band = getBand(y)
    profile[band] = max(z, profile[band])


with open('working/profile.json', 'w', encoding='utf-8') as f:
    json.dump({'bands': bands, 'yMin': yMin, 'yMax': yMax,
              'profile': profile}, f, ensure_ascii=False, indent=4)
