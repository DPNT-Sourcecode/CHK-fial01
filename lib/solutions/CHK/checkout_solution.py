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

        regex = r"(\d+[ABCD]){1,4}"
        units = re.findall(regex, skus)
        print(f"units = {units}")
        if len(units) == 0:
            return -1

        # noOfA = re.
        return 0