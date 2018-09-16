from unittest import TestCase, main
from down_to_zero_II import downToZero

class Test(TestCase):

    def test_n_3(self):
        self.assertEqual(downToZero(3), 3)

    def test_n_4(self):
        self.assertEqual(downToZero(4), 3)

    def test_n_966514(self):
        self.assertEqual(downToZero(966514), 8)

if __name__ == '__main__':
    main()
