import pymesh
from common.helpers import save_mesh_verbose

out = pymesh.generate_box_mesh([-10, -10, -10], [10, 10, 10])

save_mesh_verbose('working/nib.stl', out)
