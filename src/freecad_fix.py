import FreeCAD
import Mesh

mesh = Mesh.Mesh('root/mcup.stl')

# print('Orientation - harmonizeNormals')
# mesh.harmonizeNormals()

# print('Duplicated faces - removeDuplicatedFacets')
# mesh.removeDuplicatedFacets()

# print('Duplicated points - removeDuplicatedPoints')
# mesh.removeDuplicatedPoints()

# print('Degenerated faces - fixDegenerations')
# mesh.fixDegenerations()

# print('Face indices - fixIndices')
# mesh.fixIndices()

# for i in range(5):
#     print('Non-manifolds - removeNonManifolds')
#     mesh.removeNonManifolds()

print('Self-intersections - removeSelfIntersections')
mesh.fixSelfIntersections()

# print('fillupHoles')
# mesh.fillupHoles(100)

mesh.write('root/mcup-fixed.stl')



