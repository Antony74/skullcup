import pymesh
from common.helpers import save_mesh_verbose

radius = 3

out = pymesh.generate_box_mesh([-radius, -radius, -radius], [radius, radius, radius])

save_mesh_verbose('working/nib.stl', out)
