from unittest import TestCase, main
from fraudulent_activity_notifications import activityNotifications


class Test(TestCase):
    def test_fraudulent_activity_notifications_odd(self):
        self.assertEqual(activityNotifications([10, 20, 30, 40, 50], 3), 1)

    def test_fraudulent_activity_notifications_odd_1(self):
        self.assertEqual(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2)

    def test_fraudulent_activity_notifications_even(self):
        self.assertEqual(activityNotifications([1, 2, 3, 4, 4], 4), 0)

if __name__ == '__main__':
     main()
