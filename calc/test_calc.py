
import unittest
from calc import Calculator

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(15,15), 30)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(45,5), 225)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(100,2), 50)


if __name__ == "__main__":
    unittest.main()