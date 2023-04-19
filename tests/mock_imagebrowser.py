from photov.util import is_image_file


class MockImageBrowser:
    def __init__(self):
        self.dir = []
        self._images: list[str] = []
        self.current_image = ...

    @property
    def images(self) -> list[str]:
        self._images = self.get_images_in_dir()
        self.current_image = self._images[0]
        return self._images

    def get_images_in_dir(self) -> list[str]:
        image_files = filter(is_image_file, self.dir)
        return list(image_files)

    def get_image_at(self, index: int) -> str:
        try:
            return self.images[index]
        except IndexError:
            try:
                return self.images[-1]
            except IndexError:
                return ''

    def get_image_index(self, img_path: str):
        if img_path not in self.images:
            return -1

        return self.images.index(img_path)

    def prev_image(self):
        current = self.get_image_index(self.current_image)
        next = self.get_image_at(current - 1)
        return next

    def next_image(self):
        current = self.get_image_index(self.current_image)
        next = self.get_image_at(current + 1)
        return next
