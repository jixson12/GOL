class Spaceship(object):
    GRID_SIZE = (0, 0)
    DIRECTION = (0, 0)
    SPEED = 0.0
    CELLS = []

    def __init__(self, grid_size=None, direction=None, speed=None):
        self.behavior = 'MOVE'
        self.grid_size = grid_size if grid_size else self.GRID_SIZE
        self.direction = direction if direction else self.DIRECTION
        self.speed = speed if speed else self.SPEED


class Glider(Spaceship):
    GRID_SIZE = (5, 5)
    DIRECTION = (1, -1)
    SPEED = 0.25
    CELLS = [(1, 2),
             (2, 3),
             (3, 1), (3, 2), (3, 3)]

    def __init__(self):
        super().__init__()


class LWSS(Spaceship):
    GRID_SIZE = (7, 6)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(1, 3), (1, 4),
             (2, 1), (2, 2), (2, 4), (2, 5),
             (3, 1), (3, 2), (3, 3), (3, 4),
             (4, 2), (4, 3)]

    def __init__(self):
        super().__init__()


class MWSS(Spaceship):
    GRID_SIZE = (8, 6)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(1, 4), (1, 5),
             (2, 1), (2, 2), (2, 3), (2, 5), (2, 6),
             (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
             (4, 2), (4, 3), (4, 4)]

    def __init__(self):
       super().__init__()


class HWSS(Spaceship):
    GRID_SIZE = (9, 6)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(1, 5), (1, 6),
             (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7),
             (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
             (4, 2), (4, 3), (4, 4), (4, 5)]

    def __init__(self):
        super().__init__()
