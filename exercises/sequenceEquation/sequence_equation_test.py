from unittest import TestCase, main
from sequence_equation import permutationEquation

class Test(TestCase):

    def test_0(self):
        self.assertEqual(permutationEquation([2, 3, 1]), [2, 3, 1])

    def test_1(self):
        self.assertEqual(permutationEquation([5, 2, 1, 3, 4]), [4, 2, 5, 1, 3])

    def test_2(self):
        self.assertEqual(permutationEquation([1, 4, 2, 3, 5]), [1, 4, 2, 3, 5])


if __name__ == '__main__':
    main()
