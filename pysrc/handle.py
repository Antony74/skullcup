import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

handle = pymesh.generate_box_mesh([-70, -20, -50], [-25, 50, 50])

handle = AffineMatrix().rotateZ(5, degrees=True).dot(handle)

save_mesh_verbose('working/handle.stl', handle)

