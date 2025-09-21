import pytest

from solutions.CHK.checkout_solution import calculate_naive_a_cost
from solutions.CHK.checkout_solution import get_a_cost


def test_get_a_naive_cost():
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
    assert calculate_naive_a_cost(14) == 480
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
    assert get_a_cost(14) == 480
    assert get_a_cost(15) == 450

