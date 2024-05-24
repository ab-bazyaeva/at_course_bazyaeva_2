# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import time
import pytest


@pytest.fixture(scope="class")
def class_timestamp():
    start_time = time.time()
    yield "Started at " + time.ctime(start_time)
    end_time = time.time()
    print("\nFinished at " + time.ctime(end_time))
