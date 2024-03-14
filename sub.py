import sys
import pymesh
from helpers import save_mesh_verbose

if(len(sys.argv) != 4):
    print('Usage: python3 sub.py [output-difference].stl [minuend].stl [subtrahend].stl')
    exit(1)

minuend = pymesh.load_mesh(sys.argv[2])
subtrahend = pymesh.load_mesh(sys.argv[3])

difference = pymesh.boolean(minuend, subtrahend, 'difference')

save_mesh_verbose(sys.argv[1], difference)
