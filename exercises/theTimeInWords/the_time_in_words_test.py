from unittest import TestCase, main
from the_time_in_words import timeInWords

class Test(TestCase):
    def test_o_clock(self):
        self.assertEqual(timeInWords(5, 0), "five o' clock", msg=None)

    def test_one_minute(self):
        self.assertEqual(timeInWords(5, 1), "one minute past five", msg=None)

    def test_ten_minutes(self):
        self.assertEqual(timeInWords(5, 10), "ten minutes past five", msg=None)

    def test_quarter_past(self):
        self.assertEqual(timeInWords(5, 15), "quarter past five", msg=None)

    def test_half(self):
        self.assertEqual(timeInWords(5, 30), "half past five", msg=None)

    def test_twenty_to(self):
        self.assertEqual(timeInWords(5, 40), "twenty minutes to six", msg=None)

    def test_quarter_to(self):
        self.assertEqual(timeInWords(5, 45), "quarter to six", msg=None)

    def test_thirteen_to(self):
        self.assertEqual(timeInWords(5, 47), "thirteen minutes to six")

    def test_twenty_eight_past(self):
        self.assertEqual(timeInWords(5, 28), "twenty eight minutes past five", msg=None)             

if __name__ == '__main__':
    main()
