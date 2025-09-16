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
    assert get_units("3A") == ["3A"]
    assert get_units("3A5B") == ["3A", "5B"]
    assert get_units("1A2B6A") == ["1A", "2B", "6A"]


def test_get_a():
    assert get_a(["1A", "2B", "6A"]) == [1,6]



