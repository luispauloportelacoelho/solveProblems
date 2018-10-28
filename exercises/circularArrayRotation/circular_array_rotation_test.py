from unittest import TestCase, main
from circular_array_rotation import circularArrayRotation

class Test(TestCase):

    def test_0(self):
        self.assertEqual(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]), [2, 3, 1])

    def test_1(self):
        self.assertEqual(circularArrayRotation([1, 2, 3], 2, [0, 1]), [2, 3])

    def test_2(self):
        self.assertEqual(circularArrayRotation([1, 2, 3], 2, [0, 2]), [2, 1])

    def test_3(self):
        self.assertEqual(circularArrayRotation([5, 4, 2, 10], 2, [0, 2]), [2, 5])

    def test_4(self):
        self.assertEqual(circularArrayRotation([3, 4, 1], 3, [0, 1, 2]), [3, 4, 1])

    def test_5(self):
        self.assertEqual(circularArrayRotation([3, 4, 1], 4, [0, 1, 2]), [1, 3, 4])

    def test_6(self):
        self.assertEqual(circularArrayRotation([3, 4, 1], 3, [2, 0, 1]), [1, 3, 4])

    def test_7(self):
        self.assertEqual(circularArrayRotation([1, 2, 3, 4], 4, [2, 0, 1, 3]), [3, 1, 2, 4])

    def test_8(self):
        self.assertEqual(circularArrayRotation([1, 2, 3, 4], 4, [1, 3]), [2, 4])

    def test_9(self):
        self.assertEqual(circularArrayRotation([1, 2, 3, 4], 1, [1, 3, 1, 3, 0]), [1, 3, 1, 3, 4])


if __name__ == '__main__':
    main()
