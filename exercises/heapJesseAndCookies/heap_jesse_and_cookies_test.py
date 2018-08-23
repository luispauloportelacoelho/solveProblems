from unittest import TestCase, main
from heap_jesse_and_cookies import cookies

class Test(TestCase):

    def test_sample_input(self):
        self.assertEqual(cookies(7, [1, 2, 3, 9, 10, 12]), 2)

    def test_sample_impossible_increase(self):
        self.assertEqual(cookies(100000, [1, 1, 1, 1, 1, 1, 1]), -1)

if __name__ == '__main__':
    main()
