import time

from cell import Cell
from geometry import Point
from window import Window


class Maze:
    SLEEP_TIME = 0.05

    def __init__(
        self,
        point: Point,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window = None,
    ):
        self.x1 = point.x
        self.y1 = point.y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                top_left_point = Point(
                    self.x1 + col * self.cell_size_x, self.y1 + row * self.cell_size_y
                )
                bottom_right_point = Point(
                    self.x1 + (col + 1) * self.cell_size_x,
                    self.y1 + (row + 1) * self.cell_size_y,
                )
                self._cells[col].append(
                    Cell(top_left_point, bottom_right_point, self._win)
                )
        if not self._win:
            return
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self._draw_cell(i, j)
                self._animate()

    def _draw_cell(self, row, column):
        self._cells[column][row].draw()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(Maze.SLEEP_TIME)
