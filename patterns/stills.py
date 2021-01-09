class Still(object):

    GRID_SIZE = (0, 0)
    CELLS = []

    def __init__(self, grid_size=None):
        self.behavior = "STILL"
        self.grid_size = grid_size if grid_size else self.GRID_SIZE


class Block(Still):

    GRID_SIZE = (4, 4)
    CELLS = [(0, 0), (0, 1),
             (1, 0), (1, 1)]

    def __init__(self):
        super().__init__()



class Beehive(Still):
    GRID_SIZE = (6, 5)
    CELLS = [(-1, 0), (-1, 1),
             (0, -1), (0, 2),
             (1, 0), (1, 1)]

    def __init__(self):
        super().__init__()


class Loaf(Still):
    GRID_SIZE = (6, 6)
    CELLS = [(-1, 0), (-1, 1),
             (0, -1), (0, 2),
             (1, 0), (1, 2),
             (2, 1)]

    def __init__(self):
        super().__init__()


class Boat(Still):
    GRID_SIZE = (5, 5)
    CELLS = [(-1, 1), (-1, 0),
             (0, -1), (0, 1),
             (1, 0)]

    def __init__(self):
        super().__init__()


class Tub(Still):
    GRID_SIZE = (5, 5)
    CELLS = [(-1, 0),
             (0, -1), (0, 1),
             (1, 0)]

    def __init__(self):
        super().__init__()
