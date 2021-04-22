from Calculator import Calc
import pytest

class TestCalc:
    def test_add(self):
        assert 4 == Calc.add(4, 0)

    def test_sub(self):
        assert 10 == Calc.sub(20, 10)