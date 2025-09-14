from lib.solutions.SUM.sum_solution import SumSolution
import pytest


@pytest.mark.parametrize("inputX, inputY,inputZ")
def test_sum():
    assert SumSolution().compute(1, 2) == 3


def test_sum_out_of_bounds():
    with pytest.raises(ValueError):
        SumSolution().compute(-1, 1)


