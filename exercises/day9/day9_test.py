from unittest import TestCase, main
from day9 import factorial

class Test(TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(5), 120)



if __name__ == '__main__':
    main()
