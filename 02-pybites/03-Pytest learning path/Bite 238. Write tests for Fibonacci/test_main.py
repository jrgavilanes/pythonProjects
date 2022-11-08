import pytest

from main import fib


def test_positives_greater_1():
    assert fib(6) == 8


def test_fib_negatives():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_0_1():
    assert fib(0) == 0
    assert fib(1) == 1
