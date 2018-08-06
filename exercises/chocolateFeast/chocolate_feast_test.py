from unittest import TestCase, main
from chocolate_feast import chocolateFeast

class Test(TestCase):

    def test_chocolate_1(self):
        self.assertEqual(chocolateFeast(10, 2, 5), 6)

    def test_chocolate_2(self):
        self.assertEqual(chocolateFeast(12, 4, 4), 3)

    def test_chocolate_3(self):
        self.assertEqual(chocolateFeast(6, 2, 2), 5)    


if __name__ == '__main__':
    main()
