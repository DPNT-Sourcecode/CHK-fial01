from solutions.CHK.checkout_solution import get_amounts

empty_amounts_dict = dict(A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0, I=0, J=0, K=0, L=0,
                          M=0, N=0, O=0, P=0, Q=0, R=0, S=0, T=0, U=0, V=0, W=0, X=0,
                          Y=0, Z=0)

upper_alphabet = {chr(letter) for letter in range(ord('A'), ord('Z') + 1)}


def test_test_data():
    assert empty_amounts_dict.keys() == upper_alphabet


def test_get_amounts():
    input = "AABFCCEDAEFG"
    expected = empty_amounts_dict.copy()
    expected["A"] = 3
    expected["B"] = 1
    expected["C"] = 2
    expected["D"] = 1
    expected["E"] = 2
    expected["F"] = 2
    expected["G"] = 1
    assert expected == get_amounts(input)


def test_get_amounts_empty():
        assert get_amounts("") == empty_amounts_dict

