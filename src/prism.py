import math
import numpy as np
import pymesh

from common.linearMap import linearMap
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

rotationMatrix = AffineMatrix().rotateX(0.25 * math.pi)
translationMatrix = AffineMatrix().translate(0.5, 0, 0)

unitBox = pymesh.generate_box_mesh([-0.5, -0.5, -0.5], [0.5, 0.5, 0.5])
unitBox = rotationMatrix.dot(unitBox)

remove = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

difference = pymesh.boolean(unitBox, remove, 'difference', engine='cgal')

prism = translationMatrix.dot(difference)

print('remove_duplicated_vertices')
prism, __ = pymesh.remove_duplicated_vertices(prism)

print('remove_degenerated_triangles')
prism, __ = pymesh.remove_degenerated_triangles(prism, 100)

save_mesh_verbose('working/prism.stl', prism)

# Cone


def generateCone(baseX, baseY, baseZ, height, radius, num_segments):
    base = np.array([baseX, baseY, baseZ])
    apex = np.array([baseX, baseY + height, baseZ])

    angles = np.linspace(0, 2 * np.pi, num_segments, endpoint=False)
    
    base_vertices = np.array([[baseX + (radius * np.cos(angle)), baseY, baseZ + (radius * np.sin(angle))] for angle in angles])
    vertices = np.vstack([apex, base_vertices])
    vertices = np.vstack([vertices, base])

    faces = np.array([[i + 1, 0, (i + 1) % num_segments + 1] for i in range(num_segments)])
    base_faces = np.array([[i + 1, (i + 1) % num_segments + 1, num_segments + 1] for i in range(num_segments)])
    faces = np.vstack([faces, base_faces])

    return pymesh.form_mesh(vertices, faces)


coneHeight = prism.bbox[1][1]
coneBase = -0.1
coneRadius = linearMap(coneBase, 0, coneHeight, coneHeight, 0)

cone = generateCone(0, coneBase, 0, coneHeight + 0.1, coneRadius, 32)

save_mesh_verbose('working/cone.stl', cone)
