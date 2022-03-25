from .Converters.VolumeToQTConverter import VolumeToQTConverter
from .Converters.QTConverter import QTConverter
from .Converters.QAmendmentConverter import QAmendmentConverter
from .GrdMap import GrdMap
import pandas as pd
from.MainDirectories import ALLOWED_LAND_USAGE_FILEPATH
from .MainDirectories import RETROSPECTIVE_HYDROGRAPHS_FILEPATH

__all__ = ('V_TO_QT_CONVERTER', 'QT_CONVERTER', 'ALLOWED_LAND_USAGE_MAP','RETROSPECTIVE_HYDROGRAPHS_TABLE',
           'Q_AMEND_CONVERTER')

"""default converter for getting QT from volume"""
V_TO_QT_CONVERTER = VolumeToQTConverter()

"""default converter for getting library QT"""
QT_CONVERTER = QTConverter()

"""default converter for Q amendment depending on year"""
Q_AMEND_CONVERTER = QAmendmentConverter

"""grd map with allowed types of use"""
ALLOWED_LAND_USAGE_MAP = GrdMap()
ALLOWED_LAND_USAGE_MAP.read_map_from_file(filepath=ALLOWED_LAND_USAGE_FILEPATH)

"""table with retrospective hydrograph parameters"""
RETROSPECTIVE_HYDROGRAPHS_TABLE = pd.read_excel(RETROSPECTIVE_HYDROGRAPHS_FILEPATH)[['Year', 'Q', 't']]
