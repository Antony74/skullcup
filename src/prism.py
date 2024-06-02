import math
import pymesh

from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

rotationMatrix = AffineMatrix().rotateX(0.25 * math.pi)
translationMatrix = AffineMatrix().translate(0.5, 0, 0)

unitBox = pymesh.generate_box_mesh([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5])
unitBox = rotationMatrix.dot(unitBox)

remove = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

difference = pymesh.boolean(unitBox, remove, 'difference')

prism = translationMatrix.dot(difference)

coneHeight = prism.bbox[1][1]
cone = pymesh.generate_cylinder([0, 0, 0], [0, coneHeight, 0], coneHeight, 0, num_segments=32)

save_mesh_verbose('working/prism.stl', prism)
save_mesh_verbose('working/cone.stl', cone)
