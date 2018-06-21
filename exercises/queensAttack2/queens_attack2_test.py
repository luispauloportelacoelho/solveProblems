from unittest import TestCase, main
from queens_attack2 import queensAttack

class Test(TestCase):
    def test_queens_attack2_0(self):
        self.assertEqual(queensAttack(4, 0, 4, 4, []),
                         9)

    def test_queens_attack2_1(self):
        self.assertEqual(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]),
                         10)

if __name__ == '__main__':
    main()
