import pytest

from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.checkout_solution import get_a
from solutions.CHK.checkout_solution import get_amounts
from solutions.CHK.checkout_solution import get_units_list


def test_get_amounts():
    result = get_amounts(["14A", "0B", "16C"])


def test_get_amounts_raises_value_error():
    with pytest.raises(ValueError):
        get_amounts(["1A", "2B", "6A"])


def test_checkout_missing_quantity():
    result = CheckoutSolution().checkout("A")
    assert result == -1


def test_checkout_invalid_input():
    result = CheckoutSolution().checkout(12)
    assert result == -1


def test_checkout_repeated_sku():
    result = CheckoutSolution().checkout("1A2B6A")
    assert result == -1


def test_get_units_list():
    assert get_units_list("3A") == ["3A"]
    assert get_units_list("3A5B") == ["3A", "5B"]
    assert get_units_list("1A2B6A") == ["1A", "2B", "6A"]


def test_get_a():
    assert get_a(["1A", "2B", "6A"]) == [1, 6]


