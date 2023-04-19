import customtkinter

from photov.util import bytes_to_nearest_unit


class InfoBar:
    def __init__(self, root: customtkinter.CTk, parent_widget, parent):
        self.root: customtkinter.CTk = root
        self.parent_widget = parent_widget
        self.parent: object = parent

        self.FRAME = customtkinter.CTkFrame(self.root, height=50)
        self.FRAME.pack(fill="x", expand=True)

        self.INNERFRAME = customtkinter.CTkFrame(self.FRAME, height=50)
        self.INNERFRAME.grid(sticky="nsew")

        self.IMG_SIZE_LABEL = customtkinter.CTkLabel(self.INNERFRAME, text="%x%")
        self.IMG_SIZE_LABEL.grid(row=0, column=0)

        self.SEPARATOR = customtkinter.CTkLabel(self.INNERFRAME, text=" | ")
        self.SEPARATOR.grid(row=0, column=1)

        self.IMG_FILESIZE_LABEL = customtkinter.CTkLabel(self.INNERFRAME, text="%")
        self.IMG_FILESIZE_LABEL.grid(row=0, column=2)

    def set_img_size_text(self, size: tuple[int, int]):
        self.IMG_SIZE_LABEL.configure(text=f"{size[0]}x{size[1]}")

    def set_img_filesize_text(self, size: int):
        filesize = bytes_to_nearest_unit(size)
        text = f"{int(filesize[0])} {filesize[1]}"
        self.IMG_FILESIZE_LABEL.configure(text=text)
