from __future__ import annotations
from typing import TYPE_CHECKING

from tkinter import *

if TYPE_CHECKING:
    from photov.viewer import ImageBrowser


class ImageBrowserGUI:
    def __init__(self, parent: ImageBrowser):
        self.parent = parent

        self.ROOT = Tk()
        self.ROOT.title("Photo Viewer")
        self.ROOT.geometry("500x400")

        self.LABEL = Label(self.ROOT)
        self.LABEL.pack(expand=True)

        self.PREVBUTTON = Button(self.ROOT,
                                 text="< Prev",
                                 font=('Helvetica', 13, 'bold'),
                                 command=self.parent.next_image)
        self.PREVBUTTON.pack(pady=15, side="left")

        self.NEXTBUTTON = Button(self.ROOT,
                                 text="Next >",
                                 font=('Helvetica', 13, 'bold'),
                                 command=self.parent.next_image)
        self.NEXTBUTTON.pack(pady=15, side="left")

    def set_image(self, *args):
        img = args[0]
        self.LABEL.configure(image=img.get_image)
        self.ROOT.title(f"{img.location} - PhotoViewer")