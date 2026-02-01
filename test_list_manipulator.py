import pytest
from list_manipulator import exchange


@pytest.mark.parametrize("lst, index, expected", [
    ([1, 2, 3, 4, 5], 0, [2, 3, 4, 5, 1]),
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5], 4, [1, 2, 3, 4, 5]),
])
def test_exchange_valid_cases(lst, index, expected):
    assert exchange(lst, index) == expected


def test_exchange_negative_index():
    assert exchange([1, 2, 3, 3, 5], -2) == "Invalid index"


def test_exchange_index_out_of_range():
    assert exchange([1, 2, 3, 4, 5], 6) == "Invalid index"
