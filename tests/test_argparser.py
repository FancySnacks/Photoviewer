import pytest

from photov.arg_parser import ArgParser


@pytest.fixture
def argparser() -> ArgParser:
    return ArgParser([])


def test_parses_args():
    argv = ['-p.']
    argparser = ArgParser(argv)
    assert isinstance(argparser.parsed_args, dict)


@pytest.mark.parametrize("args, key, expected", [
    (['-p./resources/img'], 'path', './resources/img'),
    (['-t./test/img'], 'target', './test/img'),
])
def test_arg_parsing(args, key, expected):
    parser = ArgParser(args)
    assert parser.get_arg(key) == expected


def test_raises_exception_when_invalid_args():
    with pytest.raises(BaseException):
        ArgParser(['-n0'])
