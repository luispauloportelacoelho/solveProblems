from unittest import TestCase, main
from day10 import countOne


class Test(TestCase):
    def test_count_one_5(self):
        self.assertEqual(countOne(5), 1)

    def test_count_one_13(self):
        self.assertEqual(countOne(13), 2)

    def test_count_one_439(self):
        self.assertEqual(countOne(439), 3)


if __name__ == '__main__':
    main()
