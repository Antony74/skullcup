import sys
import pymesh
from fix_mesh.fix_mesh import fix_mesh
from common.helpers import save_mesh_verbose

if (len(sys.argv) != 3):
    print(
        'Usage: python3 src/fix_mesh_cli.py [output-mesh].stl [input-mesh].stl')
    exit(1)

inputMesh = pymesh.load_mesh(sys.argv[2])

outputMesh = fix_mesh(inputMesh)

save_mesh_verbose(sys.argv[1], outputMesh)
