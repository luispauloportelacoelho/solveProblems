from unittest import TestCase, main
from equal_stacks import equalStacks

class Test(TestCase):
    def test_equal_stack_1(self):
        self.assertEqual(equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]),
                                    5)


if __name__ == '__main__':
    main()    
