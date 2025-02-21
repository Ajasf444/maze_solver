from cell import Cell
from geometry import Line, Point
from window import Window


def main():
    win = Window(800, 600)
    pA, pB = Point(0, 0), Point(400, 300)
    line = Line(pA, pB)
    win.draw_line(line, "black")
    pC, pD = Point(400, 0), Point(0, 300)
    line = Line(pC, pD)
    win.draw_line(line, "red")
    cellA = Cell(pA, pB, win)
    cellB = Cell(
        Point(400, 400), Point(500, 500), win, has_left_wall=False, has_right_wall=False
    )
    cellA.draw()
    cellB.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
