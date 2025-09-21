import re

A_PRICE: int = 50
B_PRICE: int = 30
C_PRICE: int = 20
D_PRICE: int = 15
A_THREE_PRICE: int = 130  # 3A for 130
A_FIVE_PRICE: int = 150  # 3A for 150
B_SPECIAL_PRICE: int = 45   # 2B for 45


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
    invalid_match = re.search(r"[^ABCD]", skus)
    if invalid_match is not None:
        raise ValueError
    return dict(A=len(a_codes), B=len(b_codes), C=len(c_codes), D=len(d_codes))


def get_cost(amounts_dict: dict[str, int]) -> int:
    c_cost: int = amounts_dict["C"] * C_PRICE
    d_cost: int = amounts_dict["D"] * D_PRICE
    a_cost = (amounts_dict["A"] // 5) * A_FIVE_PRICE + (amounts_dict["A"] % 5) * A_PRICE

    b_cost = (amounts_dict["B"] // 2) * B_SPECIAL_PRICE + (amounts_dict["B"] % 2) * B_PRICE
    return a_cost + b_cost + c_cost + d_cost


# Could there be cases where it's cheaper to break the last 5 into more threes?
# consider no_of_a = 6. Either 150 + 50 = 200 or 130*2 = 260
def calculate_naive_a_cost(no_of_a: int) -> int:
    no_of_fives = no_of_a // 5
    remainder_from_fives = no_of_a % 5
    no_of_threes_in_remainder = remainder_from_fives // 3
    remainder_of_remainder = remainder_from_fives % 3
    return (no_of_fives * A_FIVE_PRICE +
            no_of_threes_in_remainder * A_THREE_PRICE +
            remainder_of_remainder * A_PRICE)
