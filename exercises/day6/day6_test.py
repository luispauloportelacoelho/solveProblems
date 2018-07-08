from unittest import TestCase, main
from day6 import separate


class Test(TestCase):
    def test_separate_1(self):
        self.assertEqual(separate("Hacker"), "Hce akr")

    def test_separate_2(self):
        self.assertEqual(separate("Rank"), "Rn ak")    

if __name__ == '__main__':
    main()
