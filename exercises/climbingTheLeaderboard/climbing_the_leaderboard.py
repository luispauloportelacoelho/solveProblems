def climbingLeaderboard(scores, alice):
    """Climbing the leadboard."""
    allPositions, numberScores = classify_scores(scores)

    playerPosition = []

    numberGames = len(alice)

    for x in range(numberGames):

        if alice[x] in scores:
            value_index = scores.index(alice[x])
            playerPosition.append(allPositions[value_index])
        else:
            if alice[x] < scores[-1]:
                playerPosition.append(allPositions[-1] + 1)
            elif alice[x] > scores[0]:
                playerPosition.append(1)
            else:
                vector = [i for i in scores if i > alice[x]]
                sizeVector = len(vector)
                playerPosition.append(allPositions[sizeVector])

    return playerPosition


def classify_scores(scores):
    """Give a classification for all scores."""

    numberScores = len(scores)

    position = [1]

    for x in range(1, numberScores):
        if scores[x-1] == scores[x]:
            position.append(position[x-1])
        else:
            position.append(position[x-1] + 1)

    return position, numberScores
