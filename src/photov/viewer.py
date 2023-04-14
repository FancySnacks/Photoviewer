from PIL import Image, ImageTk

import os

from photov.GUI.ImageBrowser import ImageBrowserGUI
from photov.util import is_image_file


class ImageBrowser:
    def __init__(self, show_widget = False, path: str = "."):
        self.current_dir = path
        self._images: list[str] = self.get_images_in_dir()
        self.current_image: MainImage = MainImage()

        if show_widget is True:
            self.widget = ImageBrowserGUI(self)
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
        try:
            return self.images[index]
        except IndexError:
            return self.images[0]

    def get_image_index(self, img_path: str):
        if img_path not in self.images:
            return -1

        return self.images.index(img_path)

    def change_image(self, location: str = ""):
        if location == "":
            self.current_image.load_image(self.images[0])
        else:
            self.current_image.load_image(location)

        if self.widget:
            self.widget.set_image(self.current_image)

    def prev_image(self, *args):
        current_index = self.get_image_index(self.current_image.location)
        prev_img = self.get_image_at(current_index - 1)
        self.change_image(prev_img)

    def next_image(self, *args):
        current_index = self.get_image_index(self.current_image.location)
        next_img = self.get_image_at(current_index + 1)
        self.change_image(next_img)


class MainImage:
    def __init__(self, location: str = ""):
        self.location: str = location
        self._image = None

    @property
    def get_image(self):
        self.img = ImageTk.PhotoImage(self._image)
        return self.img

    def load_image(self, location: str):
        self._image = Image.open(location)
        self.location = location
