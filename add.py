import sys
import pymesh
from helpers import save_mesh_verbose

if(len(sys.argv) != 4):
    print('Usage: python3 add.py [output-mesh].stl [in1].stl [in2].stl')
    exit(1)

in1 = pymesh.load_mesh(sys.argv[2])
in2 = pymesh.load_mesh(sys.argv[3])

mesh = pymesh.boolean(in1, in2, 'union')

save_mesh_verbose(sys.argv[1], mesh)
