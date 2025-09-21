import re

A_PRICE: int = 50
B_PRICE: int = 30
C_PRICE: int = 20
D_PRICE: int = 15
A_SPECIAL_PRICE: int = 130
B_SPECIAL_PRICE: int = 45

# well I fundamentally misunderstood the format..
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
    invalid = re.search(r"[^ABCD]")
    return dict(A=len(a_codes), B=len(b_codes), C=len(c_codes), D=len(d_codes))


def get_cost(amounts_dict: dict[str, int]) -> int:
    c_cost: int = amounts_dict["C"] * C_PRICE
    d_cost: int = amounts_dict["D"] * D_PRICE
    a_cost = (amounts_dict["A"] // 3) * A_SPECIAL_PRICE + (amounts_dict["A"] % 3) * A_PRICE
    b_cost = (amounts_dict["B"] // 2) * B_SPECIAL_PRICE + (amounts_dict["B"] % 2) * B_PRICE
    return a_cost + b_cost + c_cost + d_cost





