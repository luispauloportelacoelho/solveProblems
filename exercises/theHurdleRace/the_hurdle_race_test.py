from unittest import TestCase, main
from the_hurdle_race import hurdleRace

class Test(TestCase):
    def test_hurdle_Race(self):
        self.assertEqual(hurdleRace(4, [1, 6, 3, 5, 2]), 2)


if __name__ == '__main__':
    main()
