import pathlib
from os import getcwd

from enum import StrEnum


PATH = pathlib.Path(getcwd())
ABSPATH = pathlib.Path(__file__).parent

PATH_TYPE_FILE = "FILE"
PATH_TYPE_DIR = "DIR"
PATH_TYPE_INVALID = "INVALID"

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")


class PathType(StrEnum):
    file: str = PATH_TYPE_FILE
    dir: str = PATH_TYPE_DIR
    invalid: str = PATH_TYPE_INVALID
