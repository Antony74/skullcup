import numpy as np
from scipy.spatial.transform import Rotation
import pymesh
from copy import deepcopy


class AffineMatrix:

    def __init__(self, matrix44=np.identity(4)):
        self.m44 = deepcopy(matrix44)
        self.m33 = matrix44[:3, :3]
        self.translation = matrix44[3, :3]

    def print(self):
        print(self.m44)
        print(self.m33)
        print(self.translation)

    def dot(self, operand):
        if hasattr(operand, 'vertices'):
            # Perform affine transformation on mesh
            return pymesh.form_mesh([self.m33.dot(v) + self.translation for v in operand.vertices], operand.faces)
        else:
            # Perform affine transformation on vector
            return self.m33.dot(operand) + self.translation

    def translate(self, x, y, z):
        matrix = deepcopy(self.matrix)
        matrix[0][3] += x
        matrix[1][3] += y
        matrix[2][3] += z
        return AffineMatrix(matrix)

    def rotate(self, seq, angles, degrees=False):
        rotationMatrix = np.identity(4)
        rotationMatrix[:3, :3] = Rotation.from_euler(seq, angles, degrees).as_matrix()
        return AffineMatrix(self.m44 * rotationMatrix)

    def rotateX(self, angle, degrees=False):
        return self.rotate('x', angle, degrees)

    def rotateY(self, angle, degrees=False):
        return self.rotate('y', angle, degrees)

    def rotateZ(self, angle, degrees=False):
        return self.rotate('z', angle, degrees)

    def scale(self, x, y=None, z=None):
        if z == None:
            y = x
            z = x

        return AffineMatrix(self.m44 * [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])

    def scaleX(self, x):
        return self.scale(x, 1, 1)

    def scaleY(self, y):
        return self.scale(1, y, 1)

    def scaleX(self, z):
        return self.scale(1, 1, z)
