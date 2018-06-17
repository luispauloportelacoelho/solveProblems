def climbingLeaderboard(scores, alice):

    allPositions, numberScores = classify_scores(scores)

    playerPosition = []

    numberGames = len(alice)

    for x in range(0, numberGames):
        for y in range (0, numberScores):
            if alice[x] == scores[y]:
                playerPosition.append(allPositions[y])
                break
            elif alice[x] > scores[y]:
                if y == 0:
                    playerPosition.append(1)
                    break
                else:
                    playerPosition.append(allPositions[y])
                    break
            elif y == numberScores - 1:
                playerPosition.append(numberScores-1)



    return playerPosition


def classify_scores(scores):
    numberScores = len(scores)

    position = [1]

    for x in range(1, numberScores):
        if scores[x-1] == scores[x]:
            position.append(position[x-1])
        else:
            position.append(position[x-1] + 1)

    return position, numberScores


print(classify_scores([100, 100, 50, 40, 40, 30]))
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],
                                     [5, 25, 50, 120]))
