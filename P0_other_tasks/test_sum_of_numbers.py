from P0_other_tasks.sum_of_numbers import sum_of_numbers
import pytest


@pytest.mark.parametrize("numlist, nsum, result", [([1, 12, 5, 7, 3, 875, 343, 8, 43, 56, 6, 2, 10, 54],15,[(1, 4), (2, 12), (3, 7)]),
                                                  ([2.5, 3 , 678, 3, 5, 12, 7, 2.5, 11], 5, [(0, 7)]),
                                                  ([3, 6, 21, 67, 0, 2, 323, 665, 3, -4, 23, 0], -4, [(4,9), (9, 11)])
                                                  ])
def test_sum_of_numbers_positive(numlist, nsum, result):
    assert sum_of_numbers(numlist, nsum) == result


@pytest.mark.parametrize("expected_exemption, numlist, nsum", [(TypeError, [41, 52,4 ,67, 23, 67], '9'),
                                                              (TypeError, [4, '5', 67, 23, 67], '17'),
                                                              (TypeError, [14, '65', 607, 2, 627], 54),
                                                              (TypeError, [14, 65, 607, 2, 627], [(2, 4)]),
                                                              (TypeError, [92, 625, 0, 2, [(1, 6, 2)], 890, 2, -3, 2.5], 2)
                                                              ])
def test_sum_of_numbers_with_type_error(expected_exemption, numlist, nsum):
    with pytest.raises(TypeError):
        sum_of_numbers(numlist, nsum)
