import numpy as np
import struct
from .MainDirectories import FLOODING_MAPS_LIBRARY_DIRPATH
from .MainConstants import DEFAULT_DECREASE_HEIGHT
from .MainObjects import QT_CONVERTER

__all__ = ('GrdMap',)


class InvalidType(Exception):
    pass


class NegativeData(Exception):
    pass


class WrongDimensionArray(Exception):
    pass


class GrdMap:
    def __init__(self):
        self._descriptor = b'DSBB'
        self._filename = ''
        self._rows = 944
        self._cols = 944
        self._minX = 8457525
        self._maxX = 8504675
        self._minY = 5364775
        self._maxY = 5411925
        self._minZ = 0
        self._maxZ = 0
        self._cells = np.zeros((self._rows, self._cols))
        self.q = None
        self.t = None

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def filename(self):
        return self._filename

    @property
    def shape(self):
        return self._rows, self._cols

    @property
    def cells(self):
        return self._cells

    @property
    def min_max_z(self):
        return self._minZ, self._maxZ

    @cells.setter
    def cells(self, value):
        if value.shape != (self._rows, self._cols):
            raise WrongDimensionArray("Check shape of an array")
        self._cells = value
        self._maxZ = np.max(self._cells)
        self._minZ = np.min(self._cells)

    def __getitem__(self, key):
        if type(key) is tuple:
            return self._cells[(key[0], key[1])]
        else:
            raise InvalidType("Write coordinates as tuple")

    def __setitem__(self, key, value):
        if type(key) is tuple:
            self._cells[(key[0], key[1])] = value
            self._maxZ = np.max(self._cells)
            self._minZ = np.min(self._cells)
        else:
            raise InvalidType("Write coordinates as tuple")

    def read_similar_map_from_library(self, *, q, t, height_to_reduce=DEFAULT_DECREASE_HEIGHT):
        self.q, self.t = QT_CONVERTER.convert(q=q, t=t)
        if self.q is not None:
            if (self.t + 9) <= 9:
                result_map_filepath = FLOODING_MAPS_LIBRARY_DIRPATH / str(self.q) / ("H_    " + str(self.t + 9) + ".grd")
            else:
                result_map_filepath = FLOODING_MAPS_LIBRARY_DIRPATH / str(self.q) / ("H_   " + str(self.t + 9) + ".grd")

        return self.read_map_from_file(filepath=result_map_filepath, height_to_reduce=height_to_reduce)

    def read_map_from_file(self, *, filepath, height_to_reduce=0):
        with open(filepath, 'rb') as infile:
            block = infile.read()
            self._descriptor = struct.unpack('4s', block[:4])[0]
            self._rows = struct.unpack('H', block[4:6])[0]
            self._cols = struct.unpack('H', block[6:8])[0]
            self._minX = struct.unpack('d', block[8:16])[0]
            self._maxX = struct.unpack('d', block[16:24])[0]
            self._minY = struct.unpack('d', block[24:32])[0]
            self._maxY = struct.unpack('d', block[32:40])[0]
            self._minZ = struct.unpack('d', block[40:48])[0]
            self._maxZ = struct.unpack('d', block[48:56])[0]

            tmp = []
            counter = 56

            while counter + 4 <= len(block):
                tmp.append(struct.unpack('f', block[counter:counter + 4])[0])
                counter = counter + 4

            self._cells = np.reshape(np.array(tmp), (self._rows, self._rows))
            self.reduce_height_to_map(height_to_reduce)
            self._maxZ = np.max(self._cells)
            self._minZ = np.min(self._cells)

        return self

    def write_map_to_file(self, filepath):
        with open(filepath, 'wb') as outfile:
            outfile.write(struct.pack('4s', self._descriptor))
            outfile.write(struct.pack('H', self._rows))
            outfile.write(struct.pack('H', self._cols))
            outfile.write(struct.pack('d', self._minX))
            outfile.write(struct.pack('d', self._maxX))
            outfile.write(struct.pack('d', self._minY))
            outfile.write(struct.pack('d', self._maxY))
            outfile.write(struct.pack('d', self._minZ))
            outfile.write(struct.pack('d', self._maxZ))

            for row in self._cells:
                for col in row:
                    outfile.write(struct.pack('f', col))

    def reduce_height_to_map(self, height):
        if height < 0:
            raise NegativeData("Height can't be negative")

        self._cells = (self._cells - np.ones((self._rows, self._cols)) * height).clip(0)
        self._maxZ = np.max(self._cells)
        self._minZ = np.min(self._cells)

        return self

    def add_height_to_map(self, height):
        if height < 0:
            raise NegativeData("Height can't be negative")

        self._cells = self._cells + np.ones((self._rows, self._cols)) * height
        self._maxZ = np.max(self._cells)
        self._minZ = np.min(self._cells)

        return self

    def get_map_unique_values_count(self,*, list_of_excluded_values=[]):
        unique_values, counts = np.unique(self._cells, return_counts=True)
        total_count = sum([count for value,count in zip(unique_values, counts) if value not in list_of_excluded_values])
        percents = [np.round(100*count/total_count, 4) for value, count in zip(unique_values, counts) if value not in list_of_excluded_values]
        return unique_values, counts, percents
