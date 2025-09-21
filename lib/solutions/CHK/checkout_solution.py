import re

A_PRICE: int = 50
B_PRICE: int = 30
C_PRICE: int = 20
D_PRICE: int = 15
E_PRICE: int = 40
A_THREE_PRICE: int = 130  # 3A for 130
# FFS 200 not 150
A_FIVE_PRICE: int = 200  # 5A for 200
B_SPECIAL_PAIR_PRICE: int = 45   # 2B for 45
F_PRICE: int = 10
F_THREE_PRICE: int = 20


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
    a_codes = re.findall(r"A", skus)
    b_codes = re.findall(r"B", skus)
    c_codes = re.findall(r"C", skus)
    d_codes = re.findall(r"D", skus)
    e_codes = re.findall(r"E", skus)
    f_codes = re.findall(r"F", skus)
    invalid_match = re.search(r"[^ABCDEF]", skus)
    if invalid_match is not None:
        raise ValueError
    return dict(A=len(a_codes), B=len(b_codes), C=len(c_codes), D=len(d_codes), E=len(e_codes), F=len(f_codes))


def get_cost(amounts_dict: dict[str, int]) -> int:
    a_cost: int = get_a_cost(amounts_dict["A"])
    b_cost: int = get_b_cost(amounts_dict["B"], amounts_dict["E"])
    c_cost: int = amounts_dict["C"] * C_PRICE
    d_cost: int = amounts_dict["D"] * D_PRICE
    e_cost: int = amounts_dict["E"] * E_PRICE
    f_cost: int = amounts_dict["F"] * E_PRICE
    return a_cost + b_cost + c_cost + d_cost + e_cost + f_cost


def get_a_cost(no_of_a: int) -> int:
    no_of_fives = no_of_a // 5
    remainder_from_fives = no_of_a % 5
    no_of_threes_in_remainder = remainder_from_fives // 3
    remainder_of_remainder = remainder_from_fives % 3
    return (no_of_fives * A_FIVE_PRICE +
            no_of_threes_in_remainder * A_THREE_PRICE +
            remainder_of_remainder * A_PRICE)


def get_b_cost(no_of_b: int, no_of_e: int):
    no_of_free_b = no_of_e // 2
    b_to_pay = no_of_b - no_of_free_b
    if b_to_pay <= 0:
        return 0
    pairs_of_b = b_to_pay // 2
    single_b = b_to_pay % 2
    return pairs_of_b * B_SPECIAL_PAIR_PRICE + single_b * B_PRICE


def get_f_cost(no_of_f: int) -> int:
    no_of_threes = no_of_f // 3
    remainder = no_of_f % 3
    return no_of_threes * F_THREE_PRICE + remainder * F_PRICE

