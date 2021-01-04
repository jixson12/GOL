class Spaceship(object):
    GRID_SIZE = (0, 0)
    DIRECTION = (0, 0)
    SPEED = 0.0
    PATTERN = [[]]

    def __init__(self, grid_size=None, direction=None, speed=None):
        self.behavior = 'MOVE'
        self.grid_size = grid_size if grid_size else self.GRID_SIZE
        self.direction = direction if direction else self.DIRECTION
        self.speed = speed if speed else self.SPEED


class Glider(Spaceship):
    GRID_SIZE = (6, 6)
    DIRECTION = (1, -1)
    SPEED = 0.25
    PATTERN = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()


class LWSS(Spaceship):
    GRID_SIZE = (9, 7)
    DIRECTION = (1, 0)
    SPEED = 0.5
    PATTERN = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()


class MWSS(Spaceship):
    GRID_SIZE = (11, 9)
    DIRECTION = (1, 0)
    SPEED = 0.5
    PATTERN = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self):
       super().__init__()


class HWSS(Spaceship):
    GRID_SIZE = (12, 9)
    DIRECTION = (1, 0)
    SPEED = 0.5
    PATTERN = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self):
        super().__init__()
