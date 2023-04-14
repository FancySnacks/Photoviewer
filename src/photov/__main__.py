from typing import Sequence, Optional

from photov.arg_parser import ArgParser
from photov.viewer import ImageBrowser


def main(argv: Optional[Sequence[str]] | None = None):
    parser = ArgParser(argv)
    work_dir = parser.get_arg('path')
    use_gui = not parser.get_arg('nogui')
    image_browser = ImageBrowser(show_widget=use_gui, path=work_dir)


if __name__ == "__main__":
    main()
