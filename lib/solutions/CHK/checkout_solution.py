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

        units = get_units(skus)
        print(f"units = {units}")
        if len(units) == 0:
            return -1

        # noOfA = re.
        return 0


def get_a(units: list[str]):
    a_reg = r"\d+A"
    units_of_a = [unit for unit in units if re.match(a_reg, unit)]
    for unit in units:
        match = re.match(a_reg, unit)
        if match:
            print(f"unit = {unit}")
            print(f"match = {match}")
            number = re.sub(unit, "A", '')
            print(f"number = {number}")
    return units_of_a


# my regex is wrong
def get_units(skus: str) -> list[str]:
    regex = r"(\d+[ABCD])"
    units = re.findall(regex, skus)
    print(f"type units = {type(units)}")
    return units


