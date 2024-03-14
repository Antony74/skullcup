import pymesh
from AffineMatrix import AffineMatrix

handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = AffineMatrix().rotateZ(5, degrees=True).dot(handle)

pymesh.save_mesh('working/handle.stl', handle)

