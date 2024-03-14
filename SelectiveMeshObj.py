import pymesh
from MeshObj import MeshObj
from helpers import mesh_info


class SelectiveMeshObj(MeshObj):

    def __init__(self, name, mesh):
        super().__init__(name, mesh)

    @staticmethod
    def create(name, mesh):
        return SelectiveMeshObj(name, mesh)

    def __sub__(self, other):
        result = super().__sub__(other)

        if result.name == '(convex_hull((cup - handle) - lip) - cup)':
            sep = pymesh.separate_mesh(result.mesh())
            result = self.create(result.name, sep[1])
            filename = '/skullcup/working/SelectiveMeshObj(' + \
                result.name + ').stl'
            print(filename)
            mesh_info(result.mesh())
            pymesh.save_mesh(
                filename, result.mesh())

        return result
