from unittest import TestCase
from unittest import main
from greedy_florist import getMinimumCost

class Test(TestCase):

    def test_0(self):
        self.assertEqual(getMinimumCost(3, [1, 3, 5, 7, 9]), 29)

    def test_1(self):
        self.assertEqual(getMinimumCost(2, [2, 5, 6]), 15)

    def test_3(self):
        self.assertEqual(getMinimumCost(3, [2, 5, 6]), 13)

if __name__ == '__main__':
    main()
