import pathlib

from photov.const import IMAGE_EXTENSIONS


def is_image_file(path: str) -> bool:
    file_suffix = pathlib.Path(path).suffix

    if file_suffix.lower() in IMAGE_EXTENSIONS:
        return True
    else:
        return False
