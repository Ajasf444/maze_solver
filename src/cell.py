from geometry import Line, Point
from window import Window


class Cell:
    def __init__(
        self,
        top_left: Point,
        bottom_right: Point,
        window: Window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
        wall_color="black",
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1, self._y1 = top_left.x, top_left.y
        self._x2, self._y2 = bottom_right.x, bottom_right.y
        self._window = window
        self.wall_color = wall_color

    def draw(self):
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y2),
                              Point(self._x2, self._y1))
            self._window.draw_line(right_wall, self.wall_color)
        if self.has_top_wall:
            top_wall = Line(Point(self._x2, self._y1),
                            Point(self._x1, self._y1))
            self._window.draw_line(top_wall, self.wall_color)
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1),
                             Point(self._x1, self._y2))
            self._window.draw_line(left_wall, self.wall_color)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2),
                               Point(self._x2, self._y2))
            self._window.draw_line(bottom_wall, self.wall_color)

    def draw_move(self, to_cell: "Cell", undo=False):
        from_center_point = self.get_center_point()
        to_center_point = to_cell.get_center_point()
        center_to_center_line = Line(from_center_point, to_center_point)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._window.draw_line(center_to_center_line, fill_color)

    def get_center_point(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)
