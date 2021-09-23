import unittest
from quadraticEquations import QuadraticEquations

class TestQuadraticEquations(unittest.TestCase):
    def setUp(self):
        self.qe = QuadraticEquations()

    def test_solve1(self):
        self.assertEqual(self.qe.solve(2, 5, -3), [0.5, -3.0, 1])

    def test_solve2(self):
        self.assertEqual(self.qe.solve(0, 5, -3), [-1, -1, -1])

    def test_solve3(self):
        self.assertEqual(self.qe.solve(5, 4, 3), ['-0.4+i 6.6332495807108', '-0.4-i 6.6332495807108', -1])


if __name__ == "__main__":
    unittest.main()