from solutions.CHK.checkout_solution import get_cost_for_stxyz
from solutions.CHK.checkout_solution import remove_items_used_in_offers

S_PRICE: int = 20
T_PRICE: int = 20
X_PRICE: int = 17
Y_PRICE: int = 20
Z_PRICE: int = 21
S_T_X_Y_Z_THREE_PRICE: int = 45


def test_get_cost_for_stxyz():
    input = {"S": 3, "T": 1, "X": 2, "Y": 1, "Z": 0}
    assert get_cost_for_stxyz(input) == 107


def test_remove_items_used_in_offers():
    input = {"S": 3, "T": 1, "X": 2, "Y": 1, "Z": 0}
    assert (remove_items_used_in_offers(input) ==
            {"S": 0, "T": 0, "X": 1, "Y": 0, "Z": 0})
