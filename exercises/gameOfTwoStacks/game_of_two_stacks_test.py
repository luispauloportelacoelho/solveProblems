from unittest import TestCase, main
from game_of_two_stacks import twoStacks

class Test(TestCase):

    def test_0(self):
        self.assertEqual(twoStacks(12, [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]), 32)

    def test_1(self):
        self.assertEqual(twoStacks(40, [5, 15, 30], [5, 5, 20, 5]), 5)

if __name__ == '__main__':
    main()
