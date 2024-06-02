import math
import pymesh

from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

rotationMatrix = AffineMatrix().rotateX(0.25 * math.pi)
translationMatrix = AffineMatrix().translate(0.5, 0, 0)

# 'bottom' denotes the origin (0,0,0) end of the prism 'top' the other end
# 'left' and 'right' are the two sides off the prism - their respective assignment 
# is arbitrary, so there's a 50% chance I've assigned them correctly ;-)

unitBox = pymesh.generate_box_mesh([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5])
maskTopRight = pymesh.generate_box_mesh([0, 0.5, -0.5], [1, 1.5, 0.5])
maskBottomRight = pymesh.generate_box_mesh([-1, 0.5, -0.5], [0, 1.5, 0.5])
maskTopLeft = pymesh.generate_box_mesh([0, -0.5, -1.5], [1, 0.5, -0.5])
maskBottomLeft = pymesh.generate_box_mesh([-1, -0.5, -1.5], [0, 0.5, -0.5])

unitBox = rotationMatrix.dot(unitBox)
maskTopRight = rotationMatrix.dot(maskTopRight)
maskBottomRight = rotationMatrix.dot(maskBottomRight)
maskTopLeft = rotationMatrix.dot(maskTopLeft)
maskBottomLeft = rotationMatrix.dot(maskBottomLeft)

remove = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

difference = pymesh.boolean(unitBox, remove, 'difference')

prism = translationMatrix.dot(difference)
maskTopRight = translationMatrix.dot(maskTopRight)
maskBottomRight = translationMatrix.dot(maskBottomRight)
maskTopLeft = translationMatrix.dot(maskTopLeft)
maskBottomLeft = translationMatrix.dot(maskBottomLeft)

unitVector = pymesh.generate_box_mesh([0, -0.1, -0.1], [1, 0.1, 0.1])
prism = pymesh.boolean(prism, unitVector, 'union')

print(prism.bbox)

coneHeight = prism.bbox[1][1]
cone = pymesh.generate_cylinder([0, 0, 0], [0, coneHeight, 0], coneHeight, 0, num_segments=32)

save_mesh_verbose('working/prism.stl', prism)
save_mesh_verbose('working/maskTopRight.stl', maskTopRight)
save_mesh_verbose('working/maskBottomRight.stl', maskBottomRight)
save_mesh_verbose('working/maskTopLeft.stl', maskTopLeft)
save_mesh_verbose('working/maskBottomLeft.stl', maskBottomLeft)
save_mesh_verbose('working/cone.stl', cone)
