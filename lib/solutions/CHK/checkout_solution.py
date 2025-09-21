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


@dataclass(frozen=True)
class FreeOffer:
    code: str
    quantity: int


@dataclass
class SpecialOffer:
    price: int
    quantity: int
    free_offer: FreeOffer = None



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
    a_cost: int = get_cost_for_code(amounts_dict["A"],
                                    [
                                        SpecialOffer(A_FIVE_PRICE, 5),
                                        SpecialOffer(A_THREE_PRICE, 3),
                                        SpecialOffer(A_PRICE, 1)
                                    ])
    b_cost: int = get_cost_for_code(amounts_dict["B"] - (amounts_dict["E"] // 2),
                                    [
                                        SpecialOffer(price=F_THREE_PRICE, quantity=3),
                                        SpecialOffer(price=F_PRICE, quantity=1)
                                    ])
    c_cost: int = get_cost_for_code(amounts_dict["C"],
                                    [SpecialOffer(price=C_PRICE, quantity=1)])
    d_cost: int = get_cost_for_code(amounts_dict["D"],
                                    [SpecialOffer(price=D_PRICE, quantity=1)])
    e_cost: int = get_cost_for_code(amounts_dict["E"],
                                    [SpecialOffer(price=E_PRICE, quantity=1)])
    f_cost: int = get_cost_for_code(amounts_dict["F"],
                                    [
                                        SpecialOffer(price=F_THREE_PRICE, quantity=3),
                                        SpecialOffer(price=F_PRICE, quantity=1)
                                    ])

    return a_cost + b_cost + c_cost + d_cost + e_cost + f_cost


def get_a_cost(no_of_a: int) -> int:
    return get_cost_for_code(no_of_a, [
        SpecialOffer(A_FIVE_PRICE, 5),
        SpecialOffer(A_THREE_PRICE, 3),
        SpecialOffer(A_PRICE, 1),
    ])


def get_b_cost(no_of_b: int, no_of_e: int):
    no_of_free_b = no_of_e // 2
    b_to_pay = no_of_b - no_of_free_b
    return get_cost_for_code(b_to_pay, [
        SpecialOffer(B_SPECIAL_PAIR_PRICE, 2),
        SpecialOffer(B_PRICE, 1)
    ])


def get_f_cost(no_of_f: int) -> int:
    return get_cost_for_code(no_of_f,
                             [
                                 SpecialOffer(price=F_THREE_PRICE, quantity=3),
                                 SpecialOffer(price=F_PRICE, quantity=1)
                             ])





# assume special prizes list sorted descending amount order
def get_cost_for_code(amount: int, special_prices: list[SpecialOffer]):
    total_cost = 0
    if amount <= 0:
        return total_cost
    left_to_pay = amount
    for special_price in special_prices:
        amount_at_price = left_to_pay // special_price.quantity
        cost = amount_at_price * special_price.price
        left_to_pay = left_to_pay % special_price.quantity
        total_cost += cost
    return total_cost

