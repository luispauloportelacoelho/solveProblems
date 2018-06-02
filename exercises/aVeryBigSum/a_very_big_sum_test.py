from unittest import TestCase, main
from a_very_big_sum import aVeryBigSum


class Test(TestCase):
    def test_array_sum(self):
        self.assertEqual(aVeryBigSum([5, 2, 3, 5]), 15)

if __name__ == '__main__':
    main()
