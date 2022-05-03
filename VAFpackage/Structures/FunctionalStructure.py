import copy
import numpy as np
from .CriteriaFuncs import f1, f2, f3, f4
__all__ = ('FunctionalStructure',)


class TypeGroup:
    def __init__(self, type_group_name, list_of_types, ecol_func, econ_func, soc_func):
        self.type_group_name = type_group_name
        self.list_of_types = list_of_types
        self.ecol_func = ecol_func
        self.econ_func = econ_func
        self.soc_func = soc_func

    def calculate_relative_area(self, map_with_types):
        binary_map_with_types = np.where(map_with_types.cells > 0, 1, 0)
        unique_values, counts = np.unique(binary_map_with_types, return_counts=True)

        binary_map_with_types2 = np.where(np.isin(map_with_types.cells, self.list_of_types), 1, 0)
        unique_values2, counts2 = np.unique(binary_map_with_types2, return_counts=True)

        return counts2[1] / counts[1]


class FunctionalStructure:
    def __init__(self, map_with_types):
        self.map_with_types = copy.deepcopy(map_with_types)
        self.list_of_ecol_groups = []
        self.list_of_econ_groups = []
        self.list_of_soc_groups = []

        self.list_of_ecol_groups.append(TypeGroup('vodno_bolontye_ugodia',
                                             [187, 189, 219, 220, 31, 214],
                                             soc_func=lambda freq: 1 * f1(freq),
                                             ecol_func=f1,
                                             econ_func=lambda freq: 1 * f1(freq)
                                             ))
        self.list_of_ecol_groups.append(TypeGroup('lesa',
                                             [215, 216],
                                             soc_func=lambda freq: 1 * f2(freq),
                                             ecol_func=f2,
                                             econ_func=lambda freq: 1 * f2(freq)
                                             ))
        self.list_of_soc_groups.append(TypeGroup('recreazionnye_zony',
                                             [195, 200, 203, 205, 207],
                                             soc_func=f2,
                                             ecol_func=lambda freq: 0,
                                             econ_func=lambda freq: 0
                                             ))
        self.list_of_soc_groups.append(TypeGroup('zhilye_zony',
                                             [58, 61, 63, 87, 66, 171],
                                             soc_func=f3,
                                             ecol_func=lambda freq: 0,
                                             econ_func=lambda freq: 0
                                             ))
        self.list_of_econ_groups.append(TypeGroup('zalivnye_luga',
                                             [37, 39],
                                             soc_func=lambda freq: 1 * f1(freq),
                                             ecol_func=f1,
                                             econ_func=f1
                                             ))
        self.list_of_econ_groups.append(TypeGroup('hozyastvennye_zony_irrigated_agriculture',
                                             [12, 38, 43, 44, 45, 95, 132, 135, 150, 186, 224, 222, 221, 103],
                                             soc_func=lambda freq: 0,
                                             ecol_func=lambda freq: 0,
                                             econ_func=lambda freq: f4(freq)
                                             ))

    def define_typegroup(self, type_number):
        for typegroup in self.list_of_ecol_groups:
            if type_number in typegroup.list_of_types:
                return typegroup
        for typegroup in self.list_of_econ_groups:
            if type_number in typegroup.list_of_types:
                return typegroup
        for typegroup in self.list_of_soc_groups:
            if type_number in typegroup.list_of_types:
                return typegroup
        return None

    def calculate_relative_group_areas(self):
        group_rel_area = {}
        ecol_sum = 0
        econ_sum = 0
        soc_sum = 0
        for typegroup in self.list_of_ecol_groups:
            rel_area = typegroup.calculate_relative_area(self.map_with_types)
            group_rel_area[typegroup.type_group_name] = rel_area
            ecol_sum += rel_area
        for typegroup in self.list_of_econ_groups:
            rel_area = typegroup.calculate_relative_area(self.map_with_types)
            group_rel_area[typegroup.type_group_name] = rel_area
            econ_sum += rel_area
        for typegroup in self.list_of_soc_groups:
            rel_area = typegroup.calculate_relative_area(self.map_with_types)
            group_rel_area[typegroup.type_group_name] = rel_area
            soc_sum += rel_area

        biggroup_rel_area = {'ecol': ecol_sum, 'econ': econ_sum, 'soc': soc_sum}

        return group_rel_area, biggroup_rel_area




