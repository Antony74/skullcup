# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh
from scipy.spatial.transform import Rotation

cup = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
skull = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

rotation = Rotation.from_euler('x', 45, degrees=True).as_matrix()

newCup = pymesh.form_mesh([rotation.dot(v) for v in cup.vertices], cup.faces)

# skullcup = pymesh.convex_hull(cup)
# skullcup = pymesh.boolean(cup, skull, 'union', 'cork')
skullcup = pymesh.merge_meshes([newCup, skull])

pymesh.save_mesh('/working/skullcup.stl', skullcup)
