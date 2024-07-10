import sys
import pymesh
from common.helpers import save_mesh_verbose

if (len(sys.argv) != 4):
    print(
        'Usage: python3 pysrc/difference.py [output-difference].stl [in1].stl [in2].stl')
    exit(1)

print(sys.argv[1].split('/').pop() + ' = ' +
      sys.argv[2].split('/').pop() + ' - ' + sys.argv[3].split('/').pop())

in1 = pymesh.load_mesh(sys.argv[2])
in2 = pymesh.load_mesh(sys.argv[3])

difference = pymesh.boolean(in1, in2, 'difference')

save_mesh_verbose(sys.argv[1], difference)
