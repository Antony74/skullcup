import FreeCAD
import Mesh

mesh = Mesh.Mesh('root/mcup.stl')

mesh.removeDuplicatedFacets()

mesh.write('root/mcup-fixed.stl')



