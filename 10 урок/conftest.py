# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import time
import pytest

# Вторая попытка


@pytest.fixture(scope="class")
def class_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


@pytest.fixture()
def test_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class TestClass:
    @classmethod
    def setup_class(cls):
        cls.class_timestamp = test_timestamp()
        print(f"Class {cls.__name__} started at {cls.class_timestamp}")

    @classmethod
    def teardown_class(cls):
        cls.class_timestamp = class_timestamp
        print(f"Class {cls.__name__} finished at {cls.class_timestamp}")

    def test_example(self, test_timestamp):
        print(f"Test {self.test_example.__name__} started at {test_timestamp}")
        assert True
        print(f"Test {self.test_example.__name__} finished at {test_timestamp}")


def pytest_runtest_setup(item, test_timestamp):
    print(f"Test {item.name} started at {test_timestamp}")


def pytest_runtest_teardown(item, test_timestamp):
    print(f"Test {item.name} finished at {test_timestamp}")


# Первая попытка всё ниже
# @pytest.fixture(scope="class")
# def class_timestamp():
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# @pytest.fixture()
# def test_timestamp():
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# class TestClass:
#     @classmethod
#     def setup_class(cls, class_timestamp):
#         cls.class_timestamp = class_timestamp
#         print(f"Class {cls.__name__} started at {cls.class_timestamp}")
#
#     @classmethod
#     def teardown_class(cls):
#         print(f"Class {cls.__name__} finished at {cls.class_timestamp}")
#
#     def test_example(self, test_timestamp):
#         print(f"Test {self.test_example.__name__} started at {test_timestamp}")
#         assert True
#
#         print(f"Test {self.test_example.__name__} finished at {test_timestamp}")
# # def pytest_class_setup(cls, class_timestamp):
# #     print(f"Class {cls.__name__} started at {class_timestamp}")
# #
# # def pytest_class_teardown(cls, class_timestamp):
# #     print(f"Class {cls.__name__} finished at {class_timestamp}")
#
# # --Текст НИЖЕ был изначально
# # def pytest_runtest_setup(item, test_timestamp):
# #     print(f"Test {item.name} started at {test_timestamp}")
# #
# # def pytest_runtest_teardown(item, test_timestamp):
# #     print(f"Test {item.name} finished at {test_timestamp}")
# # --Текст ВЫШЕ был изначально
#
# def pytest_runtest_setup(item):
#     # test_timestamp = item.getfuncargvalue("test_timestamp")
#     test_timestamp = item.funcargs['test_timestamp']
#     print(f"Test {item.name} started at {test_timestamp}")
#
# def pytest_runtest_teardown(item):
#     test_timestamp = item.getfuncargvalue("test_timestamp")
#     print(f"Test {item.name} finished at {test_timestamp}")