from ..MainConstants import Q_MIN, AKHTUBA_ENTRANCE_COORDS, RETROSPECTIVE_HYDROGRAPHS_TABLE
from ..GrdMap import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

__all__ = ('QAmendmentConverter',)

class QAmendmentConverter:
    def __init__(self):
        """water level decrease with every year"""
        def func(x, a, b):
            return a * x + b

        popt, _ = curve_fit(func, [1961, 1998], [1.3, 0])
        self._slope = popt[0]
        self._intercept = popt[1]

        def func(x, b, c, d):
            return b * x ** 2 + c * x + d

        """dependency function between h and Q"""
        q_list = []
        h_list = []

        for index, row in RETROSPECTIVE_HYDROGRAPHS_TABLE.iterrows():
            flooding_map = GrdMap().read_similar_map_from_library(q=row['Q'], t=row['t'])
            q_list.append(row['Q'])
            h_list.append(flooding_map[AKHTUBA_ENTRANCE_COORDS])

        self._popt, self._pcov = curve_fit(func, h_list, q_list)
        self._approximation_func = func

    def _calculate_delta_h(self, year):
        return year*self._slope+self._intercept

    def convert(self, year, q, t):
        flooding_map = GrdMap().read_similar_map_from_library(q=q, t=t)
        h = flooding_map[AKHTUBA_ENTRANCE_COORDS]
        new_h = h + self._calculate_delta_h(year)
        new_Q = self._approximation_func(new_h, *self._popt)
        if new_Q <= Q_MIN*1000:
            return Q_MIN*1000
        else:
            return int(np.round(new_Q, 0))