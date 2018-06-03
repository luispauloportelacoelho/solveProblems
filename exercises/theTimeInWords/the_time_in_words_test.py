from unittest import TestCase, main
from the_time_in_words import timeInWords


class Test(TestCase):
    """Class to test the function: the_time_in_words."""

    def test_o_clock(self):
        """Test zero minutes."""
        self.assertEqual(timeInWords(5, 0), "five o' clock", msg=None)

    def test_one_minute(self):
        """Test one minute."""
        self.assertEqual(timeInWords(5, 1), "one minute past five", msg=None)

    def test_ten_minutes(self):
        """Test ten minutes past."""
        self.assertEqual(timeInWords(5, 10), "ten minutes past five", msg=None)

    def test_quarter_past(self):
        """Test quarter past."""
        self.assertEqual(timeInWords(5, 15), "quarter past five", msg=None)

    def test_half(self):
        """Test half past."""
        self.assertEqual(timeInWords(5, 30), "half past five", msg=None)

    def test_twenty_to(self):
        """Test twenty to."""
        self.assertEqual(timeInWords(5, 40), "twenty minutes to six", msg=None)

    def test_quarter_to(self):
        """Test quarter to."""
        self.assertEqual(timeInWords(5, 45), "quarter to six", msg=None)

    def test_thirteen_to(self):
        """Test thirteen to."""
        self.assertEqual(timeInWords(5, 47), "thirteen minutes to six")

    def test_twenty_eight_past(self):
        """Test twenty eight past."""
        self.assertEqual(timeInWords(5, 28),
                         "twenty eight minutes past five")


if __name__ == '__main__':
    main()
