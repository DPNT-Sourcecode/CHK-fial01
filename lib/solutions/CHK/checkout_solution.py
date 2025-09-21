import re
import string
from dataclasses import dataclass

A_PRICE: int = 50
B_PRICE: int = 30
C_PRICE: int = 20
D_PRICE: int = 15
E_PRICE: int = 40
F_PRICE: int = 10
A_THREE_PRICE: int = 130  # 3A for 130
A_FIVE_PRICE: int = 200  # 5A for 200
B_SPECIAL_PAIR_PRICE: int = 45  # 2B for 45
F_THREE_PRICE: int = 20  # 3F for 20


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1

        try:
            amounts_dict: dict[str, int] = get_amounts(skus)
        except ValueError:
            return -1
        return get_cost(amounts_dict)


def get_amounts(skus: str) -> dict[str, int]:
    invalid_match = re.search(r"[^A-Z]", skus)
    if invalid_match is not None:
        raise ValueError
    codes_dict = {}
    for letter in string.ascii_uppercase:
        codes_dict[letter] = 0
    for c in skus:
        if c not in codes_dict.keys():
            raise ValueError(f"Item with code: {c} does not match expected "
                             f"codes: {codes_dict.keys()}")
        codes_dict[c] += 1
    return codes_dict


def get_cost(amounts_dict: dict[str, int]) -> int:
    a_cost: int = get_cost_for_code(amounts_dict["A"], [
        SpecialPrice(A_FIVE_PRICE, 5),
        SpecialPrice(A_THREE_PRICE, 3),
        SpecialPrice(A_PRICE, 1),
    ])
    b_cost: int = get_b_cost(amounts_dict["B"], amounts_dict["E"])
    c_cost: int = get_cost_for_code(amounts_dict["C"],
                                    [SpecialPrice(price=C_PRICE, quantity=1)])
    d_cost: int = get_cost_for_code(amounts_dict["D"],
                                    [SpecialPrice(price=D_PRICE, quantity=1)])
    e_cost: int = get_cost_for_code(amounts_dict["E"],
                                    [SpecialPrice(price=E_PRICE, quantity=1)])
    f_cost: int = get_cost_for_code(amounts_dict["F"],
                                    [
                                        SpecialPrice(price=F_THREE_PRICE, quantity=3),
                                        SpecialPrice(price=F_PRICE, quantity=1)
                                    ])

    return a_cost + b_cost + c_cost + d_cost + e_cost + f_cost


def get_a_cost(no_of_a: int) -> int:
    return get_cost_for_code(no_of_a, [
        SpecialPrice(A_FIVE_PRICE, 5),
        SpecialPrice(A_THREE_PRICE, 3),
        SpecialPrice(A_PRICE, 1),
    ])


def get_b_cost(no_of_b: int, no_of_e: int):
    no_of_free_b = no_of_e // 2
    b_to_pay = no_of_b - no_of_free_b
    if b_to_pay <= 0:
        return 0
    return get_cost_for_code(b_to_pay, [
        SpecialPrice(B_SPECIAL_PAIR_PRICE, 2),
        SpecialPrice(B_PRICE, 1)
    ])


def get_f_cost(no_of_f: int) -> int:
    return get_cost_for_code(no_of_f,
                             [
                                 SpecialPrice(price=F_THREE_PRICE, quantity=3),
                                 SpecialPrice(price=F_PRICE, quantity=1)
                             ])


@dataclass(frozen=True)
class SpecialPrice:
    price: int
    quantity: int


# assume special prizes list sorted descending amount order
def get_cost_for_code(amount: int, special_prices: list[SpecialPrice]):
    left_to_pay = amount
    total_cost = 0
    for special_price in special_prices:
        amount_at_price = left_to_pay // special_price.quantity
        cost = amount_at_price * special_price.price
        left_to_pay = left_to_pay % special_price.quantity
        total_cost += cost
    return total_cost


