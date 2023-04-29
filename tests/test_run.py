import subprocess

from photov.const import ABSPATH


def run_module(args: list[str] = None):
    path = f'python {ABSPATH}'

    if args:
        path = path + ' ' + ' '.join(args)

    process = subprocess.run(path, capture_output=True, text=True, shell=True)
    return process.returncode


def test_module_runs_via_console():
    exit_code = run_module([])
    assert exit_code == 0
