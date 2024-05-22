# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

import pytest
from your_module import all_division  # replace 'your_module' with the actual name of your module

@pytest.mark.smoke
def test_all_division_simple():
    assert all_division(10, 2, 5) == 1

def test_all_division_single_arg():
    assert all_division(10) == 10

def test_all_division_many_args():
    assert all_division(100, 2, 2, 5, 5) == 1

def test_all_division_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

def test_all_division_no_args():
    with pytest.raises(TypeError):
        all_division()

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
