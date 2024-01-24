# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from scipy.spatial.transform import Rotation


def transformMesh(mesh, fn):
    return pymesh.form_mesh([fn(v) for v in mesh.vertices], mesh.faces)


scale = 0.6

cup = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
skull = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()
handleBoxRotationMatrix = Rotation.from_euler('z', 5, degrees=True).as_matrix()

skullRotationMatrix = Rotation.from_euler(
    'xy', [-90, 90], degrees=True).as_matrix()

# We want a box containing the handle, and a tiny sliver of cup just so we can
# be certain we're not missing any of the handle.  Any amount of cup that doesn't
# cut through to the cup's interior will be fine.
handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = transformMesh(handle, lambda v: handleBoxRotationMatrix.dot(v))

cup = transformMesh(cup, lambda v: cupRotationMatrix.dot(v))

cupWithoutHandle = pymesh.boolean(cup, handle, 'difference', 'cork')

skull = transformMesh(skull, lambda v: scale *
                      skullRotationMatrix.dot(v))

cupCenterX = (cupWithoutHandle.bbox[0][0] + cupWithoutHandle.bbox[1][0]) / 2
skullCenterX = (skull.bbox[0][0] + skull.bbox[1][0]) / 2
xAdjustment = cupCenterX - skullCenterX
yAdjustment = cup.bbox[0][1] - skull.bbox[0][1]

skull = transformMesh(skull, lambda v: v + [xAdjustment, yAdjustment, 10])

# skullcup = pymesh.convex_hull(cup)
# skullcup = pymesh.boolean(cup, skull, 'union', 'cork')
skullcup = pymesh.merge_meshes([cup, skull])

pymesh.save_mesh('/working/skullcup.stl', skullcup)
