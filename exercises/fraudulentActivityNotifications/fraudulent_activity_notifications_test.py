from unittest import TestCase, main
from fraudulent_activity_notifications import activityNotifications
from fraudulent_activity_notifications import calculateMedian                                              calculateMedian


class Test(TestCase):
    def test_input0(self):
        self.assertEqual(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5),
                         2)

    def test_input1(self):
        self.assertEqual(activityNotifications([1, 2, 3, 4, 4], 4), 0)

    def test_input2(self):
        self.assertEqual(activityNotifications([10, 20, 30, 40, 50], 3), 1)

    def test_median_odd(self):
        self.assertEqual(calculateMedian([10, 20, 30], False, 1), 20)

    def test_median_even(self):
        self.assertEqual(calculateMedian([1, 2, 3, 4, 5, 6, 8, 9], True, 4), 4.5)


if __name__ == '__main__':
     main()
