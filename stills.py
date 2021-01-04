class Still(object):

    GRID_SIZE = (0, 0)
    PATTERN = [[]]

    def __init__(self, grid_size=None, pattern=None):
        self.behavior = "STILL"
        self.grid_size = grid_size if grid_size else self.GRID_SIZE
        self.pattern = pattern if pattern else self.PATTERN


class Block(Still):

    GRID_SIZE = (4, 4)
    PATTERN = [[0, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]]

    def __init__(self):
        super().__init__()



class Beehive(Still):
    GRID_SIZE = (6, 5)
    PATTERN = [[0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 1, 0, 0, 1, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()


class Loaf(Still):
    GRID_SIZE = (6, 6)
    PATTERN = [[0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 1, 0, 0, 1, 0],
               [0, 0, 1, 0, 1, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()


class Boat(Still):
    GRID_SIZE = (5, 5)
    PATTERN = [[0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0],
               [0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()


class Tub(Still):
    GRID_SIZE = (5, 5)
    PATTERN = [[0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()