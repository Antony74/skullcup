from pathlib import Path
import pymesh
from fix_mesh.fix_mesh import fix_mesh

def load_fixed_mesh(originalFilename, fixedFilename):
    if (Path(fixedFilename).exists()):
        print('Loading ' + fixedFilename)
        mesh = pymesh.load_mesh(fixedFilename)
    else:
        print('Loading ' + originalFilename)
        mesh = pymesh.load_mesh(originalFilename)
        print('Fixing ' + originalFilename)
        mesh = fix_mesh(mesh)
        pymesh.save_mesh(fixedFilename, mesh)
    return mesh
