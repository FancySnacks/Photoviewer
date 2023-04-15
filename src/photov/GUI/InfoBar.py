from tkinter import *
from photov.util import bytes_to_nearest_unit


class InfoBar:
    def __init__(self, root: Tk, parent_widget, parent):
        self.root: Tk = root
        self.parent_widget: BaseWidget = parent_widget
        self.parent: object = parent

        self.FRAME = Frame(self.root, borderwidth=2, height=50)
        self.FRAME.pack(fill="x", expand=True)

        self.INNERFRAME = Frame(self.FRAME, borderwidth=2, height=50)
        self.INNERFRAME.grid(sticky="nsew")

        self.IMG_SIZE_LABEL = Label(self.INNERFRAME, text="%x%")
        self.IMG_SIZE_LABEL.grid(row=0, column=0)

        self.SEPARATOR = Label(self.INNERFRAME, text=" | ")
        self.SEPARATOR.grid(row=0, column=1)

        self.IMG_FILESIZE_LABEL = Label(self.INNERFRAME, text="%")
        self.IMG_FILESIZE_LABEL.grid(row=0, column=2)

    def set_img_size_text(self, size: tuple[int, int]):
        self.IMG_SIZE_LABEL.configure(text=f"{size[0]}x{size[1]}")

    def set_img_filesize_text(self, size: int):
        filesize = bytes_to_nearest_unit(size)
        text = f"{int(filesize[0])} {filesize[1]}"
        self.IMG_FILESIZE_LABEL.configure(text=text)
