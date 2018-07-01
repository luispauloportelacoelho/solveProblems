from unittest import TestCase, main
from fibonacci_recursion import fib_recusion

class Test(TestCase):
    def test_fib0(self):
        self.assertEqual(fib_recusion(0), 0)

    def test_fib1(self):
        self.assertEqual(fib_recusion(1), 1)

    def test_fib2(self):
        self.assertEqual(fib_recusion(2), 1)

    def test_fib6(self):
        self.assertEqual(fib_recusion(6), 8)

if __name__ == '__main__':
    main()
