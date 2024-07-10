import pymesh
from common.helpers import save_mesh_verbose

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')

box = pymesh.generate_box_mesh([-100, -100, -100], [100, 100, 20])

out = pymesh.boolean(cup, box, 'difference')

save_mesh_verbose('working/partialCup.stl', out)
