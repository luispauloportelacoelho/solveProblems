def climbingLeaderboard(scores, alice):

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

                '''for y in range(numberScores):

                    if alice[x] > scores[y]:
                        playerPosition.append(allPositions[y])
                        break'''

    #print([i for i in scores if i >= 60])

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
