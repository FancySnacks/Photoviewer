from __future__ import annotations

import shutil
import pathlib
import os

from argparse import ArgumentParser, RawTextHelpFormatter, Action
from typing import Optional, Sequence, Any
from abc import ABC, abstractmethod

from photov.const import PATH
from photov.util import get_images_in_dir


class ArgParser:
    def __init__(self, args: Optional[Sequence[str]] | None, subparsers: list = None):
        self._parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
        self._subparsers: list[Subparser] = []

        self.setup()

        self.subparsers = self._parser.add_subparsers(
            description="Subparser Group", help=""
        )

        for subparser in subparsers:
            self.add_subparser(subparser)

        self.parsed_args = self._parser.parse_args(args)
        self.parsed_args: dict = vars(self.parsed_args)

        for subparser in self._subparsers:
            subparser.parse(self.parsed_args)

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

    def get_arg(self, key: str) -> Any:
        return self.parsed_args[key]

    def add_subparser(self, subparser):
        sub: Subparser = subparser(parent=self)
        new_parser = self.subparsers.add_parser(name=sub.name, help=sub.help)
        subparser.setup(self, new_parser)
        self._subparsers.append(sub)


class Subparser(ABC):
    def __init__(self, parent: ArgParser):
        self.parent: ArgParser = parent

        self.name: str = ""
        self.help: str = ""

    @abstractmethod
    def setup(self, parser_instance):
        pass


class MoveCopyParser(Subparser):
    def __init__(self, parent: ArgParser):
        super().__init__(parent)
        self.parent: ArgParser = parent

        self.name: str = "Select"
        self.help: str = (
            "-d / --date Select files by date\n"
            "-r / --regex Select files by regex pattern\n"
        )

    def setup(self, parser_instance):
        parser_instance.add_argument(
            "-d",
            "--date",
            help="Select files by date",
        )

        parser_instance.add_argument(
            "-r", "--regex", help="Select files by regex pattern"
        )

        parser_instance.add_argument(
            "-c",
            "--copy",
            action="store_const",
            const=True,
            default=False,
            help="Copy files to target dir",
        )

        parser_instance.add_argument(
            "-m",
            "--move",
            action="store_const",
            const=True,
            default=False,
            help="Move files to target dir",
        )

        parser_instance.add_argument(
            "-x",
            "--delete",
            action="store_const",
            const=True,
            default=False,
            help="Move files to target dir",
        )

    def parse(self, args):
        if args.get("copy"):
            path = args.get("path")
            target = args.get("target")
            img_files = get_images_in_dir(path)

            for im in img_files:
                shutil.copy(path + "\\" + im, target)

        if args.get("move"):
            path = args.get("path")
            target = args.get("target")
            img_files = args.get(path)

            for im in img_files:
                shutil.move(path + "\\" + im, target)

        if args.get("delete"):
            path = args.get("path")
            img_files = get_images_in_dir(path)

            for img in img_files:
                img_to_del = pathlib.Path.joinpath(pathlib.Path(path), pathlib.Path(img))
                os.remove(img_to_del)