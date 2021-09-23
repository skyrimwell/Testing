import unittest
from sort import InsertionSort

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.insSort = InsertionSort()

    def test_sort1(self):
        self.assertEqual(self.insSort.sort([3, 2, 1]), [1, 2, 3])

    def test_sort2(self):
        self.assertEqual(self.insSort.sort([-11, 10, 0, -99]), [-99, -11, 0, 10])

    def test_sort3(self):
        self.assertEqual(self.insSort.sort([1, 1, 1]), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()