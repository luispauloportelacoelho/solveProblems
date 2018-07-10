from unittest import TestCase, main
from leap_year import is_leap

class Test(TestCase):
    def test_leap_year_1990(self):
        self.assertEqual(is_leap(1990), False)

    def test_leap_year_2100(self):
        self.assertEqual(is_leap(2100), False)

    def test_leap_year_1992(self):
        self.assertEqual(is_leap(1992), True)    


if __name__ == '__main__':
    main()
