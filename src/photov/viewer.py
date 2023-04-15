from PIL import Image, ImageTk

import os
import pathlib
import shutil

from photov.GUI.ImageBrowser import ImageBrowserGUI
from photov.util import is_image_file


class ImageBrowser:
    def __init__(self, show_widget=False, path: str = None):
        self.current_dir = path or pathlib.Path().cwd()
        self._images: list[str] = self.get_images_in_dir()
        self.current_image: MainImage = MainImage()

        if show_widget is True:
            self.widget = ImageBrowserGUI(self)
            self.widget.set_img_path_info(self.current_dir)
            self.widget.ROOT.mainloop()

    @property
    def images(self) -> list[str]:
        self._images = self.get_images_in_dir()
        return self._images

    def get_images_in_dir(self) -> list[str]:
        files: list[str] = os.listdir(self.current_dir)
        image_files: list[str] = list(filter(is_image_file, files))
        return image_files

    def get_image_at(self, index: int) -> str:
        print(index)
        try:
            return self.images[index]
        except IndexError:
            return self.images[0]

    def get_image_index(self, img_path: str):
        if img_path not in self.images:
            return -1

        return self.images.index(img_path)

    def change_image(self, location: str = ""):
        if location == "" or location == ".":
            self.current_image.load_image(self.full_path(self.images[0]), 1)
        else:
            img_index: int = self.images.index(location)
            self.current_image.load_image(self.full_path(location), img_index + 1)

        if self.widget:
            self.widget.set_image(self.current_image)
            self.widget.update_img_count(self.current_image.index, len(self.images))

    def prev_image(self, *args):
        current_index: int = self.get_image_index(self.current_image.location)
        prev_img_path: str = self.get_image_at(current_index - 1)
        self.change_image(prev_img_path)

    def next_image(self, *args):
        current_index: int = self.get_image_index(self.current_image.location)
        next_img_path: str = self.get_image_at(current_index + 1)
        self.change_image(next_img_path)

    def full_path(self, img_path: str) -> str:
        path: pathlib.Path = pathlib.Path(self.current_dir).joinpath(img_path)
        return str(path)

    def copy_file(self, target_path: str):
        shutil.copy(self.current_image.get_full_path(), target_path)

    def move_file(self, target_path: str):
        shutil.move(self.current_image.get_full_path(), target_path)


class MainImage:
    def __init__(self, location: str = ""):
        self._location: str = location
        self.image: Image = None
        self.index: int = 0
        self.file_size: int = 0

    @property
    def get_image(self) -> ImageTk:
        self.img = ImageTk.PhotoImage(self.image)
        return self.img

    @property
    def location(self) -> str:
        path = pathlib.Path(self._location).parts[-1]
        return path

    def load_image(self, location: str, img_index: int):
        self.image: Image = Image.open(location)
        self._location: str = location
        self.index: int = img_index
        self.file_size: int = os.path.getsize(self.get_full_path())

    def get_full_path(self) -> str:
        return self._location
