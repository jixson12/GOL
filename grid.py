import random
from copy import deepcopy
from collections import OrderedDict
from patterns.spaceships import Glider, LWSS, MWSS, HWSS


class Grid:

    def __init__(self, size=12, shadow=False):
        self.size = size
        self._coo_matrix = {}
        self.shadow = shadow

    def init_pattern(self, pattern, x_offset=0, y_offset=0, rotation='0', flipped=False):
        cells = self.rotate_pattern(pattern, rotation, flipped)
        for cell in cells:
            self.set(cell[0] + x_offset, cell[1] + y_offset, 1)

    @staticmethod
    def flipped_cells(cells):
        flipped = {}
        for cell_x, cell_y in cells:
            if cell_x == 0:
                flipped[(cell_x, cell_y)] = 1
            else:
                flipped[(-cell_x, cell_y)] = 1
        return flipped

    def rotate_pattern(self, pattern, rotation, flipped):
        rot_pat = {}
        cells = pattern.CELLS if not flipped else self.flipped_cells(pattern.CELLS)
        for cell in cells:
            if rotation == '0':
                rot_pat[(cell[0], cell[1])] = 1
            elif rotation == '90':
                rot_pat[(cell[0] * -1, cell[1])] = 1
            elif rotation == '180':
                rot_pat[(cell[0] * -1, cell[1] * -1)] = 1
            elif rotation == '270':
                rot_pat[(cell[0], cell[1] * -1)] = 1
        return rot_pat

    def init_glider(self):
        self.init_pattern(Glider)

    def init_lwss(self):
        self.init_pattern(LWSS)

    def init_mwss(self):
        self.init_pattern(MWSS)

    def init_hwss(self):
        self.init_pattern(HWSS)

    def clear(self):
        self._coo_matrix = {}

    def set(self, x, y, value=1):
        if (x, y) not in self._coo_matrix.keys():
            self._coo_matrix[(x, y)] = value
            return True
        return False

    def increment(self, x, y):
        if (x, y) in self._coo_matrix.keys():
            self.set(x, y, self.get(x, y) + 1)

    def decrement(self, x, y):
        if (x, y) in self._coo_matrix.keys():
            self.set(x, y, self.get(x, y) - 1)

    def unset(self, x, y):
        if (x, y) not in self._coo_matrix.keys():
            raise KeyError("Cannot unset unset key value pair")
        else:
            return not self._coo_matrix.pop((x, y))

    def get(self, x, y):
        return self._coo_matrix[(x, y)] if (x, y) in self._coo_matrix.keys() else 0

    def birth_cell(self, x, y):
        self.set(x, y, 1)

    def kill_cell(self, x, y):
        self._coo_matrix.pop((x, y))

    def is_alive(self, x, y):
        return (x, y) in self._coo_matrix.keys()

    def is_dead(self, x, y):
        return not self.is_alive(x, y)

    def flip(self, x, y):
        if (x, y) in self._coo_matrix.keys():
            return self.unset(x, y)
        else:
            return self.set(x, y)

    def points(self):
        return list(self._coo_matrix.keys())

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

    def check_neighbors(self, x, y, dict_copy, shadow_world):
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
                        # shadow_world.set(x, y, 5)
                else:
                    if (xi, yj) not in dict_copy.keys():
                        if self.count_neighbors(xi, yj, dict_copy) == 3:
                            self.set(xi, yj, 1)

    def get_next_state(self, shadow_world):
        if not shadow_world.shadow:
            raise AttributeError("Shadow world is not a shadow grid")
        cur_state = OrderedDict(sorted(self._coo_matrix.items(), key=lambda t: t[0]))
        # if shadow_world.points():
        #     print(shadow_world.points())
        #     for px, py in shadow_world.points():
        #         shadow_world.decrement(px, py)
        #         if shadow_world.get(px, py) == 0:
        #             shadow_world.pop((px, py))
        for cell_x, cell_y in cur_state.keys():
            self.check_neighbors(cell_x, cell_y, cur_state, shadow_world)
