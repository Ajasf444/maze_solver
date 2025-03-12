from cell import Cell
from maze import Maze
from geometry import Line, Point
from window import Window
import sys
import random


def main():
    #    num_rows = 195
    #    num_cols = 360
    num_rows = 335
    num_cols = 630
    cell_size = 4
    win_width = 10 + num_cols * cell_size
    win_height = 10 + num_rows * cell_size
    sys.setrecursionlimit(num_rows * num_cols)
    win = Window(win_width, win_height)
    pA, pB = Point(5, 5), Point(400, 300)
    #    line = Line(pA, pB)
    #    win.draw_line(line, "black")
    #    pC, pD = Point(400, 0), Point(0, 300)
    #    line = Line(pC, pD)
    #    win.draw_line(line, "red")
    #    cellA = Cell(pA, pB, win)
    #    cellB = Cell(
    #        Point(400, 400), Point(500, 500), win, has_left_wall=False, has_right_wall=False
    #    )
    #    cellA.draw()
    #    cellB.draw()
    #    cellA.draw_move(cellB)

    maze = Maze(pA, num_rows, num_cols, cell_size, cell_size, win)
    maze.solve("depth_first_search")
    win.wait_for_close()


if __name__ == "__main__":
    main()
