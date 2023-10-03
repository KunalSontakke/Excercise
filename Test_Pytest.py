import pytest
import math


def test_compare_1():
    num = 25
    assert math.sqrt(num) == 5


def test_compare_2():
    a = 1
    b = 2
    assert a + b == 5


def test_3():
    stri = "Hi,My name is kunal"
    assert "kunal" in stri


@pytest.fixture
def input_value():
    input = 39
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_5(input_value):
    assert input_value % 3 == 0


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11 * num == output
