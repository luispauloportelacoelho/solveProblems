from unittest import TestCase, main
from taum_bday import taumBday

class Test(TestCase):

    def test_1(self):
        self.assertEquals(taumBday(10, 10, 1, 1, 1), 20)

    def test_2(self):
        self.assertEquals(taumBday(5, 9, 2, 3, 4), 37)

    def test_3(self):
        self.assertEquals(taumBday(3, 6, 9, 1, 1), 12)

    def test_4(self):
        self.assertEquals(taumBday(7, 7, 4, 2, 1), 35)

    def test_5(self):
        self.assertEquals(taumBday(3, 3, 1, 9, 2), 12)

    def test_6(self):
        self.assertEquals(taumBday(384, 887, 2778, 6916, 7794), 7201244)


if __name__ == '__main__':
    main()
