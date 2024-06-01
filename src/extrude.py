import sys
import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

scaleFactor = 1.05

if (len(sys.argv) != 3):
    print(
        'Usage: python3 src/extrude.py [output].stl [input].stl')
    exit(1)

mesh = pymesh.load_mesh(sys.argv[2])

out = AffineMatrix().scale(scaleFactor, 1, scaleFactor).dot(mesh)

save_mesh_verbose(sys.argv[1], out)
