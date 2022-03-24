import pandas as pd
from ..MainDirectories import RETROSPECTIVE_HYDROGRAPHS_FILEPATH
from scipy.optimize import curve_fit
import numpy as np

__all__ = ('VolumeToQTConverter',)


class VolumeToQTConverter:
    def __init__(self):
        data = pd.read_excel(RETROSPECTIVE_HYDROGRAPHS_FILEPATH)

        def func(x, a, b):
            return a * x + b

        popt, _ = curve_fit(func, data['t'], data['Q'])
        self._slope = popt[0]
        self._intercept = popt[1]

    @property
    def slope(self):
        return self._slope

    @property
    def intercept(self):
        return self._intercept

    def convert(self, volume):
        temp_t = int(np.round(
            (-self._slope + np.sqrt(np.power(self._slope, 2) + 4 * self._intercept * volume)) / (2 * self._intercept),
            0))
        temp_q = int(np.round(volume / temp_t, 0))
        return temp_q, temp_t
