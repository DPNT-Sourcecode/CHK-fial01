import re
import string
from dataclasses import dataclass
from typing import Optional

A_PRICE: int = 50
B_PRICE: int = 30
C_PRICE: int = 20
D_PRICE: int = 15
E_PRICE: int = 40
F_PRICE: int = 10
G_PRICE: int = 20
H_PRICE: int = 10
I_PRICE: int = 35
J_PRICE: int = 60
K_PRICE: int = 70
L_PRICE: int = 90
M_PRICE: int = 15
N_PRICE: int = 40
O_PRICE: int = 10
P_PRICE: int = 50
Q_PRICE: int = 30
R_PRICE: int = 50
S_PRICE: int = 20
T_PRICE: int = 20
U_PRICE: int = 40
V_PRICE: int = 50
W_PRICE: int = 20
X_PRICE: int = 17
Y_PRICE: int = 20
Z_PRICE: int = 21
A_THREE_PRICE: int = 130  # 3A for 130
A_FIVE_PRICE: int = 200  # 5A for 200
B_PAIR_PRICE: int = 45  # 2B for 45
F_THREE_PRICE: int = 20  # 3F for 20
H_FIVE_PRICE: int = 45
H_TEN_PRICE: int = 80
K_TWO_PRICE: int = 120
P_FIVE_PRICE: int = 200
Q_THREE_PRICE: int = 80
U_FOUR_PRICE: int = 120
V_TWO_PRICE: int = 90
V_THREE_PRICE: int = 130
S_T_X_Y_Z_THREE_PRICE: int = 45


@dataclass(frozen=True)
class FreeOffer:
    code: str
    quantity: int


@dataclass
class SpecialPrice:
    price: int
    quantity: int


@dataclass
class SpecialOffer:
    code: str
    special_prices: list[SpecialPrice]
    free_offer: Optional[FreeOffer] = None


offers = dict(
    A=SpecialOffer(code="A", special_prices=[
        SpecialPrice(A_FIVE_PRICE, 5),
        SpecialPrice(A_THREE_PRICE, 3),
        SpecialPrice(A_PRICE, 1)
    ]),
    B=SpecialOffer(code="B", special_prices=[
        SpecialPrice(price=B_PAIR_PRICE, quantity=2),
        SpecialPrice(price=B_PRICE, quantity=1)
    ], free_offer=FreeOffer(code="E", quantity=2)),
    C=SpecialOffer(code="C", special_prices=[SpecialPrice(price=C_PRICE, quantity=1)]),
    D=SpecialOffer(code="D", special_prices=[SpecialPrice(price=D_PRICE, quantity=1)]),
    E=SpecialOffer(code="E", special_prices=[SpecialPrice(price=E_PRICE, quantity=1)]),
    F=SpecialOffer(code="F", special_prices=[
        SpecialPrice(price=F_THREE_PRICE, quantity=3),
        SpecialPrice(price=F_PRICE, quantity=1)
    ]),
    G=SpecialOffer(code="G", special_prices=[SpecialPrice(price=G_PRICE, quantity=1)]),
    H=SpecialOffer(code="H", special_prices=[
        SpecialPrice(price=H_TEN_PRICE, quantity=10),
        SpecialPrice(price=H_FIVE_PRICE, quantity=5),
        SpecialPrice(price=H_PRICE, quantity=1)
    ]),
    I=SpecialOffer(code="I", special_prices=[SpecialPrice(price=I_PRICE, quantity=1)]),
    J=SpecialOffer(code="J", special_prices=[SpecialPrice(price=J_PRICE, quantity=1)]),
    K=SpecialOffer(code="K", special_prices=[
        SpecialPrice(price=K_TWO_PRICE, quantity=2),
        SpecialPrice(price=K_PRICE, quantity=1)
    ]),
    L=SpecialOffer(code="L", special_prices=[SpecialPrice(price=L_PRICE, quantity=1)]),
    M=SpecialOffer(code="M", special_prices=[SpecialPrice(price=M_PRICE, quantity=1)],
                   free_offer=FreeOffer(code="N", quantity=3)),
    N=SpecialOffer(code="N", special_prices=[SpecialPrice(price=N_PRICE, quantity=1)]),
    O=SpecialOffer(code="O", special_prices=[SpecialPrice(price=O_PRICE, quantity=1)]),
    P=SpecialOffer(code="P", special_prices=[
        SpecialPrice(price=P_FIVE_PRICE, quantity=5),
        SpecialPrice(price=P_PRICE, quantity=1),
    ]),
    Q=SpecialOffer(code="Q",
                   special_prices=[
                       SpecialPrice(price=Q_THREE_PRICE, quantity=3),
                       SpecialPrice(price=Q_PRICE, quantity=1),
                   ],
                   free_offer=FreeOffer(code="R", quantity=3)
                   ),
    R=SpecialOffer(code="R", special_prices=[SpecialPrice(price=R_PRICE, quantity=1) ]),
    S=SpecialOffer(code="S", special_prices=[
        SpecialPrice(S_T_X_Y_Z_THREE_PRICE, quantity=3),
        SpecialPrice(price=S_PRICE, quantity=1),
    ]),
    T=SpecialOffer(code="T", special_prices=[
        SpecialPrice(S_T_X_Y_Z_THREE_PRICE, quantity=3),
        SpecialPrice(price=T_PRICE, quantity=1)
    ]),
    U=SpecialOffer(code="U", special_prices=[
        SpecialPrice(price=U_FOUR_PRICE, quantity=4),
        SpecialPrice(price=U_PRICE, quantity=1)
    ]),
    V=SpecialOffer(code="V", special_prices=[
        SpecialPrice(price=V_THREE_PRICE, quantity=3),
        SpecialPrice(price=V_TWO_PRICE, quantity=2),
        SpecialPrice(price=V_PRICE, quantity=1),
    ]),
    W=SpecialOffer(code="W", special_prices=[SpecialPrice(price=W_PRICE, quantity=1)]),
    X=SpecialOffer(code="X", special_prices=[
        SpecialPrice(S_T_X_Y_Z_THREE_PRICE, quantity=3),
        SpecialPrice(price=X_PRICE, quantity=1)
    ]),
    Y=SpecialOffer(code="Y", special_prices=[
        SpecialPrice(S_T_X_Y_Z_THREE_PRICE, quantity=3),
        SpecialPrice(price=Y_PRICE, quantity=1)
    ]),
    Z=SpecialOffer(code="Z", special_prices=[
        SpecialPrice(S_T_X_Y_Z_THREE_PRICE, quantity=3),
        SpecialPrice(price=Z_PRICE, quantity=1)
    ]),
)


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1

        try:
            amounts_dict: dict[str, int] = get_amounts(skus)
        except ValueError:
            return -1
        try:
            return get_cost(amounts_dict)
        except KeyError as e:
            print(f"keyError: {e} from get_cost on amounts_dict={amounts_dict}")
            return -1


