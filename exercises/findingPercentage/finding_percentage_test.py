from unittest import TestCase, main
from finding_percentage import calculate_note

class Test(TestCase):
    def test_calculate_average_note(self):
        self.assertEqual(calculate_note("Malika", {"Malika": [52, 56, 60]}), 56.00)


if __name__ == '__main__':
    main()
