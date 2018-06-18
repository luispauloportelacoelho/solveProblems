from unittest import TestCase, main
from climbing_the_leaderboard import climbingLeaderboard


class Test(TestCase):
    """Test for climbingLeaderboard problem."""
    def test_climbing_leader_board(self):
        """Test the climbing_leader_board with the given example."""
        self.assertEqual(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],
                                             [5, 25, 50, 120]), [6, 4, 2, 1])


if __name__ == '__main__':
    main()
