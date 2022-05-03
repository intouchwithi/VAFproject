from collections import deque
import copy

__all__ = ('RegionList',)


class Region:
    def __init__(self):
        self.points = []
        self.size = 0

    def add_point(self, x, y):
        self.points.append((x, y))
        self.size += 1


class RegionList:
    def __init__(self, map, region_size=1):
        self.regions = []
        self.region_size = region_size
        self.map = copy.deepcopy(map)

        for x in range(self.map.rows):
            for y in range(self.map.cols):
                if self.map.cells[x, y] == 1:
                    self._generate_region(x, y)

    def _add_region(self, region):
        self.regions.append(region)

    def _generate_region(self, x, y):
        point_queue = deque()
        point_queue.append((x, y))

        new_region = Region()

        while (len(point_queue) != 0) and (new_region.size!=self.region_size):
            cur_x, cur_y = point_queue.popleft()
            if self.map.cells[cur_x, cur_y] == 1:
                self.map.cells[cur_x, cur_y] = 0
                new_region.add_point(cur_x, cur_y)

                if (cur_x - 1 >= 0) and (self.map.cells[cur_x - 1, cur_y] == 1):
                    point_queue.append((cur_x-1, cur_y))
                if (cur_y - 1 >= 0) and (self.map.cells[cur_x, cur_y - 1] == 1):
                    point_queue.append((cur_x, cur_y-1))
                if (cur_y + 1 < self.map.cols) and (self.map.cells[cur_x, cur_y + 1] == 1):
                    point_queue.append((cur_x, cur_y+1))
                if (cur_x + 1 < self.map.rows) and (self.map.cells[cur_x + 1, cur_y] == 1):
                    point_queue.append((cur_x+1, cur_y))

        if new_region.size!=self.region_size:
            for (cur_x,cur_y) in new_region.points:
                self.map.cells[cur_x, cur_y] = 1
        else:
            self._add_region(new_region)






