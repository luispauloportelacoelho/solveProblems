from unittest import TestCase, main
from set_introduction import average

class Test(TestCase):

    def test_average(self):
        self.assertEqual(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]), 169.375)


if __name__ == '__main__':
    main()
