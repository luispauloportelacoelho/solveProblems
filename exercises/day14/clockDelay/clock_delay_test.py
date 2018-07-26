from unittest import TestCase, main
from clock_delay import clock_delay

class Test(TestCase):
    def test_first(self):
        self.assertEqual(clock_delay(12, 0, 12, 58, 1), 2, msg=None)

    def test_third(self):
        self.assertEqual(clock_delay(11, 40, 15, 33, 6), 127, msg=None)

    def test_four(self):
        self.assertEqual(clock_delay(18, 13, 19, 25, 5), 228)

    def test_five(self):
        self.assertEqual(clock_delay(14, 27, 21, 1, 9), 146)

    def test_six(self):
        self.assertEqual(clock_delay(16, 40, 23, 40, 7), 0)


if __name__ == '__main__':
    main()
