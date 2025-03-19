import pytest
import math


def factorial_math(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    else:
        return math.factorial(n)


def test_factorial_zero():
    assert factorial_math(0) == 1


def test_factorial_one():
    assert factorial_math(1) == 1


def test_factorial_positive():
    assert factorial_math(5) == 120
    assert factorial_math(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial_math(-1)


def test_factorial_large():
    assert factorial_math(20) == 2432902008176640000


