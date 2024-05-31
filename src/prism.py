import math
import pymesh

from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

unitBox = pymesh.generate_box_mesh([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5])

unitBox = AffineMatrix().rotateX(0.25 * math.pi).dot(unitBox)

remove = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

out = pymesh.boolean(unitBox, remove, 'difference')

save_mesh_verbose('working/prism.stl', out)