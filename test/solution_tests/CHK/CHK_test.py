from solutions.CHK.checkout_solution import CheckoutSolution


# What's the input format?
def test_checkout():
    result = CheckoutSolution().checkout("A")
    assert result == 50


def test_checkout_invalid_input():
    result = CheckoutSolution().checkout(12)
    assert result == -1
