import copy
from VAFpackage.Utilities import GrdMap
from VAFpackage.Utilities.MainMaps import ALLOWED_LAND_USAGE_MAP
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
__all__ = ('FunctionalStructure',)


class FunctionalStructure(GrdMap):
    def __init__(self, dict_with_types):
        """Input parameter - dictionary where
        keys - functional type names,
        values - lists with allowed types"""
        GrdMap.__init__(self)
        self._legend = {(idx+1): k for idx, (k, v) in enumerate(dict_with_types.items())}

        binary_land_usage_map = np.where(ALLOWED_LAND_USAGE_MAP.cells > 0, 0, 1)
        self.cells = ma.masked_array(self.cells, mask=binary_land_usage_map)
        self.cells = self.cells.filled(-1)

        for idx, legend_name in self._legend.items():
            self.cells = np.where(np.isin(ALLOWED_LAND_USAGE_MAP.cells, dict_with_types[legend_name]), idx, self._cells)

        print(f"Functional structure map created. Map legend {self._legend}")

    @property
    def legend(self):
        return self._legend

    def get_relative_area_plot(self):
        values, count, percents = self.get_map_unique_values_count(list_of_excluded_values=[0, -1])
        figure = plt.figure(figsize=(20, 7))
        plt.bar([self.legend[value] for value in values], [percent / 100.0 for percent in percents])
        plt.ylabel('Относительная площадь')
        return figure









