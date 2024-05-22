# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

import time
import pytest

@pytest.fixture(scope="class")
def class_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@pytest.fixture()
def test_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def pytest_class_setup(cls, class_timestamp):
    print(f"Class {cls.__name__} started at {class_timestamp}")

def pytest_class_teardown(cls, class_timestamp):
    print(f"Class {cls.__name__} finished at {class_timestamp}")

def pytest_runtest_setup(item, test_timestamp):
    print(f"Test {item.name} started at {test_timestamp}")

def pytest_runtest_teardown(item, test_timestamp):
    print(f"Test {item.name} finished at {test_timestamp}")