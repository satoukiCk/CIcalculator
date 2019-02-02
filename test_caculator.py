"""
Unit tests for caculator
"""


import caculator

class TestCalculator:

    def test_addition(self):
        assert 4 == caculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == caculator.sub(4, 2)
