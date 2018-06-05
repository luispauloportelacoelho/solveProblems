from unittest import TestCase, main
from forming_magic_square import forming_magic_square


class Test(TestCase):
    def test_square1(self):
        self.assertEqual(forming_magic_square([[4, 9, 2],
                                               [3, 5, 7], [8, 1, 5]]), 1)

    def test_square2(self):
        self.assertEqual(forming_magic_square([[4, 8, 2],
                                               [4, 5, 7], [6, 1, 6]]), 4)


if __name__ == '__main__':
    main()
