# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize("args, expected_result", [
    ((10, 2, 2), 2.5),  # This is the smoke test
    pytest.param((10, 5, 2), 1, marks=pytest.mark.skip),  # This test is skipped
    ((100, 10, 5), 2),
    ((1000, 10, 10, 5), 0.2),
])
def test_all_division(args, expected_result):
    assert all_division(*args) == expected_result





