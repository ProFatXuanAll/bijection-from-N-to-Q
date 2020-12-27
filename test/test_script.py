from contextlib import redirect_stdout
from typing import List, Tuple

import main


def test_script(stdout_file_path: str):
    with open(stdout_file_path, 'w') as f:
        with redirect_stdout(f):
            main.main(['--n', '0'])

    with open(stdout_file_path, 'r') as f:
        assert f.read().strip() == '0/1'


def test_correct_return(
        stdout_file_path: str,
        n_101: List[Tuple[int, int]]
):
    for n in range(101):
        with open(stdout_file_path, 'w') as f:
            with redirect_stdout(f):
                main.main(['--n', str(n)])

        with open(stdout_file_path, 'r') as f:
            assert f.read().strip() == '/'.join(map(str, n_101[n]))


def test_correct_return_all(
        stdout_file_path: str,
        n_101: List[Tuple[int, int]]
):
    with open(stdout_file_path, 'w') as f:
        with redirect_stdout(f):
            main.main(['--n', str(100), '--all'])

    with open(stdout_file_path, 'r') as f:
        for n, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                continue
            assert line.strip() == '/'.join(map(str, n_101[n]))
