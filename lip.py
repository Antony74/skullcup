import pymesh
from helpers import save_mesh_verbose

lip = pymesh.generate_box_mesh([-70, 35, -70], [70, 50, 70])

save_mesh_verbose(lip, 'working/lip.py')
