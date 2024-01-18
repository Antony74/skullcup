# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/skullcup.py

import pymesh

cup = pymesh.load_mesh('/working/Coffee_Cup.A.1.stl')
skull = pymesh.load_mesh('/working/Scull_geant_fix02.stl')

# skullcup = pymesh.convex_hull(cup)
# skullcup = pymesh.boolean(cup, skull, 'union', 'cork')
skullcup = pymesh.merge_meshes([cup, skull])

pymesh.save_mesh('/working/skullcup.stl', skullcup)
