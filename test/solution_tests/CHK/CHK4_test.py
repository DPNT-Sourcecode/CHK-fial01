from solutions.CHK.checkout_solution import get_a_cost
from solutions.CHK.checkout_solution import get_amounts
from solutions.CHK.checkout_solution import get_b_cost
from solutions.CHK.checkout_solution import get_cost
from solutions.CHK.checkout_solution import get_f_cost

empty_amounts_dict = dict(A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0, I=0, J=0, K=0, L=0,
                          M=0, N=0, O=0, P=0, Q=0, R=0, S=0, T=0, U=0, V=0, W=0, X=0,
                          Y=0, Z=0)

upper_alphabet = {chr(letter) for letter in range(ord('A'), ord('Z') + 1)}


def test_test_data():
    assert empty_amounts_dict.keys() == upper_alphabet


def test_get_amounts():
    input = "AABFCCEDAEFG"
    expected = empty_amounts_dict.copy()
    expected["A"] = 3
    expected["B"] = 1
    expected["C"] = 2
    expected["D"] = 1
    expected["E"] = 2
    expected["F"] = 2
    expected["G"] = 1
    assert expected == get_amounts(input)


def test_get_amounts_empty():
        assert get_amounts("") == empty_amounts_dict


def test_get_cost():
    amounts = empty_amounts_dict.copy()
    amounts["A"] = 4
    amounts["B"] = 3
    amounts["C"] = 1
    amounts["D"] = 1
    amounts["E"] = 2
    amounts["F"] = 3
    assert get_cost(amounts) == 360
    amounts_2 = empty_amounts_dict.copy()
    amounts_2["A"] = 4
    amounts_2["B"] = 0
    amounts_2["C"] = 1
    amounts_2["D"] = 1
    amounts_2["E"] = 2
    amounts_2["F"] = 2
    assert get_cost(amounts_2) == 315


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
    assert get_b_cost(dict(B=1, E=0)) == 30
    assert get_b_cost(dict(B=2, E=0)) == 45
    assert get_b_cost(dict(B=3, E=0)) == 75
    assert get_b_cost(dict(B=4, E=0)) == 90
    assert get_b_cost(dict(B=5, E=0)) == 120
    assert get_b_cost(dict(B=6, E=0)) == 135
    # e = 1
    assert get_b_cost(dict(B=1, E=1)) == 30
    assert get_b_cost(dict(B=2, E=1)) == 45
    assert get_b_cost(dict(B=3, E=1)) == 75
    assert get_b_cost(dict(B=4, E=1)) == 90
    assert get_b_cost(dict(B=5, E=1)) == 120
    assert get_b_cost(dict(B=6, E=1)) == 135
    # e = 2
    assert get_b_cost(dict(B=1, E=2)) == 0
    assert get_b_cost(dict(B=2, E=2)) == 30
    assert get_b_cost(dict(B=3, E=2)) == 45
    assert get_b_cost(dict(B=4, E=2)) == 75
    assert get_b_cost(dict(B=5, E=2)) == 90
    assert get_b_cost(dict(B=6, E=2)) == 120
    # e = 3
    assert get_b_cost(dict(B=1, E=3)) == 0
    assert get_b_cost(dict(B=2, E=3)) == 30
    assert get_b_cost(dict(B=3, E=3)) == 45
    assert get_b_cost(dict(B=4, E=3)) == 75
    assert get_b_cost(dict(B=5, E=3)) == 90
    assert get_b_cost(dict(B=6, E=3)) == 120
    # e = 4
    assert get_b_cost(dict(B=1, E=4)) == 0
    assert get_b_cost(dict(B=2, E=4)) == 0
    assert get_b_cost(dict(B=3, E=4)) == 30
    assert get_b_cost(dict(B=4, E=4)) == 45
    assert get_b_cost(dict(B=5, E=4)) == 75
    assert get_b_cost(dict(B=6, E=4)) == 90


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
