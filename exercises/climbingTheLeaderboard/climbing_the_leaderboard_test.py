from unittest import TestCase, main
from climbing_the_leaderboard import climbingLeaderboard
from climbing_the_leaderboard import classify_scores

class Test(TestCase):
    def test_climbing_leader_board(self):
        self.assertEqual(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],
                                             [5, 25, 50, 120]), [6, 4, 2, 1])

    def test_classify_scores(self):
        self.assertEqual(classify_scores([100, 100, 50, 40, 40, 30]),
                         ([1, 1, 2, 3, 3, 4], 6))


if __name__ == '__main__':
    main()
