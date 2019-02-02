"""
Unit tests for caculator
"""


import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.sub(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(2,50)
