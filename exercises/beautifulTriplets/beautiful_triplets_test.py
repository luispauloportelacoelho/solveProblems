from unittest import TestCase, main
from beautiful_triplets import beautifulTriplets

class Test(TestCase):

    def test_0(self):
        self.assertEqual(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]), 3)

    def test_1(self):
        self.assertEqual(beautifulTriplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]), 2)

if __name__ == '__main__':
    main()
