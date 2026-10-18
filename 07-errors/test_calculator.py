import pytest

from calculator import CalcError, calculate


def test_basic_operations():
    assert calculate("3 + 4") == 7
    assert calculate("10 - 2.5") == 7.5
    assert calculate("6 * 7") == 42
    assert calculate("9 / 3") == 3


def test_divide_by_zero():
    with pytest.raises(CalcError, match="divide by zero"):
        calculate("1 / 0")


def test_bad_number():
    with pytest.raises(CalcError, match="not a number"):
        calculate("one + 2")


def test_wrong_shape():
    with pytest.raises(CalcError, match="expected"):
        calculate("1 +")


def test_unknown_operator():
    with pytest.raises(CalcError, match="unknown operator"):
        calculate("2 ^ 3")
