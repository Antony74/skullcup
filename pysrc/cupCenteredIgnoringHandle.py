import pymesh
from common.AffineMatrix import AffineMatrix
from common.helpers import save_mesh_verbose

cup = pymesh.load_mesh('working/cup.stl')
cupWithoutHandle = pymesh.load_mesh('working/cupWithoutHandle.stl')
convexHull = pymesh.load_mesh('working/convexHull.stl')

xmin = cupWithoutHandle.bbox[0][0]
xmax = cupWithoutHandle.bbox[1][0]

adjustment = -0.5 * (xmax + xmin)

cupCenteredIgnoringHandle = AffineMatrix().translate(adjustment, 0, 0).dot(cup)

save_mesh_verbose('working/cupCenteredIgnoringHandle.stl',
                  cupCenteredIgnoringHandle)

convexHullCenteredIgnoringHandle = AffineMatrix().translate(adjustment, 0, 0).dot(convexHull)

save_mesh_verbose('working/convexHullCenteredIgnoringHandle.stl',
                  convexHullCenteredIgnoringHandle)
