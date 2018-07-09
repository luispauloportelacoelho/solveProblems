from unittest import TestCase, main
from beautiful_days_movies import beautifulDays

class Test(TestCase):
    def test_beautiful_days(self):
        self.assertEqual(beautifulDays(20, 23, 6), 2)


if __name__ == '__main__':
    main()
