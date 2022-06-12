from VAFpackage import ALLOWED_LAND_USAGE_MAP, RegionList, GrdMap,MAIN_DATA_DIRPATH
import matplotlib.pyplot as plt
import numpy as np

map=GrdMap().read_map_from_file(filepath = MAIN_DATA_DIRPATH / 'grdInputSourceNew' / 'KATZ_253.grd', height_to_reduce=0)
val,count,percent = map.get_map_unique_values_count(list_of_excluded_values=[])
print(val,count,percent)
val,count,percent = map.get_map_unique_values_count(list_of_excluded_values=[0])
print(val,count,percent)