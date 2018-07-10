from unittest import TestCase, main
from renatose import solution


class Test(TestCase):

    def test_renatose1(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_renatose2(self):
        self.assertEqual(solution([1, 2, 3]), 4)

    def test_renatose3(self):
        self.assertEqual(solution([-1, -3]), 1)


if __name__ == '__main__':
    main()
