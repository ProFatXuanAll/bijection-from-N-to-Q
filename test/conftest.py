import pytest


@pytest.fixture(params=[1, 10, 100, 1000, 10000])
def n(request) -> int:
    return request.param
