class Methuselah(object):
    GRID_SIZE = (0, 0)
    GENERATIONS = 0
    STABILIZE = False
    CELLS = []

    def __init__(self, grid_size=None, generations=None, stabilize=False):
        self.behavior = 'EVOLVE'
        self.grid_size = grid_size if grid_size else self.GRID_SIZE
        self.generations = generations if generations else self.GENERATIONS
        self.stabilize = stabilize if stabilize else self.STABILIZE


class RPentomino(Methuselah):
    GRID_SIZE = (5, 5)
    GENERATIONS = 130
    STABILIZE = True
    CELLS = [(-1, 0), (-1, 1),
             (0, -1, (0, 0),
             (1, 0)]

    def __init__(self):
        super().__init__()

class