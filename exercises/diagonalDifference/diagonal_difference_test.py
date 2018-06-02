from unittest import TestCase, main
from diagonal_difference import diagonalDifference, calculateSize


class Test(TestCase):
    def test_diagonal_difference(self):
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)

    def test_calculate_size(self):
        self.assertEqual(calculateSize([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 3)


if __name__ == '__main__':
    main()
