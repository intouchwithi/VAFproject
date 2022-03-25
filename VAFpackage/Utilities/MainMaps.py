from .GrdMap import GrdMap
from.MainDirectories import ALLOWED_LAND_USAGE_FILEPATH

__all__ = ('ALLOWED_LAND_USAGE_MAP',)

"""grd map with allowed types of use"""
ALLOWED_LAND_USAGE_MAP = GrdMap().read_map_from_file(filepath=ALLOWED_LAND_USAGE_FILEPATH)
