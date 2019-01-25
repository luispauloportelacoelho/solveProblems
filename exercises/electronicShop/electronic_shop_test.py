from unittest import TestCase, main
from electronic_shop import getMoneySpent

class Test(TestCase):

    def test_she_doesnot_have_money(self):
        self.assertEqual(getMoneySpent([4, 6], [4, 6], 1), -1)

    def test_0(self):
        self.assertEqual(getMoneySpent([5, 1, 8], [3, 1], 10), 9)

if __name__ == '__main__':
    main()
