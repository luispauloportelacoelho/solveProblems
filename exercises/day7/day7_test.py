from unittest import TestCase, main
from day7 import array_reverse


class Test(TestCase):
    def test_array_manipulation_1(self):
        self.assertEqual(array_reverse([1, 4, 3, 2]), "2 3 4 1")


if __name__ == '__main__':
    main()
