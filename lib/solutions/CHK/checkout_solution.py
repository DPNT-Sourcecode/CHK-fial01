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

        # noOfA = re.
        return 0


def get_a(units: list[str]):
    a_reg = r"\d+A"
    # check for value errors?
    units_of_a = [int(unit.replace("A", "")) for unit in units if re.match(a_reg, unit)]
    return units_of_a


def get_units_list(skus: str) -> list[str]:
    regex = r"(\d+[ABCD])"
    units = re.findall(regex, skus)
    print(f"type units = {type(units)}")
    return units





