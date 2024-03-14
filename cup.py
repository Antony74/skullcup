import pymesh
from AffineMatrix import AffineMatrix
from helpers import load_fixed_mesh, save_mesh_verbose

# https://cults3d.com/en/3d-model/home/coffee-cup
cupMesh = load_fixed_mesh('Coffee_Cup.A.1.stl')

cupMesh = AffineMatrix().rotateY(180, degrees=True).dot(cupMesh)

save_mesh_verbose('working/cup.stl', cupMesh)
