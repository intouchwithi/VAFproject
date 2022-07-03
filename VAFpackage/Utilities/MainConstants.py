import pandas as pd
from .MainDirectories import RETROSPECTIVE_HYDROGRAPHS_FILEPATH

__all__ = ('THRESHOLD1', 'THRESHOLD2', 'THRESHOLD3', 'Q_MAX', 'Q_MIN', 'T_MIN', 'T_MAX', 'DEFAULT_DECREASE_HEIGHT',
           'AKHTUBA_ENTRANCE_COORDS', 'RETROSPECTIVE_HYDROGRAPHS_TABLE', 'EPS', 'FS_7_TYPES', 'FS_4_TYPES')

""""threshold value for stable flooding"""
THRESHOLD1 = 0.85

""""threshold value for unstable flooding - 2 stage (currently is not used)"""
THRESHOLD2 = 0.1

""""threshold value for unstable flooding"""
THRESHOLD3 = 0

"""flooding maps library parameters"""
Q_MAX = 35
Q_MIN = 13
T_MAX = 50
T_MIN = 1

"""default decrease height for flooding map from library"""
DEFAULT_DECREASE_HEIGHT = 0.5

"""coordinates for Akhtuba entrance"""
AKHTUBA_ENTRANCE_COORDS = (787, 339)

"""table with retrospective hydrograph parameters"""
RETROSPECTIVE_HYDROGRAPHS_TABLE = pd.read_excel(RETROSPECTIVE_HYDROGRAPHS_FILEPATH)[['Year', 'Q', 't']]

"""parameter for criteria funcs"""
EPS = 0.1

"""dictionary for types corresponded to 4 main functional types"""
FS_4_TYPES = {"Экологические территории": [31, 187, 189, 214, 215, 216, 219, 220],
              "Социальные территории": [58, 63, 66, 87, 171, 195, 200, 205, 203, 207],
              "Экономические территории": [12, 95, 103, 37, 38, 39, 43, 44, 45, 132, 135, 150, 186, 221, 222, 224],
              "Некадастрированные территории": [8888]}

"""dictionary for types corresponded to 6 main functional types"""
FS_7_TYPES = {"Водно-болотные угодья": [31, 187, 189, 214, 219, 220],
              "Леса": [215, 216],
              "Заливные луга": [37, 39],
              "Хозяйственные зоны": [12, 38, 43, 44, 45, 95, 103, 132, 135, 150, 186, 221, 222, 224],
              "Жилые зоны": [58, 63, 66, 87, 171],
              "Рекреационные зоны": [195, 200, 203, 205, 207],
              "Некадастрированные\nтерритории": [8888]}
