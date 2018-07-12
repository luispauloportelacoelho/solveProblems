from unittest import TestCase, main
from day11 import max_hourglass

class Test(TestCase):
    def test_max_hourglass_1(self):
        self.assertEqual(max_hourglass([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
                                        [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
                                        [0, 0, 0, 2, 0, 0],
                                        [0, 0, 1, 2, 4, 0]]), 19)

    def test_max_hourglass_7(self):
        self.assertEqual(max_hourglass([[0, -4, -6, 0, -7, -6],
                                        [-1, -2, -6, -8, -3, -1],
                                        [-8, -4, -2, -8, -8, -6],
                                        [-3, -1, -2, -5, -7, -4],
                                        [-3, -5, -3, -6, -6, -6],
                                        [-3, -6, 0, -8, -6, -7]]), -19)


if __name__ == '__main__':
    main()
