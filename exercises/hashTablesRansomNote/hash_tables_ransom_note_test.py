from unittest import TestCase, main
from hash_tables_ransom_note import checkMagazine


class Test(TestCase):
    def magazine_yes(self):
        self.assertEqual(checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']), 'Yes')

    def magazine_no(self):
        self.assertEqual(checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four']), 'No')


if __name__ == '__main__':
    main()
