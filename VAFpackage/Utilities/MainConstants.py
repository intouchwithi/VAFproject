import pandas as pd
from .MainDirectories import RETROSPECTIVE_HYDROGRAPHS_FILEPATH

__all__ = ('THRESHOLD1', 'THRESHOLD2', 'THRESHOLD3', 'Q_MAX', 'Q_MIN', 'T_MIN', 'T_MAX', 'DEFAULT_DECREASE_HEIGHT',
           'AKHTUBA_ENTRANCE_COORDS','RETROSPECTIVE_HYDROGRAPHS_TABLE', 'EPS')

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
