from .Converters.VolumeToQTConverter import VolumeToQTConverter
__all__ = ('THRESHOLD1', 'THRESHOLD2', 'THRESHOLD3','V_TO_QT_CONVERTER')

""""threshold value for stable flooding"""
THRESHOLD1 = 0.85

""""threshold value for unstable flooding - 2 stage (currently is not used)"""
THRESHOLD2 = 0.1

""""threshold value for unstable flooding"""
THRESHOLD3 = 0

"""default converter for getting QT from volume"""
V_TO_QT_CONVERTER = VolumeToQTConverter()
