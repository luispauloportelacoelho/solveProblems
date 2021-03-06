from unittest import TestCase, main
from time_conversion import time_conversion


class Test(TestCase):
    def test_time_conversion(self):
        self.assertEqual(time_conversion("07:05:45PM"), "19:05:45")

    def test_time_conversion2(self):
        self.assertEqual(time_conversion("12:40:22AM"), "00:40:22")

    def test_time_conversion3(self):
        self.assertEqual(time_conversion("12:45:54PM"), "12:45:54")

if __name__ == '__main__':
    main()
