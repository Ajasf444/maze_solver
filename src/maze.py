import time
import random

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
        seed=None,
    ):
        self.x1 = point.x
        self.y1 = point.y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_wall_r(self, i, j):
        self._cells[j][i].visited = True
        while True:
            visited_cells = []
            # TODO: get adjacent cells to the current cell
            # neighboring cells ordered right, top, left, bottom
            adjacent_cells = [(i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j)]
            adjacent_cells = filter(Maze.cell_in_maze_bounds, adjacent_cells)
            possible_to_visit_cells = [
                cell for cell in adjacent_cells if not cell.visited
            ]

    def cell_in_maze_bounds(self, indices):
        i, j = indices
        return i >= 0 and i < self.num_rows and j >= 0 and j < self.num_cols
