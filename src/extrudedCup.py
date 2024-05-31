import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

scaleFactor = 1.05

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')

out = AffineMatrix().scale(scaleFactor, 1, scaleFactor).dot(cup)

save_mesh_verbose('working/extrudedCup.stl', out)
