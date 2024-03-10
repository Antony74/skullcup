import pymesh
from MeshObj import MeshObj
from helpers import biggest_piece

class SinglePieceMeshObj(MeshObj):

    def __init__(self, name, mesh):
        super().__init__(name, mesh)

    @staticmethod
    def create(name, mesh):
        return SinglePieceMeshObj(name, mesh)

    def __sub__(self, other):
        result = super().__sub__(other)
        mesh = biggest_piece(result.mesh())
        result = self.create(result.name, mesh)
        pymesh.save_mesh('/skullcup/working/biggest_piece(' + result.name + ').stl', result.mesh())
        return result
