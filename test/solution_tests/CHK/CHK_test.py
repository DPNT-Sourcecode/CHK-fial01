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
    assert get_amounts("sausage") == {"A": 0, "B": 0, "C": 0, "D": 0}


def test_get_amounts_invalid_input_raises_value_error():
    input = "AABCCDAFG"
    expected = {"A": 3, "B": 1, "C": 2, "D": 1}
    with pytest.raises(ValueError):
        assert get_amounts(input) == expected


def test_get_cost():
    input = {"A": 14, "B": 11, "C": 16, "D": 4}
    assert get_cost(input) == 1255


def test_checkout():
    input = "14A11B16C4D"
    assert CheckoutSolution().checkout(input) == 1255
    scrambled_input = "16C14A4D11B"
    assert CheckoutSolution().checkout(scrambled_input) == 1255
    input_without_A = "2B3C5D"
    assert CheckoutSolution().checkout(input_without_A) == 180
    input_with_zero_A = "2B3C5D0A"
    assert CheckoutSolution().checkout(input_with_zero_A) == 180


def test_checkout_invalid_input():
    result = CheckoutSolution().checkout(12)
    assert result == -1


def test_checkout_invalid_sku():
    result = CheckoutSolution().checkout("1A2B6A")
    assert result == -1




