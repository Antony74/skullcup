import math
import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose
from fix_mesh.fix_mesh import fix_mesh

m = pymesh.load_mesh('working/mWithSurface.stl')
cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')

backM = AffineMatrix().rotateY(math.pi).dot(m)

mCup = pymesh.boolean(m, cup, 'union')
out = pymesh.boolean(backM, mCup, 'union')

# Make it 100 units tall, which is great for interpreting as millimeters (mm)
scale = 100 / (out.bbox[1][1] - out.bbox[0][1])

out = AffineMatrix().scale(scale).dot(out)

out = fix_mesh(out)

save_mesh_verbose('mcup.stl', out)

