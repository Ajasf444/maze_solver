from window import Window
from geometry import Point, Line


def main():
    win = Window(800, 600)
    pA, pB = Point(0, 0), Point(400, 300)
    line = Line(pA, pB)
    win.draw_line(line, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
