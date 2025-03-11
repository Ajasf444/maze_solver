import random
import time

from cell import Cell
from directions import Directions
from geometry import Point
from window import Window


class Maze:
    SLEEP_TIME = 0.05
    SOLVE_ANIMATION_TIME = SLEEP_TIME / 50
    ANIMATION_TIME = SLEEP_TIME / 10

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
        self._break_entrance_and_exit()
        self._break_wall_r(0, 0)
        self._reset_cells_visited()
        self._draw_maze()

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

    def _draw_maze(self):
        if not self._win:
            return
        for j in range(self.num_cols):
            self._draw_column(j)

    def _draw_column(self, j):
        for i in range(self.num_rows):
            self._draw_cell(i, j)
        self._animate(Maze.ANIMATION_TIME)

    def _draw_cell(self, row, column):
        self._cells[column][row].draw()

    def _animate(self, sleep_time=SLEEP_TIME):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(sleep_time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

    def _break_wall_r(self, i, j):
        self._cells[j][i].visited = True
        directions = Directions(i, j)
        while True:
            # neighboring cells ordered right, top, left, bottom
            possible_to_visit_cells = self._get_visitable_cells(i, j)

            if not possible_to_visit_cells:
                return
            else:
                chosen_direction = random.choice(possible_to_visit_cells)
                i_n, j_n = chosen_direction
                neighbor_cell = self._cells[j_n][i_n]
                match chosen_direction:
                    case directions.RIGHT:
                        self._cells[j][i].has_right_wall = False
                        neighbor_cell.has_left_wall = False
                    case directions.UP:
                        self._cells[j][i].has_top_wall = False
                        neighbor_cell.has_bottom_wall = False
                    case directions.LEFT:
                        self._cells[j][i].has_left_wall = False
                        neighbor_cell.has_right_wall = False
                    case directions.DOWN:
                        self._cells[j][i].has_bottom_wall = False
                        neighbor_cell.has_top_wall = False
                next_i, next_j = chosen_direction
                self._break_wall_r(next_i, next_j)

    def _cell_in_maze_bounds(self, indices):
        i, j = indices
        return i >= 0 and i < self.num_rows and j >= 0 and j < self.num_cols

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(Maze.SOLVE_ANIMATION_TIME)
        current_cell = self._cells[j][i]
        current_cell.visited = True
        if self._cells[-1][-1].visited is True:
            return True
        visitable_cells = self._get_visitable_cells(i, j)
        #        random.shuffle(visitable_cells)
        directions = Directions(i, j)
        for cell in visitable_cells:
            match cell:
                case directions.RIGHT:
                    i_n, j_n = directions.RIGHT
                    has_wall = current_cell.has_right_wall
                case directions.UP:
                    i_n, j_n = directions.UP
                    has_wall = current_cell.has_top_wall
                case directions.LEFT:
                    i_n, j_n = directions.LEFT
                    has_wall = current_cell.has_left_wall
                case directions.DOWN:
                    i_n, j_n = directions.DOWN
                    has_wall = current_cell.has_bottom_wall
            neighbor_cell = self._cells[j_n][i_n]
            if not has_wall and not neighbor_cell.visited:
                current_cell.draw_move(neighbor_cell)
                is_exit = self._solve_r(i_n, j_n)
                if is_exit:
                    return True
                else:
                    # self._animate(Maze.SOLVE_ANIMATION_TIME)
                    current_cell.draw_move(neighbor_cell, undo=True)

    def _get_neighboring_cells(self, i, j):
        adjacent_cells = [
            (i, j + 1),
            (i + 1, j),
            (i - 1, j),
            (i, j - 1),
        ]
        return filter(self._cell_in_maze_bounds, adjacent_cells)

    def _get_visitable_cells(self, i, j):
        cells = self._get_neighboring_cells(i, j)
        return [cell for cell in cells if not self._cells[cell[1]][cell[0]].visited]
