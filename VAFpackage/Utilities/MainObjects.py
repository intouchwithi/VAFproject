from .Converters.VolumeToQTConverter import VolumeToQTConverter
from .Converters.QTConverter import QTConverter

__all__ = ('V_TO_QT_CONVERTER', 'QT_CONVERTER')

"""default converter for getting QT from volume"""
V_TO_QT_CONVERTER = VolumeToQTConverter()

"""default converter for getting library QT"""
QT_CONVERTER = QTConverter()


