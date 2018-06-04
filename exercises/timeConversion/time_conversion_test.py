from unittest import TestCase, main
from time_conversion import time_conversion


class Test(TestCase):
    def test_time_conversion(self):
        self.assertEqual(time_conversion("07:05:45PM"), "19:05:45")


if __name__ == '__main__':
    main()
