import pytest

from main import list_to_decimal


def test_numbers_with_leading_zeros():
    assert list_to_decimal([0, 4, 2, 8]) == 428


def test_two_regular_numbers():
    assert list_to_decimal([1, 2]) == 12


def test_one_regular_number():
    assert list_to_decimal([3]) == 3


def test_numbers_and_a_boolean():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])


def test_numbers_and_a_negative_number():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])


def test_float_numbers():
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 4, 1])


def test_strings_numbers():
    with pytest.raises(TypeError):
        list_to_decimal(['4', 5, 3, 1])


def test_numbers_and_a_long_number():
    with pytest.raises(ValueError):
        list_to_decimal([10])
