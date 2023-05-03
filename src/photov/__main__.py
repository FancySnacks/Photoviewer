from typing import Sequence, Optional

from photov.arg_parser import ArgParser, MoveCopyParser
from photov.viewer import ImageBrowser


def main(argv: Optional[Sequence[str]] | None = None):
    parser = ArgParser(argv, subparsers=[MoveCopyParser])

    work_dir: str = parser.get_arg("path")
    target_dir: str = parser.get_arg("target")
    use_gui: bool = parser.get_arg("gui")

    ImageBrowser(show_widget=use_gui, path=work_dir, target_dir=target_dir)


if __name__ == "__main__":
    main()
