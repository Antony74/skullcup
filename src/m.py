# usage:
# docker run -it -v .:/working pymesh/pymesh python3 /working/m.py

import pymesh
from scipy.spatial.transform import Rotation
from common.helpers import load_fixed_mesh, MeshObj, transformMesh


# https://cults3d.com/en/3d-model/home/coffee-cup
cupMesh = load_fixed_mesh(
    '/working/Coffee_Cup.A.1.stl', '/working/cup_fixed.stl')

print('Orientating cup')

cupRotationMatrix = Rotation.from_euler('y', 180, degrees=True).as_matrix()

cupMesh = transformMesh(cupMesh, lambda v: cupRotationMatrix.dot(v))

cup = MeshObj('cup', cupMesh)
