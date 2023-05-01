from argparse import ArgumentParser, Action, RawTextHelpFormatter
from typing import Optional, Sequence, Any

from photov.const import PATH


class ArgParser:
    def __init__(self, args: Optional[Sequence[str]] | None):
        self._parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

        self.setup()

        self.subparsers = self._parser.add_subparsers(
            description="Subparser Group", help="Image file selection"
        )

        self.MoveCopyParser = self.subparsers.add_parser(
            name="SelectFiles",
            help="-d / --date Select files by date\n"
            "-r / --regex Select files by regex pattern\n",
        )
        self.MoveCopyParser.add_argument("-d", "--date", help="Select files by date")

        self.MoveCopyParser.add_argument(
            "-r", "--regex", help="Select files by regex pattern"
        )

        self.parsed_args = self._parser.parse_args(args)
        self.parsed_args: dict = vars(self.parsed_args)

    def setup(self):
        self._parser.add_argument(
            "-p",
            "--path",
            type=str,
            default=PATH,
            help="Specify source directory to operate on",
        )

        self._parser.add_argument(
            "-t",
            "--target",
            type=str,
            default="",
            help="Specify target directory to operate on",
        )

        self._parser.add_argument(
            "-g",
            "--gui",
            action="store_const",
            const=True,
            default=False,
            help="Run script with GUI",
        )

        self._parser.add_argument(
            "-c",
            "--copy",
            action=Copy,
            nargs=0,
            help="Copy image files to previously specified target directory",
        )

        self._parser.add_argument(
            "-m",
            "--move",
            action=Move,
            nargs=0,
            help="Move image files to previously specified target directory",
        )

    def get_arg(self, key: str) -> Any:
        return self.parsed_args[key]


class Copy(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("copy files")


class Move(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("Move files")
