def climbingLeaderboard(scores, alice):

    allPositions, numberScores = classify_scores(scores)

    playerPosition = []

    numberGames = len(alice)

    countIteration = 0

    for x in xrange(0, numberGames):
        for y in xrange (0, numberScores):
            countIteration += 1
            print(countIteration)
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
                break


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
