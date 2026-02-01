import pytest
from list_manipulator import exchange
from list_manipulator import max_min_even_odd
from list_manipulator import first_last_even_odd


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
    assert exchange([], 0) == "Invalid index"


@pytest.mark.parametrize("lst, mode, category, expected", [
    ([1, 2, 3, 4, 5], "max", "even", 3),
    ([1, 2, 3, 4, 5], "min", "even", 1),
    ([1, 2, 3, 4, 5], "max", "odd", 4),
    ([1, 2, 3, 4, 5], "min", "odd", 0),
    ([1, 2, 3, 4, 4], "max", "even", 4),
    ([1, 2, 2, 4, 5], "min", "even", 2)
])
def test_max_min_even_odd_valid_cases(lst, mode, category, expected):
    assert max_min_even_odd(lst, mode, category) == expected


@pytest.mark.parametrize("lst, mode, category, expected", [
    ([1, 3, 5, 7, 9], "max", "even", "No matches"),
    ([2, 4, 6, 8, 10], "max", "odd", "No matches"),
    ([1, 3, 5, 7, 9], "min", "even", "No matches"),
    ([2, 4, 6, 8, 10], "min", "odd", "No matches"),
])
def test_max_min_even_odd_invalid_cases(lst, mode, category, expected):
    assert max_min_even_odd(lst, mode, category) == expected


@pytest.mark.parametrize("lst, command, expected", [
    ([1, 2, 3, 4, 5, 6], ["first", 0, "even"], []),
    ([1, 2, 3, 4, 5, 6], ["last", 0, "odd"], []),
    ([1, 3, 5], ["first", 2, "even"], []),
    ([2, 4, 6], ["last", 2, "odd"], []),
    ([1, 2, 3, 4, 5, 6], ["first", 2, "even"], [2, 4]),
    ([1, 2, 3, 4, 5, 6], ["last", 2, "even"], [4, 6]),
    ([1, 2, 3, 4, 5, 6], ["first", 2, "odd"], [1, 3]),
    ([1, 2, 3, 4, 5, 6], ["last", 2, "odd"], [3, 5]),
    ([1, 2, 3, 4, 5, 6], ["last", 4, "odd"], [1, 3, 5]),
    ([1, 2, 3, 4, 5, 6], ["first", 4, "even"], [2, 4, 6]),
])
def test_first_last_even_odd_valid_cases(lst, command, expected):
    assert first_last_even_odd(lst, command) == expected


@pytest.mark.parametrize("lst, command, expected", [
    ([1, 2, 3, 4], ["first", 5, "even"], "Invalid count"),
    ([1, 2, 3, 4], ["last", 5, "even"], "Invalid count"),
    ([1, 2, 3, 4], ["first", 5, "odd"], "Invalid count"),
    ([1, 2, 3, 4], ["last", 5,  "odd"], "Invalid count"),
])
def test_first_last_even_odd_invalid_cases(lst, command, expected):
    assert first_last_even_odd(lst, command) == expected
