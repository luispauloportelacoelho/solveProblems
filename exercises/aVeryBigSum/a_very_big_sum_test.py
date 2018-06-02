from unittest import TestCase, main
from a_very_big_sum import aVeryBigSum


class Test(TestCase):
    """Class to test the function a_very_big_sum."""

    def test_array_sum(self):
        """Test the array sum."""
        self.assertEqual(aVeryBigSum([5, 2, 3, 5]), 15)


if __name__ == '__main__':
    main()
