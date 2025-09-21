import pytest

from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.checkout_solution import get_amounts
from solutions.CHK.checkout_solution import get_cost


def test_get_amounts():
    input = "AABCCDA"
    expected = {"A": 3, "B": 1, "C": 2, "D": 1}
    assert get_amounts(input) == expected


def test_get_amounts_missing_code():
    input = "AACCDA"
    expected = {"A": 3, "B": 0, "C": 2, "D": 1}
    assert get_amounts(input) == expected


def test_get_amounts_empty():
    assert get_amounts("") == {"A": 0, "B": 0, "C": 0, "D": 0}


def test_get_amounts_invalid_input_raises_value_error():
    with pytest.raises(ValueError):
        get_amounts("AABCCDAFG")
        get_amounts("sausage")


def test_get_cost():
    input = {"A": 14, "B": 11, "C": 16, "D": 4}
    assert get_cost(input) == 1255


def test_checkout():
    assert CheckoutSolution().checkout("AABCABADCB") == 310
    assert CheckoutSolution().checkout("") == 0
    assert CheckoutSolution().checkout("ABCC") == 120
    assert CheckoutSolution().checkout("AAA") == 130


def test_checkout_invalid_input():
    assert CheckoutSolution().checkout("1A2B6A") == -1
    assert CheckoutSolution().checkout("aAA") == -1
    assert CheckoutSolution().checkout(12) == -1
    assert CheckoutSolution().checkout("carrotsA") == -1



