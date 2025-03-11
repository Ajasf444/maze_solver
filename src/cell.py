from geometry import Line, Point
from window import Window


class Cell:
    def __init__(
        self,
        top_left: Point,
        bottom_right: Point,
        window: Window = None,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
        wall_color="black",
        no_wall_color="gray",
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1, self._y1 = top_left.x, top_left.y
        self._x2, self._y2 = bottom_right.x, bottom_right.y
        self._window = window
        self.wall_color = wall_color
        self.no_wall_color = no_wall_color
        self.visited = False

    def draw(self):
        if not self._window:
            return
        right_wall = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
        top_wall = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        walls = [
            (right_wall, self.has_right_wall),
            (top_wall, self.has_top_wall),
            (left_wall, self.has_left_wall),
            (bottom_wall, self.has_bottom_wall),
        ]
        for wall_line, is_solid in walls:
            self._draw_wall(wall_line, is_solid)

    def _draw_wall(self, wall_line: Line, is_solid: bool):
        if not is_solid:
            return
        return self._window.draw_line(wall_line, self.wall_color)

    def draw_move(self, to_cell: "Cell", undo=False):
        from_center_point = self.get_center_point()
        to_center_point = to_cell.get_center_point()
        center_to_center_line = Line(from_center_point, to_center_point)
        fill_color = "green"
        if undo:
            fill_color = "red4"
        self._window.draw_line(center_to_center_line, fill_color)

    def get_center_point(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)
