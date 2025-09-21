from solutions.CHK.checkout_solution import calculate_naive_a_cost


def test_get_a_cost():
    assert calculate_naive_a_cost(3) == 130
    assert calculate_naive_a_cost(4) == 180  # whoops
    assert calculate_naive_a_cost(5) == 150
    assert calculate_naive_a_cost(6) == 200
    assert calculate_naive_a_cost(7) == 250
    assert calculate_naive_a_cost(8) == 280
    assert calculate_naive_a_cost(9) == 330  # whoops
    assert calculate_naive_a_cost(10) == 300