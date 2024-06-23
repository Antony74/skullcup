import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

# https://cults3d.com/en/3d-model/home/coffee-cup
cupMesh = pymesh.load_mesh('Coffee_Cup.A.1.stl')

cupMesh = AffineMatrix().rotateY(180, degrees=True).dot(cupMesh)

save_mesh_verbose('working/cup.stl', cupMesh)
