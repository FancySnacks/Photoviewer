import pathlib
from tkinter import *


class SrcTargetInfo:
    def __init__(self, root: Tk, parent_widget, parent):
        self.root: Tk = root
        self.parent_widget = parent_widget
        self.parent = parent

        self.source_path: StringVar = StringVar(self.root)
        self.target_path: StringVar = StringVar(self.root)

        # ==== Widget Components ==== #

        self.FRAME = Frame(self.parent_widget)
        self.FRAME.pack(pady=10)

        self.LABEL_FRAME = Frame(self.FRAME)
        self.LABEL_FRAME.grid(row=0, column=0)

        self.ENTRIES_FRAME = Frame(self.FRAME)
        self.ENTRIES_FRAME.grid(row=0, column=1)

        self.SRC_LABEL = Label(self.LABEL_FRAME, text="SRC")
        self.SRC_LABEL.grid(row=0, column=0, sticky="e")

        self.SRC_FRAME = Frame(self.ENTRIES_FRAME)
        self.SRC_FRAME.grid()

        self.SRC_ENTRY = Entry(self.SRC_FRAME, textvariable=self.source_path, width=75)
        self.SRC_ENTRY.grid(padx=5, row=0, column=1)

        self.SRC_BUTTON = Button(self.SRC_FRAME, text="CHANGE", command=self.change_source)
        self.SRC_BUTTON.grid(row=0, column=2)

        self.TARGET_FRAME = Frame(self.ENTRIES_FRAME)
        self.TARGET_FRAME.grid(pady=5)

        self.TARGET_LABEL = Label(self.LABEL_FRAME, text="TARGET")
        self.TARGET_LABEL.grid(row=1, column=0)

        self.TARGET_ENTRY = Entry(self.TARGET_FRAME, textvariable=self.target_path, width=75)
        self.TARGET_ENTRY.grid(padx=5, row=1, column=1)

        self.MOVE_BUTTON = Button(self.TARGET_FRAME, text="COPY", command=self.copy_file)
        self.MOVE_BUTTON.grid(row=1, column=2)

    def set_source_dir(self, path: str):
        self.SRC_ENTRY.delete(0, END)
        self.SRC_ENTRY.insert(0, path)
        self.SRC_ENTRY.xview_moveto(len(self.SRC_ENTRY.get()))

    def change_source(self):
        path = pathlib.Path(self.source_path.get()).parent
        if path == self.parent.parent.current_dir:
            return

        input_path = self.source_path.get().replace('"', '')
        self.parent.parent.current_dir = input_path
        self.parent.load_default_image()

    def copy_file(self):
        if target_dir := self.target_path.get():
            if pathlib.Path(target_dir).exists():
                self.parent.parent.copy_file(self.target_path.get())
