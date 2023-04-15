from tkinter import *


class StatusBar:
    def __init__(self, root: Tk, parent_widget, parent):
        self.root: Tk = root
        self.parent_widget: BaseWidget = parent_widget
        self.parent: object = parent

        self.FRAME = Label(self.root, text="1/13")
        self.FRAME.pack(fill="x", expand=True)