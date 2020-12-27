from typing import Tuple

import pytest

import main


@pytest.fixture(params=[
    (0, 0, None),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
    (2, 3, 1),
    (3, 2, 1),
    (100, 10, 10),
    (35, 42, 7),
    (99, 100, 1),
    (100000, 100001, 1),
])
def a_and_b_and_gcd(request) -> Tuple[int, int, int]:
    return request.param


def test_gcd(a_and_b_and_gcd: Tuple[int, int, int]):
    a, b, gcd = a_and_b_and_gcd
    gen = main.FractionGenerator()

    assert gen.gcd(a, b) == gcd
