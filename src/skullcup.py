import pymesh
from fix_mesh.fix_mesh import fix_mesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

skullcup = pymesh.load_mesh('working/skullWithCup.stl')

# Make it 100 units tall, which is great for interpreting as millimeters (mm)
scale = 100 / (skullcup.bbox[1][1] - skullcup.bbox[0][1])

skullcup = AffineMatrix().scale(scale).dot(skullcup)

skullcup = fix_mesh(skullcup)

save_mesh_verbose('skullcup.stl', skullcup)
