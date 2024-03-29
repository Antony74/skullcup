import pymesh
from common.helpers import save_mesh_verbose

cup = pymesh.load_mesh('working/cupCenteredIgnoringHandle.stl')
nib = pymesh.load_mesh('working/nib.stl')

out = pymesh.boolean(cup, nib, 'union')

save_mesh_verbose('working/m.stl', out)
