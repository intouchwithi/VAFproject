from VAFpackage.Utilities import GrdMap
from VAFpackage.Utilities.MainMaps import ALLOWED_LAND_USAGE_MAP
import numpy as np
import numpy.ma as ma

__all__ = ('FloodingFrequencyMap',)


class FloodingFrequencyMap(GrdMap):

    def __init__(self, *, list_of_qt, list_of_maps=None):
        GrdMap.__init__(self)

        binary_land_usage_map = np.where(ALLOWED_LAND_USAGE_MAP.cells > 0, 0, 1)
        n = len(list_of_qt)

        for (q, t) in list_of_qt:
            current_map = GrdMap().read_similar_map_from_library(q=q, t=t)
            current_map.cells = np.where(current_map.cells > 0, 1, 0)
            self._cells = self._cells + current_map.cells

        if list_of_maps is not None:
            n += len(list_of_maps)
            for flooding_map in list_of_maps:
                current_map_cells = np.where(flooding_map.cells > 0, 1, 0)
                self._cells = self._cells + current_map_cells

        self._cells = np.divide(self._cells, n)
        self._cells = ma.masked_array(self._cells, mask=binary_land_usage_map)
        self._cells = self._cells.filled(-1)

        self._maxZ = np.max(self._cells)
        self._minZ = np.min(self._cells)

        print("Flooding frequency map created")

    def create_region_flooding_frequency_map(self, region_boundaries):
        """region_boundaries is an array of tuples - each tuple is left (included) and right (not included)
        boundaries of segment"""

        result_map = GrdMap()
        result_map.cells += np.where(self._cells == -1, -1, 0)
        for index, region_boundary in enumerate(region_boundaries):
            if index == len(region_boundaries)-1:
                result_map.cells += np.where((self._cells >= region_boundary[0]) & (self._cells <= region_boundary[1]),
                                            index,
                                            0)
            else:
                result_map.cells += np.where((self._cells >= region_boundary[0]) & (self._cells < region_boundary[1]),
                                            index,
                                            0)

        return result_map
