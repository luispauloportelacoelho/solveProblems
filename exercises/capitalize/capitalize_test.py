from unittest import TestCase, main
from capitalize import solve

class Test(TestCase):

    def test_one_words(self):
        self.assertEqual(solve('hello'), 'Hello')

    def test_two_words(self):
        self.assertEqual(solve('hello world'), 'Hello World')

    def test_three_words(self):
        self.assertEqual(solve('hello my     world'), 'Hello My     World')


if __name__ == '__main__':
    main()
