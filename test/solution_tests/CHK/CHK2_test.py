import pytest

from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.checkout_solution import calculate_naive_a_cost
from solutions.CHK.checkout_solution import get_b_cost
from solutions.CHK.checkout_solution import get_a_cost
from solutions.CHK.checkout_solution import get_amounts
from solutions.CHK.checkout_solution import get_cost


def test_get_amounts():
    input = "AABCCEDAE"
    expected = {"A": 3, "B": 1, "C": 2, "D": 1, "E": 2}
    assert get_amounts(input) == expected


def test_get_amounts_missing_code():
    input = "AACCDA"
    expected = {"A": 3, "B": 0, "C": 2, "D": 1, "E": 0}
    assert get_amounts(input) == expected


def test_get_amounts_empty():
    assert get_amounts("") == {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}


def test_get_amounts_invalid_input_raises_value_error():
    with pytest.raises(ValueError):
        get_amounts("AABCCDAFG")
        get_amounts("sausage")


def test_get_cost():
    input = {"A": 4, "B": 3, "C": 1, "D": 1, "E": 2}
    assert get_cost(input) == 310
    # 150 + 0 + 20 + 15 + 80 = 265
    input = {"A": 4, "B": 0, "C": 1, "D": 1, "E": 2}


def test_get_b_naive_cost():
    # e = 0
    assert get_b_cost(1, 0) == 30
    assert get_b_cost(2, 0) == 45
    assert get_b_cost(3, 0) == 75
    assert get_b_cost(4, 0) == 90
    assert get_b_cost(5, 0) == 120
    assert get_b_cost(6, 0) == 135
    # e = 1
    assert get_b_cost(1, 1) == 30
    assert get_b_cost(2, 1) == 45
    assert get_b_cost(3, 1) == 75
    assert get_b_cost(4, 1) == 90
    assert get_b_cost(5, 1) == 120
    assert get_b_cost(6, 1) == 135
    # e = 2
    assert get_b_cost(1, 2) == 0
    assert get_b_cost(2, 2) == 30
    assert get_b_cost(3, 2) == 45
    assert get_b_cost(4, 2) == 75
    assert get_b_cost(5, 2) == 90
    assert get_b_cost(6, 2) == 120
    # e = 3
    assert get_b_cost(1, 3) == 0
    assert get_b_cost(2, 3) == 30
    assert get_b_cost(3, 3) == 45
    assert get_b_cost(4, 3) == 75
    assert get_b_cost(5, 3) == 90
    assert get_b_cost(6, 3) == 120
    # e = 4
    assert get_b_cost(1, 4) == 0
    assert get_b_cost(2, 4) == 0
    assert get_b_cost(3, 4) == 30
    assert get_b_cost(4, 4) == 45
    assert get_b_cost(5, 4) == 75
    assert get_b_cost(6, 4) == 90


def test_get_a_naive_cost():
    assert calculate_naive_a_cost(1) == 50
    assert calculate_naive_a_cost(2) == 100
    assert calculate_naive_a_cost(3) == 130
    assert calculate_naive_a_cost(4) == 180  # whoops
    assert calculate_naive_a_cost(5) == 150
    assert calculate_naive_a_cost(6) == 200  # < 260
    assert calculate_naive_a_cost(7) == 250
    assert calculate_naive_a_cost(8) == 280
    assert calculate_naive_a_cost(9) == 330  # whoops
    assert calculate_naive_a_cost(10) == 300
    assert calculate_naive_a_cost(11) == 350
    assert calculate_naive_a_cost(12) == 400
    assert calculate_naive_a_cost(13) == 430
    assert calculate_naive_a_cost(14) == 480  # whoops
    assert calculate_naive_a_cost(15) == 450


def test_get_a_cost():
    assert get_a_cost(3) == 130
    assert get_a_cost(4) == 150  # whoops
    assert get_a_cost(5) == 150
    assert get_a_cost(6) == 200  # < 260
    assert get_a_cost(7) == 250
    assert get_a_cost(8) == 280
    assert get_a_cost(9) == 300  # whoops
    assert get_a_cost(10) == 300
    assert get_a_cost(11) == 350
    assert get_a_cost(12) == 400
    assert get_a_cost(13) == 430
    assert get_a_cost(14) == 450
    assert get_a_cost(15) == 450


def test_checkout_invalid_input():
    assert CheckoutSolution().checkout("1A2B6A") == -1
    assert CheckoutSolution().checkout("aAA") == -1
    assert CheckoutSolution().checkout(12) == -1
    assert CheckoutSolution().checkout("carrotsA") == -1


def test_checkout():
    assert CheckoutSolution().checkout("AABCABADBEE") == 310
    assert CheckoutSolution().checkout("AACAADEE") == 265
    assert CheckoutSolution().checkout("") == 0
    assert CheckoutSolution().checkout("ABCC") == 120
    assert CheckoutSolution().checkout("AAA") == 130