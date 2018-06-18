def climbingLeaderboard(scores, alice):
    """Climbing the leadboard."""

    leaderboard = sorted(set(scores), reverse = True)
    sizeLeaderboard = len(leaderboard)

    result = []

    for a in alice:
        while (sizeLeaderboard > 0) and (a >= leaderboard[sizeLeaderboard-1]):
            sizeLeaderboard -= 1
        result.append(sizeLeaderboard+1)

    return result  
