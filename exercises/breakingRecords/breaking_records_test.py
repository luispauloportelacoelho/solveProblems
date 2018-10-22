from unittest import TestCase, main
from breaking_records import breakingRecords

class Test(TestCase):

    def test_0(self):
        self.assertEqual(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])


if __name__ == '__main__':
    main()
