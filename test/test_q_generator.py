from typing import List, Tuple

import pytest

import main


def test_return_type(n: int):
    gen = main.q_generator()

    for i in range(n):
        res = next(gen)
        assert isinstance(res, tuple)
        assert len(res) == 2
        assert isinstance(res[0], int)
        assert isinstance(res[1], int)


def test_consistent_return(n: int):
    gen1 = main.q_generator()
    gen2 = main.q_generator()

    for i in range(n):
        assert next(gen1) == next(gen2)


def test_correct_return(n_101: List[Tuple[int, int]]):
    gen = main.q_generator()

    assert n_101 == [next(gen) for i in range(101)]
