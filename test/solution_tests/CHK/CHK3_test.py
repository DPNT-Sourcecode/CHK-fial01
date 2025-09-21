import pytest

from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.checkout_solution import get_a_cost
from solutions.CHK.checkout_solution import get_amounts
from solutions.CHK.checkout_solution import get_b_cost
from solutions.CHK.checkout_solution import get_cost
from solutions.CHK.checkout_solution import get_f_cost


def test_get_amounts():
    input = "AABFCCEDAEF"
    expected = {"A": 3, "B": 1, "C": 2, "D": 1, "E": 2, "F": 2}
    assert get_amounts(input) == expected


def test_get_amounts_missing_code():
    input = "AACCDA"
    expected = {"A": 3, "B": 0, "C": 2, "D": 1, "E": 0, "F": 0}
    assert get_amounts(input) == expected


def test_get_amounts_empty():
    assert get_amounts("") == {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}


def test_get_cost():
    input = {"A": 4, "B": 3, "C": 1, "D": 1, "E": 2, "F": 3}
    assert get_cost(input) == 360
    # 180 + 45 + 20 + 15 + 80 + 20 =
    input = {"A": 4, "B": 0, "C": 1, "D": 1, "E": 2, "F": 2}
    assert get_cost(input) == 285


def test_get_amounts_invalid_input_raises_value_error():
    with pytest.raises(ValueError):
        get_amounts("AABCCDAFGX")
        get_amounts("AABCCDAFG")
        get_amounts("sausage")


def test_get_f_cost():
    assert get_f_cost(1) == 10
    assert get_f_cost(2) == 20  # buy 2
    assert get_f_cost(3) == 20  # buy 2 get one free
    assert get_f_cost(4) == 30  # buy 3 get one free
    assert get_f_cost(5) == 40  # buy 4 get one free
    assert get_f_cost(6) == 40  # buy 4 get two free
    assert get_f_cost(7) == 50  # buy 5 get two free
    assert get_f_cost(8) == 60  # buy 6 get two fre
    assert get_f_cost(9) == 60  # buy 6 get three free
    assert get_f_cost(10) == 70  # buy 7 get three free
    assert get_f_cost(11) == 80  # buy 8 get three free
    assert get_f_cost(12) == 80  # buy 8 get four free


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
    assert get_a_cost(1) == 50
    assert get_a_cost(2) == 100
    assert get_a_cost(3) == 130
    assert get_a_cost(4) == 180  # whoops
    assert get_a_cost(5) == 200
    assert get_a_cost(6) == 250  # < 260
    assert get_a_cost(7) == 300
    assert get_a_cost(8) == 330
    assert get_a_cost(9) == 380  # whoops
    assert get_a_cost(10) == 400
    assert get_a_cost(11) == 450
    assert get_a_cost(12) == 500
    assert get_a_cost(13) == 530
    assert get_a_cost(14) == 580  # whoops
    assert get_a_cost(15) == 600


def test_checkout_invalid_input():
    assert CheckoutSolution().checkout("1A2B6A") == -1
    assert CheckoutSolution().checkout("aAA") == -1
    assert CheckoutSolution().checkout(12) == -1
    assert CheckoutSolution().checkout("carrotsA") == -1


def test_checkout():
    assert CheckoutSolution().checkout("AABCABADBEE") == 340
    assert CheckoutSolution().checkout("AACAADEE") == 295
    assert CheckoutSolution().checkout("") == 0
    assert CheckoutSolution().checkout("ABCC") == 120
    assert CheckoutSolution().checkout("AAA") == 130

