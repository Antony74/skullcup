import math
from common.linearMap import linearMap
import pymesh

from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

rotationMatrix = AffineMatrix().rotateX(0.25 * math.pi)
translationMatrix = AffineMatrix().translate(0.5, 0, 0)

unitBox = pymesh.generate_box_mesh([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5])
unitBox = rotationMatrix.dot(unitBox)

remove = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

difference = pymesh.boolean(unitBox, remove, 'difference', engine='cgal')

prism = translationMatrix.dot(difference)

coneHeight = prism.bbox[1][1]
coneBase = -0.1
coneRadius = linearMap(coneBase, 0, coneHeight, coneHeight, 0)
cone = pymesh.generate_cylinder([0, coneBase, 0], [0, coneHeight, 0], coneRadius, 0.1 * coneRadius, num_segments=32)

print('remove_duplicated_vertices')
prism, __ = pymesh.remove_duplicated_vertices(prism)

print('remove_degenerated_triangles')
prism, __ = pymesh.remove_degenerated_triangles(prism, 100)

save_mesh_verbose('working/prism.stl', prism)
save_mesh_verbose('working/cone.stl', cone)
