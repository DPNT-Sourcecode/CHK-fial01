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

        units: list[str] = get_units_list(skus)
        if len(units) == 0:
            return -1

        try:
            amounts_dict: dict[str, int] = get_amounts(units)
        except ValueError:
            return -1
        return get_cost(amounts_dict)


def get_units_list(skus: str) -> list[str]:
    regex = r"(\d+[ABCD])"
    units = re.findall(regex, skus)
    return units


def get_amounts(units: list[str]) -> dict[str, int]:
    a_amounts = get_a_amounts(units)
    b_amounts = get_b_amounts(units)
    c_amounts = get_c_amounts(units)
    d_amounts = get_d_amounts(units)
    if len(a_amounts) > 1 or len(b_amounts) > 1 or len(c_amounts) > 1 or len(d_amounts) > 1:
        raise ValueError("duplicate units")
    a_amount = a_amounts[0] if len(a_amounts) > 0 else 0
    b_amount = b_amounts[0] if len(b_amounts) > 0 else 0
    c_amount = c_amounts[0] if len(c_amounts) > 0 else 0
    d_amount = d_amounts[0] if len(d_amounts) > 0 else 0
    return dict(A=a_amount, B=b_amount, C=c_amount, D=d_amount)


# for a larger list would combine these methods
def get_a_amounts(units: list[str]) -> list[int]:
    a_reg = r"\d+A"
    return [int(unit.replace("A", "")) for unit in units if re.match(a_reg, unit)]


def get_b_amounts(units: list[str]) -> list[int]:
    reg = r"\d+B"
    return [int(unit.replace("B", "")) for unit in units if re.match(reg, unit)]


def get_c_amounts(units: list[str]) -> list[int]:
    reg = r"\d+C"
    return [int(unit.replace("C", "")) for unit in units if re.match(reg, unit)]


def get_d_amounts(units: list[str]) -> list[int]:
    reg = r"\d+D"
    return [int(unit.replace("D", "")) for unit in units if re.match(reg, unit)]


def get_cost(amounts_dict: dict[str, int]) -> int:
    c_cost: int = amounts_dict["C"] * C_PRICE
    d_cost: int = amounts_dict["D"] * D_PRICE
    a_cost = (amounts_dict["A"] // 3) * A_SPECIAL_PRICE + (amounts_dict["A"] % 3) * A_PRICE
    b_cost = (amounts_dict["B"] // 2) * B_SPECIAL_PRICE + (amounts_dict["B"] % 2) * B_PRICE
    return a_cost + b_cost + c_cost + d_cost