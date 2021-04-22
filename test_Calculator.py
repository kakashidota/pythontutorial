from Calculator import Calc
import pytest

class TestCalc:
    def test_add(self):
        assert 4 == Calc.add(4, 0)

    def test_sub(self):
        assert 10 == Calc.sub(20, 10)

    def test_multi(self):
        assert 100 == Calc.multi(10, 10)

    def test_div(self):
        assert 10 == Calc.div(100, 10)