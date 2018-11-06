from unittest import TestCase, main
from closest_numbers import closestNumbers

class Test(TestCase):

    def test_0(self):
        self.assertEqual(closestNumbers([3, 4, 50, 1, 2]), [1, 2, 2, 3, 3, 4])

    def test_1(self):
        self.assertEqual(closestNumbers([5, 4, 3, 2]), [2, 3, 3, 4, 4, 5])


if __name__ == '__main__':
    main()
