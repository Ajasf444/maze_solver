from geometry import Point


class Cell:
    def __init__(
        self,
        top_left: Point,
        bottom_right: Point,
        window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1, self._y1 = top_left.x, top_left.y
        self._x2, self._y2 = bottom_right.x, bottom_right.y
        self._window = window
