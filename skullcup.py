# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from scipy.spatial.transform import Rotation

scale = 0.75

initialCup = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
initialSkull = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()

skullRotationMatrix = Rotation.from_euler(
    'xy', [-90, 90], degrees=True).as_matrix()

# cupBox = pymesh.generate_box_mesh(initialCup.bbox[0], initialCup.bbox[1])
# skullBox = pymesh.generate_box_mesh(initialSkull.bbox[0], initialSkull.bbox[1])


def transformCupVertex(v):
    # rotate
    v = cupRotationMatrix.dot(v)

    return v


def transformSkullVertex(v):
    # rotate
    v = skullRotationMatrix.dot(v)

    # scale
    v *= scale

    return v


def translateSkullVertex(v):
    # translate
    v = v + [0, yAdjustment, 0]

    return v


cup = pymesh.form_mesh([transformCupVertex(v)
                        for v in initialCup.vertices], initialCup.faces)

skull = pymesh.form_mesh([transformSkullVertex(v)
                         for v in initialSkull.vertices], initialSkull.faces)

yAdjustment = cup.bbox[0][1] - skull.bbox[0][1]

skull = pymesh.form_mesh([translateSkullVertex(v)
                         for v in skull.vertices], skull.faces)

# skullcup = pymesh.convex_hull(cup)
# skullcup = pymesh.boolean(cup, skull, 'union', 'cork')
skullcup = pymesh.merge_meshes([cup, skull])

pymesh.save_mesh('/working/skullcup.stl', skullcup)
