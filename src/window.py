from tkinter import Tk, BOTH, Canvas


class Window:
    DEFAULT_TITLE = "Baconator Fries"

    def __init__(self, width, height):
        self.root = Tk(Window.DEFAULT_TITLE)
        self.canvas = Canvas()
        self.canvas.pack()
        self.is_running = False
