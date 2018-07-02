from unittest import TestCase, main
from operators_day2 import solve

class Test(TestCase):
    def test_total_cost(self):
        self.assertEqual(solve(12.00, 20, 8), "The total meal cost is 15 dollars.", msg=None)

if __name__ == '__main__':
    main()
