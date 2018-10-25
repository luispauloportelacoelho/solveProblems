from unittest import TestCase, main
from day_programmer import dayProgrammer

class Test(TestCase):

    def test_2017(self):
        self.assertEqual(dayProgrammer(2017), "13.09.2017")

    def test_2016(self):
        self.assertEqual(dayProgrammer(2016), "12.09.2016")

    def test_1800(self):
        self.assertEqual(dayProgrammer(1800), "12.09.1800")

    def test_1917(self):
        self.assertEqual(dayProgrammer(1917), "13.09.1917")

    def test_1918(self):
        self.assertEqual(dayProgrammer(1918), '26.09.1918')

if __name__ == '__main__':
    main()
