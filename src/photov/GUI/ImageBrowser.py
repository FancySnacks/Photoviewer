from __future__ import annotations
from typing import TYPE_CHECKING

from tkinter import *

from photov.GUI.SrcTargetInfo import SrcTargetInfo

if TYPE_CHECKING:
    from photov.viewer import ImageBrowser


class ImageBrowserGUI:
    def __init__(self, parent: ImageBrowser):
        self.parent = parent

        self.ROOT = Tk()
        self.ROOT.title("Photo Viewer")
        self.ROOT.geometry("500x400")

        self.FRAME = Frame(self.ROOT)
        self.FRAME.pack(expand=True, fill="both")

        self.SrcTarget = SrcTargetInfo(root=self.ROOT, parent_widget=self.FRAME, parent=self)

        self.LABEL = Label(self.FRAME)
        self.LABEL.pack(expand=True)

        self.BUTTONFRAME = Frame(self.FRAME)
        self.BUTTONFRAME.pack()

        self.PREVBUTTON = Button(self.BUTTONFRAME,
                                 text="< Prev",
                                 font=('Helvetica', 13, 'bold'),
                                 command=self.parent.next_image)
        self.PREVBUTTON.pack(pady=15, side="left")

        self.SEPARATOR = Frame(self.BUTTONFRAME)
        self.SEPARATOR.pack(expand=True, padx=50)

        self.NEXTBUTTON = Button(self.BUTTONFRAME,
                                 text="Next >",
                                 font=('Helvetica', 13, 'bold'),
                                 command=self.parent.next_image)
        self.NEXTBUTTON.pack(pady=15, side="right")

        self.bind_key_shortcuts()

        self.ROOT.after(100, self.load_default_image)

    def set_image(self, *args):
        img = args[0]
        self.LABEL.configure(image=img.get_image)
        self.ROOT.title(f"{img.location} - PhotoViewer")
        self.set_img_path_info(img.get_full_path())

    def set_img_path_info(self, path: str):
        self.SrcTarget.set_source_dir(path)

    def load_default_image(self, *args):
        self.parent.change_image()

    def bind_key_shortcuts(self):
        self.ROOT.bind('<Left>', self.parent.prev_image)
        self.ROOT.bind('<Right>', self.parent.next_image)
