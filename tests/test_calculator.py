# tests/test_calculator.py

import unittest
from src.calculator import advanced_calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(advanced_calculate(5, 3, "add"), 8)

    def test_divide(self):
        self.assertEqual(advanced_calculate(10, 2, "divide"), 5)

    def test_divide_by_zero(self):
        self.assertEqual(advanced_calculate(10, 0, "divide"), "Error: Division by zero")