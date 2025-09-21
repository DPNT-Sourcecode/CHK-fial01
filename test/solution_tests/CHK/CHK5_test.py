from solutions.CHK.checkout_solution import get_cost
from solutions.CHK.checkout_solution import get_cost_for_stxyz
from solutions.CHK.checkout_solution import remove_items_used_in_offers

empty_amounts_dict = dict(A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0, I=0, J=0, K=0, L=0,
                          M=0, N=0, O=0, P=0, Q=0, R=0, S=0, T=0, U=0, V=0, W=0, X=0,
                          Y=0, Z=0)

def test_get_cost_for_stxyz():
    input = {"S": 3, "T": 1, "X": 2, "Y": 1, "Z": 0}
    assert get_cost_for_stxyz(input) == 107


def test_remove_items_used_in_offers():
    input = {"S": 3, "T": 1, "X": 2, "Y": 1, "Z": 0}
    assert (remove_items_used_in_offers(input) ==
            {"S": 0, "T": 0, "X": 1, "Y": 0, "Z": 0})


def test_get_cost():
    amounts = empty_amounts_dict.copy()
    amounts["A"] = 1  # 50
    amounts["B"] = 2  # 45
    amounts["S"] = 1  # 20
    amounts["T"] = 1  # 20
    amounts["X"] = 1  # 17
    amounts["Y"] = 1  # 20
    amounts["Z"] = 1  # 21
    assert get_cost(amounts) == 177
    # 50 + 45 + 45 + 17 + 20 = 177



