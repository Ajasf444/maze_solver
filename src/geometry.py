from tkinter import Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color):
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
