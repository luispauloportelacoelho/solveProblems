from unittest import TestCase, main
from find_angle_MBC import find_angle


class Test(TestCase):
    def test_find_angle_1(self):
        self.assertEqual(find_angle(10, 10), "45°")

    def test_find_angle_2(self):
        self.assertEqual(find_angle(100, 1), "89°")

    def test_find_angle_3(self):
        self.assertEqual(find_angle(1, 10), "6°")


if __name__ == '__main__':
    main()
