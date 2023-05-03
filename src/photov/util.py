import pathlib
import os

from typing import Tuple, Sequence

from photov.const import IMAGE_EXTENSIONS


def is_image_file(path: str) -> bool:
    file_suffix = pathlib.Path(path).suffix

    if file_suffix.lower() in IMAGE_EXTENSIONS:
        return True
    else:
        return False


def get_possible_img_extensions() -> Sequence[tuple[str, str]]:
    extensions = [
        (f.upper().replace(".", "") + " Files", "*" + f) for f in IMAGE_EXTENSIONS
    ]
    return extensions


def bytes_to_nearest_unit(b: int) -> Tuple[float, str]:
    import math

    units = ["B", "KB", "MB", "GB", "TB"]
    div = int(math.floor(math.log(b, 1024)))
    p = math.pow(1024, div)
    r = round(b / p, 2)
    result = (r, units[div])
    return result


def get_images_in_dir(dir: str) -> list[str]:
    files: list[str] = os.listdir(dir)
    image_files: list[str] = list(filter(is_image_file, files))
    return image_files
