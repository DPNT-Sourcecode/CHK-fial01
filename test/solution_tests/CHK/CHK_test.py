from solutions.CHK.checkout_solution import CheckoutSolution


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
