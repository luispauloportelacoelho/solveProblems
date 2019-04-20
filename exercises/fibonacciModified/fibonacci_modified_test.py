from unittest import TestCase, main
from fibonacci_modified import fibonacciModified

class Test(TestCase):

    def test_fib_modified_0_1_1(self):
        self.assertEquals(fibonacciModified(0, 1, 1), 0)

    def test_fib_modified_0_1_5(self):
        self.assertEquals(fibonacciModified(0, 1, 5), 5)


if __name__ == '__main__':
    main()
