import unittest
from primeFinder import PrimeChecker


class TestPrime(unittest.TestCase):
    def setUp(self):
        self.prime = PrimeChecker()

    def test1(self):
        self.assertEqual(self.prime.Checker(99990001), 1)

    def test2(self):
        self.assertEqual(self.prime.Checker(21), 0)


if __name__ == '__main__':
    unittest.main()
