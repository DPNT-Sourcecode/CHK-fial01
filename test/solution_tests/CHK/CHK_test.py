from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.checkout_solution import get_a
from solutions.CHK.checkout_solution import get_units


# What's the input format?
def test_checkout_missing_quantity():
    result = CheckoutSolution().checkout("A")
    assert result == -1


def test_checkout_invalid_input():
    result = CheckoutSolution().checkout(12)
    assert result == -1


def test_checkout_repeated_sku():
    result = CheckoutSolution().checkout("1A2B6A")
    assert result == -1


def test_get_units():
    get_units("3A") == ["3A"]
    get_units("3A5B") == ["3A", "5B"]

