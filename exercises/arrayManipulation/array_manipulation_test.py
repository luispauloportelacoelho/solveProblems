from unittest import TestCase, main
from array_manipulation import arrayManipulation


class Test(TestCase):
    def test_array_manipulation_1(self):
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        self.assertEqual(arrayManipulation(5, queries), 200, msg=None)

if __name__ == '__main__':
    main()
