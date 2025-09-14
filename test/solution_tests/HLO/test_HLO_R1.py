from solutions.HLO.hello_solution import HelloSolution


def test_hello():
    assert HelloSolution().hello("Sophie") == "Hello Sophie!"
