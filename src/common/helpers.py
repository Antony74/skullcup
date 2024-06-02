import time
from datetime import timedelta
import numpy as np
import pymesh
from fix_mesh.fix_mesh import fix_mesh


def load_fixed_mesh(originalFilename):
    print('Loading ' + originalFilename)
    mesh = pymesh.load_mesh(originalFilename)
    mesh_info(mesh)
    print('Fixing ' + originalFilename)
    mesh = fix_mesh(mesh)
    return mesh


def mesh_info(mesh):
    print('vertices ' + str(len(mesh.vertices)) +
          ', faces ' + str(len(mesh.faces)))


start_time = time.monotonic()


def save_mesh_verbose(filename, mesh):
    print('Saving ' + filename)
    mesh_info(mesh)
    pymesh.save_mesh(filename, mesh)
    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))


def createEmptyMesh():
    return pymesh.form_mesh(np.empty([0, 3]), np.empty([0, 3]), np.empty([0, 3]))
