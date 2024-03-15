import sys
import pymesh
from common.helpers import save_mesh_verbose

if(len(sys.argv) != 3):
    print('Usage: python3 convexHull.py [output-convex-hull].stl [input-mesh].stl')
    exit(1)

print(sys.argv[1].split('/').pop() + ' = convex_hull(' + sys.argv[2].split('/').pop() + ')')

mesh = pymesh.load_mesh(sys.argv[2])

convexHull = pymesh.convex_hull(mesh)

save_mesh_verbose(sys.argv[1], convexHull)
