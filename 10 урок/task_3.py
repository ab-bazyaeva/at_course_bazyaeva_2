# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните


import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize("args, expected, smoke, skip", [
    ((10, 2, 5), 1, True, False),  # smoke-тест
    ((10,), 10, False, False),
    ((100, 2, 2, 5, 5), 1, False, False),
    ((10, 0), None, False, True),  # пропущен
    ((), None, False, False),
])
def test_all_division(args, expected, smoke, skip):
    if skip:
        pytest.skip("Тест пропущен")
    if expected is not None:
        assert all_division(*args) == expected
    else:
        with pytest.raises(ZeroDivisionError if args else TypeError):
            all_division(*args)





