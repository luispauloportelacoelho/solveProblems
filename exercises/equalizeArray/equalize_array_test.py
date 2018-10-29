from unittest import TestCase, main
from equalize_array import equalizeArray


class Test(TestCase):

    def test_1(self):
        self.assertEqual(equalizeArray([3, 3, 1, 2, 3]), 2)


if __name__ == '__main__':
    main()
