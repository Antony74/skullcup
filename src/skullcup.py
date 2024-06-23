import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

skullcup = pymesh.load_mesh('working/skullWithCup.stl')

# Make it 100 units tall, which is great for interpreting as millimeters (mm)
scale = 100 / (skullcup.bbox[1][1] - skullcup.bbox[0][1])

skullcup = AffineMatrix().scale(scale).dot(skullcup)    

save_mesh_verbose('working/skullcupUnfixed.stl', skullcup)
