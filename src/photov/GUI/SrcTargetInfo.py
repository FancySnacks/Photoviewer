import tkinter
from tkinter import *


class SrcTargetInfo:
    def __init__(self, root: tkinter.Tk, parent_widget, parent):
        self.root: tkinter.Tk = root
        self.parent_widget = parent_widget
        self.parent = parent

        self.source_path: StringVar = StringVar(self.root)
        self.target_path: StringVar = StringVar(self.root)

        self.FRAME = Frame(self.parent_widget)
        self.FRAME.pack(pady=10)

        self.SRC_FRAME = Frame(self.FRAME)
        self.SRC_FRAME.grid()

        self.SRC_LABEL = Label(self.SRC_FRAME, text="SRC")
        self.SRC_LABEL.grid(row=0, column=0)

        self.SRC_ENTRY = Entry(self.FRAME, textvariable=self.source_path, width=75)
        self.SRC_ENTRY.grid(padx=5, row=0, column=1)

        self.TARGET_FRAME = Frame(self.FRAME)
        self.TARGET_FRAME.grid(pady=5)

        self.TARGET_LABEL = Label(self.TARGET_FRAME, text="TARGET")
        self.TARGET_LABEL.grid(row=1, column=0)

        self.TARGET_ENTRY = Entry(self.FRAME, textvariable=self.target_path, width=75)
        self.TARGET_ENTRY.grid(padx=5, row=1, column=1)

    def set_source_dir(self, path: str):
        self.SRC_ENTRY.delete(0, END)
        self.SRC_ENTRY.insert(0, path)
        self.SRC_ENTRY.xview_moveto(len(self.SRC_ENTRY.get()))
