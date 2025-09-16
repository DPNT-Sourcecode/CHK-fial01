import re

# Assuming input format is such that each item is represented once
# with a number then the item code.
# i.e. no repetitions
# does every item have to be represented? Guessing no.
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1

        units = get_units_list(skus)
        print(f"units = {units}")
        if len(units) == 0:
            return -1

        try:
            amounts_dict = get_amounts(units)
        except ValueError:
            return -1
        return get_cost(amounts_dict)


def get_cost(amounts_dict: dict[str, int]) -> int:
    a_price: int = 50
    b_price: int = 30
    c_price: int = 20
    d_price: int = 15
    a_special_price: int = 130
    b_special_price: int = 45
    c_cost: int = amounts_dict["C"] * c_price
    d_cost: int = amounts_dict["D"] * d_price
    a_cost = (amounts_dict["A"] // 3) * a_special_price + (amounts_dict["A"] % 3) * a_price
    b_cost = (amounts_dict["A"] // 2) * b_special_price + (amounts_dict["A"] % 2) * b_price
    return a_cost + b_cost + c_cost + d_cost




def get_amounts(units: list[str]) -> dict[str, int]:
    a_amounts = get_a(units)
    b_amounts = get_b(units)
    c_amounts = get_c(units)
    d_amounts = get_d(units)
    if len(a_amounts) > 1 or len(b_amounts) > 1 or len(c_amounts) > 1 or len(d_amounts) > 1:
        raise ValueError("duplicate units")
    a_amount = a_amounts[0] if len(a_amounts) > 0 else 0
    b_amount = b_amounts[0] if len(b_amounts) > 0 else 0
    c_amount = c_amounts[0] if len(c_amounts) > 0 else 0
    d_amount = d_amounts[0] if len(d_amounts) > 0 else 0
    return dict(A=a_amount, B=b_amount, C=c_amount, D=d_amount)


# brute force
def get_a(units: list[str]) -> list[int]:
    a_reg = r"\d+A"
    return [int(unit.replace("A", "")) for unit in units if re.match(a_reg, unit)]


def get_b(units: list[str]) -> list[int]:
    reg = r"\d+B"
    return [int(unit.replace("B", "")) for unit in units if re.match(reg, unit)]


def get_c(units: list[str]) -> list[int]:
    reg = r"\d+C"
    return [int(unit.replace("C", "")) for unit in units if re.match(reg, unit)]


def get_d(units: list[str]) -> list[int]:
    reg = r"\d+D"
    return [int(unit.replace("D", "")) for unit in units if re.match(reg, unit)]


def get_units_list(skus: str) -> list[str]:
    regex = r"(\d+[ABCD])"
    units = re.findall(regex, skus)
    print(f"type units = {type(units)}")
    return units
