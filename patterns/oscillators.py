class Oscillator(object):
    GRID_SIZE = (0, 0)
    PERIOD = 0
    CELLS = []

    def __init__(self, grid_size=None, period=None):
        self.behavior = 'OSCILLATE'
        self.grid_size = grid_size if grid_size else self.GRID_SIZE
        self.period = period if period else self.PERIOD


class Blinker(Oscillator):
    GRID_SIZE = (5, 5)
    PERIOD = 2
    CELLS = [(0, 1), (0, 0), (0, -1)]

    def __init__(self):
        super().__init__()


class Toad(Oscillator):
    GRID_SIZE = (6, 6)
    PERIOD = 2
    CELLS = [(-1, 0), (-1, 1), (-1, 2),
             (0, -1), (0, 0), (0, 1)]

    def __init__(self):
        super().__init__()


class Beacon(Oscillator):
    GRID_SIZE = (6, 6)
    PERIOD = 2
    CELLS = [(-3, 0), (-3, 1),
             (-2, 0),
             (-1, 3),
             (0, 2), (0, 3)]

    def __init__(self):
        super().__init__()


class Pulsar(Oscillator):
    GRID_SIZE = (15, 15)
    PERIOD = 3
    CELLS = [(-5, -4), (-5, -3), (-5, -2), (-5, 2), (-5, 3), (-5, 4),
             (-4, -5), (-4, -1), (-4, 1), (-4, 5),
             (-3, -5), (-3, -1), (-3, 1), (-3, 5),
             (-2, -5), (-2, -1), (-2, 1), (-2, 5),
             (-1, -4), (-1, -3), (-1, -2), (-1, 2), (-1, 3), (-1, 4),
             (1, -4), (1, -3), (1, -2), (1, 2), (1, 3), (1, 4),
             (2, -5), (2, -1), (2, 1), (2, 5),
             (3, -5), (3, -1), (3, 1), (3, 5),
             (4, -5), (4, -1), (4, 1), (4, 5),
             (5, -4), (5, -3), (5, -2), (5, 2), (5, 3), (5, 4)]

    def __init__(self):
        super().__init__()


class PentaDecathlon(Oscillator):
    GRID_SIZE = (11, 18)
    PERIOD = 15
    CELLS = [(-4, -1), (-4, 0), (-4, 1),
             (-3, -1), (-3, 1),
             (-2, -1), (-2, 0), (-2, 1),
             (-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 0), (0, 1),
             (1, -1), (1, 0), (1, 1),
             (2, -1), (2, 1),
             (3, -1), (3, 0), (3, 1)]

    def __init__(self):
        super().__init__()
