import pytest
from src import calculator


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(10, 100) == 110


def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(10, 100) == -90


def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(10, 100) == 1000


def test_divide():
    assert calculator.divide(2, 4) == 0.5
    assert calculator.divide(10, 100) == 0.1
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
