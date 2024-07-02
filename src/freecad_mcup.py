import FreeCAD
import Mesh
import OpenSCADUtils

mesh0 = Mesh.Mesh('root/working/m0.stl')
mesh1 = Mesh.Mesh('root/working/m1.stl')

mesh = OpenSCADUtils.meshoptempfile('union', (mesh0, mesh1))

mesh.write('root/mcup.stl')
