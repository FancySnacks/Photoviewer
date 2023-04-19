import customtkinter

import pathlib
import tkinter.filedialog


class SrcTargetInfo:
    def __init__(self, root: customtkinter.CTk, parent_widget, parent, image_browser):
        self.root: customtkinter.CTk = root
        self.parent_widget = parent_widget
        self.parent = parent
        self.image_browser = image_browser

        self.source_path: customtkinter.StringVar = customtkinter.StringVar(self.root)
        self.target_path: customtkinter.StringVar = customtkinter.StringVar(self.root)

        # ==== Widget Components ==== #

        self.FRAME = customtkinter.CTkFrame(self.parent_widget)
        self.FRAME.pack(pady=10)

        self.LABEL_FRAME = customtkinter.CTkFrame(self.FRAME)
        self.LABEL_FRAME.grid(row=0, column=0)

        self.ENTRIES_FRAME = customtkinter.CTkFrame(self.FRAME)
        self.ENTRIES_FRAME.grid(row=0, column=1)

        self.SRC_LABEL = customtkinter.CTkLabel(self.LABEL_FRAME, text="SRC")
        self.SRC_LABEL.grid(row=0, column=0, sticky="e")

        self.SRC_FRAME = customtkinter.CTkFrame(self.ENTRIES_FRAME)
        self.SRC_FRAME.grid()

        self.SRC_ENTRY = customtkinter.CTkEntry(
            self.SRC_FRAME, textvariable=self.source_path, width=450
        )
        self.SRC_ENTRY.grid(padx=5, row=0, column=1)

        self.SRC_BUTTON = customtkinter.CTkButton(
            self.SRC_FRAME,
            text="Update",
            command=self.change_source,
            width=5,
        )
        self.SRC_BUTTON.grid(row=0, column=2)

        self.BROWSE_SRC_BUTTON = customtkinter.CTkButton(
            self.SRC_FRAME,
            text="Browse..",
            command=self.browse_source,
            width=5,
        )
        self.BROWSE_SRC_BUTTON.grid(row=0, column=3)

        self.TARGET_FRAME = customtkinter.CTkFrame(self.ENTRIES_FRAME)
        self.TARGET_FRAME.grid(pady=5)

        self.TARGET_LABEL = customtkinter.CTkLabel(self.LABEL_FRAME, text="TARGET")
        self.TARGET_LABEL.grid(row=1, column=0)

        self.TARGET_ENTRY = customtkinter.CTkEntry(
            self.TARGET_FRAME, textvariable=self.target_path, width=450
        )
        self.TARGET_ENTRY.grid(padx=5, row=1, column=1)

        self.MOVE_BUTTON = customtkinter.CTkButton(
            self.TARGET_FRAME,
            text="Copy",
            command=self.copy_file,
            width=5,
        )
        self.MOVE_BUTTON.grid(row=1, column=2)

        self.BROWSE_TARGET_BUTTON = customtkinter.CTkButton(
            self.TARGET_FRAME,
            text="Browse..",
            command=self.browse_destination,
            width=5,
        )
        self.BROWSE_TARGET_BUTTON.grid(row=1, column=3)

    def set_source_dir(self, path: str):
        self.SRC_ENTRY.delete(0, customtkinter.END)
        self.SRC_ENTRY.insert(0, path)
        self.SRC_ENTRY.xview_moveto(len(self.SRC_ENTRY.get()))

    def change_source(self):
        path = self.source_path.get()
        self.update_cwd(path)

    def update_cwd(self, path: str):
        cwd_path: pathlib.Path = pathlib.Path(path)

        if cwd_path == self.image_browser.current_dir:
            return

        if cwd_path.is_file():
            cwd_path: str = str(cwd_path.parent).replace('"', "")

        self.image_browser.current_dir = cwd_path
        self.parent.load_default_image()

    def copy_file(self):
        if target_dir := self.target_path.get():
            if pathlib.Path(target_dir).exists():
                self.image_browser.copy_file(self.target_path.get())

    def browse_source(self):
        try:
            source_dir: str = tkinter.filedialog.askdirectory(
                initialdir=self.image_browser.current_dir, mustexist=True
            )
            if source_dir:
                self.source_path.set(source_dir)
                self.update_cwd(source_dir)
        except Exception:
            return

    def browse_destination(self):
        try:
            target_dir: str = tkinter.filedialog.askdirectory(
                initialdir=self.image_browser.current_dir, mustexist=True
            )
            if target_dir:
                self.target_path.set(target_dir)
        except Exception:
            return
