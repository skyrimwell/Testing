import unittest
from primeFinder import PrimeChecker


class TestPrime(unittest.TestCase):
    def setUp(self):
        self.prime = PrimeChecker()

    def test1(self):
        self.assertEqual(self.prime.Checker(99990001), 1)

    def test2(self):
        self.assertEqual(self.prime.Checker(21), 0)

    def test3(self):
        self.assertEqual(self.prime.Checker(-5), -1)

    def test4(self):
        self.assertEqual(self.prime.Checker(11), 1)

    def test5(self):
        self.assertEqual(self.prime.Checker(0), -1)


if __name__ == '__main__':
    unittest.main()
