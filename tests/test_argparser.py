import pytest

from photov.arg_parser import ArgParser


@pytest.fixture
def argparser() -> ArgParser:
    return ArgParser([])


def test_parses_args():
    argv = ['-p.']
    argparser = ArgParser(argv)
    assert isinstance(argparser.parsed_args, dict)


def test_parse_working_directory():
    target_dir = './resources/img'
    parser = ArgParser([f'-p{target_dir}'])
    assert parser.get_arg('path') == target_dir


def test_raises_exception_when_invalid_args():
    with pytest.raises(BaseException):
        ArgParser(['-n0'])
