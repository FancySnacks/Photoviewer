import pathlib


def path_test(tmp_path, filename: str):
    path = pathlib.Path(tmp_path).joinpath(filename)
    return path
