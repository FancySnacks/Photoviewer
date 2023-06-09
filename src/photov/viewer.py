from PIL import Image, ImageTk

import os
import pathlib
import shutil

from photov.GUI.ImageBrowser import ImageBrowserGUI
from photov.util import get_images_in_dir


class ImageBrowser:
    def __init__(self, path: str, show_widget: bool = False, target_dir: str = ""):
        self._current_dir: str = (
            str(pathlib.Path(path).parent) if pathlib.Path(path).is_file() else path
        )
        self._images: list[str] = get_images_in_dir(self.current_dir)
        self.current_image: MainImage = MainImage()
        self.target_dir = target_dir

        if show_widget is True:
            self.widget = ImageBrowserGUI(self)
            self.widget.set_img_path_info(self.current_dir)
            self.widget.SrcTarget.target_path.set(self.target_dir)
            self.widget.ROOT.mainloop()

    @property
    def current_dir(self) -> str:
        return self._current_dir

    @current_dir.setter
    def current_dir(self, value: str):
        if pathlib.Path(value).is_file():
            self._current_dir = str(pathlib.Path(value).parent)
        else:
            self._current_dir = value

    @property
    def images(self) -> list[str]:
        self._images = get_images_in_dir(self.current_dir)
        return self._images

    def get_image_at(self, index: int) -> str:
        try:
            return self.images[index]
        except IndexError:
            return self.images[0]

    def get_image_index(self, img_path: str):
        if img_path not in self.images:
            return -1

        return self.images.index(img_path)

    def change_image(self, location: pathlib.Path = ""):
        self._file_pointer(location)

        if pathlib.Path(location).is_dir():
            self.current_image.load_image(self.full_path(self.images[0]), 1)

        if location == "" or location == ".":
            self.current_image.load_image(self.full_path(self.images[0]), 1)

        if self.widget:
            self.widget.set_image(self.current_image)
            self.widget.update_img_count(self.current_image.index, len(self.images))

    def _file_pointer(self, path: pathlib.Path):
        if pathlib.Path(path).is_file():
            img_index: int = self.images.index(path.name)
            self.current_image.load_image(self.full_path(path), img_index + 1)
        elif self.full_path(path).is_file():
            img_index: int = self.images.index(self.full_path(path).name)
            self.current_image.load_image(self.full_path(path), img_index + 1)

    def prev_image(self, *args):
        current_index: int = self.get_image_index(self.current_image.location)
        prev_img_path = self.get_image_at(current_index - 1)
        prev_img_path = pathlib.Path(prev_img_path)
        self.change_image(prev_img_path)

    def next_image(self, *args):
        current_index: int = self.get_image_index(self.current_image.location)
        next_img_path = self.get_image_at(current_index + 1)
        next_img_path = pathlib.Path(next_img_path)
        self.change_image(next_img_path)

    def full_path(self, img_path) -> pathlib.Path:
        path: pathlib.Path = pathlib.Path(self.current_dir).joinpath(img_path)
        return path

    def copy_file(self, *args):
        if self.target_dir:
            if pathlib.Path(self.target_dir).exists():
                shutil.copy(self.current_image.get_full_path(), self.target_dir)
                self.widget.SrcTarget._update_target_dir_img_count()
                print(f"Copied 1 image to {self.target_dir}")

    def move_file(self, *args):
        if self.target_dir:
            if pathlib.Path(self.target_dir).exists():
                shutil.move(self.current_image.get_full_path(), self.target_dir)
                self.widget.SrcTarget._update_target_dir_img_count()
                print(f"Moved 1 image to {self.target_dir}")

    def delete_file(self, *args):
        if not self.target_dir:
            return

        if self._is_img_in_target_dir(self.current_image.location, self.target_dir):
            img_to_delete = pathlib.Path.joinpath(pathlib.Path(self.target_dir),
                                                  pathlib.Path(self.current_image.location))
            print(img_to_delete)
            self.next_image()
            os.remove(img_to_delete)

    def delete_files(self, img_files: list = None, target_dir: str = None):
        if not target_dir:
            return

        for img in img_files:
            if self._is_img_in_target_dir(img, target_dir):
                img_to_delete = pathlib.Path.joinpath(pathlib.Path(target_dir),
                                                      pathlib.Path(img))
                print(img_to_delete)
                os.remove(img_to_delete)

    def _is_img_in_target_dir(self, img_path, dir_path) -> bool:
        return img_path in get_images_in_dir(dir_path)


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
        path = pathlib.Path(self._location).name
        return path

    def load_image(self, location: pathlib.Path, img_index: int):
        self.image: Image = Image.open(location)
        self._location: str = str(location)
        self.index: int = img_index
        self.file_size: int = os.path.getsize(self.get_full_path())

    def get_full_path(self) -> str:
        return self._location
