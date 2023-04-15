import pathlib

from photov.const import IMAGE_EXTENSIONS


def is_image_file(path: str) -> bool:
    file_suffix = pathlib.Path(path).suffix

    if file_suffix.lower() in IMAGE_EXTENSIONS:
        return True
    else:
        return False


def bytes_to_nearest_unit(bytes: int) -> (int, str):
    import math
    units = ["B", "KB", "MB", "GB", "TB"]
    div = int(math.floor(math.log(bytes, 1024)))
    p = math.pow(1024, div)
    r = round(bytes / p, 2)
    result = (r, units[div])
    return result
