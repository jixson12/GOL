import random
from collections import OrderedDict
from spaceships import Glider, LWSS, MWSS, HWSS


class Grid:

    def __init__(self, size=12):
        self.size = size
        self._coo_matrix = {}

    def init_glider(self):
        for cell in Glider.CELLS:
            self.set(cell[0], cell[1], 1)

    def init_lwss(self):
        for cell in LWSS.CELLS:
            self.set(cell[0], cell[1], 1)

    def init_mwss(self):
        for cell in MWSS.CELLS:
            self.set(cell[0], cell[1], 1)

    def init_hwss(self):
        for cell in HWSS.CELLS:
            self.set(cell[0], cell[1], 1)

    def clear(self):
        self._coo_matrix = {}

    def set(self, x, y, value=1):
        if (x, y) not in self._coo_matrix.keys():
            self._coo_matrix[(x, y)] = value
            return True
        return False

    def unset(self, x, y):
        if (x, y) not in self._coo_matrix.keys():
            raise KeyError("Cannot unset unset key value pair")
        else:
            return not self._coo_matrix.pop((x, y))

    def get(self, x, y):
        return self._coo_matrix[(x, y)] if (x, y) in self._coo_matrix.keys() else 0

    def flip(self, x, y):
        if (x, y) in self._coo_matrix.keys():
            return self.unset(x, y)
        else:
            return self.set(x, y)

    @staticmethod
    def count_neighbors(x, y, dict_copy):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                xi = x + i
                yj = y + j
                neighbors += dict_copy[(xi, yj)] if (xi, yj) in dict_copy.keys() else 0
        return neighbors

    def check_neighbors(self, x, y, dict_copy):
        for i in range(-1, 2):
            for j in range(-1, 2):
                xi = x + i
                yj = y + j
                if i == j == 0:
                    neighbor_count = self.count_neighbors(x, y, dict_copy)
                    flip = False
                    if neighbor_count < 2:
                        flip = True
                    elif neighbor_count > 3:
                        flip = True
                    if flip:
                        self.flip(x, y)
                else:
                    if (xi, yj) not in dict_copy.keys():
                        if self.count_neighbors(xi, yj, dict_copy) == 3:
                            self.set(xi, yj, 1)

    def get_next_state(self):
        cur_state = OrderedDict(sorted(self._coo_matrix.items(), key=lambda t: t[0]))
        for cell_x, cell_y in cur_state.keys():
            self.check_neighbors(cell_x, cell_y, cur_state)
