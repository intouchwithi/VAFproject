
__all__ = ('THRESHOLD1', 'THRESHOLD2', 'THRESHOLD3', 'Q_MAX', 'Q_MIN', 'T_MIN', 'T_MAX', 'DEFAULT_DECREASE_HEIGHT',
           'AKHTUBA_ENTRANCE_COORDS')

""""threshold value for stable flooding"""
THRESHOLD1 = 0.85

""""threshold value for unstable flooding - 2 stage (currently is not used)"""
THRESHOLD2 = 0.1

""""threshold value for unstable flooding"""
THRESHOLD3 = 0

"""flooding maps library parameters"""
Q_MAX = 50
Q_MIN = 13
T_MAX = 50
T_MIN = 1

"""default decrease height for flooding map from library"""
DEFAULT_DECREASE_HEIGHT = 0.5

"""coordinates for Akhtuba entrance"""
AKHTUBA_ENTRANCE_COORDS = (788, 340)
