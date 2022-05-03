from VAFpackage import ALLOWED_LAND_USAGE_MAP, RegionList, GrdMap
import numpy as np


map = GrdMap()
map.cells = np.where(ALLOWED_LAND_USAGE_MAP.cells == 8888, 1, 0)
r = RegionList(map,10)
print(r.regions[1].points)