from typing import Tuple

import pytest

import main


def test_return_type(n: int):
    res = main.bijection(n=n)

    assert isinstance(res, list)
    for t in res:
        assert isinstance(t, tuple)
        assert len(t) == 2
        assert isinstance(t[0], int)
        assert isinstance(t[1], int)


def test_bijective(n: int):
    res = main.bijection(n=n)

    assert len(res) == len(set(res)) == n + 1


def test_reimplementation(n: int):
    res = main.bijection(n=n)
    res_r = [i for i, _ in zip(main.QGenerater(), range(n))]
    for i, j in zip(res, res_r):
        assert i == j
