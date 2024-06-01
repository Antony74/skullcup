import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

m = pymesh.load_mesh('working/mWithSurface.stl')
cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')

backM = AffineMatrix().rotateY(math.pi).dot(m)

mCup = pymesh.boolean(m, cup, 'union')
out = pymesh.boolean(backM, mCup, 'union')

save_mesh_verbose('working/mcup.stl', out)

