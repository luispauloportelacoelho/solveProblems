from unittest import TestCase, main
from heap_find_running_median import runningMedian


class Test(TestCase):
    def test_1(self):
        self.assertEqual(runningMedian([12]), 12)

    def test_2(self):
        self.assertEqual(runningMedian([12, 4]), 8)

    def test_3(self):
        self.assertEqual(runningMedian([12, 4, 5]), 5)

    def test_4(self):
        self.assertEqual(runningMedian([12, 4, 5, 3]), 4.5)

    def test_5(self):
        self.assertEqual(runningMedian([12, 4, 5, 3, 8]), 5)

    def test_6(self):
        self.assertEqual(runningMedian([12, 4, 5, 3, 8, 7]), 6)

if __name__ == '__main__':
    main()
