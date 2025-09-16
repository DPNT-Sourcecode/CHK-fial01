from solutions.HLO.hello_solution import HelloSolution


def test_hello():
    output = HelloSolution().hello("Sophie")
    assert output == "Hello, Sophie!"
