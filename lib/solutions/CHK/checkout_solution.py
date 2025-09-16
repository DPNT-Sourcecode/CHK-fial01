import re

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1

        regex = r"(\d+[ABCD]){1,4}"

