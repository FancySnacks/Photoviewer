from __future__ import annotations
from typing import TYPE_CHECKING

import customtkinter

from photov.GUI.SrcTargetInfo import SrcTargetInfo
from photov.GUI.InfoBar import InfoBar

if TYPE_CHECKING:
    from photov.viewer import ImageBrowser


class ImageBrowserGUI:
    def __init__(self, parent: ImageBrowser):
        self.parent = parent

        customtkinter.set_appearance_mode("dark")

        # ==== Widget Components ==== #

        self.ROOT = customtkinter.CTk()
        self.ROOT.title("Photo Viewer")
        self.ROOT.geometry("800x600")

        self.FRAME = customtkinter.CTkFrame(self.ROOT)
        self.FRAME.pack(expand=True, fill="both")

        self.SrcTarget = SrcTargetInfo(
            root=self.ROOT,
            parent_widget=self.FRAME,
            parent=self,
            image_browser=self.parent,
        )
        self.InfoBar = InfoBar(root=self.ROOT, parent_widget=self.FRAME, parent=self)

        self.IMAGE = customtkinter.CTkLabel(self.FRAME, width=1000, height=845, text="")
        self.IMAGE.pack(expand=True)

        self.BUTTONFRAME = customtkinter.CTkFrame(self.FRAME)
        self.BUTTONFRAME.pack(anchor="s")

        self.PREVBUTTON = customtkinter.CTkButton(
            self.BUTTONFRAME,
            text="< Prev",
            font=("Helvetica", 11, "bold"),
            command=self.parent.next_image,
            width=5,
        )
        self.PREVBUTTON.pack(pady=15, side="left")

        self.IMG_COUNTER = customtkinter.CTkLabel(self.BUTTONFRAME, text="1/13")
        self.IMG_COUNTER.pack(expand=True, fill="x", side="left", padx=15)

        self.NEXTBUTTON = customtkinter.CTkButton(
            self.BUTTONFRAME,
            text="Next >",
            font=("Helvetica", 11, "bold"),
            command=self.parent.next_image,
            width=5,
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
        self.ROOT.bind("<Control-n>", self.parent.copy_file)
        self.ROOT.bind("<Control-m>", self.parent.move_file)

    def update_img_count(self, current_index: int, length: int):
        self.IMG_COUNTER.configure(text=f"{current_index}/{length}")

    def update_img_size(self, size: tuple[int, int], filesize: int):
        self.InfoBar.set_img_size_text(size)
        self.InfoBar.set_img_filesize_text(filesize)
