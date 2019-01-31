from unittest import TestCase, main
from save_prisoner import saveThePrisoner


class Test(TestCase):

    def test_0(self):
        self.assertEqual(saveThePrisoner(5, 2, 1), 2, msg=None)

    def test_1(self):
        self.assertEqual(saveThePrisoner(5, 5, 1), 5, msg=None)

    def test_2(self):
        self.assertEqual(saveThePrisoner(5, 6, 1), 1, msg=None)

    def test_3(self):
        self.assertEqual(saveThePrisoner(5, 10, 1), 5, msg=None)

    def test_4(self):
        self.assertEqual(saveThePrisoner(5, 11, 1), 1, msg=None)

    def test_5(self):
        self.assertEqual(saveThePrisoner(7, 19, 2), 6, msg=None)

    def test_6(self):
        self.assertEqual(saveThePrisoner(3, 7, 3), 3, msg=None)

if __name__ == '__main__':
    main()
