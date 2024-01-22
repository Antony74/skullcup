# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from scipy.spatial.transform import Rotation


def transformMesh(mesh, fn):
    return pymesh.form_mesh([fn(v) for v in mesh.vertices], mesh.faces)


scale = 0.75

initialCup = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
initialSkull = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()

skullRotationMatrix = Rotation.from_euler(
    'xy', [-90, 90], degrees=True).as_matrix()

# cupBox = pymesh.generate_box_mesh(initialCup.bbox[0], initialCup.bbox[1])
# skullBox = pymesh.generate_box_mesh(initialSkull.bbox[0], initialSkull.bbox[1])

cup = transformMesh(initialCup, lambda v: cupRotationMatrix.dot(v))

skull = transformMesh(initialSkull, lambda v: scale * skullRotationMatrix.dot(v))

yAdjustment = cup.bbox[0][1] - skull.bbox[0][1]

skull = transformMesh(skull, lambda v: v + [0, yAdjustment, 0])

# skullcup = pymesh.convex_hull(cup)
# skullcup = pymesh.boolean(cup, skull, 'union', 'cork')
skullcup = pymesh.merge_meshes([cup, skull])

pymesh.save_mesh('/working/skullcup.stl', skullcup)
