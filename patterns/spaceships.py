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
    CELLS = [(-1, 0),
             (0, 1),
             (1, -1), (1, 0), (1, 1)]

    def __init__(self):
        super().__init__()


class LWSS(Spaceship):
    GRID_SIZE = (7, 7)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(0, -2), (1, -2),
             (-2, -1), (-1, -1), (1, -1), (2, -1),
             (-2, 0), (-1, 0), (0, 0), (1, 0),
             (-1, 1), (0, 1)]

    def __init__(self):
        super().__init__()


class MWSS(Spaceship):
    GRID_SIZE = (9, 7)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(1, -2), (2, -2),
             (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
             (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
             (-1, 1), (0, 1), (1, 1)]

    def __init__(self):
        super().__init__()


class HWSS(Spaceship):
    GRID_SIZE = (9, 7)
    DIRECTION = (1, 0)
    SPEED = 0.5
    CELLS = [(1, -2), (2, -2),
             (-3, -1), (-2, -1), (-1, -1), (0, -1), (2, -1), (3, -1),
             (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
             (-2, 1), (-1, 1), (0, 1), (1, 1)]

    def __init__(self):
        super().__init__()
