import pymesh

class MeshObj:

    def __init__(self, name, mesh):
        self.name = name
        self._mesh = mesh

    @staticmethod
    def create(name, mesh):
        return MeshObj(name, mesh)

    def mesh(self):
        return self._mesh

    def __add__(self, other):
        name = self.name + ' + ' + other.name
        print(name)
        result = self.create('(' + name + ')', pymesh.boolean(self._mesh, other._mesh, 'union'))
        pymesh.save_mesh('/skullcup/working/' + name + '.stl', result.mesh())
        return result

    def __sub__(self, other):
        name = self.name + ' - ' + other.name
        print(name)
        result = self.create('(' + name + ')', pymesh.boolean(self._mesh, other._mesh, 'difference'))
        pymesh.save_mesh('/skullcup/working/' + name + '.stl', result.mesh())
        return result
