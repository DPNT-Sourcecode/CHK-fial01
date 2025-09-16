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

        a = get_a(units)
        b = get_b(units)
        c = get_c(units)
        d = get_d(units)
        if len(a) > 1 or len(b) > 1 or len(c) > 1 or len(d) > 1:
            return -1
        return 0


# brute force
def get_a(units: list[str]):
    a_reg = r"\d+A"
    return [int(unit.replace("A", "")) for unit in units if re.match(a_reg, unit)]


def get_b(units: list[str]):
    reg = r"\d+B"
    return [int(unit.replace("B", "")) for unit in units if re.match(reg, unit)]


def get_c(units: list[str]):
    reg = r"\d+C"
    return [int(unit.replace("C", "")) for unit in units if re.match(reg, unit)]


def get_d(units: list[str]):
    reg = r"\d+D"
    return [int(unit.replace("D", "")) for unit in units if re.match(reg, unit)]


def get_units_list(skus: str) -> list[str]:
    regex = r"(\d+[ABCD])"
    units = re.findall(regex, skus)
    print(f"type units = {type(units)}")
    return units






