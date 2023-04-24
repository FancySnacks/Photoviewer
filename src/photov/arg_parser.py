from argparse import ArgumentParser
from typing import Optional, Sequence, Any

from photov.const import PATH


class ArgParser(ArgumentParser):
    def __init__(self, args: Optional[Sequence[str]] | None):
        super().__init__()
        self.setup()

        self.parsed_args = self.parse_args(args)
        self.parsed_args: dict = vars(self.parsed_args)

    def setup(self):
        self.add_argument(
            "-p",
            "--path",
            type=str,
            default=PATH,
            help="Specify source directory to operate on",
        )

        self.add_argument(
            "-g",
            "--gui",
            action="store_const",
            const=True,
            default=False,
            help="Run script with GUI",
        )

    def get_arg(self, key: str) -> Any:
        return self.parsed_args[key]
