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
    CELLS = [(1, 2), (2, 2), (3, 2)]

    def __init__(self):
        super().__init__()


class Toad(Oscillator):
    GRID_SIZE = (6, 6)
    PERIOD = 2
    CELLS = [(2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (3, 4)]

    def __init__(self):
        super().__init__()


class Beacon(Oscillator):
    GRID_SIZE = (6, 6)
    PERIOD = 2
    CELLS = [(1, 1), (1, 2), (2, 1), (3, 4), (4, 3), (4, 4)]

    def __init__(self):
        super().__init__()


class Pulsar(Oscillator):
    GRID_SIZE = (15, 15)
    PERIOD = 3
    CELLS = [(2, 3), (2, 4), (2, 5), (2, 9), (2, 10), (2, 11),
             (3, 2), (3, 6), (3, 8), (3, 12),
             (4, 2), (4, 6), (4, 8), (4, 12),
             (5, 2), (5, 6), (5, 8), (5, 12),
             (6, 3), (6, 4), (6, 5), (6, 9), (6, 10), (6, 11),
             (8, 3), (8, 4), (8, 5), (8, 9), (8, 10), (8, 11),
             (9, 2), (9, 6), (9, 8), (9, 12),
             (10, 2), (10, 6), (10, 8), (10, 12),
             (11, 2), (11, 6), (11, 8), (11, 12),
             (12, 3), (12, 4), (12, 5), (12, 9), (12, 10), (12, 11)]

    def __init__(self):
        super().__init__()


class PentaDecathlon(Oscillator):
    GRID_SIZE = (11, 18)
    PERIOD = 15
    CELLS = [(5, 4), (5, 5), (5, 6),
             (6, 4), (6, 6),
             (7, 4), (7, 5), (7, 6),
             (8, 4), (8, 5), (8, 6),
             (9, 4), (9, 5), (9, 6),
             (10, 4), (10, 5), (10, 6),
             (11, 4), (11, 6),
             (12, 4), (12, 5), (12,6)]

    def __init__(self):
        super().__init__()
