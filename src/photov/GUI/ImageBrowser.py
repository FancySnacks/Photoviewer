from __future__ import annotations
from typing import TYPE_CHECKING

from tkinter import *

from photov.GUI.SrcTargetInfo import SrcTargetInfo
from photov.GUI.InfoBar import InfoBar

if TYPE_CHECKING:
    from photov.viewer import ImageBrowser


class ImageBrowserGUI:
    def __init__(self, parent: ImageBrowser):
        self.parent = parent

        self.ROOT = Tk()
        self.ROOT.title("Photo Viewer")
        self.ROOT.geometry("800x600")

        self.FRAME = Frame(self.ROOT)
        self.FRAME.pack(expand=True, fill="both")

        self.SrcTarget = SrcTargetInfo(
            root=self.ROOT, parent_widget=self.FRAME, parent=self
        )
        self.InfoBar = InfoBar(root=self.ROOT, parent_widget=self.FRAME, parent=self)

        self.IMAGE = Label(self.FRAME, width=1000, height=845)
        self.IMAGE.pack(expand=True)

        self.BUTTONFRAME = Frame(self.FRAME)
        self.BUTTONFRAME.pack(anchor="s")

        self.PREVBUTTON = Button(
            self.BUTTONFRAME,
            text="< Prev",
            font=("Helvetica", 11, "bold"),
            command=self.parent.next_image,
        )
        self.PREVBUTTON.pack(pady=15, side="left")

        self.IMG_COUNTER = Label(self.BUTTONFRAME, text="1/13")
        self.IMG_COUNTER.pack(expand=True, fill="x", side="left", padx=15)

        self.NEXTBUTTON = Button(
            self.BUTTONFRAME,
            text="Next >",
            font=("Helvetica", 11, "bold"),
            command=self.parent.next_image,
        )
        self.NEXTBUTTON.pack(pady=15, side="right")

        self.bind_key_shortcuts()

        self.ROOT.after(100, self.load_default_image)

    def set_image(self, *args):
        img = args[0]
        self.IMAGE.configure(image=img.get_image)
        self.update_widgets(img)

    def update_widgets(self, img):
        self.ROOT.title(f"{img.location} - PhotoViewer")
        self.set_img_path_info(img.get_full_path())
        self.update_img_size(img.image.size, img.file_size)

    def set_img_path_info(self, path: str):
        self.SrcTarget.set_source_dir(path)

    def load_default_image(self, *args):
        self.parent.change_image()

    def bind_key_shortcuts(self):
        self.ROOT.bind("<Left>", self.parent.prev_image)
        self.ROOT.bind("<Right>", self.parent.next_image)

    def update_img_count(self, current_index: int, length: int):
        self.IMG_COUNTER.configure(text=f"{current_index}/{length}")

    def update_img_size(self, size: tuple[int, int], filesize: int):
        self.InfoBar.set_img_size_text(size)
        self.InfoBar.set_img_filesize_text(filesize)
