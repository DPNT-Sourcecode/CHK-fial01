from lib.solutions.SUM.sum_solution import SumSolution
import pytest


@pytest.mark.parametrize("input_x, input_y, output", [(1, 2, 3), (47, 22, 69), (0, 12, 12), (71, 44, 115),
                                                      (7, 100, 107)])
def test_sum(input_x, input_y, output):
    assert SumSolution().compute(input_x, input_y) == output


@pytest.mark.parametrize("input_x, input_y", [(-1, 2), (-10, -11), (18, -9), (105, 4), (105, 204), (14, 341)])
def test_sum_out_of_bounds(input_x, input_y):
    with pytest.raises(ValueError):
        SumSolution().compute(input_x, input_y)


