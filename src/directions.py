class Directions:
    RIGHT = None
    UP = None
    LEFT = None
    DOWN = None

    def __init__(self, i, j):
        self.RIGHT = (i, j + 1)
        self.UP = (i - 1, j)
        self.LEFT = (i, j - 1)
        self.DOWN = (i + 1, j)
