import pytest

import main


def test_return_type(n: int):
    gen = main.FractionGenerator()

    for i in range(n):
        res = next(gen)
        assert isinstance(res, tuple)
        assert len(res) == 2
        assert isinstance(res[0], int)
        assert isinstance(res[1], int)


def test_consistent_return(n: int):
    gen1 = main.FractionGenerator()
    gen2 = main.FractionGenerator()

    for i in range(n):
        assert next(gen1) == next(gen2)


def test_correct_return():
    gen = main.FractionGenerator()
    res = [
        (0, 0), (1, 1), (-1, 1), (2, 1), (1, 2), (-2, 1), (-1, 2), (3, 1),
        (3, 2), (1, 3), (2, 3), (-3, 1), (-3, 2), (-1, 3), (-2, 3), (4, 1),
        (4, 3), (1, 4), (3, 4), (-4, 1), (-4, 3), (-1, 4), (-3, 4), (5, 1),
        (5, 2), (5, 3), (5, 4), (1, 5), (2, 5), (3, 5), (4, 5), (-5, 1),
        (-5, 2), (-5, 3), (-5, 4), (-1, 5), (-2, 5), (-3, 5), (-4, 5), (6, 1),
        (6, 5), (1, 6), (5, 6), (-6, 1), (-6, 5), (-1, 6), (-5, 6), (7, 1),
        (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (1, 7), (2, 7), (3, 7), (4, 7),
        (5, 7), (6, 7), (-7, 1), (-7, 2), (-7, 3), (-7, 4), (-7, 5), (-7, 6),
        (-1, 7), (-2, 7), (-3, 7), (-4, 7), (-5, 7), (-6, 7), (8, 1), (8, 3),
        (8, 5), (8, 7), (1, 8), (3, 8), (5, 8), (7, 8), (-8, 1), (-8, 3),
        (-8, 5), (-8, 7), (-1, 8), (-3, 8), (-5, 8), (-7, 8), (9, 1), (9, 2),
        (9, 4), (9, 5), (9, 7), (9, 8), (1, 9), (2, 9), (4, 9), (5, 9), (7, 9),
        (8, 9), (-9, 1), (-9, 2)
    ]
