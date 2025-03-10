from cell import Cell
from maze import Maze
from geometry import Line, Point
from window import Window
# import sys


def main():
    # sys.setrecursionlimit(20_000)
    win = Window(800, 600)
    pA, pB = Point(20, 20), Point(400, 300)
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

    maze = Maze(pA, 10, 10, 50, 50, win)
    maze._break_entrance_and_exit()
    maze._break_wall_r(0, 0)
    win.wait_for_close()


if __name__ == "__main__":
    main()
