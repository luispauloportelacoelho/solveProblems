from unittest import TestCase, main
from day8 import search_contact


class Test(TestCase):
    def test_maps(self):
        self.assertEqual(search_contact("sam", {'sam': '99912222'}), "sam=99912222")


if __name__ == '__main__':
    main()
