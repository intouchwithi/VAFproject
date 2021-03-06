from pathlib import Path

__all__ = ('MAIN_DATA_DIRPATH', 'ALLOWED_LAND_USAGE_FILEPATH', 'RETROSPECTIVE_HYDROGRAPHS_FILEPATH',
           'FLOODING_MAPS_LIBRARY_DIRPATH', 'ERIKI_MAP_FILEPATH')

"""main directory for input data"""
#MAIN_DATA_DIRPATH = Path('D:\От 04.02.22\УНИВЕР\Программирование\ВАП\Input')
MAIN_DATA_DIRPATH = Path(r'C:\Users\isaev\Мои файлы\УНИВЕР\Программирование\ВАП\Input')

"""main directory for output data"""
#MAIN_DATA_DIRPATH = Path('D:\От 04.02.22\УНИВЕР\Программирование\ВАП\Input')
MAIN_DATA_OUTPUT_DIRPATH = Path(r'C:\Users\isaev\Мои файлы\УНИВЕР\Программирование\ВАП\Output')

"""directory for a library with flooding maps (Q=13-35, t=0-50)"""
FLOODING_MAPS_LIBRARY_DIRPATH = MAIN_DATA_DIRPATH / 'grdInputSourceNew'

"""grd map path with allowed types of use"""
ALLOWED_LAND_USAGE_FILEPATH = MAIN_DATA_DIRPATH / 'grdInputSourceNew' / 'TypeUseWithNonCadastr.grd'

"""xlsx file with retrospective year, Q, t"""
RETROSPECTIVE_HYDROGRAPHS_FILEPATH = MAIN_DATA_DIRPATH / 'data' / 'ПараметрыГидрографов v02.xls'

"""grd map with 0-1 channel structure"""
ERIKI_MAP_FILEPATH = MAIN_DATA_DIRPATH / 'grdInputSourceNew' / 'eriki.grd'