def get_amounts(skus: str) -> dict[str, int]:
    invalid_match = re.search(r"[^A-Z]", skus)
    if invalid_match is not None:
        raise ValueError
    codes_dict = {}
    for letter in string.ascii_uppercase:
        codes_dict[letter] = 0
    for c in skus:
        if c not in codes_dict.keys():
            raise ValueError(f"Item with code: {c} does not match expected "
                             f"codes: {codes_dict.keys()}")
        codes_dict[c] += 1
    return codes_dict


def get_cost(amounts_dict: dict[str, int]) -> int:
    cost = 0
    for key in offers.keys():
        cost += get_cost_for_code(amounts_dict, offers[key])
    return cost


# assume special prices list sorted descending amount order
def get_cost_for_code(amounts_dict: dict[str, int], special_offer: SpecialOffer):
    total_cost = 0
    left_to_pay = amounts_dict[special_offer.code]
    free_offer = special_offer.free_offer
    if free_offer:
        left_to_pay = left_to_pay - amounts_dict[free_offer.code] // free_offer.quantity
    if left_to_pay <= 0:
        return total_cost
    for special_price in special_offer.special_prices:
        amount_at_price = left_to_pay // special_price.quantity
        cost = amount_at_price * special_price.price
        left_to_pay = left_to_pay % special_price.quantity
        total_cost += cost
    return total_cost


def get_cost_for_stxyz(amounts_dict):
    no_of_triples = (amounts_dict["S"] + amounts_dict["T"] + amounts_dict["X"]
                     + amounts_dict["Y"] + amounts_dict["Z"]) // 3
    cost_of_triples = no_of_triples * S_T_X_Y_Z_THREE_PRICE
    remainder = no_of_triples % 3
    return 0


def get_cheapest_remainder(amounts_dict):
    cost = 0
    no_of_triples = (amounts_dict["S"] + amounts_dict["T"] + amounts_dict["X"]
                     + amounts_dict["Y"] + amounts_dict["Z"]) // 3
    remainder = no_of_triples % 3
    remainder_of_non_x = remainder - amounts_dict["X"]
    if remainder > amounts_dict["X"]:
        cost = amounts_dict["X"] + X_PRICE
        remainder_of_non_x_non_z = (remainder_of_non_x - amounts_dict["S"]
                                    + amounts_dict["T"] + amounts_dict["Y"])
        if remainder_of_non_x_non_z > 0:
    else:
        return X_PRICE * remainder