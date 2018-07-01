from unittest import TestCase, main
from array_left_rotation import array_left_rotation


class Test(TestCase):
    def test_array_left_rotation1(self):
        self.assertEqual(array_left_rotation([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])


if __name__ == '__main__':
    main()
