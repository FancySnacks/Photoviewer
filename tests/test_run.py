import subprocess

from photov.const import PATH


def run_module(args: list[str] = None):
    path = f'python {PATH}'

    if args:
        path = path + ' ' + ' '.join(args)

    process = subprocess.run(path, capture_output=True, text=True, shell=True)
    print(process.stderr)
    return process.returncode


def test_module_runs_via_console():
    exit_code = run_module(['-g'])
    assert exit_code == 0
