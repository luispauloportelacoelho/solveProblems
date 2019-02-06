from unittest import TestCase, main
from largest_rectangle import largestRectangle

class Test(TestCase):

    def test_0(self):
        self.assertEqual(largestRectangle([1, 2, 3, 4, 5]), 9)


if __name__ == '__main__':
    main()
